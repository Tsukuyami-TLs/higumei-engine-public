label event01_34_04:
 show black_background onlayer black
 $ event_store.current_event='umi2'
 $ event_store.current_progress=1
 $ event_store.current_chapter='event01_34_04'
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
 show expression 'images/bg/AdvBg_262.png' as bg
 play music "<loop 2.36>audio/bgm/BGM_EVENT1.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator '...We split up, individually taking care of the {b}Tsukuyami{/b} surrounding us, surely and steadily.'
 narrator 'By the time we had completely wiped out the horde from front to back, the sun had gone down... the sky gradually darkening.'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_2462.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 show mion_v002 smile at mei_left
 with Dissolve(0.5)
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") '...In any event, we were able to clear out almost all of the {b}Tsukuyami{/b} in the vicinity. Great work, everyone!'
 show satoko_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at inactive
 show satoko_v002 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Ohohoho! Thanks to them coming at us all at once in that huge crowd, we made easy work out of them~!'
 show mion_v002 smile at inactive
 show satoko_v002 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Miyuki-san in particular had more force in her movements than usual today. She could have scared off a demon lord with her fierce fighting.'
 hide mion_v002
 show miyuki_v002 smile at mei_left
 with Dissolve(0.5)
 show satoko_v002 smile at inactive
 show miyuki_v002 smile at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Ahaha, I guess!\nIf I put my mind to it, I could go neck to neck with an evil deity~♪'
 hide satoko_v002
 hide miyuki_v002
 with Dissolve(0.2)
 narrator 'As Miyuki-chan says that, she puts on a triumphant face and tries to stick out her chest.'
 narrator 'So her father being around does give her strength and motivation...? That girl today was the queen of all trades, never mind jack.'
 show akasaka_v003 smile at mei_right
 show miyuki_v002 smile at mei_left
 with Dissolve(0.5)
 show miyuki_v002 smile at inactive
 show akasaka_v003 smile at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "...But I spent too much time sitting in the back, you know? You aren't fighting alone, so I think you could depend on me a little more."
 show miyuki_v002 smile at inactive
 show akasaka_v003 smile_close at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "I don't want to see any one of you in danger...\nYou understand how important that sentiment is too."
 show miyuki_v002 smile at inactive
 show akasaka_v003 smile at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'I feel as though letting yourself get hurt will be more painful to everyone else, of course, myself included.'
 show akasaka_v003 smile at inactive
 show miyuki_v002 fuan at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Ah...'
 show miyuki_v002 fuan at inactive
 show akasaka_v003 smile at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "Even I don't plan on being weak forever.\nSo, depend on the grown-up just a little bit and he'll be happy."
 show akasaka_v003 smile at inactive
 show miyuki_v002 smile_close at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "...Understood. I'll be careful."
 hide miyuki_v002
 hide akasaka_v003
 with Dissolve(0.2)
 narrator "Miyuki-chan nodded obediently to Akasaka-san's advice. It was like her face was pretending not to be... but happiness was still written all over it."
 narrator 'Even without having to reveal it... being together with her father clearly does bring her great joy.'
 show kazuho_v002 smile at mei_center
 with Dissolve(0.5)
 show kazuho_v002 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "(...Isn't that nice, Miyuki-chan?)"
 hide kazuho_v002
 with Dissolve(0.2)
 narrator "What a pleasant and lovely scene.\nBut what's been bothering us up until now was..."
 show nao_v002 fuan at mei_left
 show akasaka_v003 smile at mei_right
 with Dissolve(0.5)
 show akasaka_v003 smile at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Um... Akasaka-san.\nWhat's up with that outfit?"
 show nao_v002 fuan at inactive
 show akasaka_v003 smile at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Ah, this? When I used the {b}Role Card{/b} you lent me, it changed me into this.'
 hide nao_v002
 show satoko_v002 normal at mei_left
 with Dissolve(0.5)
 show akasaka_v003 smile at inactive
 show satoko_v002 normal at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "...It looks quite like Battler-san's outfit, doesn't it?"
 hide satoko_v002
 show battler_v001 smile at mei_left
 with Dissolve(0.5)
 show akasaka_v003 smile at inactive
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Now that you say it, it looks {i}just{/i} like my suit, huh?'
 show battler_v001 smile at inactive
 show akasaka_v003 fuan at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Ah, sorry. Does it offend you?'
 hide akasaka_v003
 hide battler_v001
 with Dissolve(0.2)
 show battler_v001 smile at mei_center
 with Dissolve(0.5)
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'No, no, not at all. Kinda looks like I have an older brother now. Not bad! Ihihihi!'
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "But... that's funny? Even when I used a {b}Role Card{/b}, my clothes and stuff didn't do jack."
 show battler_v001 fuan_close at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Tch... I was hoping for something more like... a sick transformation into a tension-raising outfit!'
 hide battler_v001
 with Dissolve(0.2)
 show hanyuu_v002 smile at mei_left
 show battler_v001 smile at mei_right
 with Dissolve(0.5)
 show battler_v001 smile at inactive
 show hanyuu_v002 smile at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'What kind of outfit would you like?'
 show hanyuu_v002 smile at inactive
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Mmm, good question...'
 hide hanyuu_v002
 show satoko_v002 smile at mei_left
 with Dissolve(0.5)
 show battler_v001 normal at inactive
 show satoko_v002 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'What about a breastplate and a helmet? \nI feel that would raise your defensive stats quite a lot~!'
 hide battler_v001
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show satoko_v002 smile at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "But wouldn't that make it difficult to move around in the mountains?\nFor me, I think light armor would definitely be the better way to go."
 hide satoko_v002
 show rena_v002 smile at mei_left
 with Dissolve(0.5)
 show mion_v002 smile at inactive
 show rena_v002 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Hau... Rena thinks something kyute would be best!\nMaybe a big Mr. Bear suit, Bear suit?'
 show rena_v002 smile at inactive
 show mion_v002 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...That's even worse in terms of mobility, though?"
 hide mion_v002
 hide rena_v002
 with Dissolve(0.2)
 show satoko_v002 fuan at mei_right
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "If Battler-san put a big bear head on, wouldn't he pass 2 meters in height?"
 show satoko_v002 fuan at inactive
 show nao_v002 fuan_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...At that point, he would make it look like it was an actual bear instead of a guy in a costume.'
 hide nao_v002
 hide satoko_v002
 with Dissolve(0.2)
 show mion_v002 fuan at mei_center
 with Dissolve(0.5)
 show mion_v002 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "If someone from the hunters' club caught sight of him, they'd probably mistake him for one and gun him down on the spot, huh?"
 hide mion_v002
 with Dissolve(0.2)
 show rika_v002 smile at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at inactive
 show rika_v002 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep. I think light armor would definitely be best then.\nButt-naked light... *giggle*.'
 show rika_v002 smile at inactive
 show mion_v002 normal at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Encountering a completely butt-naked enemy...\nYeah, visually speaking, that's pretty intimidating."
 hide rika_v002
 show satoko_v002 fuan at mei_left
 with Dissolve(0.5)
 show mion_v002 normal at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "If you encountered something like that in the back mountains, you'd want to make a break for it even if it wasn't a {b}Tsukuyami{/b}...!"
 hide mion_v002
 show hanyuu_v002 fuan at mei_right
 with Dissolve(0.5)
 show satoko_v002 fuan at inactive
 show hanyuu_v002 fuan at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'I-I feel like seeing a completely naked child would be way too scary!\nAt least put some underwear on...!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide satoko_v002
 hide hanyuu_v002
 hide fade onlayer curtain
 show mion_v002 futeki at mei_center
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_226_shine.wav'
 show mion_v002 futeki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Or a pair of speedos?'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide mion_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...I wonder why, but...\n...that feels even more atrocious than encountering someone naked...'
 hide nao_v002
 with Dissolve(0.2)
 show rena_v002 smile at mei_left
 show mion_v002 futeki at mei_right
 with Dissolve(0.5)
 show mion_v002 futeki at inactive
 show rena_v002 smile at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Ah, then perhaps how would a ballerina outfit be, outfit be?'
 show rena_v002 smile at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Yeah, then the beautiful swan underneath can stretch out its long neck!'
 hide rena_v002
 show satoko_v002 fuan at mei_left
 with Dissolve(0.5)
 show mion_v002 smile at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Is that what a ballerina is?\n ...He'd likely become quite the massive swan."
 hide mion_v002
 show rika_v002 smile at mei_right
 with Dissolve(0.5)
 show satoko_v002 fuan at inactive
 show rika_v002 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep. Maybe even ostrich size.'
 stop music fadeout 0.5
 hide satoko_v002
 hide rika_v002
 with Dissolve(0.2)
 show battler_v001 normal at mei_center
 with Dissolve(0.5)
 show battler_v001 normal at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '............'
 hide battler_v001
 with Dissolve(0.2)
 narrator 'While everyone was getting pumped up in their clothing discussion, Battler-san drooped his shoulders in defeat. Even his face is starting to look sad...?'
 show battler_v001 fuan at mei_right
 show kazuho_v002 fuan at mei_left
 with Dissolve(0.5)
 show kazuho_v002 fuan at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Hey...\nDo you guys hate me or something?'
 show battler_v001 fuan at inactive
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Huh?! W-Why would you think that...?'
 play music "<loop 2.36>audio/bgm/BGM_EVENT1.ogg"
 show kazuho_v002 odoroki at inactive
 show battler_v001 fuan_close at active
 show battler_v001 fuan_close at chara_shake_transform
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Maybe 'cuz... I thought we'd talk about a sick set of armor I'd wear, but it turned into a game where you keep suggesting all these different punishing costumes?"
 show kazuho_v002 odoroki at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Or is this some type of initiation into Hinamizawa...?!'
 show battler_v001 fuan at inactive
 show kazuho_v002 fuan at active
 show kazuho_v002 fuan at jump_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "I'm... I'm sorry! I'm sorry!"
 hide kazuho_v002
 hide battler_v001
 with Dissolve(0.2)
 narrator 'I bow repeatedly to Battler-san, who had asked that question out of sheer embarrassment and annoyance.'
 narrator "It definitely might not be much of an exaggeration to say that it's pretty rude to bully someone we just met this freely..."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show keiichi_v002 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show keiichi_v002 sinken at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "H-Hey, you guys! He's not from the village, so lay off on him, will ya...?"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide keiichi_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show rika_v002 smile at mei_right
 show keiichi_v002 sinken at mei_left
 with Dissolve(0.5)
 show keiichi_v002 sinken at inactive
 show rika_v002 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "...Meep. Keiichi's jealous."
 show rika_v002 smile at inactive
 show keiichi_v002 odoroki at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'Huh...?'
 hide keiichi_v002
 hide rika_v002
 with Dissolve(0.2)
 narrator 'The very moment Rika-chan let out those two words, {i}swwwoooop{/i}!\nEveryone turns over and fixes their gaze on Maebara-kun?!'
 show satoko_v002 smile at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at inactive
 show satoko_v002 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "My, Keiichi-san.\nBattler-san becomes the center of attention, and now you're lonely?"
 play audio 'audio/sfx/SE_226_shine.wav'
 show satoko_v002 smile at inactive
 show mion_v002 futeki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Right, right, okaaaay!\nEveryone, let's continue this clothing conversation with Kei-chan in mind! *cackle*cackle*cackle*...!"
 hide satoko_v002
 show rena_v002 smile_blush at mei_left
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_215_heartgrow.wav'
 show mion_v002 futeki at inactive
 show rena_v002 smile_blush at active
 show rena_v002 smile_blush at jumping_transform
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Hau~! Rena really thinks Keiichi-kun would look best in kyute clothes!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide mion_v002
 hide rena_v002
 hide fade onlayer curtain
 show keiichi_v002 fuan at mei_center
 with Dissolve(0.08333333333333333)
 show keiichi_v002 fuan at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'W-w-whaaat?!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide keiichi_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show kazuho_v002 fuan at mei_center
 with Dissolve(0.5)
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '(The center of attention has shifted to Maebara-kun?!)'
 hide kazuho_v002
 with Dissolve(0.2)
 show mion_v002 smile at mei_center
 with Dissolve(0.5)
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "If we're making Kei-chan wear something, this ol' man indeed thinks a lovely, frilly dress would do wonders!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide mion_v002
 hide fade onlayer curtain
 show keiichi_v002 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 show keiichi_v002 odoroki at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'Huuuh?!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide keiichi_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show satoko_v002 smile at mei_right
 show rika_v002 smile at mei_left
 with Dissolve(0.5)
 show rika_v002 smile at inactive
 show satoko_v002 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "If it's a frilly maid outfit... we could discuss it with the Coach, and if we ask Nao-san, she could probably prepare one in no time at all."
 show satoko_v002 smile at inactive
 show rika_v002 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'I think Battler and Keiichi being in maid outfits together would be nice too. Nipah~'
 hide satoko_v002
 show hanyuu_v002 fuan at mei_right
 with Dissolve(0.5)
 show rika_v002 smile at inactive
 show hanyuu_v002 fuan at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Au au, setting Keiichi aside, I wonder if they have maid outfits the size of Battler out there?'
 hide rika_v002
 show nao_v002 smile at mei_left
 with Dissolve(0.5)
 show hanyuu_v002 fuan at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'The Coach has one for sure. If the measurements are a bit off, I can adjust it myself too.'
 hide hanyuu_v002
 show rena_v002 smile_blush at mei_right
 with Dissolve(0.5)
 show nao_v002 smile at inactive
 show rena_v002 smile_blush at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Hau~, maid outfit besties! \nMaybe the Coach will pick out some Western style ones for them, for them? Heehee, heehehehe!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide nao_v002
 hide rena_v002
 hide fade onlayer curtain
 show keiichi_v002 sinken at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show keiichi_v002 sinken at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'H-Hold on, hold on!\nWhy am I getting dragged into this now?!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide keiichi_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show mion_v002 smile at mei_right
 show rena_v002 smile_blush at mei_left
 with Dissolve(0.5)
 show rena_v002 smile_blush at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Now we just gotta figure out the bottom half...\nThis ol' man highly recommends wearing a miniskirt, y'know!"
 show mion_v002 smile at inactive
 show rena_v002 smile_blush at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Hauuuu~♪\nRena will put in one vote for a long skirt, then!'
 hide mion_v002
 show satoko_v002 normal_close at mei_right
 with Dissolve(0.5)
 show rena_v002 smile_blush at inactive
 show satoko_v002 normal_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Other than the skirt's length, the design is also incredibly important.\nMaybe we could do old-fashioned ones..."
 hide rena_v002
 show rika_v002 smile at mei_left
 with Dissolve(0.5)
 show satoko_v002 normal_close at inactive
 show rika_v002 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'I think a bold skirt with a slit in it would match them nicely.\nMake it go all the way up to the base of the leg so you can see everything too... *giggle*giggle*.'
 hide satoko_v002
 show hanyuu_v002 fuan at mei_right
 with Dissolve(0.5)
 show rika_v002 smile at inactive
 show hanyuu_v002 fuan at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") "I-I don't think a get-up you could get cold in would be very nice... au au."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide rika_v002
 hide hanyuu_v002
 hide fade onlayer curtain
 show keiichi_v002 fuan at mei_center
 with Dissolve(0.08333333333333333)
 show keiichi_v002 fuan at active
 show keiichi_v002 fuan at chara_shake_transform
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'H-Hey...!\nAre you done trying to put us in maid outfits or not?!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide keiichi_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show kazuho_v002 fuan at mei_center
 with Dissolve(0.5)
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'A-Ahhh...!!'
 hide kazuho_v002
 with Dissolve(0.2)
 narrator 'Everyone just keeps rolling with it.\nBut I have no idea how to make them stop...!'
 show kazuho_v002 sinken at mei_center
 with Dissolve(0.5)
 show kazuho_v002 sinken at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "(Th-that's right... Miyuki-chan!\nThe only person who could change the topic is her!)"
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Mi-Miyuki-chan...!'
 hide kazuho_v002
 with Dissolve(0.2)
 narrator 'Just as I expected, everyone turns their heads towards-- me?!'
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show akasaka_v003 smile at mei_right
 show miyuki_v002 smile_blush at mei_left
 with Dissolve(0.5)
 show miyuki_v002 smile_blush at inactive
 show akasaka_v003 smile at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "No, no... You're seriously reliable, Miyuki-san.\nYou got some guts going after all of those monsters without even flinching."
 show miyuki_v002 smile_blush at inactive
 show akasaka_v003 smile at active
 Character('Mamoru Akasaka',ctc="ctcArrow", ctc_position="fixed") "Earlier, you said you aspire to be a police officer, right?\nI'd love for you to be my subordinate down the road."
 play audio 'audio/sfx/SE_311_ls_cutejump.wav'
 show akasaka_v003 smile at inactive
 show miyuki_v002 smile_blush at active
 show miyuki_v002 smile_blush at jump_transform
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "R-Really?! A-Ahaha~, I'm glad to hear you say that, Da-... Akasaka-san."
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 hide miyuki_v002
 hide akasaka_v003
 with Dissolve(0.2)
 narrator '...She seemed like she was having fun chatting with Akasaka-san.\nOn the other hand, my whole body gave off the aura of a third wheel cutting in.'
 camera at screenshake_transform
 pause 0.0
 narrator "And if I did cut in, she'd likely resort to violence even before I got a word out... no, definitely!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show miyuki_v002 smile_blush at mei_center
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_215_heartgrow.wav'
 show miyuki_v002 smile_blush at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "I'll do my best to become a police officer!\nI'll preserve the peace of city life!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide miyuki_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show kazuho_v002 fuan at mei_center
 with Dissolve(0.5)
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '(Rather than city life, focus on the hot spring district first, Miyuki-chan! At this rate, Battler-san is going to end up having the worst possible impression of Hinamizawaaa!)'
 show kazuho_v002 fuan at active
 show kazuho_v002 fuan at chara_shake_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '(The only thing Battler-san will be able to take back as a memory from inspecting this place is them trying to dress him in female clooothes~!!)'
 hide kazuho_v002
 with Dissolve(0.2)
 show battler_v001 normal_close at mei_right
 show keiichi_v002 fuan at mei_left
 with Dissolve(0.5)
 show keiichi_v002 fuan at inactive
 show battler_v001 normal_close at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '...Ah~, you said it, Keiichi.'
 show battler_v001 normal_close at inactive
 show keiichi_v002 fuan at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'Huh, uh, yeah.'
 show keiichi_v002 fuan at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "You say three women make a madhouse... but I didn't think having this many together would make it this chaotic?"
 show battler_v001 fuan at inactive
 show keiichi_v002 normal at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "It's all good. When push comes to shove, we'll be in the same boat... and we won't have to deal with the shame of being in women's clothes alone."
 show keiichi_v002 normal at inactive
 show battler_v001 odoroki at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "H-Hey... Are you sure it's all good?\nAren't you getting kinda near-sighted on this?!"
 show battler_v001 odoroki at inactive
 show keiichi_v002 fuan_close at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "Well, now that it's gotten this far, these girls can't be stopped, so I think it'd be better to take it as is..."
 show keiichi_v002 fuan_close at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Keiichi... you've really been spending time with such powerfully energetic and aggressive girls day in, day out?"
 show battler_v001 fuan at inactive
 show keiichi_v002 fuan at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "A-Ahahaha... This stuff does come up, but it's not every {i}single{/i} day."
 show keiichi_v002 fuan at inactive
 show battler_v001 fuan at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Haha~, I'm honestly impressed...\nIf it were me, I'd absoluuutely get pissed day one."
 show battler_v001 fuan at inactive
 show keiichi_v002 smile at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "Huh, really? Nah, once you get used to it, it's actually pretty fun."
 show battler_v001 fuan at inactive
 show keiichi_v002 smile at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "They mean well, so there's no need to get bent up over it."
 show keiichi_v002 smile at inactive
 show battler_v001 smile at active
 show battler_v001 smile at updown_shake_transform
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Ihihihi! You're cool, Keiichi!\nWanna come to the room I'm staying at? We can chat it up all night!"
 show battler_v001 smile at inactive
 show keiichi_v002 smile at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'Yes, sir!'
 camera:
  parallel:
   linear 0.5 pos (960, 590)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show keiichi_v002 smile at inactive
 show battler_v001 smile at active
 Character('Battler Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Hey, hey, just relax!! When it's just us dudes, there's no need for formalities!"
 show battler_v001 smile at inactive
 show keiichi_v002 smile at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'Yes, si-... I mean, gotcha!'
 show keiichi_v002 smile at active
 show battler_v001 smile at active
 show battler_v001 smile at updown_shake_transform
 show keiichi_v002 smile at updown_shake_transform
 Character('Keiichi and Battler',ctc="ctcArrow", ctc_position="fixed") 'Wahahahahahahaha!!!'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide keiichi_v002
 hide battler_v001
 with Dissolve(0.2)
 stop music fadeout 0.5
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 pause 1.0
 hide fade onlayer curtain
 with Dissolve(1.0)
 show ange_v001 normal at mei_center
 with Dissolve(0.5)
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '...That looks fun, Onii-chan.'
 show ange_v001 normal at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'I wonder how they can have so much fun in this strange world full of monsters.'
 show ange_v001 normal_close at active
 Character('Ange Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '............'
 call chapter_end
 jump event01_34_05