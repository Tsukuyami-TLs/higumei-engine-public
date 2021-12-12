import json
import math
import csv

SHAKEMAP = {}

def get_args(params):
    length, direc, mag, speed = int(params['arg1']), params['arg2'], int(params['arg3']), int(params['arg4'])
    return length/60, direc, mag, speed/60

with open('shakes.json', 'r') as jsonfile:
    shakes = json.load(jsonfile)

with open('mappings/shakes.csv') as cnames:
    reader = csv.reader(cnames)
    for line in reader:
        if len(line) < 2: continue
        SHAKEMAP[line[0]] = line[1]


def getshake(p, d, m):
    easer = f"ease {p}"
    if d == "RANDOM":
        dirs = [(m,0), (-m,0), (0,m), (0,-m), (m,m), (-m,-m), (-m,m), (m,-m)]
        return '\n'.join(f' choice:\n  {easer} offset {move}' for move in dirs)
    
    if d == "UP":
        move = (0, -m)
    elif d == "DOWN":
        move = (0, m)
    elif d == "LEFT":
        move = (-m, 0)
    elif d == "RIGHT":
        move = (m, 0)
    else:
        print(d)

    return f" {easer} offset {move}"
        

for name, params in shakes.items():
    length, direc, mag, period = get_args(params)
    times = math.ceil(length/period) 
    period2 = period/2
    
    fronthalf = getshake(period2, direc, mag)
    backhalf = f" ease {period2} offset (0,0)"
    print(f'transform {SHAKEMAP[name]}:')
    print(fronthalf)
    print(backhalf)
    if times > 1:
        print(f' repeat {times}')


