label chara442001_03:
 show black_background onlayer black
 $ event_store.current_event='chara442001'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara442001_03'
 $ persistent.menu_return='chara'
 camera:
  anchor (0.5, 0.5)
  pos (960, 540)
  zoom 1.0
  matrixcolor IdentityMatrix()
 pause 0.0
 scene
 stop music
 stop sound
 show expression 'images/bg/AdvBg_262.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_501_crow.wav'
 pause 1.0
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_512.png' as bg
 play music "<loop 2.36>audio/bgm/BGM_EVENT1.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show satoko_v002 fuan at mei_left
 show kazuho_v002 smile at mei_right
 with Dissolve(0.5)
 show kazuho_v002 smile at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "You've been waiting at the shrine... but are you guys okay?"
 show satoko_v002 fuan at inactive
 show kazuho_v002 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "You don't have to worry, I think. We gathered up the ingredients fast, and they said making it won't take very long either..."
 play audio 'audio/sfx/SE_536_up_stairs.wav'
 show satoko_v002 fuan at inactive
 show kazuho_v002 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Ah... it looks like Miyuki-chan and the others are here.'
 hide kazuho_v002
 hide satoko_v002
 with Dissolve(0.2)
 show miyuki_v002 smile at mei_center
 with Dissolve(0.5)
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Sorry for making you wait, Kazuho~!\nOh, Satoko met up with you too?'
 hide miyuki_v002
 with Dissolve(0.2)
 show satoko_v002 smile at mei_left
 with Dissolve(0.5)
 show satoko_v002 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Y-Yeah. ...Wow, that basket has a super nice smell coming from it...!'
 show rena_v002 smile at mei_right
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_577_ls_sanriokirakira.wav'
 show satoko_v002 smile at inactive
 show rena_v002 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Ahahaha, tadaaa! Because I made these churros~!'
 hide satoko_v002
 show kazuho_v002 smile_blush at mei_left
 with Dissolve(0.5)
 show rena_v002 smile at inactive
 show kazuho_v002 smile_blush at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Woah, cool! There's so many!"
 hide rena_v002
 show nao_v002 smile at mei_right
 with Dissolve(0.5)
 show kazuho_v002 smile_blush at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Rena-chan made a bunch so that we can all eat our fill.'
 hide kazuho_v002
 show miyuki_v002 smile at mei_left
 with Dissolve(0.5)
 show nao_v002 smile at inactive
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "The flavor is a bit different from what I know, but it's delicious in its own right!"
 show miyuki_v002 smile at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Naturally. Rena-chan made them, so how can they not be delicious?'
 hide miyuki_v002
 show satoko_v002 normal_close at mei_left
 with Dissolve(0.5)
 show nao_v002 smile at inactive
 show satoko_v002 normal_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "...It looks like I'll be able to get by with these."
 hide nao_v002
 show kazuho_v002 odoroki at mei_right
 with Dissolve(0.5)
 show satoko_v002 normal_close at inactive
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Huh...?'
 show kazuho_v002 odoroki at inactive
 show satoko_v002 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Nothing at all!\nNow, I do believe I've been eagerly waiting for this~!"
 hide satoko_v002
 hide kazuho_v002
 with Dissolve(0.2)
 call wipeout_routine
 call wipein_routine
 show mion_v002 smile at mei_left
 show hanyuu_v002 smile at mei_right
 with Dissolve(0.5)
 show hanyuu_v002 smile at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") '...Oh, Rena! Inside that basket... could it be...?'
 show mion_v002 smile at inactive
 show hanyuu_v002 smile at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Au au au! Are those... churros?!'
 hide mion_v002
 show rika_v002 smile at mei_left
 with Dissolve(0.5)
 show hanyuu_v002 smile at inactive
 show rika_v002 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Meep. There's a ton of sugar on it, so it looks really tasty."
 hide hanyuu_v002
 show rena_v002 smile at mei_right
 with Dissolve(0.5)
 show rika_v002 smile at inactive
 show rena_v002 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "I've already memorized the recipe, so I'll be making more tasty things for next month's screening party."
 hide rika_v002
 show hanyuu_v002 smile at mei_left
 with Dissolve(0.5)
 show rena_v002 smile at inactive
 show hanyuu_v002 smile at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Au au, these look good too! Please let me try a bite!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide rena_v002
 hide hanyuu_v002
 hide fade onlayer curtain
 show satoko_v002 sinken at mei_center
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_556_netdown.wav'
 show satoko_v002 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '...nn...'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide satoko_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show nao_v002 sinken at mei_left
 show rika_v002 odoroki at mei_right
 with Dissolve(0.5)
 show rika_v002 odoroki at inactive
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Ah, Satoko! Did you pull out some churros just now?!'
 show nao_v002 sinken at inactive
 show rika_v002 odoroki at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep. Where are you going, Satoko?'
 hide rika_v002
 hide nao_v002
 with Dissolve(0.2)
 show satoko_v002 smile at mei_center
 with Dissolve(0.5)
 show satoko_v002 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'J-Just going to wash my hands~!'
 play audio 'audio/sfx/SE_408_run.wav'
 hide satoko_v002
 with Dissolve(0.2)
 show kazuho_v002 fuan at mei_right
 show rika_v002 normal at mei_left
 with Dissolve(0.5)
 show rika_v002 normal at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "But with those churros? ...Ah, she's already gone?"
 show kazuho_v002 fuan at inactive
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Satoko...?'
 hide rika_v002
 hide kazuho_v002
 with Dissolve(0.2)
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_244.png' as bg
 stop music fadeout 0.5
 hide fade onlayer curtain
 with Dissolve(1.0)
 show satoko_v002 normal at mei_center
 with Dissolve(0.5)
 show satoko_v002 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Haaah, haaah... I brought them here... um, Eua-san?'
 play audio 'audio/sfx/SE_539_warp.wav'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_220.png' as bg
 play music "<loop 1.87>audio/bgm/BGM_EVENT6.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show satoko_v002 odoroki at active
 show satoko_v002 odoroki at jumping_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '...Hya-?!'
 hide satoko_v002
 with Dissolve(0.2)
 show eua_v001 normal at mei_left
 show satoko_v002 odoroki at mei_right
 with Dissolve(0.5)
 show satoko_v002 odoroki at inactive
 show eua_v001 normal at active
 Character('Eua',ctc="ctcArrow", ctc_position="fixed") 'You called, child of man?'
 show eua_v001 normal at inactive
 show satoko_v002 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'U-... Um, for the sweets as requested for your spectating stuff, I brought you churros.'
 show eua_v001 normal at inactive
 show satoko_v002 odoroki at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '...Wait, huh? The churros aren’t here...?!'
 show satoko_v002 odoroki at inactive
 show eua_v001 smile at active
 Character('Eua',ctc="ctcArrow", ctc_position="fixed") 'Good, Satoko. Now, present me your head.'
 show eua_v001 smile at inactive
 show satoko_v002 odoroki at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Huh...?'
 hide satoko_v002
 hide eua_v001
 with Dissolve(0.2)
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/card/Card_442001.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'L-Like this...?'
 Character('Eua',ctc="ctcArrow", ctc_position="fixed") 'That is right. Just like that; do not move.'
 Character('Eua',ctc="ctcArrow", ctc_position="fixed") 'Hoh, I see... well, well, well.'
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Do you see it now?'
 Character('Eua',ctc="ctcArrow", ctc_position="fixed") 'Mhm. I am receiving it from Satoko’s memories.'
 Character('Eua',ctc="ctcArrow", ctc_position="fixed") 'I see... these sweets do seem quite appropriate for theatergoing. This is not so bad...'
 Character('Eua',ctc="ctcArrow", ctc_position="fixed") '...Good, now lift your head.'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_220.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 show eua_v001 smile at mei_left
 show satoko_v002 fuan at mei_right
 with Dissolve(0.5)
 show satoko_v002 fuan at inactive
 show eua_v001 smile at active
 Character('Eua',ctc="ctcArrow", ctc_position="fixed") 'Splendidly done, child of man.\nI shall accept this as a success. I lend you my thanks.'
 show eua_v001 smile at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Umm... so you eat it like that?'
 show satoko_v002 fuan at inactive
 show eua_v001 smile at active
 Character('Eua',ctc="ctcArrow", ctc_position="fixed") 'Correct. I have already learned the stuff of what {b}churros{/b} are.'
 show eua_v001 smile at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "...But I still haven't had one to eat, though?"
 show satoko_v002 fuan at inactive
 show eua_v001 smile at active
 Character('Eua',ctc="ctcArrow", ctc_position="fixed") 'Will you not eat some afterwards?\nThe fact that they will already be eaten has been shared between us a few seconds in advance.'
 show eua_v001 smile at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'I don’t understand very well... but if you don’t actually eat it, wouldn’t you be unable to grasp its true deliciousness?'
 show satoko_v002 fuan at inactive
 show eua_v001 smile at active
 Character('Eua',ctc="ctcArrow", ctc_position="fixed") 'Worry over such trivialities is unnecessary. With this fact absolutely certain to come, the difference between the future and now would be slim to none.'
 show eua_v001 smile at inactive
 show satoko_v002 fuan_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '(...Is that actually true......?)'
 show satoko_v002 fuan_close at inactive
 show eua_v001 smile at active
 Character('Eua',ctc="ctcArrow", ctc_position="fixed") 'Now, return... to your broken “World” you so desire.'
 show eua_v001 smile at inactive
 show satoko_v002 odoroki at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Huh...?'
 hide satoko_v002
 hide eua_v001
 with Dissolve(0.2)
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_244.png' as bg
 stop music fadeout 0.5
 hide fade onlayer curtain
 with Dissolve(1.0)
 show hanyuu_v002 odoroki at mei_left
 show rika_v002 odoroki at mei_right
 with Dissolve(0.5)
 show rika_v002 odoroki at inactive
 show hanyuu_v002 odoroki at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Ah-... Satoko is over here!'
 show hanyuu_v002 odoroki at inactive
 show rika_v002 odoroki at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Satokoo...!'
 hide rika_v002
 hide hanyuu_v002
 with Dissolve(0.2)
 show satoko_v002 odoroki at mei_center
 with Dissolve(0.5)
 show satoko_v002 odoroki at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Rika... Hanyuu-san? What could have happened for you to have such rushed looks on your faces?'
 hide satoko_v002
 with Dissolve(0.2)
 show rika_v002 fuan at mei_right
 show hanyuu_v002 fuan at mei_left
 with Dissolve(0.5)
 show hanyuu_v002 fuan at inactive
 show rika_v002 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep. That’s my line. Why were you over here?'
 show rika_v002 fuan at inactive
 show hanyuu_v002 fuan at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Au au... You suddenly disappeared, and everyone got worried~.'
 hide hanyuu_v002
 hide rika_v002
 with Dissolve(0.2)
 show satoko_v002 fuan at mei_center
 with Dissolve(0.5)
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Huh? Um, it’s not like I had... any reason to go anywhere... wh-what...?'
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '...Why am I standing out here with some treat I’ve never seen before in my hand...?'
 hide satoko_v002
 with Dissolve(0.2)
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_220.png' as bg
 play music "<loop 6.86>audio/bgm/BGM_OYASHIRO.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show eua_v001 smile at mei_center
 with Dissolve(0.5)
 show eua_v001 smile at active
 Character('Eua',ctc="ctcArrow", ctc_position="fixed") 'Now this is how you kill time... is it not it the same for {b}you{/b}?'
 show eua_v001 smile at active
 Character('Eua',ctc="ctcArrow", ctc_position="fixed") 'I understand how you are always watching. And yet, to my lament, your form is not perceivable... no, you are unable to be perceived as a {b}shattered being{/b}.'
 show eua_v001 smile_close at active
 Character('Eua',ctc="ctcArrow", ctc_position="fixed") 'Do not fret. I approached you to stave off my boredom for just a little bit of time. This is not my game board.'
 show eua_v001 futeki at active
 Character('Eua',ctc="ctcArrow", ctc_position="fixed") 'Well, it is not your game board either, is it...? *cackle*cackle*cackle*!!'
 show eua_v001 odoroki at active
 Character('Eua',ctc="ctcArrow", ctc_position="fixed") '...Oh, have I angered you? I had felt the color of your presence sticking out. Even without seeing your form, your presence is truly easy to realize.'
 show eua_v001 smile at active
 Character('Eua',ctc="ctcArrow", ctc_position="fixed") 'Not a worry; I suppose I will be taking my leave soon... or would you rather I hand over some payment for spectating...?'
 show eua_v001 smile at active
 Character('Eua',ctc="ctcArrow", ctc_position="fixed") 'What are you saying? Precisely because you have already obtained the possibility of my existence appearing as a fragment, you were able to observe me manifesting this way?'
 show eua_v001 smile at active
 Character('Eua',ctc="ctcArrow", ctc_position="fixed") 'Then is payment for it not enough? ...Or is the amount lacking? You truly are a greedy one. If that is the case, then it would be marvellous if you were to remember this parting gift of mine ahead of time.'
 show eua_v001 normal at active
 Character('Eua',ctc="ctcArrow", ctc_position="fixed") '------What you are dreaming is not a dream.\nThis is a fact that lies beyond all possibilities.'
 show eua_v001 smile at active
 Character('Eua',ctc="ctcArrow", ctc_position="fixed") 'Hmm... I am warming up to this. I shall continue.'
 show eua_v001 normal at active
 Character('Eua',ctc="ctcArrow", ctc_position="fixed") 'Under the influence of your proximity, the amount of people who will end up dreaming of different possibilities will slowly but surely increase.'
 show eua_v001 smile at active
 Character('Eua',ctc="ctcArrow", ctc_position="fixed") '*chuckle*... Are you frustrated? That is right.\nI do have to affirm, it would have been possible to dismiss the dream as simply a dream.'
 show eua_v001 smile at active
 Character('Eua',ctc="ctcArrow", ctc_position="fixed") 'However, that margin of opportunity has already vanished for you. This is already a fact you must face.'
 show eua_v001 smile at active
 Character('Eua',ctc="ctcArrow", ctc_position="fixed") 'The reality is that with you nearby, the probability of those suffering from nightmares will also increase...'
 show eua_v001 smile at active
 Character('Eua',ctc="ctcArrow", ctc_position="fixed") "Does the thought of someone close to you suffering frustrate you? If so, wouldn't it be better if you parted from them?"
 show eua_v001 smile at active
 Character('Eua',ctc="ctcArrow", ctc_position="fixed") 'Ah, really? It was impossible for you to part from them, was it? ...My, my, how troublesome this has become.'
 show eua_v001 normal at active
 Character('Eua',ctc="ctcArrow", ctc_position="fixed") 'Nevertheless, because you are nearby, everyone shall suffer! And on the other hand, if you break away from society, no one will be saved!'
 show eua_v001 futeki at active
 Character('Eua',ctc="ctcArrow", ctc_position="fixed") '*cackle*cackle*! You pain me, {b}shattered being{/b}! Nonetheless, that was the reason that I went through the trouble of coming to you!'
 show eua_v001 smile at active
 Character('Eua',ctc="ctcArrow", ctc_position="fixed") 'Well, at best, I hope you can struggle about.\nShould there arise another opportunity, you ought to thoroughly appreciate it.'
 show eua_v001 smile at active
 Character('Eua',ctc="ctcArrow", ctc_position="fixed") 'Haha, haha... hahahahahahahahahaha!!'
 call chapter_end
 
 $ persistent.chara442001_done = True
 return