label chara032009_02:
 show black_background onlayer black
 $ event_store.current_event='chara032009'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara032009_02'
 stop sound
 scene #000
 play music 'audio/bgm/BGM_EVENT6.ogg'
 show expression 'images/bg/AdvBg_2190.png' as bg
 with Dissolve(1.0)
 show beatrice_v001 smile at mei_right
 show nao_v002 odoroki at mei_left
 with Dissolve(0.5)
 show nao_v002 odoroki at active
 show beatrice_v001 smile at inactive
 nao 'Huh...?'
 show beatrice_v001 smile at active
 show nao_v002 odoroki at inactive
 beatrice 'Long time no see, Nao. More than anything, you seem to be in good spirits to have returned there.'
 show nao_v002 fuan at active
 show beatrice_v001 smile at inactive
 nao "Wh-who are you... wait, I shouldn't be asking that!"
 show nao_v002 sinken at active
 show beatrice_v001 smile at inactive
 nao 'I... I know about you...? The Golden Witch, Beatrice...?!'
 show beatrice_v001 smile at active
 show nao_v002 sinken at inactive
 beatrice 'Hoh, you still remember my name?'
 show nao_v002 fuan at nod_transform,active
 show beatrice_v001 smile at inactive
 nao 'Yes. Rather, I less understand why I had forgotten your name up until now. You give off an intense personal experience even considering.'
 show beatrice_v001 normal_close at active
 show nao_v002 fuan at inactive
 beatrice '...I see. Magic was cast on you, wiping all knowledge of you and I from your memory?'
 show nao_v002 odoroki at jump_transform,active
 show beatrice_v001 normal_close at inactive
 nao '...Huh? So then, my memory is being tampered with by someone...?'
 show beatrice_v001 smile at active
 show nao_v002 odoroki at inactive
 beatrice "Don't make such a hateful face. The alterations on your memory will not do you any harm; I suppose they are steps taken to protect it instead."
 show beatrice_v001 smile at active
 show nao_v002 odoroki at inactive
 beatrice 'Since the game this time is irregular, the Game Master figured it would be good to continue to hold onto your memories relating to me.'
 show beatrice_v001 futeki_close at active
 show nao_v002 odoroki at inactive
 beatrice 'Hmm, yes... from me inviting you here, it seems that effect has worn off. *cackle*cackle*cackle*cackle*cackle*!!!'
 show nao_v002 normal at active
 show beatrice_v001 futeki_close at inactive
 nao '...Ehh, I kind of wish that it had made me continue to forget about you.'
 show nao_v002 normal_close at active
 show beatrice_v001 futeki_close at inactive
 nao "Clearly, the battle between Beatrice and Erika-san made my head spin, though... I'm different from that sort of affair."
 show beatrice_v001 futeki at updown_shake_transform,active
 show nao_v002 normal_close at inactive
 beatrice "*cackle*cackle*cackle*... you don't have to say it. That hesitant behavior... I'm gradually growing an interest in it. "
 show nao_v002 normal at active
 show beatrice_v001 futeki at inactive
 nao '... Anyway, what on earth could you want from me today? Could it be that another logic battle is starting up?'
 show beatrice_v001 smile at active
 show nao_v002 normal at inactive
 beatrice 'Do not fret; such caution is unnecessary. I have invited you as my boredom has gotten slightly out of hand.'
 show beatrice_v001 smile at active
 show nao_v002 normal at inactive
 beatrice 'What I need, is something to kill time.'
 show nao_v002 fuan at active
 show beatrice_v001 smile at inactive
 nao 'Killing time... huh? What an incomprehensible existence witches are, calling me up to places like this just for that one reason.'
 show beatrice_v001 futeki at active
 show nao_v002 fuan at inactive
 beatrice '*cackle*cackle*cackle*, a reasonable thought! Boredom to witches is a poison... you are not just important to me, you are {i}extremely{/i} valuable.'
 show beatrice_v001 normal at active
 show nao_v002 fuan at inactive
 beatrice 'Aside from that... Nao, are you up to spectate a story I have prepared?'
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao 'Spectating, a story...?'
 show beatrice_v001 normal_close at active
 show nao_v002 normal at inactive
 beatrice 'Mhm. Up until now, I have set up numerous stages on Rokkenjima as game boards. This time will for sure be a different locked-room murder incident.'
 show beatrice_v001 smile at active
 show nao_v002 normal at inactive
 beatrice '...*cackle*cackle*cackle*. My games are entertaining. Not only do I observe my pieces, for I can even move them through the gameboard.'
 show nao_v002 odoroki at active
 show beatrice_v001 smile at inactive
 nao "Rokkenjima...? I've heard that name somewhere... ah-?!"
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide beatrice_v001
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 show nao_v002 sinaken at mei_center
 with Dissolve(0.08333333333333333)
 show nao_v002 sinken at active
 nao "That's right, I just remembered...! Around October of 1986, a mysterious explosion occurred on one of the islands in the Izu Archipelago..."
 show nao_v002 sinken at active
 nao 'The relatives of a wealthy family had gathered for a meeting on a small island where a massive amount of them lost their lives; the name of it was clearly "Rokkenjima" ... uh...'
 show nao_v002 normal at active
 nao "...I see. That island was a certain fateful destination for them, wasn't it?"
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show beatrice_v001 smile at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show beatrice_v001 smile at inactive
 nao 'Then... the game board that you made, how would one play on it, I wonder?'
 show beatrice_v001 smile at active
 show nao_v002 normal at inactive
 beatrice 'Oooh, then I have it you would enjoy my game?'
 show nao_v002 smile at nod_transform,active
 show beatrice_v001 smile at inactive
 nao "Yes. I like games regardless of what they are... So, what are the rules? What's the goal?"
 stop music fadeout 0.5
 show beatrice_v001 futeki at active
 show nao_v002 smile at inactive
 beatrice 'That is, well... look here.'
 play music 'audio/bgm/BGM_EVENT5.ogg'
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide beatrice_v001
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 show nao_v002 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_230_charge.wav'
 show nao_v002 odoroki at chara_shake_transform,active
 nao "Huh-, wai-, what is this huge hole...! I'm, I'm fal-... kyaaaaaaaaaaaa-!!"
 show nao_v002 odoroki
 show nao_v002 odoroki:
  linear 0.5 pos (960,2280)
 pause 0.5
 show black_cover as fade with Dissolve(1.0)
 hide nao_v002
 with Dissolve(0.2)
 stop sound
 scene black_cover
 show expression 'images/bg/AdvBg_2201.png' as bg
 with Dissolve(1.0)
 show nao_v014 odoroki at mei_center
 with Dissolve(0.5)
 show nao_v014 odoroki at active
 nao 'Kya... uh, huh?'
 show nao_v014 fuan at active
 nao "I'm, I'm floating...?"
 play music 'audio/bgm/BGM_QUEST.ogg'
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide nao_v014
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show beatrice_v001 smile at mei_right
 show nao_v014 fuan at mei_left
 with Dissolve(0.5)
 show beatrice_v001 smile at active
 show nao_v014 fuan at inactive
 beatrice "You currently are a soldier of the Dragon King Pendragon-- as a host for the Chiester Sisters. Even flying through the sky should be as easy as twisting a baby's hand for you now."
 show nao_v014 fuan at active
 show beatrice_v001 smile at inactive
 nao '...Even Beatrice is floating normally. Just how are you flying?'
 show beatrice_v001 futeki at active
 show nao_v014 fuan at inactive
 beatrice '*cackle*cackle*cackle*... I am a witch! Something like flying through the sky is nothing strange.'
 show nao_v014 normal at active
 show beatrice_v001 futeki at inactive
 nao 'So, witches flew even without brooms... hup!'
 show black_cover as fade with Dissolve(1.0)
 stop sound
 scene black_cover
 show expression 'images/bg/AdvBg_2220.png' as bg
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_232_landing.wav'
 nao 'Alright, I landed down here in the courtyard, but what do I do from here?'
 beatrice "Now, you wait for the boat from Niijima. You are being taken to Battler Ushiromiya's location."
 beatrice "There, from that man's shoes, you can witness the events that occurred on Rokkenjima with your own eyes."
 nao 'I see. In this man "Battler\'s" viewpoint, you can mobilize him on top of the gameboard, right?'
 beatrice "That's right. Having such sharpness and frankness is key. ...Also, Nao, that uniform that you are wearing is battle furniture that has signed a contract to me."
 nao 'Huh...?'
 beatrice "If you consider that, you also become my furniture... it can be considered that way, don't you think?"
 nao "If it's said like that, it makes me want to take it off..."
 beatrice '*cackle*cackle*cackle*, I jest, I jest. Now look ahead; the game will begin from here.'
 nao 'Huh-...? Wh-, what should I do?'
 beatrice "Anything is fine. Whenever you're ready, step up right behind Battler."
 beatrice "Enjoy the close-up seat in Battler's fight against me."
 nao "I'm not playing the game? No matter how you say it, whoever plays is really just watching him through his eyes...?"
 beatrice "This is Battler's and my game; therefore, you are not the one who can be called my competition."
 beatrice 'Still, the ones spectating, even up until now, are the Witch of Miracles and the Witch of Certainty. With a little change of plans, I still wanted to hear your thoughts.'
 nao "...If it's a game, I think me playing myself is more fun."
 beatrice 'Are you unsatisfied?'
 nao "Yeah, kind of... It's just, I didn't know of any other way of playing a game than playing it yourself."
 nao 'But, well... right. If that type of enjoyment exists, then I will have to try it out.'
 beatrice '*cackle*cackle*cackle*... This open-minded and frank attitude is an irreplaceable element to enjoying the game. Not bad at all.'
 nao "I'll accept those words of praise. Umm, do people normally wait for the end of the story?"
 show black_cover as fade with Dissolve(1.0)
 hide beatrice_v001
 hide nao_v014
 with Dissolve(0.2)
 stop sound
 scene black_cover
 show expression 'images/card/Card_032009.png' as bg
 with Dissolve(1.0)
 nao 'Uuum, *ahem*.'
 nao "Nao Houtani... rightfully spectating the witch Beatrice's game board."
 nao 'Please, if you would kindly begin...'
 show black_cover as fade with Dissolve(1.0)
 stop sound
 scene black_cover
 show expression 'images/bg/AdvBg_2220.png' as bg
 with Dissolve(1.0)
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide fade with Dissolve(0.08333333333333333)
 show beatrice_v001 futeki at mei_center
 with Dissolve(0.08333333333333333)
 show beatrice_v001 futeki at updown_shake_transform,active
 beatrice "Hu, hahahahahahahaha... Once you hear Battler's greeting, it begins! How this is so incredibly entertaining!"
 show beatrice_v001 futeki_close at active
 beatrice 'However, you are unrefined, Nao. If you were Maria, you would be flying around with such vigor. *cackle*cackle*cackle*!'
 show beatrice_v001 smile at active
 beatrice "Oh, look, do not make such a face. The story is already beginning. At best, don't be shaken off. "
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide beatrice_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show nao_v014 fuan at mei_left
 show beatrice_v001 smile at mei_right
 with Dissolve(0.5)
 show nao_v014 fuan at active
 show beatrice_v001 smile at inactive
 nao 'Thank you, w-wait a minute. Just what will I be "shaken off" from?'
 show beatrice_v001 futeki at active
 show nao_v014 fuan at inactive
 beatrice 'Of course, from my game boooard!'
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide nao_v014
 hide beatrice_v001
 hide fade with Dissolve(0.08333333333333333)
 show nao_v014 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_611_ls_wind.wav'
 camera at screenshake_transform
 pause 0.0
 show nao_v014 odoroki at active
 nao "I-I didn't know there was a type of vehicle like tha-... aaaaaaaaaaat?!"
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide nao_v014
 hide fade with Dissolve(0.08333333333333333)
 show beatrice_v001 futeki at mei_center
 with Dissolve(0.08333333333333333)
 show beatrice_v001 futeki at updown_shake_transform,active
 beatrice "Kuhahhahhahhahha! A great scream that tugs on the heartstrings! Let's enjoy this as much as possibleeeeeeeee!!"
 call chapter_end
 jump chara032009_03