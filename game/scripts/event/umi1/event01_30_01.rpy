label event01_30_01:
 show black_background onlayer black
 $ event_store.current_event='umi1'
 $ event_store.current_progress=2
 $ event_store.current_chapter='event01_30_01'
 $ persistent.menu_return='event'
 camera:
  anchor (0.5, 0.5)
  pos (960, 540)
 scene
 stop music
 stop sound
 show expression 'images/bg/AdvBg_2101.png' as bg
 play music "<loop 0>audio/bgm/BGM_GACHA_COLLAB2.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator 'To get to Rokkenjima, we transferred onto another boat at Niijima.'
 narrator 'Unlike the ferry, it was a smaller, faster boat, so it shook considerably, but that made it thrilling and interesting.'
 narrator 'However......'
 show nao_v002 fuan at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at active
 show nao_v002 fuan at inactive
 mion "What's up, Nao-chan? Do you need to go to the washroom?"
 show nao_v002 fuan_close at active
 show mion_v002 smile at inactive
 nao "It's not that..."
 hide nao_v002
 hide mion_v002
 with Dissolve(0.2)
 narrator "The reason I'm so gloomy is... because of {i}her{/i}."
 show shion_v002 smile at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show shion_v002 smile at inactive
 erika 'Well, it really is just a coincidence. I thought I was going to drown back then.'
 show shion_v002 smile at active
 show erika_v001 normal at inactive
 shion 'What a wonderful coincidence you ended up washing up on an isolated island with a western mansion, though!'
 play audio 'audio/sfx/SE_215_heartgrow.wav'
 show shion_v002 smile_blush at jumping_transform,active
 show erika_v001 normal at inactive
 shion "If a handsome young man living in the mansion fell in love with you at first sight, ugh! At that rate, it'd be just like a romance novel!"
 hide shion_v002
 hide erika_v001
 with Dissolve(0.2)
 narrator "Just... like us... she's coming as a guest invited to stay at Rokkenjima for two nights."
 narrator "We even said we'd never see each other again... \nThis couldn't get any more awkward..."
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika 'Pleased to meet you. My name is Erika Furudo.'
 hide erika_v001
 with Dissolve(0.2)
 narrator 'It seems that she had once drifted near Rokkenjima when she fell out of a pleasure boat.'
 narrator "Then, by coincidence, she washed up on Rokkenjima and was taken care of. Since then, she's had a small connection with them..."
 show nao_v002 normal at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show nao_v002 normal at inactive
 erika 'The twins have already given me their names. Little girl, if would you allow me to hear your name as well, please?'
 show nao_v002 normal at active
 show erika_v001 normal at inactive
 nao '..................'
 show nao_v002 normal_close at active
 show erika_v001 normal at inactive
 nao "I'm... Nao Houtani..."
 show erika_v001 normal at active
 show nao_v002 normal_close at inactive
 erika "My, isn't that a lovely name? Would it be alright if I called you Nao-chan?"
 show nao_v002 normal_close at active
 show erika_v001 normal at inactive
 nao '...Do what you want.'
 play audio 'audio/sfx/SE_530_walk_one.wav'
 hide nao_v002
 with Dissolve(0.6)
 show erika_v001 normal at active
 erika "Oh dear, someone's in a foul mood. *giggle*."
 hide erika_v001
 with Dissolve(0.2)
 show shion_v002 fuan at mei_left
 show mion_v002 fuan at mei_right
 with Dissolve(0.5)
 show mion_v002 fuan at active
 show shion_v002 fuan at inactive
 mion "I wonder what happened. Nao-chan's been upset since a while ago."
 show shion_v002 fuan at active
 show mion_v002 fuan at inactive
 shion "She's not seasick is she? I think it'd be best to leave her alone."
 show shion_v002 smile at active
 show mion_v002 fuan at inactive
 shion 'Anyways, Erika-san! Which Detective Wanyan case is your favorite episode?'
 show mion_v002 smile at active
 show shion_v002 smile at inactive
 mion "A strange turn of fate, isn't it? All of our friends going to the island are Detective Wanyan fans!"
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika 'I suppose I am a fan. Even if it is a work of fiction, I both pity and envy anyone calling themself a detective.'
 show erika_v001 normal_close at active
 erika 'The reasoning in the show is admirable. My only gripe with it is that I could have demonstrated even more brilliant deductions were I the detective.'
 hide erika_v001
 with Dissolve(0.2)
 narrator "The Sonozaki sisters and Erika...san have somehow hit it off. \nI'm the only one left out. ......*sigh*."
 narrator "We haven't even made it to Rokkenjima and I'm already getting the feeling that I shouldn't have come."
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 nao 'Rena-chan... was looking forward to it so much, but she let me go instead, so I have to enjoy myself.'
 show nao_v002 smile at active
 nao 'I need to forget about my troubles and clear my head.'
 hide nao_v002
 with Dissolve(0.2)
 play sound ['audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav'] fadeout 1.0
 stop music fadeout 2.0
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika "It might be a bit difficult since the boat is rocking back and forth, but can you see it? That's Rokkenjima over there."
 hide erika_v001
 with Dissolve(0.2)
 show shion_v002 smile at mei_left
 show mion_v002 odoroki at mei_right
 with Dissolve(0.5)
 show mion_v002 odoroki at jump_transform,active
 show shion_v002 smile at inactive
 mion "Ah! There?! Wow! It's really an island!!"
 show shion_v002 fuan at active
 show mion_v002 odoroki at inactive
 shion "...Sis, please calm down. Everyone's going to think you're a country bumpkin seeing the ocean for the first time."
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika 'Now, I have a question... Why do you think the island is called Rokkenjima (Six House Island)?'
 hide erika_v001
 with Dissolve(0.2)
 narrator "...If it's just because there were six houses on the island a long time ago , then it'd be too easy."
 narrator "But it's also the exact answer that comes out of Mion-san's mouth."
 play music "<loop 0>audio/bgm/BGM_QUEST4_COLLAB2.ogg"
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika "That's half right. The name comes from the fact that even in its most prosperous times, there were no more than six houses on the island."
 hide erika_v001
 with Dissolve(0.2)
 show mion_v002 fuan at mei_right
 show shion_v002 odoroki at mei_left
 with Dissolve(0.5)
 show shion_v002 odoroki at active
 show mion_v002 fuan at inactive
 shion 'No more than six houses?'
 show mion_v002 fuan at active
 show shion_v002 odoroki at inactive
 mion "Don't tell me the island's cursed..."
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika 'The seas near Rokkenjima have many reefs, and the currents are complicated, so there used to be many accidents.'
 show erika_v001 normal at active
 erika 'As a result, fishermen avoided getting close to the island, and it became known as a cursed island.'
 show erika_v001 normal_close at active
 erika "Brave people who didn't believe in those superstitions tried to settle on the island many times but..."
 show erika_v001 normal_close at active
 erika 'Mysterious disappearances, strange diseases of unknown origin. The people who moved there were wiped out every time...'
 show erika_v001 normal at active
 erika "No matter how many people moved to the island, before they'd built more than six houses, they would all be wiped out. And because of that, it was called Rokkenjima."
 hide erika_v001
 with Dissolve(0.2)
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 nao "...What the heck... that's scary..."
 stop music
 play sound ['audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav'] fadeout 1.0
 hide nao_v002
 with Dissolve(0.2)
 show shion_v002 smile at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_311_ls_cutejump.wav'
 show mion_v002 smile at jump_transform,active
 show shion_v002 smile at inactive
 mion "Whoa, that's super mysterious! This ol' man's fired up! It's just like an episode of Detective Wanyan!"
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion "An isolated island with a mysterious Western mansion... I think it'd be popular if you put it that way."
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion "We're not just reviewers this time, we're resort consultants too!"
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 narrator "...The Sonozaki sisters really are unfazed. \nMaybe it's not a big deal when you're constantly living under Oyashiro-sama's curse."
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika 'Although, that story was something I just made up.'
 show erika_v001 normal at active
 erika '...The truth is that the island used to be called Akujikishima (Evil Appetite Island) because the souls of anyone who came near would be eaten by evil spirits.'
 hide erika_v001
 with Dissolve(0.2)
 narrator '"You sure know your stuff.", interjected the captain.'
 Character('Captain',ctc="ctcArrow", ctc_position="fixed") "Though, rumor has it, there's a witch living there now instead of the evil spirits..."
 show erika_v001 normal at mei_right
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at active
 show erika_v001 normal at inactive
 nao '.........A witch...?'
 show erika_v001 normal at active
 show nao_v002 fuan at inactive
 erika '*giggle*...'
 show nao_v002 sinken at active
 show erika_v001 normal at inactive
 nao "I don't really care what's living on the island. ...Ghosts or spirits, I don't believe in any of that."
 show erika_v001 normal at active
 show nao_v002 sinken at inactive
 erika 'Oh?'
 show nao_v002 sinken at active
 show erika_v001 normal at inactive
 nao 'What is it...'
 show erika_v001 normal_close at active
 show nao_v002 sinken at inactive
 erika "Don't you think you should be more careful about your attitude towards Rokkenjima?"
 show erika_v001 normal_close at active
 show nao_v002 sinken at inactive
 erika 'It is said that the true master of the island does not tolerate those who do not believe in witches.'
 hide erika_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator '......I only came to enjoy embroidery in that beautiful rose garden, though.'
 narrator 'The Sonozaki sisters, excited by the talk of the witch, seemed to be in high spirits even before reaching the island.'
 narrator "It's not like I'm afraid but...\nI'm not particularly fond of taking a vacation on an island of witches and evil spirits. "
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_2251.png' as bg
 play music "<loop 0>audio/bgm/BGM_HOME_COLLAB2.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show shannon_v001 smile at mei_right
 show jessica_v001 smile at mei_left
 with Dissolve(0.5)
 show jessica_v001 smile at active
 show shannon_v001 smile at inactive
 jessica 'Welcome to Rokkenjima, everyone!'
 show shannon_v001 smile at active
 show jessica_v001 smile at inactive
 shannon 'You must all be exhausted from the long boat ride.'
 hide shannon_v001
 hide jessica_v001
 with Dissolve(0.2)
 narrator "The Ushiromiya family's daughter and servants had gone out of their way to wait for us at the dock."
 narrator 'I feel sorry for disparaging the island with talk of witches and evil spirits just before being welcomed onto it.'
 Character('Gohda',ctc="ctcArrow", ctc_position="fixed") 'Now then, allow me to take care of your luggage.'
 show shion_v002 smile at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at active
 show shion_v002 smile at inactive
 mion "No, no, it's fine! My luggage is really heavy!"
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion "I think I'll let you take care of mine then. Pleased to meet you!"
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 Character('Gohda',ctc="ctcArrow", ctc_position="fixed") 'Yes. Leave it to me. ...nnn ...guh...'
 play audio 'audio/sfx/SE_5005_grab.wav'
 camera at screenshake_transform
 pause 0.0
 pause 1.0
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 nao "...I've been thinking you two had trunks way too heavy just for a two night stay."
 hide nao_v002
 with Dissolve(0.2)
 show shion_v002 smile at mei_left
 show mion_v002 futeki at mei_right
 with Dissolve(0.5)
 show mion_v002 futeki at updown_shake_transform,active
 show shion_v002 smile at inactive
 mion 'Heheh. A maiden must be suitably prepared when staying elsewhere.'
 show shion_v002 smile at active
 show mion_v002 futeki at inactive
 shion 'One should be thoroughly prepared for this island.'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 stop sound
 show expression 'images/bg/AdvBg_2261.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator 'Here, there are no restrictions like tour bus times or group activities. \nEveryone can enjoy things at their own leisurely pace.'
 narrator 'I only brought a change of clothes, toiletries, a book to read, and an embroidery set, so a cutely sized trunk was enough.'
 show shannon_v001 smile at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show shannon_v001 smile at inactive
 erika "I don't have any luggage for you to carry."
 show shannon_v001 smile_close at active
 show erika_v001 normal at inactive
 shannon 'Do excuse me. I will now take everyone to the guesthouse where you will be staying.'
 hide shannon_v001
 hide erika_v001
 with Dissolve(0.2)
 narrator 'The only thing Erika-san was carrying was a lolita-style backpack.'
 narrator "It's like she's just casually staying over at a friend's house."
 show erika_v001 normal at mei_left
 show jessica_v001 smile at mei_right
 with Dissolve(0.5)
 show jessica_v001 smile at active
 show erika_v001 normal at inactive
 jessica 'Erika-san! Long time no see! Those clothes really do suit you amazingly.'
 show erika_v001 normal at active
 show jessica_v001 smile at inactive
 erika 'Thank you very much. I like them a lot as well.'
 show erika_v001 normal at active
 show jessica_v001 smile at inactive
 erika 'Last time, I was an uninvited guest who had drifted ashore, so I am greatly honored to be welcomed to the front door this time.'
 show jessica_v001 smile at active
 show erika_v001 normal at inactive
 jessica "Nice to meet you. Um, Nao-san, that's you, right?"
 hide erika_v001
 show nao_v002 smile at mei_left
 with Dissolve(0.5)
 show nao_v002 smile at active
 show jessica_v001 smile at inactive
 nao "That's right. ...So you could figure that out."
 hide jessica_v001
 hide nao_v002
 with Dissolve(0.2)
 show erika_v001 normal_close at mei_center
 with Dissolve(0.5)
 show erika_v001 normal_close at active
 erika "It's a simple process of elimination. She and I are acquainted, and two of the three left are twins. The only one left would be Nao-chama, so you'd know who that is."
 hide erika_v001
 with Dissolve(0.2)
 narrator "Just as I thought, there {i}is{/i} some sharpness to her words. I just can't come to like this person, and I sense she doesn't like me either."
 show jessica_v001 smile at mei_right
 show mion_v002 smile at mei_left
 with Dissolve(0.5)
 show mion_v002 smile at active
 show jessica_v001 smile at inactive
 mion "Wow! An entire island as your home! Man, Jessica-san, I'm so jealous of you!"
 show jessica_v001 fuan_close at active
 show mion_v002 smile at inactive
 jessica "It's not great at all. Personally, I wish I could walk to all my friends' houses."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide jessica_v001
 hide mion_v002
 hide fade onlayer curtain
 show shion_v002 smile at mei_center
 with Dissolve(0.08333333333333333)
 show shion_v002 smile at updown_shake_transform,active
 shion "Sis! Nao-san! Quickly, quickly! Isn't this amazing?!?!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide shion_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 narrator 'Shion-san, who was free from her luggage, reached the top of the long flight of stairs ahead of the rest of us.'
 narrator 'And so, as the scene spread out before me, I became so overcome with emotion that I almost lost myself...'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_2221.png' as bg
 play music "<loop 0>audio/bgm/BGM_GACHA_COLLAB2.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 camera:
  parallel:
   linear 0.5 pos (810, 460)
  parallel:
   linear 0.5 zoom 1.5
 pause 0.5
 pause 1.0
 camera:
  parallel:
   linear 1.0 pos (960, 460)
  parallel:
   linear 1.0 zoom 1.5
 pause 1.0
 pause 1.0
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 show nao_v002 smile_blush at mei_center
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_215_heartgrow.wav'
 show nao_v002 smile_blush at jumping_transform,active
 nao 'W-... Woaaah.........!'
 hide nao_v002
 with Dissolve(0.2)
 narrator "The spectacular view truly had me speechless. \n...Aah, and to think I'd been so worried about not being able to have fun because of the incident on the ferry."
 show shion_v002 smile at mei_left
 show mion_v002 odoroki at mei_right
 with Dissolve(0.5)
 show mion_v002 odoroki at active
 show shion_v002 smile at inactive
 mion 'Th-... this is fantastic...'
 show shion_v002 smile at active
 show mion_v002 odoroki at inactive
 shion "St. Lucia also had a rose garden but... it's nothing compared to this."
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 narrator 'This is what I came for. \nA beautiful rose garden out of this world.'
 narrator '"If I could choose where I die... then I would want to be surrounded by these beautiful roses, and fall asleep as if I were taking a nap." \nIt was the type of scene that made you think something like that...'
 show jessica_v001 smile at mei_left
 show shannon_v001 smile at mei_right
 with Dissolve(0.5)
 show shannon_v001 smile at active
 show jessica_v001 smile at inactive
 shannon 'Thank you very much for the words of praise.'
 show jessica_v001 smile at active
 show shannon_v001 smile at inactive
 jessica "Heheh. Thanks to Kanon-kun's handiwork, we've had the best roses ever this year!"
 hide jessica_v001
 show erika_v001 normal at mei_left
 with Dissolve(0.5)
 show erika_v001 normal at active
 show shannon_v001 smile at inactive
 erika 'I would like to express my gratitude to Kanon-san directly. Is there any way you could call him?'
 show shannon_v001 smile_close at active
 show erika_v001 normal at inactive
 shannon 'Your words are too kind. I will pass your message on to him.'
 hide shannon_v001
 hide erika_v001
 with Dissolve(0.2)
 show shion_v002 smile at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show shion_v002 smile at inactive
 nao "Such a beautiful rose garden, and no one outside the household is allowed to see it. I can't believe it..."
 show shion_v002 smile at active
 show nao_v002 normal at inactive
 shion "Absolutely. In a way, it's an affront to the roses..."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide shion_v002
 hide nao_v002
 hide fade onlayer curtain
 show mion_v002 smile at mei_center
 with Dissolve(0.08333333333333333)
 show mion_v002 smile at jump_transform,active
 mion "Shion~!! Over here!  Wouldn't it be pretty good if I took a picture from this angle?!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide mion_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika "The Ushiromiya family doesn't get guests like her much. I'm sure Beato won't be bored."
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide erika_v001
 with Dissolve(0.2)
 stop sound
 show expression 'images/bg/AdvBg_2271.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 show jessica_v001 smile at mei_left
 show shannon_v001 smile at mei_right
 with Dissolve(0.5)
 show shannon_v001 smile at active
 show jessica_v001 smile at inactive
 shannon 'And this way is the guesthouse everyone will be staying at.'
 show jessica_v001 smile at active
 show shannon_v001 smile at inactive
 jessica 'Think of it as your own home! The rooms are on the second floor, by the way.'
 play audio 'audio/sfx/SE_510_sand_foot.wav'
 show shannon_v001 smile at active
 show jessica_v001 smile at inactive
 shannon 'Watch your step. Please come this way.'
 hide jessica_v001
 hide shannon_v001
 with Dissolve(0.2)
 show shion_v002 smile at mei_left
 show mion_v002 fuan at mei_right
 with Dissolve(0.5)
 show mion_v002 fuan at active
 show shion_v002 smile at inactive
 mion "...I sure wish they'd renovate the Sonozaki main house into a Western mansion like this."
 show shion_v002 fuan at active
 show mion_v002 fuan at inactive
 shion "Do you think the old hag would be fine with that? I can't even see Mother letting that happen. "
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 show nao_v002 normal at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_5020_key.wav'
 show erika_v001 normal at active
 show nao_v002 normal at inactive
 erika "Here, Nao-chama. It looks like that's your room key."
 show nao_v002 normal at active
 show erika_v001 normal at inactive
 nao '...Please stop calling me "chama", thank you very much.'
 show nao_v002 odoroki at active
 show erika_v001 normal at inactive
 nao 'Is there only one key?'
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 narrator 'Normally, there are as many keys as guests staying in the room, but...'
 show nao_v002 normal at mei_left
 show erika_v001 normal_close at mei_right
 with Dissolve(0.5)
 show erika_v001 normal_close at active
 show nao_v002 normal at inactive
 erika "What a cheap plot. Well, whatever, it'll be nice to have fewer keys so the story won't end up so complicated."
 show nao_v002 fuan at active
 show erika_v001 normal_close at inactive
 nao '...If we end up losing the only key......'
 show erika_v001 normal at active
 show nao_v002 fuan at inactive
 erika "Don't worry. Please kindly tell one of the servants if that happens. They have master keys."
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 narrator "In any case, it's an important key. I'd better leave it in the hands of my seniors. I'll give it to Mion-san."
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 show black_cover as bg
 play audio 'audio/sfx/SE_5013_down.wav'
 narrator 'We went up to the second floor, entered our rooms, and set down our bags.'
 stop sound
 show expression 'images/bg/AdvBg_2281.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator "Our room is a three-person room with three beds. \nErika-san's room next to ours is the same, although she's the only one using it."
 show shion_v002 smile at mei_right
 show nao_v002 smile at mei_left
 with Dissolve(0.5)
 show nao_v002 smile at active
 show shion_v002 smile at inactive
 nao "...This is a nice room, isn't it?"
 show shion_v002 smile at active
 show nao_v002 smile at inactive
 shion "You can visit these types of buildings, but it's not often you get to stay in one."
 hide shion_v002
 hide nao_v002
 with Dissolve(0.2)
 narrator 'More than luxurious, the room was calm, and had a sense of refined, quiet beauty.'
 narrator 'It was built right after the war, so some of the facilities are clearly aging, but that gives it an antique taste.'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show mion_v002 smile at mei_center
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_592_Is_plastic.wav'
 show mion_v002 smile at updown_shake_transform,active
 mion 'Yahoo!! Hoho! These bed springs are the best!'
 play audio 'audio/sfx/SE_526_door_open.wav'
 show mion_v002 smile at jump_transform,active
 mion "I wonder what the view from the window is like! Ohh, you can feel the sea breeze!! Look, look, Shion!! It's an ocean vieeeewwww!!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide mion_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show nao_v002 fuan at mei_left
 show shion_v002 fuan at mei_right
 with Dissolve(0.5)
 show shion_v002 fuan at active
 show nao_v002 fuan at inactive
 shion "...Sis. You're not an elementary school student on a school trip."
 show nao_v002 fuan at active
 show shion_v002 fuan at inactive
 nao 'Mion-san, please close the window for now. Strong winds will bring in dust.'
 hide nao_v002
 hide shion_v002
 with Dissolve(0.2)
 show mion_v002 fuan at mei_center
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_5056_toy.wav'
 show mion_v002 fuan at active
 mion 'Aah, sorry, sorry. I got excited! ...Huh? ...Uh oh...'
 hide mion_v002
 with Dissolve(0.2)
 show nao_v002 odoroki at mei_left
 show shion_v002 odoroki at mei_right
 with Dissolve(0.5)
 show shion_v002 odoroki at active
 show nao_v002 odoroki at inactive
 shion 'What is it? ...Eeee-, Sis, did you break iiit?!'
 show nao_v002 odoroki at active
 show shion_v002 odoroki at inactive
 nao '...Uh. When you opened the window in excitement just now... did you break the lock?'
 hide nao_v002
 hide shion_v002
 with Dissolve(0.2)
 show mion_v002 fuan at mei_center
 with Dissolve(0.5)
 show mion_v002 fuan at chara_shake_transform,active
 mion "I-It's not broken! There's just a trick to closing it, isn't there? ......Hmm, let's see..."
 hide mion_v002
 with Dissolve(0.2)
 narrator "That's Mion-san for you. I can't believe she broke the window's lock almost immediately after entering the room, let alone on the first day."
 narrator "Well, the window closes on its own. Since we're on the second floor, I'm not that worried about being unable to lock it."
 show mion_v002 fuan at mei_right
 show shion_v002 fuan_close at mei_left
 with Dissolve(0.5)
 show shion_v002 fuan_close at active
 show mion_v002 fuan at inactive
 shion 'Jeez, Sis... you really make me worry about you.'
 show mion_v002 smile at active
 show shion_v002 fuan_close at inactive
 mion 'Well... anyways, moving on! Ahh, what a nice room!'
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 narrator 'Skillfully avoiding the subject. ...As expected of Mion-san.'
 show nao_v002 normal at mei_left
 show mion_v002 fuan at mei_right
 with Dissolve(0.5)
 show mion_v002 fuan at active
 show nao_v002 normal at inactive
 mion 'Man, if we had gotten two rooms, we could have invited Kei-chan.'
 show nao_v002 fuan at active
 show mion_v002 fuan at inactive
 nao "Aah... it wouldn't be good for a girl to stay in a room with a boy before she gets married after all."
 hide nao_v002
 hide mion_v002
 with Dissolve(0.2)
 show shion_v002 fuan at mei_center
 with Dissolve(0.5)
 show shion_v002 fuan at active
 shion 'Sis, you really are an idiot. If you just told him that there were two rooms and called him over,'
 show shion_v002 smile at active
 shion "and it turned out there was only one room when we arrived, he'd have no choice but to stay in the same room! Wouldn't that have been nice?"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide shion_v002
 hide fade onlayer curtain
 show mion_v002 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show mion_v002 odoroki at active
 mion "Aaaaaaaaaargghhh!! I should've done that!! "
 show mion_v002 fuan at active
 mion 'Shion! Go back right now and switch with Kei-chan!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide mion_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show nao_v002 fuan at mei_left
 show shion_v002 smile at mei_right
 with Dissolve(0.5)
 show shion_v002 smile at active
 show nao_v002 fuan at inactive
 shion 'I never knew you had that little self respect, Sis.'
 show nao_v002 fuan_close at active
 show shion_v002 smile at inactive
 nao "I-If you did that and he turned it down, I wouldn't know how to respond..."
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide nao_v002
 hide shion_v002
 with Dissolve(0.2)
 stop sound
 show expression 'images/bg/AdvBg_2371.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_5007_keyroll.wav'
 narrator 'We left our bags and locked the room.'
 narrator 'Erika-san had also just come out and locked her room.'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_2291.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_5049_cup.wav'
 narrator 'When we went downstairs, Gohda-san was setting out some drinks to welcome us.'
 Character('Gohda',ctc="ctcArrow", ctc_position="fixed") 'Welcome, everyone. Please enjoy these beverages.'
 Character('Gohda',ctc="ctcArrow", ctc_position="fixed") 'I would like to present the refreshing taste of the end of autumn, to you who have travelled so far to arrive here...'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show mion_v002 smile at mei_center
 with Dissolve(0.08333333333333333)
 show mion_v002 smile at chara_shake_transform,active
 mion "Hwaa~!! This is great! I'd like a refill!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide mion_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_333_ls_ppuringtea.wav'
 Character('Gohda',ctc="ctcArrow", ctc_position="fixed") 'Of course, here you are... Speaking of the fruits of autumn--'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show mion_v002 smile at mei_center
 with Dissolve(0.08333333333333333)
 show mion_v002 smile at chara_shake_transform,active
 mion 'Hwaa~!! This really is the stuff! I can drink it all in one gulp!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide mion_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show shion_v002 fuan at mei_left
 show erika_v001 normal_close at mei_right
 with Dissolve(0.5)
 show erika_v001 normal_close at active
 show shion_v002 fuan at inactive
 erika '...Could you at least wait until Gohda-san has finished with his explanation?'
 show shion_v002 fuan at active
 show erika_v001 normal_close at inactive
 shion 'Oh well. Sis is a country bumpkin with no table manners after all.'
 show erika_v001 normal at active
 show shion_v002 fuan at inactive
 erika 'Oh? It seems like Nao-chama has no problem waiting patiently.'
 show erika_v001 normal at active
 show shion_v002 fuan at inactive
 erika '......You. Do you happen to be from a good family?'
 hide shion_v002
 show nao_v002 normal_close at mei_left
 with Dissolve(0.5)
 show nao_v002 normal_close at active
 show erika_v001 normal at inactive
 nao "I'm not. You're just imagining things."
 show erika_v001 normal at active
 show nao_v002 normal_close at inactive
 erika 'Hmm, I see...'
 hide erika_v001
 hide nao_v002
 with Dissolve(0.2)
 show shannon_v001 smile at mei_center
 with Dissolve(0.5)
 show shannon_v001 smile at active
 shannon 'Everyone, I would like to show you the mansion.'
 hide shannon_v001
 with Dissolve(0.2)
 narrator 'After the refreshments and a little break, Jessica-san arrived to come get us.'
 narrator "First, we'll go greet the family members that will be taking care of us these next few days. Then after that, we'll be shown around the Western-style mansion built right after the war."
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_2221.png' as bg
 play music "<loop 0>audio/bgm/BGM_HOME_COLLAB2.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show jessica_v001 smile at mei_right
 show nao_v002 smile at mei_left
 with Dissolve(0.5)
 show nao_v002 smile at active
 show jessica_v001 smile at inactive
 nao '...Jessica-san, have you always been living on this island?'
 show jessica_v001 smile at active
 show nao_v002 smile at inactive
 jessica "Pretty much. I didn't mind at first because that's how it's been since I was born but..."
 show jessica_v001 fuan at active
 show nao_v002 smile at inactive
 jessica "It's really lonely. There's no one on the island but my family, so it gets boring."
 hide nao_v002
 show shannon_v001 smile at mei_left
 with Dissolve(0.5)
 show shannon_v001 smile at active
 show jessica_v001 fuan at inactive
 shannon '*giggle*. Milady Jessica has been looking forward to everyone coming here today.'
 show jessica_v001 smile at jump_transform,active
 show shannon_v001 smile at inactive
 jessica "It's like having some new friends over, so I'm really happy!"
 show jessica_v001 smile at active
 show shannon_v001 smile at inactive
 jessica "Ask me anything you'd like to know about this island! Or even if you just want someone to talk to, or play a game with! Just give me a shout!"
 hide jessica_v001
 hide shannon_v001
 with Dissolve(0.2)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika 'Spending only a few days here is wonderful, but anyone would get lonely if they lived their whole life on this island.'
 hide erika_v001
 with Dissolve(0.2)
 show shion_v002 smile at mei_right
 show mion_v002 smile at mei_left
 with Dissolve(0.5)
 show mion_v002 smile at active
 show shion_v002 smile at inactive
 mion "Just leave that kind of thing to this ol' man! Especially when it comes to games!"
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion 'In these few days, you will experience trauma you will never forget for the rest of your life.'
 hide mion_v002
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at active
 show shion_v002 smile at inactive
 nao "...Mion-san's club activity punishment games sure are brutal."
 hide shion_v002
 show erika_v001 normal_close at mei_right
 with Dissolve(0.5)
 show erika_v001 normal_close at active
 show nao_v002 fuan at inactive
 erika 'Even without punishment games, it will definitely be an unforgettably traumatic experience.'
 show erika_v001 normal at active
 show nao_v002 fuan at inactive
 erika "Because, this is the witch's island..."
 show nao_v002 normal at active
 show erika_v001 normal at inactive
 nao '...Witch......?'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 stop sound
 show expression 'images/bg/AdvBg_2301.png' as bg
 play music "<loop 0>audio/bgm/BGM_QUEST2_COLLAB2.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator 'The masters of the house, Krauss Ushiromiya-san and Natsuhi-san, came to greet us.'
 narrator 'Krauss-san was a wealthy looking, well-dressed gentleman. \nHis wife Natsuhi-san was an impeccable lady, reminiscent of the aristocracy of the Meiji and Taisho periods.'
 show mion_v002 smile at mei_center
 with Dissolve(0.5)
 show mion_v002 smile at active
 mion 'What an amazing mansion... To build a house like this in one generation, I really admire that!'
 hide mion_v002
 with Dissolve(0.2)
 Character('Krauss Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Hahaha. It was my father who built this mansion.'
 Character('Krauss Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Normally, we'd expect my father to come and greet you, but he has been busy with some advanced research. Please forgive our rudeness."
 show shion_v002 smile at mei_center
 with Dissolve(0.5)
 show shion_v002 smile at active
 shion "We'll do our best to give a young person's point of view as resort consultants! Please leave it to us!"
 hide shion_v002
 with Dissolve(0.2)
 Character('Natsuhi Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "You don't have to be so formal about it. Please take your time and enjoy your stay at this house."
 show nao_v002 smile at mei_left
 with Dissolve(0.5)
 show nao_v002 smile at active
 nao "...It's a lovely house. ...I wonder if it's the work of {note_green}Josiah Conder{/note_green}."
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show nao_v002 smile at inactive
 erika 'This house was built after the war, remember? Conder died in 1920.'
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 show jessica_v001 smile at mei_center
 with Dissolve(0.5)
 show jessica_v001 smile at active
 jessica 'Uh, apparently it was designed by the apprentice of some great architect named Conder.'
 hide jessica_v001
 with Dissolve(0.2)
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at active
 mion "Man, I'd love to build a mansion from scratch! I could fill it with secret rooms and hidden doors!"
 show erika_v001 normal at mei_left
 with Dissolve(0.5)
 show erika_v001 normal at active
 show mion_v002 smile at inactive
 erika "That's right. You could even build a secret room for your mistress to live in."
 hide mion_v002
 show shion_v002 smile at mei_right
 with Dissolve(0.5)
 show shion_v002 smile at active
 show erika_v001 normal at inactive
 shion "It might be inappropriate to say this about someone's home, but if you just close your eyes, all sorts of mysteries and suspenseful things come to mind."
 hide erika_v001
 show nao_v002 smile at mei_left
 with Dissolve(0.5)
 show nao_v002 smile at active
 show shion_v002 smile at inactive
 nao "That's certainly... quite inappropriate."
 hide shion_v002
 hide nao_v002
 with Dissolve(0.2)
 Character('Natsuhi Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Jessica, Shannon. I'll leave the guests to you two. ...Jessica, do not forget your manners."
 show jessica_v001 fuan_close at mei_center
 with Dissolve(0.5)
 show jessica_v001 fuan_close at active
 jessica 'I-I know...'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide jessica_v001
 with Dissolve(0.2)
 stop sound
 show expression 'images/bg/AdvBg_2161.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator 'With that, we were shown around the house.'
 narrator 'We were nervous at first, but around the end, the Sonozaki sisters were totally relaxed. They started getting excited and talking about how great it would be if some kind of incident occurred here, among other indiscreet topics.  '
 narrator 'Then, on the way back to the front door, we walked through a great hall.'
 narrator 'And there... I met the true master of this island.'
 show mion_v002 odoroki at mei_right
 show shion_v002 odoroki at mei_left
 with Dissolve(0.5)
 show shion_v002 odoroki at active
 show mion_v002 odoroki at inactive
 shion '...Woah, what beautiful blonde hair...'
 show mion_v002 odoroki at active
 show shion_v002 odoroki at inactive
 mion 'Who is... this person...'
 stop music fadeout 2.0
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 play sound ['audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav'] fadeout 1.0
 stop sound
 show expression 'images/bg/AdvBg_2311.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 camera:
  parallel:
   linear 1.0 pos (960, 540)
  parallel:
   linear 1.0 zoom 1.3
 pause 1.0
 pause 1.0
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao '........................'
 hide nao_v002
 with Dissolve(0.2)
 narrator "I'm not psychic or anything. \n...But, the painting was making me feel something."
 narrator 'It was... a feeling of deep love for the woman in the painting... bordering on or even exceeding... that of madness.'
 narrator "It should only be a beautiful portrait... but that's how it made me feel. \nI wonder if I've also... been poisoned by the cliche of mysteries on isolated islands."
 show jessica_v001 normal at mei_right
 with Dissolve(0.5)
 show jessica_v001 normal at active
 jessica "It's a portrait of our family alchemist."
 $ event_store.current_progress = 3
 show jessica_v001 normal at active
 jessica 'According to Grandfather, the Ushiromiya family would not have prospered if she had not lent him {note_green}100 tons{/note_green} of gold.'
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show jessica_v001 normal at inactive
 nao 'Alchemy... like in the occult?'
 show jessica_v001 smile at active
 show nao_v002 normal at inactive
 jessica 'Well, if she can produce 100 tons of gold with a poof, then I suppose you could call her an alchemist.'
 hide jessica_v001
 hide nao_v002
 with Dissolve(0.2)
 show shion_v002 smile at mei_left
 show mion_v002 normal at mei_right
 with Dissolve(0.5)
 show mion_v002 normal at active
 show shion_v002 smile at inactive
 mion "So, in other words, it's a portrait of the Ushiromiya family's great benefactor...?"
 show shion_v002 smile at active
 show mion_v002 normal at inactive
 shion "Judging by the aura, it doesn't seem like she's from Japan."
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 show shannon_v001 smile at mei_center
 with Dissolve(0.5)
 show shannon_v001 smile at active
 shannon 'This is a portrait of the Ushiromiya family alchemist, Beatrice-sama.'
 hide shannon_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_left
 show erika_v001 normal_close at mei_right
 with Dissolve(0.5)
 show erika_v001 normal_close at active
 show nao_v002 normal at inactive
 erika '...Also known as the Golden Witch, Beatrice.'
 show nao_v002 normal at active
 show erika_v001 normal_close at inactive
 nao 'The Golden... Witch...'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 show black_cover as bg
 narrator 'That was the first meeting between me and the witch.'
 narrator 'However, this first meeting was preferable to what came next.\nBecause she was still in the portrait......'
 window hide None
 pause 2.0
 play audio 'audio/sfx/SE_324_ls_thundercroud.wav'
 pause 1.0
 play audio 'audio/sfx/SE_325_ls_thunderfall.wav'
 beatrice '"{b}*cackle*cackle* Welcome to my Rokkenjima! Enjoy your stay, Humans...!!{/b}"'
 call chapter_end from _call_chapter_end_3
 jump event01_30_02