# higumei-engine

Higurashi Mei in ren'py

## Character name mapping

Character name mappings are in `mappings/charname.csv`.

Each row is in the format JP_NAME, INTERNAL_ID, EN_NAME

Often temporary characters are introduced with setdispname, and you may want to add a translated name for them. 
Put the display name (arg1) as the JP_NAME, and the english name as EN_NAME. If there is furigana in JP_NAME, strip out the furigana. 
INTERNAL_ID can be left empty in these cases.

## Outfit mapping

These are in `mappings/outfits/<name>.csv`. <name> should match the INTERNAL_ID associated with the character. 

These are stored in OUTFIT_JP_NAME, DIRECTORY pairs. Outfits appear as CHARACTER_JP_NAME：OUTFIT_JP_NAME in the script, and are stored under `game/characters/sprites`

## mei2rp
  
`python mei2rp.py {event,chara} <filename_without_extension>`
  
For example: `python mei2rp.py event event01_30_01`
