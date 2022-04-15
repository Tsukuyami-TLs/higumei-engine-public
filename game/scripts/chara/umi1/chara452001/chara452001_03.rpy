label chara452001_03:
 show black_background onlayer black
 $ event_store.current_event='chara452001'
 $ event_store.current_progress=2
 $ event_store.current_chapter='chara452001_03'
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
 show expression 'images/bg/AdvBg_591.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator 'Several days later...'
 play music "<loop 0>audio/bgm/BGM_HOME_COLLAB2.ogg"
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Thank you very much--!'
 show nao_v002 smile at mei_center
 with Dissolve(0.5)
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...I didn't think I would get my hands on that this soon. I need to thank Mion-san next time I see her."
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Now that I have what I wanted to get, the next step is getting in touch with them...'
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...How and where did I meet that person?'
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I can't remember... I wonder if it's when I was invited over there."
 show nao_v002 fuan_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...It appears I'll just have to be patient. Well then, back to the house--"
 stop music fadeout 0.5
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_2211.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 show nao_v002 odoroki at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Huh?'
 show nao_v002 odoroki at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'This place...! So that means...?'
 hide nao_v002
 with Dissolve(0.2)
 play music "<loop 0>audio/bgm/BGM_EVENT_TOP_COLLAB2.ogg"
 show beatrice_v001 normal at mei_left
 show nao_v002 odoroki at mei_right
 with Dissolve(0.5)
 show nao_v002 odoroki at inactive
 show beatrice_v001 futeki at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "*cackle*cackle*...! It's been a while."
 show beatrice_v001 futeki at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Beatrice...!'
 show nao_v002 smile at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Have you been well? It seems you desired a meeting and called for me.'
 show nao_v002 smile at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'I had a bit of free time, so I called you here. Mind thanking me? *cackle*cackle*cackle*!'
 show beatrice_v001 smile at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Thank you, Beatrice. I didn't know how I could get a hold of you, so this helped."
 show nao_v002 smile at inactive
 show beatrice_v001 fuan at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "Oh, mm... I didn't think you'd be so straightforward about being grateful."
 show nao_v002 smile at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "Hm...? What's that bag that you're carrying? Something inside smells nice."
 show beatrice_v001 smile at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Ah, you saw...? Here, it's some slightly unusual herbal tea. If you'd like, I thought we could drink it together."
 play audio 'audio/sfx/SE_5037_getup.wav'
 show nao_v002 smile at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "Hoh, a souvenir for the witch? Since you said it was a herbal tea, I wonder what kind of plant it's from..."
 show nao_v002 smile at inactive
 show beatrice_v001 smile at active
 show beatrice_v001 smile at jump_transform
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "...Oooh? If it isn't butterfly pea flower tea."
 show beatrice_v001 smile at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'I really enjoyed drinking it when I was in a foreign country a long time ago, and thought you would like it too.'
 show beatrice_v001 smile at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Since the store in Okinomiya didn't have it, I was able to get it through a friend. So, this is my gift to you."
 show nao_v002 smile at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") '*cackle*... How thoughtful. But to bring tea for a courtesy visit... you truly are interesting.'
 show beatrice_v001 smile at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "It's not like I wanted to do it out of courtesy or anything..."
 show beatrice_v001 smile at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "By the way, Beatrice, what do you think of the tea? I apologize if I chose something you don't like."
 show nao_v002 normal at inactive
 show beatrice_v001 smile_close at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'I am the Golden Witch, Beatrice, who has enjoyed all kinds of teas both ancient and modern for one thousand years, black tea becoming my favorite.'
 show nao_v002 normal at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'I welcome all delicious tea, from the name brands to the hidden gems. Naturally, that includes herbal tea as well.'
 show beatrice_v001 smile at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '*giggle*. Thank goodness. Then try this whenever you feel like it.'
 show nao_v002 smile at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "What do you mean? Isn't answering my invitation, giving me a gift, and then leaving tremendously inelegant?"
 show nao_v002 smile at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "Since you are here, let's brew this and have a tea party. We can hang out for a short while."
 show beatrice_v001 smile at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Thank you. ...I believe I'll accept your treat then. Ah, but where are the teacups...?"
 show nao_v002 smile at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") '...Hah, preparations are being made now.'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide nao_v002
 hide beatrice_v001
 hide fade onlayer curtain
 show nao_v002 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_515_tableware.wav'
 show nao_v002 odoroki at active
 show nao_v002 odoroki at jump_transform
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Wow... a-amazing...! In a single instant, teacups and tea cakes appeared on the table...?!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show beatrice_v001 futeki at mei_center
 with Dissolve(0.5)
 show beatrice_v001 futeki at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") '*cackle*cackle*... This level of magic is simple for me.'
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "Well, if we're talking about skill in teamaking, I'm not as talented as my furniture, Ronove, but between you and me, it's only right that I be your host."
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Hmm... this tea is as fascinating as ever. When you add lemon, it turns from a vivid blue into a red color. It certainly is a magical tea.'
 hide beatrice_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_right
 show beatrice_v001 normal at mei_left
 with Dissolve(0.5)
 show beatrice_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "You say that, but I heard that it's caused by a chemical reaction called a Litmus solution."
 show nao_v002 normal at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Chemistry is also a form of magic. The difference is that numbers have replaced the words explaining how it works.'
 show nao_v002 normal at inactive
 show beatrice_v001 fuan_close at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "Nonetheless, chemistry eventually morphed into anti-magic toxin... Their roots are the same, but I don't know where the two diverged."
 show beatrice_v001 fuan_close at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Now that you mention it, I've heard that magic and science, including chemistry, used to be studied in similar ways."
 show nao_v002 normal at inactive
 show beatrice_v001 normal at active
 show beatrice_v001 normal at nod_transform
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'I have a deep understanding of this. In fact, a few hundred years ago, alchemy, a branch of study that bridged the gap between magic and science, was something that many intellectuals would devote themselves to acquiring knowledge in.'
 show nao_v002 normal at inactive
 show beatrice_v001 normal_close at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'However, magic is delicate, and not everyone can use it...'
 show nao_v002 normal at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'On the other hand, they say that science can be easy for anybody to do, so long as they have the proper equipment and procedures. This is because science and magic are polar opposites. Magic loses its power from--'
 show beatrice_v001 normal at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'But... magic does exist. At the very least, the Golden Witch, Beatrice, was able to help me.'
 stop music fadeout 0.5
 show nao_v002 smile at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") '............'
 play music "<loop 0>audio/bgm/BGM_QUEST8_COLLAB2.ogg"
 show nao_v002 smile at inactive
 show beatrice_v001 normal_close at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'I would like to ask you something.'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide beatrice_v001
 hide nao_v002
 with Dissolve(0.2)
 stop sound
 show expression 'images/card/Card_452001.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Previously, you said you were on the brink of despair, but you were able to find hope after crossing over to that "World".'
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "However, as a result of that, you've experienced an even greater level of tragedy... Perhaps at this point, the only way forward is straight into hell."
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "And even so, you continue to push forward? Wouldn't it have been more peaceful to have met your demise with that initial despair...?"
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...No, I have to keep going. After coming this far, I can't quit halfway through."
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Besides... thanks to all of the "different" results that I\'ve come upon, I understand that there is a possibility I can reach one where things went well by continuing to the end.'
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'I will not disregard the existence of that "possibility". \n...I can\'t ever despair.'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_2211.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 show nao_v002 smile at mei_right
 show beatrice_v001 normal at mei_left
 with Dissolve(0.5)
 show beatrice_v001 normal at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "And aside from that, I've made friends."
 show nao_v002 smile at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Friends?'
 show beatrice_v001 normal at inactive
 show nao_v002 smile_close at active
 show nao_v002 smile_close at nod_transform
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Yeah. They're older, but since they're a little unreliable, I need to be there for them."
 show beatrice_v001 normal at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Because... even they couldn't despair."
 show nao_v002 smile at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") '............'
 show nao_v002 smile at inactive
 show beatrice_v001 smile_close at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'I really do still need to thank you, lost child...... no, "Nao Houtani".'
 show beatrice_v001 smile_close at inactive
 show nao_v002 odoroki at active
 show nao_v002 odoroki at jump_transform
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Huh?'
 show nao_v002 odoroki at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") '*cackle*cackle*... this truly was a pleasantly strange coincidence. I plan to show my face in your village in the future, so I hope you receive me well then.'
 show beatrice_v001 smile at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Yes, of course... but wait, you're going to Hinamizawa? As a witch? How?"
 show nao_v002 smile at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'That would be through magic, of course... but I do not know if you will remember me or have forgotten about me at that point.'
 show beatrice_v001 smile at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I don't want to forget about you, but I don't think there's anything I can do about it."
 show beatrice_v001 smile at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'If it does happen, could we start over with a "Nice to meet you"?'
 show nao_v002 smile at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") '............'
 show beatrice_v001 normal at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Ah, it\'s impossible, huh? But in that case, I wonder if there are options other than starting over with "Nice to meet you".'
 show nao_v002 fuan at inactive
 show beatrice_v001 smile_close at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'No, it\'s not impossible... I get it. When that time comes, let\'s start over with a "Nice to meet you".'
 show nao_v002 fuan at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") '...Then, until we meet again, Nao Houtani.'
 show beatrice_v001 smile at inactive
 show nao_v002 odoroki at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Yeah... ah, wo-... woah!'
 stop music fadeout 0.5
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide beatrice_v001
 hide nao_v002
 with Dissolve(0.2)
 stop sound
 show expression 'images/bg/AdvBg_1161.png' as bg
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 hide fade onlayer curtain
 with Dissolve(1.0)
 show miyuki_v002 sinken at mei_center
 with Dissolve(0.5)
 camera at screenshake_transform
 pause 0.0
 show miyuki_v002 sinken at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") '...Uh...... Nao. Hey, Nao!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide miyuki_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 play music "<loop 0>audio/bgm/BGM_GACHA_COLLAB2.ogg"
 show nao_v002 odoroki at mei_center
 with Dissolve(0.5)
 show nao_v002 odoroki at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Huh?'
 hide nao_v002
 with Dissolve(0.2)
 show kazuho_v002 fuan at mei_left
 show nao_v002 fuan at mei_right
 with Dissolve(0.5)
 show nao_v002 fuan at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'What is it? Are you okay?'
 show kazuho_v002 fuan at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Miyuki... Kazuho? You're shouting; what happened?"
 show nao_v002 fuan at inactive
 show kazuho_v002 sinken at active
 show kazuho_v002 sinken at chara_shake_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "H-Hey... that's my line!"
 hide kazuho_v002
 show miyuki_v002 sinken at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at inactive
 show miyuki_v002 sinken at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'When me and Kazuho got back to the living room, we were surprised to see you, who was supposed to be out of the house, absentmindedly drinking tea in the kitchen...!'
 show miyuki_v002 sinken at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Ah... I see.'
 show miyuki_v002 sinken at inactive
 show nao_v002 normal_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '(When did I come back here...)'
 hide miyuki_v002
 show kazuho_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 normal_close at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Nao-chan... did something happen when you were out?'
 show kazuho_v002 fuan at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...No, it's nothing. I just spaced out, and before I realized it, the sun had set."
 hide kazuho_v002
 show miyuki_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show miyuki_v002 fuan at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "I can't see well since the lights are off... \nWh-what? Whose teacup is that?"
 hide nao_v002
 show kazuho_v002 odoroki at mei_right
 with Dissolve(0.5)
 show miyuki_v002 fuan at inactive
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Did you have a visitor by any chance?'
 hide miyuki_v002
 hide kazuho_v002
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...No, no one came.'
 show nao_v002 normal_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "(Yeah, that's... probably it...)"
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Oh, right, I got this rare tea from Mion-san. Do you two want to try drinking it?'
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I'll brew you some. Please pardon the lack of sweets."
 stop music fadeout 0.5
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide nao_v002
 with Dissolve(0.2)
 stop sound
 show expression 'images/bg/AdvBg_2190.png' as bg
 pause 1.0
 play music "<loop 0>audio/bgm/BGM_QUEST9_COLLAB2.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show beatrice_v001 smile at mei_center
 with Dissolve(0.5)
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "But what a strange girl, looking like she's hosting for a witch. *cackle*cackle*cackle*!"
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") '...If I had left the island, I wonder if I could have met a girl like that.'
 show beatrice_v001 smile_close at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "Hm. It's no use thinking about it too much."
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") '....Nao, you have my thanks. The time we spent together was short, but it was incredibly fun.'
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'The scenery outside the island that I saw through your eyes was quite beautiful...'
 call chapter_end
 
 $ persistent.chara452001_done = True
 return