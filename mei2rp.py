import os
import sys
import csv
import json
import wave

sys.tracebacklimit = 1

#Variables for the Mappings
OUTFIT_MAPS = 'mappings/outfits/'
JP2ID = {}
ID2NAME = {}
OUTFITS = {}
BACKGROUND = {}
BGM = {}
SFX = {}
SHAKEMAP = {}

# Variables for cover backgrounds
COLORS = {
    '黒': "black_cover",
    '白': "white_cover",
    '赤': "red_cover", # TODO tune the red
}

# Open all the mapping files/import the mappings
with open('mappings/charnames.csv', 'r', encoding='utf8') as cnames:
    reader = csv.reader(cnames)
    for line in reader:
        if len(line) < 3: continue
        JP2ID[line[0]] = line[1]
        ID2NAME[line[1]] = line[2]

with open('mappings/bg.csv', 'r', encoding='utf8') as cnames:
    reader = csv.reader(cnames)
    for line in reader:
        if len(line) < 2: continue
        BACKGROUND[line[0]] = line[1]

with open('mappings/bgm.csv', 'r', encoding='utf8') as cnames:
    reader = csv.reader(cnames)
    for line in reader:
        if len(line) < 2: continue
        loop = 0 if len(line) < 3 else line[2]
        BGM[line[0]] = line[1], loop

with open('mappings/se.csv', 'r', encoding='utf8') as cnames:
    reader = csv.reader(cnames)
    for line in reader:
        if len(line) < 2: continue
        SFX[line[0]] = line[1]

with open('mappings/shakes.csv', 'r', encoding='utf8') as cnames:
    reader = csv.reader(cnames)
    for line in reader:
        if len(line) < 2: continue
        SHAKEMAP[line[0]] = line[1]

for outfit in os.listdir(OUTFIT_MAPS):
    name = outfit.split('.')[0]
    OUTFITS[name] = {}

    with open(OUTFIT_MAPS + outfit, 'r', encoding='utf8') as cnames:
        reader = csv.reader(cnames)
        for line in reader:
            if len(line) < 2: continue
            OUTFITS[name][line[0]] = line[1]

# Simple Getter functions
def get_outfit(jp):
    if jp == '：': return None
    jp = jp.split('：')
    if len(jp) == 1:
        return f'{JP2ID[jp[0]]}_v001'

    cid, oid = jp
    cid = JP2ID[cid]
    if cid in OUTFITS and oid in OUTFITS[cid]:
        # NOTE: May want to not have 'v'
        oid = 'v' + OUTFITS[cid][oid]
    elif oid == '私服':
        oid = 'v002'
    else:
        raise KeyError(f'Outfit {oid} not found')

    return f'{cid}_{oid}'

def get_name(jp, local=None):
    if jp == '：': return None
    jp = jp.split('：')[0]
    if local is not None and jp in local:
        jp = strip_furigana(local[jp])

    cid = JP2ID[jp]
    return ID2NAME[cid]

def get_cmd(command):
    if 'cmd1' in command: return 1, command['cmd1']
    else: return 0, command['cmd0']

def get_pos(p):
    if p == '左': return 'mei_left'
    elif p == '右': return 'mei_right'
    elif p == '中': return 'mei_center'
    elif p == '左外': return 'mei_outerleft'
    elif p == '右外': return 'mei_outerright'
    else: return None

def get_ypos(p):
    if p == '下外': return -1080
    else: return int(p)

def get_id(jp, local=None):
    if local is not None and jp in local:
        jp = strip_furigana(local[jp])
        
    if jp == '：': return None
    jp = jp.split('：')
    if jp[0] not in JP2ID: return None
    return JP2ID[jp[0]]

    
# Helper Functions
def strip_furigana(t):
    return t.split('#s')[0].lstrip('#p')

def indent(text, n):
    return '\n'.join(map(lambda line: n*' ' + line, text.split('\n')))

# Functions to Show a character
class ShowChara:
    def __init__(self, order, outfit, expression="normal"):
        self.outfit = outfit
        self.expression = expression
        self.transforms = []
        self.move_transform = ""
        self.transition = 0
        self.atl = None
        self.move_end = None
        self.wait = 0
        self.order = order

    def construct(self):
        s = ""
        if not self.transforms:
            s =  f'show {self.outfit} {self.expression}'
        else:
            for trans in self.transforms[:-1]:
                    s += f'show {self.outfit} {self.expression} at {trans}\n'
            s += f'show {self.outfit} {self.expression} at {self.transforms[-1]}'

        if self.atl:
            if self.move_transform == "":
                s += f'\nshow {self.outfit} {self.expression}:\n{indent(self.atl,1)}'
            else:
                s += f'\nshow {self.outfit} {self.expression} at {self.move_transform}:\n{indent(self.atl, 1)}'  
                
            if self.move_end:
                self.move_end = f'show {self.outfit} {self.expression}:\n{indent(self.move_end,1)}'                
        return s

class CameraTransform:
    def __init__(self):
        self.time = 0

# Main Compiler
class Compiler:
    def __init__(self, commands, translation, forcelines={}):
        self.bgm = self.bgm2
        self.commands = commands
        self.translation = translation
        self.forcelines = forcelines
        self.outlines = []
        self.local = {}
        self.shown = {}
        self.to_show = {}
        # TODO: tune 右 and 左 variables
        self.variables = {
            '中': 960,
            '左': 480,
            '右': 1920-480,
            '右外': 1920+480,
            '左外': -480,
        }
        self.background = None
        self.cam_extras = ""
        self.save_shake = ""

    def talk(self, n, line, cmd):
        name = ''
        nameid = get_id(cmd, self.local)
        cid = get_id(cmd)
        if cmd in self.local:
            name = get_name(self.local[cmd])
            speaker = f'Character({repr(name)},ctc="ctcArrow", ctc_position="fixed")'
        else:
            if cid is not None: 
                speaker = f'Character({repr(ID2NAME[cid])},ctc="ctcArrow", ctc_position="fixed")'
            else:
                speaker = None
    
        text = self.translation.get(n, line['arg1']).replace('%', '%%').replace('[', '[[')
        for c, o in self.to_show.items():
            if c == cid or (c in str(nameid) and '_' in str(nameid)):
                self.to_show[c].transforms.insert(0,'active')
            else:
                o.transforms.insert(0,'inactive')
               
        for c, o in self.shown.items():
            if c not in self.to_show:
                self.to_show[c] = ShowChara(len(self.to_show), o[0], o[1])
                if c == cid or (c in str(nameid) and '_' in str(nameid)):
                    self.to_show[c].transforms.insert(0,'active') 
                else:
                    self.to_show[c].transforms.insert(0,'inactive')
           
        if speaker is None:
            return f'narrator {repr(text)}'
        else:
            return f'{speaker} {repr(text)}'

    def setdispname(self, typ, line, cmd):
        self.local[line['arg0']] = line['arg1']

    def removedispname(self, typ, line, cmd):
        del self.local[line['arg0']]
            
    def serifclose(self, typ, line, cmd):
        self.outlines.append('window hide None')

    def chara(self, typ, line, cmd):
        outfit = get_outfit(line['arg0'])
        expr = line['arg1'].replace('目閉じ', 'close')
        pos = get_pos(line['arg2'])
       
        showchara = ShowChara(len(self.to_show), outfit, expr)
        if pos is not None:
            showchara.transforms.append(pos)
        else:
            # NOTE. be CAREFUL Untested. rare codepath
            xpos = self.variables[line['arg2']]
            ypos = 1200
            showchara.atl = f"yanchor 1.0\npos ({xpos}, 1200)"
            
        if typ == 0 and 'arg4' in line:
            time = int(line["arg4"]) / 60
            showchara.transition = time
        elif showchara not in self.shown:
            showchara.transition = 0.5
            
        

        self.to_show[get_id(line['arg0'])] = showchara

    def effect(self, typ, line, cmd):
        eff = line['arg0']
        if eff != 'flash': raise ValueError('Effect type is not flash')

        self.outlines.append('show white_cover as flash with Dissolve(0.1)')
        self.outlines.append('pause 0.1')
        self.outlines.append('hide flash with Dissolve(0.2)')

    def 変数(self, typ, line, cmd):
        dx = int(line.get('arg2', '0'))
        self.variables[line['arg0']] = self.variables[line['arg1']] + dx

    def crack(self, typ, line, cmd):
        print('If this is not umineko collab event 4, this will be borked')
        self.outlines.append('show crack_effect')

    def zoom(self, typ, line, cmd):
        mag = line['arg0']
        xpos = self.variables[line['arg1']]
        ypos = 540 + int(line['arg2'])
        time = int(line['arg3']) / 60
        if time == 0:
            self.outlines.append(f"""
camera:
 pos ({xpos}, {ypos})
 zoom {mag}
            """.strip())
        else:
            self.outlines.append(f"""
camera:
 parallel:
  linear {time} pos ({xpos}, {ypos})
 parallel:
  linear {time} zoom {mag}
            """.strip())
            if typ == 0: self.outlines.append(f'pause {time}')
    
    def shakechara(self, typ, line, cmd):
        oid = get_id(line['arg0'])
        anim = line['arg1']
        if oid not in self.shown:
            self.save_shake = SHAKEMAP[anim]
            return
        if oid not in self.to_show:
            o = self.shown[oid]
            self.to_show[oid] = ShowChara(len(self.to_show), o[0], o[1])
        self.to_show[oid].transforms.append(SHAKEMAP[anim])       
        if(SHAKEMAP[anim] not in {'active', 'inactive'}):
            self.save_shake = SHAKEMAP[anim]

    def shakedisp(self, typ, line, cmd):
        anim = SHAKEMAP[line['arg0']]
        self.outlines.append(f'camera at {anim}{self.cam_extras}\npause 0.0')
        
    def motion(self, typ, line, cmd):
        oid = get_id(line['arg0'])
        if oid not in self.shown: return
        if oid not in self.to_show:
            o = self.shown[oid]
            self.to_show[oid] = ShowChara(len(self.to_show), o[0], o[1])
       
        self.to_show[oid].expression = line['arg1']

    def hide(self, typ, line, cmd):
        cid = get_id(line['arg0'])
        outfit = get_outfit(line['arg0'])
        self.outlines.append(f'hide {outfit}')

        try: del self.shown[cid]
        except KeyError: pass

        try: del self.to_show[cid]
        except KeyError: pass

        if typ == 0 and 'arg1' in line:
            time = int(line["arg1"]) / 100
            self.outlines.append(f'with Dissolve({time})')

    def 背景(self, typ, line, cmd):
        bgname = line["arg0"]
        #self.shown.clear()
        if bgname == "暗幕" or bgname == "暗転":
            self.outlines.append(f'show black_cover as bg')
        elif bgname == "暗背景":
            self.outlines.append(f'show white_cover as bg')
        else:
            bgname = BACKGROUND[bgname]
            bgname = f"images/{bgname}.png"
            self.outlines.append('stop sound')
            self.outlines.append(f'show expression {repr(bgname)} as bg')

    def fadein(self, typ, line, cmd):
        time = int(line['arg0']) / 60
        self.outlines.append(f'hide fade onlayer curtain')
        
        for showchara in self.to_show.values():
            showchara.transition = 0
        self.output_shows()

        self.outlines.append(f'with Dissolve({time})')

    def fadeout(self, typ, line, cmd):
        color = COLORS[line['arg0']]
        time = int(line['arg1']) / 60
        self.outlines.append(f'show {color} onlayer curtain as fade with Dissolve({time})')

    def wipeout(self, typ, line, cmd):
        self.outlines.append('call wipeout_routine')

    def wipein(self, typ, line, cmd):
        if self.background: 
            self.outlines.append(self.background.replace('scene', 'show', 1))
            self.background = None
        
        self.output_shows()
        self.outlines.append('call wipein_routine')

    def bgm2(self, typ, line, cmd):
        name = BGM[line["arg0"]][0]
        name = f"audio/bgm/{name}.ogg"
        looptime = BGM[line["arg0"]][1]
        self.outlines.append(f'play music "<loop {looptime}>{name}"')

    def bgmstop(self, typ, line, cmd):
        if "arg0" in line:
            tim = int(line["arg0"])/60
            self.outlines.append(f'stop music fadeout {tim}')
        else:
            self.outlines.append(f'stop music')

    def move(self, typ, line, cmd):
        cid = get_id(line['arg0'])
        xpos = self.variables[line['arg1']]
        ypos = 1200 - get_ypos(line['arg2'])
        time = int(line['arg3'])/60
        if cid not in self.to_show and cid in self.shown:
            outfit, expression = self.shown[cid]
            self.to_show[cid] = ShowChara(len(self.to_show), outfit, expression)         
        if cid not in self.shown:
            self.to_show[cid].transition = 0.5    
            
        self.to_show[cid].move_transform = self.save_shake
        self.to_show[cid].atl = f'yanchor 1.0\nlinear {time} pos ({xpos},{ypos})'
        self.to_show[cid].move_end = f'yanchor 1.0\npos ({xpos},{ypos})'
        self.to_show[cid].wait = max(self.to_show[cid].wait, time)     

    def shader(self, typ, line, cmd):
        if line['arg0'] == 'セピア':
            self.outlines.append(f'camera at sepia_shader\npause 0.0')
            self.cam_extras = ",sepia_shader"
        else:
            self.outlines.append(f'camera at reset_shader\npause 0.0')
            self.cam_extras = ",reset_shader"

    def se2(self, typ, line, cmd):
        sename = SFX[line['arg0']]
        if not sename: print(line)
        sename = f"audio/sfx/{sename}.wav"
        if 'arg1' not in line:
            self.outlines.append(f'play audio {repr(sename)}')
        else:
            desired_len = int(line['arg1']) / 60
            with wave.open(f'game/{sename}', 'rb') as wavfile:
                flen = wavfile.getnframes() / wavfile.getframerate()

            count = int(desired_len / flen)

            l = ",".join([repr(sename)]*count)
            self.outlines.append(f'play sound [{l}] fadeout 1.0')

    def wait(self, typ, line, cmd):
        self.outlines.append(f'pause {int(line["arg0"])/60}')

    def output_shows(self):
        transition = 0
        wait = 0
        for cid, showchara in sorted(self.to_show.items(), key=lambda x:-x[1].order):
            self.shown[cid] = showchara.outfit, showchara.expression
            if showchara.transition != 0:
                transition = showchara.transition
           
            self.outlines.append(showchara.construct())
            wait = max(wait, showchara.wait)
            transition = max(transition, showchara.transition)
                    
        if wait and transition:
            wait = wait - transition
        if transition:
            self.outlines.append(f'with Dissolve({transition})')
        if wait:
            self.outlines.append(f'pause {(wait)}')
            
        for cid, showchara in sorted(self.to_show.items(), key=lambda x:-x[1].order):
            if(showchara.move_end):
                self.outlines.append(showchara.move_end)
                       
        self.to_show.clear()

    def compile_commands(self): 
        self.outlines.append('camera:\n anchor (0.5, 0.5)\n pos (960, 540)\n zoom 1.0\n matrixcolor IdentityMatrix()\npause 0.0')
        self.outlines.append('scene')
        self.outlines.append('stop music')
        for n, line in enumerate(self.commands): 
            typ, cmd = get_cmd(line)
            is_talk = 'arg0' not in line and 'arg1' in line
            text_out = ""

            if(cmd != "move" and cmd != "bgm2" and cmd != "se2" and cmd != "audio"):
                self.save_shake = ''
                
            if n in self.forcelines:
                self.outlines.append(self.forcelines[n])

            if is_talk:
                text_out = self.talk(n, line, cmd)
            elif hasattr(self, cmd):
                getattr(self, cmd)(typ, line, cmd)
            elif cmd not in ['shakeset', 'charaload']:
                # charaload is not needed for rpy and shakeset is handled elsewhere
                # any other commands are ones I don't know about and should look at
                # or I know about them but they are unimplemented
                print(cmd)

            if is_talk or typ == 0: 
                self.output_shows()
            if is_talk:
                self.outlines.append(text_out)

        return "\n".join(self.outlines)

# Setting up the compiler
def compile_script(folder, fname):
    ssrname, num = fname.split('_')
    header = f'''label {fname}:
 show black_background onlayer black
 $ event_store.current_event={repr(ssrname)}
 $ event_store.current_progress=0
 $ event_store.current_chapter={repr(fname)}'''
    
    with open(f'scripts/{folder}/{fname}.bytes', 'rb') as jsonfile:
        og_script = json.load(jsonfile)['scr']

    try:
        tl_dict = {}
        with open(f'translations/{folder}/{fname}.csv', 'r', encoding='utf8') as tlfile:
            reader = csv.reader(tlfile)
            for line in reader:
                if len(line) < 4: continue
                try: tl_dict[int(line[0])] = line[3]
                except ValueError: pass

    except IOError:
        tl_dict = {}

    compiled = Compiler(og_script, tl_dict).compile_commands()
    
    if num == "03":
        end = "return"
    else:
        end = f"jump {ssrname}_{int(num)+1:02d}"

    with open(f'game/scripts/{folder}/{fname}.rpy', 'w', encoding='utf8') as outfile:
        outfile.write(header + '\n' + indent(compiled, 1) + '\n call chapter_end\n ' + end)

# Start
if __name__ == '__main__':
    folder = sys.argv[1]
    fname = sys.argv[2]
    compile_script(folder,fname)


