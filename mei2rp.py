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

def NOP(*args, **kwargs): pass
'''
COMMAND_DICT = {
    'charaload': NOP,
    '変数': NOP,
    'shakeset': shakeset,
    '背景': background,
    'bgm2': bgm,
    'bgm': bgm,
    'fadein': fadein,
    'motion': motion,
    'hide': hide,
    'chara': chara,
    'fadeout': fadeout,
    'zoom': zoom,
    'shakedisp': shakedisp,
    'shakechara': shakechara,
    'se2': se2,
    'wait': wait,
    'serifclose': serifclose,
    'move': move,
    'bgmstop': bgmstop,
    'wipeout': wipeout,
    'wipein': wipein,
    'shader': shader,
    'setdispname': setdispname,
    'removedispname': removedispname,
    'effect': effect,
    'voice': voice,
}
'''
def compile_commands(commands, translation):
    outlines = []
    local = {}
    for n, line in enumerate(commands):
        typ, cmd = get_cmd(line)
        if 'arg0' not in line and 'arg1' in line:
            name = get_name(cmd, local)
            text = translation.get(n, line['arg1'])
            if name is None:
                outlines.append(repr(text))
            else:
                outlines.append(f'{repr(name)} {repr(text)}')

        elif cmd == 'setdispname':
            local[line['arg0']] = line['arg1']

        elif cmd == 'chara':
            outfit = get_outfit(line['arg0'])
            expr = line['arg1']
            pos = get_pos(line['arg2'])
            outlines.append(f'show {outfit} {expr} at {pos}')
            if typ == 0 and 'arg4' in line:
                time = int(line["arg4"]) / 100
                outlines.append(f'with Dissolve({time})')

        elif cmd == 'hide':
            outfit = get_outfit(line['arg0'])
            outlines.append(f'hide {outfit}')
            if typ == 0 and 'arg1' in line:
                time = int(line["arg1"]) / 100
                outlines.append(f'with Dissolve({time})')

        elif cmd == "背景":
            bgname = line["arg0"]
            if bgname == "暗幕":
                outlines.append(f'hide bg')
            else:
                bgname = BACKGROUND[bgname]
                bgname = f"images/bg/{bgname}.png"
                outlines.append(f'scene expression {repr(bgname)} as bg')

        elif cmd == "bgm2":
            name = BGM[line["arg0"]]
            name = f"audio/bgm/{name}.wav"
            outlines.append(f'play music {repr(name)}')

        elif cmd == "bgmstop":
            if "arg0" in line:
                tim = int(line["arg0"])/60
                outlines.append(f'stop music fadeout {tim}')
            else:
                outlines.append(f'stop music')

        elif cmd == "se2":
            sename = SFX[line['arg0']]
            sename = f"audio/sfx/{sename}.wav"
            if 'arg1' not in line:
                outlines.append(f'play audio {repr(sename)}')
            else:
                desired_len = int(line['arg1']) / 30
                with wave.open(f'game/{sename}', 'rb') as wavfile:
                    flen = wavfile.getnframes() / wavfile.getframerate()

                count = int(desired_len / flen)
                #leftover = desired_len % flen

                l = ",".join([repr(sename)]*count)
                #l += "," + repr(f"<from 0 to {leftover}>{sename}")
                outlines.append(f'play sound [{l}] fadeout 1.0')


    return "\n".join(outlines)

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

    compiled = compile_commands(og_script, tl_dict)

    with open(f'game/scripts/{folder}/{fname}.rpy', 'w') as outfile:
        outfile.write(header + '\n' + indent(compiled, 1))


if __name__ == '__main__':
    folder = sys.argv[1]
    fname = sys.argv[2]
    compile_script(folder,fname)


