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
    if oid in OUTFITS[cid]:
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
    else: return 'mei_center'

class Compiler:
    def __init__(self, commands, translation):
        '''
        self.COMMAND_DICT = {
            'shakeset': shakeset,
            'fadein': fadein,
            'motion': motion,
            'fadeout': fadeout,
            'zoom': zoom,
            'shakedisp': shakedisp,
            'shakechara': shakechara,
            'serifclose': serifclose,
            'move': move,
            'wipeout': wipeout,
            'wipein': wipein,
            'shader': shader,
            'effect': effect,
            'voice': voice,
            '変数': None,
        }
        '''
        self.bgm = self.bgm2
        self.commands = commands
        self.translation = translation
        self.outlines = []
        self.local = {}
        self.shown = {}


    def talk(self, n, line, cmd):
        cid = get_id(cmd)
        if cid is None and cmd in self.local:
            name = get_name(cmd, self.local)
            cid = f'Character({repr(name)},ctc="ctcArrow", ctc_position="fixed")'
    
        text = self.translation.get(n, line['arg1'])
        for c, o in self.shown.items():
            if c == cid: continue
            self.outlines.append(f'{o}, inactive')
        if cid in self.shown:
            self.outlines.append(f'{self.shown[cid]}, active')
    
        if cid is None:
            self.outlines.append(f'narrator {repr(text)}')
        else:
            self.outlines.append(f'{cid} {repr(text)}')

    def setdispname(self, typ, line, cmd):
        self.local[line['arg0']] = line['arg1']
            
    def chara(self, typ, line, cmd):
        outfit = get_outfit(line['arg0'])
        expr = line['arg1']
        pos = get_pos(line['arg2'])
        self.outlines.append(f'show {outfit} {expr} at {pos}, active')
        self.shown[get_id(line['arg0'])] = f'show {outfit} {expr} at {pos}'
        if typ == 0 and 'arg4' in line:
            time = int(line["arg4"]) / 100
            self.outlines.append(f'with Dissolve({time})')
    
    def motion(self, typ, line, cmd):
        if get_id(line['arg0']) not in self.shown: return
        oid = get_id(line['arg0'])
        outfit = get_outfit(line['arg0'])
        curr_line = self.shown[oid]
        parts = curr_line.split(' ')
        expr = line['arg1']
        parts[2] = expr
        self.shown[oid] = ' '.join(parts)
        self.outlines.append(f'show {outfit} {expr}')

    def hide(self, typ, line, cmd):
        outfit = get_outfit(line['arg0'])
        self.outlines.append(f'hide {outfit}')

        try: del self.shown[get_id(line['arg0'])]
        except KeyError: pass

        if typ == 0 and 'arg1' in line:
            time = int(line["arg1"]) / 100
            self.outlines.append(f'with Dissolve({time})')

    def 背景(self, typ, line, cmd):
        bgname = line["arg0"]
        self.shown.clear()
        if bgname == "暗幕":
            self.outlines.append(f'scene expression "#000" as bg')
        else:
            bgname = BACKGROUND[bgname]
            bgname = f"images/{bgname}.png"
            self.outlines.append('stop sound')
            self.outlines.append(f'scene expression {repr(bgname)} as bg')

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

    def se2(self, typ, line, cmd):
        sename = SFX[line['arg0']]
        if not sename: print(line)
        sename = f"audio/sfx/{sename}.wav"
        # TODO: Figure out what the hell arg1 does
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

    def compile_commands(self): 
        for n, line in enumerate(self.commands): 
            typ, cmd = get_cmd(line)

            if 'arg0' not in line and 'arg1' in line:
                self.talk(n, line, cmd)
            elif hasattr(self, cmd):
                getattr(self, cmd)(typ, line, cmd)
    
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


