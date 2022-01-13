label chara472001_03:
 show black_background onlayer black
 $ event_store.current_event='chara472001'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara472001_03'
 $ persistent.menu_return='chara'
 camera:
  anchor (0.5, 0.5)
  pos (960, 540)
 scene
 stop music
 stop sound
 show expression 'images/bg/AdvBg_103.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 show nao_v001 sinken at mei_center
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_528_unfold_cloth.wav'
 camera at screenshake_transform
 pause 0.0
 show nao_v001 sinken at active
 nao 'Wait!'
 hide nao_v001
 with Dissolve(0.2)
 play music "<loop 0>audio/bgm/BGM_HOME_COLLAB2.ogg"
 show kazuho_v001 normal at mei_left
 show miyuki_v001 normal at mei_right
 with Dissolve(0.5)
 show miyuki_v001 normal at active
 show kazuho_v001 normal at inactive
 miyuki "Hm? What's up, Nao?"
 show kazuho_v001 normal at active
 show miyuki_v001 normal at inactive
 kazuho 'Have you woken up from your nap?'
 hide miyuki_v001
 show nao_v001 normal_close at mei_right
 with Dissolve(0.5)
 show nao_v001 normal_close at active
 show kazuho_v001 normal at inactive
 nao "Yeah... I'm up."
 show kazuho_v001 fuan at active
 show nao_v001 normal_close at inactive
 kazuho "What's up? Still sleepy?"
 show nao_v001 fuan at active
 show kazuho_v001 fuan at inactive
 nao "I don't think that's it... but I feel like I should have slept just a little more."
 show nao_v001 smile_close at active
 show kazuho_v001 fuan at inactive
 nao 'It feels like I was having a super fun dream.'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide kazuho_v001
 hide nao_v001
 with Dissolve(0.2)
 stop sound
 show expression 'images/bg/AdvBg_2190.png' as bg
 pause 1.0
 play music "<loop 0>audio/bgm/BGM_QUEST6_COLLAB2.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show beatrice_v001 normal_close at mei_right
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show beatrice_v001 normal_close at inactive
 dlanor 'People do not exist for the LAW. The law exists for PEOPLE.'
 show dlanor_v001 normal at active
 show beatrice_v001 normal_close at inactive
 dlanor 'Nevertheless, there are cases borne from villains hurting others through abusing the power of laws that protect PEOPLE.'
 show dlanor_v001 normal at active
 show beatrice_v001 normal_close at inactive
 dlanor '...With rules that are made to protect, there is always someone on the other end who has already weaponized it against someone ELSE.'
 show beatrice_v001 normal at active
 show dlanor_v001 normal at inactive
 beatrice "But if Lady Dlanor and her followers hadn't continued to protect others, mystery itself as a genre would have likely crumbled apart."
 show dlanor_v001 fuan_close at active
 show beatrice_v001 normal at inactive
 dlanor 'AGREED... Although it is true that there are also those who think "Knox\'s Decalogue" serves to constrict the mystery GENRE.'
 show beatrice_v001 normal_close at active
 show dlanor_v001 fuan_close at inactive
 beatrice 'That is true. However, since there are definite rules to mystery, the genre can continue to exist in the time of that lost child.'
 show beatrice_v001 normal at active
 show dlanor_v001 fuan_close at inactive
 beatrice 'I suppose mystery is a genre that will temporarily wane, but will never completely blow out.'
 show beatrice_v001 smile at active
 show dlanor_v001 fuan_close at inactive
 beatrice '...As proof of that, that girl will surely gets her hands on a mystery novel once she awakens. Perhaps then we shall reunite.'
 show dlanor_v001 normal at active
 show beatrice_v001 smile at inactive
 dlanor 'But then... what about Nao forgetting that she had ever been HERE?'
 show beatrice_v001 normal_close at active
 show dlanor_v001 normal at inactive
 beatrice "Ah, I guess she is forgetting each time, isn't she? And even if she does remember, she'll see it as a dream that has already ended."
 show beatrice_v001 normal at active
 show dlanor_v001 normal at inactive
 beatrice 'Even so, her feelings of amusement will strike at the depths of her heart.'
 show beatrice_v001 smile at active
 show dlanor_v001 normal at inactive
 beatrice 'The lost child that found "Knox\'s Decalogue" amusing will surely reach her hands out to mystery.'
 show dlanor_v001 normal_close at active
 show beatrice_v001 smile at inactive
 dlanor 'I hope that it does become SO... Now, I think I will again take my LEAVE.'
 show beatrice_v001 smile at active
 show dlanor_v001 normal_close at inactive
 beatrice 'Are you going out to meet her?'
 show dlanor_v001 normal at active
 show beatrice_v001 smile at inactive
 dlanor 'YES. Around now, I think she would be lazing around in her ROOM. ...Miss Beatrice?'
 show beatrice_v001 normal at active
 show dlanor_v001 normal at inactive
 beatrice 'Yes?'
 show dlanor_v001 smile at active
 show beatrice_v001 normal at inactive
 dlanor 'Those leftover COOKIES, may I take them back with ME?'
 stop music fadeout 0.5
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide beatrice_v001
 hide dlanor_v001
 with Dissolve(0.2)
 stop sound
 show expression 'images/bg/AdvBg_2180.png' as bg
 play music "<loop 0>audio/bgm/BGM_QUEST5_COLLAB2.ogg"
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 hide fade onlayer curtain
 with Dissolve(1.0)
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show erika_v001 odoroki_close at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 odoroki_close at active
 erika "Uuuuuuu, for me to have fallen for a FAKE version of my master in Hinamizawa; it can't be...!"
 show erika_v001 odoroki_close at chara_shake_transform,active
 erika "Uuuu, I won't ever make that mistake again! Uuuu... WAAAAHHhhHHHHAHHH...!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show erika_v001 odoroki_close at mei_right
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show erika_v001 odoroki_close at inactive
 dlanor 'Lady ERIKA.'
 show erika_v001 sinken at active
 show dlanor_v001 normal at inactive
 erika "...Is that you, Dlanor? What is it? Have you come to laugh at me after I've received a scolding from my master?"
 show dlanor_v001 normal_close at active
 show erika_v001 sinken at inactive
 dlanor "Not at ALL. I wouldn't do something like THAT."
 show erika_v001 sinken at active
 show dlanor_v001 normal_close at inactive
 erika 'THEN WHY-... oh, what are those cookies there?'
 show dlanor_v001 smile at active
 show erika_v001 sinken at inactive
 dlanor "They are for us to HAVE. If you'd like, we can eat them TOGETHER."
 show erika_v001 sinken_close at active
 show dlanor_v001 smile at inactive
 erika "...Then I'll... have some."
 show erika_v001 normal at active
 show dlanor_v001 smile at inactive
 erika "Mm... they aren't bad. A little too sweet to be nutritious for my brain, though."
 show dlanor_v001 smile_close at active
 show erika_v001 normal at inactive
 dlanor "If you think it's tasty, then I'm HAPPY."
 show erika_v001 normal at active
 show dlanor_v001 smile_close at inactive
 erika "...You're in a really good mood, huh? Has something nice happened?"
 show dlanor_v001 smile at active
 show erika_v001 normal at inactive
 dlanor 'YES. We may have gotten a new mystery READER.'
 show erika_v001 normal at active
 show dlanor_v001 smile at inactive
 erika "Hmm? Isn't that nice. I'll also warmly welcome someone new who is capable of talking about mystery."
 show erika_v001 futeki at active
 show dlanor_v001 smile at inactive
 erika "Even just dabbling in this idea a little, I'm getting interested, I find. I'm looking forward to ripping this person's heart in half..."
 show dlanor_v001 normal at active
 show erika_v001 futeki at inactive
 dlanor 'This opponent might not be so easily BREAKABLE.'
 show erika_v001 normal at active
 show dlanor_v001 normal at inactive
 erika "Woah... what unusual confidence. I'm looking forward to this battle with them now since you seem so sure about it."
 show dlanor_v001 smile at active
 show erika_v001 normal at inactive
 dlanor 'YES. ...I am also looking forward to IT.'
 call chapter_end
 return