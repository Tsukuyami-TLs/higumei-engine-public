label event01_30_09:
 stop sound
 scene expression "#000"
 play music 'audio/bgm/BGM_QUEST1_COLLAB2.wav'
 show expression 'images/bg/AdvBg_2190.png' as bg
 with Dissolve(1.0)
 show erika_v001 normal at mei_left
 show beatrice_v001 normal at mei_right
 with Dissolve(0.5)
 show beatrice_v001 normal at active
 show erika_v001 normal at inactive
 beatrice "It's my turn now. I'll attack Erika next."
 show beatrice_v001 normal at active
 show erika_v001 normal at inactive
 beatrice 'Erika argued that Shion was the culprit, correct?'
 show beatrice_v001 normal at active
 show erika_v001 normal at inactive
 beatrice "......If there's something that makes you so sure of that, why don't you show it to me?"
 show erika_v001 normal at active
 show beatrice_v001 normal at inactive
 erika ''
 hide erika_v001
 hide beatrice_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao "It's true that Shion was the only one to turn back to search for something at the guesthouse, and thus lost an alibi..."
 hide nao_v002
 with Dissolve(0.2)
 narrator "But I don't want to let Shion-san be declared the culprit just because she doesn't have an alibi. "
 show nao_v002 normal at mei_left
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show nao_v002 normal at inactive
 dlanor 'Lady Beatrice, is that what you wish to DO?'
 show nao_v002 normal at active
 show dlanor_v001 normal at inactive
 nao 'I understand. Beatrice, if you will.'
 hide nao_v002
 hide dlanor_v001
 with Dissolve(0.2)
 show erika_v001 normal at mei_left
 show beatrice_v001 normal_close at mei_right
 with Dissolve(0.5)
 show beatrice_v001 normal_close at active
 show erika_v001 normal at inactive
 beatrice "Mu, then let's get to the heart of the matter!"
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show beatrice_v001 futeki at active
 show erika_v001 normal at inactive
 beatrice 'Show it to me, Erika! Proof that Shion is the culprit!'
 show erika_v001 normal_close at active
 show beatrice_v001 futeki at inactive
 erika 'If that is the case, please accept this.'
 show erika_v001 futeki at active
 show beatrice_v001 futeki at inactive
 erika 'There is clear evidence that Shion-san broke into my room!'
 window hide None
 show expression "#000" as fade with Dissolve(1.0)
 stop sound
 scene expression "#000"
 hide beatrice_v001
 with Dissolve(0.3)
 show expression 'images/bg/AdvBg_2281.png' as bg
 with Dissolve(1.0)
 pause 1.0
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show shion_v007 odoroki at mei_center
 with Dissolve(0.5)
 show shion_v007 odoroki at jump_transform,active
 shion 'Huh? Wha, what on earth...!?'
 hide shion_v007
 with Dissolve(0.2)
 narrator 'Since a magic circle had just appeared in her room, I thought Erika would have been shaking in fear.'
 narrator 'But suddenly, she burst into laughter and displayed an extression that seemed to say that some fool had fallen into her trap......'
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika 'Thank you for participating in this charade.'
 show erika_v001 normal at active
 erika "Now, let's look at the details."
 show erika_v001 normal at active
 erika 'One moment ago, everybody heard me scream and entered via the open door.'
 show erika_v001 normal at active
 erika "In other words, none of you should have touched this room's doorknob."
 hide erika_v001
 with Dissolve(0.2)
 show shion_v007 sinken at mei_left
 show mion_v008 sinken at mei_right
 with Dissolve(0.5)
 show mion_v008 sinken at active
 show shion_v007 sinken at inactive
 mion ".....What do you mean........? ....It can't be....."
 show shion_v007 sinken at active
 show mion_v008 sinken at inactive
 shion '.....'
 hide shion_v007
 hide mion_v008
 with Dissolve(0.2)
 narrator "The Sonozaki sisters' faces turned pale. .....Then, did that mean that the summoning circle was Shion's doing after all.....?!"
 show nao_v002 normal at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show nao_v002 normal at inactive
 erika "Everybody, please wait here for a moment. I'm going to close the curtains."
 show nao_v002 normal at active
 show erika_v001 normal at inactive
 nao '...What are you doing?'
 show erika_v001 normal at active
 show nao_v002 normal at inactive
 erika 'Shion Sonozaki-san. This way.'
 hide nao_v002
 show shion_v007 normal at mei_left
 with Dissolve(0.5)
 show shion_v007 normal at active
 show erika_v001 normal at inactive
 shion ".....Being treated like a criminal is upsetting, but if I refuse, she's just going to suspect me more."
 hide erika_v001
 hide shion_v007
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_229_grap.wav'
 narrator 'As Shion stepped forward...Erika grabbed her wrist in a vice-like grip, almost like it was a pair of handcuffs.'
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika "Isn't this checkmate, Shion-san?"
 hide erika_v001
 with Dissolve(0.2)
 show nao_v002 sinken at mei_left
 show mion_v008 sinken at mei_right
 with Dissolve(0.5)
 show mion_v008 sinken at active
 show nao_v002 sinken at inactive
 mion "Erika-san, you're suspecting Shion because she went back to the guesthouse after she told us she had forgot her room key!?!"
 show nao_v002 sinken at active
 show mion_v008 sinken at inactive
 nao "I agree. Just because somebody lacks an alibi doesn't nessecarily mean that person is the culprit."
 hide nao_v002
 hide mion_v008
 with Dissolve(0.2)
 show erika_v001 normal at mei_right
 show shion_v007 sinken at mei_left
 with Dissolve(0.5)
 show shion_v007 sinken at active
 show erika_v001 normal at inactive
 shion "I didn't enter that room. If you want to say otherwise, then please show me the evidence!"
 show erika_v001 smile at active
 show shion_v007 sinken at inactive
 erika '<Good!>.......those words are like music to my ears ♪'
 hide erika_v001
 hide shion_v007
 with Dissolve(0.2)
 narrator "I heard the quiet sound of teeth grinding. Shion-san's face.....was distorted in disgust."
 play audio 'audio/sfx/SE_5005_grab.wav'
 narrator "Was Erika's grip so tight that it hurt? .....Or was her evidence no longer a fatal blow?"
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika "Nao-chama, can you please turn off the lights in this room? It'll be fine; I have a penlight."
 hide erika_v001
 with Dissolve(0.2)
 narrator "She called it a penlight, but from an outsider's perspective, it looked like a rather plump fountain pen."
 narrator 'However, when Erika fiddled with it using her free hand, it became clear that it did indeed have a light function...'
 show nao_v002 normal at mei_left
 show mion_v008 sinken at mei_right
 with Dissolve(0.5)
 show mion_v008 sinken at active
 show nao_v002 normal at inactive
 mion "Hmmm.....if you say that you have evidence that Shion did it, then let's see it."
 show mion_v008 normal at active
 show nao_v002 normal at inactive
 mion 'Nao-chan, can you turn off the lights?'
 show nao_v002 normal_close at active
 show mion_v008 normal at inactive
 nao '...Understood.'
 play audio 'audio/sfx/SE_5004_lightoff.wav'
 show expression "#000" as fade with Dissolve(1.0)
 hide nao_v002
 hide mion_v008
 with Dissolve(0.2)
 play sound ['audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav'] fadeout 1.0
 stop music fadeout 2.0
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2283.png' as bg
 with Dissolve(1.0)
 narrator 'At this time of year, it would get dark quite early in the day. Once the lights were turned off and the curtains closed, it was pitch black.'
 narrator 'Erika-san immidiately turned on a penlight.'
 show mion_v008 normal at mei_center
 with Dissolve(0.5)
 show mion_v008 normal at active
 mion "It looks like a spy's tool. At first glance, it appears to be a fountain pen, but it's able to emit light."
 show mion_v008 normal at active
 mion 'I bet it has other hidden features.'
 hide mion_v008
 with Dissolve(0.2)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika "You've got a discerning eye. Naturally, this isn't the penlight's only feature."
 show erika_v001 normal_close at active
 erika 'Before explaining its features, let me reveal the secret behind this doorknob.'
 play music 'audio/bgm/BGM_QUEST3_COLLAB2.wav'
 show erika_v001 normal at active
 erika 'My mentioning that I forgot to lock my door in front of everybody was all a trap designed to draw in the culprit.'
 show erika_v001 normal at active
 erika 'In order to make the best out of this one-in-a-millenia chance, the culprit had to make an excuse to go back to the guesthouse.'
 hide erika_v001
 with Dissolve(0.2)
 show mion_v008 sinken at mei_right
 show shion_v007 sinken at mei_left
 with Dissolve(0.5)
 show shion_v007 sinken at active
 show mion_v008 sinken at inactive
 shion "I only came back in order to look for some photography equipment. I didn't do anything like enter your room!"
 show mion_v008 sinken at active
 show shion_v007 sinken at inactive
 mion '....So what is.....the secret of the doorknob.....'
 hide mion_v008
 hide shion_v007
 with Dissolve(0.2)
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 nao 'Ah.....maybe......'
 hide nao_v002
 with Dissolve(0.2)
 narrator "It couldn't be.......fingerprints? With proper equipment and knowledge, it wasn't impossible."
 narrator "In addition, Erika called herself a detective. Maybe she could identify Shion's fingerprints on the doorknob.....!"
 show nao_v002 fuan at mei_left
 show erika_v001 normal_close at mei_right
 with Dissolve(0.5)
 show erika_v001 normal_close at active
 show nao_v002 fuan at inactive
 erika 'No, no. I used a simpler, clearer, and more obvious trick.'
 show erika_v001 normal at active
 show nao_v002 fuan at inactive
 erika 'Nao-chama. Can you hold this pen light?'
 show nao_v002 fuan at active
 show erika_v001 normal at inactive
 nao 'Huh? Okay...'
 show erika_v001 normal at active
 show nao_v002 fuan at inactive
 erika "Twist it here until there's a click."
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 narrator "As I did as I was told, the penlight's light went out, and was replaced by a faint blue-purple glow."
 show mion_v008 normal at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show mion_v008 normal at inactive
 nao 'This is.....'
 show mion_v008 normal at active
 show nao_v002 normal at inactive
 mion 'A black light...?'
 hide mion_v008
 hide nao_v002
 with Dissolve(0.2)
 show erika_v001 normal at mei_right
 show shion_v007 fuan at mei_left
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_5005_grab.wav'
 show shion_v007 fuan at chara_shake_transform,active
 show erika_v001 normal at inactive
 shion '...Hey, that hurts.....can you please grip me a little more gently?'
 show erika_v001 normal at active
 show shion_v007 fuan at inactive
 erika 'Nao-chama, can you please shine that black light on my palms?'
 hide erika_v001
 hide shion_v007
 with Dissolve(0.2)
 show nao_v002 odoroki at mei_center
 with Dissolve(0.5)
 show nao_v002 odoroki at active
 nao 'Like this? .....Ah.'
 hide nao_v002
 with Dissolve(0.2)
 show erika_v001 normal at mei_right
 show shion_v007 sinken at mei_left
 with Dissolve(0.5)
 show shion_v007 sinken at active
 show erika_v001 normal at inactive
 shion "...Tch. You've been carrying that around since before you came here, haven't you....?"
 show erika_v001 normal at active
 show shion_v007 sinken at inactive
 erika "That's because I'm a detective. Even when I'm on vacation, I will at the very least bring a detective's kit with me."
 hide erika_v001
 hide shion_v007
 with Dissolve(0.2)
 show mion_v008 normal at mei_center
 with Dissolve(0.5)
 show mion_v008 normal at active
 mion '....Florescent.....paint.....'
 hide mion_v008
 with Dissolve(0.2)
 narrator "I shined the black light on Erika-san's palms.....and thin streaks of yellow-green glimmered in the light......"
 show shion_v007 sinken at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show shion_v007 sinken at inactive
 erika "I painted this room's doorknob this morning."
 show erika_v001 normal at active
 show shion_v007 sinken at inactive
 erika 'This paint is specially formulated to stick to the hands of whoever touches the doorknob for the whole day.'
 show erika_v001 normal at active
 show shion_v007 sinken at inactive
 erika 'Furthermore, once the paint has adhered to you, it cannot be removed by washing it off.'
 camera at screenshake_transform
 pause 0.0
 show shion_v007 sinken at active
 show erika_v001 normal at inactive
 shion '....Ku.........'
 show erika_v001 normal_close at active
 show shion_v007 sinken at inactive
 erika "I was the one who made this special chemical mixture. A certain chemical compound is required to remove it. Don't worry, naturally I brought it with me."
 show shion_v007 sinken at active
 show erika_v001 normal_close at inactive
 shion "...Isn't that excellent? In other words, this means that no matter how many showers I take, I will still have that florescent paint on my hands?"
 show erika_v001 normal at active
 show shion_v007 sinken at inactive
 erika "Exactly. Now, I'm going to look at your palms under the black light."
 show erika_v001 normal at active
 show shion_v007 sinken at inactive
 erika "However.......as a detective's mercy, rather than disgracing you by confronting you with lethal evidence, I'll give you the chance for a gentleman's loss and admit defeat yourself. "
 show shion_v007 normal_close at active
 show erika_v001 normal at inactive
 shion "...I don't know what's up with you playing detective......but if it involves victory and defeat......"
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide shion_v007
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 show mion_v008 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show mion_v008 sinken at active
 mion "The Sonozaki sisters.....defintely won't lose. We'll prove to you that even though it's been split between the two of us, the blood of the next head flows hot and thick through our veins!"
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide mion_v008
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika ''
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 camera at screenshake_transform
 pause 0.0
 show erika_v001 fuan at active
 erika 'Now, the time for pity is over!! Show me your palms!! Show theeeeeeeem!!!!! [erika noises]'
 stop music fadeout 0.5
 window hide None
 show expression "#000" as fade with Dissolve(1.0)
 hide erika_v001
 with Dissolve(0.2)
 pause 1.0
 stop sound
 scene expression "#000"
 play music 'audio/bgm/BGM_BOSS1_COLLAB2.wav'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 show expression 'images/bg/AdvBg_2190.png' as bg
 with Dissolve(1.0)
 show dlanor_v001 normal at mei_right
 show erika_v001 odoroki at mei_left
 with Dissolve(0.5)
 show erika_v001 odoroki at active
 show dlanor_v001 normal at inactive
 erika 'What?? O, one more check!'
 show dlanor_v001 normal at active
 show erika_v001 odoroki at inactive
 dlanor "Shion Sonozaki's hands do not have any florescent paint on THEM. "
 show erika_v001 sinken at active
 show dlanor_v001 normal at inactive
 erika 'What the hell are you talking about!? Check her again!!'
 show dlanor_v001 normal at active
 show erika_v001 sinken at inactive
 dlanor "I haven't restricted my search to just her HANDS. Shion Sonozaki's body does not have any florescent paint on IT. "
 camera at screenshake_transform
 pause 0.0
 show erika_v001 odoroki at active
 show dlanor_v001 normal at inactive
 erika 'AAAAAAAAAAAAAAAA what do you meaaaaaan!!!!! Do it again, and say it in reeeeeed!!!!!! '
 show dlanor_v001 normal at active
 show erika_v001 odoroki at inactive
 dlanor 'I will repeat it in RED.'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide dlanor_v001
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 show dlanor_v001 normal at mei_center
 with Dissolve(0.08333333333333333)
 show expression "#e11" as fade with Dissolve(0.16666666666666666)
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 hide fade with Dissolve(0.16666666666666666)
 with Dissolve(0.16666666666666666)
 show dlanor_v001 normal at active
 dlanor "#ff0000 Shion Sonozaki's body does not have any florescent paint on IT. #r"
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide dlanor_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show dlanor_v001 normal at mei_right
 show erika_v001 odoroki at mei_left
 with Dissolve(0.5)
 camera at screenshake_transform
 pause 0.0
 show erika_v001 odoroki at active
 show dlanor_v001 normal at inactive
 erika "N, nonononono, this, this!!!! I, it's impossible, there's no way!!!!"
 hide dlanor_v001
 show beatrice_v001 futeki at mei_right
 with Dissolve(0.5)
 show beatrice_v001 futeki at active
 show erika_v001 odoroki at inactive
 beatrice "Oya? Isn't this strange, Erika. Isn't this the work of a witch?"
 camera at screenshake_transform
 pause 0.0
 show erika_v001 sinken at active
 show beatrice_v001 futeki at inactive
 erika 'Shut up shut up shut uuuuuuuuuuup!!! '
 hide erika_v001
 hide beatrice_v001
 with Dissolve(0.2)
 narrator "With that, Beatrice's turn was over. Next was Erika's turn, which would probably be used trying to recover."
 narrator 'Right now, Erika is shaking after receiving a powerful blow. That meant my next turn was crucial...!'
 show erika_v001 sinken at mei_left
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show erika_v001 sinken at inactive
 dlanor 'ERIKA. This is a game for gentlemen and LADIES. Please refrain from using vulgar SPEECH.'
 show erika_v001 sinken at chara_shake_transform,active
 show dlanor_v001 normal at inactive
 erika "Shuuuuuuut up, you murder doll!!! It's my turn!!!!!"
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide erika_v001
 hide dlanor_v001
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 sinken at active
 erika 'Blue truth!'
 play audio 'audio/sfx/SE_391_ls_swing.wav'
 show expression "#fff" as flash with Dissolve(0.1)
 pause 0.1
 hide flash with Dissolve(0.2)
 show erika_v001 sinken at active
 erika "#4169e1 Shion Sonozaki used a glove when she touched the doorknob! Naturally, this means the florescent paint wasn't able to get on her palms! #r"
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show dlanor_v001 normal_close at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal_close at active
 dlanor '...VALID.'
 window hide None
 show expression "#000" as fade with Dissolve(1.0)
 hide dlanor_v001
 with Dissolve(0.2)
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2281.png' as bg
 with Dissolve(1.0)
 show erika_v001 futeki at mei_center
 with Dissolve(0.5)
 show erika_v001 futeki at active
 erika "See?! It's possible for somebody to open the door to the room without getting my florescent paint on them!"
 show erika_v001 fuan at active
 erika 'Shion-san, you truly are a despicable woman...!!!'
 camera at screenshake_transform
 pause 0.0
 show erika_v001 fuan at active
 erika "I can't belive you'd be this cautious when breaking into somebody's room. You're a professional!! A career criminal!!!! A <superior extreme> feloooooooooooon!!!!"
 hide erika_v001
 with Dissolve(0.2)
 show mion_v008 normal at mei_right
 show shion_v007 normal_close at mei_left
 with Dissolve(0.5)
 show shion_v007 normal_close at active
 show mion_v008 normal at inactive
 shion 'You can say whatever you want about me. And by the way, I consider what you just said to be a compliment.'
 show mion_v008 normal at active
 show shion_v007 normal_close at inactive
 mion "...Shion definitely doesn't have an alibi, but.....doesn't that not prove she entered your room?"
 hide mion_v008
 hide shion_v007
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao "If you're still sure that Shion is the culprit, I need to you show me something besides this."
 show expression "#000" as fade with Dissolve(1.0)
 hide nao_v002
 with Dissolve(0.2)
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2190.png' as bg
 with Dissolve(1.0)
 show erika_v001 odoroki at mei_center
 with Dissolve(0.5)
 show erika_v001 odoroki at active
 erika 'Something besides this, something besides this [erika breaking down noises]'
 show erika_v001 odoroki_close at chara_shake_transform,active
 erika "It's fine, my master...! My reasoning is flawless. Aaaaaaaaa, so don't get mad, don't get mad..."
 hide erika_v001
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_left
 show beatrice_v001 smile at mei_right
 with Dissolve(0.5)
 show beatrice_v001 smile at active
 show dlanor_v001 normal at inactive
 beatrice "The next turn is Nao's. What line of reasoning will you put forward?"
 show dlanor_v001 normal at active
 show beatrice_v001 smile at inactive
 dlanor 'Now, NAO. It is your TURN.'
 hide dlanor_v001
 hide beatrice_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao "Um, I'd like to come out with information."
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show erika_v001 odoroki at active
 erika 'Huh....?!'
 show erika_v001 sinken at active
 erika 'Why is a normal, detestable, tasteless brat whose only good point is being stubborn coming out with information!?!?!?'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show nao_v002 normal at mei_left
 show beatrice_v001 normal at mei_right
 with Dissolve(0.5)
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice 'Nao, what on earth are you confessing to...?'
 show nao_v002 normal_close at active
 show beatrice_v001 normal at inactive
 nao "I am Nao Houtani. I consider myself a normal human, but.....the truth is, I've had strange expiriences that nobody would believe were real if I were to tell them."
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao "I have physically encountered paranormal phenomena such as gods and tsukuyami, and know that this world doesn't just contain what Humans think it does."
 show beatrice_v001 odoroki at active
 show nao_v002 normal at inactive
 beatrice '...What the....are you.....a voyager witch....!?'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide nao_v002
 hide beatrice_v001
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 sinken at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show erika_v001 sinken at active
 erika "There's no way that's truuuuue!!! You're just a tiny, inconsequential piece of garbage of a braaaaaaaat!!!!!"
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show dlanor_v001 normal at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show dlanor_v001 normal at inactive
 nao 'Dlanor-san, I am not lying. Please allow me to use the red truth.'
 show dlanor_v001 normal at active
 show nao_v002 normal at inactive
 dlanor 'What would you like to use it FOR...?'
 hide dlanor_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator "I whispered into Dlanor's ear."
 show nao_v002 normal at mei_left
 show dlanor_v001 odoroki at mei_right
 with Dissolve(0.5)
 show dlanor_v001 odoroki at active
 show nao_v002 normal at inactive
 dlanor '....I, I UNDERSTAND. .....However, in order to do that, I will need to see your HAND.'
 show nao_v002 normal at active
 show dlanor_v001 odoroki at inactive
 nao 'My hand?'
 hide nao_v002
 hide dlanor_v001
 with Dissolve(0.2)
 show beatrice_v001 normal_close at mei_center
 with Dissolve(0.5)
 show beatrice_v001 normal_close at active
 beatrice '...Dlanor wants to see your Fragment.'
 hide beatrice_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_left
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show nao_v002 normal at inactive
 dlanor 'Of course, I will only need to see the parts having to do with your red truth. In addition, I swear an oath of confidentiality to the great court of heaven that I will never reveal any other truths I have learned.'
 show nao_v002 normal at active
 show dlanor_v001 normal at inactive
 nao "...You mean she wants to look inside my head? I don't mind."
 show dlanor_v001 sinken at active
 show nao_v002 normal at inactive
 dlanor 'With that......please excuse me.......'
 hide nao_v002
 hide dlanor_v001
 with Dissolve(0.2)
 narrator "Dlanor-san's eyes turned almost see-through as they emitted a faint light."
 narrator 'All she was doing was staring at me, but.....it gave me a strange, uncomfortable feeling.'
 narrator '.....I see. That was what she meant when she said she wanted to look at my hand.'
 narrator "That uncomfortable feeling was everything I'd ever expirienced in my life, my thoughts, my feelings, and my emotions, being watched by a stranger."
 show beatrice_v001 normal at mei_right
 show dlanor_v001 normal_close at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal_close at active
 show beatrice_v001 normal at inactive
 dlanor '...NAO. Thank you very MUCH. I am FINISHED.'
 show beatrice_v001 normal at active
 show dlanor_v001 normal_close at inactive
 beatrice "And with that.....Dlanor's verdict is..."
 show dlanor_v001 normal at active
 show beatrice_v001 normal at inactive
 dlanor 'VALID.'
 show expression "#e11" as fade with Dissolve(0.16666666666666666)
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 hide fade with Dissolve(0.16666666666666666)
 with Dissolve(0.16666666666666666)
 show dlanor_v001 normal at active
 show beatrice_v001 normal at inactive
 dlanor '#ff0000Nao Houtani has been confirmed to have made contact and interacted with beings who are not human. #r'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide beatrice_v001
 hide dlanor_v001
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 sinken at active
 erika 'W....who the hell are you?! I thought you were just some bratty kid I happened to meet on the ferry.....!?'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show nao_v002 normal at mei_left
 show beatrice_v001 normal at mei_right
 with Dissolve(0.5)
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice "Didn't your master say once that black tea is best enjoyed with monsters?"
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice '.....I see. If a witch opens up the game board, witches, monsters, and similar beings may be invited in......'
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao 'All kinds of mysterious entities, such as ghosts and gods, exist in that world.'
 show nao_v002 normal_close at active
 show beatrice_v001 normal at inactive
 nao "Because of that, I don't deny Beatrice's existance. Her being here is proof enough."
 show beatrice_v001 odoroki at active
 show nao_v002 normal_close at inactive
 beatrice "Y, you recognize my existance.....Nao, I've never had a guest such as yourself."
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide nao_v002
 hide beatrice_v001
 hide fade with Dissolve(0.08333333333333333)
 show nao_v002 normal at mei_center
 with Dissolve(0.08333333333333333)
 show nao_v002 normal at active
 nao 'In addition, I am going to repeat my claims as to the first and second magic circle incidents. '
 show nao_v002 normal_close at active
 nao "First, let's put the second magic circle incident on the chopping block."
 play audio 'audio/sfx/SE_391_ls_swing.wav'
 show expression "#fff" as flash with Dissolve(0.1)
 pause 0.1
 hide flash with Dissolve(0.2)
 show nao_v002 normal at active
 nao '#4169e1The suspect Shion-san is innocent.#r'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show nao_v002 normal at mei_left
 show erika_v001 odoroki at mei_right
 with Dissolve(0.5)
 camera at screenshake_transform
 pause 0.0
 show erika_v001 odoroki at active
 show nao_v002 normal at inactive
 erika "That's impossible, totally impossible!!!!! Shion's the culprit!!!! She's definitely the culpriiiiiiiit!!!!!"
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.1
 pause 0.5
 play audio 'audio/sfx/SE_391_ls_swing.wav'
 show nao_v002 normal at active
 show erika_v001 odoroki at inactive
 nao '#4169e1Erika put a tag on her doorknob saying that she did not need her bed made. In other words, the servants would not enter her room. #r'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.2
 pause 0.5
 play audio 'audio/sfx/SE_391_ls_swing.wav'
 pause 0.3333333333333333
 play audio 'audio/sfx/SE_391_ls_swing.wav'
 show nao_v002 normal at active
 show erika_v001 odoroki at inactive
 nao "#4169e1Because of this, the only person who would be able to get into the room would be Shion-san, who, despite Erika's traps, was able to prove her innocence. #r"
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 play audio 'audio/sfx/SE_5036_glass_break.wav'
 show expression "#fff" as flash with Dissolve(0.1)
 pause 0.1
 hide flash with Dissolve(0.2)
 show nao_v002 sinken at active
 show erika_v001 odoroki at inactive
 nao "#4169e1Because of that, the second magic circle was impossible for a Human to make, and therefore is clearly a witch's prank! #r"
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide nao_v002
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show erika_v001 odoroki at active
 erika "That's not clear at alllllllll!!!!! Who did it, and where did they come from!?!?!? Don't make a mockery of the blue truuuuuuuth!!!"
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show nao_v002 sinken at mei_left
 show beatrice_v001 normal at mei_right
 with Dissolve(0.5)
 show beatrice_v001 normal at active
 show nao_v002 sinken at inactive
 beatrice ''
 show nao_v002 smile at active
 show beatrice_v001 normal at inactive
 nao "Don't worry. I'm going to win, too."
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao 'Dlanor-san, is my blue truth effective?'
 hide beatrice_v001
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show nao_v002 normal at inactive
 dlanor 'It is VALID. ...In return, Erika must submit either a red truth, equivalent evidence, or a REBUTTAL.'
 hide nao_v002
 show erika_v001 sinken_close at mei_left
 with Dissolve(0.5)
 show erika_v001 sinken_close at active
 show dlanor_v001 normal at inactive
 erika '......No........'
 show dlanor_v001 normal at active
 show erika_v001 sinken_close at inactive
 dlanor '...I did not hear THAT. Please repeat YOURSELF.'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide dlanor_v001
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show erika_v001 odoroki at active
 erika "There's.....no no no no no waaaay. Shion is absolutely, positively, certainly guilty......so why........so why do I need evidence.....!!!!"
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 narrator 'It seemed that Erika-san went all in on her gambit with the florescent paint on the doorknob.'
 narrator 'She had lost the card that was supposed to be her ace in the hole......and was now waiting for the count-out. '
 show nao_v002 normal at mei_left
 show beatrice_v001 normal_close at mei_right
 with Dissolve(0.5)
 show beatrice_v001 normal_close at active
 show nao_v002 normal at inactive
 beatrice 'Nao. With this, your turn is over...'
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice '...My turn is next. By using the blue truth you have established, I will be able to claim victory.......are you sure?'
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao "I'd like to negotiate."
 show beatrice_v001 smile at active
 show nao_v002 normal at inactive
 beatrice "Hou? Since you're letting me win, I will listen to what you have to say."
 show nao_v002 normal at active
 show beatrice_v001 smile at inactive
 nao 'The next turn is yours, but before you declare your victory, I want you to make one move for me.'
 show nao_v002 normal at active
 show beatrice_v001 smile at inactive
 nao "While the second magic circle is a witch's deed, Erika-san was the culprit for the first one. And just now, it finally occured to me why Shannon-san didn't feel anything strange when she found it."
 hide nao_v002
 hide beatrice_v001
 with Dissolve(0.2)
 narrator 'At last, the soup of logic, reasoning, and mystery.....had finished thickening.'
 show beatrice_v001 normal at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao 'Beatrice. You are a witch, correct?'
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice 'Of course.'
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao "Because of that, you're an expert in all sorts of spells and rites, correct? Which of course would also include magic circles."
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice 'Mu. My title is the infinite witch. There is nothing I do not know.'
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao 'Since you just said that, I want you to look at both the first and second magic circles.'
 window hide None
 show expression "#000" as fade with Dissolve(1.0)
 hide beatrice_v001
 hide nao_v002
 with Dissolve(0.2)
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 590)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 camera at sepia_shader
 pause 0.0
 hide fade with Dissolve(1.0)
 show beatrice_v001 sinken at mei_center
 with Dissolve(1.0)
 show beatrice_v001 sinken at active
 beatrice "...Even so, I don't understand this circle.....I don't know what it's used for."
 window hide None
 show expression "#000" as fade with Dissolve(1.0)
 hide beatrice_v001
 with Dissolve(0.2)
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 camera at reset_shader
 pause 0.0
 hide fade with Dissolve(1.0)
 with Dissolve(1.0)
 narrator "That itself was an explaination. Perhaps it wasn't a magic circle at all."
 narrator "That line of reasoning explains......why Shannon-san didn't see it as strange, and why Mion-san and Shion-san didn't seem to be too shocked when they saw it......!!"
 show beatrice_v001 normal at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao 'Can you please give us a more detailed explaination?'
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice 'Mu.....the shapes of a magic circle can roughly describe things like the center and flow of energy through it.....'
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice "...This circle looks like it's gathering magical energy from outside of it, but in reality it just passes through the circle without being collected, so it doesn't look like it has any meaning in particular. "
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao "So in the eyes of the witch called the great lord Beatrice......the magic circle doesn't make any sense at all?"
 show beatrice_v001 normal_close at active
 show nao_v002 normal at inactive
 beatrice 'Mu......this thing that appears to be a magic circle is an illegible fake.'
 hide beatrice_v001
 hide nao_v002
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 dlanor 'I am a Reader, so I have kept silent, but...I have never seen the letters on the circumference of the summoning circle BEFORE.'
 show dlanor_v001 normal at active
 dlanor 'The great court of heaven uses a vast number of languages, but...I have never seen any like THIS.'
 hide dlanor_v001
 with Dissolve(0.2)
 show beatrice_v001 normal_close at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show beatrice_v001 normal_close at inactive
 nao "So from that conclusion, you could say......that this magic circle was like some kid's trick?"
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice 'Mu.'
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice 'But these two magic circles must have been made by different people, correct?'
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice "While the spirals and overlapping circles vary, it's clear that both parties were trying to draw the same magic circle."
 show nao_v002 normal_close at active
 show beatrice_v001 normal at inactive
 nao "In other words, it's possible this magic scribble was made by several people who shared some sort of common knowledge..."
 show beatrice_v001 fuan at active
 show nao_v002 normal_close at inactive
 beatrice "...I....I don't understand. Can you simplify what you're saying....?"
 show nao_v002 smile at active
 show beatrice_v001 fuan at inactive
 nao "I want you to say what I'm about to on your turn. That way, we can both be declared the victors. "
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide beatrice_v001
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 odoroki_close at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 odoroki_close at chara_shake_transform,active
 erika '........Kuuuuuu, why....why do I always lose on Rokkenjimaaaaa........!!'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show dlanor_v001 normal at mei_left
 show beatrice_v001 normal at mei_right
 with Dissolve(0.5)
 show beatrice_v001 normal at active
 show dlanor_v001 normal at inactive
 beatrice 'Dlanor....I would like to listen respectfully to Nao. May I give me turn to her?'
 show dlanor_v001 normal at active
 show beatrice_v001 normal at inactive
 dlanor 'If that is your request, it is FINE.'
 show dlanor_v001 normal at active
 show beatrice_v001 normal at inactive
 dlanor 'NAO. I would also like to hear how Shannon overlooked this magic CIRCLE.'
 hide dlanor_v001
 hide beatrice_v001
 with Dissolve(0.2)
 show erika_v001 odoroki_close at mei_right
 show nao_v002 smile at mei_left
 with Dissolve(0.5)
 show nao_v002 smile at active
 show erika_v001 odoroki_close at inactive
 nao "I wonder if Erika-san feels any detective's compassion."
 show erika_v001 sinken at active
 show nao_v002 smile at inactive
 erika 'Tch. ....lose lose lose lose.....'
 show nao_v002 normal at active
 show erika_v001 sinken at inactive
 nao 'Maybe that summoning circle.....'