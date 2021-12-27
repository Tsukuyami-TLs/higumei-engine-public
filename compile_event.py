import os
import sys
import csv
import json

from mei2rp import Compiler, indent


def main():
    event_name = sys.argv[1].split('/')[-1]
    script_source = sys.argv[1]
    tl_source = sys.argv[1].replace('scripts', 'translations')
    target = 'game/' + sys.argv[1] + '/'
    
    scripts = sorted(os.listdir(sys.argv[1]))
    translations = list(map(lambda x: x.replace('.bytes', '.csv'), scripts))
    
    greens = []
    with open(tl_source+'/green.csv', 'r') as tsvfile:
        for line in tsvfile:
            line = line.split('\t')
            greens.append((line[1], int(line[2]), line[0].strip('"'), line[3]))
    
    greens.sort()
    greencount = 0
    scriptnames = []
    for script, trans in zip(scripts, translations):
        scriptname = script.split('.')[0]
        scriptnames.append(scriptname)

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
 $ tlnote_store.current_event={repr(event_name)}
 $ tlnote_store.current_progress={greencount}
                      '''.rstrip()

        for scr, line, title, contents in greens:
            if script.endswith(scr):
                greencount += 1
                greendict[line] = f'$ tlnote_store.current_progress = {greencount}'
             
        compiled = Compiler(og_script, tl_dict, greendict).compile_commands()
        with open(target + scriptname + '.rpy', 'w', encoding='utf8') as outfile:
            outfile.write(header + '\n' + indent(compiled, 1) + '\n return')

    NEWLINE = '\n'
    greens = [l[2:] for l in greens]
    with open(target + 'event.rpy', 'w') as outfile:
        outfile.write(f"""
init python:
 tlnote_store.notes[{repr(event_name)}] = {repr(greens)}

label event_{event_name}:
 stop music
{indent(NEWLINE.join('call ' + label for label in scriptnames), 1)}
        """.strip('\n').rstrip())


if __name__ == '__main__':
    main()
