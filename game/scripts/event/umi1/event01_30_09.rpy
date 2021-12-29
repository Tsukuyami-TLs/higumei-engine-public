label event01_30_09:
 show black_background onlayer black
 $ event_store.current_event='umi1'
 $ event_store.current_progress=3
 $ event_store.current_chapter='event01_30_09'
 camera:
  anchor (0.5, 0.5)
  pos (960, 540)
 stop sound
 scene #000
 play music 'audio/bgm/BGM_QUEST1_COLLAB2.ogg'
 show expression 'images/bg/AdvBg_2190.png' as bg
 with Dissolve(1.0)
 show erika_v001 normal at mei_left
 show beatrice_v001 normal at mei_right
 with Dissolve(0.5)
 show beatrice_v001 normal at active
 show erika_v001 normal at inactive
 beatrice "It's my turn now. I will attack Erika next."
 show beatrice_v001 normal at active
 show erika_v001 normal at inactive
 beatrice 'Erika argued that Shion was the culprit, correct?'
 show beatrice_v001 normal at active
 show erika_v001 normal at inactive
 beatrice "...If there's something that makes you so sure of that, why don't you show it to me?"
 show erika_v001 normal at active
 show beatrice_v001 normal at inactive
 erika "I'll take up that offer if it's what you desire... however, this {i}will{/i} deliver the final blow, you know?"
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
 dlanor 'Lady Beatrice, do you have no issues in making this MOVE?'
 show nao_v002 normal at active
 show dlanor_v001 normal at inactive
 nao '...I want to know too. Beatrice, if you will.'
 hide nao_v002
 hide dlanor_v001
 with Dissolve(0.2)
 show erika_v001 normal at mei_left
 show beatrice_v001 normal_close at mei_right
 with Dissolve(0.5)
 show beatrice_v001 normal_close at active
 show erika_v001 normal at inactive
 beatrice "Alright, then let's get to the heart of the matter!"
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show beatrice_v001 futeki at active
 show erika_v001 normal at inactive
 beatrice 'Show it to me, Erika! Your evidence that Shion is the culprit!'
 show erika_v001 normal_close at active
 show beatrice_v001 futeki at inactive
 erika 'Very well. I will take this chance to state this.'
 show erika_v001 futeki at active
 show beatrice_v001 futeki at inactive
 erika 'There is clear evidence that Shion-san broke into my room!'
 window hide None
 show black_cover as fade with Dissolve(1.0)
 stop sound
 scene black_cover
 hide beatrice_v001
 with Dissolve(0.3)
 show expression 'images/bg/AdvBg_2281.png' as bg
 with Dissolve(1.0)
 pause 1.0
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show shion_v007 odoroki at mei_center
 with Dissolve(0.5)
 show shion_v007 odoroki at jump_transform,active
 shion 'Huh? Wha-what on earth...!?'
 hide shion_v007
 with Dissolve(0.2)
 narrator 'Since a magic circle had just appeared in her room, I thought Erika-san would have been shaking in fear.'
 narrator 'But suddenly, she burst into laughter and displayed an expression that seemed to say that some fool had fallen into her trap...'
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika 'I do thank you kindly for participating in this charade.'
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
 mion "...What do you mean......? ...It can't be......"
 show shion_v007 sinken at active
 show mion_v008 sinken at inactive
 shion '..............................'
 hide shion_v007
 hide mion_v008
 with Dissolve(0.2)
 narrator "The Sonozaki sisters' faces turned pale. ...Then, does that mean that the summoning circle was Shion-san's doing after all...?!"
 show nao_v002 normal at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show nao_v002 normal at inactive
 erika "Alright, everybody, please wait here for a moment. I'm going to close the curtains."
 show nao_v002 normal at active
 show erika_v001 normal at inactive
 nao '...What are you about to do?'
 show erika_v001 normal at active
 show nao_v002 normal at inactive
 erika 'Shion Sonozaki-san. This way.'
 hide nao_v002
 show shion_v007 normal at mei_left
 with Dissolve(0.5)
 show shion_v007 normal at active
 show erika_v001 normal at inactive
 shion "...Being treated like a criminal is upsetting, but if I refuse, she's just going to suspect me more."
 hide erika_v001
 hide shion_v007
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_229_grap.wav'
 narrator 'As Shion stepped forward... Erika-san grabbed her wrist in a vice-like grip, almost like it was a pair of handcuffs.'
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika 'I do believe this is checkmate, Shion-san?'
 hide erika_v001
 with Dissolve(0.2)
 show nao_v002 sinken at mei_left
 show mion_v008 sinken at mei_right
 with Dissolve(0.5)
 show mion_v008 sinken at active
 show nao_v002 sinken at inactive
 mion "Erika-san, you're suspecting Shion just because she went back to the guesthouse after she told us she forgot her room key, aren't you?!"
 show nao_v002 sinken at active
 show mion_v008 sinken at inactive
 nao "Right. Just because somebody lacks an alibi doesn't necessarily mean that person is the culprit."
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
 erika '<Good!> ...Those words are like music to my ears♪'
 hide erika_v001
 hide shion_v007
 with Dissolve(0.2)
 narrator "I heard the quiet sound of teeth grinding. Shion-san's face... was distorted in disgust."
 play audio 'audio/sfx/SE_5005_grab.wav'
 narrator "Was Erika-san's grip so tight that it hurt? ...Or had her evidence already delivered the fatal blow?"
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
 mion "Hmmm... if you say that you have evidence that Shion did it, then let's see it."
 show mion_v008 normal at active
 show nao_v002 normal at inactive
 mion 'Nao-chan, can you turn off the lights?'
 show nao_v002 normal_close at active
 show mion_v008 normal at inactive
 nao '...Understood.'
 play audio 'audio/sfx/SE_5004_lightoff.wav'
 show black_cover as fade with Dissolve(1.0)
 hide nao_v002
 hide mion_v008
 with Dissolve(0.2)
 play sound ['audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav'] fadeout 1.0
 stop music fadeout 2.0
 stop sound
 scene black_cover
 show expression 'images/bg/AdvBg_2283.png' as bg
 with Dissolve(1.0)
 narrator 'At this time of year, it would get dark quite early in the day. Once the lights were turned off and the curtains were closed, it was pitch black.'
 narrator 'Erika-san immediately turned on the penlight.'
 show mion_v008 normal at mei_center
 with Dissolve(0.5)
 show mion_v008 normal at active
 mion "It looks like a spy gadget. At first glance, it appears to be a fountain pen, but it's able to emit light."
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
 play music 'audio/bgm/BGM_QUEST3_COLLAB2.ogg'
 show erika_v001 normal at active
 erika 'Me mentioning that I forgot to lock my door in front of everybody was all a trap designed to draw in the culprit.'
 show erika_v001 normal at active
 erika 'In order to make the best out of this once-in-a-lifetime chance, the culprit had to make an excuse to go back to the guesthouse.'
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
 mion '...So what was... the secret trap on the doorknob...?'
 hide mion_v008
 hide shion_v007
 with Dissolve(0.2)
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 nao 'Ah... could it be......'
 hide nao_v002
 with Dissolve(0.2)
 narrator "I didn't expect this, but... is it fingerprints? With proper equipment and knowledge, it's not impossible."
 narrator "In addition, Erika-san called herself a detective. Maybe she could identify Shion-san's fingerprints on the doorknob...!"
 show nao_v002 fuan at mei_left
 show erika_v001 normal_close at mei_right
 with Dissolve(0.5)
 show erika_v001 normal_close at active
 show nao_v002 fuan at inactive
 erika 'No, no. I used a simpler, clearer, and more obvious method.'
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
 nao 'This is...'
 show mion_v008 normal at active
 show nao_v002 normal at inactive
 mion 'A blacklight... right?'
 hide mion_v008
 hide nao_v002
 with Dissolve(0.2)
 show erika_v001 normal at mei_right
 show shion_v007 fuan at mei_left
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_5005_grab.wav'
 show shion_v007 fuan at chara_shake_transform,active
 show erika_v001 normal at inactive
 shion '...Hey, that hurts... Can you please grip me a little more gently?'
 show erika_v001 normal at active
 show shion_v007 fuan at inactive
 erika 'Nao-chama, can you please shine that blacklight on my palms?'
 hide erika_v001
 hide shion_v007
 with Dissolve(0.2)
 show nao_v002 odoroki at mei_center
 with Dissolve(0.5)
 show nao_v002 odoroki at active
 nao 'Like this? ......Ah.'
 hide nao_v002
 with Dissolve(0.2)
 show erika_v001 normal at mei_right
 show shion_v007 sinken at mei_left
 with Dissolve(0.5)
 show shion_v007 sinken at active
 show erika_v001 normal at inactive
 shion "...Tch. ...You've been carrying that around since before you came here, haven't you...?"
 show erika_v001 normal at active
 show shion_v007 sinken at inactive
 erika "That's because I'm a detective. Even when I'm on vacation, I will at the very least bring a detective's kit with me."
 hide erika_v001
 hide shion_v007
 with Dissolve(0.2)
 show mion_v008 normal at mei_center
 with Dissolve(0.5)
 show mion_v008 normal at active
 mion '...Fluorescent... paint...'
 hide mion_v008
 with Dissolve(0.2)
 narrator "I shined the blacklight on Erika-san's palms... and thin streaks of yellowish-green glimmered in the light..."
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
 shion '...Gh......'
 show erika_v001 normal_close at active
 show shion_v007 sinken at inactive
 erika "I was the one who made this special chemical mixture. A certain chemical compound is required to remove it. Don't worry, naturally I brought it with me."
 show shion_v007 sinken at active
 show erika_v001 normal_close at inactive
 shion "...Isn't that wonderful? In other words, this means that no matter how many showers I take, I will still have that fluorescent paint on my hands?"
 show erika_v001 normal at active
 show shion_v007 sinken at inactive
 erika "Exactly. Now, I'm going to look at your palms under the blacklight."
 show erika_v001 normal at active
 show shion_v007 sinken at inactive
 erika "However... I'll give you mercy as a detective. Rather than disgracing you by confronting you with lethal evidence, I'll give you the chance for a gentleman's loss and admit defeat yourself. "
 show shion_v007 normal_close at active
 show erika_v001 normal at inactive
 shion "...I don't know what's up with you playing detective... but if it involves victory and defeat..."
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide shion_v007
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 show mion_v008 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show mion_v008 sinken at active
 mion "...The Sonozaki sisters... defintely won't lose. ...We'll prove to you that even though it's been split between the two of us, the blood of the next head flows hot and thick through our veins!"
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide mion_v008
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika "You are the culprit, Shion-san. Despite this, you think this will result in my loss? I don't get what you're saying at all."
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 camera at screenshake_transform
 pause 0.0
 show erika_v001 fuan at active
 erika "Now, the time for pity is over!! Show me your palms!! I'll light them up niiiice and bright for youuuuuuuuu!!!!! Uehehehehehehehehehe!!!!"
 stop music fadeout 0.5
 window hide None
 show black_cover as fade with Dissolve(1.0)
 hide erika_v001
 with Dissolve(0.2)
 pause 1.0
 stop sound
 scene black_cover
 play music 'audio/bgm/BGM_BOSS1_COLLAB2.ogg'
 camera:
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
 erika 'Wait, what? Le-let me check agai--...!!'
 show dlanor_v001 normal at active
 show erika_v001 odoroki at inactive
 dlanor "Shion Sonozaki's hands do not have any florescent paint on THEM. "
 show erika_v001 sinken at active
 show dlanor_v001 normal at inactive
 erika 'What the hell are you talking about?! Check her again!!!'
 show dlanor_v001 normal at active
 show erika_v001 sinken at inactive
 dlanor "It's not just her HANDS. Shion Sonozaki's body does not have any fluorescent paint on IT. "
 camera at screenshake_transform
 pause 0.0
 show erika_v001 odoroki at active
 show dlanor_v001 normal at inactive
 erika "WHAT DO YOU MEEEEEEEEEEEAAAAAAANNN????!!!!! YOU'D BETTER SAY IT IN REEEEEEEEEEEEDDDDDDD!!!!!! "
 show dlanor_v001 normal at active
 show erika_v001 odoroki at inactive
 dlanor 'I will repeat it in RED.'
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide dlanor_v001
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 show dlanor_v001 normal at mei_center
 with Dissolve(0.08333333333333333)
 show red_cover as fade with Dissolve(0.16666666666666666)
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 hide fade with Dissolve(0.16666666666666666)
 with Dissolve(0.16666666666666666)
 show dlanor_v001 normal at active
 dlanor "{umi_red}Shion Sonozaki's body does not have any fluorescent paint on IT.{/umi_red}"
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
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
 erika "N-nonononono, this, this couldn't be!!!! T-there's no way!!!! This is impossible!!!!"
 hide dlanor_v001
 show beatrice_v001 futeki at mei_right
 with Dissolve(0.5)
 show beatrice_v001 futeki at active
 show erika_v001 odoroki at inactive
 beatrice "Hm? Isn't this strange, Erika? Wouldn't this make this... the work of a witch?"
 camera at screenshake_transform
 pause 0.0
 show erika_v001 sinken at active
 show beatrice_v001 futeki at inactive
 erika 'Shut up shut up!!! ShutupshutupshutupSHUT UUUUUUUUUUUUUUUUUUUPPPPPPPP!!!!!!'
 hide erika_v001
 hide beatrice_v001
 with Dissolve(0.2)
 narrator "With that, Beatrice's turn was over. Next was Erika-san's turn, which would probably be used trying to recover."
 narrator 'Right now, Erika-san was shaking after receiving such a powerful blow. That meant my next turn was crucial...!'
 show erika_v001 sinken at mei_left
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show erika_v001 sinken at inactive
 dlanor 'ERIKA. This is a game for ladies and GENTLEMEN. Please refrain from using vulgar SPEECH.'
 show erika_v001 sinken at chara_shake_transform,active
 show dlanor_v001 normal at inactive
 erika "SHUUUUUUUUT THE HELLLLLL UUUUUP, YOU MURDER DOLL!!! IT'S MY TURN NOW!!"
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
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
 show white_cover as flash with Dissolve(0.1)
 pause 0.1
 hide flash with Dissolve(0.2)
 show erika_v001 sinken at active
 erika "{umi_blue}Shion Sonozaki used a glove when she touched the doorknob! Naturally, this means the fluorescent paint wasn't able to get on her palms!{/umi_blue}"
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show dlanor_v001 normal_close at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal_close at active
 dlanor '...EFFECTIVE.'
 window hide None
 show black_cover as fade with Dissolve(1.0)
 hide dlanor_v001
 with Dissolve(0.2)
 stop sound
 scene black_cover
 show expression 'images/bg/AdvBg_2281.png' as bg
 with Dissolve(1.0)
 show erika_v001 futeki at mei_center
 with Dissolve(0.5)
 show erika_v001 futeki at active
 erika "See?! It's possible for somebody to open the door to the room without getting my fluorescent paint on them!"
 show erika_v001 fuan at active
 erika 'Shion-san, you truly are a despicable woman...!!!'
 camera at screenshake_transform
 pause 0.0
 show erika_v001 fuan at active
 erika "I can't believe you'd be this cautious when breaking into somebody's room. You're a professional!! A career criminal!!!! <A superior extreme feloooooooooooon!!!!!!>"
 hide erika_v001
 with Dissolve(0.2)
 show mion_v008 normal at mei_right
 show shion_v007 normal_close at mei_left
 with Dissolve(0.5)
 show shion_v007 normal_close at active
 show mion_v008 normal at inactive
 shion "You can say whatever you want about me. And by the way, I'd consider what you just said to be a compliment."
 show mion_v008 normal at active
 show shion_v007 normal_close at inactive
 mion "...Shion definitely doesn't have an alibi, but... doesn't that prove she didn't enter your room?"
 hide mion_v008
 hide shion_v007
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao "If you're still sure that Shion-san is the culprit, I want you to show something besides that."
 show black_cover as fade with Dissolve(1.0)
 hide nao_v002
 with Dissolve(0.2)
 stop sound
 scene black_cover
 show expression 'images/bg/AdvBg_2190.png' as bg
 with Dissolve(1.0)
 show erika_v001 odoroki at mei_center
 with Dissolve(0.5)
 show erika_v001 odoroki at active
 erika 'Something besides that, something besides that... aaahh... aaaaahhhhh... ...aaaaaaAAAAHHH!'
 show erika_v001 odoroki_close at chara_shake_transform,active
 erika "It's fine, my master...! My reasoning is flawless. Aaaaaahhh, so don't get mad, don't get mad..."
 hide erika_v001
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_left
 show beatrice_v001 smile at mei_right
 with Dissolve(0.5)
 show beatrice_v001 smile at active
 show dlanor_v001 normal at inactive
 beatrice "The next turn is Nao's. You probably won't have any issues going forward, right?"
 show dlanor_v001 normal at active
 show beatrice_v001 smile at inactive
 dlanor 'Now, NAO. It is your TURN.'
 hide dlanor_v001
 hide beatrice_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao "Um, I'd like to come out with some information."
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show erika_v001 odoroki at active
 erika 'Huh...?!'
 show erika_v001 sinken at active
 erika 'What could a detestable, tasteless child who has no redeeming factors other than hating to lose {i}POSSIBLY{/i} come out with now?!?!'
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
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
 beatrice 'Nao, what on earth could you be confessing to doing...?'
 show nao_v002 normal_close at active
 show beatrice_v001 normal at inactive
 nao "I am Nao Houtani. ...I consider myself a normal human... but the truth is, I've had strange experiences that nobody would believe were real if I were to mention them."
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao 'I have physically encountered paranormal phenomena such as gods and "Tsukuyami", and know firsthand that this world doesn\'t just contain what Humans think it does.'
 show beatrice_v001 odoroki at active
 show nao_v002 normal at inactive
 beatrice '...What the... are you... a Voyager witch...!?'
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
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
 erika "There's no WAY that's truee!!! You're just a teensy, {i}tiny{/i}, little insignificant dumpster diveeeeeeerrrrrrr!!!!!"
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
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
 narrator "I whisper into Dlanor's ear."
 show nao_v002 normal at mei_left
 show dlanor_v001 odoroki at mei_right
 with Dissolve(0.5)
 show dlanor_v001 odoroki at active
 show nao_v002 normal at inactive
 dlanor '...I-I UNDERSTAND. ...However, in order to do that, I will need to see your HAND.'
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
 dlanor 'Of course, I will only need to observe that which is involved with your red TRUTH. Furthermore, it is through my oath of confidentiality with the Great Court of Heaven that I shall never reveal any other truths I have LEARNED.'
 show nao_v002 normal at active
 show dlanor_v001 normal at inactive
 nao "...You mean she wants to look inside my head? I don't mind."
 show dlanor_v001 sinken at active
 show nao_v002 normal at inactive
 dlanor 'With that... please excuse ME...'
 hide nao_v002
 hide dlanor_v001
 with Dissolve(0.2)
 narrator "Dlanor-san's eyes turned almost see-through as they emitted a faint light."
 narrator 'All she was doing was staring at me... but it gave me a strange, uncomfortable feeling.'
 narrator '...I see. That was what she meant when she said she wanted to look at my hand.'
 narrator 'The uncomfortable feeling was as though everything I had ever experienced in my life, my thoughts, my feelings, my emotions, and everything else, was all being watched by another person.'
 show beatrice_v001 normal at mei_right
 show dlanor_v001 normal_close at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal_close at active
 show beatrice_v001 normal at inactive
 dlanor '...NAO. Thank you very MUCH. I am FINISHED.'
 show beatrice_v001 normal at active
 show dlanor_v001 normal_close at inactive
 beatrice "And with that... Dlanor's verdict is..."
 show dlanor_v001 normal at active
 show beatrice_v001 normal at inactive
 dlanor 'EFFECTIVE.'
 show red_cover as fade with Dissolve(0.16666666666666666)
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 hide fade with Dissolve(0.16666666666666666)
 with Dissolve(0.16666666666666666)
 show dlanor_v001 normal at active
 show beatrice_v001 normal at inactive
 dlanor '{umi_red}Nao Houtani has been confirmed to have made contact and interacted with inhuman BEINGS.{/umi_red}'
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide beatrice_v001
 hide dlanor_v001
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 sinken at active
 erika 'W... who the hell are you?! I thought you were just some bratty kid I happened to meet on the ferry...!?'
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
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
 beatrice "Didn't your master once say that black tea is best enjoyed with monsters?"
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice '...I see. If a witch opens up the game board, witches, monsters, and similar beings may be invited in...'
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao 'All kinds of mysterious entities, such as ghosts and gods, exist in this world.'
 show nao_v002 normal_close at active
 show beatrice_v001 normal at inactive
 nao "Because of that, I don't deny Beatrice's existence. Her being here is proof enough."
 show beatrice_v001 odoroki at active
 show nao_v002 normal_close at inactive
 beatrice "Y-you recognize my existence... Nao, I've never had a guest such as yourself..."
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
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
 show white_cover as flash with Dissolve(0.1)
 pause 0.1
 hide flash with Dissolve(0.2)
 show nao_v002 normal at active
 nao '{umi_blue}The suspect Shion-san is innocent.{/umi_blue}'
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
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
 erika "That's impossible, totally impossible!!!!! Shion is the culprit!!!! She's definitely the culpriiiiiiiit!!!!!"
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.1
 pause 0.5
 play audio 'audio/sfx/SE_391_ls_swing.wav'
 show nao_v002 normal at active
 show erika_v001 odoroki at inactive
 nao '{umi_blue}Erika put a "Bedmaking Not Necessary" tag on her doorknob so that the servants would not enter her room.{/umi_blue}'
 camera:
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
 nao "{umi_blue}Because of this, the only person who would be able to get into the room would be Shion-san, who, despite Erika's traps, was able to prove her innocence.{/umi_blue}"
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 play audio 'audio/sfx/SE_5036_glass_break.wav'
 show white_cover as flash with Dissolve(0.1)
 pause 0.1
 hide flash with Dissolve(0.2)
 show nao_v002 sinken at active
 show erika_v001 odoroki at inactive
 nao "{umi_blue}So therefore, the second magic circle was impossible for a Human to make, so it's clearly a witch's prank.{/umi_blue}"
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
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
 erika "That's not clear at alllllllll!!! Who did it, and where did they come from!?!?!? Don't make a mockery of the blue truuuuuuuth!!!"
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
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
 beatrice "...Nao, you realize I'll benefit from this? Are you trying to lose...?"
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
 dlanor 'It is EFFECTIVE. ...In return, Erika must submit either a red truth, equivalent evidence, or a REBUTTAL.'
 hide nao_v002
 show erika_v001 sinken_close at mei_left
 with Dissolve(0.5)
 show erika_v001 sinken_close at active
 show dlanor_v001 normal at inactive
 erika '...............ay...'
 show dlanor_v001 normal at active
 show erika_v001 sinken_close at inactive
 dlanor '...I did not hear THAT. Please repeat YOURSELF.'
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
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
 erika 'No way... nowaynowaynowaaaaaaaaayy! Shion is absolutely, positively, certainly guilty... so why... so why is there no evidence...anywhere?!?!'
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 narrator 'It seemed that Erika-san went all in on her gambit with the fluorescent paint on the doorknob.'
 narrator 'She had lost the card that was supposed to be her ace in the hole... and was now waiting for the count-out. '
 show nao_v002 normal at mei_left
 show beatrice_v001 normal_close at mei_right
 with Dissolve(0.5)
 show beatrice_v001 normal_close at active
 show nao_v002 normal at inactive
 beatrice 'Nao. Your turn is now over...'
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice "...I'm up next. By using the blue truth you have established, I will be able to claim victory... are you okay with this?"
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao "I'd like to negotiate."
 show beatrice_v001 smile at active
 show nao_v002 normal at inactive
 beatrice "Hoh? Since you're letting me win, I will listen to what you have to say."
 show nao_v002 normal at active
 show beatrice_v001 smile at inactive
 nao 'The next turn is yours, but before you declare your victory, I want you to make one move for me.'
 show nao_v002 normal at active
 show beatrice_v001 smile at inactive
 nao "While the second magic circle is a witch's deed, Erika-san was the culprit for the first one. And just now, it finally occured to me why Shannon-san didn't feel anything strange when she found it."
 hide nao_v002
 hide beatrice_v001
 with Dissolve(0.2)
 narrator 'At last, the soup of logic, reasoning, and mystery... had finished thickening.'
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
 nao "Because of that, you're an expert in all sorts of spells and rituals, correct? Which of course would also include magic circles."
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice 'Mhm. I hold the title of Endless Witch. There is nothing I do not know.'
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao 'Since you just said that, I want you to look at both the first and second magic circles.'
 window hide None
 show black_cover as fade with Dissolve(1.0)
 hide beatrice_v001
 hide nao_v002
 with Dissolve(0.2)
 camera:
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
 beatrice "...Even so, I don't understand this circle... I don't know what it's used for."
 window hide None
 show black_cover as fade with Dissolve(1.0)
 hide beatrice_v001
 with Dissolve(0.2)
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 camera at reset_shader
 pause 0.0
 hide fade with Dissolve(1.0)
 with Dissolve(1.0)
 narrator "That itself was an explanation. Perhaps it wasn't a magic circle at all."
 narrator "That line of reasoning explains... why Shannon-san didn't see it as strange, and why Mion-san and Shion-san didn't seem to be too shocked when they saw it...!!"
 show beatrice_v001 normal at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao 'Can you please give us a more detailed explanation?'
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice 'Mhm... The shapes of a magic circle can roughly describe things like its core and the flow of energy through it...'
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice "...This circle looks like it's gathering magical energy from outside of it, but in reality it just passes through the circle without being collected, so it doesn't look like it has any meaning in particular. "
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao "So in the eyes of the Great Witch called Lady Beatrice... the magic circle doesn't make any sense at all?"
 show beatrice_v001 normal_close at active
 show nao_v002 normal at inactive
 beatrice 'Nope. ...This thing that appears to be a magic circle is an illegible fake.'
 hide beatrice_v001
 hide nao_v002
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 dlanor 'I am a Reader, so I have kept silent... but I have never seen the letters on the circumference of the summoning circle BEFORE.'
 show dlanor_v001 normal at active
 dlanor 'The Great Court of Heaven uses a vast number of languages... but I have never seen any like THIS.'
 hide dlanor_v001
 with Dissolve(0.2)
 show beatrice_v001 normal_close at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show beatrice_v001 normal_close at inactive
 nao "So from that conclusion, you could say... that this magic circle was child's play?"
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice 'Mhm.'
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice 'But these two magic circles must have been made by different people, correct?'
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice "While the spirals and overlapping circles vary, it's clear that both parties were trying to draw the same magic circle."
 show nao_v002 normal_close at active
 show beatrice_v001 normal at inactive
 nao "So in essence, it's possible this magic scribble was made by several people who shared some sort of common knowledge..."
 show beatrice_v001 fuan at active
 show nao_v002 normal_close at inactive
 beatrice "...I... I don't understand what you mean. Can you simplify what you're saying...?"
 show nao_v002 smile at active
 show beatrice_v001 fuan at inactive
 nao "I want you to say what I'm about to on your turn. That way, we can both be declared the victors. "
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide beatrice_v001
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 odoroki_close at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 odoroki_close at chara_shake_transform,active
 erika '...Nnnnnnnggghhh...... why... why do I always lose on Rokkenjimaaaaa...!!'
 show black_cover as fade with Dissolve(0.3333333333333333)
 camera:
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
 beatrice 'Dlanor... I would like to respectfully listen to Nao. May I give my turn to her?'
 show dlanor_v001 normal at active
 show beatrice_v001 normal at inactive
 dlanor 'If that is your request, then it is FINE.'
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
 nao 'Mercy as a detective, huh, Erika-san?'
 show erika_v001 sinken at active
 show nao_v002 smile at inactive
 erika 'Tch. ...Iost, lost... I lost...'
 show nao_v002 normal at active
 show erika_v001 sinken at inactive
 nao 'Maybe that summoning circle...'
 call chapter_end
 call event01_30_10