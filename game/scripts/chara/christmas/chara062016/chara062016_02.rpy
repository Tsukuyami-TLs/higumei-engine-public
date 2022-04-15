label chara062016_02:
 show black_background onlayer black
 $ event_store.current_event='chara062016'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara062016_02'
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
 show expression 'images/bg/AdvBg_741.png' as bg
 play music "<loop 2.36>audio/bgm/BGM_EVENT1.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show satoko_v015 smile at mei_center
 with Dissolve(0.5)
 show satoko_v015 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Yum...\nThis takes me back to the candies that I would eat from the supermarket.'
 hide satoko_v015
 with Dissolve(0.2)
 Character('????',ctc="ctcArrow", ctc_position="fixed") "It's especially delicious when eaten on occasion... but you actually put that in your mouth with no hesitation, huh?"
 show satoko_v015 normal at mei_center
 with Dissolve(0.5)
 show satoko_v015 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'My, what do you mean?'
 hide satoko_v015
 with Dissolve(0.2)
 Character('????',ctc="ctcArrow", ctc_position="fixed") "You aren't afraid? This candy is from an unfamiliar person... and on top of that, it's from the same person that just blackmailed you."
 show satoko_v015 smile at mei_center
 with Dissolve(0.5)
 show satoko_v015 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "The candy was wrapped individually.\n...And besides, I've already realized you have no malicious intent."
 hide satoko_v015
 with Dissolve(0.2)
 Character('????',ctc="ctcArrow", ctc_position="fixed") 'Hoh... and what makes you say I have no malicious intent?'
 show satoko_v015 normal at mei_center
 with Dissolve(0.5)
 show satoko_v015 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'If you were that way, you would have just handed the photo over to the teachers without letting me know...\nThat would have been a much safer bet for you.'
 show satoko_v015 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Anyhow, I haven't been able to get a good look at your face. Even if the truth did surface, it would seem like I was trying to shift the blame onto a fictitious being."
 show satoko_v015 smile_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Then I\'d instantly get expelled... and "The End", the truth fades into the darkness. So, I assume you not doing that would be because you\'re unwilling to have things end that way?'
 hide satoko_v015
 with Dissolve(0.2)
 Character('????',ctc="ctcArrow", ctc_position="fixed") '...Amazing. You dove that deeply into our exchange?'
 Character('????',ctc="ctcArrow", ctc_position="fixed") "And not just that, your observation skills are quite good.\nYou're the first one to break through my anti-intruder measures."
 Character('????',ctc="ctcArrow", ctc_position="fixed") "And although I was reluctant to, I had no choice but to use my more extreme methods thanks to that. ...This Polaroid camera's film isn't cheap, you know?"
 show satoko_v015 fuan at mei_center
 with Dissolve(0.5)
 show satoko_v015 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Still, my intuition has gotten rusty...\nNot only have you snuck around a blind spot of mine, but you got me at one of my sore points.'
 show satoko_v015 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'After this sloppy job, I might have to hand the title of Trapmaster to you.'
 hide satoko_v015
 with Dissolve(0.2)
 Character('????',ctc="ctcArrow", ctc_position="fixed") 'Hmm... Trapmaster...\nCould that mean that you have knowledge on survival in the wild and the like?'
 show satoko_v015 smile at mei_center
 with Dissolve(0.5)
 show satoko_v015 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Yes, of course. I played a big part in a fight against a special assault team in the back of a mountain before.'
 hide satoko_v015
 with Dissolve(0.2)
 Character('????',ctc="ctcArrow", ctc_position="fixed") "Pff... ahaha, ahahahaha! That's hilarious. That must be the most entertaining joke I've heard since coming to this school."
 show satoko_v015 odoroki at mei_center
 with Dissolve(0.5)
 show satoko_v015 odoroki at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "I'm not actually joking, though... wah?!"
 hide satoko_v015
 with Dissolve(0.2)
 window hide None
 camera at screenshake_transform
 pause 0.0
 play audio 'audio/sfx/SE_232_landing.wav'
 pause 0.5
 Character('????',ctc="ctcArrow", ctc_position="fixed") 'A successful landing... do excuse me. I started feeling like seeing your face up close.'
 show satoko_v015 odoroki at mei_center
 with Dissolve(0.5)
 show satoko_v015 odoroki at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "So it {i}is{/i} possible for someone to fall from the sky like this in reality... What's your name?"
 hide satoko_v015
 with Dissolve(0.2)
 Character('????',ctc="ctcArrow", ctc_position="fixed") "I {i}can{/i} answer, but I'm the one who asked your name first. I'd be thankful if you gave your introduction before me."
 show satoko_v015 smile at mei_center
 with Dissolve(0.5)
 show satoko_v015 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Oh yeah, you're right...\nI'm Satoko Houjou, a first year in the high school section."
 hide satoko_v015
 with Dissolve(0.2)
 Character('????',ctc="ctcArrow", ctc_position="fixed") "Hmm. ...That means you're my underclassman, a year under me.\nNice to meet ya, Houjou-san."
 show satoko_v015 odoroki at mei_center
 with Dissolve(0.5)
 show satoko_v015 odoroki at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '(She switched to casual speech...)'
 hide satoko_v015
 with Dissolve(0.2)
 Character('????',ctc="ctcArrow", ctc_position="fixed") 'And about my name--'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_1769.png' as bg
 pause 1.0
 hide fade onlayer curtain
 with Dissolve(1.0)
 show rika_v021 normal at mei_right
 show satoko_v021 normal at mei_left
 with Dissolve(0.5)
 show satoko_v021 normal at inactive
 show rika_v021 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...And that's how you met the student council president?"
 show rika_v021 normal at inactive
 show satoko_v021 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Yes. I was surprised to find out that she was rumored to be a genius, and that she planned on entering the student council election a few weeks later.'
 show satoko_v021 smile at inactive
 show rika_v021 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Rather than a genius... wasn't she often called a disaster?\nShe may have the highest grades here, but her reputation among teachers is the worst due to her eccentric and antisocial attidude..."
 show satoko_v021 smile at inactive
 show rika_v021 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Despite that, they couldn't just make a student like that drop out after placing among the top ten in the national mock exams, so they had no choice but to tolerate her selfish behavior..."
 show satoko_v021 smile at inactive
 show rika_v021 normal_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'The rumors about her were all messed up like that.'
 show rika_v021 normal_close at inactive
 show satoko_v021 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "That's information you got in class, right? I don't really talk to other students... so I didn't even know about those rumors."
 show rika_v021 normal_close at inactive
 show satoko_v021 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "...I would've never expected that she'd soon become the student council president back then, as well as the person who would eventually help me cover up the fact I escaped the academy."
 show rika_v021 normal_close at inactive
 show satoko_v021 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Moreover, I never imagined she'd make us prepare the venue for the student council's Christmas party as repayment."
 show satoko_v021 fuan at inactive
 show rika_v021 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Right... and plus, making us wear these outfits...'
 show rika_v021 fuan at inactive
 show satoko_v021 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "I-I'm sorry... Rika."
 show rika_v021 fuan at inactive
 show satoko_v021 fuan_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "I was planning on returning as soon as I bought the Christmas present.\nI didn't think you'd get involved in this too..."
 show satoko_v021 fuan_close at inactive
 show rika_v021 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'It was no big deal... anyway, what happened after that?\nWhat did you talk about with the president?'
 show rika_v021 normal at inactive
 show satoko_v021 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Ahh, if I recall...'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide satoko_v021
 hide rika_v021
 with Dissolve(0.2)
 stop sound
 show expression 'images/bg/AdvBg_741.png' as bg
 pause 1.0
 hide fade onlayer curtain
 with Dissolve(1.0)
 Character('Upperclassman',ctc="ctcArrow", ctc_position="fixed") "Oh, we have drinks too. There aren't any fancy tea cups that you'd have at a tea party, though, so you'll have to use these paper cups."
 show satoko_v015 normal at mei_center
 with Dissolve(0.5)
 show satoko_v015 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "...I'll have a bit."
 show satoko_v015 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "(She's the overly-familiar type, huh? She gave off a cold impression at first, so I was a bit on guard...)"
 hide satoko_v015
 with Dissolve(0.2)
 Character('Upperclassman',ctc="ctcArrow", ctc_position="fixed") 'But for you to see through my traps...\nThe alarm has been tripped by three girls; the pitfall, two girls; and one girl even thought a ghost came out and ran screaming.'
 Character('Upperclassman',ctc="ctcArrow", ctc_position="fixed") 'The last girl was seriously mortified...\nNo one would believe her even though she asserted she saw a ghost.\nIt was pitiful.'
 Character('Upperclassman',ctc="ctcArrow", ctc_position="fixed") 'On the other hand, it was regrettable that I never said anything...\nSure enough, this ended up adding to the seven wonders of Lucia.'
 Character('Upperclassman',ctc="ctcArrow", ctc_position="fixed") 'I wonder how many of the seven wonders there are now? Last I checked, I counted up to twelve, so this one would make thirteen... I assume?'
 show satoko_v015 normal at mei_center
 with Dissolve(0.5)
 show satoko_v015 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "You're quite the type to like traps. Any other student would be shocked to hear that Lucia's greatest and most talented student was like this."
 hide satoko_v015
 with Dissolve(0.2)
 Character('Upperclassman',ctc="ctcArrow", ctc_position="fixed") "Not really. I'm hated by everyone after all. My reputation's already the worst it could possibly be, so it can't get any lower."
 show satoko_v015 sinken at mei_center
 with Dissolve(0.5)
 show satoko_v015 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '...Contrary to what you say you seem to be having fun.\nSo they really do allow you to do anything as long as you study?'
 show satoko_v015 fuan_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "*sigh*... It's the privilege of the victor to fully enjoy freedom and self-assertion, huh? From my perspective, it's enviable, even."
 hide satoko_v015
 with Dissolve(0.2)
 Character('Upperclassman',ctc="ctcArrow", ctc_position="fixed") "Ahaha... {i}That's{/i} the line that comes out of your mouth as the one who treaded around my victoriously-made traps like they were nothing? That can't be anything but sarcastic."
 Character('Upperclassman',ctc="ctcArrow", ctc_position="fixed") "Regardless, that was my magnum opus as a culmination of the various selections of books that I've read from front to back. To think that you would go so far as to try and splendidly rip that all apart..."
 Character('Upperclassman',ctc="ctcArrow", ctc_position="fixed") "You're incredible, Houjou-san. A genius. It's frustrating, but it's an honor to meet someone with genuine abilities like you."
 show satoko_v015 odoroki at mei_center
 with Dissolve(0.5)
 show satoko_v015 odoroki at active
 show satoko_v015 odoroki at jump_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '...ah-...!!'
 show satoko_v015 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '(Huh... Huh, huh...?!)'
 show satoko_v015 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '(Rika praised me after I was able to get out of remedial classes... with an "I\'m so glad, you gave it your all".)'
 show satoko_v015 smile_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '(But... how many years has it been since anyone ever told me I\'m "incredible"...?)'
 show satoko_v015 fuan_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '...Uugh... uu...'
 hide satoko_v015
 with Dissolve(0.2)
 Character('Upperclassman',ctc="ctcArrow", ctc_position="fixed") "Eh...? W-What's wrong, Houjou-san?"
 show satoko_v015 sinken at mei_center
 with Dissolve(0.5)
 show satoko_v015 sinken at active
 show satoko_v015 sinken at jump_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "I-It's nothing! Something just got in my eye is all!"
 show satoko_v015 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'That aside, your prototype net trap over there that used the pulley...'
 show satoko_v015 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "A fragile set-up like that wouldn't even be able to lift a single person."
 show satoko_v015 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "To polish it more, you'd need to increase its strength. Otherwise, the trap might half-assedly catch the victim, potentially even causing them harm."
 hide satoko_v015
 with Dissolve(0.2)
 Character('Upperclassman',ctc="ctcArrow", ctc_position="fixed") 'I see. That definitely is true...\nI honestly thought it would be effective too, but I was hesitant in installing it originally due to the risks involved.'
 Character('Upperclassman',ctc="ctcArrow", ctc_position="fixed") "I'd better start improving the strength on each component then. \n...Which part concerns you the most?"
 show satoko_v015 sinken at mei_center
 with Dissolve(0.5)
 show satoko_v015 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'This point here. Supposing someone placed their foot in and it worked, their center of gravity would shift to around here...'
 hide satoko_v015
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_5037_getup.wav'
 Character('Upperclassman',ctc="ctcArrow", ctc_position="fixed") 'Mhm... So with the angle and position like this, the length of this rope placed here is...'
 show satoko_v015 odoroki at mei_center
 with Dissolve(0.5)
 show satoko_v015 odoroki at active
 show satoko_v015 odoroki at jump_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'W-...What is that calculator? It has a ridiculous amount of buttons on it.'
 hide satoko_v015
 with Dissolve(0.2)
 Character('Upperclassman',ctc="ctcArrow", ctc_position="fixed") "Mm? It's a scientific calculator. Using this, you only need to know the angle and the position to easily compute the length and the strength of the parts necessary."
 show satoko_v015 sinken at mei_center
 with Dissolve(0.5)
 show satoko_v015 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Scientific... like the mathematic kind?\nThat troublesome, magical-looking device has uses like that?'
 hide satoko_v015
 with Dissolve(0.2)
 Character('Upperclassman',ctc="ctcArrow", ctc_position="fixed") 'Yep. Other things include being able to create various medicinal drugs should you remember the scientific formulas for them, and you can factor in changes to your traps too. Also...'
 call chapter_end
 jump chara062016_03