label event01_34_00:
 show black_background onlayer black
 $ event_store.current_event='umi2'
 $ event_store.current_progress=0
 $ event_store.current_chapter='event01_34_00'
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
 narrator "It was from the moment we arrived here... no, to be exact, it was ever since I learned of our destination that I've been at the {i}height{/i} of displeasure."
 stop sound
 show expression 'images/bg/AdvBg_471.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_543_bird.wav'
 Character('Bodyguard',ctc="ctcArrow", ctc_position="fixed") "Gotta say, I've heard the rumors, but this scenery sure is great.\nLooking at those serene waters soothes your soul."
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '............'
 Character('Bodyguard',ctc="ctcArrow", ctc_position="fixed") "Oh? Is something wrong, Lady?\nYou've been all quiet since a while ago; not feeling so good?"
 play music "<loop 0>audio/bgm/BGM_EVENT_TOP_COLLAB3.ogg"
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'I-If you get it, then...!\nDo you want me to drive a stake through your head and empty out all your rotten insides into that lake in front of us?'
 narrator "It really is a shame I don't have a handgun with me...\nIf I did, I'd shoot him dead no questions asked."
 narrator 'But that man only responded to my threat with an, "Ooh, so scary.", and posed as if surrendering, laughing frivolously with a nonchalant attitude.'
 Character('Bodyguard',ctc="ctcArrow", ctc_position="fixed") "Well, no need to get that mad. You've just looked tired lately."
 Character('Bodyguard',ctc="ctcArrow", ctc_position="fixed") "At times like this, it's good to admire a lovely view and refresh yourself."
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_141.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 show ange_v001 normal_close at mei_center
 with Dissolve(0.5)
 show ange_v001 normal_close at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "...I haven't heard of mental care being part of a bodyguard's job before. Wouldn't it be much more profitable to become an occupational physician at some company back home?"
 hide ange_v001
 with Dissolve(0.2)
 Character('Bodyguard',ctc="ctcArrow", ctc_position="fixed") 'Hyahhahaha, something like an occupational physician is the farthest job from being a mercenary. Being your bodyguard is just about right for me.'
 show ange_v001 normal at mei_center
 with Dissolve(0.5)
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '...So? Taking a detour before returning to the academy is one thing, but why would you ever go out of your way to choose this place as a rest stop?'
 hide ange_v001
 with Dissolve(0.2)
 Character('Bodyguard',ctc="ctcArrow", ctc_position="fixed") 'Good grief. And to think I tried to find a good spot for you to relax since you seemed tired...'
 show ange_v001 sinken at mei_center
 with Dissolve(0.5)
 show ange_v001 sinken at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "......Don't play dumb with me.\nI should just leave you back here and make you swim to the other side of the lake naked."
 hide ange_v001
 with Dissolve(0.2)
 Character('Bodyguard',ctc="ctcArrow", ctc_position="fixed") "Again with the jokes.\nYou're the one who'd be in trouble if I wasn't here."
 show ange_v001 normal at mei_center
 with Dissolve(0.5)
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "I'm not joking though.\n...If I remember correctly, there was a small village in the area submerged by this reservoir."
 show ange_v001 normal_close at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Its name was... that's right, it was {b}Hinamizawa Village{/b}, wasn't it?"
 hide ange_v001
 with Dissolve(0.2)
 Character('Bodyguard',ctc="ctcArrow", ctc_position="fixed") "Oh, so you're pretty familiar with it.\nWhen the dam construction project was first announced, the village led a violent movement of sorts in opposition towards it."
 Character('Bodyguard',ctc="ctcArrow", ctc_position="fixed") 'There also seemed to be a village renewal movement at some point, which served to halt the advancement of the dam and attract tourists to the area, but...'
 show ange_v001 normal at mei_center
 with Dissolve(0.5)
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '...But it all still ended up disappearing underwater.\nLooks like it was a hopeless attempt.'
 hide ange_v001
 with Dissolve(0.2)
 narrator 'Barely listening in to this story, I stare out into the vast lake horizon laid out before me, uninterested.'
 narrator 'The will of the people is much too helpless and weak in the face of the authority of governmental figures.'
 narrator 'The villagers may have also put their lives on the line to protect their homeland... but since the final product was already out of their control, it all wound up futile in the end.'
 Character('Bodyguard',ctc="ctcArrow", ctc_position="fixed") 'Well, if the hot spring district they plotted as a village renewal project did go well, I feel that they still might have been going strong today.'
 Character('Bodyguard',ctc="ctcArrow", ctc_position="fixed") "Didn't Ushiromiya Group also put in an investment towards the development? ...A shame things went this way."
 show ange_v001 odoroki at mei_center
 with Dissolve(0.5)
 show ange_v001 odoroki at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'The Ushiromiya family was involved with this village?'
 hide ange_v001
 with Dissolve(0.2)
 narrator 'A bit taken aback, I turn behind me to inquire further about it.'
 narrator "The Ushiromiya family gave out money...? And if it's about a resort, I wonder if the one who have handed it out was the eldest son, Uncle Krauss-san?"
 Character('Bodyguard',ctc="ctcArrow", ctc_position="fixed") "Oh, you didn't know? It's a pretty well-known story.\nI figured even you would've heard all about it from the boss by now, Lady."
 Character('Bodyguard',ctc="ctcArrow", ctc_position="fixed") 'In any event, the village renewal failed as a result of the hot spring district development ending up at a standstill midway... and one thing after another, the plans to build the dam started up again, turning it into a ghost town.'
 show ange_v001 normal at mei_center
 with Dissolve(0.5)
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '............'
 hide ange_v001
 with Dissolve(0.2)
 Character('Bodyguard',ctc="ctcArrow", ctc_position="fixed") "Speaking of, it feels like a ghost is gonna pop out at this reservoir, what with all those villagers' sorrows and regrets. Hyahhaa!"
 show ange_v001 normal_close at mei_center
 with Dissolve(0.5)
 show ange_v001 normal_close at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Give me a break. We’re just not on the same wavelength.'
 stop music fadeout 0.5
 hide ange_v001
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_530_walk_one.wav'
 narrator "Done with him, I turn and walk off. The pitter-patter of that man's footsteps resound as he follows suit."
 narrator 'Going along with that idle gossip would have genuinely been bothersome... but I actually started wanting to be alone as well.'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_481.png' as bg
 play music "<loop 0>audio/bgm/BGM_QUEST1_COLLAB3.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show ange_v001 normal at mei_center
 with Dissolve(0.5)
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'The main shrine gate held up after all this time... huh?'
 hide ange_v001
 with Dissolve(0.2)
 narrator '"It hasn\'t even been 10 years since then, so obviously.", I mumble to myself as I look up at it.'
 narrator 'Regardless, it looks like the houses have worn down after not being maintained by their owners. ...I wonder how long this one has left.'
 show ange_v001 normal at mei_center
 with Dissolve(0.5)
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '............'
 hide ange_v001
 with Dissolve(0.2)
 narrator 'Continuing under the shrine gate, and then partway up the stone steps... I can see the peaceful waves of the lake surface.'
 narrator "And down underneath, there's probably what would have been the road leading to the shrine from the village...\nBut even peering in slightly, I still couldn't make it out for sure."
 show ange_v001 normal at mei_center
 with Dissolve(0.5)
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Ghosts, huh...... as if.'
 hide ange_v001
 with Dissolve(0.2)
 narrator "I snort at the thought... but it doesn't stop another feeling from fluttering in my chest."
 show ange_v001 normal_close at mei_center
 with Dissolve(0.5)
 show ange_v001 normal_close at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '(If ghosts really did come out... then would there be people who knew my father, my mother, or even my big brother...?)'
 hide ange_v001
 with Dissolve(0.2)
 narrator "I kept telling myself over and over that that couldn't be true, but as soon as I concluded that my exhaustion was why I was feeling so sentimental--"
 stop music fadeout 0.5
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show ange_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_510_sand_foot.wav'
 show ange_v001 odoroki at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Ah...?!'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide ange_v001
 with Dissolve(0.2)
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 show black_cover as bg
 narrator 'I slip on the step below me, which causes me to lose my footing, rendering me airborne.'
 play audio 'audio/sfx/SE_315_ls_splash.wav'
 narrator 'Another second later, I heard a truly silly noise as my view ahead of me dulled out... and transformed.'
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Nnh... ngh...?!'
 narrator "My body won't move. My consciousness is getting farther away.\nBefore long, my field of view dyes itself in complete darkness..."
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '(Onii...chan...)'
 play audio 'audio/sfx/SE_382_ls_water.wav'
 narrator '{i}Snip{/i}, I felt the sound of something snapping in the back of my head... and so, I lost consciousness.'
 window hide None
 stop sound
 show expression 'images/bg/AdvBg_261.png' as bg
 pause 1.0
 hide fade onlayer curtain
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_543_bird.wav'
 pause 1.0
 call wipeout_routine
 stop sound
 show expression 'images/bg/AdvBg_691.png' as bg
 play music "<loop 0>audio/bgm/BGM_TITLE_COLLAB3.ogg"
 call wipein_routine
 show battler_v001 smile at mei_left
 show jessica_v001 smile at mei_right
 with Dissolve(0.5)
 show jessica_v001 smile at inactive
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Maaan~, to think we could reminisce about all of that in a blink of an eye! Time really does fly when you're having fun!"
 show jessica_v001 smile at inactive
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Come to think of it, Jessica, the last time we met was 6 years ago, huh? So of course the stuff we can talk about is endless!'
 show battler_v001 smile at inactive
 show jessica_v001 smile at active
 show jessica_v001 smile at updown_shake_transform
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Ahahaha, for real! You and I were on the phone for a super long time last week too.'
 show battler_v001 smile at inactive
 show jessica_v001 normal at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'But still, even though I thought about how deep your voice got over the phone, I was like, "Battler hasn\'t changed at all!"...'
 show battler_v001 smile at inactive
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "But what the hell is that huge body frame?! I was sitting here waiting and waiting at the meeting spot and it turns out we didn't even realize we passed each other on the way!"
 show jessica_v001 smile at inactive
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "You've grown a bunch too since back then, but damn, those milkers grew {i}that{/i} much already?!"
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 play audio 'audio/sfx/SE_374_ls_question.wav'
 show jessica_v001 smile at inactive
 show battler_v001 futeki at active
 show battler_v001 futeki:
  yanchor 1.0
  linear 2.0 pos (960,1200)
 pause 2.0
 show battler_v001 futeki:
  yanchor 1.0
  pos (960,1200)
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Ihihihi, they look like they need someone to hold them~!'
 show battler_v001 futeki at inactive
 show jessica_v001 sinken at active
 show jessica_v001 sinken at jump_transform
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Piss ooooffff!! As if I'd let your sorry ass grab my boobs!"
 show battler_v001 futeki at inactive
 show jessica_v001 sinken at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "I'm just growing into an adult! Have some delicacy with your words next time!"
 hide battler_v001
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 show battler_v001 smile at mei_left
 with Dissolve(0.5)
 show jessica_v001 sinken at inactive
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Ihihihihi! My bad, my bad, just a joooke!'
 show jessica_v001 sinken at inactive
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'But... hey, Jessica, I know it might not be my position to say this, but hear me out...'
 show jessica_v001 sinken at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Are we okay... coming off at this station?\nThis area just has your everyday town feel, nothing like a hot spring district.'
 show battler_v001 fuan at inactive
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Aah, no, no! This is Okinomiya City. Our destination is more out back. It's a small village called Hinamizawa."
 show jessica_v001 smile at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "If it's more out back than {i}this{/i}, wouldn't the possibility of it being deserted get much higher? I'm kinda getting worried."
 show battler_v001 fuan at inactive
 show jessica_v001 normal at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "...Well, I do know what you mean. Let's just go in the meantime.\n Uhhh, the boarding area for the transit bus is at..."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide jessica_v001
 hide battler_v001
 hide fade onlayer curtain
 show battler_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 show battler_v001 odoroki at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '...H-Hey. Could that dangerous looking place over there be our bus stop?'
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'If I\'m not mistaken... there\'s a worn out poster taped up saying, "Out of service".'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide battler_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show battler_v001 fuan at mei_left
 show jessica_v001 fuan at mei_right
 with Dissolve(0.5)
 show battler_v001 fuan at inactive
 show jessica_v001 fuan at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "...Ah shoot, that's unexpected. The form said there was a transit bus, but it looks like that's outdated information."
 show jessica_v001 fuan at inactive
 show battler_v001 fuan_close at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '...Jessica.\nSorry for doubting your dad Uncle Krauss-san, but...'
 show jessica_v001 fuan at inactive
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Wasn't it just you and I on the train coming here?"
 show jessica_v001 fuan at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Guess it really was excessive to expect that this desolate place would... have crowds of tourists pouring out left and right.'
 show battler_v001 fuan at inactive
 show jessica_v001 fuan at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "...I feel you on that. That's why my mom asked me to check this place out for myself in person."
 show jessica_v001 fuan at inactive
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Well, uh, from a third person's perspective, I'd say you'd need bodyguards to help escort you around here."
 show battler_v001 normal at inactive
 show jessica_v001 smile at active
 show jessica_v001 smile at nod_transform
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Yup, exactly. Thanks for coming here, Battler.'
 show battler_v001 normal at inactive
 show jessica_v001 fuan at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'At first I was thinking about inviting Shannon since she was on break, but my mom wouldn\'t shut up about, "Going there as women alone is dangerous!". And all the other servants had their own chores to take care of, so...'
 show jessica_v001 fuan at inactive
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '...With a conversation like that, I guess I barely pass as a male cousin of yours.'
 show battler_v001 normal at inactive
 show jessica_v001 fuan at active
 show jessica_v001 fuan at nod_transform
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Yup. Well, it was pretty annoying because she made me promise that we use separate rooms and not go into each other's, though."
 show jessica_v001 fuan at inactive
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Well, honestly, when I heard that you called and wanted to talk to me, I was shocked.'
 show jessica_v001 fuan at inactive
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "This was right on schedule with my free time, so I'm not opposed at all to going to a hot spring."
 show battler_v001 smile at inactive
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Heheh, thank you, Battler.'
 show jessica_v001 smile at inactive
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'But still... that lonely Aunt Natsuhi-san really just gave permission for us kids to go on a trip, huh?'
 show jessica_v001 smile at inactive
 show battler_v001 normal_close at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "It's been a minute since I've seen your mom, so maybe my idea of her is wrong, though?"
 show battler_v001 normal_close at inactive
 show jessica_v001 fuan at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "In any normal situation, she'd absolutely be against this.\n...To be real, Battler, she's getting more and more unstable lately."
 show battler_v001 normal_close at inactive
 show jessica_v001 fuan_close at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Anyways, my dad's investment projects keep failing. It was better to do it when the economy was up, but lately it's, uhhh, well..."
 show jessica_v001 fuan_close at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Yeah... if there's anything you need off your chest, it's cool by me.\nIt's just you and I here, so whatever you say won't be an issue since it can't reach that geezer's ears."
 show jessica_v001 fuan_close at inactive
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "But really, assuming this resort facility Uncle Krauss-san invested in actually did bring in customers, how would he judge whether he's able to collect a portion of that investment back...?"
 show jessica_v001 fuan_close at inactive
 show battler_v001 fuan_close at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Taking another look at his goal, he has a pretty heavy weight on his shoulders.'
 show battler_v001 fuan_close at inactive
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "You don't have to think about it that stiffly. It's fine just giving your opinion on whether or not you'd want to come back to the hot spring as a guest!"
 show battler_v001 fuan_close at inactive
 show jessica_v001 normal at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Ah, by the way... my mom said that she doubted the previous beneficiary of the settlement a bit, saying that he's pulling one over on my dad. Helping me investigate that portion of it would be a huge help..."
 show jessica_v001 normal at inactive
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Pulling one over, like that kind? So, like, the landowner hid the fact it was a plot of land that he got for a steal since it had a bunch of problems, and then scammed him with a high price... something like that?'
 show battler_v001 normal at inactive
 show jessica_v001 fuan at active
 show jessica_v001 fuan at nod_transform
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '...Yeah. Even if I asked Dad about it, he\'d say, "Stay out of my business.", so it looks like he won\'t give straight answers himself.'
 show battler_v001 normal at inactive
 show jessica_v001 normal at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Anyways, I think judging a place based on someone else's words without going there ourselves is what my mom has anxiety about."
 show jessica_v001 normal at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Well, it's not like I can't understand that anxiety..."
 show battler_v001 fuan at inactive
 show jessica_v001 fuan at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Ah! We just said this earlier, but keep this a secret from Uncle Rudolf-san.'
 show jessica_v001 fuan at inactive
 show battler_v001 smile at active
 show battler_v001 smile at nod_transform
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "No worries, for real! I won't even utter a peep about it.\nI feel like anyone who's been in business for a while wouldn't necessarily be surprised at stuff like that happening anyways."
 show jessica_v001 fuan at inactive
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "So to make a long story short, Aunt Natsuhi-san gets put at ease by seeing the place or whatever, and it'll be fine if I just put in a good word for this place?"
 show battler_v001 normal at inactive
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "You catch on quick! I'm counting on you, Battler!"
 show battler_v001 normal at inactive
 show jessica_v001 fuan_close at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Yeah, no, my mom\'s like... if Dad really did get tricked, he has to pull out of the investment at all costs, and if that can\'t happen, she\'d \n"snuff his life out" and then off herself.'
 show jessica_v001 fuan_close at inactive
 show battler_v001 smile at active
 show battler_v001 smile at updown_shake_transform
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Ahhahahahaha! That's Aunt Natsuhi-san for ya. Snuff his life out! An outbreak of murder incidents in the family is what you'd see on TV at 2PM!"
 stop music fadeout 0.5
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide jessica_v001
 hide battler_v001
 hide fade onlayer curtain
 show jessica_v001 normal at mei_center
 with Dissolve(0.08333333333333333)
 show jessica_v001 normal at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "...It's good that you can laugh about it at least."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide jessica_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show battler_v001 fuan at mei_left
 show jessica_v001 normal at mei_right
 with Dissolve(0.5)
 show jessica_v001 normal at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "W-What's with that face? Don't tell me she was being serious when she said that?!"
 play music "<loop 0>audio/bgm/BGM_QUEST1_COLLAB3.ogg"
 show battler_v001 fuan at inactive
 show jessica_v001 normal_close at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "In my eyes, I think she's on the edge."
 show battler_v001 fuan at inactive
 show jessica_v001 normal at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Dad's investment conversation started with my mom bickering at him. And again, I absolutely expect you to keep what I'm about to say a secret."
 show jessica_v001 normal at inactive
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Well, maybe she doesn't wanna have to hear about his business troubles all the time... And so?"
 show battler_v001 normal at inactive
 show jessica_v001 fuan at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "While they were having that conversation, Mom kept polishing the Winchester gun that Grandfather's always had."
 show battler_v001 normal at inactive
 show jessica_v001 fuan_close at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'And she kept muttering, "If that person has to suffer any longer...", and stuff.'
 show jessica_v001 fuan_close at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '............'
 show battler_v001 fuan at inactive
 show jessica_v001 fuan_close at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Stuff like, "I\'d rather just...", y\'know?'
 show jessica_v001 fuan_close at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "That's... definitely freaky...\nShe get sick worrying too much or something?"
 stop music fadeout 0.5
 show battler_v001 fuan at inactive
 show jessica_v001 normal at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "So, I proposed that I go out on a field study... so that Mom wouldn't get so hasty."
 show jessica_v001 normal at inactive
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "If you didn't, who knows what decisions she'd have rushed to..."
 show battler_v001 normal at inactive
 show jessica_v001 normal at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "To be honest, I don't know much about all that investy, costy stuff, but if it's something like seeing if there are a bunch of tourists at some place or not, I can understand that much."
 play music "<loop 0>audio/bgm/BGM_TITLE_COLLAB3.ogg"
 show jessica_v001 normal at inactive
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "W-... Well, anyways, let's try heading to that place for now!\nYou were talking about how it's in a pre-opening phase back there, right?"
 show battler_v001 smile at inactive
 show jessica_v001 normal at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Y-Yeah... It's just, I said this in the car too, but we're keeping this inspection secret from my dad. I'm relying on you not to stand out too much."
 show jessica_v001 normal at inactive
 show battler_v001 smile at active
 show battler_v001 smile at nod_transform
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Yup, got it. Leave it to me!'
 show jessica_v001 normal at inactive
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Aah, but I'm looking forward to the hot spring itself too!\nIf there are swarms of people gathering there, it might turn out to be pretty sick!"
 show battler_v001 smile at inactive
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "...You're right. No sense grumbling about it. Let's go to that hot spring facility!"
 show jessica_v001 smile at inactive
 show battler_v001 smile at active
 show battler_v001 smile at updown_shake_transform
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Yep, yep, that's the spirit!"
 show battler_v001 smile at inactive
 show jessica_v001 normal at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Oh, right, how should we get there? I was looking earlier, but I didn't catch glimpse of any taxies or anything..."
 show jessica_v001 normal at inactive
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '...Worst case, we have no choice but to walk there, huh?'
 camera at screenshake_transform
 pause 0.0
 show battler_v001 normal at inactive
 show jessica_v001 odoroki at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'For real?! But this suitcase is heavy as hell?!'
 show jessica_v001 odoroki at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Shouldn't there basically be nothing in it? How much do you need for a one night stay?!"
 show battler_v001 fuan at inactive
 show jessica_v001 sinken at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "I'm at that age for a young lady! Don't you know this is light compared to other girls out on a trip?"
 show jessica_v001 sinken at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Seriously... what the hell do you girls even put in those bags?'
 hide jessica_v001
 hide battler_v001
 with Dissolve(0.2)
 Character('????',ctc="ctcArrow", ctc_position="fixed") 'Excuse me... is everything alright?'
 show battler_v001 odoroki at mei_left
 with Dissolve(0.5)
 show battler_v001 odoroki at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Huh...?'
 show irie_v003 fuan at mei_right
 with Dissolve(0.5)
 show battler_v001 odoroki at inactive
 show irie_v003 fuan at active
 Character('Man in the Car',ctc="ctcArrow", ctc_position="fixed") 'I apologize for speaking from my window. If you have issues with luggage...'
 show battler_v001 odoroki at inactive
 show irie_v003 smile at active
 Character('Man in the Car',ctc="ctcArrow", ctc_position="fixed") 'Could you perhaps be travelling? May I ask where you would be planning to leave to?'
 show irie_v003 smile at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Uhhh... um...?'
 show battler_v001 fuan at inactive
 show irie_v003 smile at active
 Character('Kyousuke Irie',ctc="ctcArrow", ctc_position="fixed") 'Ah, forgive me. I lead the clinic in the village, where I just came from. My name is Irie.'
 hide battler_v001
 show jessica_v001 odoroki at mei_left
 with Dissolve(0.5)
 show irie_v003 smile at inactive
 show jessica_v001 odoroki at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "A clinic, so you're a doctor? But that outfit is..."
 hide irie_v003
 show shion_v002 smile at mei_right
 with Dissolve(0.5)
 show jessica_v001 odoroki at inactive
 show shion_v002 smile at active
 Character('Girl in the Back Seat',ctc="ctcArrow", ctc_position="fixed") "This guy coaches for a boys baseball team as a hobby. Speaking of, I'm their manager, Shion Sonozaki."
 hide jessica_v001
 hide shion_v002
 with Dissolve(0.2)
 show battler_v001 smile at mei_left
 show jessica_v001 smile at mei_right
 with Dissolve(0.5)
 show jessica_v001 smile at inactive
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Jessica... these people are pretty nice, huh?'
 show battler_v001 smile at inactive
 show jessica_v001 smile at active
 show jessica_v001 smile at nod_transform
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Y-Yeah. To think lost souls getting sent off to hell would be like this.'
 hide jessica_v001
 hide battler_v001
 with Dissolve(0.2)
 show irie_v003 fuan at mei_center
 with Dissolve(0.5)
 show irie_v003 fuan at active
 Character('Kyousuke Irie',ctc="ctcArrow", ctc_position="fixed") "...? If I'm causing a nuisance, I'll part ways here, though..."
 hide irie_v003
 with Dissolve(0.2)
 show jessica_v001 smile at mei_right
 show battler_v001 smile at mei_left
 with Dissolve(0.5)
 show battler_v001 smile at inactive
 show jessica_v001 smile at active
 show jessica_v001 smile at jump_transform
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Aah, wait, wait! We're actually in a super tight spot right now!"
 show jessica_v001 smile at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "We're looking to get to some place called Hinamizawa... but is it possible to get an arrangement for a ride somewhere?"
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide battler_v001
 hide jessica_v001
 with Dissolve(0.2)
 pause 1.0
 hide fade onlayer curtain
 with Dissolve(1.0)
 stop music fadeout 0.5
 show ange_v001 normal at mei_center
 with Dissolve(0.5)
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '............'
 show ange_v001 fuan at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'What is this...? Why are Onii-chan and Jessica Onee-chan here...?'
 show ange_v001 fuan at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "I say that, but I should have fallen at the dam reservoir. So why did I wake up in this city I've never seen before...?"
 show ange_v001 fuan at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Could this be the city of the dead? ...No way.'
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "This isn't a forgery, but I came here through the work of some sort of power..."
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "...Let's follow those two for now. Wait, but following a car on foot is... hm?"
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "A bike... talk about lucky. And it's unlocked too..."
 show ange_v001 normal_close at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "...I'm sorry.\nI'll absolutely bring it back later...!"
 call chapter_end
 jump event01_34_01