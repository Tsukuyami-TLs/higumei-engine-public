label chara032009_03:
 show black_background onlayer black
 $ event_store.current_event='chara032009'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara032009_03'
 $ persistent.menu_return='chara'
 camera:
  anchor (0.5, 0.5)
  pos (960, 540)
  matrixcolor IdentityMatrix()
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
 nao '(Through his eyes and ears, I bear witness to the Rokkenjima of the 4th and 5th of October in 1986...)'
 nao "(The mysterious epitaph written below the portrait imitates the locked-room murder incidents, containing various prophecies regarding the pursuit of the witch's gold, including...)"
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
 beatrice 'Ooh, have you finished, Nao?!'
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
 beatrice 'Instead of saying the story "was brought to an end", the saying "has incidentally reached the end" would be more appropriate.'
 show beatrice_v001 normal at active
 show nao_v002 fuan at inactive
 beatrice 'And thus... how was my game board?'
 show nao_v002 normal_close at active
 show beatrice_v001 normal at inactive
 nao "I see. If there's one way to say it..."
 show beatrice_v001 normal at active
 show nao_v002 normal_close at inactive
 beatrice 'If there is?'
 show nao_v002 sinken at active
 show beatrice_v001 normal at inactive
 nao "...It's in bad taste."
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
 beatrice 'Pff... *cackle*cackle*cackle*, hyyyaaahahahahaha! Really, is that so? Bad taste!?'
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
 nao "Well... I'm not saying it's {i}tasteless{/i}. Because it isn't entirely in bad taste."
 show beatrice_v001 normal at active
 show nao_v002 normal_close at inactive
 beatrice '...Hm?'
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao "I don't know how much of that story is real, as well as how much of it is a lie. I feel like this is because there are tricks scattered about here and there to deceive readers."
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice '...Hm, are you saying my existence is a lie?'
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao "I don't think so. But after having spectated the game board through Battler-san's eyes..."
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao "In essence, they aren't my own eyes. Someone else's perspectives and biases are also included."
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice "Without being able to see with your own eyes, the full truth is unable to be seen... So you're saying the witch's existence isn't being believed in again...?"
 show nao_v002 smile at active
 show beatrice_v001 normal at inactive
 nao "It's not like I'm completely denying it. If I were, then who would I be talking to right now? But..."
 show nao_v002 normal_close at active
 show beatrice_v001 normal at inactive
 nao "What I'm talking about is chewing before you swallow. Checking whether or not information is correct by properly verifying it through your own investigation..."
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao "In doing this, information becomes knowledge, and that's how you become educated... That's what my mom taught me."
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao 'So, even if I actually go to that place myself, I believe that not being able to use my own body to observe disables me from making a foundation for my conclusions.'
 show beatrice_v001 fuan at active
 show nao_v002 normal at inactive
 beatrice "...I don't know whether you are a doubtful or thoughtful child."
 show nao_v002 smile at active
 show beatrice_v001 fuan at inactive
 nao "Sorry, that's just how I am... but it not being just bad taste is my straight-forward opinion."
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
 nao "Well, I feel like it's trying to convey some sort of message."
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
 nao "All the stories that I've read have had some sort of theme. This is different from whether it suits one's tastes or not."
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao 'Basically, stories require a theme, right?'
 show nao_v002 fuan_close at active
 show beatrice_v001 normal at inactive
 nao "But, if I can't find the theme, then it was likely hidden in a clever way... which means that I'm lacking in some way."
 show nao_v002 smile at active
 show beatrice_v001 normal at inactive
 nao "Maybe if I reread the story few times I'll understand. Ah, unless there's more I can read?"
 show beatrice_v001 normal_close at active
 show nao_v002 smile at inactive
 beatrice '...How can you be so sure that a theme has been hidden?'
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
 nao 'Because this story... was really amusing.'
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
 beatrice 'I admire you for reading that story and flat out declaring it as amusing!'
 show beatrice_v001 smile at active
 show nao_v002 fuan at inactive
 beatrice 'I get it now! To think that having a story read to you by a miko could be this entertaining...!'
 show beatrice_v001 futeki_close at active
 show nao_v002 fuan at inactive
 beatrice 'After living for one thousand years, discovering something new is just... *cackle*cackle*cackle*!!'
 show nao_v002 fuan at active
 show beatrice_v001 futeki_close at inactive
 nao 'I-I wonder if a... thank you is right here?'
 show beatrice_v001 smile at active
 show nao_v002 fuan at inactive
 beatrice "*giggle*... I've had a lot of fun, Nao. If another chance arises, it would be grand if you came again to read another game board I put together."
 show beatrice_v001 smile_close at active
 show nao_v002 fuan at inactive
 beatrice "As long as it's you, I'd welcome you with open arms... But alas, it appears you will have to deal with needing permission from that guest."
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
 hanyuu "Au au, this is the library. If you don't be quiet, it could get bad~!"
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
 satoko 'M-My apologies... Nao-san had gotten bored because I took up so much time...'
 show nao_v002 fuan at active
 show satoko_v002 fuan at inactive
 nao "Ah, I don't really think you have to apologize..."
 hide satoko_v002
 show hanyuu_v002 normal at mei_right
 with Dissolve(0.5)
 show hanyuu_v002 normal at active
 show nao_v002 fuan at inactive
 hanyuu 'At any rate, "I want to know how it continues."... what was that about?'
 show nao_v002 odoroki at active
 show hanyuu_v002 normal at inactive
 nao 'Huh? U-Umm... I wonder what that was too. Somehow I feel like I was reading an interesting book in my dream, though.'
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
 satoko 'I was the one following along with you, but sure... \nWas there a book you wanted to read?'
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
 nao "Not sure. I just have a feeling that I'll be able to enjoy the rest of my dream this way."
 show nao_v002 smile_close at active
 show rika_v002 odoroki at inactive
 nao "But it's just a feeling, you know? *giggle*"
 call chapter_end
 return