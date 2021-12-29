label chara032009_03:
 show black_background onlayer black
 $ event_store.current_event='chara032009'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara032009_03'
 camera:
  anchor (0.5, 0.5)
  pos (960, 540)
 stop sound
 scene #000
 play music 'audio/bgm/BGM_QUEST.ogg'
 show expression 'images/bg/AdvBg_2201.png' as bg
 with Dissolve(1.0)
 nao "(And so, I landed down on Beatrice's game board.)"
 nao '(The title is "Ougon no Majo no Densetsu" ...Legend of the Golden Witch.)'
 nao '(There, I\'ve lurked in "Battler Ushiromiya-san\'s" shadow, having been allowed to spectate what he sees and hears from start to finish.)'
 nao '(October 4th, 1986: 5 days until I witness and lend my ears to the aftermath of Rokkenjima...)'
 nao "(There is an epitaph mystery written below the portrait. That message imitates the locked-room murder incidents. There are various prophecies in the text regarding the pursuit of the witch's gold. And then...)"
 nao "(--the island's hidden Golden Land...)"
 window hide None
 show black_cover as fade with Dissolve(1.0)
 stop sound
 scene black_cover
 show expression 'images/bg/AdvBg_2190.png' as bg
 show beatrice_v001 normal_close at mei_right
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
 nao 'Yes, although the one who closed the curtains on this play was Battler.'
 show nao_v002 fuan at active
 show beatrice_v001 smile at inactive
 nao 'But, I wonder if that expression "closed the curtains" is actually correct?'
 show beatrice_v001 smile_close at active
 show nao_v002 fuan at inactive
 beatrice '*cackle*cackle*cackle*, I know what you are trying to say. That point when the screen cuts out with "Game Over" when the ending has arrived.'
 show beatrice_v001 smile at active
 show nao_v002 fuan at inactive
 beatrice 'Instead of saying the story "was caused to end", the saying "has ended incidentally" should be more appropriate.'
 show beatrice_v001 normal at active
 show nao_v002 fuan at inactive
 beatrice 'And thus... how was my game board?'
 show nao_v002 normal_close at active
 show beatrice_v001 normal at inactive
 nao "That's right, if there is one way to express it..."
 show beatrice_v001 normal at active
 show nao_v002 normal_close at inactive
 beatrice 'If there is?'
 show nao_v002 sinken at active
 show beatrice_v001 normal at inactive
 nao "... It's bad taste."
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide beatrice_v001
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 show beatrice_v001 futeki at mei_center
 with Dissolve(0.08333333333333333)
 show beatrice_v001 futeki at updown_shake_transform,active
 beatrice 'Hm, Hm... *cackle*cackle*cackle*, hyyyaaahahahahaha! Is that so, is that so? Bad taste!?'
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide beatrice_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show beatrice_v001 futeki at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show beatrice_v001 futeki at inactive
 nao "Like really, even if the the epitaph aligning with the locked-room murders {i}was{/i} good taste, I don't think I would even mention it."
 show nao_v002 normal_close at active
 show beatrice_v001 futeki at inactive
 nao "Well... I don't think I would say the taste itself is bad. Because, it isn't just bad taste."
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
 nao "I don't think so. But with me having followed Battler's eyes, spectating the game board..."
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao "In essence, they aren't my own eyes. Someone else's perspectives and biases also filter in."
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice "If you were to see with your own eyes, all truth would be uncovered. Again, the witch's existence isn't being believed in, so...?"
 show nao_v002 smile at active
 show beatrice_v001 normal at inactive
 nao 'It\'s not like I\'m completely denying it. If it was that way, I guess it would be a, "who would I be chatting with at this moment", sort of thing. But...'
 show nao_v002 normal_close at active
 show beatrice_v001 normal at inactive
 nao "It's that taking in all of someone else's story without questioning it that I mean. I should be able to check whether or not that information is correct by properly verifying it through my own investigation..."
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao 'Doing that, information becomes knowledge, your eyes become nourished with intelligence... Something that my mom taught me.'
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao 'So, even if I actually go to that spot myself, I believe that not seeing things with my eyes and not feeling things disables me from making a foundation for my conclusions.'
 show beatrice_v001 fuan at active
 show nao_v002 normal at inactive
 beatrice '...Is this with deep doubt or with deep prudence, you ignorant child?'
 show nao_v002 smile at active
 show beatrice_v001 fuan at inactive
 nao "I'm sorry, the nature of it is as you say... but me saying it isn't just bad taste is my straightforward opinion."
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide beatrice_v001
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 show nao_v002 normal at mei_center
 with Dissolve(0.08333333333333333)
 show nao_v002 normal at active
 nao 'That story has the purpose of sharing some kind of possibility of a truth of what might have occurred on the island...'
 show nao_v002 normal_close at active
 nao "Yeah, I feel like it's intending to give that kind of message."
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
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
 nao "The story that I've read until now had some sort of theme. This is like whether or not its own taste fits in with it, right?"
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao 'Basically, stories require a theme, right?'
 show nao_v002 fuan_close at active
 show beatrice_v001 normal at inactive
 nao "But, being unable to find the theme because it was most likely cleverly hidden well... it's a weakness of mine when it's not easily noticeable."
 show nao_v002 smile at active
 show beatrice_v001 normal at inactive
 nao "No matter how many times I read it over to correct myself, I probably understand it, right? Ah, unless there's more to it?"
 show beatrice_v001 normal_close at active
 show nao_v002 smile at inactive
 beatrice '... Why can you assert that the theme has been hidden?'
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
 nao "Huh... wait, what happened?! Is my opinion that dissatisfying? My bad that it wasn't up to your expectations, but..."
 show beatrice_v001 smile_close at active
 show nao_v002 fuan at inactive
 beatrice "No, that's not it! That's not it!"
 show beatrice_v001 smile at active
 show nao_v002 fuan at inactive
 beatrice 'You read that story, and you flat out declared that it was amusing as you had admired it.'
 show beatrice_v001 smile at active
 show nao_v002 fuan at inactive
 beatrice 'Now I get it! To think that something like arranging to have a story be read to you by a miko could be this entertaining...!'
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
 beatrice "If it's you, I would openly welcome you... But alas, you will have to deal with needing permission from that visitor, it seems."
 show nao_v002 normal at active
 show beatrice_v001 smile_close at inactive
 nao 'Permission...?'
 show beatrice_v001 smile at active
 show nao_v002 normal at inactive
 beatrice 'Mhm... if he has another fit of rage, he may use magic to wipe your memory.'
 show beatrice_v001 smile at active
 show nao_v002 normal at inactive
 beatrice 'But do not fret. If you close your eyes, you will return to your original world.'
 show nao_v002 odoroki at jump_transform,active
 show beatrice_v001 smile at inactive
 nao "...Huh, this is the end?! It's not gonna keep going on?!"
 show beatrice_v001 normal_close at active
 show nao_v002 odoroki at inactive
 beatrice 'Come, try to remember...'
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide nao_v002
 hide beatrice_v001
 hide fade with Dissolve(0.08333333333333333)
 show nao_v002 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show nao_v002 sinken at active
 nao 'Wait...!'
 stop music fadeout 0.5
 show black_cover as fade with Dissolve(1.0)
 stop sound
 scene black_cover
 show expression 'images/bg/AdvBg_351.png' as bg
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_528_unfold_cloth.wav'
 camera at screenshake_transform
 pause 0.0
 nao "I'm interested in how it continueeees!!"
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 play music 'audio/bgm/BGM_EVENT1.ogg'
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
 hanyuu "Huh?! I'm, I'm sorry..."
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
 rika 'Meep. While we were waiting for you to teach Satoko how to improve her writing in her book report, Nao got sleepy.'
 hide rika_v002
 show satoko_v002 fuan at mei_right
 with Dissolve(0.5)
 show satoko_v002 fuan at active
 show nao_v002 fuan at inactive
 satoko 'My, my apologies... because I took so much time up, Nao-san had gotten bored...'
 show nao_v002 fuan at active
 show satoko_v002 fuan at inactive
 nao "Ah, I don't think you really have to apologize but..."
 hide satoko_v002
 show hanyuu_v002 normal at mei_right
 with Dissolve(0.5)
 show hanyuu_v002 normal at active
 show nao_v002 fuan at inactive
 hanyuu 'At any rate, "I\'m interested in how it continues"... what was that about?'
 show nao_v002 odoroki at active
 show hanyuu_v002 normal at inactive
 nao 'Huh? U-umm... I wonder what that was too? I feel like I was reading an interesting book in the middle of my dream, though.'
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
 nao '...Hey, Satoko. Even if it takes a bit to write a report on my opinion of the text, I would like to check out a book for a bit.'
 show satoko_v002 fuan at active
 show nao_v002 normal at inactive
 satoko "I was the one following along with you, but that's fine... was there a book you would like to read?"
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
 nao "All of a sudden for some reason, I've started to want to study the mystery theme."
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
 nao 'Just randomly. I have a feeling it would be more enjoyable to see the rest of my dream like this.'
 show nao_v002 smile_close at active
 show rika_v002 odoroki at inactive
 nao "But it's just a feeling, yeah? *giggle*"
 call chapter_end
 return