import os
import sys
import csv
import json

from mei2rp import Compiler, indent


def get_chname(s):
    num = s.split('_')[-1]
    if num == '00': return 'Prologue'
    elif num == '99': return 'Epilogue'
    else: return f'Chapter {num}'

def main():
    event_name = sys.argv[1].split('/')[-1]
    script_source = sys.argv[1]
    tl_source = sys.argv[1].replace('scripts', 'translations')
    target = 'game/' + sys.argv[1] + '/'
    
    scripts = sorted(os.listdir(sys.argv[1]))
    translations = list(map(lambda x: x.replace('.bytes', '.csv'), scripts))
    
    greens = []
    try:
        with open(tl_source+'/green.csv', 'r') as tsvfile:
            for line in tsvfile:
                line = line.split('\t')
                greens.append((line[1], int(line[2]), line[0].strip('"'), line[3]))
    except FileNotFoundError:
        pass
    
    greens.sort()
    greencount = 0
    scriptnames = []
    chapter_jump = []

    script_type = ""

    for script in scripts:
        scriptname = script.split('.')[0]
        scriptnames.append(scriptname)
        chapter_jump.append((get_chname(scriptname), scriptname))

    if scriptnames[0].startswith('event'):
        script_type = "event"
    elif scriptnames[0].startswith('chara'):
        script_type = "chara"

    for n, script, trans in zip(range(len(scripts)), scripts, translations):
        scriptname = scriptnames[n]
        with open(script_source + '/' + script, 'rb') as jsonfile:
            og_script = json.load(jsonfile)['scr']

        tl_dict = {}
        with open(tl_source + '/' + trans, 'r', encoding='utf8') as tlfile:
            reader = csv.reader(tlfile)
            for line in reader:
                if len(line) < 4: continue
                try: tl_dict[int(line[0])] = line[3]
                except ValueError: pass

        greendict = {}
        header = f'''label {scriptname}:
 show black_background onlayer black
 $ event_store.current_event={repr(event_name)}
 $ event_store.current_progress={greencount}
 $ event_store.current_chapter={repr(scriptname)}
 $ persistent.menu_return={repr(script_type)}
                      '''.rstrip()

        for scr, line, title, contents in greens:
            if script.endswith(scr):
                greencount += 1
                greendict[line] = f'$ event_store.current_progress = {greencount}'
             
        compiled = Compiler(og_script, tl_dict, greendict).compile_commands()

        if n == len(scripts)-1:
            end = 'return'
        else:
            end = f'jump {scriptnames[n+1]}'

        with open(target + scriptname + '.rpy', 'w', encoding='utf8') as outfile:
            outfile.write(header + '\n' + indent(compiled, 1) + '\n call chapter_end\n ' + end)

    NEWLINE = '\n'
    greens = [l[2:] for l in greens]
    with open(target + 'event.rpy', 'w') as outfile:
        outfile.write(f"""
init python:
 event_store.notes[{repr(event_name)}] = {repr(greens)}
 event_store.chapters[{repr(event_name)}] = {repr(chapter_jump)}

label event_{event_name}:
 stop music
 jump {scriptnames[0]}
        """.strip('\n').rstrip())


if __name__ == '__main__':
    main()
