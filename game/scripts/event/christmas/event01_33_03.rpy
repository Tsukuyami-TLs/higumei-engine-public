label event01_33_03:
 show black_background onlayer black
 $ event_store.current_event='christmas'
 $ event_store.current_progress=0
 $ event_store.current_chapter='event01_33_03'
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
 narrator 'December 12th, 1983--'
 stop sound
 show expression 'images/bg/AdvBg_323.png' as bg
 window hide None
 hide fade onlayer curtain
 with Dissolve(1.0)
 pause 1.0
 call wipeout_routine
 stop sound
 show expression 'images/bg/AdvBg_333.png' as bg
 play music "<loop 2.36>audio/bgm/BGM_EVENT1.ogg"
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 call wipein_routine
 show mion_v007 smile at mei_center
 with Dissolve(0.5)
 show mion_v007 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Alright everyone~, have you gotten your drinks?\nWe're gonna do a toast!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide mion_v007
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show kazuho_v007 smile at mei_center
 with Dissolve(0.5)
 show kazuho_v007 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'O-Okay...!'
 hide kazuho_v007
 with Dissolve(0.2)
 narrator 'As I held the two cups in my hands up, Shion-san nodded with an "Alright.", and called out to Mion-san.'
 show shion_v006 smile at mei_left
 show mion_v007 smile at mei_right
 with Dissolve(0.5)
 show mion_v007 smile at inactive
 show shion_v006 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "It looks like everyone's gotten one, Sis.\nPreparations are complete."
 show shion_v006 smile at inactive
 show mion_v007 smile_close at active
 show mion_v007 smile_close at deepbreath_transform
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Alright, let's do this formally... *ahem*!"
 show shion_v006 smile at inactive
 show mion_v007 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Everyone, we did a suuuuper great job!'
 show mion_v007 smile at inactive
 show shion_v006 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Thanks to everyone's help, we've somehow gotten past the Angel Mort Christmas Fair... or rather, the crunch beforehand!"
 show mion_v007 smile at inactive
 show shion_v006 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'So, for that, this gathering is a small thanks from us and the restaurant.'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide mion_v007
 hide shion_v006
 hide fade onlayer curtain
 show mion_v007 smile at mei_center
 with Dissolve(0.08333333333333333)
 show mion_v007 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Christmas Eve has already passed, but our Christmas starts here!'
 show mion_v007 smile_close at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "So, let's eat and drink as much as we like! And without further ado--"
 show mion_v007 smile at active
 show mion_v007 smile at jump_transform
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Merry Christmas!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide mion_v007
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 play audio 'audio/sfx/SE_5062_cheers.wav'
 Character('Everyone',ctc="ctcArrow", ctc_position="fixed") 'Merry Christmas!!'
 show miyuki_v006 smile at mei_right
 show kazuho_v007 smile at mei_left
 with Dissolve(0.5)
 show kazuho_v007 smile at inactive
 show miyuki_v006 smile at active
 show miyuki_v006 smile at updown_shake_transform
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") '*gulp*, *gulp*, *gulp*... *burp*, haaahh!!\nA full glass is great after a hard few days at work! Another one for me!'
 show miyuki_v006 smile at inactive
 show kazuho_v007 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "I-If you drink that much at once, won't it take you off somewhere strange?"
 show kazuho_v007 fuan at inactive
 show miyuki_v006 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "No worries, I'm minding my limits.\n...And besides, yesterday I was parched the whooooole time we were sweating it up on the job, so I'm still catching up."
 show kazuho_v007 fuan at inactive
 show miyuki_v006 fuan at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Speaking of, the people at the family restaurant weren't even given the chance to take a water break because we were so busy over Christmas, right? But not many people are even here partying..."
 show kazuho_v007 fuan at inactive
 show miyuki_v006 fuan_close at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'We should call it Cursedmas instead of Christmas...'
 hide kazuho_v007
 show nao_v006 normal at mei_left
 with Dissolve(0.5)
 show miyuki_v006 fuan_close at inactive
 show nao_v006 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "There are various ways of celebrating Christmas all around... so it's not like I don't understand why."
 show miyuki_v006 fuan_close at inactive
 show nao_v006 fuan_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "It really was tough work for a while though, wasn't it...?\nMy arm won't even lift after whisking cream so much."
 hide miyuki_v006
 hide nao_v006
 with Dissolve(0.2)
 narrator 'After taking a sip of her juice with a straw and placing her cup on the table, Nao-chan said that while lifting her arm a little.'
 narrator "It's rare for her to be anything less than composed... but even so, that thin, tiny arm was trembling without her doing a single thing."
 show rena_v007 smile at mei_right
 show nao_v006 fuan_close at mei_left
 with Dissolve(0.5)
 show nao_v006 fuan_close at inactive
 show rena_v007 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Ahahaha. Nao-chan helped out with making a bunch of cakes after all.'
 show nao_v006 fuan_close at inactive
 show rena_v007 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'But thanks to that, you saved Rena a lot.\nNow Rena can forkfeed some cakes into your mouth!'
 play audio 'audio/sfx/SE_311_ls_cutejump.wav'
 show rena_v007 smile at inactive
 show nao_v006 odoroki_blush at active
 show nao_v006 odoroki_blush at jumping_transform
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Whaa-?! C-Can you really?! Th-then... a-ahh!'
 play audio 'audio/sfx/SE_215_heartgrow.wav'
 show nao_v006 odoroki_blush at inactive
 show rena_v007 smile_blush at active
 show rena_v007 smile_blush at chara_shake_transform
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "Hau~, Nao-chan's wittle mouf and her wittle teefs... so kyuuuute~!!"
 hide nao_v006
 hide rena_v007
 with Dissolve(0.2)
 show shion_v006 fuan at mei_left
 with Dissolve(0.5)
 show shion_v006 fuan at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") '...Was that a compliment?'
 show miyuki_v006 fuan_close at mei_right
 with Dissolve(0.5)
 show shion_v006 fuan at inactive
 show miyuki_v006 fuan_close at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Ah, it'd be thoughtful to leave it as is. Those two are already lost in their own world, y'know?"
 hide shion_v006
 show kazuho_v007 fuan at mei_left
 with Dissolve(0.5)
 show miyuki_v006 fuan_close at inactive
 show kazuho_v007 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'A-Ahaha...'
 hide miyuki_v006
 hide kazuho_v007
 with Dissolve(0.2)
 narrator 'As I laughed nervously, I took in my surroundings.'
 show hanyuu_v010 fuan at mei_right
 show rika_v009 normal at mei_left
 with Dissolve(0.5)
 show rika_v009 normal at inactive
 show hanyuu_v010 fuan at active
 show hanyuu_v010 fuan at chara_shake_transform
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Au au~... Working non-stop got me all worn out~...'
 show hanyuu_v010 fuan at inactive
 show rika_v009 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Hanyuu, it's no good to limp around forever. Just look at Satoko."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide rika_v009
 hide hanyuu_v010
 hide fade onlayer curtain
 show satoko_v006 smile at mei_center
 with Dissolve(0.08333333333333333)
 show satoko_v006 smile at active
 show satoko_v006 smile at updown_shake_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "*om*, *chomp*, *munch*...!\nThese cakes are quite the masterpiece, if I must say~!\nWhy doesn't Hanyuu-san also dig in?"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide satoko_v006
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show hanyuu_v010 fuan at mei_right
 with Dissolve(0.5)
 show hanyuu_v010 fuan at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") "I-I want to eat, but my hands are trembling... it's too painful even to hold a fork like this..."
 show hanyuu_v010 fuan at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Au au... s-someone please feed me the cake...'
 show rika_v009 smile at mei_left
 with Dissolve(0.5)
 show hanyuu_v010 fuan at inactive
 show rika_v009 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Here, Hanyuu. Say "aah".'
 show rika_v009 smile at inactive
 show hanyuu_v010 smile at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Rika...! Aah... *munch*munch*.'
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show hanyuu_v010 smile at inactive
 show rika_v009 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "It's fried rice with kimchi."
 camera at screenshake_transform
 pause 0.0
 show rika_v009 smile at inactive
 show hanyuu_v010 fuan at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Mugaaah?!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide hanyuu_v010
 hide rika_v009
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show mion_v007 fuan at mei_right
 show shion_v006 fuan at mei_left
 with Dissolve(0.5)
 show shion_v006 fuan at inactive
 show mion_v007 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'You brought that one upon yourself...'
 show mion_v007 fuan at inactive
 show shion_v006 fuan at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Those two never betray expectations.\nAre they... aware of how predictable they are?'
 hide shion_v006
 hide mion_v007
 with Dissolve(0.2)
 narrator 'The Sonozaki sisters gazed at Hanyuu-chan, who was now fainting in agony. They had looks of accomplishment on their faces, paired with the noticeable presense of exhaustion...'
 show kazuho_v007 normal at mei_center
 with Dissolve(0.5)
 show kazuho_v007 normal at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Um, Mion-san, Shion-san...'
 show kazuho_v007 normal at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Why did the majority of the waitresses in Okinomiya get rounded up by that store in Gogura during the height of all that Christmas stuff?'
 hide kazuho_v007
 with Dissolve(0.2)
 show satoko_v006 normal at mei_left
 with Dissolve(0.5)
 show satoko_v006 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Now that you say it, I was never informed of the specifics on that either. Could you allow me to hear what happened?'
 show mion_v007 normal at mei_right
 with Dissolve(0.5)
 show satoko_v006 normal at inactive
 show mion_v007 normal at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Uhhhh, alright. You remember that Japanese dessert set from earlier?'
 show mion_v007 normal at inactive
 show satoko_v006 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "That was a suggestion you guys put in for Angel Mort's new menu, right? What happened with it?"
 show satoko_v006 normal at inactive
 show mion_v007 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Of course, it's a popular order at the Angel Mort in Okinomiya, but it's in such high demand at the one in Gogura that it sold out in a day, making it a huge issue, y'know...?"
 hide satoko_v006
 show shion_v006 smile at mei_left
 with Dissolve(0.5)
 show mion_v007 fuan at inactive
 show shion_v006 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "What's more, it looks like rumors have been calling about even more rumors, and it's been causing their overall sales to skyrocket."
 show shion_v006 smile at inactive
 show mion_v007 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'The manager in Gogura also came out with the promotion catchphrase, "Instant sellouts at this shop; get our renown to the top!", and customers went going hog wild flocking to their door...'
 hide shion_v006
 show kazuho_v007 fuan at mei_left
 with Dissolve(0.5)
 show mion_v007 fuan at inactive
 show kazuho_v007 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'U-Uwaah...'
 show kazuho_v007 fuan at inactive
 show mion_v007 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'So, the girls working part time in Okinomiya needed to be sent out to work part time in Gogura.'
 hide kazuho_v007
 show shion_v006 fuan at mei_left
 with Dissolve(0.5)
 show mion_v007 fuan at inactive
 show shion_v006 fuan at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'And thanks to that, Okinomiya Angel Mort ended up getting in a pinch. Talk about getting your priorities backwards...\nIt feels more like a, "Thanks, dumbass!", than anything.'
 show mion_v007 fuan at inactive
 show shion_v006 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "But because of that, everyone coming together to help saved the day. I'd like to extend my thanks to you guys for taking the manager's place after he went home all flabberghasted."
 hide mion_v007
 hide shion_v006
 with Dissolve(0.2)
 show kazuho_v007 smile at mei_center
 with Dissolve(0.5)
 show kazuho_v007 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Ah, no. You don't have to thank us...\nIt should be, well, reciprocal in troubled times."
 hide kazuho_v007
 with Dissolve(0.2)
 show shion_v006 smile at mei_left
 show mion_v007 smile at mei_right
 with Dissolve(0.5)
 show mion_v007 smile at inactive
 show shion_v006 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Thanks for sparing me the effort in having to.\n...Well, it wasn't too awful through and through, though."
 show shion_v006 smile at inactive
 show mion_v007 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'We snatched up a boatload of money as a reward, so we got to reserve this store for tonight and throw a Christmas party to congratulate all of our hard work!'
 hide shion_v006
 show kazuho_v007 smile at mei_left
 with Dissolve(0.5)
 show mion_v007 smile at inactive
 show kazuho_v007 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Ahaha... That's also true."
 show kazuho_v007 smile at inactive
 show mion_v007 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Well, isn't that right everyone?! Make sure you eat, drink, and bustle around to your heart's content!!"
 hide mion_v007
 hide kazuho_v007
 with Dissolve(0.2)
 camera at screenshake_transform
 pause 0.0
 play audio 'audio/sfx/SE_515_tableware.wav'
 Character('Everyone',ctc="ctcArrow", ctc_position="fixed") 'Yeaaaah!'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 show black_cover as bg
 pause 1.0
 narrator '...And so, we regained all of that energy we spent working by enjoying ourselves, eating, drinking...'
 stop sound
 show expression 'images/bg/AdvBg_333.png' as bg
 pause 1.0
 hide fade onlayer curtain
 with Dissolve(1.0)
 show kazuho_v007 smile at mei_center
 with Dissolve(0.5)
 show kazuho_v007 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Haah, I'm so full... That was delicious."
 hide kazuho_v007
 with Dissolve(0.2)
 show nao_v006 fuan at mei_left
 with Dissolve(0.5)
 show nao_v006 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I might have eaten a little too much... maybe.\nI'm so full, I can't move."
 show miyuki_v006 normal at mei_right
 with Dissolve(0.5)
 show nao_v006 fuan at inactive
 show miyuki_v006 normal at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Even though you were just saying you were so tired that you couldn't move?"
 show miyuki_v006 normal at inactive
 show nao_v006 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Do you really think there's a person out there who can resist being fed delicious food and desserts with Rena-chan in front of them?"
 hide nao_v006
 hide miyuki_v006
 with Dissolve(0.2)
 show kazuho_v007 fuan at mei_center
 with Dissolve(0.5)
 show kazuho_v007 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '(I feel like that last part only applies to Nao-chan, though...)'
 hide kazuho_v007
 with Dissolve(0.2)
 narrator 'Since we were so full and content, all that was left to do was sit back with a smile thinking about going home and sleeping with a full belly. But then...'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show mion_v007 smile_close at mei_center
 with Dissolve(0.08333333333333333)
 show mion_v007 smile_close at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Alright, guys. Now that the party is about to be in full swing...'
 show mion_v007 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Tonight, an ol' Santa brought presents here for everyoooone!!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide mion_v007
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show miyuki_v006 odoroki at mei_left
 show mion_v007 smile at mei_right
 with Dissolve(0.5)
 show mion_v007 smile at inactive
 show miyuki_v006 odoroki at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Woah... a present from Mion?'
 show miyuki_v006 odoroki at inactive
 show mion_v007 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Noooope~! This ol' man is an ol' man, but these were actually from ol' man Yoshiro!"
 hide miyuki_v006
 show rena_v007 smile at mei_left
 with Dissolve(0.5)
 show mion_v007 smile at inactive
 show rena_v007 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "Hau~, Angel Mort's manager?"
 hide mion_v007
 show shion_v006 smile at mei_right
 with Dissolve(0.5)
 show rena_v007 smile at inactive
 show shion_v006 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Yep, that's right. Uncle Yoshiro happened to be out in Tokyo by chance while he requested everyone to work part time temporarily over Christmas."
 show rena_v007 smile at inactive
 show shion_v006 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Instead of an additional bonus for all of us working overtime, he went out and brought these back for everyone.'
 hide rena_v007
 show kazuho_v007 odoroki at mei_left
 with Dissolve(0.5)
 show shion_v006 smile at inactive
 show kazuho_v007 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Eh... R-Really?'
 show kazuho_v007 odoroki at inactive
 show shion_v006 fuan at active
 show shion_v006 fuan at nod_transform
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Yes. According to him, he actually did mean to tack on a bonus to it, but with Rika-chama and kids, that becomes a different issue...'
 hide kazuho_v007
 show rika_v009 fuan at mei_left
 with Dissolve(0.5)
 show shion_v006 fuan at inactive
 show rika_v009 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep. Setting helping out aside, there are too many issues in giving us honest labor.'
 hide shion_v006
 hide rika_v009
 with Dissolve(0.2)
 show kazuho_v007 fuan at mei_center
 with Dissolve(0.5)
 show kazuho_v007 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Th-that's also true... considering your age and stuff."
 hide kazuho_v007
 with Dissolve(0.2)
 show rena_v007 fuan at mei_left
 show mion_v007 smile at mei_right
 with Dissolve(0.5)
 show mion_v007 smile at inactive
 show rena_v007 fuan at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Hau... but then at this point, I wonder if there would have been issues with Mii-chan and Shii-chan working too... working too?'
 show rena_v007 fuan at inactive
 show mion_v007 smile at active
 show mion_v007 smile at jump_transform
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "No, that's, uh... It's okay because we're relatives!"
 hide rena_v007
 show shion_v006 smile at mei_left
 with Dissolve(0.5)
 show mion_v007 smile at inactive
 show shion_v006 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Yep, yep. Anyway, we're giving out presents now~!"
 hide mion_v007
 show miyuki_v006 odoroki at mei_right
 with Dissolve(0.5)
 show shion_v006 smile at inactive
 show miyuki_v006 odoroki at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Woah, dodging the question I see.'
 hide shion_v006
 show nao_v006 smile at mei_left
 with Dissolve(0.5)
 show miyuki_v006 odoroki at inactive
 show nao_v006 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Well, that's okay. Pointing out every little thing is more boorish on our end."
 hide miyuki_v006
 hide nao_v006
 with Dissolve(0.2)
 show satoko_v006 smile at mei_center
 with Dissolve(0.5)
 show satoko_v006 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Well then, I will gladly accept some presents. If we were only going to make do with the party, I would have planned on having the favor returned to me in the future, but...'
 show satoko_v006 smile at active
 show satoko_v006 smile at updown_shake_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "I'd probably reconsider that scenario depending on the contents of the presents anyway~! Ohohohoho!"
 hide satoko_v006
 with Dissolve(0.2)
 show hanyuu_v010 smile at mei_left
 show mion_v007 smile at mei_right
 with Dissolve(0.5)
 show mion_v007 smile at inactive
 show hanyuu_v010 smile at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") "Au au, speaking of, what's in those presents?"
 show hanyuu_v010 smile at inactive
 show mion_v007 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'A bunch of stuff~. They were already wrapped when he handed them to us, so we never actually figured out what they had inside.'
 hide hanyuu_v010
 show shion_v006 smile at mei_left
 with Dissolve(0.5)
 show mion_v007 smile at inactive
 show shion_v006 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "So, let's get to unwrapping them right away!"
 hide shion_v006
 show rena_v007 smile at mei_left
 with Dissolve(0.5)
 show mion_v007 smile at inactive
 show rena_v007 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Hau~! My heart is super thumping thinking about what type of present I got~!'
 play audio 'audio/sfx/SE_5037_getup.wav'
 show rena_v007 smile at inactive
 show mion_v007 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Here, let's give Rena the one with the kyute wrapping paper.\nAnd Kazuho... what about this one?"
 hide rena_v007
 show kazuho_v007 smile at mei_left
 with Dissolve(0.5)
 show mion_v007 smile at inactive
 show kazuho_v007 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Th-thanks.'
 hide mion_v007
 hide kazuho_v007
 with Dissolve(0.2)
 narrator '{i}Boop{/i}, I accept the present that was handed to me.\n...The subdued pattern of the design somehow suits my tastes.'
 show mion_v007 smile at mei_right
 with Dissolve(0.5)
 show mion_v007 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Miyuki, here's yours, and Nao-chan, here's yours.\nNext is Hanyuu, Rika, Satoko... and all's that's left is Shion and I..."
 show shion_v006 smile at mei_left
 with Dissolve(0.5)
 show mion_v007 smile at inactive
 show shion_v006 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "I'm fine being last.\n...Has everyone received one?"
 hide mion_v007
 hide shion_v006
 with Dissolve(0.2)
 show rika_v009 normal at mei_left
 show hanyuu_v010 smile at mei_right
 with Dissolve(0.5)
 show hanyuu_v010 smile at inactive
 show rika_v009 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Meep. Just from a glance, I can't tell what's inside at all."
 show rika_v009 normal at inactive
 show hanyuu_v010 smile at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") "Au au. Let's try opening it right away!"
 hide hanyuu_v010
 hide rika_v009
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_528_unfold_cloth.wav'
 narrator "Following along with Hanyuu's voice, everyone tore into their gifts."
 show miyuki_v006 smile at mei_center
 with Dissolve(0.5)
 show miyuki_v006 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Kazuho, Nao. What was in yours?'
 hide miyuki_v006
 with Dissolve(0.2)
 show nao_v006 smile at mei_right
 show kazuho_v007 smile at mei_left
 with Dissolve(0.5)
 show kazuho_v007 smile at inactive
 show nao_v006 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Mine was a stylish candle... \nQuite tasteful if you ask me.'
 show nao_v006 smile at inactive
 show kazuho_v007 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Mine was... ah, a purse.'
 hide kazuho_v007
 hide nao_v006
 with Dissolve(0.2)
 narrator 'Inside my gift was a fashionable purse.'
 show miyuki_v006 smile at mei_right
 with Dissolve(0.5)
 show miyuki_v006 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Oooh, cool, yours give off a mature feel!'
 show kazuho_v007 smile at mei_left
 with Dissolve(0.5)
 show miyuki_v006 smile at inactive
 show kazuho_v007 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'And what about Miyuki-chan?'
 play audio 'audio/sfx/SE_326_ls_spacestop.wav'
 show kazuho_v007 smile at inactive
 show miyuki_v006 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Socks! They look so nice and warm!'
 hide kazuho_v007
 show nao_v006 smile at mei_left
 with Dissolve(0.5)
 show miyuki_v006 smile at inactive
 show nao_v006 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Wool? They're very high quality. These look really expensive."
 show nao_v006 smile at inactive
 show miyuki_v006 fuan at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "O-Oh... I know you're interested in them, but it's a Christmas present, so don't try to guess what the price is, yeah...?"
 hide miyuki_v006
 hide nao_v006
 with Dissolve(0.2)
 show rena_v007 smile_blush at mei_center
 with Dissolve(0.5)
 show rena_v007 smile_blush at active
 show rena_v007 smile_blush at jump_transform
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Hau~, Rena got a music box! So kyute~~!!'
 hide rena_v007
 with Dissolve(0.2)
 show mion_v007 odoroki at mei_right
 with Dissolve(0.5)
 show mion_v007 odoroki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "This ol' man got a... geh, a lace handkerchief...?"
 show shion_v006 smile at mei_left
 with Dissolve(0.5)
 show mion_v007 odoroki at inactive
 show shion_v006 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "My, isn't that nice? How about you use that lace handkerchief to turn yourself into a wonderful lady from today forward?"
 show shion_v006 smile at inactive
 show mion_v007 sinken at active
 show mion_v007 sinken at chara_shake_transform
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Hell no! I've already had my fill of styles outside of my usual charm!"
 show mion_v007 sinken at inactive
 show shion_v006 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Should we exchange presents, then?\nMine was a namebrand perfume, though.'
 show shion_v006 smile at inactive
 show mion_v007 odoroki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Isn't that worse?! Where would I use that? And when?!"
 show shion_v006 smile at inactive
 show mion_v007 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Aren't the present choices this time around way too mature?!\nWhere did Uncle even go in Tokyo?"
 hide mion_v007
 hide shion_v006
 with Dissolve(0.2)
 show hanyuu_v010 smile at mei_left
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_577_ls_sanriokirakira.wav'
 show hanyuu_v010 smile at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Au au! Mine had an elegant porcelain bowl inside with konpeito~♪'
 show nao_v006 smile at mei_right
 with Dissolve(0.5)
 show hanyuu_v010 smile at inactive
 show nao_v006 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Ah... that's konpeito from a store in Ginza, Tokyo. I've seen it before; they serve it as a refreshment in that area."
 hide hanyuu_v010
 show shion_v006 fuan at mei_left
 with Dissolve(0.5)
 show nao_v006 smile at inactive
 show shion_v006 fuan at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "The fact that you've seen it is amazing by itself, but to remember it this well..."
 hide nao_v006
 show satoko_v006 smile at mei_right
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_528_unfold_cloth.wav'
 show shion_v006 fuan at inactive
 show satoko_v006 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "There's quite the variety among these presents, isn't there? \nNow then, I wonder what mine is..."
 hide shion_v006
 hide satoko_v006
 with Dissolve(0.2)
 narrator 'As she said that, Satoko-chan opened her package...'
 show satoko_v006 normal at mei_center
 with Dissolve(0.5)
 show satoko_v006 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '............'
 hide satoko_v006
 with Dissolve(0.2)
 narrator 'She froze in the position she opened the package in.'
 show kazuho_v007 fuan at mei_center
 with Dissolve(0.5)
 show kazuho_v007 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "(Satoko-chan? I wonder what's wrong...?)"
 hide kazuho_v007
 with Dissolve(0.2)
 narrator 'I was wondering if I should ask her, but then she quickly hid the present next to her feet and faced Rika-chan.'
 show satoko_v006 smile at mei_right
 show rika_v009 normal at mei_left
 with Dissolve(0.5)
 show rika_v009 normal at inactive
 show satoko_v006 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'R-Rika, what did you get? Come on, show it to us already!'
 show satoko_v006 smile at inactive
 show rika_v009 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep? Umm, mine is...'
 hide rika_v009
 hide satoko_v006
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_5037_getup.wav'
 narrator 'Hastened by Satoko-chan, Rika-chan takes to opening her present, which had still been left unopen.'
 narrator 'And what she brought out from the package was...'
 show rika_v009 smile at mei_left
 show satoko_v006 smile at mei_right
 with Dissolve(0.5)
 show satoko_v006 smile at inactive
 show rika_v009 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...Meep. It's a scarf."
 show rika_v009 smile at inactive
 show satoko_v006 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Oh my, it looks like a fox tail! How about you wear it right away, Rika?'
 show satoko_v006 smile at inactive
 show rika_v009 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep. Before I do that, what did you get, Satoko?'
 show rika_v009 normal at inactive
 show satoko_v006 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '...U-Um.'
 hide rika_v009
 show kazuho_v007 normal at mei_left
 with Dissolve(0.5)
 show satoko_v006 fuan at inactive
 show kazuho_v007 normal at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Satoko-chan, what's wrong?"
 hide satoko_v006
 hide kazuho_v007
 with Dissolve(0.2)
 narrator 'After I called out to her, Satoko-chan looked at me and Rika-chan with a troubled expression on her face...'
 narrator 'As if giving in, she pulled out the present from the package hidden next to her feet.'
 show satoko_v006 fuan_close at mei_right
 with Dissolve(0.5)
 show satoko_v006 fuan_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Mine was... these gloves.'
 show kazuho_v007 smile at mei_left
 with Dissolve(0.5)
 show satoko_v006 fuan_close at inactive
 show kazuho_v007 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Wow, they look warm and fashionable. Don't you think so, Rika-chan? ...Rika-chan?"
 hide satoko_v006
 hide kazuho_v007
 with Dissolve(0.2)
 show rika_v009 fuan at mei_center
 with Dissolve(0.5)
 show rika_v009 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '............'
 hide rika_v009
 with Dissolve(0.2)
 narrator 'I turned over to Rika-chan, but she kept silent with a complicated look on her face.'
 show kazuho_v007 fuan at mei_left
 show rika_v009 fuan at mei_right
 with Dissolve(0.5)
 show rika_v009 fuan at inactive
 show kazuho_v007 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'U-Um... why are you making those faces? Do you not like the gloves?'
 show kazuho_v007 fuan at inactive
 show rika_v009 fuan_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Meep, that's not it... Satoko actually bought new gloves not too long ago."
 show rika_v009 fuan_close at inactive
 show kazuho_v007 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Ah...'
 hide rika_v009
 hide kazuho_v007
 with Dissolve(0.2)
 narrator "After hearing that, I shut my mouth in consideration for those two's feelings."
 narrator "There's no real harm in having two pairs of gloves.\n...But just after buying new gloves, it's iffy receiving another brand-new pair."
 show satoko_v006 smile at mei_right
 with Dissolve(0.5)
 show satoko_v006 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Ah, um... well, there's no issue. Now I have two gloves I can choose between depending on how I feel!"
 show rika_v009 fuan at mei_left
 with Dissolve(0.5)
 show satoko_v006 smile at inactive
 show rika_v009 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Satoko...'
 show rika_v009 fuan at inactive
 show satoko_v006 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'And look, these gloves give off a bit of a grown-up aura to them, and the design fits me beautifully~!'
 hide satoko_v006
 hide rika_v009
 with Dissolve(0.2)
 narrator 'Satoko-chan merrily held the gloves as she said that. ...But it bothered us as we were fully aware that she was pushing herself.'
 show satoko_v006 fuan at mei_right
 show rika_v009 normal at mei_left
 with Dissolve(0.5)
 show rika_v009 normal at inactive
 show satoko_v006 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "O-Oh my...? They're a bit big. But surely I'll grow into them, and they'll..."
 show satoko_v006 fuan at inactive
 show rika_v009 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...Satoko. Would you like to swap mine for yours?'
 show rika_v009 smile at inactive
 show satoko_v006 odoroki at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Huh...?'
 show satoko_v006 odoroki at inactive
 show rika_v009 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "If we exchange that scarf and those gloves, it'll all end well."
 show rika_v009 smile at inactive
 show satoko_v006 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "B-But... you liked that scarf, didn't you?\nWhen you saw it earlier you looked really happy..."
 show satoko_v006 fuan at inactive
 show rika_v009 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep. But I think this scarf would certainly look better on you than me.'
 show satoko_v006 fuan at inactive
 show rika_v009 smile_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Plus, since the day you bought those gloves, I also felt like I wanted new ones myself.'
 show satoko_v006 fuan at inactive
 show rika_v009 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "So, I'd like to trade with you. Nipah~"
 show rika_v009 smile at inactive
 show satoko_v006 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Rika...'
 hide rika_v009
 hide satoko_v006
 with Dissolve(0.2)
 narrator 'While holding the gloves, Satoko looked all over the room searching for an answer... then she finally met my gaze with a few blinks.'
 narrator 'I was kind of lost for words watching it... but I shared what I had to say.'
 show kazuho_v007 smile at mei_left
 show satoko_v006 fuan at mei_right
 with Dissolve(0.5)
 show satoko_v006 fuan at inactive
 show kazuho_v007 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "...Wouldn't it be nice to trade?"
 show kazuho_v007 smile at inactive
 show satoko_v006 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'B-But... this was something that was gifted to Rika...'
 hide satoko_v006
 hide kazuho_v007
 with Dissolve(0.2)
 show kazuho_v007 smile at mei_center
 with Dissolve(0.5)
 show kazuho_v007 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "That's true, but Mion-san handed out these presents randomly..."
 show kazuho_v007 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'So instead, maybe Rika-chan should have actually gotten the gloves... and Satoko-chan should have gotten the scarf.'
 show kazuho_v007 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Fate only played a prank on you, switching out both of your presents... Why not try thinking about it that way?'
 hide kazuho_v007
 with Dissolve(0.2)
 show rika_v009 normal at mei_left
 show satoko_v006 normal at mei_right
 with Dissolve(0.5)
 show satoko_v006 normal at active
 show rika_v009 normal at active
 Character('Rika and Satoko',ctc="ctcArrow", ctc_position="fixed") '............'
 hide satoko_v006
 hide rika_v009
 with Dissolve(0.2)
 narrator 'After I finished saying that, Rika-chan and Satoko-chan... just stare at me blankly.'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show kazuho_v007 odoroki_blush at mei_center
 with Dissolve(0.08333333333333333)
 show kazuho_v007 odoroki_blush at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Ah, um, aaah...!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide kazuho_v007
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 narrator 'It made me realize that I had said something terrifyingly embarrassing. That feeling rose up to my face, making it heat up with a puff of steam.'
 show kazuho_v007 fuan at mei_center
 with Dissolve(0.5)
 show kazuho_v007 fuan at active
 show kazuho_v007 fuan at chara_shake_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Ah, uh, um... I must have heard that in a TV soap, um, uhhh...!'
 hide kazuho_v007
 with Dissolve(0.2)
 narrator 'I was panicking and flustered and grasping for literally anything to say next when Rika-chan smiled softly at me.'
 show rika_v009 smile at mei_left
 show satoko_v006 normal at mei_right
 with Dissolve(0.5)
 show satoko_v006 normal at inactive
 show rika_v009 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...Meep. Kazuho is right. Our presents were switched since fate played a prank on us.'
 show satoko_v006 normal at inactive
 show rika_v009 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "So, it's okay for Satoko to receive this scarf♪"
 show rika_v009 smile at inactive
 show satoko_v006 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "...I understand. I'll accept it gratefully then."
 show satoko_v006 smile at inactive
 show rika_v009 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Okay, Satoko, please come closer. I'll put it around you."
 show rika_v009 smile at inactive
 show satoko_v006 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Eh? I-It's okay. I can do that myself..."
 show satoko_v006 fuan at inactive
 show rika_v009 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep. Just behave and sit down.'
 hide satoko_v006
 hide rika_v009
 with Dissolve(0.2)
 narrator "Forcefully making her sit down, Rika-chan swiftly wraps the scarf around Satoko-chan's neck."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show satoko_v006 smile_blush at mei_center
 with Dissolve(0.08333333333333333)
 show satoko_v006 smile_blush at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '............'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide satoko_v006
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 narrator "The long scarf was a little too big and covered about half of Satoko-chan's face... but she smiled shyly."
 show satoko_v006 smile at mei_right
 show rika_v009 smile at mei_left
 with Dissolve(0.5)
 show rika_v009 smile at inactive
 show satoko_v006 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "...It's very warm."
 show satoko_v006 smile at inactive
 show rika_v009 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep. It looks good on you after all.'
 hide rika_v009
 hide satoko_v006
 with Dissolve(0.2)
 narrator "While saying that, she pats Satoko's head."
 show satoko_v006 smile_close at mei_center
 with Dissolve(0.5)
 show satoko_v006 smile_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '............'
 hide satoko_v006
 with Dissolve(0.2)
 narrator "Then, Satoko-chan softly grabbed ahold of both Rika-chan's free hand and the one that had been caressing her head and brought them in front of the two of them."
 show satoko_v006 smile at mei_center
 with Dissolve(0.5)
 show satoko_v006 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Okay, and in return...'
 hide satoko_v006
 with Dissolve(0.2)
 narrator "Satoko-chan gently slides Rika-chan's hands into the gloves."
 narrator 'Those gloves were a little bit too big for Rika-chan as well, but...'
 narrator "As if they were puzzle pieces being slotted into place, they looked like they were meant to be Rika-chan's from the beginning."
 narrator 'They were so perfect for her that that idea came to mind.'
 show satoko_v006 smile at mei_right
 show rika_v009 smile at mei_left
 with Dissolve(0.5)
 show rika_v009 smile at inactive
 show satoko_v006 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'These gloves really do suit you, Rika... \nMaybe the presents actually were switched.'
 show satoko_v006 smile at inactive
 show rika_v009 smile at active
 show rika_v009 smile at nod_transform
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Yes... but now, they're back to where they belong."
 hide rika_v009
 hide satoko_v006
 with Dissolve(0.2)
 narrator 'My mouth naturally loosened into a smile as I watched the two of them grinning at each other.'
 show kazuho_v007 smile at mei_center
 with Dissolve(0.5)
 show kazuho_v007 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'What a relief; you two have... wah!?'
 hide kazuho_v007
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_101_hit_strike1.wav'
 narrator 'All of a sudden, something flung into me and hit me like a truck...?!'
 show kazuho_v007 odoroki at mei_outerleft
 show miyuki_v006 smile at mei_right
 with Dissolve(0.5)
 show miyuki_v006 smile at inactive
 show kazuho_v007 odoroki at active
 show kazuho_v007 odoroki:
  yanchor 1.0
  linear 0.5 pos (1110,1200)
 pause 0.5
 show kazuho_v007 odoroki:
  yanchor 1.0
  pos (1110,1200)
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Waaah?!'
 play audio 'audio/sfx/SE_5013_down.wav'
 show kazuho_v007 odoroki at inactive
 show miyuki_v006 odoroki at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'O-Oof!'
 hide miyuki_v006
 hide kazuho_v007
 with Dissolve(0.2)
 narrator 'As I flew back from the impact, Miyuki-chan caught me.'
 show miyuki_v006 fuan at mei_right
 show kazuho_v007 fuan at mei_left
 with Dissolve(0.5)
 show kazuho_v007 fuan at inactive
 show miyuki_v006 fuan at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Woah... you flew over here, Kazuho. You were like Santa getting thrown off his sleigh.'
 show miyuki_v006 fuan at inactive
 show kazuho_v007 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'H-Huh? When did I become Santa?'
 hide miyuki_v006
 show mion_v007 fuan at mei_right
 with Dissolve(0.5)
 show kazuho_v007 fuan at inactive
 show mion_v007 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Well, it wasn't a reindeer running buck wild... but it's safe to say {i}something{/i} running buck wild is involved."
 hide kazuho_v007
 hide mion_v007
 with Dissolve(0.2)
 narrator '"Check it", and what Mion-san pointed to was...'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show rena_v007 smile_blush at mei_center
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_215_heartgrow.wav'
 show rena_v007 smile_blush at active
 show rena_v007 smile_blush at jumping_transform
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Hauu!! Rika-chan, Satoko-chan, you two are so kyute~!!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide rena_v007
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 narrator "Rika-chan and Satoko-chan were stuffed into Rena-san's arms as she was grinning from ear to ear."
 show kazuho_v007 fuan at mei_center
 with Dissolve(0.5)
 show kazuho_v007 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'W-What happened...?'
 hide kazuho_v007
 with Dissolve(0.2)
 show mion_v007 fuan_close at mei_right
 show shion_v006 fuan at mei_left
 with Dissolve(0.5)
 show shion_v006 fuan at inactive
 show mion_v007 fuan_close at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Don't think bad of her, okay, Kazuho?"
 show mion_v007 fuan_close at inactive
 show shion_v006 fuan at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "It seems that seeing Rika-chama and Satoko made some of Rena-san's loose screws fall off completely."
 hide shion_v006
 hide mion_v007
 with Dissolve(0.2)
 show kazuho_v007 fuan at mei_center
 with Dissolve(0.5)
 show kazuho_v007 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Th-that I understood, but...'
 hide kazuho_v007
 with Dissolve(0.2)
 show nao_v006 fuan_close at mei_left
 show hanyuu_v010 fuan_close at mei_right
 with Dissolve(0.5)
 show hanyuu_v010 fuan_close at inactive
 show nao_v006 fuan_close at active
 show nao_v006 fuan_close at chara_shake_transform
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'H-Howahh...'
 show nao_v006 fuan_close at inactive
 show hanyuu_v010 fuan_close at active
 show hanyuu_v010 fuan_close at chara_shake_transform
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'A-Au au...'
 hide hanyuu_v010
 hide nao_v006
 with Dissolve(0.2)
 show kazuho_v007 fuan at mei_left
 with Dissolve(0.5)
 show kazuho_v007 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'W-Why are Nao-chan and Hanyuu-chan over there with their eyes spinning...?'
 show miyuki_v006 fuan_close at mei_right
 with Dissolve(0.5)
 show kazuho_v007 fuan at inactive
 show miyuki_v006 fuan_close at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "The destruction in Rena's wake."
 hide kazuho_v007
 hide miyuki_v006
 with Dissolve(0.2)
 narrator '...Just with those few words, I caught onto what happened.'
 show rena_v007 smile_blush at mei_center
 show satoko_v006 odoroki at mei_right
 show rika_v009 fuan at mei_left
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_5005_grab.wav'
 show rika_v009 fuan at inactive
 show satoko_v006 odoroki at inactive
 show rena_v007 smile_blush at active
 show rena_v007 smile_blush at chara_shake_transform
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "Hau~, at this rate, I'm gonna want to take eeeeveryone here home with me as a Christmas preseeeenttt~!"
 show rika_v009 fuan at inactive
 show rena_v007 smile_blush at inactive
 show satoko_v006 odoroki at active
 show satoko_v006 odoroki at jump_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Gweh?! Hol-, Rena-san!'
 show satoko_v006 odoroki at inactive
 show rena_v007 smile_blush at inactive
 show rika_v009 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "D-Don't hold us so tightly...!"
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 play audio 'audio/sfx/SE_215_heartgrow.wav'
 show rika_v009 fuan at inactive
 show satoko_v006 odoroki at inactive
 show rena_v007 smile_blush at active
 show rena_v007 smile_blush at chara_shake_transform
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "But, but, you're so kyuuuuutee!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide rika_v009
 hide satoko_v006
 hide rena_v007
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 narrator '{i}Squeeeeze{/i}, Rena-san had Rika-chan and Satoko-chan tight in her clutches.'
 narrator 'It looked a little bit painful... but the two of them looked like they were having fun being held together perfectly, no gaps between them.'
 show satoko_v006 fuan at mei_right
 show rika_v009 fuan at mei_left
 with Dissolve(0.5)
 show rika_v009 fuan at inactive
 show satoko_v006 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Jeez, how troublesome this is, even if this is the same old pattern...'
 show satoko_v006 fuan at inactive
 show rika_v009 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...*giggle*.'
 show rika_v009 smile at inactive
 show satoko_v006 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") '*chuckle*...'
 show rika_v009 smile at active
 show satoko_v006 smile at active
 Character('Rika and Satoko',ctc="ctcArrow", ctc_position="fixed") 'Ahahahaha...'
 call chapter_end
 jump event01_33_04