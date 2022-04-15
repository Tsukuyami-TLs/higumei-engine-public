init python:
 event_store.notes['christmas'] = []
 event_store.chapters['christmas'] = [('Prologue', 'event01_33_00'), ('Chapter 01', 'event01_33_01'), ('Chapter 02', 'event01_33_02'), ('Chapter 03', 'event01_33_03'), ('Chapter 04', 'event01_33_04'), ('Epilogue', 'event01_33_99')]

label event_christmas:
 stop music
 jump event01_33_00