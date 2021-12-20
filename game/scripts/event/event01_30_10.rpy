label event01_30_10:
 stop sound
 scene expression "#000"
 play music 'audio/bgm/BGM_QUEST6_COLLAB2.wav'
 show expression 'images/bg/AdvBg_2190.png' as bg
 with Dissolve(1.0)
 show beatrice_v001 normal at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao 'I think something like this has been in manga or anime before...'
 show beatrice_v001 fuan at active
 show nao_v002 normal at inactive
 beatrice 'Huh? Ca, can you run that over once more...?'
 show nao_v002 normal at active
 show beatrice_v001 fuan at inactive
 nao 'I think... that this magic circle appeared in some manga or anime before, probably.'
 camera at screenshake_transform
 pause 0.0
 show beatrice_v001 odoroki at active
 show nao_v002 normal at inactive
 beatrice "What'd you say?! Manga....?!?!"
 hide nao_v002
 show erika_v001 sinken_close at mei_left
 with Dissolve(0.5)
 show erika_v001 sinken_close at active
 show beatrice_v001 odoroki at inactive
 erika "Beatrice, haven't you seen it...? Detective Wanyan."
 show beatrice_v001 futeki at updown_shake_transform,active
 show erika_v001 sinken_close at inactive
 beatrice "Huh? Ahahaha, I'm more into the Kaneda Case Files."
 show beatrice_v001 futeki at active
 show erika_v001 sinken_close at inactive
 beatrice "Detective Wanyan is too childish, so I don't watch it. That said, I remember Shannon saying it's interesting and recommending it to me."
 show erika_v001 odoroki at active
 show beatrice_v001 futeki at inactive
 erika ''
 show erika_v001 odoroki_close at chara_shake_transform,active
 show beatrice_v001 futeki at inactive
 erika ''
 hide beatrice_v001
 hide erika_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao ''
 show nao_v002 normal at active
 nao ''
 hide nao_v002
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 dlanor ''
 show erika_v001 odoroki at mei_right
 with Dissolve(0.5)
 show erika_v001 odoroki at active
 show dlanor_v001 normal at inactive
 erika ''
 hide dlanor_v001
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show erika_v001 odoroki at inactive
 nao ''
 show erika_v001 sinken at active
 show nao_v002 normal at inactive
 erika ''
 show nao_v002 normal at active
 show erika_v001 sinken at inactive
 nao ''
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide erika_v001
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 sinken at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show erika_v001 sinken at active
 erika ''
 show erika_v001 smile at active
 erika ''
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show beatrice_v001 fuan at mei_center
 with Dissolve(0.5)
 show beatrice_v001 fuan at active
 beatrice ''
 hide beatrice_v001
 with Dissolve(0.2)
 show erika_v001 fuan at mei_center
 with Dissolve(0.5)
 show erika_v001 fuan at active
 erika ''
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.1
 pause 0.5
 show erika_v001 smile at active
 erika ''
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.2
 pause 0.5
 camera at screenshake_transform
 pause 0.0
 show erika_v001 fuan at active
 erika ''
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 play audio 'audio/sfx/SE_226_shine.wav'
 show erika_v001 futeki at active
 erika ''
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 hide erika_v001
 with Dissolve(0.2)
 show dlanor_v001 fuan at mei_left
 show beatrice_v001 fuan at mei_right
 with Dissolve(0.5)
 show beatrice_v001 fuan at active
 show dlanor_v001 fuan at inactive
 beatrice ''
 show dlanor_v001 fuan at active
 show beatrice_v001 fuan at inactive
 dlanor ''
 hide dlanor_v001
 hide beatrice_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao ''
 show nao_v002 normal at active
 nao ''
 hide nao_v002
 with Dissolve(0.2)
 show nao_v002 normal at mei_left
 show beatrice_v001 fuan at mei_right
 with Dissolve(0.5)
 show beatrice_v001 fuan at active
 show nao_v002 normal at inactive
 beatrice ''
 show nao_v002 normal_close at active
 show beatrice_v001 fuan at inactive
 nao ''
 hide beatrice_v001
 show dlanor_v001 fuan_close at mei_right
 with Dissolve(0.5)
 show dlanor_v001 fuan_close at active
 show nao_v002 normal_close at inactive
 dlanor ''
 show nao_v002 normal at active
 show dlanor_v001 fuan_close at inactive
 nao ''
 show nao_v002 normal at active
 show dlanor_v001 fuan_close at inactive
 nao ''
 hide dlanor_v001
 show beatrice_v001 futeki at mei_right
 with Dissolve(0.5)
 show beatrice_v001 futeki at active
 show nao_v002 normal at inactive
 beatrice ''
 show nao_v002 smile at active
 show beatrice_v001 futeki at inactive
 nao ''
 show nao_v002 normal at active
 show beatrice_v001 futeki at inactive
 nao ''
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide nao_v002
 hide beatrice_v001
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 sinken_close at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 sinken_close at chara_shake_transform,active
 erika ''
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show erika_v001 sinken_close at mei_right
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show erika_v001 sinken_close at inactive
 dlanor ''
 show erika_v001 sinken_close at active
 show dlanor_v001 normal at inactive
 erika ''
 hide erika_v001
 hide dlanor_v001
 with Dissolve(0.2)
 show beatrice_v001 smile at mei_center
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_311_ls_cutejump.wav'
 show beatrice_v001 smile at jumping_transform,active
 beatrice ''
 hide beatrice_v001
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 dlanor ''
 hide dlanor_v001
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_5040_handclap.wav'
 pause 1.3333333333333333
 play audio 'audio/sfx/SE_5040_handclap.wav'
 narrator ''
 narrator ''
 show beatrice_v001 futeki at mei_center
 with Dissolve(0.5)
 show beatrice_v001 futeki at active
 beatrice ''
 show beatrice_v001 futeki at jump_transform,active
 beatrice ''
 show beatrice_v001 smile at active
 beatrice ''
 show beatrice_v001 smile at active
 beatrice ''
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide beatrice_v001
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 smile at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 smile at chara_shake_transform,active
 erika ''
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show nao_v002 normal at mei_left
 show dlanor_v001 normal_close at mei_right
 with Dissolve(0.5)
 show dlanor_v001 normal_close at active
 show nao_v002 normal at inactive
 dlanor ''
 show nao_v002 smile at active
 show dlanor_v001 normal_close at inactive
 nao ''
 show dlanor_v001 smile at active
 show nao_v002 smile at inactive
 dlanor ''
 hide dlanor_v001
 show beatrice_v001 smile at mei_right
 with Dissolve(0.5)
 show beatrice_v001 smile at active
 show nao_v002 smile at inactive
 beatrice ''
 show nao_v002 fuan at active
 show beatrice_v001 smile at inactive
 nao ''
 show nao_v002 smile at active
 show beatrice_v001 smile at inactive
 nao ''
 show beatrice_v001 normal_close at active
 show nao_v002 smile at inactive
 beatrice ''
 show beatrice_v001 smile at active
 show nao_v002 smile at inactive
 beatrice ''
 show nao_v002 smile at active
 show beatrice_v001 smile at inactive
 nao ''
 show beatrice_v001 futeki at active
 show nao_v002 smile at inactive
 beatrice ''
 hide nao_v002
 hide beatrice_v001
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show dlanor_v001 normal at inactive
 erika ''
 show dlanor_v001 normal_close at active
 show erika_v001 normal at inactive
 dlanor ''
 show dlanor_v001 normal at active
 show erika_v001 normal at inactive
 dlanor ''
 hide dlanor_v001
 hide erika_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao ''
 hide nao_v002
 with Dissolve(0.2)
 show expression "#000" as fade with Dissolve(1.0)
 hide fade with Dissolve(1.0)
 with Dissolve(1.0)
 narrator ''
 narrator ''
 narrator ''
 stop music fadeout 2.0
 window hide None
 show expression "#000" as fade with Dissolve(3.0)
 play music 'audio/bgm/BGM_GACHA_COLLAB2.wav'
 show expression "#fff" as fade with Dissolve(2.0)
 stop sound
 scene expression "#fff"
 show expression 'images/bg/AdvBg_2221.png' as bg
 with Dissolve(1.0)
 pause 1.0
 call wipeout_routine
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2271.png' as bg
 call wipein_routine
 pause 1.0
 call wipeout_routine
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2281.png' as bg
 call wipein_routine
 play audio 'audio/sfx/SE_543_bird.wav'
 narrator ''
 narrator ''
 narrator ''
 narrator ''
 stop music fadeout 0.5
 scene expression "#000" as bg
 narrator ''
 play music 'audio/bgm/BGM_QUEST7_COLLAB2.wav'
 nao ''
 nao ''
 show expression "#000" as fade with Dissolve(1.0)
 stop sound
 scene expression "#000"
 play audio 'audio/sfx/SE_346_ls_blood.wav'
 show expression 'images/bg/AdvBg_1270.png' as bg
 with Dissolve(1.0)
 play sound ['audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav'] fadeout 1.0
 narrator ''
 narrator ''
 narrator ''
 narrator ''
 narrator ''
 narrator ''
 narrator ''
 narrator ''
 narrator ''
 show expression "#000" as fade with Dissolve(1.0)
 scene expression "#000"
 play audio 'audio/sfx/SE_527_door_close.wav'
 narrator ''
 nao ''
 stop sound
 scene expression "#000"
 play audio 'audio/sfx/SE_526_door_open.wav'
 show expression 'images/bg/AdvBg_2281.png' as bg
 with Dissolve(1.0)
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 nao ''
 hide nao_v002
 with Dissolve(0.2)
 narrator ''
 narrator ''
 narrator ''
 narrator ''
 narrator ''
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 nao ''
 show expression "#000" as fade with Dissolve(1.0)
 hide nao_v002
 with Dissolve(0.2)
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_1270.png' as bg
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_017_TragedyStart.wav'
 narrator ''
 camera at screenshake_transform
 pause 0.0
 nao ''
 window hide None
 show expression "#000" as fade with Dissolve(2.0)
 scene expression "#000"
 pause 2.0
 stop music
 nao ''
 narrator ''
 play music 'audio/bgm/BGM_QUEST6_COLLAB2.wav'
 narrator ''
 play audio 'audio/sfx/SE_5005_grab.wav'
 erika ''
 erika ''
 erika ''
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2281.png' as bg
 with Dissolve(1.0)
 show nao_v002 normal at mei_left
 show erika_v001 odoroki at mei_right
 with Dissolve(0.5)
 camera at screenshake_transform
 pause 0.0
 show erika_v001 odoroki at active
 show nao_v002 normal at inactive
 erika ''
 show nao_v002 normal at active
 show erika_v001 odoroki at inactive
 nao ''
 show nao_v002 normal at active
 show erika_v001 odoroki at inactive
 nao ''
 show erika_v001 futeki at active
 show nao_v002 normal at inactive
 erika ''
 show erika_v001 smile at active
 show nao_v002 normal at inactive
 erika ''
 show nao_v002 fuan_close at active
 show erika_v001 smile at inactive
 nao ''
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_408_run.wav'
 narrator ''
 call wipeout_routine
 call wipein_routine
 pause 2.0
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 smile at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show erika_v001 smile at active
 erika ''
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show nao_v002 sinken at mei_center
 with Dissolve(0.5)
 show nao_v002 sinken at active
 nao ''
 hide nao_v002
 with Dissolve(0.2)
 narrator ''
 show erika_v001 smile at mei_center
 with Dissolve(0.5)
 show erika_v001 smile at active
 erika ''
 play audio 'audio/sfx/SE_215_heartgrow.wav'
 show erika_v001 smile at jumping_transform,active
 erika ''
 show erika_v001 smile at chara_shake_transform,active
 erika ''
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 show shion_v002 smile_blush at mei_center
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_311_ls_cutejump.wav'
 show shion_v002 smile_blush at jump_transform,active
 shion ''
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide shion_v002
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 nao ''
 hide nao_v002
 with Dissolve(0.2)
 show erika_v001 smile at mei_center
 with Dissolve(0.5)
 show erika_v001 smile at active
 erika ''
 show erika_v001 smile at active
 erika ''
 hide erika_v001
 with Dissolve(0.2)
 show nao_v002 fuan at mei_left
 show shion_v002 smile at mei_right
 with Dissolve(0.5)
 show shion_v002 smile at active
 show nao_v002 fuan at inactive
 shion ''
 show nao_v002 fuan_close at active
 show shion_v002 smile at inactive
 nao ''
 hide nao_v002
 hide shion_v002
 with Dissolve(0.2)
 show erika_v001 smile at mei_center
 with Dissolve(0.5)
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.1
 pause 0.5
 show erika_v001 smile at active
 erika ''
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.2
 pause 0.5
 show erika_v001 fuan at active
 erika ''
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 play audio 'audio/sfx/SE_5037_getup.wav'
 pause 2.0
 camera at screenshake_transform
 pause 0.0
 show erika_v001 smile at active
 erika ''
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at active
 nao ''
 show mion_v002 futeki at mei_right
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_226_shine.wav'
 show mion_v002 futeki at active
 show nao_v002 fuan at inactive
 mion ''
 show nao_v002 fuan_close at active
 show mion_v002 futeki at inactive
 nao ''
 hide nao_v002
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at jump_transform,active
 show mion_v002 futeki at inactive
 shion ''
 play audio 'audio/sfx/SE_215_heartgrow.wav'
 show mion_v002 smile at jumping_transform,active
 show shion_v002 smile at inactive
 mion ''
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show nao_v002 fuan_close at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan_close at active
 nao ''
 hide nao_v002
 with Dissolve(0.2)
 narrator ''
 narrator ''
 narrator ''
 narrator ''
 show erika_v001 smile at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show erika_v001 smile at inactive
 nao ''
 show erika_v001 normal at active
 show nao_v002 normal at inactive
 erika ''
 hide erika_v001
 hide nao_v002
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
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide mion_v002
 hide shion_v002
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 sinken at mei_center
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_341_ls_WhistleShort.wav'
 pause 0.16666666666666666
 play audio 'audio/sfx/SE_341_ls_WhistleLong.wav'
 camera at screenshake_transform
 pause 0.0
 show erika_v001 sinken at active
 erika ''
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show shion_v002 smile at mei_center
 with Dissolve(0.5)
 show shion_v002 smile at updown_shake_transform,active
 shion ''
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide shion_v002
 hide fade with Dissolve(0.08333333333333333)
 show nao_v002 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show nao_v002 sinken at active
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
 window hide None
 show expression "#000" as fade with Dissolve(1.0)
 pause 1.0
 play music 'audio/bgm/BGM_QUEST5_COLLAB2.wav'
 hide fade with Dissolve(1.0)
 with Dissolve(1.0)
 show mion_v002 fuan at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show mion_v002 fuan at inactive
 nao ''
 show nao_v002 normal at active
 show mion_v002 fuan at inactive
 nao ''
 show mion_v002 fuan at chara_shake_transform,active
 show nao_v002 normal at inactive
 mion ''
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.2
 pause 0.5
 show nao_v002 sinken at active
 show mion_v002 fuan at inactive
 nao ''
 hide mion_v002
 show shion_v002 fuan at mei_right
 with Dissolve(0.5)
 show shion_v002 fuan at active
 show nao_v002 sinken at inactive
 shion ''
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide nao_v002
 hide shion_v002
 hide fade with Dissolve(0.08333333333333333)
 show nao_v002 sinken at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show nao_v002 sinken at active
 nao ''
 camera at screenshake_transform
 pause 0.0
 show nao_v002 sinken at active
 nao ''
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show mion_v002 fuan at mei_right
 show shion_v002 normal at mei_left
 with Dissolve(0.5)
 show shion_v002 normal at active
 show mion_v002 fuan at inactive
 shion ''
 show mion_v002 fuan_close at active
 show shion_v002 normal at inactive
 mion ''
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao ''
 show nao_v002 normal_close at active
 nao ''
 hide nao_v002
 with Dissolve(0.2)
 show erika_v001 normal_close at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show erika_v001 normal_close at inactive
 nao ''
 show erika_v001 smile at active
 show nao_v002 normal at inactive
 erika ''
 camera at screenshake_transform
 pause 0.0
 show nao_v002 sinken at active
 show erika_v001 smile at inactive
 nao ''
 show nao_v002 normal at active
 show erika_v001 smile at inactive
 nao ''
 show erika_v001 normal at active
 show nao_v002 normal at inactive
 erika ''
 show nao_v002 normal_close at active
 show erika_v001 normal at inactive
 nao ''
 show nao_v002 normal at active
 show erika_v001 normal at inactive
 nao ''
 hide erika_v001
 hide nao_v002
 with Dissolve(0.2)
 camera at screenshake_transform
 pause 0.0
 narrator ''
 narrator ''
 show nao_v002 normal_close at mei_center
 with Dissolve(0.5)
 show nao_v002 normal_close at active
 nao ''
 hide nao_v002
 with Dissolve(0.2)
 show shion_v002 smile at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at chara_shake_transform,active
 show shion_v002 smile at inactive
 mion ''
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion ''
 hide mion_v002
 show erika_v001 smile at mei_right
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_215_heartgrow.wav'
 show erika_v001 smile at jumping_transform,active
 show shion_v002 smile at inactive
 erika ''
 hide shion_v002
 hide erika_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao ''
 show nao_v002 normal at active
 nao ''
 show nao_v002 normal_close at active
 nao ''
 show nao_v002 fuan at active
 nao ''
 hide nao_v002
 with Dissolve(0.2)
 narrator ''
 narrator ''
 narrator ''
 return