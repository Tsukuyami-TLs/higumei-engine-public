label chara032009_03:
 show black_background onlayer black
 $ event_store.current_event='chara032009'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara032009_03'
 camera:
  anchor (0.5, 0.5)
  pos (960, 540)
 scene
 stop music
 stop sound
 show expression 'images/bg/AdvBg_2201.png' as bg
 play music "<loop 3.16>audio/bgm/BGM_QUEST.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 nao "(And so, I landed down on Beatrice's game board.)"
 nao '(The title is "Ougon no Majo no Densetsu" ...Legend of the Golden Witch.)'
 nao '(There, I lurked in "Battler Ushiromiya-san\'s" shadow, being allowed to spectate what he sees and hears from start to finish.)'
 nao '(October 4th, 1986: 5 days until I witness and lend my ears to the aftermath of Rokkenjima...)'
 nao "(A mysterious epitaph written below the portrait. Locked-room murder incidents following the message. Various speculation surrounding of the witch's gold. And then...)"
 nao "(--the island's hidden Golden Land...)"
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_2190.png' as bg
 show beatrice_v001 normal_close at mei_right
 with Dissolve(0.5)
 hide fade onlayer curtain
 with Dissolve(1.0)
 pause 1.0
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show beatrice_v001 normal_close at inactive
 nao '...Alright, there we go.'
 show beatrice_v001 smile at jump_transform,active
 show nao_v002 normal at inactive
 beatrice 'Ooh, have you finished, Nao!?'
 show nao_v002 normal at active
 show beatrice_v001 smile at inactive
 nao 'Yes, although the one who closed the curtains on this tale was Battler...'
 show nao_v002 fuan at active
 show beatrice_v001 smile at inactive
 nao 'But, I wonder if the expression "closed the curtains" is accurate...?'
 show beatrice_v001 smile_close at active
 show nao_v002 fuan at inactive
 beatrice '*cackle*cackle*cackle*, I get what you\'re trying to say. It was essentially a "Time Over" ending where the clock ran out.'
 show beatrice_v001 smile at active
 show nao_v002 fuan at inactive
 beatrice 'Instead of saying the story "was brought to an end", the saying "incidentally reached the end" would be more appropriate.'
 show beatrice_v001 normal at active
 show nao_v002 fuan at inactive
 beatrice 'And thus... how was my game board?'
 show nao_v002 normal_close at active
 show beatrice_v001 normal at inactive
 nao 'I see. If there is one way to say it...'
 show beatrice_v001 normal at active
 show nao_v002 normal_close at inactive
 beatrice 'If there is?'
 show nao_v002 sinken at active
 show beatrice_v001 normal at inactive
 nao "...It's tasteless."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide beatrice_v001
 hide nao_v002
 hide fade onlayer curtain
 show beatrice_v001 futeki at mei_center
 with Dissolve(0.08333333333333333)
 show beatrice_v001 futeki at updown_shake_transform,active
 beatrice 'Pff... *cackle*cackle*cackle*, hyyyaaahahahahaha! Is that so, is that so? Tasteless!?'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide beatrice_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show beatrice_v001 futeki at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show beatrice_v001 futeki at inactive
 nao "Like really, I don't even think I could say the locked-room murders aligning with the epitaph was tasteful."
 show nao_v002 normal_close at active
 show beatrice_v001 futeki at inactive
 nao "Well... I'm not saying it's in {i}bad{/i} taste, and it isn't entirely tasteless either."
 show beatrice_v001 normal at active
 show nao_v002 normal_close at inactive
 beatrice '...Hm?'
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao "We don't know how much of that story is real, as well as how much of it is a lie. I feel like this is because there are tricks scattered about here and there to deceive readers."
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice '...Hm, you mean the lie that I exist?'
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao "I don't think so. But after having spectated the game board through Battler's eyes..."
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao "In essence, they aren't my own eyes. Someone else's perspectives and biases are also included."
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice "If you were to see with your own eyes, it would all be revealed. Again, the witch's existence isn't being believed in... is that so?"
 show nao_v002 smile at active
 show beatrice_v001 normal at inactive
 nao "It's not like I'm completely denying it. If I were, then who would I be talking to right now? But..."
 show nao_v002 normal_close at active
 show beatrice_v001 normal at inactive
 nao "What I mean is taking in all of someone else's story without questioning it. I should be able to check whether or not that information is correct by properly verifying it through my own investigation..."
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao "In doing that, information becomes knowledge, and you can become educated... That's what my mom taught me."
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao 'So, even if I actually go to that place myself, I believe that not seeing things with my eyes and not feeling things disables me from making a foundation for my conclusions.'
 show beatrice_v001 fuan at active
 show nao_v002 normal at inactive
 beatrice "...I don't know whether you are a doubtful or thoughtful child."
 show nao_v002 smile at active
 show beatrice_v001 fuan at inactive
 nao "Sorry, that's just how I am... but I have to admit it's not all bad taste either."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide beatrice_v001
 hide nao_v002
 hide fade onlayer curtain
 show nao_v002 normal at mei_center
 with Dissolve(0.08333333333333333)
 show nao_v002 normal at active
 nao "The story's purpose is to tell a possible truth of what might have occurred on the island..."
 show nao_v002 normal_close at active
 nao "Well, I think it's trying to convey some sort of message."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show nao_v002 normal_close at mei_left
 show beatrice_v001 normal at mei_right
 with Dissolve(0.5)
 show beatrice_v001 normal at active
 show nao_v002 normal_close at inactive
 beatrice '...Hoh. Why would you think that?'
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao 'Because I still haven\'t been able to discover the theme of "Legend of the Golden Witch".'
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice 'The theme?'
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao "All the stories that I've read have had some sort of theme. Whether or not it fits my tastes is another matter."
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao 'Basically, stories require a theme, right?'
 show nao_v002 fuan_close at active
 show beatrice_v001 normal at inactive
 nao "But, if I can't find the theme, then it was likely hidden in a clever way... it means I'm lacking in some way."
 show nao_v002 smile at active
 show beatrice_v001 normal at inactive
 nao "Maybe if I reread the story few times I'll understand. Ah, or if there's a continuation?"
 show beatrice_v001 normal_close at active
 show nao_v002 smile at inactive
 beatrice '... How can you be so sure a theme has been hidden?'
 show nao_v002 normal at active
 show beatrice_v001 normal_close at inactive
 nao 'Because I can.'
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show nao_v002 smile at active
 show beatrice_v001 normal_close at inactive
 nao 'Like this story... it was really amusing.'
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 show beatrice_v001 normal at active
 show nao_v002 smile at inactive
 beatrice '............'
 show nao_v002 fuan at active
 show beatrice_v001 normal at inactive
 nao 'Beatrice?'
 camera at screenshake_transform
 pause 0.0
 show beatrice_v001 futeki at active
 show nao_v002 fuan at inactive
 beatrice '*cackle*cackle*... *cackle*cackle*cackle*cackle!!! Hahahahahaha! Ahaaahahahahahahahaha!!!'
 show nao_v002 fuan at active
 show beatrice_v001 futeki at inactive
 nao "Huh... wait, what happened?! Is my opinion that dissatisfying? Sorry it wasn't up to your expectations, but..."
 show beatrice_v001 smile_close at active
 show nao_v002 fuan at inactive
 beatrice "No, that's not it! That's not it!"
 show beatrice_v001 smile at active
 show nao_v002 fuan at inactive
 beatrice 'I admire you for reading that story, and flat out declaring it as amusing!'
 show beatrice_v001 smile at active
 show nao_v002 fuan at inactive
 beatrice 'I get it now! To think that something like having a story read to you by a miko could be this entertaining...!'
 show beatrice_v001 futeki_close at active
 show nao_v002 fuan at inactive
 beatrice 'In all of my 1,000 years of living, discovering something new is just... *cackle*cackle*cackle*!!'
 show nao_v002 fuan at active
 show beatrice_v001 futeki_close at inactive
 nao 'I wonder if a... thank you is right here?'
 show beatrice_v001 smile at active
 show nao_v002 fuan at inactive
 beatrice "*giggle*... I've had a lot of fun, Nao. If another chance arises, it would be grand if you came again to read another game board I put together."
 show beatrice_v001 smile_close at active
 show nao_v002 fuan at inactive
 beatrice "As long as it's you, I'd welcome you with open arms... But alas, you will have to deal with needing permission from that guest, it seems."
 show nao_v002 normal at active
 show beatrice_v001 smile_close at inactive
 nao 'Permission...?'
 show beatrice_v001 smile at active
 show nao_v002 normal at inactive
 beatrice 'Mhm... if they have another fit of rage, they may use magic to wipe your memory again.'
 show beatrice_v001 smile at active
 show nao_v002 normal at inactive
 beatrice "But don't worry. If you close your eyes, you will return to your original world."
 show nao_v002 odoroki at jump_transform,active
 show beatrice_v001 smile at inactive
 nao "...Huh, this is the end?! You're not going to keep reading it for me?!"
 show beatrice_v001 normal_close at active
 show nao_v002 odoroki at inactive
 beatrice 'Come, try to remember...'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide nao_v002
 hide beatrice_v001
 hide fade onlayer curtain
 show nao_v002 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show nao_v002 sinken at active
 nao 'Wait...!'
 stop music fadeout 0.5
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_351.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_528_unfold_cloth.wav'
 camera at screenshake_transform
 pause 0.0
 show nao_v002 sinken at active
 nao 'I want to know how it continueeees!!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 play music "<loop 2.36>audio/bgm/BGM_EVENT1.ogg"
 show rika_v002 odoroki at mei_center
 with Dissolve(0.5)
 show rika_v002 odoroki at active
 rika 'Huh?'
 hide rika_v002
 with Dissolve(0.2)
 show hanyuu_v002 odoroki at mei_right
 show satoko_v002 fuan at mei_left
 with Dissolve(0.5)
 show satoko_v002 fuan at active
 show hanyuu_v002 odoroki at inactive
 satoko 'Wh-what happened, Nao-san?'
 show hanyuu_v002 sinken at active
 show satoko_v002 fuan at inactive
 hanyuu "Au au, this is the library. If you won't be quiet, it could get bad~!"
 hide satoko_v002
 show rika_v002 fuan at mei_left
 with Dissolve(0.5)
 show rika_v002 fuan at active
 show hanyuu_v002 sinken at inactive
 rika 'Hanyuu is also speaking in a loud voice.'
 show hanyuu_v002 fuan at active
 show rika_v002 fuan at inactive
 hanyuu "Huh?! I-I'm sorry..."
 hide rika_v002
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at active
 show hanyuu_v002 fuan at inactive
 nao 'Ah, umm, was I sleeping, just now?'
 hide hanyuu_v002
 show rika_v002 smile at mei_right
 with Dissolve(0.5)
 show rika_v002 smile at active
 show nao_v002 fuan at inactive
 rika 'Meep. While we were waiting for you to teach Satoko how to improve the writing in her book report, Nao got sleepy.'
 hide rika_v002
 show satoko_v002 fuan at mei_right
 with Dissolve(0.5)
 show satoko_v002 fuan at active
 show nao_v002 fuan at inactive
 satoko 'M-my apologies... because I took so much time, Nao-san had gotten bored...'
 show nao_v002 fuan at active
 show satoko_v002 fuan at inactive
 nao "Ah, I don't think you really have to apologize but..."
 hide satoko_v002
 show hanyuu_v002 normal at mei_right
 with Dissolve(0.5)
 show hanyuu_v002 normal at active
 show nao_v002 fuan at inactive
 hanyuu 'At any rate, "I want to know how it continues"... what was that about?'
 show nao_v002 odoroki at active
 show hanyuu_v002 normal at inactive
 nao 'Huh? U-Umm... I wonder what that was too. For some reason I feel like I was reading an interesting book in the middle of my dream.'
 show nao_v002 normal at active
 show hanyuu_v002 normal at inactive
 nao '............'
 hide hanyuu_v002
 show satoko_v002 fuan at mei_right
 with Dissolve(0.5)
 show satoko_v002 fuan at active
 show nao_v002 normal at inactive
 satoko 'Nao-san?'
 show nao_v002 normal at active
 show satoko_v002 fuan at inactive
 nao '...Hey, Satoko. If it takes you a long time to write your report, could I go check out a book maybe?'
 show satoko_v002 fuan at active
 show nao_v002 normal at inactive
 satoko "You're the one keeping us company here, so that's fine, but... was there a book you would like to read?"
 show nao_v002 smile at nod_transform,active
 show satoko_v002 fuan at inactive
 nao 'Yes, I believe I would like to read a mystery.'
 hide satoko_v002
 show hanyuu_v002 odoroki at mei_right
 with Dissolve(0.5)
 show hanyuu_v002 odoroki at active
 show nao_v002 smile at inactive
 hanyuu 'Au... Mystery?'
 show nao_v002 smile_close at active
 show hanyuu_v002 odoroki at inactive
 nao "For some reason, I've suddenly developed a strong desire to research the mystery genre."
 show nao_v002 smile at active
 show hanyuu_v002 odoroki at inactive
 nao "For now, let's see how many famous mystery novels I can check out..."
 hide hanyuu_v002
 show rika_v002 odoroki at mei_right
 with Dissolve(0.5)
 show rika_v002 odoroki at active
 show nao_v002 smile at inactive
 rika 'Meep. Where did this come from?'
 show nao_v002 smile at active
 show rika_v002 odoroki at inactive
 nao "I don't know. I just think it'd be fun to see the rest of the dream..."
 show nao_v002 smile_close at active
 show rika_v002 odoroki at inactive
 nao "But it's just a feeling, yeah? *giggle*"
 call chapter_end
 return