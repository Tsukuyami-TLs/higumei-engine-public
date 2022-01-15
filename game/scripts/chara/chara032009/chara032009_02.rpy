label chara032009_02:
 show black_background onlayer black
 $ event_store.current_event='chara032009'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara032009_02'
 $ persistent.menu_return='chara'
 camera:
  anchor (0.5, 0.5)
  pos (960, 540)
  matrixcolor IdentityMatrix()
 scene
 stop music
 stop sound
 show expression 'images/bg/AdvBg_2190.png' as bg
 play music "<loop 1.87>audio/bgm/BGM_EVENT6.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show beatrice_v001 smile at mei_right
 show nao_v002 odoroki at mei_left
 with Dissolve(0.5)
 show nao_v002 odoroki at active
 show beatrice_v001 smile at inactive
 nao 'Huh...?'
 show beatrice_v001 smile at active
 show nao_v002 odoroki at inactive
 beatrice 'Long time no see, Nao. You seem to be in good spirits after returning home from your trip.'
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
 nao "Yes. Rather, I don't quite understand why I had forgotten about you up until now. You gave me a strong impression after all..."
 show beatrice_v001 normal_close at active
 show nao_v002 fuan at inactive
 beatrice '...I see. Magic was cast on you, wiping all knowledge of myself from your memory.'
 show nao_v002 odoroki at jump_transform,active
 show beatrice_v001 normal_close at inactive
 nao '...Huh? So then, my memory is being tampered with by someone...?'
 show beatrice_v001 smile at active
 show nao_v002 odoroki at inactive
 beatrice "Don't make such a sour face. The alterations on your memory were not meant to harm you, but measures taken to protect you."
 show beatrice_v001 smile at active
 show nao_v002 odoroki at inactive
 beatrice 'Since the game was irregular, the Game Master figured it would be a good idea to hold onto your memories relating to me.'
 show beatrice_v001 futeki_close at active
 show nao_v002 odoroki at inactive
 beatrice 'Hmm, yes... by inviting you here, it seems that effect has worn off. *cackle*cackle*cackle*cackle*cackle*!!!'
 show nao_v002 normal at active
 show beatrice_v001 futeki_close at inactive
 nao "...Ehh, I kind of wish that I hadn't forgotten about you in the first place, though."
 show nao_v002 normal_close at active
 show beatrice_v001 futeki_close at inactive
 nao "The battle between Beatrice and Erika-san certainly gave me a headache... but it's not going to change who I am."
 show beatrice_v001 futeki at updown_shake_transform,active
 show nao_v002 normal_close at inactive
 beatrice "*cackle*cackle*cackle*... you said it. \nThat headstrong attitude... I'm liking it more and more. "
 show nao_v002 normal at active
 show beatrice_v001 futeki at inactive
 nao '...Anyways, what could you possibly want from me today? Could it be that another logic battle is starting up?'
 show beatrice_v001 smile at active
 show nao_v002 normal at inactive
 beatrice 'Do not worry, as such caution is unnecessary. I have merely invited you as my boredom has gotten slightly out of hand.'
 show beatrice_v001 smile at active
 show nao_v002 normal at inactive
 beatrice 'What I need, is something to kill time.'
 show nao_v002 fuan at active
 show beatrice_v001 smile at inactive
 nao 'Killing time... huh? What an incomprehensible existence witches are, calling me to places like this just for that reason.'
 show beatrice_v001 futeki at active
 show nao_v002 fuan at inactive
 beatrice '*cackle*cackle*cackle*, a reasonable thought! Boredom to witches is a poison... you are not just important to me, you are {i}extremely{/i} valuable.'
 show beatrice_v001 normal at active
 show nao_v002 fuan at inactive
 beatrice 'Aside from that... Nao, are you up to spectate a story that I have prepared?'
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao 'Spectate... a story...?'
 show beatrice_v001 normal_close at active
 show nao_v002 normal at inactive
 beatrice 'Mhm. Up until now, I have set up numerous stages on Rokkenjima as game boards. Although this time will be a different locked-room murder incident.'
 show beatrice_v001 smile at active
 show nao_v002 normal at inactive
 beatrice '...*cackle*cackle*cackle*. My games are entertaining. Not only do I watch my pieces; I move them through the gameboard as well.'
 show nao_v002 odoroki at active
 show beatrice_v001 smile at inactive
 nao "Rokkenjima...? I've heard that name somewhere... ah-?!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide beatrice_v001
 hide nao_v002
 hide fade onlayer curtain
 show nao_v002 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show nao_v002 sinken at active
 nao "That's right, I just remembered...! Around October of 1986, a mysterious explosion occurred on one of the islands in the Izu Archipelago..."
 show nao_v002 sinken at active
 nao 'The relatives of a wealthy family had gathered for a meeting on a small island where most of them lost their lives. The name of it was certainly "Rokkenjima"... ah...'
 show nao_v002 normal at active
 nao "...I see. That island was a fateful place for them, wasn't it?"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show beatrice_v001 smile at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show beatrice_v001 smile at inactive
 nao 'Then... the game board that you made, how would one play on it, I wonder?'
 show beatrice_v001 smile at active
 show nao_v002 normal at inactive
 beatrice 'Oooh, then I take it you would enjoy my game?'
 show nao_v002 smile at nod_transform,active
 show beatrice_v001 smile at inactive
 nao "Yeah. I like games regardless of what they are... So, what are the rules? What's the goal?"
 stop music fadeout 0.5
 show beatrice_v001 futeki at active
 show nao_v002 smile at inactive
 beatrice 'That is, well... look here.'
 play music "<loop 5.836>audio/bgm/BGM_EVENT5.ogg"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide beatrice_v001
 hide nao_v002
 hide fade onlayer curtain
 show nao_v002 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_230_charge.wav'
 show nao_v002 odoroki at chara_shake_transform,active
 nao "Huh-, wa-, what is this huge hole...?! I'm, I'm fal-... kyaaaaaaaaaaaa-!!"
 show nao_v002 odoroki
 show nao_v002 odoroki:
  linear 0.5 pos (960,2280)
 pause 0.5
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide nao_v002
 with Dissolve(0.2)
 stop sound
 show expression 'images/bg/AdvBg_2201.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 show nao_v014 odoroki at mei_center
 with Dissolve(0.5)
 show nao_v014 odoroki at active
 nao 'Kya... uh... huh?'
 show nao_v014 fuan at active
 nao "I'm, I'm floating...?"
 play music "<loop 3.16>audio/bgm/BGM_QUEST.ogg"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide nao_v014
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show beatrice_v001 smile at mei_right
 show nao_v014 fuan at mei_left
 with Dissolve(0.5)
 show beatrice_v001 smile at active
 show nao_v014 fuan at inactive
 beatrice 'Currently, you are a soldier of the Dragon King Pendragon-- as a representative of the Chiester Sisters. Even flying through the sky should be as easy as taking candy from a baby for you now.'
 show nao_v014 fuan at active
 show beatrice_v001 smile at inactive
 nao '...Even Beatrice is floating normally. What are you using to fly?'
 show beatrice_v001 futeki at active
 show nao_v014 fuan at inactive
 beatrice '*cackle*cackle*cackle*... I am a witch! Something like me flying through the sky is nothing strange.'
 show nao_v014 normal at active
 show beatrice_v001 futeki at inactive
 nao 'So, witches could fly even without brooms... hup!'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_2220.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_232_landing.wav'
 show nao_v014 normal at active
 show beatrice_v001 futeki at inactive
 nao 'Alright, I landed down here in the courtyard, but what do I do from here?'
 show beatrice_v001 normal at active
 show nao_v014 normal at inactive
 beatrice "Now, you wait for the boat from Niijima. You are being taken to Battler Ushiromiya's location."
 show beatrice_v001 normal at active
 show nao_v014 normal at inactive
 beatrice "There, in that man's shoes, you can witness the events that occurred on Rokkenjima with your own eyes."
 show nao_v014 normal at active
 show beatrice_v001 normal at inactive
 nao 'I see. You want me to move around on your game board from the perspective of this man, "Battler", right?'
 show beatrice_v001 smile at nod_transform,active
 show nao_v014 normal at inactive
 beatrice "That's right. Being sharp and straight-forward is key. \n...Also, Nao, that uniform that you are wearing is that of battle furniture which has signed a contract to me."
 show nao_v014 odoroki at active
 show beatrice_v001 smile at inactive
 nao 'Huh...?'
 show beatrice_v001 smile at active
 show nao_v014 odoroki at inactive
 beatrice "Considering this, that would make you my furniture too... wouldn't it?"
 show nao_v014 fuan at active
 show beatrice_v001 smile at inactive
 nao 'If you put it that way, it makes me want to take it off...'
 show beatrice_v001 smile_close at active
 show nao_v014 fuan at inactive
 beatrice '*cackle*cackle*cackle*, I jest, I jest. Now look ahead. The game will begin from here.'
 show nao_v014 odoroki at active
 show beatrice_v001 smile_close at inactive
 nao 'Huh...? Wh-what should I do?'
 show beatrice_v001 smile at active
 show nao_v014 odoroki at inactive
 beatrice "Anything is fine. Whenever you're ready, step up right behind Battler."
 show beatrice_v001 futeki at active
 show nao_v014 odoroki at inactive
 beatrice "Enjoy the close-up seat in Battler's fight against me."
 show nao_v014 fuan at active
 show beatrice_v001 futeki at inactive
 nao "I'm not playing the game? However you put it, am I not just watching someone else play from behind...?"
 show beatrice_v001 normal at nod_transform,active
 show nao_v014 fuan at inactive
 beatrice 'This is a game between me and Battler. Therefore, you are not the one who can be called my opponent.'
 show beatrice_v001 normal_close at active
 show nao_v014 fuan at inactive
 beatrice "It's just that the Witch of Miracles and the Witch of Certainty are the only ones who have spectated so far. I wanted to shake things up a little and hear your thoughts."
 show nao_v014 fuan_close at active
 show beatrice_v001 normal_close at inactive
 nao "...If it's a game, I think playing myself is more fun."
 show beatrice_v001 normal at active
 show nao_v014 fuan_close at inactive
 beatrice 'Are you unsatisfied?'
 show nao_v014 normal at active
 show beatrice_v001 normal at inactive
 nao "No, not at all... It's just, I didn't know of any other way of playing a game than playing it yourself."
 show nao_v014 smile at active
 show beatrice_v001 normal at inactive
 nao 'But, well... alright. If that type of enjoyment exists, then I will have to give it a shot.'
 show beatrice_v001 futeki at active
 show nao_v014 smile at inactive
 beatrice '*cackle*cackle*cackle*... \nThis open-minded and honest attitude is an essential element to enjoying the game. Not bad at all.'
 show nao_v014 sinken at active
 show beatrice_v001 futeki at inactive
 nao "I'll accept those words of praise. \nUmm, so do people normally have wait for this story to begin...?"
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide beatrice_v001
 hide nao_v014
 with Dissolve(0.2)
 stop sound
 show expression 'images/card/Card_032009.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 nao 'Uuum... *ahem*.'
 nao "Nao Houtani... rightfully spectating the witch Beatrice's game board."
 nao 'Please, if you would kindly begin...'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_2220.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show beatrice_v001 futeki at mei_center
 with Dissolve(0.08333333333333333)
 show beatrice_v001 futeki at updown_shake_transform,active
 beatrice "Pff, hahahahahahahaha... Once you hear Battler's greeting, it begins! How incredibly entertaining this is!"
 show beatrice_v001 futeki_close at active
 beatrice 'However, you are unrefined, Nao. If you were Maria, you would be flying around with such vigor. *cackle*cackle*cackle*!'
 show beatrice_v001 smile at active
 beatrice "Oh, look, don't make such a face. The story is already beginning. \nIf anything, try not to get shaken off. "
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide beatrice_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show nao_v014 fuan at mei_left
 show beatrice_v001 smile at mei_right
 with Dissolve(0.5)
 show nao_v014 fuan at active
 show beatrice_v001 smile at inactive
 nao 'Thank you... w-wait a minute. Just what will I be "shaken off" from?'
 show beatrice_v001 futeki at active
 show nao_v014 fuan at inactive
 beatrice 'Of course, from my game boooard!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide nao_v014
 hide beatrice_v001
 hide fade onlayer curtain
 show nao_v014 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_611_ls_wind.wav'
 camera at screenshake_transform
 pause 0.0
 show nao_v014 odoroki at active
 nao "I-I didn't know there was a type of vehicle like tha-... AAAAAAATT?!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide nao_v014
 hide fade onlayer curtain
 show beatrice_v001 futeki at mei_center
 with Dissolve(0.08333333333333333)
 show beatrice_v001 futeki at updown_shake_transform,active
 beatrice "Kuhahhahhahhahha! A great scream that tugs on the heartstrings! Let's enjoy this as much as possibleeeeeeeee!!"
 call chapter_end
 jump chara032009_03