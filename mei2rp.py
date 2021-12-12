import os
import sys
import csv
import json
import wave

OUTFIT_MAPS = 'mappings/outfits/'

JP2ID = {}
ID2NAME = {}
OUTFITS = {}
BACKGROUND = {}
BGM = {}
SFX = {}
SHAKEMAP = {}

COLORS = {
    '黒': "#000",
    '白': "#fff",
    '赤': "#e11", # TODO tune the red
}

with open('mappings/charnames.csv') as cnames:
    reader = csv.reader(cnames)
    for line in reader:
        if len(line) < 3: continue
        JP2ID[line[0]] = line[1]
        ID2NAME[line[1]] = line[2]

with open('mappings/bg.csv') as cnames:
    reader = csv.reader(cnames)
    for line in reader:
        if len(line) < 2: continue
        BACKGROUND[line[0]] = line[1]

with open('mappings/bgm.csv') as cnames:
    reader = csv.reader(cnames)
    for line in reader:
        if len(line) < 2: continue
        BGM[line[0]] = line[1]

with open('mappings/se.csv') as cnames:
    reader = csv.reader(cnames)
    for line in reader:
        if len(line) < 2: continue
        SFX[line[0]] = line[1]

with open('mappings/shakes.csv') as cnames:
    reader = csv.reader(cnames)
    for line in reader:
        if len(line) < 2: continue
        SHAKEMAP[line[0]] = line[1]

for outfit in os.listdir(OUTFIT_MAPS):
    name = outfit.split('.')[0]
    OUTFITS[name] = {}

    with open(OUTFIT_MAPS + outfit) as cnames:
        reader = csv.reader(cnames)
        for line in reader:
            if len(line) < 2: continue
            OUTFITS[name][line[0]] = line[1]


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

def get_id(jp):
    if jp == '：': return None
    jp = jp.split('：')
    if jp[0] not in JP2ID: return None
    return JP2ID[jp[0]]

def strip_furigana(t):
    return t.split('#s')[0].lstrip('#p')

def get_name(jp, local=None):
    if jp == '：': return None
    jp = jp.split('：')[0]
    if local is not None and jp in local:
        jp = strip_furigana(local[jp])

    cid = JP2ID[jp]
    return ID2NAME[cid]

def indent(text, n):
    return '\n'.join(map(lambda line: n*' ' + line, text.split('\n')))

def get_cmd(command):
    if 'cmd1' in command: return 1, command['cmd1']
    else: return 0, command['cmd0']

def get_pos(p):
    if p == '左': return 'mei_left'
    elif p == '右': return 'mei_right'
    elif p == '中': return 'mei_center'
    else: return None

def get_ypos(p):
    if p == '下外': return -1080
    else: return int(p)

class ShowChara:
    def __init__(self, outfit, expression="normal"):
        self.outfit = outfit
        self.expression = expression
        self.transforms = []
        self.transition = None
        self.atl = None
        self.wait = 0

    def construct(self):
        s = ""
        if not self.transforms:
            s =  f'show {self.outfit} {self.expression}'
        else:
            s = f'show {self.outfit} {self.expression} at {",".join(self.transforms)}'

        if self.atl: 
            s += f'\nshow {self.outfit} {self.expression}:\n{indent(self.atl,1)}'
        return s

class Compiler:
    def __init__(self, commands, translation):
        '''
        self.COMMAND_DICT = {
            'wipeout': wipeout,
            'wipein': wipein,
            'shader': shader,
            'effect': effect,
            'voice': voice,
        }
        '''
        self.bgm = self.bgm2
        self.commands = commands
        self.translation = translation
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

        self.faded = "#000"
        self.background = None

    def talk(self, n, line, cmd):
        cid = get_id(cmd)
        if cid is None and cmd in self.local:
            name = get_name(cmd, self.local)
            cid = f'Character({repr(name)},ctc="ctcArrow", ctc_position="fixed")'
    
        text = self.translation.get(n, line['arg1'])
        for c, o in self.to_show.items():
            if c == cid: continue
            o.transforms.append('inactive')

        for c, o in self.shown.items():
            if c == cid: continue
            if c not in self.to_show:
                self.to_show[c] = ShowChara(o[0], o[1])
            self.to_show[c].transforms.append('inactive')

            
        if cid in self.shown or cid in self.to_show:
            if c not in self.to_show:
                o = self.to_show[cid]
                self.to_show[cid] = ShowChara(o[0], o[1])
            self.to_show[cid].transforms.append('active')
    
        if cid is None:
            return f'narrator {repr(text)}'
        else:
            return f'{cid} {repr(text)}'

    def setdispname(self, typ, line, cmd):
        self.local[line['arg0']] = line['arg1']
            
    def serifclose(self, typ, line, cmd):
        self.outlines.append('window hide None')

    def chara(self, typ, line, cmd):
        outfit = get_outfit(line['arg0'])
        expr = line['arg1']
        pos = get_pos(line['arg2'])
       
        showchara = ShowChara(outfit, expr)
        if pos is not None:
            showchara.transforms.append(pos)
        else:
            # NOTE. be CAREFUL Untested. rare codepath
            xpos = self.variables[line['arg2']]
            ypos = 1200
            showchara.atl = f"pos ({xpos}, 1200)"

        if typ == 0 and 'arg4' in line:
            time = int(line["arg4"]) / 60
            showchara.transition = f'Dissolve({time})'

        self.to_show[get_id(line['arg0'])] = showchara

    def effect(self, typ, line, cmd):
        eff = line['arg0']
        if eff != 'flash': raise ValueError('Effect type is not flash')

        self.outlines.append('show expression "#fff" as flash with Dissolve(0.1)')
        self.outlines.append('pause 0.1')
        self.outlines.append('hide flash with Dissolve(0.2)')

    def 変数(self, typ, line, cmd):
        dx = int(line.get('arg2', '0'))
        self.variables[line['arg0']] = self.variables[line['arg1']] + dx

    def zoom(self, typ, line, cmd):
        mag = line['arg0']
        xpos = self.variables[line['arg1']]
        ypos = 540 + int(line['arg2'])
        time = int(line['arg3']) / 60
        if time == 0:
            self.outlines.append(f"""
camera:
 anchor (0.5,0.5)
 pos ({xpos}, {ypos})
 zoom {mag}
            """.strip())
        else:
            self.outlines.append(f"""
camera:
 anchor (0.5,0.5)
 pos (960,540)
 parallel:
  linear {time} pos ({xpos}, {ypos})
 parallel:
  linear {time} zoom {mag}
            """.strip())
            if typ == 0: self.outlines.append(f'pause {time}')
    
    def shakechara(self, typ, line, cmd):
        oid = get_id(line['arg0'])
        anim = line['arg1']
        if oid not in self.shown: return
        if oid not in self.to_show:
            o = self.shown[oid]
            self.to_show[oid] = ShowChara(o[0], o[1])
        self.to_show[oid].transforms.append(SHAKEMAP[anim])

    def shakedisp(self, typ, line, cmd):
        anim = SHAKEMAP[line['arg0']]
        self.outlines.append(f'camera at {anim}\npause 0.0')
        
    def motion(self, typ, line, cmd):
        oid = get_id(line['arg0'])
        if oid not in self.shown: return
        if oid not in self.to_show:
            o = self.shown[oid]
            self.to_show[oid] = ShowChara(o[0], o[1])
        
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
        self.shown.clear()
        command = ""
        if bgname == "暗幕":
            self.background = f'scene expression "#000" as bg'
        else:
            bgname = BACKGROUND[bgname]
            bgname = f"images/{bgname}.png"
            self.outlines.append('stop sound')
            self.background = f'scene expression {repr(bgname)} as bg'

        if not self.faded:
            self.outlines.append(command)
        else:
            self.outlines.append(f'scene expression "{self.faded}"')
            self.background = self.background.replace('scene', 'show', 1)

    def fadein(self, typ, line, cmd):
        time = int(line['arg0']) / 60
        if self.background:
            self.outlines.append(f'{self.background}')
            self.background = None
        else:
            self.outlines.append(f'hide fade with Dissolve({time})')
        self.faded = False
        
        for showchara in self.to_show.values():
            showchara.transition = None
        self.output_shows()

        self.outlines.append(f'with Dissolve({time})')

    def fadeout(self, typ, line, cmd):
        color = COLORS[line['arg0']]
        time = int(line['arg1']) / 60
        self.faded = color
        self.outlines.append(f'show expression "{color}" as fade with Dissolve({time})')

    def bgm2(self, typ, line, cmd):
        name = BGM[line["arg0"]]
        name = f"audio/bgm/{name}.wav"
        self.outlines.append(f'play music {repr(name)}')

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
        outfit, expression = self.shown[cid]
        
        if cid not in self.to_show:
            self.to_show[cid] = ShowChara(outfit, expression)
        
        self.to_show[cid].atl = f"linear {time} pos ({xpos},{ypos})"
        self.to_show[cid].wait = max(self.to_show[cid].wait, time)

    def shader(self, typ, line, cmd):
        if line['arg0'] == 'セピア':
            self.outlines.append(f'camera at sepia_shader\npause 0.0')
        else:
            self.outlines.append(f'camera at reset_shader\npause 0.0')

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
        self.outlines.append(f'pause {int(line["arg0"])/30}')

    def output_shows(self):
        if self.faded: return
        transition = None
        wait = 0
        for cid, showchara in self.to_show.items():
            self.shown[cid] = showchara.outfit, showchara.expression
            if showchara.transition is not None:
                transition = showchara.transition
           
            self.outlines.append(showchara.construct())
            wait = max(wait, showchara.wait)

        if transition:
            self.outlines.append(f'with {transition}')
        if wait:
            self.outlines.append(f'pause {wait}')
        self.to_show.clear()

    def compile_commands(self): 
        for n, line in enumerate(self.commands): 
            typ, cmd = get_cmd(line)
            is_talk = 'arg0' not in line and 'arg1' in line
            text_out = ""

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

def compile_script(folder, fname):
    header = f'label {fname}:'
    
    with open(f'scripts/{folder}/{fname}.bytes') as jsonfile:
        og_script = json.load(jsonfile)['scr']

    try:
        tl_dict = {}
        with open(f'translations/{folder}/{fname}.csv') as tlfile:
            reader = csv.reader(tlfile)
            for line in reader:
                if len(line) < 4: continue
                try: tl_dict[int(line[0])] = line[3]
                except ValueError: pass

    except IOError:
        tl_dict = {}

    compiled = Compiler(og_script, tl_dict).compile_commands()

    with open(f'game/scripts/{folder}/{fname}.rpy', 'w') as outfile:
        outfile.write(header + '\n' + indent(compiled, 1))


if __name__ == '__main__':
    folder = sys.argv[1]
    fname = sys.argv[2]
    compile_script(folder,fname)


