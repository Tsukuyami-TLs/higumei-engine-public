label event01_30_08:
 show black_background onlayer black
 play sound ['audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav'] fadeout 1.0
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2331.png' as bg
 with Dissolve(1.0)
 narrator 'That final night on Rokkenjima...'
 narrator 'I was supposed to sleep soundly with my heart and stomach full of happiness after the most wonderful dinner...'
 Character('Gohda',ctc="ctcArrow", ctc_position="fixed") 'What kind of after-dinner beverages would you like? We have coffee, black tea, salted kelp tea...'
 show erika_v001 sinken at mei_center
 with Dissolve(0.5)
 show erika_v001 sinken at active
 erika '........................'
 hide erika_v001
 with Dissolve(0.2)
 show mion_v002 sinken at mei_center
 with Dissolve(0.5)
 show mion_v002 sinken at active
 mion '...........................'
 hide mion_v002
 with Dissolve(0.2)
 show nao_v002 fuan at mei_left
 show shion_v002 smile at mei_right
 with Dissolve(0.5)
 show shion_v002 smile at active
 show nao_v002 fuan at inactive
 shion "...I-I'll have hot black tea."
 show nao_v002 smile at active
 show shion_v002 smile at inactive
 nao 'Bring some warm black tea for everyone else, please.'
 hide nao_v002
 hide shion_v002
 with Dissolve(0.2)
 Character('Gohda',ctc="ctcArrow", ctc_position="fixed") 'A-as you wish...'
 narrator "The atmosphere was heavy, ever since Mion-san exposed Erika-san's charades."
 narrator "At the very least, the culprit behind yesterday's prank was definitely Erika-san."
 narrator 'And Erika-san already knew she was the first to be suspected.'
 show erika_v001 sinken at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show erika_v001 sinken at inactive
 nao "And yet... you put up an act and then made an appeal to us that you weren't the culprit... didn't you...?"
 show erika_v001 sinken at active
 show nao_v002 normal at inactive
 erika "I would never do that. I didn't make that magic circle!"
 show nao_v002 normal at active
 show erika_v001 sinken at inactive
 nao "Yeah, sure. ...Even if we are assuming it was an act... it still wasn't very tasteful."
 show erika_v001 sinken_close at active
 show nao_v002 normal at inactive
 erika '...Hmph.'
 show expression "#000" as fade with Dissolve(1.0)
 scene expression "#000"
 hide erika_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator '...At that moment, I felt my surroundings growing dim.'
 stop sound
 scene expression "#000"
 play music 'audio/bgm/BGM_QUEST1_COLLAB2.wav'
 show expression 'images/bg/AdvBg_2190.png' as bg
 with Dissolve(1.0)
 narrator 'Huh? ...Mion-san and Shion-san are... disappearing as if they were a mirage the whole time.'
 narrator 'Erika-san and I remained. In place of where Mion-san and Shion-san vanished... wait, those witches appeared in my dreams...'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide fade with Dissolve(0.08333333333333333)
 show beatrice_v001 futeki at mei_center
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_610_ls_plosive.wav'
 show beatrice_v001 futeki at active
 beatrice '<Happy Birthday!!!> Congrats to me! And thank you, everyone! I truly am a lucky person!'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide beatrice_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_381_ls_gaya.wav'
 play audio 'audio/sfx/SE_525_applause.wav'
 narrator '*clap*clap*clap*! I heard the resounding applause and congratulations of an invisible audience.'
 show nao_v002 fuan at mei_left
 show beatrice_v001 futeki at mei_right
 with Dissolve(0.5)
 show beatrice_v001 futeki at active
 show nao_v002 fuan at inactive
 beatrice "How's that, Nao? This is your final night, right? Hope you enjoyed looking at that second magic circleeee!"
 show nao_v002 fuan at active
 show beatrice_v001 futeki at inactive
 nao "...I'm... dreaming all of a sudden...?"
 show nao_v002 normal at active
 show beatrice_v001 futeki at inactive
 nao "Well, I guess I shouldn't get anxious about it. I'm here, Erika-san's here, Beatrice is here, and Dlanor-san is here. That would make everyone."
 hide nao_v002
 hide beatrice_v001
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 dlanor 'You are very quick to change your MIND. ...The ability to adapt to foreign situations is necessary for a VOYAGER.'
 hide dlanor_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_left
 show erika_v001 smile at mei_right
 with Dissolve(0.5)
 show erika_v001 smile at active
 show nao_v002 normal at inactive
 erika "Well, Nao-chama? Let's have some fun! If you keep working hard, Beato will give you a prize, won't she?"
 show nao_v002 fuan at active
 show erika_v001 smile at inactive
 nao "I couldn't solve that riddle from last night... And now tonight..."
 hide erika_v001
 show beatrice_v001 smile at mei_right
 with Dissolve(0.5)
 show beatrice_v001 smile at active
 show nao_v002 fuan at inactive
 beatrice "Don't fret. Yesterday was just a little test."
 show beatrice_v001 smile at active
 show nao_v002 fuan at inactive
 beatrice "Tonight, if you solve the mystery with magic circle in Erika's room, I'll bestow upon you a reward."
 hide nao_v002
 hide beatrice_v001
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 dlanor 'Please do your best, NAO. I will continue to give you my SUPPORT.'
 hide dlanor_v001
 with Dissolve(0.2)
 show beatrice_v001 smile at mei_right
 show nao_v002 fuan_close at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan_close at active
 show beatrice_v001 smile at inactive
 nao "I've already had enough of this game... is what I want to say, though."
 show beatrice_v001 futeki at active
 show nao_v002 fuan_close at inactive
 beatrice "Sure! This game won't end until the morning comes, though! *cackle*cackle*cackle*!"
 hide beatrice_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator "*sigh*... Guess I'd better prepare for the worst."
 narrator "At least in yesterday's exchange, I don't think they were trying to give me a hard time."
 narrator 'Erika-san and that witch seem suspicious, but I feel like I can trust Dlanor-san...'
 show dlanor_v001 normal at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show dlanor_v001 normal at inactive
 nao 'Dlanor-san... why am I fighting against the witch in this game?'
 show nao_v002 normal at active
 show dlanor_v001 normal at inactive
 nao "Don't tell me... I'm going to be sacrificed as the witch's birthday present...?"
 show dlanor_v001 normal_close at active
 show nao_v002 normal at inactive
 dlanor 'Lady Beatrice, as the master of this island and of the Golden Land, has a particular disease that all witches have difficulty ESCAPING...'
 show nao_v002 normal at active
 show dlanor_v001 normal_close at inactive
 nao '...Disease......?'
 hide dlanor_v001
 show beatrice_v001 futeki_close at mei_right
 with Dissolve(0.5)
 show beatrice_v001 futeki_close at active
 show nao_v002 normal at inactive
 beatrice "That disease is boredom! *cackle*cackle*cackle*!! A witch won't die if you stab or burn them, but they can drown to death in the sea of boredom."
 hide nao_v002
 hide beatrice_v001
 with Dissolve(0.2)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika "For that reason, witches will sometimes send each other letters and Fragments. They'll share stimulating stories with each other and cure their illnesses."
 show erika_v001 normal_close at active
 erika 'Well, this time, it took the form of a birthday celebration for Beatrice, though.'
 hide erika_v001
 with Dissolve(0.2)
 show beatrice_v001 smile at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show beatrice_v001 smile at inactive
 nao '...Why me and not Mion-san or Shion-san?'
 show beatrice_v001 smile at active
 show nao_v002 normal at inactive
 beatrice "Of course, it's because of {i}that{/i}! It's because I got along with you best!"
 hide beatrice_v001
 hide nao_v002
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 dlanor 'There is no ulterior MOTIVE. I can guarantee THAT.'
 hide dlanor_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao 'So then, this battle of wits between the witch and I has just been because she wanted to relieve herself of her boredom?'
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show nao_v002 normal at inactive
 erika 'That is the plan. Even witches tend to be lonely creatures.'
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 show beatrice_v001 normal_close at mei_center
 with Dissolve(0.5)
 show beatrice_v001 normal_close at active
 beatrice 'With that said, having the modesty to ask something like, "Please play with me.", is where witches fall short.'
 show beatrice_v001 smile at active
 beatrice 'It has been awfully fun playing this game with you. It was enough to cure me and bring me great happiness.'
 hide beatrice_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show nao_v002 normal at inactive
 erika 'How generous. Not worrying about the outcome of the game, just letting go and having fun.'
 show nao_v002 normal at active
 show erika_v001 normal at inactive
 nao "This isn't some secret plan to steal my soul or whatever if I lose, is it...?"
 hide erika_v001
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show nao_v002 normal at inactive
 dlanor 'That will not HAPPEN. As a first-class archbishop of the Great Court of Heaven, I, Dlanor A. Knox, will guarantee THAT.'
 show nao_v002 normal_close at active
 show dlanor_v001 normal at inactive
 nao '...........................'
 stop music fadeout 2.0
 hide nao_v002
 hide dlanor_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao "Very well. If that's the case..."
 play music 'audio/bgm/BGM_TITLE_COLLAB2.wav'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show nao_v002 smile at active
 nao 'Happy birthday, <Miss Beatrice>.'
 show nao_v002 normal at active
 nao "I humbly accept your challenge. ...It's just, I'm..."
 hide nao_v002
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_5001_sitdown2.wav'
 narrator 'Though it might be ill-mannered of me, I pulled up a chair and crossed my legs.'
 narrator 'This was no longer a dinner table, so I felt I could ignore a few manners. ...After all, this was a competition, a game to kill some boredom.'
 show nao_v002 sinken at mei_center
 with Dissolve(0.5)
 show nao_v002 sinken at active
 nao "...I'm rather competitive. Win or lose, I won't say I had fun."
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika '<Good>. I suppose you never fail to meet my expectations.'
 show erika_v001 normal at active
 erika 'I had felt that from your appearance when we were on the ferry, and it turns out my intuition was on point.'
 hide erika_v001
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_left
 show beatrice_v001 futeki at mei_right
 with Dissolve(0.5)
 show beatrice_v001 futeki at active
 show dlanor_v001 normal at inactive
 beatrice "I'm delighted, Nao! You really are an upstanding girl! Now, let us enjoy ourselves to our heart's content on this night!"
 show dlanor_v001 normal at active
 show beatrice_v001 futeki at inactive
 dlanor 'Nao... once again, I will explain the SITUATION.'
 show dlanor_v001 normal at active
 show beatrice_v001 futeki at inactive
 dlanor "A magic circle prank appeared in Erika's ROOM..."
 show beatrice_v001 futeki at active
 show dlanor_v001 normal at inactive
 beatrice 'I claim it was impossible for a human; therefore, it is the work of a witch!'
 hide dlanor_v001
 show nao_v002 sinken at mei_left
 with Dissolve(0.5)
 show nao_v002 sinken at active
 show beatrice_v001 futeki at inactive
 nao 'I posit that it was possible for a human to pull off this prank. And that human is none other than Erika-san!'
 hide beatrice_v001
 show erika_v001 futeki at mei_right
 with Dissolve(0.5)
 show erika_v001 futeki at active
 show nao_v002 sinken at inactive
 erika '*giggle*, <Good>. Please do come at me with all of your might.'
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 dlanor 'And so, Erika is a player once AGAIN.'
 hide dlanor_v001
 with Dissolve(0.2)
 show beatrice_v001 futeki at mei_right
 show nao_v002 odoroki at mei_left
 with Dissolve(0.5)
 show nao_v002 odoroki at active
 show beatrice_v001 futeki at inactive
 nao "What do you mean? This isn't just a fight between the witch and I?"
 show beatrice_v001 futeki at active
 show nao_v002 odoroki at inactive
 beatrice 'Tonight, we have a mêlée à trois! This will truly be entertaining!'
 hide beatrice_v001
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show nao_v002 odoroki at inactive
 erika 'Both I and Nao-chama claim that a Human pulled off this prank.'
 show nao_v002 normal at active
 show erika_v001 normal at inactive
 nao "We're working together?"
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide nao_v002
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 futeki at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 futeki at active
 erika 'Not quite. I believe that the culprit is Shion-san.'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 narrator 'I see. Three participants, each one claiming a different side.'
 camera at screenshake_transform
 pause 0.0
 narrator "With tonight's magic circle, it was either a magic trick poofed in by the witch, a farce performed by Erika-san, or a crime committed by Shion-san!"
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 dlanor 'For tonight, I believe I do have the responsibility of READER.'
 show dlanor_v001 normal at active
 dlanor 'For you three, I shall explain the SITUATION. ...Please listen CAREFULLY.'
 stop music fadeout 2.0
 show expression "#000" as fade with Dissolve(1.0)
 hide dlanor_v001
 with Dissolve(0.2)
 stop sound
 scene expression "#000"
 play music 'audio/bgm/BGM_QUEST3_COLLAB2.wav'
 show expression 'images/bg/AdvBg_2371.png' as bg
 with Dissolve(1.0)
 pause 1.0
 call wipeout_routine
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2281.png' as bg
 call wipein_routine
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 dlanor "This time, a magic circle was discovered inside of Erika's ROOM."
 show dlanor_v001 normal at active
 dlanor 'When Erika returned and unlocked the door, she discovered her bed was left RANSACKED. A magic circle was found drawn on the SHEETS.'
 hide dlanor_v001
 with Dissolve(0.2)
 narrator "...I want to confirm something here to boot, though I'll have to behave and lend my ears for now."
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 dlanor 'Earlier today, Erika forgot to lock her room until she returned to the guesthouse at NOON.'
 show dlanor_v001 normal at active
 dlanor 'Therefore, until the room was locked at noon, anybody could have entered the ROOM.'
 hide dlanor_v001
 with Dissolve(0.2)
 narrator "This was the crux. ...The point being that it's the same as last night's magic circle. Erika-san confirmed there was nothing weird inside her room when she locked it."
 narrator 'Normally, the crime would have occurred from that point onward... but it became a perfect closed room.'
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show expression "#e11" as fade with Dissolve(0.16666666666666666)
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 hide fade with Dissolve(0.16666666666666666)
 with Dissolve(0.16666666666666666)
 show dlanor_v001 normal at active
 dlanor '{umi_red}From the point the door is locked until Erika unlocks it, the room is a perfect closed ROOM.{/umi_red}'
 show expression "#e11" as fade with Dissolve(0.16666666666666666)
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 hide fade with Dissolve(0.16666666666666666)
 with Dissolve(0.16666666666666666)
 show dlanor_v001 normal at active
 dlanor '{umi_red}Nobody existed inside the room at that time, and nobody can enter by any other METHOD.{/umi_red}'
 show expression "#e11" as fade with Dissolve(0.16666666666666666)
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 hide fade with Dissolve(0.16666666666666666)
 with Dissolve(0.16666666666666666)
 show dlanor_v001 normal at active
 dlanor '{umi_red}The magic circle prank cannot be completed unless the person enters the ROOM.{/umi_red}'
 show dlanor_v001 normal_close at active
 dlanor 'That will be all for NOW. ...Everyone, please begin your INVESTIGATION...'
 hide dlanor_v001
 with Dissolve(0.2)
 narrator 'Us three players looked at each other with inquisitive expressions.'
 narrator 'It seems everyone is still theorycrafting. I was itching to ask questions and throw blue truths at Dlanor-san...'
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 dlanor "Now then, we shall BEGIN. Since it is Lady Beatrice's birthday, she has the privilege of going FIRST."
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide dlanor_v001
 hide fade with Dissolve(0.08333333333333333)
 show beatrice_v001 futeki at mei_center
 with Dissolve(0.08333333333333333)
 show beatrice_v001 futeki at active
 beatrice "Well, happy birthday to me!! Let's get started, then."
 show beatrice_v001 normal at active
 beatrice "When Erika returned, she unlocked her room and entered it, so there must have been a short interval before Nao's group heard her scream."
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide beatrice_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika "That is correct. Before I entered the room, I ensured that there wasn't any garbage packed into the keyhole, so a bit of time."
 hide erika_v001
 with Dissolve(0.2)
 narrator "...Why is Beatrice focusing on that? My plan of attack was centered on Erika-san's acting..."
 show dlanor_v001 normal at mei_left
 show beatrice_v001 normal at mei_right
 with Dissolve(0.5)
 show beatrice_v001 normal at active
 show dlanor_v001 normal at inactive
 beatrice "Let's dash Nao's hopes. Dlanor, repeat this in red."
 show beatrice_v001 normal at active
 show dlanor_v001 normal at inactive
 beatrice '"From the time Erika entered her room to the time Nao\'s group entered after hearing her scream, it was impossible to place the magic circle."'
 show dlanor_v001 normal at active
 show beatrice_v001 normal at inactive
 dlanor 'Request GRANTED.'
 show expression "#e11" as fade with Dissolve(0.16666666666666666)
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 hide fade with Dissolve(0.16666666666666666)
 with Dissolve(0.16666666666666666)
 show dlanor_v001 normal at active
 show beatrice_v001 normal at inactive
 dlanor "{umi_red}From the time Erika entered her room to the time Nao's group entered after hearing her scream, it was impossible to place the magic CIRCLE.{/umi_red}"
 hide dlanor_v001
 hide beatrice_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao 'Umm, so does that include everyone other than Erika-san?'
 hide nao_v002
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 dlanor 'YES.'
 show expression "#e11" as fade with Dissolve(0.16666666666666666)
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 hide fade with Dissolve(0.16666666666666666)
 with Dissolve(0.16666666666666666)
 show dlanor_v001 normal at active
 dlanor '{umi_red}From the time Erika entered her room, it was impossible to place the magic circle by any kind of METHOD.{/umi_red}'
 hide dlanor_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show nao_v002 normal at inactive
 erika "Thank you very much for clearing up those false accusations for me. See? See how I wasn't acting? I just needed more time."
 show nao_v002 normal_close at active
 show erika_v001 normal at inactive
 nao '...How terrible. But this was still the same as what happened to my bed...'
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 narrator 'So, the only time it was possible to place the magic circle was before Erika-san locked her room...'
 narrator "It's the same as yesterday. The magic circle then could only be placed before Shannon-san locked the window."
 narrator 'And in both cases, people confirmed nothing was wrong when they entered the room...'
 show beatrice_v001 futeki at mei_center
 with Dissolve(0.5)
 show beatrice_v001 futeki at active
 beatrice 'My turn ends here. *cackle*cackle*cackle*'
 hide beatrice_v001
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 dlanor 'Now then, as we do traditionally, we will go in a clockwise DIRECTION.'
 show dlanor_v001 normal at active
 dlanor 'Next up is ERIKA.'
 show erika_v001 normal_close at mei_right
 with Dissolve(0.5)
 show erika_v001 normal_close at active
 show dlanor_v001 normal at inactive
 erika 'Well then. *ahem*'
 show erika_v001 normal at active
 show dlanor_v001 normal at inactive
 erika "I think this will be much too complicated with three players, so I'll make this quick. Nao-san, you should drop out."
 hide dlanor_v001
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show erika_v001 normal at inactive
 nao '...Thought you might say that. I would have said the same thing if I were you.'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide erika_v001
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 normal at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 normal at active
 erika "*giggle*giggle*giggle*. ...Anyway, I'm going to talk about the differences between the two magic circles seen today and yesterday."
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show nao_v002 normal at mei_left
 show beatrice_v001 normal at mei_right
 with Dissolve(0.5)
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice 'Hoh? Differences, you say?'
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao '...I thought they were the same circle though......'
 show expression "#000" as fade with Dissolve(1.0)
 hide nao_v002
 hide beatrice_v001
 with Dissolve(0.2)
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2320.png' as bg
 with Dissolve(1.0)
 dlanor 'Over here is the first magic circle, and over here is the SECOND. Please compare THEM.'
 beatrice '...Hmm......? How are they different?'
 show expression "#000" as fade with Dissolve(1.0)
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2281.png' as bg
 with Dissolve(1.0)
 show erika_v001 normal at mei_right
 show nao_v002 sinken at mei_left
 with Dissolve(0.5)
 show nao_v002 sinken at jump_transform,active
 show erika_v001 normal at inactive
 nao '...Ah...... there!'
 show erika_v001 normal at active
 show nao_v002 sinken at inactive
 erika '<Good>. Nao-chama has noticed it, and very quickly at that.'
 hide erika_v001
 hide nao_v002
 with Dissolve(0.2)
 show beatrice_v001 fuan at mei_center
 with Dissolve(0.5)
 show beatrice_v001 fuan at active
 beatrice 'Eh? What? ...Is this some kinda Spot the Difference puzzle???'
 hide beatrice_v001
 with Dissolve(0.2)
 show erika_v001 normal at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show erika_v001 normal at inactive
 nao 'I happen to have a photographic memory.'
 show erika_v001 normal at active
 show nao_v002 normal at inactive
 erika 'A photographic memory... an invaluable tool for a detective.'
 show nao_v002 normal_close at active
 show erika_v001 normal at inactive
 nao "I was panicking yesterday and was in shock, so I assumed that today's magic circle was the exact same..."
 show nao_v002 normal at active
 show erika_v001 normal at inactive
 nao 'There. See these letters surrounding the magic circle in a ring? ... This one specifically is different.'
 hide erika_v001
 show beatrice_v001 sinken at mei_right
 with Dissolve(0.5)
 show beatrice_v001 sinken at active
 show nao_v002 normal at inactive
 beatrice "Hmmm, I see... This letter should be a little swirl, but instead, it's two circles."
 show nao_v002 smile at active
 show beatrice_v001 sinken at inactive
 nao 'Indeed. I doubt this was a simple drawing error. This same symbol appears in 3 other places.'
 show beatrice_v001 sinken at active
 show nao_v002 smile at inactive
 beatrice 'That there are! There are double circles in three spots where there should be swirls! ...What on earth is this?!'
 hide nao_v002
 hide beatrice_v001
 with Dissolve(0.2)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika 'If you look closely, you can detect many other minute differences.'
 show expression "#000" as fade with Dissolve(1.0)
 hide erika_v001
 with Dissolve(0.2)
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2190.png' as bg
 with Dissolve(1.0)
 show dlanor_v001 normal at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show dlanor_v001 normal at inactive
 erika 'After putting together these clues, I would like to request you to repeat something, Dlanor.'
 show dlanor_v001 normal at active
 show erika_v001 normal at inactive
 dlanor 'Go ahead, ERIKA.'
 hide dlanor_v001
 hide erika_v001
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_204_shot.wav'
 show expression "#fff" as flash with Dissolve(0.1)
 pause 0.1
 hide flash with Dissolve(0.2)
 narrator 'Do repeat this in red: "The two magic circles were drawn onto two separate sheets by different people."'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide fade with Dissolve(0.08333333333333333)
 show nao_v002 sinken at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show nao_v002 sinken at active
 nao '.........?!?!'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show erika_v001 normal at mei_left
 show beatrice_v001 normal at mei_right
 with Dissolve(0.5)
 show beatrice_v001 normal at active
 show erika_v001 normal at inactive
 beatrice "I see... So you want to prove that this all wasn't an act."
 show beatrice_v001 normal at active
 show erika_v001 normal at inactive
 beatrice "But if that's the case... won't you have to to admit it...?"
 show erika_v001 normal at active
 show beatrice_v001 normal at inactive
 erika "*giggle*. I don't mind at all saying that."
 show erika_v001 normal at active
 show beatrice_v001 normal at inactive
 erika 'Well, Dlanor? Will you do the honors?'
 hide erika_v001
 hide beatrice_v001
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 dlanor '...YES. Sorry for the WAIT. I shall repeat IT.'
 play sound ['audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav'] fadeout 1.0
 show expression "#e11" as fade with Dissolve(0.16666666666666666)
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 hide fade with Dissolve(0.16666666666666666)
 with Dissolve(0.16666666666666666)
 show dlanor_v001 normal at active
 dlanor '{umi_red}The two magic circles were drawn onto two separate sheets by different PEOPLE.{/umi_red}'
 hide dlanor_v001
 with Dissolve(0.2)
 show erika_v001 normal_close at mei_center
 with Dissolve(0.5)
 show erika_v001 normal_close at active
 erika 'Do a C.O. as well.'
 hide erika_v001
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_right
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at active
 show dlanor_v001 normal at inactive
 nao 'C.O.?'
 show dlanor_v001 normal at active
 show nao_v002 fuan at inactive
 dlanor '"Coming OUT".  The disclosure of information that only you aren\'t aware of, or a CONFESSION.'
 hide dlanor_v001
 hide nao_v002
 with Dissolve(0.2)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika 'That first magic circle was drawn by me, Erika-san.'
 hide erika_v001
 with Dissolve(0.2)
 show erika_v001 normal at mei_right
 show nao_v002 sinken at mei_left
 with Dissolve(0.5)
 camera at screenshake_transform
 pause 0.0
 show nao_v002 sinken at active
 show erika_v001 normal at inactive
 nao 'See, so you really were the culprit after all!!'
 show erika_v001 normal at active
 show nao_v002 sinken at inactive
 erika "Oh quiet. It was just a prank, wasn't it? And you {i}are{/i} aware bringing personal grudges into this game is boorish, correct?"
 hide nao_v002
 show beatrice_v001 normal at mei_left
 with Dissolve(0.5)
 show beatrice_v001 normal at active
 show erika_v001 normal at inactive
 beatrice "We already knew Erika was the perpetrator behind that first magic circle. That said, how Shannon didn't notice the magic circle at all is still a mystery, isn't it?"
 show beatrice_v001 normal at active
 show erika_v001 normal at inactive
 beatrice 'If you want to deny Erika as a witch, you must show how she tricked Shannon.'
 show erika_v001 normal_close at active
 show beatrice_v001 normal at inactive
 erika 'On top of that, you must present it in the form of a blue truth. ...That does it for my turn.'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide erika_v001
 hide beatrice_v001
 hide fade with Dissolve(0.08333333333333333)
 show beatrice_v001 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show beatrice_v001 sinken at active
 beatrice "......That being said... I still don't understand this magic circle at all. ...Just why was it made that way?"
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide beatrice_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao '.....................?'
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show nao_v002 normal at inactive
 dlanor "Thank you for WAITING. It is now Nao's TURN."
 stop music fadeout 2.0
 show nao_v002 normal_close at active
 show dlanor_v001 normal at inactive
 nao '...........................'
 hide nao_v002
 hide dlanor_v001
 with Dissolve(0.2)
 narrator 'Inside my head, many thoughts swirled around like soup.'
 narrator '...It feels like the ingredients came together and began to boil. ...Could it be......'
 show dlanor_v001 normal at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show dlanor_v001 normal at inactive
 nao '...Dlanor-san, a question.'
 show dlanor_v001 normal at active
 show nao_v002 normal at inactive
 dlanor 'What is IT?'
 play music 'audio/bgm/BGM_QUEST7_COLLAB2.wav'
 show nao_v002 normal at active
 show dlanor_v001 normal at inactive
 nao "In Erika-san's C.O., she admitted that she was the culprit behind the first magic circle."
 show nao_v002 normal at active
 show dlanor_v001 normal at inactive
 nao 'Is that confession as good as red truth?'
 hide dlanor_v001
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show nao_v002 normal at inactive
 erika 'No. It is not red, so it may contain some lies.'
 show nao_v002 normal at active
 show erika_v001 normal at inactive
 nao 'But, Erika-san, can you still repeat it?'
 show erika_v001 normal at nod_transform,active
 show nao_v002 normal at inactive
 erika "Why yes, how could I not? Of course, I'll have you state it for me first."
 show nao_v002 normal at active
 show erika_v001 normal at inactive
 nao 'Well then, please repeat this:'
 show expression "#fff" as flash with Dissolve(0.1)
 pause 0.1
 hide flash with Dissolve(0.2)
 show nao_v002 normal at active
 show erika_v001 normal at inactive
 nao '"The one who created the first magic circle and placed it was Erika-san."'
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 narrator "......For a moment, I saw hesitation in Erika-san's eyes. I bet she was thinking about how to answer this in such a way as to confuse me more."
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika "I'll respond."
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show expression "#e11" as fade with Dissolve(0.16666666666666666)
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 hide fade with Dissolve(0.16666666666666666)
 with Dissolve(0.16666666666666666)
 show erika_v001 normal at active
 erika '{umi_red}The one who created the first magic circle and placed it was Erika Furudo.{/umi_red}'
 show erika_v001 normal at active
 erika "However, how and when I placed it and how I tricked Shannon-san are things I refuse to answer. I do hope you'll forgive me."
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
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 dlanor "Nao's turn is now OVER. Lady Beatrice may go AGAIN."
 hide dlanor_v001
 with Dissolve(0.2)
 narrator '...I used up my precious turn to confirm something I already knew.'
 narrator "My opponents are seriously Erika-san and that witch? ...I couldn't win this three-way fight if the other sides united against me."
 show dlanor_v001 normal at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show dlanor_v001 normal at inactive
 nao '...Dlanor-san, can you go over the rules once more please?'
 show nao_v002 normal at active
 show dlanor_v001 normal at inactive
 nao 'This three-way fight can only have one winner, right?'
 show dlanor_v001 normal at active
 show nao_v002 normal at inactive
 dlanor 'Two winners are POSSIBLE.'
 show nao_v002 smile at active
 show dlanor_v001 normal at inactive
 nao '......Thank you. Beatrice was next, right?'
 show nao_v002 normal at active
 show dlanor_v001 normal at inactive
 nao "Though, I wonder if you're going to corner me...?"
 hide dlanor_v001
 show beatrice_v001 smile at mei_right
 with Dissolve(0.5)
 show beatrice_v001 smile at active
 show nao_v002 normal at inactive
 beatrice "I don't care about winning or losing, this game is purely for entertainment. I still intend to have a fair fight, however."
 show beatrice_v001 smile at active
 show nao_v002 normal at inactive
 beatrice 'I attacked Nao just now, so next, I will place my attack on Erika.'
 hide nao_v002
 show erika_v001 normal at mei_left
 with Dissolve(0.5)
 show erika_v001 normal at active
 show beatrice_v001 smile at inactive
 erika 'Do as you wish.'
 hide beatrice_v001
 hide erika_v001
 with Dissolve(0.2)
 narrator '...Erika-san is definitely gunning for me. She wants to claim victory, but she also wants me to lose more than anything.'
 narrator 'Meanwhile, I sense no ill will at all from Beatrice. She just wants to have a fair game. ...Of course, with the way things are playing out, she might press on if victory is in sight.'
 narrator '...Maybe, as Erika-san and I hold our positions... I can try to pull Beatrice over to my side...'
 narrator 'For me to win, I need to prove Erika-san was acting.'
 narrator 'For Beatrice to win, she must prove the crime was impossible for humans......'
 show dlanor_v001 normal at mei_right
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at active
 show dlanor_v001 normal at inactive
 nao '...Dlanor-san, excuse me again. I would like to confirm something else...'
 show dlanor_v001 normal at active
 show nao_v002 fuan at inactive
 dlanor 'Rest ASSURED. I will listen to what you have to SAY.'
 show nao_v002 fuan at active
 show dlanor_v001 normal at inactive
 nao 'Ah... um.'
 hide dlanor_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator 'I gave an awkward look and motioned for Dlanor-san to come over for a private talk, and she understood immediately.'
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 dlanor 'We can WHISPER. It is not an ISSUE.'
 hide dlanor_v001
 with Dissolve(0.2)
 narrator 'No matter the game, the very act of checking a rule could reveal your hand.'
 narrator "I especially didn't want Erika-san to hear me..."
 show erika_v001 normal at mei_left
 show beatrice_v001 smile at mei_right
 with Dissolve(0.5)
 show beatrice_v001 smile at active
 show erika_v001 normal at inactive
 beatrice 'Hmm-hmm, having a private chat, are we?'
 show erika_v001 normal at active
 show beatrice_v001 smile at inactive
 erika 'Who knows? Well, she is a novice, so we must lend her our support.'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide erika_v001
 hide beatrice_v001
 hide fade with Dissolve(0.08333333333333333)
 show dlanor_v001 normal_close at mei_center
 with Dissolve(0.08333333333333333)
 show dlanor_v001 normal_close at active
 dlanor '...Mm-HMM. ......I SEE.'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide dlanor_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 narrator "My face was pressed against Dlanor-san's as we spoke in hushed tones."
 narrator '...She smelled nice. This was a fragrance I had never experienced before. ...I wanted to press my nose against her hair and take it all in...'
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika "Dlanor gives off an audaciously bewitching scent, doesn't she?"
 show erika_v001 smile at active
 erika 'I have a good nose, so I can smell her from a mile away. *giggle*giggle*'
 hide erika_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_left
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show nao_v002 normal at inactive
 dlanor '...Nao, there is no issue at ALL.'
 show dlanor_v001 normal at active
 show nao_v002 normal at inactive
 dlanor 'The first magic circle was proven to be possible for a Human, but if the second magic circle was proven IMPOSSIBLE...'
 show nao_v002 normal at active
 show dlanor_v001 normal at inactive
 nao 'Then Beatrice and I would be the winners...'
 show dlanor_v001 normal at active
 show nao_v002 normal at inactive
 dlanor 'However, as the reciter, this is nothing more than just a whisper to ME.'
 show dlanor_v001 normal at active
 show nao_v002 normal at inactive
 dlanor 'You are free to tell Lady Beatrice and ally with her; however, Erika-san will hear it as WELL.'
 hide nao_v002
 hide dlanor_v001
 with Dissolve(0.2)
 narrator 'Alright, <good>. ......Is that how you say it?'
 narrator 'Erika-san, I hate losing. I will win with certainty. And I {i}will{/i} uncover the secrets of these two magic circles.'
 narrator 'Erika-san, I learned it from you. This battle of wits was more like a fistfight.'
 narrator 'The victor will be the one who amasses all claims, all logic, and all evidence... so that they can beat the enemy down thoroughly.'
 camera at screenshake_transform
 pause 0.0
 narrator 'I will win, and I WILL defeat her!'
 show erika_v001 normal at mei_right
 show nao_v002 sinken at mei_left
 with Dissolve(0.5)
 show nao_v002 sinken at active
 show erika_v001 normal at inactive
 nao '........................'
 show erika_v001 futeki at active
 show nao_v002 sinken at inactive
 erika '...<Good>.'
 return