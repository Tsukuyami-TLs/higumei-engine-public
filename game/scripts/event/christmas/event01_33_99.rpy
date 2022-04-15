label event01_33_99:
 show black_background onlayer black
 $ event_store.current_event='christmas'
 $ event_store.current_progress=0
 $ event_store.current_chapter='event01_33_99'
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
 narrator '-On a certain day in December 1987-'
 stop sound
 show expression 'images/bg/AdvBg_1761.png' as bg
 play music "<loop 2.36>audio/bgm/BGM_EVENT1.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'I wonder if I should put the decoration up like this...\nRika, how are preparations going on your end?'
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Ah... good. Now that we've got everything set up, we can go to the party venue and start decorating right away."
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Ohohoho! That's excellent. Well then, what's next..."
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...Hey, Satoko...?'
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'What is it?'
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'In exchange for helping us after we snuck out the other day, the president asked us to help out with preparations for the student council Christmas party... that much I understand.'
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Just barely anyway.\nBut... but, you know...'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show rika_v021 sinken at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show rika_v021 sinken at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Of all things, why do we have to do it in these outfits?!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide rika_v021
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show satoko_v021 fuan at mei_right
 show rika_v021 sinken at mei_left
 with Dissolve(0.5)
 show rika_v021 sinken at inactive
 show satoko_v021 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "That again...? I think you're better off just accepting it already."
 show satoko_v021 fuan at inactive
 show rika_v021 sinken_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "You say that, but no one told me we'd have to wear such embarrassing outfits!"
 show rika_v021 sinken_close at inactive
 show satoko_v021 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'What are you saying, Rika? The outfits we had to wear for our punishment games in the past were much wilder than these.'
 show satoko_v021 normal at inactive
 show rika_v021 fuan at active
 show rika_v021 fuan at chara_shake_transform
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "That's true, but...!"
 hide rika_v021
 hide satoko_v021
 with Dissolve(0.2)
 narrator "I really don't get why Satoko accepted this situation so quietly and is just going along with setting things up for the party."
 narrator "What's more... I couldn't come up with a reason why the strong-willed Satoko would so honestly obey the student council president's orders...!"
 show rika_v021 sinken_close at mei_center
 with Dissolve(0.5)
 show rika_v021 sinken_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "(All of this... it's all her fau-...!)"
 hide rika_v021
 with Dissolve(0.2)
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 pause 1.0
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'Hey, seems like preparations are going smoothly.'
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 show rika_v021 odoroki at mei_center
 with Dissolve(0.5)
 show rika_v021 odoroki at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Ah...?!'
 hide rika_v021
 with Dissolve(0.2)
 narrator 'As soon as I turn towards the voice behind me, the person I was just thinking of popped into my field of vision, carrying a cardboard box.'
 show rika_v021 sinken at mei_center
 with Dissolve(0.5)
 show rika_v021 sinken at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'President...!'
 hide rika_v021
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'Yep, that outfit does suit you. Guess Houjou-san and I chose well after all.'
 show rika_v021 normal at mei_center
 with Dissolve(0.5)
 show rika_v021 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'President... why did you keep quiet about this?'
 hide rika_v021
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'Mm? About what?'
 show rika_v021 sinken at mei_center
 with Dissolve(0.5)
 show rika_v021 sinken at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "That you're acquainted with Satoko...\nNo, if anything, the fact that you two are so close that you've helped Satoko study is news to me!"
 hide rika_v021
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'Hmm... you never asked, so I never gave an answer.\nWell, I did forbid Houjou-san from saying anything about it, though.'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show rika_v021 sinken at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show rika_v021 sinken at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'That just means you kept quiet about it!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide rika_v021
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 narrator 'I toss the entirety of my usual demeanor in the trash with a forceful and indignant bellow.'
 narrator 'Satoko awkwardly smiled and said, "Now, now...", and of all things she could do, she opened her mouth to {i}defend{/i} the student council president.'
 show satoko_v021 fuan at mei_center
 with Dissolve(0.5)
 show satoko_v021 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Rika, I've told you many times already, haven't I? The president kept quiet about it for my sake."
 show satoko_v021 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'She told me that... "If people knew that you were hanging out with someone as infamous as me, the teachers would keep an eye on you even more than before", you see.'
 hide satoko_v021
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") "Furude-san, you're aware of my bad reputation too, aren't you?\nIf a bad person approaches someone important to you, you'd feel anxious... It's a very natural feeling to have."
 Character('President',ctc="ctcArrow", ctc_position="fixed") "But, thankfully, I have absolute authority as student council president now... so from here on out, I can use that triumph to deepen our friendship, y'know?"
 narrator 'The president rests her chin on the cardboard boxes left in the corner of the room, grinning.'
 narrator "There's a lot I want to say... a mountain at that.\nBut, what bothers me now is..."
 show rika_v021 normal at mei_center
 with Dissolve(0.5)
 show rika_v021 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "What's with... that manner of speech? Have you ever spoken like this up until now?"
 hide rika_v021
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'I usually chat in an uber polite manner so that people won’t catch onto my accent. In truth, this is my natural speech pattern.'
 show rika_v021 normal at mei_center
 with Dissolve(0.5)
 show rika_v021 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...No matter how hard I listen, I hear nothing other than the standard dialect. What kind of accent is it?'
 hide rika_v021
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") "Wanna know? Try to guess then. Get it right, and I'll buy you a can of coffee everyday."
 narrator "...I don't need that. And I don't even care."
 Character('President',ctc="ctcArrow", ctc_position="fixed") "Also, people often tell me I sound condescending when talking like this. It's not necessarily my intention... but I'm trying to fix that."
 Character('President',ctc="ctcArrow", ctc_position="fixed") "Well, not like I care about how people perceive me though, y'know?"
 show satoko_v021 fuan at mei_center
 with Dissolve(0.5)
 show satoko_v021 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "...Haven't you ever thought that approaching people with that behavior is a bad idea?"
 hide satoko_v021
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") "I see. You mean that no matter what I do, if people have a bad first impression of me, they'll see me as a bad person? \nMhm... good on you for bringing up the primacy effect."
 show rika_v021 sinken at mei_center
 with Dissolve(0.5)
 show rika_v021 sinken at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Let's not get off topic...! You knew it all to begin with, didn't you?"
 hide rika_v021
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'Knew what?'
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.1
 show rika_v021 sinken at mei_center
 with Dissolve(0.5)
 show rika_v021 sinken at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "That Satoko was trying to sneak out...\nIf you knew, then couldn't you have been able to stop her?"
 hide rika_v021
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") "Hmm. So assuming I did know, I guess that means you want to say that I facilitated Houjou-san's escape... or something like that?"
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.2
 show rika_v021 sinken at mei_center
 with Dissolve(0.5)
 show rika_v021 sinken at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Is that wrong? If there was a potential for that happening, I don't see why I have to wear such an embarrassing outfit as punishment...!"
 hide rika_v021
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") "Oh, who cares about the reason, Furude-san? It's an undeniable fact that you left the academy without permission, right?"
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 show rika_v021 fuan at mei_center
 with Dissolve(0.5)
 show rika_v021 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Bu-... But that's because you told me to go-"
 hide rika_v021
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") "It's not like I pressured you to. You did have the option to refuse to go."
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 show rika_v021 fuan at mei_center
 with Dissolve(0.5)
 show rika_v021 fuan at active
 show rika_v021 fuan at chara_shake_transform
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'That... may be so; however...!'
 hide rika_v021
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'Also... that punishment outfit is your repayment to me.'
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'The cost of fixing the fence Houjou-san broke when escaping. The price of the bullet train ticket. The supplier that got involved as well as all of my other connections...'
 Character('President',ctc="ctcArrow", ctc_position="fixed") "Man, it was quite expensive. Can't someone comfort me after properly taking care of all that hard work...?"
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'Just as I thought that, I went and decided to put you two in charge of my "healing". No, really, you\'re too kind to me; I\'m just so grateful!'
 show rika_v021 fuan at mei_center
 with Dissolve(0.5)
 show rika_v021 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...gh...?!'
 hide rika_v021
 with Dissolve(0.2)
 narrator 'Should someone who threatens people this easily really be the student council president...?'
 show rika_v021 sinken_close at mei_center
 with Dissolve(0.5)
 show rika_v021 sinken_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "(If this is how she's going to be, her attempts at inviting me into the student council might be more tolerable... no, no! Isn't getting me to pledge to her her true goal...?)"
 hide rika_v021
 with Dissolve(0.2)
 narrator "All in all, I risk being taken advantage of by making a careless remark like that... It's safer just being quiet and obeying her orders."
 show satoko_v021 normal at mei_center
 with Dissolve(0.5)
 show satoko_v021 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Did you close off the hole in that fence?'
 hide satoko_v021
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") "Yeah. It seems people found out about it, so I was afraid it would be put to misuse while I'm not looking. So I went and fixed it myself."
 show rika_v021 sinken at mei_center
 with Dissolve(0.5)
 show rika_v021 sinken at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "You could've just asked the director to fix the fence. Everyone asks for the director's help when it comes to fixing-... ah?"
 hide rika_v021
 with Dissolve(0.2)
 narrator 'I gasp in realization.'
 narrator "The traces of the fence being broken weren't new... but they weren't that old either."
 narrator "Which probably means the one who did the deed wasn't Satoko. Of course, it wasn't me either."
 narrator 'Which means, the one who broke it was...?'
 show rika_v021 normal at mei_center
 with Dissolve(0.5)
 show rika_v021 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "President... the one who broke that fence... wasn't actually you back in the day, was it?"
 hide rika_v021
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'Who knows? Whoever it was, I believe fixing it was for the best.'
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'With that hole gone, your worries over any possibility of Houjou-san escaping will lessen.'
 show rika_v021 normal at mei_center
 with Dissolve(0.5)
 show rika_v021 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '............'
 hide rika_v021
 with Dissolve(0.2)
 narrator 'I lost my words since she had a point. Is this what it feels like to be utterly perplexed?'
 show satoko_v021 fuan at mei_center
 with Dissolve(0.5)
 show satoko_v021 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "More importantly, you've used my stories about club activities and punishment games as reference to make us wear outfits like these...?"
 hide satoko_v021
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") "Yeah. I won't deny that."
 show satoko_v021 fuan_close at mei_center
 with Dissolve(0.5)
 show satoko_v021 fuan_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'I wanted you to deny it, though...'
 hide satoko_v021
 with Dissolve(0.2)
 narrator 'After saying that, Satoko droops over.'
 narrator "She's fed up... but even so, she seems to be receptive towards it too."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show rika_v021 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show rika_v021 sinken at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "B-But! These outfits... if the teachers find out you're holding a private party like this they'll-"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide rika_v021
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'The teachers are already aware of it. Well, some of them, that is.'
 show rika_v021 odoroki at mei_center
 with Dissolve(0.5)
 show rika_v021 odoroki at active
 show rika_v021 odoroki at jump_transform
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Eh?! N-No way...'
 hide rika_v021
 with Dissolve(0.2)
 narrator "No way. That can't be possible. After all, there's no way Lucia's strict teachers would allow an event with such shameless outfits... nn-?"
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'Listen up, Furude-san. Information is important.'
 Character('President',ctc="ctcArrow", ctc_position="fixed") "As long as you thoroughly acquire intel towards key individuals of the opposite party you're dealing with, there will be multitudinous effective means at your disposal to achieve what you want."
 Character('President',ctc="ctcArrow", ctc_position="fixed") "Those who are obsessed with power especially prioritize themselves, and it's adorable... In these situations, this gives them a blind spot."
 Character('President',ctc="ctcArrow", ctc_position="fixed") "And so, the very moment my opponent becomes aware of how I'm prepared for mutual destruction, they flinch. \n...With that, my side would have already gained the lead."
 show rika_v021 odoroki at mei_center
 with Dissolve(0.5)
 show rika_v021 odoroki at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Wha-...?!'
 hide rika_v021
 with Dissolve(0.2)
 narrator "Sh-she's evil...! The part of her that can speak with such a {i}shady{/i} smile is just like {i}her{/i}...!"
 Character('President',ctc="ctcArrow", ctc_position="fixed") "Also... when you're unable to find their weaknesses, all you have to do is to make some yourself in one simple move."
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'For example, tempting one to leave without permission... right?'
 show rika_v021 fuan at mei_center
 with Dissolve(0.5)
 show rika_v021 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...ngh...'
 hide rika_v021
 with Dissolve(0.2)
 narrator 'My body gets whiplash remembering that prospect, staggering me...'
 show rika_v021 sinken_close at mei_center
 with Dissolve(0.5)
 show rika_v021 sinken_close at active
 show rika_v021 sinken_close at chara_shake_transform
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '(I was vaguely aware that I was set up, but for her to reveal her tricks this easily...!)'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide rika_v021
 hide fade onlayer curtain
 show satoko_v021 fuan at mei_center
 with Dissolve(0.08333333333333333)
 show satoko_v021 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '*sigh*...'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide satoko_v021
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 narrator "Satoko's sigh brought me back to reality."
 show satoko_v021 fuan at mei_center
 with Dissolve(0.5)
 show satoko_v021 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "President... I don't appreciate the way you make yourself seem like the bad one here."
 show satoko_v021 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "I'm aware that you're not as bad as the rumors say, and I'm sure Rika knows as well. Just please keep your misinterpretable antics to a moderate level."
 hide satoko_v021
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") "It's okay, I'm already convinced of it myself.\n...Still, you're wishy-washy too, Houjou-san."
 Character('President',ctc="ctcArrow", ctc_position="fixed") "If you had informed me of it in advance, we could've snuck out together, and I could've come up with a safer plan to buy the scarf."
 show satoko_v021 normal at mei_center
 with Dissolve(0.5)
 show satoko_v021 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "If by any chance that ended in failure, you'd be held responsible for it too. I can't get people involved like that."
 hide satoko_v021
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") "I wouldn't commit such a blunder. Even if I'm not at class, they'd just assume I was doing intensive courses at some cram school."
 Character('President',ctc="ctcArrow", ctc_position="fixed") "Lucia is an educational institution after all. No matter how annoying a student, they'll approve a request to leave as long as you say it's to study for entrance exams."
 Character('President',ctc="ctcArrow", ctc_position="fixed") "Fortunately, you two didn't have to resort to this to leave... but well, as long as you remember that this can be used as one of your countermeasures, I'm sure it'll be useful sometime."
 show satoko_v021 fuan at mei_center
 with Dissolve(0.5)
 show satoko_v021 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "That means I'd have to get a good grade on my final though, right? ...That's far too difficult."
 hide satoko_v021
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_5037_getup.wav'
 narrator 'Satoko shrugs and takes the cardboard box the president brought.\nOn the side of the box, "Decoration tinsel" was written.'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show satoko_v021 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 show satoko_v021 odoroki at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '...Wait, President! What in the world is this!\nThe tinsel inside of the box is all tangled up?!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide satoko_v021
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 Character('President',ctc="ctcArrow", ctc_position="fixed") "Ohh, it's all tangled up like a snake. I don't know who could've done such a thing... Now what should we do about this?"
 show satoko_v021 sinken at mei_center
 with Dissolve(0.5)
 show satoko_v021 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Don\'t say "What should we do"! Ahh, jeez, we don\'t have that much time before the party starts...!'
 hide satoko_v021
 with Dissolve(0.2)
 narrator "As I peek at Satoko's hands, I see the tinsel is pretty jumbled up.\n...Surely it will take a lot of patience to untangle it."
 show rika_v021 normal at mei_left
 show satoko_v021 sinken at mei_right
 with Dissolve(0.5)
 show satoko_v021 sinken at inactive
 show rika_v021 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Should I do it?'
 show rika_v021 normal at inactive
 show satoko_v021 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "N-... No, it's okay!"
 hide satoko_v021
 hide rika_v021
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_528_unfold_cloth.wav'
 narrator 'As she stated that, Satoko pulled the entire tinsel out and began her subdued yet painstaking struggle.'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show satoko_v021 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show satoko_v021 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Nghhhyrrghghhh...!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide satoko_v021
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show rika_v021 normal at mei_center
 with Dissolve(0.5)
 show rika_v021 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '............'
 hide rika_v021
 with Dissolve(0.2)
 narrator 'Satoko glares at the tinsel with a frustrated look on her face.\nI was about to say, "I\'ll help you", when I felt someone tap my shoulder.'
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'Now, why not enjoy the show with me? Or do you not feel like chatting?'
 show rika_v021 normal_close at mei_center
 with Dissolve(0.5)
 show rika_v021 normal_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...It's not that."
 hide rika_v021
 with Dissolve(0.2)
 narrator "I couldn't just say yes, so I sit in a chair as prompted by the student council president."
 narrator 'She lowered down to look at me in the eyes and said something with a low voice, almost at a whisper.'
 stop music fadeout 0.5
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'Do you feel lonely...? After having your best friend stolen?'
 play music "<loop 3.16>audio/bgm/BGM_QUEST.ogg"
 show rika_v021 normal at mei_center
 with Dissolve(0.5)
 show rika_v021 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...What are you talking about?'
 hide rika_v021
 with Dissolve(0.2)
 narrator 'The president gracefully takes a can of coffee out from her pocket and lifts the pull tab.'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show satoko_v021 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show satoko_v021 sinken at active
 show satoko_v021 sinken at chara_shake_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Th-thiiiis...!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide satoko_v021
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 narrator 'She brought the coffee to her mouth as she fondly watched Satoko wrestle with the tinsel.'
 Character('President',ctc="ctcArrow", ctc_position="fixed") "Houjou-san's grades improved thanks to her own efforts.\n...I didn't really do anything."
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'If anything, I only used the traps she loves so much to explain Mathemathics, Physics, Chemistry.'
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'And I even recommended her some interesting anime and manga for English and Social Studies.'
 show rika_v021 normal at mei_center
 with Dissolve(0.5)
 show rika_v021 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'But... Satoko said that her grades went up thanks to you assisting with her studies...'
 hide rika_v021
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") "What she lacked wasn't academic skill. She just needed a bit of feedback and confidence."
 show rika_v021 normal_close at mei_center
 with Dissolve(0.5)
 show rika_v021 normal_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '............'
 hide rika_v021
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") "Even if someone tells you to keep running, it's difficult to keep running, no matter who you are."
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'So, you must set a smaller goal to strive towards and reach, then start towards a brand new goal...'
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'What would you call the reward that comes from this cycle?'
 narrator "I think about how to answer the president's question for a moment.\n...Then it hit me right away."
 show rika_v021 normal at mei_center
 with Dissolve(0.5)
 show rika_v021 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'A sense of accomplishment... maybe?'
 hide rika_v021
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") "Yes. At the end of the day, I believe that's the difference between being able to and not being able to succeed."
 narrator 'The student council president pulled another can of coffee out from her pocket and threw it to me.'
 Character('President',ctc="ctcArrow", ctc_position="fixed") "I was able to make amends with friends I've fought with. I was able to make good food. I was able to finish reading a complicated book. The circle of wisdom has since been unraveled..."
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'It may seem like a small victory to others, but that sense of accomplishment leads to self-confidence, which makes people stronger. That self-confidence gives us strength to take the next step forward.'
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'The more you accumulate a sense of accomplishment, the more it will be worth... but by the time I met Houjou-san, she had lost sight of the goal she was trying to accomplish.'
 show rika_v021 normal at mei_center
 with Dissolve(0.5)
 show rika_v021 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '............'
 hide rika_v021
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") "It's not that that this school has little opportunity to gain a sense of accomplishment... it's more that the system is bad. It's truly outdated and feels more like a marathon."
 Character('President',ctc="ctcArrow", ctc_position="fixed") "No matter how many problem-solving books you complete, you won't remember the problems you can't do. You won't be able to understand them. Then you'll feel like your efforts were for nothing, and it ends up not being fun."
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'Effort that ends in unhappiness is just torture.\nSo as a result, you start to feel disgust at the act of putting any effort in.'
 Character('President',ctc="ctcArrow", ctc_position="fixed") "Whether someone is capable or incapable of studying all lies on whether they can keep enjoying their efforts... that's all there is to it.\nBut you've already been aware of that, haven't you?"
 show rika_v021 normal_close at mei_center
 with Dissolve(0.5)
 show rika_v021 normal_close at active
 show rika_v021 normal_close at nod_transform
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...Yes.'
 hide rika_v021
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'So for her to build that confidence, I simply taught her how to set small goals for herself so she could start accumulating her own accomplishments.'
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'And well, because she regained that confidence, she found room to worry about what Christmas present to give you...'
 Character('President',ctc="ctcArrow", ctc_position="fixed") "If that's what led to her escape, then I believe I have no choice but to apologize, right?"
 show rika_v021 normal at mei_center
 with Dissolve(0.5)
 show rika_v021 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '............'
 hide rika_v021
 with Dissolve(0.2)
 narrator "I silently listened to the president's words, holding the canned coffee."
 narrator "I... understand what she's saying. The feelings I always wanted to convey to Satoko... she perfectly verbalized them."
 narrator 'So I definitely feel grateful that she saved Satoko... but...'
 stop music fadeout 0.5
 Character('President',ctc="ctcArrow", ctc_position="fixed") "...Well don't you look dissatisfied?"
 play music "<loop 0>audio/bgm/BGM_OP_MUSICBOX.ogg"
 show rika_v021 fuan at mei_center
 with Dissolve(0.5)
 show rika_v021 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "That's..."
 show rika_v021 fuan_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "That's because I couldn't help Satoko at all... just by being by her side.\nI couldn't save her in the end......"
 hide rika_v021
 with Dissolve(0.2)
 narrator 'Yes, even though I was by her side... I was only "there".'
 narrator "I knew Satoko was losing her confidence... but I couldn't think of a way to retrieve it."
 narrator "I don't know... how much time the student council president spent with Satoko."
 narrator "But it's definitely far less than the time I spent with her."
 show rika_v021 fuan_close at mei_center
 with Dissolve(0.5)
 show rika_v021 fuan_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '(And yet... this person was able to save Satoko this easily.)'
 hide rika_v021
 with Dissolve(0.2)
 narrator "Had it been Keiichi, I could've honestly felt grateful.\nIf it was Rena, Mion, or even Shion..."
 narrator "But even if I was able to respect the president, I somehow still wouldn't be able to feel grateful in an honest way, and I would only acquire a distorted feeling of anger..."
 Character('President',ctc="ctcArrow", ctc_position="fixed") '...The phrase "It\'s hard to see what\'s right under your nose" must be referring to moments like this.'
 show rika_v021 odoroki at mei_center
 with Dissolve(0.5)
 show rika_v021 odoroki at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Huh...?'
 hide rika_v021
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'Sometimes, poison can be a medicine... and the other way around as well. And for the disease that had fallen upon Houjou-san, the poison that was effective for her was me myself.'
 Character('President',ctc="ctcArrow", ctc_position="fixed") "...But even if you pour medicine over a corpse, it will stay a corpse. The reason her heart didn't die out in the first place was you, Furude-san.\nI believe it was you being by her side that kept her propped up."
 show rika_v021 normal at mei_center
 with Dissolve(0.5)
 show rika_v021 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '............'
 hide rika_v021
 with Dissolve(0.2)
 narrator "I wonder if she's... complimenting me?\nHowever, I can't receive it as a honest compliment."
 narrator 'So instead of thanking her, I just felt like throwing words of hatred at her.'
 show rika_v021 normal at mei_center
 with Dissolve(0.5)
 show rika_v021 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...So you think you're poison?"
 hide rika_v021
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") "Well, that's what I think."
 Character('President',ctc="ctcArrow", ctc_position="fixed") "I can affirm that I'm harmless all I want; I'm sure people would still lug rocks at me from all over! Ahahahaha!"
 show rika_v021 normal at mei_center
 with Dissolve(0.5)
 show rika_v021 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '............'
 hide rika_v021
 with Dissolve(0.2)
 narrator "I didn't think she'd deny it, but I also didn't think she'd say that with a smile."
 show rika_v021 fuan_close at mei_center
 with Dissolve(0.5)
 show rika_v021 fuan_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '(My head started hurting a little... but...)'
 hide rika_v021
 with Dissolve(0.2)
 narrator 'On the other hand, there was something I noticed with this election... no, I realized I was underestimating the students at this academy.'
 show rika_v021 normal at mei_center
 with Dissolve(0.5)
 show rika_v021 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...To be honest, it still feels like a lie that you became the student council president.'
 hide rika_v021
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'I was surprised too.\nI was fighting empty-handed, ready for a merciless death despite wishing to add some signs of change to this academy.'
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'I mentioned how I tried a few things, but I still viewed it like...\n"It doesn\'t matter how close the battle gets if I\'m on the losing side".'
 show rika_v021 normal at mei_center
 with Dissolve(0.5)
 show rika_v021 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...But, you surprisingly accumulated a high number of votes. Even though they weren't outwardly saying things couldn't continue the way they were, they still may have felt that in their hearts."
 show rika_v021 normal_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '"I want to change and I want to better myself". Everyone had those feelings hidden inside of them just like you did. So... they voted for you. Just as... I did...'
 hide rika_v021
 with Dissolve(0.2)
 narrator "...I hesitated many times. I figured that one single vote wouldn't matter much at all, and that it would be a complete waste of time."
 narrator 'But... I wanted to see it.\nWhether it was possible for there to be any room for change at this academy. That hopeful image.'
 narrator 'And, above all... even if I knew the possibility of such a thing was infinitely low...'
 narrator 'I wanted to see the beauty of a "miracle" once again, the kind I\'ve seen after my countless repeated nightmares were over and I was finally able to move forward.'
 Character('President',ctc="ctcArrow", ctc_position="fixed") "...I see, thank you. I guess democracy hasn't been abandoned."
 show rika_v021 normal at mei_center
 with Dissolve(0.5)
 show rika_v021 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...But you'll graduate in 1 year. Once that happens, it's back to..."
 hide rika_v021
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") "You're right. No matter how hard I work to change the school's rules and social etiquette, once I graduate, it might all go back to square one."
 Character('President',ctc="ctcArrow", ctc_position="fixed") "The fact a president like me ever existed may disappear from everyone's memories. But..."
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'Once an event occurs, the memory of it will remain somewhere.\nEven when we become adults, when we look back and it seems like a trivial memory...'
 Character('President',ctc="ctcArrow", ctc_position="fixed") "A trace of it will be left somewhere, and that'll turn into a seed. Someday, someone will find it, and it might sprout once again... right?"
 show rika_v021 normal at mei_center
 with Dissolve(0.5)
 show rika_v021 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...And what if no one finds it at all? I think that possibility also exists.'
 hide rika_v021
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'Yes, perhaps a human may not see it.'
 Character('President',ctc="ctcArrow", ctc_position="fixed") "However... God will see it. That's what I believe."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show rika_v021 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 show rika_v021 odoroki at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '--ah...!'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide rika_v021
 with Dissolve(0.2)
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 stop sound
 show expression 'images/bg/AdvBg_1103.png' as bg
 camera at sepia_shader
 pause 0.0
 show hanyuu_v009 smile at mei_center
 with Dissolve(0.5)
 hide fade onlayer curtain
 with Dissolve(1.0)
 show hanyuu_v009 smile at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") '...Rika.'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_1761.png' as bg
 hide hanyuu_v009
 with Dissolve(0.2)
 camera at reset_shader
 pause 0.0
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator 'A nostalgic figure comes to the back of my mind... and for a moment, I felt a weight press onto my heart.'
 narrator 'Seeing my reaction to that, the president continued to speak as if glossing over whatever my thoughts were.'
 stop music fadeout 0.5
 Character('President',ctc="ctcArrow", ctc_position="fixed") "And with that... that's just about the right number of topics for the letter I'll send this week. That's enough of a reward to me."
 show rika_v021 fuan at mei_center
 with Dissolve(0.5)
 show rika_v021 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...Letter?'
 hide rika_v021
 with Dissolve(0.2)
 narrator 'Just as I was about to ask, "A letter to who?"--'
 play music "<loop 2.36>audio/bgm/BGM_EVENT1.ogg"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show satoko_v021 smile at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform,reset_shader
 pause 0.0
 show satoko_v021 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "I did it... I untangled it~! It's finally undone!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide satoko_v021
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 narrator "My voice was drowned out by Satoko's cheering."
 show satoko_v021 smile at mei_center
 with Dissolve(0.5)
 show satoko_v021 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Rikaa~! President~! The tinsel is finally untangled~!'
 hide satoko_v021
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'Ooh, how wonderful. I have a proposal for such a wonderful Houjou-san.'
 Character('President',ctc="ctcArrow", ctc_position="fixed") "My invitation to the student council... won't you think it over again?"
 show satoko_v021 fuan at mei_center
 with Dissolve(0.5)
 show satoko_v021 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Y-You're trying to persuade me again all of a sudden... I've already refused it over and over; I don't have any time for that at the moment."
 show satoko_v021 sinken at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "If my grades I finally managed to raise lowered again, I don't even want to think of what they'd say to me!"
 hide satoko_v021
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'I see. Well, if you change your mind, you can always come to me. Together with Furude-san.'
 show satoko_v021 normal at mei_center
 with Dissolve(0.5)
 show satoko_v021 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'You believe that if you manage to lure me in, Rika will join too?'
 hide satoko_v021
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'I want both of you, Houjou-san and Furude-san. You have different charms and abilities, after all... and I want to make the student council livelier.'
 show satoko_v021 fuan at mei_center
 with Dissolve(0.5)
 show satoko_v021 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '...In all seriousness? You can do such a thing?'
 hide satoko_v021
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'I will do it. I have decided it in my heart.'
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'And as a first step in that process, I invite students I like to my party and make them wear entertaining outfits...... just kidding!'
 show rika_v021 fuan at mei_left
 show satoko_v021 normal at mei_right
 with Dissolve(0.5)
 show satoko_v021 normal at inactive
 show rika_v021 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '--kh...!'
 show rika_v021 fuan at inactive
 show satoko_v021 normal_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "...I'll think about it."
 hide satoko_v021
 hide rika_v021
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'Ooh, this is the first time I got a positive response. I truly am happy...\nYippie!'
 show rika_v021 fuan at mei_center
 with Dissolve(0.5)
 show rika_v021 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '(...Yippie?)'
 hide rika_v021
 with Dissolve(0.2)
 Character('President',ctc="ctcArrow", ctc_position="fixed") "Ahh, I won't be forcing you two to join the student council, so just join us at the party."
 Character('President',ctc="ctcArrow", ctc_position="fixed") "On top of canned coffee, I'll have many more luxurious things there that you wouldn't be able to find anywhere else at school."
 Character('President',ctc="ctcArrow", ctc_position="fixed") 'Well then, the venue will be open soon, so I hope you guys have the decorations ready by then. Hahahahaha...!'
 narrator "The student council president walks away, laughing happily.\n...As soon as I couldn't see her any longer, I felt a rush of exhaustion."
 show rika_v021 fuan_close at mei_center
 with Dissolve(0.5)
 show rika_v021 fuan_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "(I can't do it... I really just don't like that person...)"
 hide rika_v021
 with Dissolve(0.2)
 narrator "I don't think she's as bad as she says. But, even if she's good at persuading... she's the direct opposite of Keiichi, for example."
 show rika_v021 fuan at mei_center
 with Dissolve(0.5)
 show rika_v021 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "(If I had to liken her to someone... who would it be?\nI guess if I had to pick, it'd probably be Shion.)"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide rika_v021
 hide fade onlayer curtain
 show satoko_v021 normal at mei_center
 with Dissolve(0.08333333333333333)
 show satoko_v021 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '............'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide satoko_v021
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 narrator 'Satoko lets out a deep sigh.'
 narrator "She's been sighing a lot today...\nDespite that, all of her sighs sounded coloured with fun."
 show satoko_v021 fuan at mei_right
 show rika_v021 normal at mei_left
 with Dissolve(0.5)
 show rika_v021 normal at inactive
 show satoko_v021 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Oh brother; that person indeed always surprises me... but Mion-san was the one who surprised me the most.'
 show satoko_v021 fuan at inactive
 show rika_v021 odoroki at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Eh...?'
 show rika_v021 odoroki at inactive
 show satoko_v021 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'For Mion-san to appear together with you at Ginza...\nMy heart nearly stopped back then, Rika.'
 show satoko_v021 smile at inactive
 show rika_v021 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'O-Oh...'
 hide rika_v021
 hide satoko_v021
 with Dissolve(0.2)
 narrator "For Satoko, that definitely must've been the most unexpected development to happen."
 show rika_v021 smile at mei_left
 show satoko_v021 smile at mei_right
 with Dissolve(0.5)
 show satoko_v021 smile at inactive
 show rika_v021 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Who would've thought I was riding the same train as Mion...\nSure it was a coincidence, but it felt way too surreal."
 show rika_v021 smile at inactive
 show satoko_v021 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Maybe it's not a coincidence, but a miracle?"
 show satoko_v021 smile at inactive
 show rika_v021 odoroki at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'A miracle...?'
 show rika_v021 odoroki at inactive
 show satoko_v021 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "It's almost Christmas, after all!\nIt wouldn't be weird for one or two miracles to happen~!"
 show satoko_v021 smile at inactive
 show rika_v021 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...Miracles.'
 hide satoko_v021
 hide rika_v021
 with Dissolve(0.2)
 narrator 'Miracle... a miracle. Maybe that was it.'
 narrator "If Mion wasn't there, Satoko and I would have went our separate ways."
 narrator "If Shion hadn't happened to send the magazine with that ad in the first place, Satoko wouldn't have even known about the scarf being on resale."
 show rika_v021 normal_close at mei_center
 with Dissolve(0.5)
 show rika_v021 normal_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '(After getting this miracle... what now?)'
 hide rika_v021
 with Dissolve(0.2)
 narrator "The scarf is still at Satoko's dorm.\nShe said she'd give me it on Christmas."
 show rika_v021 normal_close at mei_center
 with Dissolve(0.5)
 show rika_v021 normal_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "(It's a little bit frustrating to ask for that student council president's help, but...)"
 hide rika_v021
 with Dissolve(0.2)
 show rika_v021 smile at mei_left
 show satoko_v021 smile at mei_right
 with Dissolve(0.5)
 show satoko_v021 smile at inactive
 show rika_v021 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Hey, Satoko. On Christmas, why don't we ask the president for help so the two of us can go out together?"
 show rika_v021 smile at inactive
 show satoko_v021 odoroki at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Go out... you said? Go out where?'
 show satoko_v021 odoroki at inactive
 show rika_v021 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Anywhere. Even if it's just taking a stroll nearby.\nI want to go somewhere with you wearing our matching scarves."
 show rika_v021 smile at inactive
 show satoko_v021 smile at active
 show satoko_v021 smile at nod_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '......Okay! And gladly, of course~!'
 stop music fadeout 0.5
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide satoko_v021
 hide rika_v021
 with Dissolve(0.2)
 show black_cover as bg
 narrator 'Now... the story that happened a little before Christmas ends here.'
 narrator 'What might happen after Christmas is over?\n...It certainly all depends on those two.'
 play audio 'audio/sfx/SE_5052_bell.wav'
 narrator 'Happy Holidays. And may you have a pleasant Christmas Eve.'
 call chapter_end
 
 $ persistent.christmas_done = True
 return