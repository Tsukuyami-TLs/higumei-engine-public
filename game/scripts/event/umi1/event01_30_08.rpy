label event01_30_08:
 show black_background onlayer black
 $ event_store.current_event='umi1'
 $ event_store.current_progress=4
 $ event_store.current_chapter='event01_30_08'
 $ persistent.menu_return='event'
 camera:
  anchor (0.5, 0.5)
  pos (960, 540)
  zoom 1.0
  matrixcolor IdentityMatrix()
 pause 0.0
 scene
 stop music
 play sound ['audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav'] fadeout 1.0
 stop sound
 show expression 'images/bg/AdvBg_2331.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator 'That final night on Rokkenjima...'
 narrator 'I was supposed to sleep soundly with my heart and stomach full of happiness after the most wonderful dinner...'
 Character('Toshiro Gohda',ctc="ctcArrow", ctc_position="fixed") 'What kind of after-dinner beverages would you like? We have coffee, black tea, salted kelp tea...'
 show erika_v001 sinken at mei_center
 with Dissolve(0.5)
 show erika_v001 sinken at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") '........................'
 hide erika_v001
 with Dissolve(0.2)
 show mion_v002 sinken at mei_center
 with Dissolve(0.5)
 show mion_v002 sinken at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") '...........................'
 hide mion_v002
 with Dissolve(0.2)
 show shion_v002 smile at mei_right
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at inactive
 show shion_v002 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...I-I'll have hot black tea."
 show shion_v002 smile at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Bring some warm black tea for everyone else, please.'
 hide nao_v002
 hide shion_v002
 with Dissolve(0.2)
 Character('Toshiro Gohda',ctc="ctcArrow", ctc_position="fixed") 'A-As you wish...'
 narrator "The atmosphere was heavy, ever since Mion-san exposed Erika-san's charades."
 narrator "At the very least, the culprit behind yesterday's prank was definitely Erika-san."
 narrator 'And Erika-san already knew she was the first to be suspected.'
 show nao_v002 normal at mei_left
 show erika_v001 sinken at mei_right
 with Dissolve(0.5)
 show erika_v001 sinken at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "And yet... you put up an act and then appealed to us that you weren't the culprit... didn't you...?"
 show nao_v002 normal at inactive
 show erika_v001 sinken at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "I would never do that. I didn't make that magic circle!"
 show erika_v001 sinken at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Yeah, sure. ...Even if we are assuming it was an act... it still wasn't very tasteful."
 show nao_v002 normal at inactive
 show erika_v001 sinken_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") '...Hmph.'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 show black_cover as bg
 hide erika_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator '...At that moment, I felt my surroundings growing dim.'
 stop sound
 show expression 'images/bg/AdvBg_2190.png' as bg
 play music "<loop 0>audio/bgm/BGM_QUEST1_COLLAB2.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator 'Huh? ...Mion-san and Shion-san... disappeared as if they were a mirage the whole time.'
 narrator 'Erika-san and I remained. In place of where Mion-san and Shion-san vanished... the form of those witches from my dreams appeared...'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show beatrice_v001 futeki at mei_center
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_610_ls_plosive.wav'
 show beatrice_v001 futeki at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") '<Happy Birthday!!!> to me! And thank you, everyone! I truly am a lucky person!!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide beatrice_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_381_ls_gaya.wav'
 play audio 'audio/sfx/SE_525_applause.wav'
 narrator '*clap*clap*clap*! I heard the resounding applause and congratulations of an invisible audience.'
 show beatrice_v001 futeki at mei_right
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at inactive
 show beatrice_v001 futeki at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "How's that, Nao? This is your final night, right? Hope you enjoyed looking at that second magic circleeee!"
 show beatrice_v001 futeki at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...I'm... dreaming all of a sudden...?"
 show beatrice_v001 futeki at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Well, I guess I shouldn't get anxious about it. I'm here, Erika-san's here, Beatrice is here, and Dlanor-san is here. That would make everyone."
 hide nao_v002
 hide beatrice_v001
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'You are very quick to change your MIND. ...The ability to adapt to foreign situations is necessary for a VOYAGER.'
 hide dlanor_v001
 with Dissolve(0.2)
 show erika_v001 smile at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show erika_v001 smile at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Well, Nao-chama? Let's have some fun! If you keep working hard, Beato will give you a prize, won't she?"
 show erika_v001 smile at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I couldn't solve that riddle from last night... And now tonight..."
 hide erika_v001
 show beatrice_v001 smile at mei_right
 with Dissolve(0.5)
 show nao_v002 fuan at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "Don't fret. Yesterday was just a little test."
 show nao_v002 fuan at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "Tonight, if you solve the mystery with the magic circle in Erika's room, I'll present you with a reward."
 hide nao_v002
 hide beatrice_v001
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'Please do your best, NAO. I will continue to give you my SUPPORT.'
 hide dlanor_v001
 with Dissolve(0.2)
 show nao_v002 fuan_close at mei_left
 show beatrice_v001 smile at mei_right
 with Dissolve(0.5)
 show beatrice_v001 smile at inactive
 show nao_v002 fuan_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I've already had enough of this game... is what I want to say, though."
 show nao_v002 fuan_close at inactive
 show beatrice_v001 futeki at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "Sure! This game won't end until the morning comes, though! *cackle*cackle*cackle*!"
 hide beatrice_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator "*sigh*... Guess I'd better prepare for the worst."
 narrator "At least in yesterday's exchange, I don't think they were trying to give me a hard time."
 narrator 'Erika-san and that witch seem suspicious, but I feel like I can trust Dlanor-san...'
 show nao_v002 normal at mei_left
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 show dlanor_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Dlanor-san... why am I fighting against the witch in this game?'
 show dlanor_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Don't tell me... I'm going to be sacrificed as the witch's birthday present...?"
 show nao_v002 normal at inactive
 show dlanor_v001 normal_close at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'Lady Beatrice, as the master of this island and of the Golden Land, has a particular disease that all witches have difficulty ESCAPING...'
 show dlanor_v001 normal_close at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Disease......?'
 hide dlanor_v001
 show beatrice_v001 futeki_close at mei_right
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show beatrice_v001 futeki_close at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "That disease is boredom! *cackle*cackle*cackle*!! A witch won't die if you stab or burn them, but they can drown to death in the sea of boredom."
 hide nao_v002
 hide beatrice_v001
 with Dissolve(0.2)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "For that reason, witches will sometimes send each other letters and Fragments. They'll share stimulating stories with each other and cure their illnesses."
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Well, this time, it took the form of a birthday celebration for Beatrice, though.'
 hide erika_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_left
 show beatrice_v001 smile at mei_right
 with Dissolve(0.5)
 show beatrice_v001 smile at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Why me and not Mion-san or Shion-san?'
 show nao_v002 normal at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "Of course, it's because of {i}that{/i}! It's because I got along with you best!"
 hide beatrice_v001
 hide nao_v002
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'There is no ulterior MOTIVE. I can guarantee THAT.'
 hide dlanor_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'So then, this battle of wits between the witch and I has just been because she wanted to relieve herself of her boredom?'
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'That is the plan. Even witches tend to be lonely creatures.'
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 show beatrice_v001 normal_close at mei_center
 with Dissolve(0.5)
 show beatrice_v001 normal_close at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'With that said, having the modesty to ask something like, \n"Please play with me.", is where witches fall short.'
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'It has been awfully fun playing this game with you. It was enough to cure me and bring me great happiness.'
 hide beatrice_v001
 with Dissolve(0.2)
 show erika_v001 normal at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'How generous. Not worrying about the outcome of the game, just letting go and having fun.'
 show erika_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "This isn't some secret plan to steal my soul or whatever if I lose, is it...?"
 hide erika_v001
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'That will not HAPPEN. As a first-class archbishop of the Great Court of Heaven, I, Dlanor A. Knox, will guarantee THAT.'
 show dlanor_v001 normal at inactive
 show nao_v002 normal_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...........................'
 stop music fadeout 2.0
 hide nao_v002
 hide dlanor_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Very well. If that's the case..."
 play music "<loop 0>audio/bgm/BGM_TITLE_COLLAB2.ogg"
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Happy birthday, <Miss Beatrice>.'
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I humbly accept your challenge. ...It's just, I'm..."
 hide nao_v002
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_5001_sitdown2.wav'
 narrator 'Though it might be ill-mannered of me, I pulled up a chair and crossed my legs.'
 narrator 'This was no longer a dinner table, so I felt I could ignore a few manners. ...After all, this was a competition, a game to kill some boredom.'
 show nao_v002 sinken at mei_center
 with Dissolve(0.5)
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...I'm rather competitive. Win or lose, I won't say I had fun."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") '<Good>. I suppose you never fail to meet my expectations.'
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'I had felt that from your appearance when we were on the ferry, and it turns out my intuition was on point.'
 hide erika_v001
 with Dissolve(0.2)
 show beatrice_v001 futeki at mei_right
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal at inactive
 show beatrice_v001 futeki at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "I'm delighted, Nao! You really are an upstanding girl! Now, let us enjoy ourselves to our heart's content on this night!"
 show beatrice_v001 futeki at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'Nao... once again, I will explain the SITUATION.'
 show beatrice_v001 futeki at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") "A magic circle prank appeared in Erika's ROOM..."
 show dlanor_v001 normal at inactive
 show beatrice_v001 futeki at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'I claim it was impossible for a human; therefore, it is the work of a witch!'
 hide dlanor_v001
 show nao_v002 sinken at mei_left
 with Dissolve(0.5)
 show beatrice_v001 futeki at inactive
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'I posit that it was possible for a human to pull off this prank. And that human is none other than Erika-san!'
 hide beatrice_v001
 show erika_v001 futeki at mei_right
 with Dissolve(0.5)
 show nao_v002 sinken at inactive
 show erika_v001 futeki at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") '*giggle*, <Good>. Please do come at me with all of your might.'
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'And so, Erika is a player once AGAIN.'
 hide dlanor_v001
 with Dissolve(0.2)
 show nao_v002 odoroki at mei_left
 show beatrice_v001 futeki at mei_right
 with Dissolve(0.5)
 show beatrice_v001 futeki at inactive
 show nao_v002 odoroki at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "What do you mean? This isn't just a fight between the witch and I?"
 show nao_v002 odoroki at inactive
 show beatrice_v001 futeki at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Tonight, we have a mêlée à trois! This truly will be entertaining!'
 hide beatrice_v001
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show nao_v002 odoroki at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Both I and Nao-chama claim that a Human pulled off this prank.'
 show erika_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "We're working together?"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide nao_v002
 hide erika_v001
 hide fade onlayer curtain
 show erika_v001 futeki at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 futeki at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Not quite. I believe that the culprit is Shion-san.'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 narrator 'I see. Three participants, each one claiming a different side.'
 camera at screenshake_transform
 pause 0.0
 narrator "Tonight's magic circle was either magic cast by the witch, a farce performed by Erika-san, or a crime committed by Shion-san!"
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'For tonight, I believe I do have the responsibility of READER.'
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'So, I shall explain the situation for you THREE. Please listen CAREFULLY...'
 stop music fadeout 2.0
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide dlanor_v001
 with Dissolve(0.2)
 stop sound
 show expression 'images/bg/AdvBg_2371.png' as bg
 play music "<loop 0>audio/bgm/BGM_QUEST3_COLLAB2.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 pause 1.0
 call wipeout_routine
 stop sound
 show expression 'images/bg/AdvBg_2281.png' as bg
 call wipein_routine
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") "This time, a magic circle was discovered inside of Erika's ROOM."
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'When Erika returned and unlocked the door, she discovered her bed was left RANSACKED. A magic circle was found drawn on the SHEETS.'
 hide dlanor_v001
 with Dissolve(0.2)
 narrator "...I want to confirm something here to boot, though I'll have to behave and lend my ears for now."
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'Earlier today, Erika forgot to lock her room until she returned to the guesthouse at NOON.'
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'Therefore, until the room was locked at noon, anybody could have entered the ROOM.'
 hide dlanor_v001
 with Dissolve(0.2)
 narrator "This was the crux. ...The point being that it's the same as last night's magic circle. Erika-san confirmed there was nothing weird inside her room when she locked it."
 narrator 'Normally, the crime could have occurred from that point onward... but at that point it became a perfect closed room.'
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show red_cover onlayer curtain as fade with Dissolve(0.16666666666666666)
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 hide fade onlayer curtain
 with Dissolve(0.16666666666666666)
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") '{umi_red}From the point the door is locked until Erika unlocked it, the room was a perfect closed ROOM.{/umi_red}'
 show red_cover onlayer curtain as fade with Dissolve(0.16666666666666666)
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 hide fade onlayer curtain
 with Dissolve(0.16666666666666666)
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") '{umi_red}Nobody existed inside the room at that time, and nobody could have entered by any other METHOD.{/umi_red}'
 show red_cover onlayer curtain as fade with Dissolve(0.16666666666666666)
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 hide fade onlayer curtain
 with Dissolve(0.16666666666666666)
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") '{umi_red}The magic circle prank could not have been completed unless the person entered the ROOM.{/umi_red}'
 show dlanor_v001 normal_close at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'That will be all for NOW. ...Everyone, please begin your INVESTIGATION...'
 hide dlanor_v001
 with Dissolve(0.2)
 narrator 'Us three players looked at each other with inquisitive expressions.'
 narrator 'It seems everyone is still theorycrafting. I was itching to ask questions and throw blue truths at Dlanor-san...'
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") "Now then, we shall BEGIN. Since it is Lady Beatrice's birthday, she has the privilege of going FIRST."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide dlanor_v001
 hide fade onlayer curtain
 show beatrice_v001 futeki at mei_center
 with Dissolve(0.08333333333333333)
 show beatrice_v001 futeki at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "Well, happy birthday to me!! Let's get started, then."
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "When Erika returned, she unlocked her room and entered it, so there must have been a short interval before Nao's group heard her scream."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide beatrice_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "That is correct. Before I entered the room, I ensured that there wasn't any garbage packed into the keyhole, so it took a bit of time."
 hide erika_v001
 with Dissolve(0.2)
 narrator '...Why is Beatrice focusing on that? My plan of attack was centered on Erika-san acting...'
 show beatrice_v001 normal at mei_right
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "Let's dash Nao's hopes. Dlanor, repeat this in red."
 show dlanor_v001 normal at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") '"From the time Erika entered her room to the time Nao\'s group entered after hearing her scream, it was impossible to place the magic circle."'
 show beatrice_v001 normal at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'Request GRANTED.'
 show red_cover onlayer curtain as fade with Dissolve(0.16666666666666666)
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 hide fade onlayer curtain
 with Dissolve(0.16666666666666666)
 show beatrice_v001 normal at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") "{umi_red}From the time Erika entered her room to the time Nao's group entered after hearing her scream, it was impossible for her to place the magic CIRCLE.{/umi_red}"
 hide dlanor_v001
 hide beatrice_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Umm, so does that also include everyone other than Erika-san?'
 hide nao_v002
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'YES.'
 show red_cover onlayer curtain as fade with Dissolve(0.16666666666666666)
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 hide fade onlayer curtain
 with Dissolve(0.16666666666666666)
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") '{umi_red}After Erika enters her room, placing the magic circle through any kind of method is not DOABLE.{/umi_red}'
 hide dlanor_v001
 with Dissolve(0.2)
 show erika_v001 normal at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Thank you very much for clearing up those false accusations for me. See? See how I wasn't acting? I just wasn't given enough time to explain."
 show erika_v001 normal at inactive
 show nao_v002 normal_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...How terrible. But this was still the same as what happened to my bed...'
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 narrator 'So, the only time it was possible to place the magic circle was before Erika-san locked her room...'
 narrator "It's the same as yesterday. The magic circle then could only be placed before Shannon-san locked the window."
 narrator 'And in both cases, people confirmed nothing was wrong when they entered the room...'
 show beatrice_v001 futeki at mei_center
 with Dissolve(0.5)
 show beatrice_v001 futeki at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'My turn ends here. *cackle*cackle*cackle*'
 hide beatrice_v001
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'Now then, as we do traditionally, we will go in a clockwise DIRECTION.'
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'Next up is ERIKA.'
 show erika_v001 normal_close at mei_right
 with Dissolve(0.5)
 show dlanor_v001 normal at inactive
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Well then. *ahem*.'
 show dlanor_v001 normal at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "I think this will be much too complicated with three players, so I'll make this quick. Nao-san, you should drop out."
 hide dlanor_v001
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Thought you might say that. I would have said the same thing if I were you.'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide erika_v001
 hide nao_v002
 hide fade onlayer curtain
 show erika_v001 normal at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "*giggle*giggle*giggle*. ...Anyway, I'm going to talk about the differences between the two magic circles seen today and yesterday."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show beatrice_v001 normal at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Hoh? Differences, you say?'
 show beatrice_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...I thought they were the same circle though......'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide nao_v002
 hide beatrice_v001
 with Dissolve(0.2)
 stop sound
 show expression 'images/bg/AdvBg_2320.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'Over here is the first magic circle, and over there is the SECOND. Please compare THEM.'
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") '...Hmm......? How are they different?'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_2281.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 show nao_v002 sinken at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show nao_v002 sinken at active
 show nao_v002 sinken at jump_transform
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Ah...... there!'
 show nao_v002 sinken at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") '<Good>. Nao-chama has noticed it, and very quickly at that.'
 hide erika_v001
 hide nao_v002
 with Dissolve(0.2)
 show beatrice_v001 fuan at mei_center
 with Dissolve(0.5)
 show beatrice_v001 fuan at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Eh? What? ...Is this some kinda Spot the Difference puzzle???'
 hide beatrice_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'I happen to have a photographic memory.'
 show nao_v002 normal at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'A photographic memory... an invaluable tool for a detective.'
 show erika_v001 normal at inactive
 show nao_v002 normal_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I was panicking yesterday and I was in shock, so I assumed that today's magic circle was the exact same..."
 show erika_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'There. See these letters surrounding the magic circle in a ring? ...This one specifically is different.'
 hide erika_v001
 show beatrice_v001 sinken at mei_right
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show beatrice_v001 sinken at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "Hmmm, I see... This letter should be a little swirl, but instead, it's two circles."
 show beatrice_v001 sinken at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Indeed. I doubt this was a simple drawing error. This same symbol appears in three other places.'
 show nao_v002 smile at inactive
 show beatrice_v001 sinken at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'That there are! There are double circles in three spots where there should be swirls! ...What on earth is this?!'
 hide nao_v002
 hide beatrice_v001
 with Dissolve(0.2)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'If you look closely, you can detect many other minute differences.'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide erika_v001
 with Dissolve(0.2)
 stop sound
 show expression 'images/bg/AdvBg_2190.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 show erika_v001 normal at mei_right
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'After putting together these clues, I would like to request you to repeat something, Dlanor.'
 show erika_v001 normal at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'Go ahead, ERIKA.'
 hide dlanor_v001
 hide erika_v001
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_204_shot.wav'
 show white_cover as flash with Dissolve(0.1)
 pause 0.1
 hide flash with Dissolve(0.2)
 narrator 'Repeat this in red: "The two magic circles were drawn onto two separate sheets by different people.".'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show nao_v002 sinken at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '.........?!?!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show beatrice_v001 normal at mei_right
 show erika_v001 normal at mei_left
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "I see... So you want to prove that this all wasn't an act."
 show erika_v001 normal at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "But if that's the case... won't you have to to admit it...?"
 show beatrice_v001 normal at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "*giggle*. I don't mind at all saying that."
 show beatrice_v001 normal at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Well, Dlanor? Will you do the honors?'
 hide erika_v001
 hide beatrice_v001
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") '...YES. Sorry for the WAIT. I shall repeat IT.'
 play sound ['audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav'] fadeout 1.0
 show red_cover onlayer curtain as fade with Dissolve(0.16666666666666666)
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 hide fade onlayer curtain
 with Dissolve(0.16666666666666666)
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") '{umi_red}The two magic circles were drawn onto two separate sheets by different PEOPLE.{/umi_red}'
 hide dlanor_v001
 with Dissolve(0.2)
 show erika_v001 normal_close at mei_center
 with Dissolve(0.5)
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'I will do a C.O. as well.'
 hide erika_v001
 with Dissolve(0.2)
 show nao_v002 fuan at mei_left
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 show dlanor_v001 normal at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'C.O.?'
 show nao_v002 fuan at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") '"Coming OUT".  The disclosure of information that others aren\'t aware of, or a CONFESSION.'
 hide dlanor_v001
 hide nao_v002
 with Dissolve(0.2)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'That first magic circle was drawn by me, Erika-san.'
 hide erika_v001
 with Dissolve(0.2)
 show nao_v002 sinken at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 camera at screenshake_transform
 pause 0.0
 show erika_v001 normal at inactive
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'See, so you really were the culprit after all!!'
 show nao_v002 sinken at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Oh quiet. It was just a prank, wasn't it? And you {i}are{/i} aware bringing personal grudges into this game is boorish, correct?"
 hide nao_v002
 show beatrice_v001 normal at mei_left
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "We already knew Erika was the perpetrator behind that first magic circle. That said, how Shannon didn't notice the magic circle at all is still a mystery, isn't it?"
 show erika_v001 normal at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'If you want to deny Erika as a witch, you must show how she tricked Shannon.'
 show beatrice_v001 normal at inactive
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'On top of that, you must present it in the form of a blue truth. ...That does it for my turn.'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide erika_v001
 hide beatrice_v001
 hide fade onlayer curtain
 show beatrice_v001 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show beatrice_v001 sinken at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "......That being said... I still don't understand this magic circle at all. ...Just why was it made that way?"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide beatrice_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '.....................?'
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") "Thank you for WAITING. It is now Nao's TURN."
 stop music fadeout 2.0
 show dlanor_v001 normal at inactive
 show nao_v002 normal_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...........................'
 hide nao_v002
 hide dlanor_v001
 with Dissolve(0.2)
 narrator 'Inside my head, many thoughts swirled around like soup.'
 narrator '...It feels like the ingredients came together and began to boil. ...Could it be......'
 show nao_v002 normal at mei_left
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 show dlanor_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Dlanor-san, a question.'
 show nao_v002 normal at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'What is IT?'
 play music "<loop 0>audio/bgm/BGM_QUEST7_COLLAB2.ogg"
 show dlanor_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "In Erika-san's C.O., she admitted that she was the culprit behind the first magic circle."
 show dlanor_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Is that confession as good as red truth?'
 hide dlanor_v001
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'No. It is not red, so it may contain some lies.'
 show erika_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'But, Erika-san, can you still repeat it?'
 show nao_v002 normal at inactive
 show erika_v001 normal at active
 show erika_v001 normal at nod_transform
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Why yes, how could I not? Of course, I'll have you state it for me first."
 show erika_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Well then, please repeat this:'
 show white_cover as flash with Dissolve(0.1)
 pause 0.1
 hide flash with Dissolve(0.2)
 show erika_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '"The one who created the first magic circle and placed it was Erika-san."'
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 narrator "......For a moment, I saw hesitation in Erika-san's eyes. I bet she was thinking about how to answer this in such a way as to confuse me more."
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "I'll respond."
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show red_cover onlayer curtain as fade with Dissolve(0.16666666666666666)
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 hide fade onlayer curtain
 with Dissolve(0.16666666666666666)
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") '{umi_red}The one who created the first magic circle and placed it was Erika Furudo.{/umi_red}'
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "However, how and when I placed it and how I tricked Shannon-san are things I refuse to answer. I do hope you'll forgive me."
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 hide erika_v001
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") "Nao's turn is now OVER. Lady Beatrice may go AGAIN."
 hide dlanor_v001
 with Dissolve(0.2)
 narrator '...I used up my precious turn to confirm something I already knew.'
 narrator "My opponents are seriously Erika-san and that witch? ...I couldn't win this three-way fight if the other sides united against me."
 show nao_v002 normal at mei_left
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 show dlanor_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Dlanor-san, can you go over the rules once more please?'
 show dlanor_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'This three-way fight can only have one winner, right?'
 show nao_v002 normal at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'Two winners are POSSIBLE.'
 show dlanor_v001 normal at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '......Thank you. Beatrice was next, right?'
 show dlanor_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Though, I wonder if you're going to corner me...?"
 hide dlanor_v001
 show beatrice_v001 smile at mei_right
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "I don't care about winning or losing, this game is purely for entertainment. I still intend to have a fair fight, however."
 show nao_v002 normal at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'I attacked you just now, so next, I will place my attack on Erika.'
 hide nao_v002
 show erika_v001 normal at mei_left
 with Dissolve(0.5)
 show beatrice_v001 smile at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Do as you wish.'
 hide beatrice_v001
 hide erika_v001
 with Dissolve(0.2)
 narrator '...Erika-san is definitely gunning for me. She wants to claim victory, but she also wants me to lose more than anything.'
 narrator 'Meanwhile, I sense no ill will at all from Beatrice. She just wants to have a fair game. ...Of course, with the way things are playing out, she might press on if victory is in sight.'
 narrator '...Maybe, as Erika-san and I hold our positions... I can try to pull Beatrice over to my side...'
 narrator 'For me to win, I need to prove Erika-san was acting.'
 narrator 'For Beatrice to win, she must prove the crime was impossible for humans......'
 show nao_v002 fuan at mei_left
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 show dlanor_v001 normal at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Dlanor-san, excuse me again. I would like to confirm something else...'
 show nao_v002 fuan at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'Rest ASSURED. I will listen to what you have to SAY.'
 show dlanor_v001 normal at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Ah... um.'
 hide dlanor_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator 'I gave an awkward look and motioned for Dlanor-san to come over for a private talk, and she understood immediately.'
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'We can WHISPER. It is not an ISSUE.'
 hide dlanor_v001
 with Dissolve(0.2)
 narrator 'No matter the game, the very act of checking a rule could reveal your hand.'
 narrator "I especially didn't want Erika-san to hear me..."
 show beatrice_v001 smile at mei_right
 show erika_v001 normal at mei_left
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Hmm-hmm, having a private chat, are we?'
 show beatrice_v001 smile at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Who knows? Well, she is a novice, so we must lend her our support.'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide erika_v001
 hide beatrice_v001
 hide fade onlayer curtain
 show dlanor_v001 normal_close at mei_center
 with Dissolve(0.08333333333333333)
 show dlanor_v001 normal_close at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") '...Mm-HMM. ......I SEE.'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide dlanor_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 narrator "My face was pressed against Dlanor-san's as we spoke in hushed tones."
 narrator '...She smelled nice. This was a fragrance I had never experienced before. ...I wanted to press my nose against her hair and take it all in...'
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Dlanor gives off an audaciously bewitching scent, doesn't she?"
 show erika_v001 smile at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'I have a good nose, so I can smell her from a mile away. *giggle*giggle*.'
 hide erika_v001
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") '...Nao, there is no issue at ALL.'
 show nao_v002 normal at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'The first magic circle was proven to be possible for a Human, but if the second magic circle was proven IMPOSSIBLE...'
 show dlanor_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Then Beatrice and I would be the winners...'
 show nao_v002 normal at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'However, as the Reader, this is nothing more than just a whisper to ME.'
 show nao_v002 normal at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'You are free to tell Lady Beatrice and ally with her; however, Erika-san will hear it as WELL.'
 hide nao_v002
 hide dlanor_v001
 with Dissolve(0.2)
 narrator 'Alright, <good>. ......Is that how you say it?'
 narrator 'Erika-san, I hate losing. I will win with certainty. And I {i}will{/i} uncover the secrets of these two magic circles.'
 narrator 'Erika-san, I learned it from you. This battle of wits... was more like a fistfight.'
 narrator 'The victor will be the one who amasses all claims, all logic, and all evidence... so that they can beat the enemy down thoroughly.'
 camera at screenshake_transform
 pause 0.0
 narrator 'I will win, and I WILL defeat her!'
 show nao_v002 sinken at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '........................'
 show nao_v002 sinken at inactive
 show erika_v001 futeki at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") '...<Good>.'
 call chapter_end
 jump event01_30_09