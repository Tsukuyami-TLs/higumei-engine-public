label event01_30_99:
 show black_background onlayer black
 play sound ['audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav'] fadeout 1.0
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2320.png' as bg
 with Dissolve(2.0)
 pause 1.0
 show expression "#000" as fade with Dissolve(1.0)
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2281.png' as bg
 with Dissolve(1.0)
 show nao_v002 sinken at mei_center
 with Dissolve(0.5)
 camera at screenshake_transform
 pause 0.0
 show nao_v002 sinken at active
 nao ''
 hide nao_v002
 with Dissolve(0.2)
 show mion_v002 sinken at mei_right
 show shion_v002 odoroki at mei_left
 with Dissolve(0.5)
 show shion_v002 odoroki at jump_transform,active
 show mion_v002 sinken at inactive
 shion "What's wrong? ...Wha?!?! S-sis..."
 show mion_v002 futeki at active
 show shion_v002 odoroki at inactive
 mion "....I'll do it,... let's give it to them...."
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 narrator 'The story goes back to when I first found the magic circle on my bed sheet.'
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 nao "W,..... what's that...."
 hide nao_v002
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_017_TragedyStart.wav'
 narrator "On Mion and Shion's bed,.... there's nothing. \nBut on my bed... /They'll be killed/."
 narrator 'The blankets were scattered in a crude pile...., the sheets were exposed like skin...., painted red....'
 narrator "That's not it. It's not just paint. It was dyed in.... fresh red blood...."
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 nao 'A.... magic circle....'
 play music 'audio/bgm/BGM_EVENT_TOP_COLLAB2.wav'
 hide nao_v002
 with Dissolve(0.2)
 narrator 'I was enraptured by that horrible magic circle. That was when the Sonozaki Sister spoke.'
 narrator 'Wha?!? S-sis...!!\nDo ...... give me.....'
 narrator "The following is an exchange that only the two Sonozaki sisters can hear.\u3000I was so terrified that I couldn't even hear it."
 show mion_v002 futeki at mei_right
 show shion_v002 sinken at mei_left
 with Dissolve(0.5)
 camera at screenshake_transform
 pause 0.0
 show shion_v002 sinken at active
 show mion_v002 futeki at inactive
 shion "....That....., is the scoundrel's magic circle?!?"
 show mion_v002 futeki at active
 show shion_v002 sinken at inactive
 mion ''
 show shion_v002 sinken at active
 show mion_v002 futeki at inactive
 shion ''
 show mion_v002 sinken at jump_transform,active
 show shion_v002 sinken at inactive
 mion ''
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 narrator ''
 narrator ''
 narrator ''
 show expression "#000" as fade with Dissolve(1.0)
 stop sound
 scene expression "#000"
 camera at sepia_shader
 pause 0.0
 show expression 'images/bg/AdvBg_2331.png' as bg
 show shannon_v001 smile at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(1.0)
 show erika_v001 normal at active
 show shannon_v001 smile at inactive
 erika ''
 show shannon_v001 smile_close at active
 show erika_v001 normal at inactive
 shannon ''
 hide shannon_v001
 hide erika_v001
 with Dissolve(0.2)
 narrator ''
 narrator ''
 narrator ''
 narrator ''
 narrator ''
 narrator ''
 show expression "#000" as fade with Dissolve(1.0)
 camera at reset_shader
 pause 0.0
 scene expression "#000"
 narrator ''
 narrator ''
 narrator ''
 narrator ''
 narrator ''
 narrator ''
 narrator ''
 narrator ''
 narrator ''
 narrator ''
 stop sound
 scene expression "#000"
 play music 'audio/bgm/BGM_BATTLE1_COLLAB2.wav'
 show expression 'images/bg/AdvBg_2281.png' as bg
 with Dissolve(1.0)
 narrator ''
 narrator ''
 narrator ''
 narrator ''
 camera at screenshake_transform
 pause 0.0
 narrator ''
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 smile at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 smile at active
 erika ''
 show erika_v001 smile at active
 erika ''
 camera at screenshake_transform
 pause 0.0
 show erika_v001 fuan at active
 erika ''
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 narrator ''
 play audio 'audio/sfx/SE_5046_scratch.wav'
 narrator ''
 narrator ''
 narrator ''
 narrator ''
 camera at screenshake_transform
 pause 0.0
 narrator ''
 narrator ''
 show expression "#fff" as flash with Dissolve(0.1)
 pause 0.1
 hide flash with Dissolve(0.2)
 narrator ''
 show erika_v001 futeki at mei_center
 with Dissolve(0.5)
 show erika_v001 futeki at active
 erika ''
 hide erika_v001
 with Dissolve(0.2)
 narrator ''
 narrator ''
 play audio 'audio/sfx/SE_325_ls_thunderfall.wav'
 narrator ''
 camera at screenshake_transform
 pause 0.0
 narrator ''
 narrator ''
 narrator ''
 narrator ''
 narrator ''
 narrator ''
 narrator ''
 narrator ''
 narrator ''
 narrator ''
 narrator ''
 narrator ''
 narrator ''
 narrator ''
 narrator ''
 narrator ''
 narrator ''
 narrator ''
 narrator ''
 narrator ''
 narrator ''
 narrator ''
 narrator ''
 camera at screenshake_transform
 pause 0.0
 narrator ''
 narrator ''
 narrator ''
 narrator ''
 narrator ''
 narrator ''
 narrator ''
 stop music fadeout 2.0
 window hide None
 show expression "#000" as fade with Dissolve(1.0)
 stop sound
 scene expression "#000"
 play music 'audio/bgm/BGM_GACHA_COLLAB2.wav'
 show expression 'images/bg/AdvBg_2271.png' as bg
 with Dissolve(1.0)
 pause 1.0
 call wipeout_routine
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2221.png' as bg
 call wipein_routine
 pause 1.0
 call wipeout_routine
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2251.png' as bg
 call wipein_routine
 show jessica_v001 smile at mei_center
 with Dissolve(0.5)
 show jessica_v001 smile at active
 jessica ''
 hide jessica_v001
 with Dissolve(0.2)
 Character('Krauss Ushiromiya',ctc="ctcArrow", ctc_position="fixed") ''
 Character('Natsuhi Ushiromiya',ctc="ctcArrow", ctc_position="fixed") ''
 show shion_v002 smile at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at active
 show shion_v002 smile at inactive
 mion ''
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion ''
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 narrator ''
 narrator ''
 show erika_v001 normal at mei_right
 show kanon_v001 normal_close at mei_left
 with Dissolve(0.5)
 show kanon_v001 normal_close at active
 show erika_v001 normal at inactive
 kanon ''
 show erika_v001 normal at active
 show kanon_v001 normal_close at inactive
 erika ''
 show kanon_v001 normal at active
 show erika_v001 normal at inactive
 kanon ''
 play audio 'audio/sfx/SE_226_shine.wav'
 show erika_v001 smile at active
 show kanon_v001 normal at inactive
 erika ''
 hide erika_v001
 hide kanon_v001
 with Dissolve(0.2)
 show nao_v002 smile at mei_left
 show jessica_v001 fuan_blush at mei_right
 with Dissolve(0.5)
 show jessica_v001 fuan_blush at active
 show nao_v002 smile at inactive
 jessica ''
 show jessica_v001 smile_blush at jump_transform,active
 show nao_v002 smile at inactive
 jessica ''
 show nao_v002 smile at active
 show jessica_v001 smile_blush at inactive
 nao ''
 hide nao_v002
 hide jessica_v001
 with Dissolve(0.2)
 narrator ''
 show nao_v002 smile at mei_left
 show beatrice_v001 smile at mei_right
 with Dissolve(0.5)
 show beatrice_v001 smile at active
 show nao_v002 smile at inactive
 beatrice ''
 show nao_v002 smile at active
 show beatrice_v001 smile at inactive
 nao ''
 show beatrice_v001 futeki at active
 show nao_v002 smile at inactive
 beatrice ''
 show beatrice_v001 futeki at active
 show nao_v002 smile at inactive
 beatrice ''
 show nao_v002 smile at active
 show beatrice_v001 futeki at inactive
 nao ''
 hide beatrice_v001
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show nao_v002 smile at inactive
 dlanor ''
 show nao_v002 smile at active
 show dlanor_v001 normal at inactive
 nao ''
 hide dlanor_v001
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show nao_v002 smile at inactive
 erika ''
 show nao_v002 smile at active
 show erika_v001 normal at inactive
 nao ''
 show erika_v001 smile at active
 show nao_v002 smile at inactive
 erika ''
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 show shion_v002 smile at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at active
 show shion_v002 smile at inactive
 mion ''
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion ''
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika ''
 show erika_v001 futeki at active
 erika ''
 hide erika_v001
 with Dissolve(0.2)
 show mion_v002 smile at mei_right
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion ''
 show mion_v002 smile at active
 show shion_v002 smile at inactive
 mion ''
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao ''
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 normal_close at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 normal_close at active
 erika ''
 show erika_v001 normal at active
 erika ''
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show nao_v002 futeki at mei_center
 with Dissolve(0.5)
 show nao_v002 futeki at active
 nao ''
 show expression "#fff" as fade with Dissolve(2.5)
 window hide None
 hide nao_v002
 with Dissolve(0.2)
 pause 3.0
 play sound ['audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav'] fadeout 1.0
 stop sound
 scene expression "#fff"
 play music 'audio/bgm/BGM_HOME_COLLAB2.wav'
 show expression 'images/bg/AdvBg_2101.png' as bg
 with Dissolve(1.0)
 show erika_v001 normal at mei_right
 show nao_v002 smile at mei_left
 with Dissolve(0.5)
 show nao_v002 smile at active
 show erika_v001 normal at inactive
 nao ''
 show erika_v001 normal_close at active
 show nao_v002 smile at inactive
 erika ''
 show erika_v001 normal at active
 show nao_v002 smile at inactive
 erika ''
 show nao_v002 normal at active
 show erika_v001 normal at inactive
 nao ''
 hide erika_v001
 hide nao_v002
 with Dissolve(0.2)
 show shion_v002 fuan at mei_left
 show mion_v002 odoroki at mei_right
 with Dissolve(0.5)
 camera at screenshake_transform
 pause 0.0
 show mion_v002 odoroki at active
 show shion_v002 fuan at inactive
 mion ''
 show shion_v002 fuan at active
 show mion_v002 odoroki at inactive
 shion ''
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika ''
 show erika_v001 normal at active
 erika ''
 hide erika_v001
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_5037_getup.wav'
 narrator ''
 narrator ''
 play audio 'audio/sfx/SE_006_WindowScroll.wav'
 narrator ''
 show shion_v002 smile at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at active
 show shion_v002 smile at inactive
 mion ''
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion ''
 camera at screenshake_transform
 pause 0.0
 show mion_v002 odoroki at active
 show shion_v002 smile at inactive
 mion ''
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 show nao_v002 normal at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show nao_v002 normal at inactive
 erika ''
 show nao_v002 fuan at active
 show erika_v001 normal at inactive
 nao ''
 show erika_v001 normal_close at active
 show nao_v002 fuan at inactive
 erika ''
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 show shion_v002 smile at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at active
 show shion_v002 smile at inactive
 mion ''
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion ''
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika ''
 show erika_v001 normal at active
 erika ''
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 show nao_v002 normal at mei_center
 with Dissolve(0.08333333333333333)
 show nao_v002 normal at active
 nao ''
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 narrator ''
 stop music fadeout 0.5
 play audio 'audio/sfx/SE_325_ls_thunderfall.wav'
 show expression "#fff" as fade with Dissolve(1.0)
 erika ''
 stop sound
 scene expression "#fff"
 play music 'audio/bgm/BGM_EVENT_TOP_COLLAB2.wav'
 show expression 'images/bg/AdvBg_2101.png' as bg
 with Dissolve(1.0)
 show shion_v011 fuan at mei_left
 show mion_v012 fuan at mei_right
 with Dissolve(0.5)
 show mion_v012 fuan at active
 show shion_v011 fuan at inactive
 mion ''
 camera at screenshake_transform
 pause 0.0
 show shion_v011 odoroki at active
 show mion_v012 fuan at inactive
 shion ''
 hide shion_v011
 hide mion_v012
 with Dissolve(0.2)
 show erika_v001 normal at mei_right
 show nao_v014 odoroki at mei_left
 with Dissolve(0.5)
 show nao_v014 odoroki at jump_transform,active
 show erika_v001 normal at inactive
 nao ''
 show erika_v001 normal at active
 show nao_v014 odoroki at inactive
 erika ''
 show erika_v001 normal at active
 show nao_v014 odoroki at inactive
 erika ''
 show nao_v014 odoroki_blush at chara_shake_transform,active
 show erika_v001 normal at inactive
 nao ''
 hide erika_v001
 hide nao_v014
 with Dissolve(0.2)
 show mion_v012 smile at mei_right
 show shion_v011 fuan at mei_left
 with Dissolve(0.5)
 show shion_v011 fuan at active
 show mion_v012 smile at inactive
 shion ''
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show mion_v012 smile at active
 show shion_v011 fuan at inactive
 mion ''
 play audio 'audio/sfx/SE_311_ls_cutejump.wav'
 show shion_v011 smile at jump_transform,active
 show mion_v012 smile at inactive
 shion ''
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide mion_v012
 hide shion_v011
 hide fade with Dissolve(0.08333333333333333)
 show nao_v014 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show nao_v014 sinken at active
 nao ''
 camera at screenshake_transform
 pause 0.0
 show nao_v014 fuan at active
 nao ''
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide nao_v014
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika ''
 show erika_v001 normal at active
 erika ''
 hide erika_v001
 with Dissolve(0.2)
 show mion_v012 smile at mei_center
 with Dissolve(0.5)
 show mion_v012 smile at active
 mion ''
 hide mion_v012
 with Dissolve(0.2)
 show erika_v001 normal at mei_right
 show nao_v014 sinken_blush at mei_left
 with Dissolve(0.5)
 show nao_v014 sinken_blush at chara_shake_transform,active
 show erika_v001 normal at inactive
 nao ''
 show erika_v001 normal at active
 show nao_v014 sinken_blush at inactive
 erika ''
 hide erika_v001
 hide nao_v014
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_006_WindowScroll.wav'
 narrator ''
 narrator ''
 narrator ''
 show nao_v014 fuan at mei_center
 with Dissolve(0.5)
 show nao_v014 fuan at active
 nao ''
 hide nao_v014
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_006_WindowScroll.wav'
 narrator ''
 narrator ''
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide fade with Dissolve(0.08333333333333333)
 show nao_v014 fuan_blush at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show nao_v014 fuan_blush at active
 nao ''
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide nao_v014
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show erika_v001 normal_close at mei_center
 with Dissolve(0.5)
 show erika_v001 normal_close at active
 erika ''
 hide erika_v001
 with Dissolve(0.2)
 show mion_v012 smile at mei_right
 show shion_v011 smile at mei_left
 with Dissolve(0.5)
 show shion_v011 smile at active
 show mion_v012 smile at inactive
 shion "Wait- that's a bit like the Angel Mort's outfits!"
 show mion_v012 smile at active
 show shion_v011 smile at inactive
 mion ''
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide mion_v012
 hide shion_v011
 hide fade with Dissolve(0.08333333333333333)
 show nao_v014 sinken at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show nao_v014 sinken at active
 nao ''
 camera at screenshake_transform
 pause 0.0
 show nao_v014 sinken at active
 nao ''
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide nao_v014
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika ''
 hide erika_v001
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_006_WindowScroll.wav'
 narrator ''
 narrator ''
 narrator ''
 show nao_v014 odoroki at mei_center
 with Dissolve(0.5)
 show nao_v014 odoroki at active
 nao ''
 hide nao_v014
 with Dissolve(0.2)
 show shion_v011 smile at mei_left
 show mion_v012 smile at mei_right
 with Dissolve(0.5)
 show mion_v012 smile at active
 show shion_v011 smile at inactive
 mion ''
 show shion_v011 fuan at active
 show mion_v012 smile at inactive
 shion ''
 hide mion_v012
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show shion_v011 fuan at inactive
 erika ''
 show shion_v011 fuan_close at active
 show erika_v001 normal at inactive
 shion ''
 hide erika_v001
 show mion_v012 smile at mei_right
 with Dissolve(0.5)
 show mion_v012 smile at active
 show shion_v011 fuan_close at inactive
 mion ''
 hide shion_v011
 hide mion_v012
 with Dissolve(0.2)
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika ''
 show nao_v014 sinken_blush at mei_left
 with Dissolve(0.5)
 show nao_v014 sinken_blush at active
 show erika_v001 normal at inactive
 nao ''
 show nao_v014 sinken_blush at chara_shake_transform,active
 show erika_v001 normal at inactive
 nao ''
 show erika_v001 futeki at active
 show nao_v014 sinken_blush at inactive
 erika '*giggle*giggle*giggle* <May I help you?>'
 hide erika_v001
 hide nao_v014
 with Dissolve(0.2)
 show nao_v014 sinken at mei_center
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_311_ls_cutejump.wav'
 show nao_v014 sinken at jump_transform,active
 nao "<Yes!! I need> Ummm.... This skirt's front!!"
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.2
 pause 0.5
 show nao_v014 sinken at active
 nao 'Give me back the front part of this skirt! At least let me cover the abdomen area!!'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.4
 pause 0.5
 camera at screenshake_transform
 pause 0.0
 show nao_v014 sinken at active
 nao "What's with this outfit!! It's tasteless!! It's the worstttttttt!!!"
 show expression "#000" as fade with Dissolve(3.0)
 pause 1.5
 return