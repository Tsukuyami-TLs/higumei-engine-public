label event01_33_00:
 show black_background onlayer black
 $ event_store.current_event='christmas'
 $ event_store.current_progress=0
 $ event_store.current_chapter='event01_33_00'
 $ persistent.menu_return='event'
 camera:
  anchor (0.5, 0.5)
  pos (960, 540)
  zoom 1.0
  matrixcolor IdentityMatrix()
 pause 0.0
 scene
 stop music
 stop sound
 show expression 'images/bg/AdvBg_261.png' as bg
 play music "<loop 3.16>audio/bgm/BGM_QUEST.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_5061_horn.wav'
 narrator 'As I ran up the stairs and out onto the platform, a white railroad car came into sight.'
 narrator "Unlike the charming, round faced ones I've seen on TV, this one looked prim, with sharp, slender eyes."
 narrator 'The now outdated 0-type series bullet trains were replaced by the 100-type series after they were first introduced about 2 years ago, in 1985.'
 narrator 'I still vividly remember when they were featured on several TV programs, which would detail how they would start operating.'
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'I used to watch them around dinnertime with Satoko...'
 narrator 'What would that girl say while we watched?'
 narrator 'If I recall, she\'d say, "I\'d like to ride it at least once, but I can\'t think of a reason why I\'d have to take a bullet train."... or something along those lines.'
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '......Satoko......... ah.'
 narrator 'The railroad car stopped right in the front of my eyes, cutting me off.\nIt travels at a tremendous speed, so the fact they have technology to make it stop that accurately is remarkable.'
 narrator 'I snatched up my ticket and entered through the open door.'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_2421.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator "Fortunately, it's a weekday, so there are a lot of seats available."
 show rika_v024 fuan at mei_center
 with Dissolve(0.5)
 show rika_v024 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Phew...'
 hide rika_v024
 with Dissolve(0.2)
 narrator 'I sit down on the window side of an available two-person seat. I finally take a breather as I gaze out the window to watch the scenery, which is slowly starting to move.'
 narrator "...But I still couldn't get myself to relax. Instead, my emotions continued to rush into each other all at once until they simmered down into irritation alone."
 show rika_v024 fuan at mei_center
 with Dissolve(0.5)
 show rika_v024 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Why...?'
 hide rika_v024
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_5037_getup.wav'
 narrator 'I look away from the landscape displayed beyond the window and open the small bag that I was carrying with me.'
 narrator "Although I was in a hurry, I couldn't forget this photo frame, so I took it with me on my way out."
 narrator 'What makes it so important is the picture I keep inside.\nHer appearance and height are different now, but I have no choice but to show this to people when asking around.'
 show rika_v024 fuan at mei_center
 with Dissolve(0.5)
 show rika_v024 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Just... why... Satoko...?'
 hide rika_v024
 with Dissolve(0.2)
 narrator 'I once again asked the Satoko in the picture, who was standing right next to me, wearing a carefree smile.'
 narrator "She won't reply... and expecting her to come back is... impossible.\nDespite that, I couldn't help but ask over and over."
 stop music fadeout 0.5
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 pause 1.0
 show black_cover as bg
 narrator '----December 1987.'
 narrator 'The story goes back a few hours before I stepped onto this bullet train.'
 stop sound
 show expression 'images/bg/AdvBg_1761.png' as bg
 play music "<loop 3.16>audio/bgm/BGM_QUEST.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show rika_v017 fuan at mei_center
 with Dissolve(0.5)
 show rika_v017 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...The student council president?'
 hide rika_v017
 with Dissolve(0.2)
 narrator 'I had just finished eating lunch when a classmate of mine called out to me as I was returning to my room.'
 Character('Classmate',ctc="ctcArrow", ctc_position="fixed") 'Yes... she said she would be waiting for you in the courtyard.'
 narrator 'I found the words of this classmate I recently became friends with rather dubious.'
 narrator "It's not like I've never had any prior contact with the student council president. ...It's more so the odd manner that she went about fetching for me."
 narrator "But really... this is peculiar. When she wants to talk to someone, she'll usually come up to them directly instead of using someone else as a messenger..."
 show rika_v017 normal_close at mei_center
 with Dissolve(0.5)
 show rika_v017 normal_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Okay... I understand. Thank you for coming all the way just to tell me.'
 hide rika_v017
 with Dissolve(0.2)
 Character('Classmate',ctc="ctcArrow", ctc_position="fixed") "No, it's no problem, but..."
 show rika_v017 normal at mei_center
 with Dissolve(0.5)
 show rika_v017 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...But?'
 hide rika_v017
 with Dissolve(0.2)
 Character('Classmate',ctc="ctcArrow", ctc_position="fixed") 'In my head, I was like, "That person seriously hasn\'t given up yet, huh?" \nYou should watch your step.'
 show rika_v017 normal at mei_center
 with Dissolve(0.5)
 show rika_v017 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '............'
 hide rika_v017
 with Dissolve(0.2)
 Character('Classmate',ctc="ctcArrow", ctc_position="fixed") "That student council president--\nAlthough the election was a month ago already, I'm still not used to calling her that..."
 Character('Classmate',ctc="ctcArrow", ctc_position="fixed") 'That person is incredibly despised by the teachers, so most students tend to avoid her.'
 Character('Classmate',ctc="ctcArrow", ctc_position="fixed") "In all honesty, I think it's better for you to stay away from her..."
 show rika_v017 smile at mei_center
 with Dissolve(0.5)
 show rika_v017 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Thank you for your concern. But it'll be okay. I'll just hear her main points and come right back."
 hide rika_v017
 with Dissolve(0.2)
 Character('Classmate',ctc="ctcArrow", ctc_position="fixed") '...Understood. But do be careful.'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 show black_cover as bg
 play audio 'audio/sfx/SE_526_door_open.wav'
 narrator 'I show a smile as thanks for her consideration and say goodbye to her before leaving the room.'
 stop sound
 show expression 'images/bg/AdvBg_1751.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator 'December had just arrived, so the courtyard grew chilly from the cold winter breeze.'
 narrator 'Bunches of students were passing by rapidly while shivering from the cold. ...But under that cold winter sky, the person who called me simply sat there, waiting on a bench.'
 Character('President',ctc="ctcArrow", ctc_position="fixed") "...Ah, so you've arrived. I was a smidge worried I would get ignored and that my wait would be in vain."
 show rika_v017 normal at mei_center
 with Dissolve(0.5)
 show rika_v017 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "(If I did that, she'd come directly to my room anyway...)"
 hide rika_v017
 with Dissolve(0.2)
 narrator 'Pushing aside the foul-mouthed words that I nearly said out loud, I decide to show her a smile.'
 narrator "As long as you smile at someone at this academy, you can deceive them. ...It's doubtful whether it works on this person or not, though."
 show rika_v017 smile at mei_center
 with Dissolve(0.5)
 show rika_v017 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'My apologies for keeping you waiting in the cold. I was out for lunch.'
 hide rika_v017
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'It was me who called you out here, so do be without worry. Also, waiting out in the cold can be rather elegant depending on your mindset.'
 narrator 'The student council president smiles innocently while saying that, almost as if she were a friendly dog.'
 narrator "...It's always hard to tell whether she's being genuine or sarcastic. It's the reason why I find it hard to smile back at her."
 show rika_v017 normal at mei_center
 with Dissolve(0.5)
 show rika_v017 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '(Student council president...)'
 hide rika_v017
 with Dissolve(0.2)
 narrator 'I don\'t... remember her real name. But she responded nonchalantly with, "As long as you\'re aware of my title as student council president, then that\'s good enough". A truly odd person.'
 narrator 'You could say that this attitude of hers made me dislike her even more than the teachers do, as if she was always my "natural enemy".'
 Character('President',ctc="ctcArrow", ctc_position="fixed") '...Speaking of, that also happened here back then.'
 show rika_v017 normal at mei_center
 with Dissolve(0.5)
 show rika_v017 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...Back then?'
 hide rika_v017
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") "Hm? Maybe you've forgotten? That day I tried to get in contact with you for the first time?"
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'I built up all of that courage to approach you... and it seems you still found my method unsatisfactory.'
 show rika_v017 sinken at mei_center
 with Dissolve(0.5)
 show rika_v017 sinken at active
 show rika_v017 sinken at chara_shake_transform
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'D-Don\'t phrase it so weirdly, please! That wasn\'t even you "approaching" me. That was...!'
 hide rika_v017
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") '"If I become the student council president in this upcoming election, would you like to join as my right-hand?"'
 Character('President',ctc="ctcArrow", ctc_position="fixed") "I figured being straightforward and inviting you would convey my intentions sincerely, but it seems it didn't leave a strong impression on you regardless..."
 narrator "No, it did. It really did. So much so that if there was a soap that could wash away memories completely, I'd go on a shopping spree."
 show rika_v017 normal_close at mei_center
 with Dissolve(0.5)
 show rika_v017 normal_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...No matter how you would have invited me, I had no intentions of joining the student council.'
 hide rika_v017
 with Dissolve(0.2)
 narrator 'Yes. Because if I joined the student council, I would miss out on more time with Satoko.'
 narrator "Satoko Houjou... the one who I enrolled into St. Lucia Academy with. My irreplaceable best friend who's more important to me than anyone else."
 narrator "My precious time with her was already not enough; I couldn't allow it to dwindle any further."
 show rika_v017 normal at mei_center
 with Dissolve(0.5)
 show rika_v017 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "I think it's inexcusable that I declined the invitation that you took great pains to come out with."
 show rika_v017 fuan_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "But I couldn't have..."
 hide rika_v017
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") "Couldn't have... what, I wonder?"
 show rika_v017 fuan at mei_center
 with Dissolve(0.5)
 show rika_v017 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Ah, nothing...'
 hide rika_v017
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") "You couldn't have imagined I'd really become the student council president as I declared I would, maybe?"
 show rika_v017 fuan at mei_center
 with Dissolve(0.5)
 show rika_v017 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '............'
 hide rika_v017
 with Dissolve(0.2)
 narrator 'As an answer to my silence, the president just shrugs, smiling.'
 narrator "I more or less hadn't expected such faultless and graceful movements from her back then... but it seems like she treats life as if it were a play, and I'm kind of sick and tired of it."
 Character('President',ctc="ctcArrow", ctc_position="fixed") "Well, I guess it's no surprise. There were four other candidates alongside me in this election. Historically speaking, it was a fierce battle rarely ever seen at St. Lucia Academy."
 Character('President',ctc="ctcArrow", ctc_position="fixed") "There weren't many students supporting me at all, and people were sure that I wouldn't be able to win."
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'But life really is unexpected. It seems I stole the fun of the people who were going to laugh at me when I lost.'
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'It was quite the sight to see when they crumbled down to their knees with expressions of disgust because their expectations were blown out of the water.'
 show rika_v017 fuan at mei_center
 with Dissolve(0.5)
 show rika_v017 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '(...Really, why...?)'
 hide rika_v017
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") '...Why has this girl with an awful personality become president of the student council, right?'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show rika_v017 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 show rika_v017 odoroki at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Huh...?'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide rika_v017
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'No, pay no mind. I have already been made aware that a considerable amount of people have this same thought.'
 narrator '............'
 narrator 'Right. The reason why I was worrying about being called over here... was that the new president has a smeared reputation.'
 narrator 'She skips classes. She speaks in a manner that sounds as if she looks down on other people, she causes trouble here and there.'
 narrator 'And she placed first on the national mock exam, which is just another "reason" permitting her to speak egotistically. Among teachers and adults, she is an absolute problem child.'
 narrator 'Her quirky, freakish way of speaking has yet to reach a level of kindness.'
 narrator "Her character sucks, she's a villain, a person worthy of police surveillance. She's the shame of the school, wannabe criminal, her presence makes you want to hurl... and so on. The list of disses towards her is endless."
 narrator 'Because those rumors have jumped all over the school, even spreading into the first year circles... the degree of hatred towards her was substantial.'
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'Then, Furude-san, had you actually thought that I was going to be voted for president?'
 show rika_v017 normal_close at mei_center
 with Dissolve(0.5)
 show rika_v017 normal_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "I... that's... let's see."
 hide rika_v017
 with Dissolve(0.2)
 narrator "I stopped... trying to cover for myself lazily.\nThe president is incredibly persistent. I feel like I won't be able to get away that easily."
 show rika_v017 normal at mei_center
 with Dissolve(0.5)
 show rika_v017 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Winning or losing aside... there wasn't even a need for a tie-breaking vote. It was a surprise that you won by that massive of a margin."
 show rika_v017 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "According to pre-election speculations, I've heard that you had no supporting layer of voters either, as well as no outlook on a block vote."
 hide rika_v017
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") "Well, it's a school election at the end of the day. No one is going to spend however many months scrutinizing a candidate like an election in the Americas."
 Character('President',ctc="ctcArrow", ctc_position="fixed") "Amassing a vast amount of votes in a tight environment was barely any trouble. ...And I more or less didn't have to devise a means of winning either."
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'But... *chuckle*, you really are great. That side of yours makes a favorable impression.'
 show rika_v017 fuan at mei_center
 with Dissolve(0.5)
 show rika_v017 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Huuh...?'
 hide rika_v017
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") "Once you've prepared yourself, you do not waver.\nYou clearly say what you have to say."
 Character('President',ctc="ctcArrow", ctc_position="fixed") "It's the uncommon quality that the students at this academy do not have. Just one student having it is precious."
 show rika_v017 normal at mei_center
 with Dissolve(0.5)
 show rika_v017 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '............'
 hide rika_v017
 with Dissolve(0.2)
 narrator "The feeling welling up within me from receiving that compliment wasn't joy... it was, of course, wariness."
 show rika_v017 normal_close at mei_center
 with Dissolve(0.5)
 show rika_v017 normal_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '(So it {i}was{/i} about this again...)'
 show rika_v017 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'I said it before, but if this is an invite to the student council, my answer will not change no matter how many times you ask.'
 play audio 'audio/sfx/SE_510_sand_foot.wav'
 show rika_v017 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Is that all you wanted? I'll excuse myself the-"
 hide rika_v017
 with Dissolve(0.2)
 stop music fadeout 0.5
 Character('President',ctc="ctcArrow", ctc_position="fixed") "I believe you'll regret leaving at this point."
 play music "<loop 1.87>audio/bgm/BGM_EVENT6.ogg"
 show rika_v017 fuan at mei_center
 with Dissolve(0.5)
 show rika_v017 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Huh...?'
 hide rika_v017
 with Dissolve(0.2)
 narrator 'She calls out to me in a tone of voice much different from earlier, which causes my legs to stop from moving any further.'
 Character('President',ctc="ctcArrow", ctc_position="fixed") "It's true that I very much want you to join the student council. But the reason I called you here today wasn't to talk about that."
 Character('President',ctc="ctcArrow", ctc_position="fixed") "I'm sure you won't be late if you at least confirm this with me before leaving."
 show rika_v017 normal at mei_center
 with Dissolve(0.5)
 show rika_v017 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...What do you mean?'
 hide rika_v017
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'Satoko Houjou-san.'
 show rika_v017 odoroki at mei_center
 with Dissolve(0.5)
 show rika_v017 odoroki at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...Huh?'
 hide rika_v017
 with Dissolve(0.2)
 narrator 'I feel a cool breeze flow through my body as she uttered that name.'
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'If I told you that I wanted to talk to you about her... would you feel like listening to me?'
 narrator "I wasn't able to answer her."
 show rika_v017 sinken at mei_center
 with Dissolve(0.5)
 show rika_v017 sinken at active
 show rika_v017 sinken at chara_shake_transform
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '(She seriously does have a terrible personality...!!)'
 call chapter_end
 jump event01_33_01