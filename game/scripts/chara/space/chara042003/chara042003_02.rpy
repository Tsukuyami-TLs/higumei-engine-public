label chara042003_02:
 show black_background onlayer black
 $ event_store.current_event='chara042003'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara042003_02'
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
 show expression 'images/bg/AdvBg_021.png' as bg
 play music "<loop 2.36>audio/bgm/BGM_EVENT1.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show mion_v002 sinken at mei_left
 with Dissolve(0.5)
 show mion_v002 sinken at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Anyways, Kei-chan, let's get this battle started!\nAnd no hard feelings whoever loses, right?"
 show keiichi_v002 futeki at mei_right
 with Dissolve(0.5)
 show mion_v002 sinken at inactive
 show keiichi_v002 futeki at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "Yeah, that's fine by me! I won't allow you to complain or make excuses when I'm done with you either!"
 show keiichi_v002 futeki at inactive
 show mion_v002 futeki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Hahah, as if I'd do something as shameful as that!\nAlright, is everyone ready?"
 hide keiichi_v002
 show miyuki_v002 normal at mei_right
 with Dissolve(0.5)
 show mion_v002 futeki at inactive
 show miyuki_v002 normal at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Umm, well, ready or not... you seriously plan on duking it out with {b}Role Cards{/b} to decide if the protagonist should use a sword or a gun?'
 show miyuki_v002 normal at inactive
 show mion_v002 futeki_close at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Of course! That's the reason I got express permission from the town council to run wild here!"
 hide miyuki_v002
 show rena_v002 fuan at mei_right
 with Dissolve(0.5)
 show mion_v002 futeki_close at inactive
 show rena_v002 fuan at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "Hau... Mii-chan, no matter how you look at it, isn't this maybe going a little overboard... a little overboard?"
 show rena_v002 fuan at inactive
 show mion_v002 sinken at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'What are you guys even saying?! We got the hopes of hundreds of billions of gun lovers and fanatics all over the country riding on our backs!'
 show rena_v002 fuan at inactive
 show mion_v002 sinken at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "If I let them down, I'd lose my right to call myself a woman!\nNo, I'd never be able to face them regardless of gender!"
 hide rena_v002
 show shion_v002 normal at mei_right
 with Dissolve(0.5)
 show mion_v002 sinken at inactive
 show shion_v002 normal at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Um... that number goes far beyond the population of people on Earth altogether. Are you positive you're not also adding ghosts to that number, Sis?"
 hide mion_v002
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show shion_v002 normal at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...It's like you've completely lost sight of yourself. I was thinking that your aggression would subside a bit after making up with Maebara-san."
 hide shion_v002
 show satoko_v002 normal_close at mei_right
 with Dissolve(0.5)
 show nao_v002 fuan at inactive
 show satoko_v002 normal_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Either way, it's apparent that Mion-san has a habit of flushing her usual rationale down the drain whenever Keiichi-san is involved..."
 hide nao_v002
 show hanyuu_v002 fuan at mei_left
 with Dissolve(0.5)
 show satoko_v002 normal_close at inactive
 show hanyuu_v002 fuan at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Au au... instead of just disliking the person like other people do, her competitiveness gets stronger, which makes the danger of the situation level up even more... wh-, hyaaaaa?!'
 hide satoko_v002
 show hanyuu_v002 fuan at jumping_transform
 show rika_v002 smile at mei_right
 with Dissolve(0.5)
 show hanyuu_v002 fuan at inactive
 show rika_v002 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Meep, I'm sorry.\nI accidentally pulled the trigger and a bullet shot out. Nipah~."
 show rika_v002 smile at inactive
 show hanyuu_v002 fuan at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Of course a bullet will shoot out if you pull the trigger, au au auu!'
 hide rika_v002
 show satoko_v002 fuan at mei_right
 with Dissolve(0.5)
 show hanyuu_v002 fuan at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "W-Well... danger levels certainly do rise massively when there's no ill will involved... but..."
 hide hanyuu_v002
 hide satoko_v002
 with Dissolve(0.2)
 show kazuho_v002 fuan at mei_left
 with Dissolve(0.5)
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "U-Um... Mion-san. I completely understand that we're having a sword versus gun fight... but don't you think the sides are a little unbalanced...?"
 show shion_v002 sinken at mei_right
 with Dissolve(0.5)
 show kazuho_v002 fuan at inactive
 show shion_v002 sinken at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "That's right, Sis! Obviously Kei-chan is on Team Sword, but Kazuho-san and I are the only other members with him, so clearly there's a problem with the distribution! "
 show shion_v002 sinken at inactive
 show kazuho_v002 sinken at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Y-Yeah...! Miyuki-chan should join us since her weapon is a striking type, not ranged...'
 hide shion_v002
 show miyuki_v002 smile_close at mei_right
 with Dissolve(0.5)
 show kazuho_v002 sinken at inactive
 show miyuki_v002 smile_close at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Too bad, Kazuho. Mion told me that firearms are essential for police officers. I'm gonna be siding with her♪"
 hide kazuho_v002
 show shion_v002 sinken at mei_left
 with Dissolve(0.5)
 show miyuki_v002 smile_close at inactive
 show shion_v002 sinken at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "I've barely ever seen Japanese police officers using their guns!\nDid you get our country confused with America?!"
 hide miyuki_v002
 show keiichi_v002 sinken at mei_right
 with Dissolve(0.5)
 show shion_v002 sinken at inactive
 show keiichi_v002 sinken at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "Anyways, Rena should definitely be over here! She has a focus on hatchets and axes and stuff! Nao-chan too, you use a knife, so what's going on?!"
 hide shion_v002
 show mion_v002 futeki at mei_left
 with Dissolve(0.5)
 show keiichi_v002 sinken at inactive
 show mion_v002 futeki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "*cackle*cackle*... what do you mean, Kei-chan?\nRena's punches can take opponents out from over 10 meters away, so she's clearly a gun-type."
 show keiichi_v002 sinken at inactive
 show mion_v002 smile_close at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "As for Nao-chan, well... since Rena's over here, it's a no brainer she'd join the same team."
 hide keiichi_v002
 show shion_v002 sinken at mei_right
 with Dissolve(0.5)
 show mion_v002 smile_close at inactive
 show shion_v002 sinken at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "These conditions are way too forced! The latter isn't even close to a reason at all! Rena-san, Nao-san, are you really okay with this?!"
 hide mion_v002
 show rena_v002 fuan at mei_left
 with Dissolve(0.5)
 show shion_v002 sinken at inactive
 show rena_v002 fuan at active
 show rena_v002 fuan at leftright_shake_transform
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'H-Hau... Mii-chan gave me invitation tickets to the Dessert Festa, so...'
 hide shion_v002
 show nao_v002 fuan at mei_right
 with Dissolve(0.5)
 show rena_v002 fuan at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...Sorry, Kazuho. Refusal wasn't an option for me since Rena-san invited me to go with her."
 hide rena_v002
 show kazuho_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "O-Oh, right...... wait, Mion-san, isn't that you bribing them...?!"
 hide nao_v002
 hide kazuho_v002
 with Dissolve(0.2)
 show mion_v002 smile_close at mei_center
 with Dissolve(0.5)
 show mion_v002 smile_close at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Mmm? Ahahaha, it's nothing like that. I just had so much politeness spilling out of me that I asked the two of them if they wanted to go."
 show mion_v002 futeki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...Well, I also happened to have some Dessert Festa tickets in my pocket that were about to expire, so I handed them over rather than let 'em go to waste, y'know~?"
 hide mion_v002
 show kazuho_v002 fuan at mei_center
 with Dissolve(0.5)
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "(Th-that's dirty...! I thought she was just our enemy before, but could her demonic energy be growing even further past that...?!)"
 hide kazuho_v002
 with Dissolve(0.2)
 show satoko_v002 smile at mei_left
 with Dissolve(0.5)
 show satoko_v002 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'And of course, Rika and I were added onto Team Gun as well. Ohohohohoho!'
 show rika_v002 smile_close at mei_right
 with Dissolve(0.5)
 show satoko_v002 smile at inactive
 show rika_v002 smile_close at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Meep. I'm just supporting the strong for my own good. Nipah~♪"
 hide satoko_v002
 show hanyuu_v002 fuan at mei_left
 with Dissolve(0.5)
 show rika_v002 smile_close at inactive
 show hanyuu_v002 fuan at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'A-Au au... I also value my life~.'
 hide rika_v002
 hide hanyuu_v002
 with Dissolve(0.2)
 show keiichi_v002 sinken at mei_left
 with Dissolve(0.5)
 show keiichi_v002 sinken at active
 show keiichi_v002 sinken at chara_shake_transform
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "Damn... I was preparing to be at a disadvantage, but I didn't think it'd be a 3v7. That's much worse than I expected!"
 show shion_v002 normal at mei_right
 with Dissolve(0.5)
 show keiichi_v002 sinken at inactive
 show shion_v002 normal at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'What do we do, Kei-chan? We might still have time to back out if we get on our knees and surrender.'
 $ event_store.current_progress = 1
 show shion_v002 normal at inactive
 show keiichi_v002 futeki at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") 'Heh... what kind of loser would do that?!\nOne of us can take three of them on {note_green}Shinsengumi{/note_green} style!'
 hide shion_v002
 show kazuho_v002 fuan at mei_right
 with Dissolve(0.5)
 show keiichi_v002 futeki at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "M-Maebara-kun, it's the reverse!\nThree of us versus one of them would be the right way to go!\nIf it's one person versus three, we'll just get shot uuuup...!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide keiichi_v002
 hide kazuho_v002
 hide fade onlayer curtain
 show keiichi_v002 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show keiichi_v002 sinken at active
 Character('Keiichi Maebara',ctc="ctcArrow", ctc_position="fixed") "Let's go! Uuooooooohhh!\nShion-chan, Kazuho-chan, follow my leeeeeeead!!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide keiichi_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show shion_v002 normal at mei_left
 with Dissolve(0.5)
 show shion_v002 normal at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...It likely goes without saying, but Kei-chan certainly isn't going to live a long life."
 show kazuho_v002 fuan at mei_right
 with Dissolve(0.5)
 show shion_v002 normal at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "(More like the people around him won't...)"
 call chapter_end
 jump chara042003_03