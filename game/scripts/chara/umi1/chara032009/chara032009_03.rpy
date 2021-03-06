label chara032009_03:
 show black_background onlayer black
 $ event_store.current_event='chara032009'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara032009_03'
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
 show expression 'images/bg/AdvBg_2201.png' as bg
 play music "<loop 3.16>audio/bgm/BGM_QUEST.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "(And so, I landed down on Beatrice's game board.)"
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '(The title is "Ougon no Majo no Densetsu" ...Legend of the Golden Witch.)'
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '(There, I lurked in "Battler Ushiromiya-san\'s" shadow, being allowed to spectate what he sees and hears from start to finish.)'
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '(Through his eyes and ears, I bear witness to the Rokkenjima of the 4th and 5th of October in 1986...)'
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "(The mysterious epitaph written below the portrait imitates the locked-room murder incidents, containing various prophecies regarding the pursuit of the witch's gold, including...)"
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "(--the island's hidden Golden Land...)"
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
 show beatrice_v001 normal_close at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Alright, there we go.'
 show nao_v002 normal at inactive
 show beatrice_v001 smile at active
 show beatrice_v001 smile at jump_transform
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Ooh, have you finished, Nao?!'
 show beatrice_v001 smile at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Yes, although the one who closed the curtains on this tale was Battler...'
 show beatrice_v001 smile at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'But, I wonder if the expression "closed the curtains" is accurate...?'
 show nao_v002 fuan at inactive
 show beatrice_v001 smile_close at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") '*cackle*cackle*cackle*, I get what you\'re trying to say. It was essentially a "Time Over" ending where the clock ran out.'
 show nao_v002 fuan at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Instead of saying the story "was brought to an end", the saying "has incidentally reached the end" would be more appropriate.'
 show nao_v002 fuan at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'And thus... how was my game board?'
 show beatrice_v001 normal at inactive
 show nao_v002 normal_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I see. If there's one way to say it..."
 show nao_v002 normal_close at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'If there is?'
 show beatrice_v001 normal at inactive
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...It's in bad taste."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide beatrice_v001
 hide nao_v002
 hide fade onlayer curtain
 show beatrice_v001 futeki at mei_center
 with Dissolve(0.08333333333333333)
 show beatrice_v001 futeki at active
 show beatrice_v001 futeki at updown_shake_transform
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Pff... *cackle*cackle*cackle*, hyyyaaahahahahaha! Really, is that so? Bad taste!?'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide beatrice_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show nao_v002 normal at mei_left
 show beatrice_v001 futeki at mei_right
 with Dissolve(0.5)
 show beatrice_v001 futeki at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Like really, I don't even think I could say the locked-room murders aligning with the epitaph was tasteful."
 show beatrice_v001 futeki at inactive
 show nao_v002 normal_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Well... I'm not saying it's {i}tasteless{/i}. Because it isn't entirely in bad taste."
 show nao_v002 normal_close at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") '...Hm?'
 show beatrice_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I don't know how much of that story is real, as well as how much of it is a lie. I feel like this is because there are tricks scattered about here and there to deceive readers."
 show nao_v002 normal at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") '...Hm, are you saying my existence is a lie?'
 show beatrice_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I don't think so. But after having spectated the game board through Battler-san's eyes..."
 show beatrice_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "In essence, they aren't my own eyes. Someone else's perspectives and biases are also included."
 show nao_v002 normal at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "Without being able to see with your own eyes, the full truth is unable to be seen... So you're saying the witch's existence isn't being believed in again...?"
 show beatrice_v001 normal at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "It's not like I'm completely denying it. If I were, then who would I be talking to right now? But..."
 show beatrice_v001 normal at inactive
 show nao_v002 normal_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "What I'm talking about is chewing before you swallow. Checking whether or not information is correct by properly verifying it through your own investigation..."
 show beatrice_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "In doing this, information becomes knowledge, and that's how you become educated... That's what my mom taught me."
 show beatrice_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'So, even if I actually go to that place myself, I believe that not being able to use my own body to observe disables me from making a foundation for my conclusions.'
 show nao_v002 normal at inactive
 show beatrice_v001 fuan at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "...I don't know whether you are a doubtful or thoughtful child."
 show beatrice_v001 fuan at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Sorry, that's just how I am... but it not being just bad taste is my straight-forward opinion."
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
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "The story's purpose is to tell a possible truth of what might have occurred on the island..."
 show nao_v002 normal_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Well, I feel like it's trying to convey some sort of message."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show beatrice_v001 normal at mei_right
 show nao_v002 normal_close at mei_left
 with Dissolve(0.5)
 show nao_v002 normal_close at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") '...Hoh. Why would you think that?'
 show beatrice_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Because I still haven\'t been able to discover the theme of "Legend of the Golden Witch".'
 show nao_v002 normal at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'The theme?'
 show beatrice_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "All the stories that I've read have had some sort of theme. This is different from whether it suits one's tastes or not."
 show beatrice_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Basically, stories require a theme, right?'
 show beatrice_v001 normal at inactive
 show nao_v002 fuan_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "But, if I can't find the theme, then it was likely hidden in a clever way... which means that I'm lacking in some way."
 show beatrice_v001 normal at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Maybe if I reread the story few times I'll understand. Ah, unless there's more I can read?"
 show nao_v002 smile at inactive
 show beatrice_v001 normal_close at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") '...How can you be so sure that a theme has been hidden?'
 show beatrice_v001 normal_close at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Because I can.'
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show beatrice_v001 normal_close at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Because this story... was really amusing.'
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 show nao_v002 smile at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") '............'
 show beatrice_v001 normal at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Beatrice?'
 camera at screenshake_transform
 pause 0.0
 show nao_v002 fuan at inactive
 show beatrice_v001 futeki at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") '*cackle*cackle*... *cackle*cackle*cackle*cackle!!! Hahahahahaha! Ahaaahahahahahahahaha!!!'
 show beatrice_v001 futeki at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Huh... wait, what happened?! Is my opinion that dissatisfying? Sorry it wasn't up to your expectations, but..."
 show nao_v002 fuan at inactive
 show beatrice_v001 smile_close at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "No, that's not it! That's not it!"
 show nao_v002 fuan at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'I admire you for reading that story and flat out declaring it as amusing!'
 show nao_v002 fuan at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'I get it now! To think that having a story read to you by a miko could be this entertaining...!'
 show nao_v002 fuan at inactive
 show beatrice_v001 futeki_close at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'After living for one thousand years, discovering something new is just... *cackle*cackle*cackle*!!'
 show beatrice_v001 futeki_close at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'I-I wonder if a... thank you is right here?'
 show nao_v002 fuan at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "*giggle*... I've had a lot of fun, Nao. If another chance arises, it would be grand if you came again to read another game board I put together."
 show nao_v002 fuan at inactive
 show beatrice_v001 smile_close at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "As long as it's you, I'd welcome you with open arms... But alas, it appears you will have to deal with needing permission from that guest."
 show beatrice_v001 smile_close at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Permission...?'
 show nao_v002 normal at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Mhm... if they have another fit of rage, they may use magic to wipe your memory again.'
 show nao_v002 normal at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "But don't worry. If you close your eyes, you will return to your original world."
 show beatrice_v001 smile at inactive
 show nao_v002 odoroki at active
 show nao_v002 odoroki at jump_transform
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...Huh, this is the end?! You're not going to keep reading it for me?!"
 show nao_v002 odoroki at inactive
 show beatrice_v001 normal_close at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Come, try to remember...'
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
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Wait...!'
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
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'I want to know how it continueeees!!'
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
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Huh?'
 hide rika_v002
 with Dissolve(0.2)
 show satoko_v002 fuan at mei_left
 show hanyuu_v002 odoroki at mei_right
 with Dissolve(0.5)
 show hanyuu_v002 odoroki at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Wh-what happened, Nao-san?'
 show satoko_v002 fuan at inactive
 show hanyuu_v002 sinken at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") "Au au, this is the library. If you don't be quiet, it could get bad~!"
 hide satoko_v002
 show rika_v002 fuan at mei_left
 with Dissolve(0.5)
 show hanyuu_v002 sinken at inactive
 show rika_v002 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Hanyuu is also speaking in a loud voice.'
 show rika_v002 fuan at inactive
 show hanyuu_v002 fuan at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") "Huh?! I-I'm sorry..."
 hide rika_v002
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show hanyuu_v002 fuan at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Ah, umm, was I sleeping, just now?'
 hide hanyuu_v002
 show rika_v002 smile at mei_right
 with Dissolve(0.5)
 show nao_v002 fuan at inactive
 show rika_v002 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep. While we were waiting for you to teach Satoko how to improve the writing in her book report, Nao got sleepy.'
 hide rika_v002
 show satoko_v002 fuan at mei_right
 with Dissolve(0.5)
 show nao_v002 fuan at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'M-My apologies... Nao-san had gotten bored because I took up so much time...'
 show satoko_v002 fuan at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Ah, I don't really think you have to apologize..."
 hide satoko_v002
 show hanyuu_v002 normal at mei_right
 with Dissolve(0.5)
 show nao_v002 fuan at inactive
 show hanyuu_v002 normal at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'At any rate, "I want to know how it continues."... what was that about?'
 show hanyuu_v002 normal at inactive
 show nao_v002 odoroki at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Huh? U-Umm... I wonder what that was too. Somehow I feel like I was reading an interesting book in my dream, though.'
 show hanyuu_v002 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '............'
 hide hanyuu_v002
 show satoko_v002 fuan at mei_right
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Nao-san?'
 show satoko_v002 fuan at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Hey, Satoko. If it takes you a long time to write your report, could I go check out a book maybe?'
 show nao_v002 normal at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'I was the one following along with you, but sure... \nWas there a book you wanted to read?'
 show satoko_v002 fuan at inactive
 show nao_v002 smile at active
 show nao_v002 smile at nod_transform
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Yes, I believe I would like to read a mystery.'
 hide satoko_v002
 show hanyuu_v002 odoroki at mei_right
 with Dissolve(0.5)
 show nao_v002 smile at inactive
 show hanyuu_v002 odoroki at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Au... Mystery?'
 show hanyuu_v002 odoroki at inactive
 show nao_v002 smile_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "For some reason, I've suddenly developed a strong desire to research the mystery genre."
 show hanyuu_v002 odoroki at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "For now, let's see how many famous mystery novels I can check out..."
 hide hanyuu_v002
 show rika_v002 odoroki at mei_right
 with Dissolve(0.5)
 show nao_v002 smile at inactive
 show rika_v002 odoroki at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep. Where did this come from?'
 show rika_v002 odoroki at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Not sure. I just have a feeling that I'll be able to enjoy the rest of my dream this way."
 show rika_v002 odoroki at inactive
 show nao_v002 smile_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "But it's just a feeling, you know? *giggle*"
 call chapter_end
 
 $ persistent.chara032009_done = True
 return