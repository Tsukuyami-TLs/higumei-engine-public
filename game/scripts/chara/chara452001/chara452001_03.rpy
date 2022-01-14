label chara452001_03:
 show black_background onlayer black
 $ event_store.current_event='chara452001'
 $ event_store.current_progress=2
 $ event_store.current_chapter='chara452001_03'
 $ persistent.menu_return='chara'
 camera:
  anchor (0.5, 0.5)
  pos (960, 540)
 scene
 stop music
 stop sound
 show expression 'images/bg/AdvBg_591.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator 'Several days later...'
 play music "<loop 0>audio/bgm/BGM_HOME_COLLAB2.ogg"
 nao 'Thank you very much--!'
 show nao_v002 smile at mei_center
 with Dissolve(0.5)
 show nao_v002 smile at active
 nao "...I didn't think I would get my hands on that this soon. I need to thank Mion next time I see her."
 show nao_v002 normal at active
 nao 'Now that I have what I wanted to get, the next step is getting in touch with them...'
 show nao_v002 fuan at active
 nao '...How and where did I meet that person?'
 show nao_v002 fuan at active
 nao "I can't remember... I wonder if it's when I was invited over there."
 show nao_v002 fuan_close at active
 nao "...It appears I'll just have to be patient. Well then, back to the house--"
 stop music fadeout 0.5
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_2211.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 show nao_v002 odoroki at active
 nao 'Huh?'
 show nao_v002 odoroki at active
 nao 'This place...! So that means...?'
 hide nao_v002
 with Dissolve(0.2)
 play music "<loop 0>audio/bgm/BGM_EVENT_TOP_COLLAB2.ogg"
 show nao_v002 odoroki at mei_right
 show beatrice_v001 normal at mei_left
 with Dissolve(0.5)
 show beatrice_v001 futeki at active
 show nao_v002 odoroki at inactive
 beatrice "*cackle*cackle*...! It's been a while."
 show nao_v002 smile at active
 show beatrice_v001 futeki at inactive
 nao 'Beatrice...!'
 show beatrice_v001 smile at active
 show nao_v002 smile at inactive
 beatrice 'Have you been well? It seems you desired a meeting and called for me.'
 show beatrice_v001 smile at active
 show nao_v002 smile at inactive
 beatrice 'I had a bit of free time, so I called you here. Mind thanking me? *cackle*cackle*cackle*!'
 show nao_v002 smile at active
 show beatrice_v001 smile at inactive
 nao "Thank you, Beatrice. I didn't know how I could get a hold of you, so this helped."
 show beatrice_v001 fuan at active
 show nao_v002 smile at inactive
 beatrice "Oh, mm... I didn't think you'd be so straightforward about being grateful."
 show beatrice_v001 smile at active
 show nao_v002 smile at inactive
 beatrice "Hm...? What's that bag that you're carrying? Something inside smells nice."
 show nao_v002 smile at active
 show beatrice_v001 smile at inactive
 nao "Ah, you saw...? Here, it's some slightly unusual herbal tea. If you'd like, I thought we could drink it together."
 play audio 'audio/sfx/SE_5037_getup.wav'
 show beatrice_v001 normal at active
 show nao_v002 smile at inactive
 beatrice "Hoh, a souvenir for the witch? Since you said it was a herbal tea, I wonder what kind of plant it's from..."
 show beatrice_v001 smile at jump_transform,active
 show nao_v002 smile at inactive
 beatrice "...Oooh? If it isn't butterfly pea flower tea."
 show nao_v002 smile at active
 show beatrice_v001 smile at inactive
 nao 'I really enjoyed drinking it when I was in a foreign country a long time ago, and thought you would like it too.'
 show nao_v002 smile at active
 show beatrice_v001 smile at inactive
 nao "Since the store in Okinomiya didn't have it, I was able to get it through a friend. So, this is my gift to you."
 show beatrice_v001 smile at active
 show nao_v002 smile at inactive
 beatrice '*cackle*... How thoughtful. But to bring tea for a courtesy visit... you truly are interesting.'
 show nao_v002 fuan at active
 show beatrice_v001 smile at inactive
 nao "It's not like I wanted to do it out of courtesy or anything..."
 show nao_v002 normal at active
 show beatrice_v001 smile at inactive
 nao "By the way, Beatrice, what do you think of the tea? I apologize if I chose something you don't like."
 show beatrice_v001 smile_close at active
 show nao_v002 normal at inactive
 beatrice 'I am the Golden Witch, Beatrice, who has enjoyed all kinds of teas both ancient and modern for one thousand years, black tea becoming my favorite.'
 show beatrice_v001 smile at active
 show nao_v002 normal at inactive
 beatrice 'I welcome all delicious tea, from the name brands to the hidden gems. Naturally, that includes herbal tea as well.'
 show nao_v002 smile at active
 show beatrice_v001 smile at inactive
 nao '*giggle*. Thank goodness. Then try this whenever you feel like it.'
 show beatrice_v001 normal at active
 show nao_v002 smile at inactive
 beatrice "What do you mean? Isn't answering my invitation, giving me a gift, and then leaving tremendously inelegant?"
 show beatrice_v001 smile at active
 show nao_v002 smile at inactive
 beatrice "Since you are here, let's brew this and have a tea party. We can hang out for a short while."
 show nao_v002 smile at active
 show beatrice_v001 smile at inactive
 nao "Thank you. ...In that case, I'll accept your treat. Ah, but where are the teacups...?"
 show beatrice_v001 smile at active
 show nao_v002 smile at inactive
 beatrice '...Hah, preparations are being made now.'
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
 show nao_v002 odoroki at jump_transform,active
 nao 'Wow... a-amazing...! In a single instant, teacups and tea cakes appeared on the table...?!'
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
 beatrice '*cackle*cackle*... This level of magic is simple for me.'
 show beatrice_v001 smile at active
 beatrice "Well, if we're talking about skill in teamaking, I'm not as talented as my furniture, Ronove, but between you and me, it's only right that I be your host."
 show beatrice_v001 normal at active
 beatrice 'Mm-mmm... this tea is as fascinating as ever. When you add lemon, it turns from a vivid blue into a red color. It surely is a magical tea.'
 hide beatrice_v001
 with Dissolve(0.2)
 show beatrice_v001 normal at mei_left
 show nao_v002 normal at mei_right
 with Dissolve(0.5)
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao 'Although, I heard that it is caused by a chemical reaction called a Litmus solution.'
 show beatrice_v001 smile at active
 show nao_v002 normal at inactive
 beatrice 'Chemistry is also a form of magic. The difference is that numbers have replaced the words explaining how it works.'
 show beatrice_v001 fuan_close at active
 show nao_v002 normal at inactive
 beatrice "Nonetheless, eventually that chemistry morphed into an anti-magic toxin... Their roots are the same, but I don't know where the two diverged."
 show nao_v002 normal at active
 show beatrice_v001 fuan_close at inactive
 nao "Now that you mention it, I've heard that magic and science, including chemistry, used to be studied in similar ways."
 show beatrice_v001 normal at nod_transform,active
 show nao_v002 normal at inactive
 beatrice 'I have a deep understanding of this. In fact, a few hundred years ago, alchemy, a branch of study that bridged the gap between magic and science, was something that many intellectuals would devote themselves to acquiring knowledge in.'
 show beatrice_v001 normal_close at active
 show nao_v002 normal at inactive
 beatrice 'However, magic is delicate, and not everyone can use it...'
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice 'They say that science can be easy for anybody to do so long as they have the proper equipment and procedures. Science and magic are polar opposites. Magic loses its power from--'
 show nao_v002 smile at active
 show beatrice_v001 normal at inactive
 nao 'But... magic does exist. At the very least, the Golden Witch, Beatrice, was able to help me.'
 stop music fadeout 0.5
 show beatrice_v001 normal at active
 show nao_v002 smile at inactive
 beatrice '............'
 play music "<loop 0>audio/bgm/BGM_QUEST8_COLLAB2.ogg"
 show beatrice_v001 normal_close at active
 show nao_v002 smile at inactive
 beatrice 'I would like to ask you something.'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide beatrice_v001
 hide nao_v002
 with Dissolve(0.2)
 stop sound
 show expression 'images/card/Card_452001.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 beatrice 'Previously, you said you were on the brink of despair, but you were able to find hope after crossing over to that "World".'
 beatrice "However, as a result of that, you've experienced an even greater level of tragedy... Perhaps at this point, the only way forward is straight into hell."
 beatrice "And even so, you continue to push forward? Wouldn't it have been more peaceful to have snuffed your life out with that initial despair?"
 nao "...No, I have to keep going. After coming this far, I can't quit halfway through."
 nao 'Besides... whichever "different" result that I come upon, by continuing to the end, there is a possibility I can reach one where things went well.'
 nao 'I will not disregard the existence of that "possibility". ...I can\'t ever despair.'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_2211.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 show beatrice_v001 normal at mei_left
 show nao_v002 smile at mei_right
 with Dissolve(0.5)
 show nao_v002 smile at active
 show beatrice_v001 normal at inactive
 nao "And aside from that, I've made friends."
 show beatrice_v001 normal at active
 show nao_v002 smile at inactive
 beatrice 'Friends?'
 show nao_v002 smile_close at nod_transform,active
 show beatrice_v001 normal at inactive
 nao "Yeah. They're older, but since they're a little unreliable, I need to be there for them."
 show nao_v002 smile at active
 show beatrice_v001 normal at inactive
 nao "Because... even they couldn't despair."
 show beatrice_v001 normal at active
 show nao_v002 smile at inactive
 beatrice '............'
 show beatrice_v001 smile_close at active
 show nao_v002 smile at inactive
 beatrice 'I really do still need to thank you, lost child...... no, "Nao Houtani".'
 show nao_v002 odoroki at jump_transform,active
 show beatrice_v001 smile_close at inactive
 nao 'Huh?'
 show beatrice_v001 smile at active
 show nao_v002 odoroki at inactive
 beatrice '*cackle*cackle*... this truly was a pleasantly strange coincidence. I plan to show my face in your village in the future, so I hope you receive me well then.'
 show nao_v002 smile at active
 show beatrice_v001 smile at inactive
 nao "Yes, of course... but wait you're going to Hinamizawa? As a witch? How?"
 show beatrice_v001 smile at active
 show nao_v002 smile at inactive
 beatrice 'That would be through magic, of course... but I do not know if you will remember me or have forgotten about me at that point.'
 show nao_v002 fuan at active
 show beatrice_v001 smile at inactive
 nao "I don't want to forget about you, but I don't think there's anything I can do about it."
 show nao_v002 smile at active
 show beatrice_v001 smile at inactive
 nao 'If it does happen, could we start over with a "Nice to meet you"?'
 show beatrice_v001 normal at active
 show nao_v002 smile at inactive
 beatrice '............'
 show nao_v002 fuan at active
 show beatrice_v001 normal at inactive
 nao 'Ah, it\'s impossible, huh? But in that case, I wonder if there are options other than starting over with "Nice to meet you".'
 show beatrice_v001 smile_close at active
 show nao_v002 fuan at inactive
 beatrice 'No, it\'s not impossible... I get it. When that time comes, let\'s start over with a "Nice to meet you".'
 show beatrice_v001 smile at active
 show nao_v002 fuan at inactive
 beatrice '...Then, until we meet again, Nao Houtani.'
 show nao_v002 odoroki at active
 show beatrice_v001 smile at inactive
 nao 'Yeah... ah, wo-... woah!'
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
 miyuki '...Uh...... Nao. Hey, Nao!'
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
 nao '...Huh?'
 hide nao_v002
 with Dissolve(0.2)
 show nao_v002 fuan at mei_right
 show kazuho_v002 fuan at mei_left
 with Dissolve(0.5)
 show kazuho_v002 fuan at active
 show nao_v002 fuan at inactive
 kazuho 'What is it? Are you okay?'
 show nao_v002 fuan at active
 show kazuho_v002 fuan at inactive
 nao "Miyuki... Kazuho? You're shouting; what happened?"
 show kazuho_v002 sinken at chara_shake_transform,active
 show nao_v002 fuan at inactive
 kazuho "H-Hey... that's my line!"
 hide kazuho_v002
 show miyuki_v002 sinken at mei_left
 with Dissolve(0.5)
 show miyuki_v002 sinken at active
 show nao_v002 fuan at inactive
 miyuki 'When me and Kazuho got back to the living room, we were surprised to see you, who was supposed to be out of the house, absentmindedly drinking tea in the kitchen...!'
 show nao_v002 fuan at active
 show miyuki_v002 sinken at inactive
 nao 'Ah... I see.'
 show nao_v002 normal_close at active
 show miyuki_v002 sinken at inactive
 nao '(When did I come back here...)'
 hide miyuki_v002
 show kazuho_v002 fuan at mei_left
 with Dissolve(0.5)
 show kazuho_v002 fuan at active
 show nao_v002 normal_close at inactive
 kazuho 'Nao-chan... did something happen when you were out?'
 show nao_v002 normal at active
 show kazuho_v002 fuan at inactive
 nao "...No, it's nothing. I just spaced out, and before I realized it, the sun had set."
 hide kazuho_v002
 show miyuki_v002 fuan at mei_left
 with Dissolve(0.5)
 show miyuki_v002 fuan at active
 show nao_v002 normal at inactive
 miyuki "I can't see well since the lights are off... wh-what? Whose teacup is that?"
 hide nao_v002
 show kazuho_v002 odoroki at mei_right
 with Dissolve(0.5)
 show kazuho_v002 odoroki at active
 show miyuki_v002 fuan at inactive
 kazuho 'Did you have a visitor by any chance?'
 hide miyuki_v002
 hide kazuho_v002
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao '...No, no one came.'
 show nao_v002 normal_close at active
 nao "(Yeah, that's... probably it...)"
 show nao_v002 smile at active
 nao 'Oh, right, I got this rare tea from Mion-san. Do you two want to try drinking it?'
 show nao_v002 smile at active
 nao "I'll brew you some. Please pardon the lack of sweets."
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
 beatrice "But what a strange girl, looking like she's hosting for a witch. *cackle*cackle*cackle*!"
 show beatrice_v001 normal at active
 beatrice '...If I had left the island, I wonder if I could have met a girl like that.'
 show beatrice_v001 smile_close at active
 beatrice "Hm. It's no use thinking about it too much."
 show beatrice_v001 smile at active
 beatrice '....Nao, you have my thanks. The time we spent together was short, but it was incredibly fun.'
 show beatrice_v001 smile at active
 beatrice 'The scenery outside the island that I saw through your eyes was quite beautiful...'
 call chapter_end from _call_chapter_end_12
 return