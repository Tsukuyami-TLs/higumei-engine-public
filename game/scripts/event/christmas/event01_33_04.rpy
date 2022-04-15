label event01_33_04:
 show black_background onlayer black
 $ event_store.current_event='christmas'
 $ event_store.current_progress=0
 $ event_store.current_chapter='event01_33_04'
 $ persistent.menu_return='event'
 camera:
  anchor (0.5, 0.5)
  pos (960, 540)
  zoom 1.0
  matrixcolor IdentityMatrix()
 pause 0.0
 scene
 stop music
 show black_cover as bg
 narrator 'December 1987, Tokyo--'
 stop sound
 show expression 'images/bg/AdvBg_2411.png' as bg
 play music "<loop 3.16>audio/bgm/BGM_QUEST.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show satoko_v023 fuan_close at mei_center
 with Dissolve(0.5)
 show satoko_v023 fuan_close at active
 show satoko_v023 fuan_close at chara_shake_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '*sigh*... I-I finally managed to leave... there were just way too many people at this store.'
 show satoko_v023 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Still... Tokyo really does have people packed together in a huge, confusing mess.'
 show satoko_v023 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Even if it's Saturday, it's still midday... I thought they were doing a festival or something, so I had to check the date."
 show satoko_v023 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'As expected, the pace and customs here are extremely different from ours... *sigh*.'
 show satoko_v023 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Well... but I did accomplish my goal safely, so I'd call this a success."
 show satoko_v023 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Now I just have to rush back to the dorm before it becomes a big deal--'
 hide satoko_v023
 with Dissolve(0.2)
 Character('????',ctc="ctcArrow", ctc_position="fixed") '...Satoko!!'
 show satoko_v023 odoroki at mei_center
 with Dissolve(0.5)
 show satoko_v023 odoroki at active
 show satoko_v023 odoroki at jump_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '...Fwah?'
 show satoko_v023 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'I feel like someone just called my name... but this is Ginza, Tokyo, right?'
 show satoko_v023 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '............'
 show satoko_v023 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "I'm just hearing things, after all. I don't even have any acquaintances in Tokyo..."
 hide satoko_v023
 with Dissolve(0.2)
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 camera at screenshake_transform
 pause 0.0
 Character('????',ctc="ctcArrow", ctc_position="fixed") 'Satoko!!!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show satoko_v023 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 show satoko_v023 odoroki at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Eh?!'
 show satoko_v023 odoroki at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "This voice... it can't be... it couldn't be?!"
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 camera:
  parallel:
   linear 0.016666666666666666 pos (960, 540)
  parallel:
   linear 0.016666666666666666 zoom 1.0
 pause 0.016666666666666666
 hide satoko_v023
 with Dissolve(0.2)
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator 'The moment I saw her familiar figure amidst the crowd... it felt like my world finally regained its brightness.'
 play audio 'audio/sfx/SE_408_run.wav'
 narrator 'Perhaps moments like this are the ones that make you want to start praising the Lord... I charged towards Satoko with that thought in mind.'
 show rika_v024 sinken at mei_left
 show satoko_v023 odoroki at mei_right
 with Dissolve(0.5)
 show satoko_v023 odoroki at inactive
 show rika_v024 sinken at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'I found you...! So you were here after all, Satoko!!'
 show rika_v024 sinken at inactive
 show satoko_v023 odoroki at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "...A-Am I dreaming? I mean, there's no way Rika and Mion-san could be at this place...?!"
 hide rika_v024
 show mion_v018 smile at mei_left
 with Dissolve(0.5)
 show satoko_v023 odoroki at inactive
 show mion_v018 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'This is no dream. This is as real as it gets. The ones standing here are Rika-chan and I.'
 show mion_v018 smile at inactive
 show satoko_v023 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "B-But Rika should've been at Lucia...!"
 hide mion_v018
 show rika_v024 sinken at mei_left
 with Dissolve(0.5)
 show satoko_v023 fuan at inactive
 show rika_v024 sinken at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'What are you saying?! I came to look for you because I heard you escaped from the academy!'
 show rika_v024 sinken at inactive
 show satoko_v023 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '...E-Escaped?'
 show satoko_v023 fuan at inactive
 show rika_v024 sinken at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'I heard it all from the student council president...!\nSomeone saw you sneaking out and it was nearly reported to the teachers...!'
 show satoko_v023 fuan at inactive
 show rika_v024 sinken_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "That's why I came all the way here to bring you back...!"
 show rika_v024 sinken_close at inactive
 show satoko_v023 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'I see... My intent was to be cautious, but someone managed to see me leaving anyway. What a blunder on my part.'
 show rika_v024 sinken_close at inactive
 show satoko_v023 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Still, Rika, you found out where I was incredibly well. This is Tokyo, you know? For a coincidence like this to happen...'
 hide rika_v024
 show mion_v018 smile_close at mei_left
 with Dissolve(0.5)
 show satoko_v023 normal at inactive
 show mion_v018 smile_close at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'It was no coincidence. It was inevitable.'
 show mion_v018 smile_close at inactive
 show satoko_v023 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Inevitable... what do you mean?'
 hide mion_v018
 show rika_v024 normal at mei_left
 with Dissolve(0.5)
 show satoko_v023 normal at inactive
 show rika_v024 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...I remembered.'
 hide satoko_v023
 hide rika_v024
 with Dissolve(0.2)
 narrator 'As I say that, I turn my gaze towards the paper bag Satoko is holding.'
 narrator "...If I'm wrong, that's what I get for being conceited.\nBut I was strangely certain that I was correct."
 show rika_v024 normal at mei_left
 show satoko_v023 normal at mei_right
 with Dissolve(0.5)
 show satoko_v023 normal at inactive
 show rika_v024 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Inside that bag you're holding close to you. ...Forgive me if I'm wrong."
 show satoko_v023 normal at inactive
 show rika_v024 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "But that's a scarf, right?"
 show rika_v024 normal at inactive
 show satoko_v023 odoroki at active
 show satoko_v023 odoroki at jump_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Wh-wha-? H-How did you...?!'
 hide rika_v024
 show mion_v018 smile at mei_left
 with Dissolve(0.5)
 show satoko_v023 odoroki at inactive
 show mion_v018 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Hey, Satoko. When you got that scarf, do you remember how you asked me if I could find out where it was bought?'
 show satoko_v023 odoroki at inactive
 show mion_v018 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'And then after pinning down that store, we tried calling them, but we were told, "As it was a limited time Christmas product, we have no plans to put it up for resale", right?'
 show mion_v018 smile at inactive
 show satoko_v023 fuan at active
 show satoko_v023 fuan at nod_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'R-...Right...'
 hide mion_v018
 show rika_v024 normal at mei_left
 with Dissolve(0.5)
 show satoko_v023 fuan at inactive
 show rika_v024 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'I remembered that thanks to coincidentally meeting Mion on the train.'
 show satoko_v023 fuan at inactive
 show rika_v024 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "As soon as we arrived at Tokyo Station, I tried calling the store. They told me that they're putting it up for resale starting today."
 show satoko_v023 fuan at inactive
 show rika_v024 fuan_close at active
 show rika_v024 fuan_close at chara_shake_transform
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'So, I thought, "If I went to that store, couldn\'t she still be there...?", and then hurried here as fast as I could...!'
 hide satoko_v023
 hide rika_v024
 with Dissolve(0.2)
 narrator "We basically never go outside... or, well, it's difficult to receive permission to leave Lucia, so we rarely have the opportunity to wear scarves."
 narrator "So if I hadn't met Mion, I likely wouldn't even have remembered the scarf."
 show satoko_v023 fuan at mei_right
 show rika_v024 fuan_close at mei_left
 with Dissolve(0.5)
 show rika_v024 fuan_close at inactive
 show satoko_v023 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Rika... U-Uh, umm.'
 show satoko_v023 fuan at inactive
 show rika_v024 fuan_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "I'm so glad I could meet up with you... \nAnd I'm so glad we didn't end up going down different paths..."
 show rika_v024 fuan_close at inactive
 show satoko_v023 fuan_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "...I'm sorry, Rika."
 show rika_v024 fuan_close at inactive
 show satoko_v023 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'That magazine I read with you yesterday... \nI took it to my room after that.'
 show rika_v024 fuan_close at inactive
 show satoko_v023 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'As I was reading it last night, this scarf was featured on a page I had missed, and it said resales for it had been confirmed... and it also listed the shop they would do it at.'
 show rika_v024 fuan_close at inactive
 show satoko_v023 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "I planned on giving up at first because I figured it would be impossible. ...But then I thought that if I let go of this opportunity, it'd be hard to expect it to happen again... so I..."
 show satoko_v023 fuan at inactive
 show rika_v024 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...I get it now. I had no idea you liked that scarf so much that you wanted to buy one of the same brand again.'
 show rika_v024 fuan at inactive
 show satoko_v023 odoroki at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Huh...?'
 hide rika_v024
 show mion_v018 smile at mei_left
 with Dissolve(0.5)
 show satoko_v023 odoroki at inactive
 show mion_v018 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Ahahaha, that's not it at all, Rika-chan. You haven't noticed?"
 hide satoko_v023
 hide mion_v018
 with Dissolve(0.2)
 narrator 'Satoko blinked a few times while Mion shook her head.'
 narrator "What could this mean... isn't she buying a replacement? I mean, I guess it's not a big deal to have two of the same thing, much like the gloves back then."
 narrator 'While I was confused about my misunderstanding... Satoko let out a small chuckle and smiled at me mischievously.'
 show satoko_v023 fuan at mei_center
 with Dissolve(0.5)
 show satoko_v023 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "...Rika, you're truly so naive.\nIf you were a detective, they'd call you Sherlost Holmes."
 hide satoko_v023
 with Dissolve(0.2)
 stop music fadeout 0.5
 play audio 'audio/sfx/SE_5037_getup.wav'
 narrator 'Satoko gave a wry smile as she pulled out a brand new scarf from the bag.'
 narrator '...It was the exact same design as the one she cherishes.'
 play music "<loop 0>audio/bgm/BGM_OP_MUSICBOX.ogg"
 show satoko_v023 smile at mei_right
 show rika_v024 fuan at mei_left
 with Dissolve(0.5)
 show rika_v024 fuan at inactive
 show satoko_v023 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'That Christmas day 4 years ago... you gave me that scarf.'
 show rika_v024 fuan at inactive
 show satoko_v023 fuan_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Even though you must've wanted it too..."
 show satoko_v023 fuan_close at inactive
 show rika_v024 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "That's..."
 hide rika_v024
 hide satoko_v023
 with Dissolve(0.2)
 narrator "Because I thought it'd make Satoko happy."
 narrator 'Because I wanted to see Satoko smile. \nBecause I thought it would look great on Satoko.'
 narrator "That's why... I handed over the scarf to her. \nI figured it was for the best..."
 show satoko_v023 smile at mei_center
 with Dissolve(0.5)
 show satoko_v023 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "I... since that day, I've been thinking. \nThat it would be really nice if there were another one of this scarf."
 show satoko_v023 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "That way, I'd be able to match with you..."
 hide satoko_v023
 with Dissolve(0.2)
 show mion_v018 smile at mei_left
 show satoko_v023 smile at mei_right
 with Dissolve(0.5)
 show satoko_v023 smile at inactive
 show mion_v018 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Yep. The reason why Satoko asked me about the store wasn't because she wanted a spare; she wanted a new one so she could match with you."
 show mion_v018 smile at inactive
 show satoko_v023 smile at active
 show satoko_v023 smile at nod_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Exactly. I thought that if I missed this opportunity, I wouldn't be able to get it ever again..."
 show mion_v018 smile at inactive
 show satoko_v023 smile_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Then I remembered the escape route I was told about.'
 show mion_v018 smile at inactive
 show satoko_v023 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "By going there, I could leave and return without anyone noticing... Once I realized that, I just couldn't stand still."
 hide mion_v018
 show rika_v024 fuan at mei_left
 with Dissolve(0.5)
 show satoko_v023 smile at inactive
 show rika_v024 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...You could've went to buy it during winter break."
 show rika_v024 fuan at inactive
 show satoko_v023 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'If it sold out, then it would have all been for nothing.\nEven today, it was already running out of stock...'
 show rika_v024 fuan at inactive
 show satoko_v023 fuan_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'But to think I had been spotted... my skills are getting rusty.'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide satoko_v023
 hide rika_v024
 hide fade onlayer curtain
 show rika_v024 fuan_close at mei_center
 with Dissolve(0.08333333333333333)
 show rika_v024 fuan_close at active
 show rika_v024 fuan_close at chara_shake_transform
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...Idiot......'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide rika_v024
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_5005_grab.wav'
 narrator 'I whispered that as I propped my arms around her neck and held her in a tight embrace, as if I myself was the scarf.'
 narrator '...Satoko has gotten taller than me. I had to stand on my tiptoes.'
 narrator 'In the past, I was able to hold Satoko just by stretching my arms out...'
 narrator 'But Satoko is already... different from then. \nAnd yet, and yet......'
 show rika_v024 fuan at mei_left
 show satoko_v023 odoroki at mei_right
 with Dissolve(0.5)
 show satoko_v023 odoroki at inactive
 show rika_v024 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Satoko, you idiot...!'
 show rika_v024 fuan at inactive
 show satoko_v023 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'I-Idiot?! Who are you calling an idiot?!'
 show satoko_v023 sinken at inactive
 show rika_v024 fuan_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...Don't make me worry like that. Why would you do something so dangerous without telling me anything at all...?!"
 show rika_v024 fuan_close at inactive
 show satoko_v023 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Because... in the worst case, I'd cause you trouble..."
 show satoko_v023 fuan at inactive
 show rika_v024 fuan_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "If it's trouble, you've already caused me enough of it.\nI was so worried, I thought I'd die."
 show rika_v024 fuan_close at inactive
 show satoko_v023 smile_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'I also... wanted to see the surprise on your face.'
 show satoko_v023 smile_close at inactive
 show rika_v024 sinken at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'This went beyond "surprise"; I thought my heart was going to stop...!'
 show satoko_v023 smile_close at inactive
 show rika_v024 sinken at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'I thought you came to hate St. Lucia and ran away!'
 show rika_v024 sinken at inactive
 show satoko_v023 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Y-You're not putting enough faith in me...!"
 show rika_v024 sinken at inactive
 show satoko_v023 fuan_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Well, you did have enough evidence to think that way, so I guess it's unavoidable that you'd have doubts..."
 show satoko_v023 fuan_close at inactive
 show rika_v024 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Please. Don't do this again."
 show satoko_v023 fuan_close at inactive
 show rika_v024 fuan_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'No, running away in general...! If you got into an accident... \nIf anything happened to you...'
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 camera at screenshake_transform
 pause 0.0
 show satoko_v023 fuan_close at inactive
 show rika_v024 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "It'd be more painful than death to me...!"
 show rika_v024 fuan at inactive
 show satoko_v023 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Rika...'
 show rika_v024 fuan at inactive
 show satoko_v023 fuan_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "...I'm sorry."
 hide satoko_v023
 hide rika_v024
 with Dissolve(0.2)
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 narrator 'Satoko put her arms around my body. \n......And somehow, I picked up a very nostalgic scent.'
 narrator "Now that I think about it, I feel like it's been a while since we last held each other so perfectly like this..."
 show mion_v018 smile at mei_center
 with Dissolve(0.5)
 show mion_v018 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Ahh, alriiiight, alriight. I feel bad throwing cold water over you guys while you're having your friendship renewal moment over there, but..."
 hide mion_v018
 with Dissolve(0.2)
 narrator 'After turning our gaze towards the direction of her voice, we saw Mion tapping her watch with the finger on her opposite hand.'
 show mion_v018 smile at mei_center
 with Dissolve(0.5)
 show mion_v018 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "If you two keep it up, your time will... \nIt'd get pretty bad, right?"
 hide mion_v018
 with Dissolve(0.2)
 show satoko_v023 fuan at mei_right
 show rika_v024 fuan at mei_left
 with Dissolve(0.5)
 show rika_v024 fuan at inactive
 show satoko_v023 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Ah...'
 show satoko_v023 fuan at inactive
 show rika_v024 sinken at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "O-Oh no! If we don't head back fast, we won't make it in time for the rollcall!"
 show rika_v024 sinken at inactive
 show satoko_v023 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "...Considering the time we'll take getting there from the station, it'll be a little tough."
 show satoko_v023 fuan at inactive
 show rika_v024 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...What should we do?'
 hide rika_v024
 hide satoko_v023
 with Dissolve(0.2)
 narrator 'One hardship gone, another hardship comes... I felt like I was going pale with all of the uneasiness welling up inside me.'
 narrator 'But Mion was already a step ahead of the game... \n"I got it", she said as she patted our shoulders.'
 show mion_v018 smile at mei_center
 with Dissolve(0.5)
 show mion_v018 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "I'll get a car ready at the station closest to Lucia. If we hightail it in a car the second we arrive at the station, you'll get there just in time, right?"
 hide mion_v018
 with Dissolve(0.2)
 show satoko_v023 odoroki at mei_right
 show rika_v024 odoroki at mei_left
 with Dissolve(0.5)
 show rika_v024 odoroki at inactive
 show satoko_v023 odoroki at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Ah.... That's our Mion-san! I'm in your debt...!"
 show satoko_v023 odoroki at inactive
 show rika_v024 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "I'm sorry... Mion.\nEven though you're on a trip, we're taking up your time for something like this."
 hide rika_v024
 hide satoko_v023
 with Dissolve(0.2)
 show mion_v018 smile at mei_center
 with Dissolve(0.5)
 show mion_v018 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Ahahaha! You don't have to worry about that."
 show mion_v018 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "If we're talking about sudden things coming up, I also had you two help out at the store during Christmas, and it caused you lot of trouble... right?"
 hide mion_v018
 with Dissolve(0.2)
 narrator 'Laughing out loud, Mion shows us a thumbs up.'
 narrator "Much like us, Mion aged up a bit. \nShe's gotten more adult-like because of that, but..."
 narrator 'That smile was just like the same old Mion we knew.'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show mion_v018 smile at mei_center
 with Dissolve(0.08333333333333333)
 show mion_v018 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Plus... we're all friends here, aren't we? Of course I'd help you out!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide mion_v018
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show rika_v024 smile at mei_left
 show satoko_v023 smile at mei_right
 with Dissolve(0.5)
 show satoko_v023 smile at inactive
 show rika_v024 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Mion...'
 show rika_v024 smile at inactive
 show satoko_v023 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "...Thank you, Mion-san. I'm honestly so glad I was able to meet you and Rika."
 hide satoko_v023
 hide rika_v024
 with Dissolve(0.2)
 show mion_v018 smile at mei_center
 with Dissolve(0.5)
 show mion_v018 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Nah, I'm not that awe-... wait, leave the sappy talk for later!\nOur priority right now is heading back to the academy!"
 hide mion_v018
 with Dissolve(0.2)
 show rika_v024 smile at mei_left
 show satoko_v023 smile at mei_right
 with Dissolve(0.5)
 show satoko_v023 smile at inactive
 show rika_v024 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Right... let's get back to Lucia as soon as possible."
 show rika_v024 smile at inactive
 show satoko_v023 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "...Ahh, but I feel I'll cause trouble for my senior with this. I'm feeling the weight of my actions already..."
 stop music fadeout 0.5
 show satoko_v023 fuan at inactive
 show rika_v024 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Your... senior?'
 show rika_v024 fuan at inactive
 show satoko_v023 smile at active
 show satoko_v023 smile at nod_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Yeah, I'm talking about that student council president."
 show satoko_v023 smile at inactive
 show rika_v024 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...What do you mean...?'
 show rika_v024 fuan at inactive
 show satoko_v023 odoroki at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'My... Rika, were you not also aware?'
 show satoko_v023 odoroki at inactive
 show rika_v024 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...What in the world are you talking about?'
 call chapter_end
 jump event01_33_99