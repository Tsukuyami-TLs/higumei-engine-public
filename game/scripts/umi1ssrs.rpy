init python:
 event_store.chapters['chara032009'] = [('Chapter 01', 'chara032009_01'), ('Chapter 02', 'chara032009_02'), ('Chapter 03', 'chara032009_03')]
 event_store.chapters['chara452001'] = [('Chapter 01', 'chara452001_01'), ('Chapter 02', 'chara452001_02'), ('Chapter 03', 'chara452001_03')]
 event_store.chapters['chara462001'] = [('Chapter 01', 'chara462001_01'), ('Chapter 02', 'chara462001_02'), ('Chapter 03', 'chara462001_03')]
 event_store.chapters['chara472001'] = [('Chapter 01', 'chara472001_01'), ('Chapter 02', 'chara472001_02'), ('Chapter 03', 'chara472001_03')]

label chara032009:
    stop music
    call chara032009_01
    return
label chara452001:
    stop music
    call chara452001_01
    return
label chara462001:
    stop music
    call chara462001_01
    return
label chara472001:
    stop music
    call chara472001_01
    eturn

