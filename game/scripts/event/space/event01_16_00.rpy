label event01_16_00:
 show black_background onlayer black
 $ event_store.current_event='space'
 $ event_store.current_progress=0
 $ event_store.current_chapter='event01_16_00'
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
 show expression 'images/bg/AdvBg_220.png' as bg
 play music "<loop 6.86>audio/bgm/BGM_OYASHIRO.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 Character('????',ctc="ctcArrow", ctc_position="fixed") '...Dreams.\nI believe that everyone has had the chance to experience all sorts of dreams up until this point.'
 Character('????',ctc="ctcArrow", ctc_position="fixed") 'For example, a happy dream where you spend time with a friend.\nOr an unusual dream where manga and anime characters appear...'
 Character('????',ctc="ctcArrow", ctc_position="fixed") 'Or perhaps... a sad one where you cry and scream — what we call "Nightmares".'
 Character('????',ctc="ctcArrow", ctc_position="fixed") 'Once you wake up, however, it all ends. The riches and objects you obtained, your friends, your memories... it all becomes "naught".'
 Character('????',ctc="ctcArrow", ctc_position="fixed") "You can feel disappointed that it's over, or you can assure to yourself that it was all just a dream. And then afterwards, it dissipates from your memory, and you return to reality..."
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_221.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 show hanyuu_v009 normal at mei_center
 with Dissolve(0.5)
 show hanyuu_v009 normal at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'But... to everyone listening;\nAre you really okay with pretending the events within your dreams mean "nothing", and allowing yourself to forget them?'
 show hanyuu_v009 normal at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Perhaps the "World" you saw in your dream was another reality that you could have sworn you lived through...?'
 show hanyuu_v009 smile at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Our story this time will go down in history as one such marvellous experience―'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide hanyuu_v009
 with Dissolve(0.2)
 stop music fadeout 0.5
 pause 2.0
 narrator '...It just happened that day.\nI woke up feeling a little listless. As I opened my eyes, I fully took in the scene in front of me...'
 stop sound
 show expression 'images/bg/AdvBg_1390.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 play music "<loop 2.36>audio/bgm/BGM_EVENT1.ogg"
 show kazuho_v002 odoroki at mei_center
 with Dissolve(0.5)
 camera:
  parallel:
   linear 0.5 pos (960, 510)
  parallel:
   linear 0.5 zoom 1.3
 show kazuho_v002 odoroki at active
 show kazuho_v002 odoroki at jumping_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Wh-...wha-...?!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide kazuho_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 narrator 'I yelled out reflexively and sprang up with a jolt... I was astonished at the scene before me.'
 show kazuho_v002 odoroki at mei_center
 with Dissolve(0.5)
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Wh-...what is this...?!'
 hide kazuho_v002
 with Dissolve(0.2)
 narrator 'I look at my surroundings and fall into a panic.'
 narrator 'Metallic walls and windows tower over me in every direction.\nThe room was illuminated by a cold light, and mysterious electronic noises were coming from who knows where.'
 narrator 'The framework looks like it came straight out of a sci-fi movie.\nAt the very least, I\'ve never seen such a "futuristic" interior of something in the real world. But—'
 show kazuho_v002 odoroki at mei_center
 with Dissolve(0.5)
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'A-...ahh...?'
 show kazuho_v002 odoroki at jumping_transform
 hide kazuho_v002
 with Dissolve(0.2)
 narrator 'Out from a giant window, I was able to see a vast black void spreading on forever, as well as... the face of a blue and white-colored spherical object.'
 narrator 'It was truly my first time seeing this sight with my own two eyes... although {i}that{/i} sort of scene was often featured on TV and all kinds of media.'
 show kazuho_v002 odoroki at mei_center
 with Dissolve(0.5)
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "Is that... the Earth?\nSo that means... I'm in space...?!"
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide kazuho_v002
 with Dissolve(0.2)
 narrator "...I don't understand at all.\nI have no idea how I'm here in space, or for what reason."
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "(A-...at any rate, let's see if I can remember what I did before going to bed...)"
 narrator 'I sift through my memory as hard as my head can manage.'
 narrator 'I went to sleep in my bed... no, wrong. I was feeling the tender grass on my back while gazing up at the stars, then I dozed off... and...'
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "(Yes... I'm certain that I fell asleep outside last night...)"
 stop sound
 show expression 'images/bg/AdvBg_132.png' as bg
 camera at sepia_shader
 pause 0.0
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator 'My tipoff was that, around noon, I got a phone call from Mion-san.'
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") '"There\'s gonna be a meteor shower tonight. The weather\'s looking good too, so why don\'t we all go to the Furude Shrine\'s lookout and do some stargazing?"'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 camera at reset_shader
 pause 0.0
 narrator "In response to Mion-san's invitation, I went with Miyuki-chan and Nao-chan to the Furude Shrine..."
 narrator 'The next day was Sunday, so we stayed up all night talking with Rena-san and the others about various things, and we had fun camping out... I think...'
 stop sound
 show expression 'images/bg/AdvBg_1390.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 show kazuho_v002 fuan at mei_center
 with Dissolve(0.5)
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'B-But... how am I here if so...?!'
 show kazuho_v002 fuan at inactive
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'Ah... you finally got up, Kazuho.'
 hide kazuho_v002
 with Dissolve(0.2)
 narrator '...Just then, I heard a voice behind me calling out my name.\nI turned my head in surprise and saw that everyone I was with before I went to sleep was gathered there.'
 show kazuho_v002 odoroki at mei_left
 with Dissolve(0.5)
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '...Miyuki-chan, Nao-chan? And Rena-chan and the others...!'
 show miyuki_v002 normal at mei_right
 with Dissolve(0.5)
 show kazuho_v002 odoroki at inactive
 show miyuki_v002 normal at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "You okay? We got a little worried since you wouldn't wake up."
 show miyuki_v002 normal at inactive
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Mi-Miyuki-chan... what is this?'
 hide miyuki_v002
 show nao_v002 fuan at mei_right
 with Dissolve(0.5)
 show kazuho_v002 odoroki at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "We're just as confused as you are. That's why we've been discussing what to do."
 hide nao_v002
 show satoko_v002 fuan at mei_right
 with Dissolve(0.5)
 show kazuho_v002 odoroki at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Well, discuss or not... this is honestly far beyond anything we could have expected, so we've given up hope."
 show satoko_v002 fuan at inactive
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") "That is... true, isn't it...?"
 hide kazuho_v002
 hide satoko_v002
 with Dissolve(0.2)
 narrator "By waking up in a place that we don't recognize... we're left with far too many questions, so we have no choice but to be perplexed."
 narrator "The club members don't look too upset all things considered.\n...Though {i}I{/i} might just be so surprised that my senses are numb."
 show kazuho_v002 smile_close at mei_center
 with Dissolve(0.5)
 show kazuho_v002 smile_close at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '(Despite that... seeing everyone here together is actually a little reassuring...)'
 hide kazuho_v002
 with Dissolve(0.2)
 show shion_v002 fuan at mei_left
 with Dissolve(0.5)
 show shion_v002 fuan at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "But regardless, why would we have been gathered in a place like this...?\nThis isn't another one of Sis's pranks, is it?"
 show mion_v002 sinken at mei_right
 with Dissolve(0.5)
 show shion_v002 fuan at inactive
 show mion_v002 sinken at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...Not at all.\nI've been telling you. Putting together a large-scale set like this is far beyond the level of jokes or playing around."
 show shion_v002 fuan at inactive
 show mion_v002 normal_close at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "I'm pretty sure last night we talked about having a contest to count how many shooting stars we saw, but..."
 show shion_v002 fuan at inactive
 show mion_v002 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "I can't believe we woke up in a place like this. I don't know how many times I pinched my cheeks trying to see if this was a dream."
 hide shion_v002
 show rena_v002 odoroki at mei_left
 with Dissolve(0.5)
 show mion_v002 fuan at inactive
 show rena_v002 odoroki at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Hau... so we really are in a spaceship?\nCould we possibly have been abducted by aliens, by aliens...?'
 hide mion_v002
 show miyuki_v002 fuan at mei_right
 with Dissolve(0.5)
 show rena_v002 odoroki at inactive
 show miyuki_v002 fuan at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "N-No way.\nThis isn't like your cliché sci-fi movie... but wait, there's something else I'm worried about."
 hide rena_v002
 show nao_v002 odoroki at mei_left
 with Dissolve(0.5)
 show miyuki_v002 fuan at inactive
 show nao_v002 odoroki at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "What's wrong, Miyuki?"
 show nao_v002 odoroki at inactive
 show miyuki_v002 fuan at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") "Where is... Rika-chan? And I don't see Hanyuu anywhere either..."
 hide nao_v002
 show satoko_v002 fuan at mei_left
 with Dissolve(0.5)
 show miyuki_v002 fuan at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "...I've been wondering that myself. I'm positive that those two were with us when we fell asleep last night, but—... oh my?"
 hide miyuki_v002
 hide satoko_v002
 with Dissolve(0.2)
 narrator 'In the midst of our conversation, a sound like an alarm buzzer suddenly started going off.'
 narrator 'As we turned towards the source of the noise, we saw the back wall open up. We all braced ourselves out of expectation for the worst.'
 show kazuho_v002 odoroki at mei_center
 with Dissolve(0.5)
 show kazuho_v002 odoroki at active
 show kazuho_v002 odoroki at jumping_transform
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'Huh...?'
 hide kazuho_v002
 with Dissolve(0.2)
 narrator 'I became weak and dumbfounded upon seeing the faces of who appeared... because those two were people that we were all very familiar with.'
 play audio 'audio/sfx/SE_540_footstep.wav'
 show keiichi_v007 smile at mei_center
 show keiichi_v007 smile at walk_transform:
  yanchor 1.0
  linear 0.6666666666666666 pos (1440,1200)
 with Dissolve(0.5)
 pause 0.16666666666666663
 show keiichi_v007 smile:
  yanchor 1.0
  pos (1440,1200)
 show keiichi_v007 smile at active
 Character('????',ctc="ctcArrow", ctc_position="fixed") "...Ah, it seems you're all awake."
 show rika_v012 smile at mei_outerleft
 show rika_v012 smile at walk_transform:
  yanchor 1.0
  linear 0.6666666666666666 pos (480,1200)
 with Dissolve(0.5)
 pause 0.16666666666666663
 show rika_v012 smile:
  yanchor 1.0
  pos (480,1200)
 show keiichi_v007 smile at inactive
 show rika_v012 smile at active
 Character('????',ctc="ctcArrow", ctc_position="fixed") 'Meep. Scanning organic data...... all green.\nAll subjects showing normal health levels, nipah.'
 hide keiichi_v007
 hide rika_v012
 with Dissolve(0.2)
 show kazuho_v002 fuan at mei_center
 with Dissolve(0.5)
 show kazuho_v002 fuan at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'U-...um...'
 hide kazuho_v002
 with Dissolve(0.2)
 narrator 'The ones who were walking in and saying these things were none other than Maebara-kun and Rika-chan... or rather, what seemed to be them...'
 show satoko_v002 smile at mei_left
 with Dissolve(0.5)
 show satoko_v002 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Rika...! I'm so glad you're alright.\nDo you have any idea how worried we were when we didn't see you anywhere?"
 show rika_v012 odoroki at mei_right
 with Dissolve(0.5)
 show satoko_v002 smile at inactive
 show rika_v012 odoroki at active
 Character('????',ctc="ctcArrow", ctc_position="fixed") '...Meep?'
 hide satoko_v002
 show rena_v002 odoroki at mei_left
 with Dissolve(0.5)
 show rika_v012 odoroki at inactive
 show rena_v002 odoroki at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "Hau... what's wrong, Rika-chan? And Keiichi-kun too... could you perhaps tell us why you're in those outfits, those outfits?"
 hide rika_v012
 hide rena_v002
 with Dissolve(0.2)
 narrator 'After seeing the two of them, Rena-san tilts her head with a look of suspicion and asks that question.'
 narrator "She was definitely right to ask; Rika-chan's attire was clearly different from what we saw her wearing last night. And Maebara-kun's outfit was... how should I put this...?"
 show mion_v002 fuan at mei_left
 with Dissolve(0.5)
 show mion_v002 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Boy... Kei-chan. I don't mean to knock on your personal tastes... but where'd you get such a gaudy outfit?"
 show nao_v002 normal at mei_right
 with Dissolve(0.5)
 show mion_v002 fuan at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'It looks sci-fi... but the style is old-fashioned.\nThe designs they have in Tokusatsu are much more purposeful and convenient. I feel like I should scold this designer.'
 hide mion_v002
 show kazuho_v002 smile at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show kazuho_v002 smile at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'A-Ahahaha...'
 hide nao_v002
 hide kazuho_v002
 with Dissolve(0.2)
 narrator 'Perhaps as a way to relieve some tension, Mion-san and the others say some pretty awful things while maintaining their baffled looks.'
 narrator "But Maebara-kun and Rika-chan didn't get angry or laugh in response... instead, they tilted their heads and stared back at us with looks just as puzzled."
 show keiichi_v007 odoroki at mei_right
 with Dissolve(0.5)
 show keiichi_v007 odoroki at active
 Character('????',ctc="ctcArrow", ctc_position="fixed") '...These guys seem to be mistaking us for other people somehow.\nWhat do you think, Lady Meep?'
 show rika_v012 smile at mei_left
 with Dissolve(0.5)
 show keiichi_v007 odoroki at inactive
 show rika_v012 smile at active
 Character('????',ctc="ctcArrow", ctc_position="fixed") 'Meep. It is conceivable that their memories may be in disarray following their resurrection. This is nothing particularly worrisome, nipah.'
 hide rika_v012
 show rena_v002 odoroki at mei_left
 with Dissolve(0.5)
 show keiichi_v007 odoroki at inactive
 show rena_v002 odoroki at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") "Hau... our memories are in disarray?\nAnd could you mean by saying we're mistaking you for other people... other people?"
 show rena_v002 odoroki at inactive
 show keiichi_v007 normal at active
 Character('????',ctc="ctcArrow", ctc_position="fixed") 'Well, to boot... I ought to introduce myself since this is our first meeting.'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide keiichi_v007
 hide rena_v002
 hide fade onlayer curtain
 show keiichi_v007 smile at mei_center
 with Dissolve(0.08333333333333333)
 show keiichi_v007 smile at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "My name is {b}K-1{/b}.\nI'm with the Universal Environment Protection Coalition, and affiliated with the Allied Police of the Great Galactic Cluster."
 show keiichi_v007 smile at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") 'I happen to be an archaeologist with a specialty in investigating Earth-era ruins. Nice to meet you.'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide keiichi_v007
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show miyuki_v002 odoroki at mei_center
 with Dissolve(0.5)
 show miyuki_v002 odoroki at active
 show miyuki_v002 odoroki at jumping_transform
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'H-...huhh? Great Galactic Cluster, Universal Environment Protection Coalition... and to top it all off, {i}archaeologyyy{/i}?!'
 hide miyuki_v002
 with Dissolve(0.2)
 narrator 'Miyuki-chan raises her voice in hysterics and exhales a deep sigh.'
 narrator 'For a joke, this was certainly elaborate.\n...The others felt the same way, and exchanged glances and nervous smiles.'
 show mion_v002 fuan at mei_left
 with Dissolve(0.5)
 show mion_v002 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...Hey, uh, Kei-chan. This is a nice joke and all, but I want a serious explanation. We seriously don't know what's going on, y'know?"
 show rika_v012 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 fuan at inactive
 show rika_v012 smile at active
 Character('Lady Meep',ctc="ctcArrow", ctc_position="fixed") "Meep. And I am {b}Lady Meep{/b}, employed as K-1's assistant.\nIt is a pleasure to make your acquaintance."
 hide mion_v002
 show nao_v002 odoroki at mei_left
 with Dissolve(0.5)
 show rika_v012 smile at inactive
 show nao_v002 odoroki at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '......U-Uuuuum...'
 hide rika_v012
 hide nao_v002
 with Dissolve(0.2)
 narrator 'Is this... some kind of game?\nRegardless of how well they personify their roles, their explanation was too abrupt, so it was incredibly hard to follow along with what they were saying.'
 narrator 'Mion-san, not liking their uncooperative way of speaking, agitatedly spat out an, "Ughh, you...!", and pressed them further.'
 show mion_v002 sinken at mei_right
 with Dissolve(0.5)
 show mion_v002 sinken at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Seriously, that's enough! Rika-chan, stop screwing around and get explaining! Are you trying to make me mad?"
 show rena_v002 fuan at mei_left
 with Dissolve(0.5)
 show mion_v002 sinken at inactive
 show rena_v002 fuan at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'Mi-...Mii-chan, please calm down.\nFighting is no good...!'
 hide rena_v002
 show shion_v002 sinken at mei_left
 with Dissolve(0.5)
 show mion_v002 sinken at inactive
 show shion_v002 sinken at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Yeah, Sis, let's tone it down. \n...Although, I do think I'm starting to feel insulted and a little annoyed myself."
 show shion_v002 sinken at inactive
 show mion_v002 sinken at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "I AM calm! Isn't it those two who are getting carried away?!"
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 narrator 'Rena-san and Shion-san try to calm her down, but Mion-san keeps glaring unhappily at Maebara-kun and Rika-chan.'
 narrator '...Despite this, Maebara-kun was simply looking through a file Rika-chan gave him while remaining indifferent.'
 show keiichi_v007 normal at mei_right
 with Dissolve(0.5)
 show keiichi_v007 normal at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "Specimen name... {b}Mion Sonozaki{/b}, huh?\nI heard you were a female student, but I didn't think you were that ferocious."
 show keiichi_v007 fuan at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "Say, Lady Meep. Out of all the samples of the dead you picked up, you couldn't find any {i}normal{/i} ones?"
 show rika_v012 normal at mei_left
 with Dissolve(0.5)
 show keiichi_v007 fuan at inactive
 show rika_v012 normal at active
 Character('Lady Meep',ctc="ctcArrow", ctc_position="fixed") 'Meep. We collected more surviving DNA samples at the site, but these six were the only successful cloning attempts.'
 show rika_v012 normal at inactive
 show keiichi_v007 normal_close at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") 'I see. Guess I gotta make do with these guys, huh...?'
 hide rika_v012
 with Dissolve(0.2)
 show mion_v002 sinken at mei_left
 show mion_v002 sinken at walk_transform:
  yanchor 1.0
  linear 0.6666666666666666 pos (960,1200)
 with Dissolve(0.5)
 pause 0.16666666666666663
 show mion_v002 sinken:
  yanchor 1.0
  pos (960,1200)
 show keiichi_v007 normal_close at inactive
 show mion_v002 sinken at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Hey... don't ignore me!\nYou wanna be like that, then I'll have to――"
 show mion_v002 sinken at inactive
 show keiichi_v007 normal_close at inactive
 narrator 'As Mion-san said that, she reached her fingers out to grab Maebara-kun. Suddenly...'
 camera:
  parallel:
   linear 0.5 pos (960, 510)
  parallel:
   linear 0.5 zoom 1.3
 show mion_v002 sinken at inactive
 show keiichi_v007 sinken at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") '...gh-...!!'
 stop music fadeout 0.5
 play audio 'audio/sfx/SE_211_electric.wav'
 show mion_v002 sinken at inactive
 show keiichi_v007 sinken at inactive
 narrator 'A flash of bluish-white light bursts in between them.'
 show keiichi_v007 sinken at inactive
 show mion_v002 odoroki at active
 show mion_v002 odoroki at jumping_transform
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Ngyaaaaaah?!'
 hide keiichi_v007
 hide mion_v002
 with Dissolve(0.2)
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 play audio 'audio/sfx/SE_218_down.wav'
 narrator 'Mion-san yelped and fell over the instant after being enveloped in that light. We helped her up as soon as we witnessed it happen.'
 play audio 'audio/sfx/SE_528_unfold_cloth.wav'
 show rena_v002 odoroki at mei_right
 with Dissolve(0.5)
 show rena_v002 odoroki at active
 Character('Rena',ctc="ctcArrow", ctc_position="fixed") 'M-Mii-chan? Are you okay?!'
 show shion_v002 sinken at mei_left
 with Dissolve(0.5)
 show rena_v002 odoroki at inactive
 show shion_v002 sinken at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Hey, Sis, please get ahold of yourself!\nSis... Siiis!'
 hide rena_v002
 hide shion_v002
 with Dissolve(0.2)
 play music "<loop 1.87>audio/bgm/BGM_EVENT6.ogg"
 narrator 'Rena-san and Shion-san called out to her fervently, but Mion-san lay limp and unresponsive. ...It looks like she lost consciousness.'
 show keiichi_v007 smile at mei_center
 with Dissolve(0.5)
 show keiichi_v007 smile at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "Ah, my bad. Didn't mean to get rough... but if she kept acting up, this conversation wouldn't go anywhere."
 hide keiichi_v007
 with Dissolve(0.2)
 narrator 'Saying that, Maebara-kun held up something like a gun.'
 narrator 'The flash of light seemed to come from that.\nBut then that would mean... he shot Mion-san...?!'
 show rika_v012 normal at mei_left
 with Dissolve(0.5)
 show rika_v012 normal at active
 Character('Lady Meep',ctc="ctcArrow", ctc_position="fixed") '...K-1. I am led to believe that their memories are in disarray post-revival.'
 show rika_v012 smile at active
 Character('Lady Meep',ctc="ctcArrow", ctc_position="fixed") 'We must explain our future plans to them.'
 show keiichi_v007 normal at mei_right
 with Dissolve(0.5)
 show rika_v012 smile at inactive
 show keiichi_v007 normal at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "Mm... I guess you're right.\nAlright, everyone, I'm gonna explain it all, so hear me out from start to finish."
 hide rika_v012
 show kazuho_v002 sinken at mei_left
 with Dissolve(0.5)
 show keiichi_v007 normal at inactive
 show kazuho_v002 sinken at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") '............'
 show kazuho_v002 sinken at inactive
 show keiichi_v007 normal at active
 Character('K-1',ctc="ctcArrow", ctc_position="fixed") "Let's see... this might be hard to believe, but a long time ago... a thousand years ago in fact, you all died. And from there, you were revived... brought back to life."
 hide kazuho_v002
 show miyuki_v002 odoroki at mei_left
 with Dissolve(0.5)
 show keiichi_v007 normal at inactive
 show miyuki_v002 odoroki at active
 Character('Miyuki Akasaka',ctc="ctcArrow", ctc_position="fixed") 'H-...huh...?!'
 hide miyuki_v002
 show kazuho_v002 odoroki at mei_left
 with Dissolve(0.5)
 show keiichi_v007 normal at inactive
 show kazuho_v002 odoroki at active
 Character('Kazuho Kimiyoshi',ctc="ctcArrow", ctc_position="fixed") 'We died... and came back to life?\nHow on earth...?'
 hide keiichi_v007
 show rika_v012 smile at mei_right
 with Dissolve(0.5)
 show kazuho_v002 odoroki at inactive
 show rika_v012 smile at active
 Character('Lady Meep',ctc="ctcArrow", ctc_position="fixed") 'Meep. Your DNA was collected from the remains of victims who died in a great disaster one-thousand years ago...'
 play audio 'audio/sfx/SE_022_WaveStart.wav'
 show kazuho_v002 odoroki at inactive
 show rika_v012 smile at active
 Character('Lady Meep',ctc="ctcArrow", ctc_position="fixed") 'You were all brought back to life as clones. Nipah.'
 hide kazuho_v002
 show nao_v002 odoroki at mei_left
 with Dissolve(0.5)
 show rika_v012 smile at inactive
 show nao_v002 odoroki at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Y-You're lying...? That couldn't be...?!"
 hide rika_v012
 hide nao_v002
 with Dissolve(0.2)
 narrator 'The fact that Rika-chan was smiling as she told us this... was a terrible gut-punch to us.'
 call chapter_end
 jump event01_16_01