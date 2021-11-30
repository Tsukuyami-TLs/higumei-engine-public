define gui.REGULAR_FONT = "NotoSansCJK-Regular.ttc"

init python:
    import json
    import unicodecsv as csv
    class Mapping:
        char_ids = {}
        names = {}
        outfits = {}

        with renpy.file('characters/map.csv') as charmap:
            for line in charmap:
                line = line.strip().split(',')
                if len(line) < 3: continue
                char_ids[line[0]] = line[1]
                names[line[1]] = line[2]


        dirs = renpy.list_files()
        dirs = [x for x in dirs if x.startswith('characters') and x.endswith('map.csv')]
        for dir in dirs:
            parts = dir.split('/')
            if len(parts) < 3: continue
            charname = parts[1]
            outfits[charname] = {'': 'v001'}

            with renpy.file(dir) as outmap:
                for line in outmap:
                    line = line.strip().split(',')
                    outfits[charname][line[0]] = 'v' + line[1]
        
        @staticmethod
        def speaker2outfit(speaker):
            if speaker == '：': 
                return '', ''

            parts = speaker.split('：')
            if parts[0] not in Mapping.char_ids:
                return parts[0], ''

            id = Mapping.char_ids[parts[0]]

            if len(parts) > 1: outfit = parts[1]
            else: outfit = ''

            if (id not in Mapping.outfits or outfit not in Mapping.outfits[id]) and outfit == '私服':
                outfit = 'v002'
            elif id not in Mapping.outfits:
                outfit = 'v001'
            else:
                outfit = Mapping.outfits[id][outfit]

            return id, id+'_'+outfit

    class Engine:
        """
        COMMAND_DICT = {
            'charaload': charaload,
            '変数': set_var,
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
        """

        @staticmethod
        def run_file(fname, tl):
            with renpy.file(fname) as f: 
                script = json.load(f)['scr']

            
            translations = {}
            with renpy.file(tl) as f:
                reader = csv.reader(f)
                for line in reader:
                    try: translations[int(line[0])] = line[3]
                    except: pass

            for n, line in enumerate(script):
                cmd = line.get('cmd0', line.get('cmd1', None))
                if 'arg0' not in line and 'arg1' in line:
                    id, outfit = Mapping.speaker2outfit(cmd)
                    name = Mapping.names.get(id, None)
                    renpy.say(name, translations.get(n, line['arg1']))
                
                if cmd == "setdispname":
                    Mapping.names[line["arg0"]] = line.get("arg1")

