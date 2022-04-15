label event01_30_09:
 show black_background onlayer black
 $ event_store.current_event='umi1'
 $ event_store.current_progress=4
 $ event_store.current_chapter='event01_30_09'
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
 show expression 'images/bg/AdvBg_2190.png' as bg
 play music "<loop 0>audio/bgm/BGM_QUEST1_COLLAB2.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show beatrice_v001 normal at mei_right
 show erika_v001 normal at mei_left
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "It's my turn now. I will attack Erika next."
 show erika_v001 normal at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Erika argued that Shion was the culprit, correct?'
 show erika_v001 normal at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "...If there's something that makes you so sure of that, why don't you show it to me?"
 show beatrice_v001 normal at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "I'll take up that offer if it's what you desire... however, this {i}will{/i} deliver the final blow, you know?"
 hide erika_v001
 hide beatrice_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "It's true that Shion-san was the only one to go back to search for something at the guesthouse, and thus lost an alibi..."
 hide nao_v002
 with Dissolve(0.2)
 narrator "But I don't want to let Shion-san be declared the culprit just because she doesn't have an alibi. "
 show dlanor_v001 normal at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'Lady Beatrice, do you have no issues in making this MOVE?'
 show dlanor_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...I want to know too. Beatrice, if you will.'
 hide nao_v002
 hide dlanor_v001
 with Dissolve(0.2)
 show beatrice_v001 normal_close at mei_right
 show erika_v001 normal at mei_left
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show beatrice_v001 normal_close at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "Alright, then let's get to the heart of the matter!"
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show erika_v001 normal at inactive
 show beatrice_v001 futeki at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Show it to me, Erika! Your evidence that Shion is the culprit!'
 show beatrice_v001 futeki at inactive
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Very well. I will take this chance to state this.'
 show beatrice_v001 futeki at inactive
 show erika_v001 futeki at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'There is clear evidence that Shion-san broke into my room!'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_2281.png' as bg
 hide beatrice_v001
 with Dissolve(0.3)
 hide fade onlayer curtain
 with Dissolve(1.0)
 pause 1.0
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show shion_v007 odoroki at mei_center
 with Dissolve(0.5)
 show shion_v007 odoroki at active
 show shion_v007 odoroki at jump_transform
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Huh? W-What on earth...!?'
 hide shion_v007
 with Dissolve(0.2)
 narrator 'Since a magic circle had just appeared in her room, I thought Erika-san would have been shaking in fear.'
 narrator 'But suddenly, she burst into laughter and displayed an expression that seemed to say that some fool had fallen into her trap...'
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'I do thank you kindly for participating in this charade.'
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Now, let's look at the details."
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'One moment ago, everybody heard me scream and entered via the open door.'
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "In other words, none of you should have touched this room's doorknob."
 hide erika_v001
 with Dissolve(0.2)
 show mion_v008 sinken at mei_right
 show shion_v007 sinken at mei_left
 with Dissolve(0.5)
 show shion_v007 sinken at inactive
 show mion_v008 sinken at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...What do you mean......? ...It can't be......"
 show mion_v008 sinken at inactive
 show shion_v007 sinken at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") '..............................'
 hide shion_v007
 hide mion_v008
 with Dissolve(0.2)
 narrator "The Sonozaki sisters' faces turned pale. ...Then, does that mean that the summoning circle was Shion-san's doing after all...?!"
 show erika_v001 normal at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Alright, everybody, please wait here for a moment. I'm going to close the curtains."
 show erika_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...What are you about to do?'
 show nao_v002 normal at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Shion Sonozaki-san. This way.'
 hide nao_v002
 show shion_v007 normal at mei_left
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show shion_v007 normal at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...Being treated like a criminal is upsetting, but if I refuse, she's just going to suspect me more."
 hide erika_v001
 hide shion_v007
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_229_grap.wav'
 narrator 'As Shion-san stepped forward... Erika-san grabbed her wrist in a vice-like grip, almost like it was a pair of handcuffs.'
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'I do believe this is checkmate, Shion-san?'
 hide erika_v001
 with Dissolve(0.2)
 show mion_v008 sinken at mei_right
 show nao_v002 sinken at mei_left
 with Dissolve(0.5)
 show nao_v002 sinken at inactive
 show mion_v008 sinken at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Erika-san, you're suspecting Shion just because she went back to the guesthouse after she told us she forgot her room key, aren't you?!"
 show mion_v008 sinken at inactive
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Right. Just because somebody lacks an alibi doesn't necessarily mean that person is the culprit."
 hide nao_v002
 hide mion_v008
 with Dissolve(0.2)
 show shion_v007 sinken at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show shion_v007 sinken at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "I didn't enter that room. If you want to say otherwise, then please show me the evidence!"
 show shion_v007 sinken at inactive
 show erika_v001 smile at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") '<Good!> ...Those words are like music to my ears♪'
 hide erika_v001
 hide shion_v007
 with Dissolve(0.2)
 narrator "I heard the quiet sound of teeth grinding. Shion-san's face... was distorted in disgust."
 play audio 'audio/sfx/SE_5005_grab.wav'
 narrator "Was Erika-san's grip so tight that it hurt? ...Or had her evidence already delivered the fatal blow?"
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Nao-chama, can you please turn off the lights in this room? It'll be fine; I have a penlight."
 hide erika_v001
 with Dissolve(0.2)
 narrator "She called it a penlight, but from an outsider's perspective, it looked like a rather plump fountain pen."
 narrator 'However, when Erika-san fiddled with it using her free hand, it became clear that it did indeed have a light function...'
 show mion_v008 sinken at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show mion_v008 sinken at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Hmmm... if you say that you have evidence that Shion did it, then let's see it."
 show nao_v002 normal at inactive
 show mion_v008 normal at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Nao-chan, can you turn off the lights?'
 show mion_v008 normal at inactive
 show nao_v002 normal_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Understood.'
 play audio 'audio/sfx/SE_5004_lightoff.wav'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide nao_v002
 hide mion_v008
 with Dissolve(0.2)
 play sound ['audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav'] fadeout 1.0
 stop music fadeout 2.0
 stop sound
 show expression 'images/bg/AdvBg_2283.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator 'At this time of year, it would get dark quite early in the day. Once the lights were turned off and the curtains were closed, it was pitch black.'
 narrator 'Erika-san immediately turned on the penlight.'
 show mion_v008 normal at mei_center
 with Dissolve(0.5)
 show mion_v008 normal at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "It looks like a spy gadget. At first glance, it appears to be a fountain pen, but it's able to emit light."
 show mion_v008 normal at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'I bet it has other hidden features.'
 hide mion_v008
 with Dissolve(0.2)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "You've got a discerning eye. Naturally, this isn't the penlight's only feature."
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Before explaining its features, let me reveal the secret behind this doorknob.'
 play music "<loop 0>audio/bgm/BGM_QUEST3_COLLAB2.ogg"
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Me mentioning that I forgot to lock my door in front of everybody was all a trap designed to draw in the culprit.'
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'In order to make the best out of this once-in-a-lifetime chance, the culprit had to make an excuse to go back to the guesthouse.'
 hide erika_v001
 with Dissolve(0.2)
 show shion_v007 sinken at mei_left
 show mion_v008 sinken at mei_right
 with Dissolve(0.5)
 show mion_v008 sinken at inactive
 show shion_v007 sinken at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "I only came back in order to look for some photography equipment. I didn't do anything like enter your room!"
 show shion_v007 sinken at inactive
 show mion_v008 sinken at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") '...So what was... the secret trap on the doorknob...?'
 hide mion_v008
 hide shion_v007
 with Dissolve(0.2)
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Ah... could it be......'
 hide nao_v002
 with Dissolve(0.2)
 narrator "I didn't expect this, but... is it fingerprints? With proper equipment and knowledge, it's not impossible."
 narrator "In addition, Erika-san called herself a detective. Maybe she could identify Shion-san's fingerprints on the doorknob...!"
 show erika_v001 normal_close at mei_right
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at inactive
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'No, no. I used a simpler, clearer, and more obvious method.'
 show nao_v002 fuan at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Nao-chama. Can you hold this penlight?'
 show erika_v001 normal at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Huh? Okay...'
 show nao_v002 fuan at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Twist it here until there's a click."
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 narrator "As I did as I was told, the penlight's light went out, and was replaced by a faint blue-purple glow."
 show nao_v002 normal at mei_left
 show mion_v008 normal at mei_right
 with Dissolve(0.5)
 show mion_v008 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'This is...'
 show nao_v002 normal at inactive
 show mion_v008 normal at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'A blacklight... right?'
 hide mion_v008
 hide nao_v002
 with Dissolve(0.2)
 show shion_v007 fuan at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_5005_grab.wav'
 show erika_v001 normal at inactive
 show shion_v007 fuan at active
 show shion_v007 fuan at chara_shake_transform
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") '...Hey, that hurts... Can you please grip me a little more gently?'
 show shion_v007 fuan at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Nao-chama, can you please shine that blacklight on my palms?'
 hide erika_v001
 hide shion_v007
 with Dissolve(0.2)
 show nao_v002 odoroki at mei_center
 with Dissolve(0.5)
 show nao_v002 odoroki at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Like this? ......Ah.'
 hide nao_v002
 with Dissolve(0.2)
 show shion_v007 sinken at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show shion_v007 sinken at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...Tch. ...You've been carrying that around since before you came here, haven't you...?"
 show shion_v007 sinken at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "That's because I'm a detective. Even when I'm on vacation, I will at the very least bring a detective's kit with me."
 hide erika_v001
 hide shion_v007
 with Dissolve(0.2)
 show mion_v008 normal at mei_center
 with Dissolve(0.5)
 show mion_v008 normal at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") '...Fluorescent... paint...'
 hide mion_v008
 with Dissolve(0.2)
 narrator "I shined the blacklight on Erika-san's palms... and thin streaks of yellowish-green glimmered in the light..."
 show erika_v001 normal at mei_right
 show shion_v007 sinken at mei_left
 with Dissolve(0.5)
 show shion_v007 sinken at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "I painted this room's doorknob this morning."
 show shion_v007 sinken at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'This paint is specially formulated to stick to the hands of whoever touches the doorknob for the whole day.'
 show shion_v007 sinken at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Furthermore, once the paint has adhered to you, it cannot be removed by washing it off.'
 camera at screenshake_transform
 pause 0.0
 show erika_v001 normal at inactive
 show shion_v007 sinken at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") '...Gh......'
 show shion_v007 sinken at inactive
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'I was the one who made this special chemical mixture. A certain chemical compound is required to remove it. Of course, I did bring it with me, so rest assured.'
 show erika_v001 normal_close at inactive
 show shion_v007 sinken at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...Isn't that wonderful? So this means that no matter how many showers I take, I will still have that fluorescent paint on my hands?"
 show shion_v007 sinken at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Exactly. Now, I'm going to look at your palms under the blacklight."
 show shion_v007 sinken at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "However... I'll give you my sympathy as a detective. Rather than disgracing you by confronting you with lethal evidence, I'll give you the chance for a gentleman's loss and admit defeat yourself. "
 show erika_v001 normal at inactive
 show shion_v007 normal_close at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...I don't know what's up with you playing detective... but if it involves victory and defeat..."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide shion_v007
 hide erika_v001
 hide fade onlayer curtain
 show mion_v008 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show mion_v008 sinken at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...The Sonozaki sisters... defintely won't lose. ...We'll prove to you that even though it's been split between the two of us, the blood of the next head flows hot and thick through our veins!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide mion_v008
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "You are the culprit, Shion-san. Despite this, you think this will result in my loss? I don't get what you're saying at all."
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 camera at screenshake_transform
 pause 0.0
 show erika_v001 fuan at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Now, the time for pity is over!! Show me your palms!! I'll light them up niiiice and bright for youuuuuuuuu!!!!! Uehehehehehehehehehe!!!!"
 stop music fadeout 0.5
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide erika_v001
 with Dissolve(0.2)
 pause 1.0
 stop sound
 show expression 'images/bg/AdvBg_2190.png' as bg
 play music "<loop 0>audio/bgm/BGM_BOSS1_COLLAB2.ogg"
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 hide fade onlayer curtain
 with Dissolve(1.0)
 show erika_v001 odoroki at mei_left
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 show dlanor_v001 normal at inactive
 show erika_v001 odoroki at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Wait, what? L-Let me check agai--...!!'
 show erika_v001 odoroki at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") "Shion Sonozaki's hands do not have any florescent paint on THEM. "
 show dlanor_v001 normal at inactive
 show erika_v001 sinken at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "What the hell are you talking about?! Let's check her again!!!"
 show erika_v001 sinken at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") "It's not just her HANDS. Shion Sonozaki's body does not have any fluorescent paint on IT. "
 camera at screenshake_transform
 pause 0.0
 show dlanor_v001 normal at inactive
 show erika_v001 odoroki at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "WHAT DO YOU MEEEEEEEEEEEAAAAAAANNN????!!!!! \nYOU'D BETTER SAY IT IN REEEEEEEEEEEEDDDDDDD!!!!!! "
 show erika_v001 odoroki at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'I will repeat it in RED.'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide dlanor_v001
 hide erika_v001
 hide fade onlayer curtain
 show dlanor_v001 normal at mei_center
 with Dissolve(0.08333333333333333)
 show red_cover onlayer curtain as fade with Dissolve(0.16666666666666666)
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 hide fade onlayer curtain
 with Dissolve(0.16666666666666666)
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") "{umi_red}Shion Sonozaki's body does not have any fluorescent paint on IT.{/umi_red}"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide dlanor_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show erika_v001 odoroki at mei_left
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 camera at screenshake_transform
 pause 0.0
 show dlanor_v001 normal at inactive
 show erika_v001 odoroki at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "N-Nonononono, this, this couldn't be!!!! T-There's no way!!!! This is impossible!!!!"
 hide dlanor_v001
 show beatrice_v001 futeki at mei_right
 with Dissolve(0.5)
 show erika_v001 odoroki at inactive
 show beatrice_v001 futeki at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "Hm? Isn't this strange, Erika? Wouldn't this make this... the work of a witch?"
 camera at screenshake_transform
 pause 0.0
 show beatrice_v001 futeki at inactive
 show erika_v001 sinken at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Shut up shut up!!! ShutupshutupshutupSHUT UUUUUUUUUUUUUUUUUUUPPPPPPPP!!!!!!'
 hide erika_v001
 hide beatrice_v001
 with Dissolve(0.2)
 narrator "With that, Beatrice's turn was over. Next was Erika-san's turn, which would probably be used trying to recover."
 narrator 'Right now, Erika-san was shaking after receiving such a powerful blow. That meant my next turn was crucial...!'
 show dlanor_v001 normal at mei_right
 show erika_v001 sinken at mei_left
 with Dissolve(0.5)
 show erika_v001 sinken at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'ERIKA. This is a game for ladies and GENTLEMEN. Please refrain from using vulgar SPEECH.'
 show dlanor_v001 normal at inactive
 show erika_v001 sinken at active
 show erika_v001 sinken at chara_shake_transform
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "SHUUUUUUUUT THE HELLLLLL UUUUUP, YOU MURDER DOLL!!! IT'S MY TURN NOW!!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide erika_v001
 hide dlanor_v001
 hide fade onlayer curtain
 show erika_v001 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 sinken at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Blue truth!'
 play audio 'audio/sfx/SE_391_ls_swing.wav'
 show white_cover as flash with Dissolve(0.1)
 pause 0.1
 hide flash with Dissolve(0.2)
 show erika_v001 sinken at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "{umi_blue}Shion Sonozaki used a glove when she touched the doorknob! Naturally, this means the fluorescent paint wasn't able to get on her palms!{/umi_blue}"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show dlanor_v001 normal_close at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal_close at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") '...EFFECTIVE.'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide dlanor_v001
 with Dissolve(0.2)
 stop sound
 show expression 'images/bg/AdvBg_2281.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 show erika_v001 futeki at mei_center
 with Dissolve(0.5)
 show erika_v001 futeki at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "See?! It's possible for somebody to open the door to the room without getting my fluorescent paint on them!"
 show erika_v001 fuan at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Shion-san, you truly are a despicable woman...!!!'
 camera at screenshake_transform
 pause 0.0
 show erika_v001 fuan at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "I can't believe you'd be this cautious when breaking into somebody's room. You're a professional!! A career criminal!!!! \n<A superior extreme feloooooooooooon!!!!!!>"
 hide erika_v001
 with Dissolve(0.2)
 show shion_v007 normal_close at mei_left
 show mion_v008 normal at mei_right
 with Dissolve(0.5)
 show mion_v008 normal at inactive
 show shion_v007 normal_close at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "You can say whatever you want about me. And by the way, I'd consider what you just said to be a compliment."
 show shion_v007 normal_close at inactive
 show mion_v008 normal at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...Shion definitely doesn't have an alibi... but doesn't that prove she didn't enter your room?"
 hide mion_v008
 hide shion_v007
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "If you're still sure that Shion-san is the culprit, I want you to show something besides that."
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide nao_v002
 with Dissolve(0.2)
 stop sound
 show expression 'images/bg/AdvBg_2190.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 show erika_v001 odoroki at mei_center
 with Dissolve(0.5)
 show erika_v001 odoroki at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Something besides that, something besides that... aaahh... aaaaahhhhh... ...aaaaaaAAAAHHH!'
 show erika_v001 odoroki_close at active
 show erika_v001 odoroki_close at chara_shake_transform
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "It's fine, my master...! My reasoning is flawless. Aaaaaahhh, so don't get mad, don't get mad..."
 hide erika_v001
 with Dissolve(0.2)
 show beatrice_v001 smile at mei_right
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "The next turn is Nao's. You probably won't have any issues going forward, right?"
 show beatrice_v001 smile at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'Please, NAO. It is your TURN.'
 hide dlanor_v001
 hide beatrice_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Um, I'd like to come out with some information."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide nao_v002
 hide fade onlayer curtain
 show erika_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show erika_v001 odoroki at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Huh...?!'
 show erika_v001 sinken at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'What could a detestable, tasteless child who has no redeeming factors other than hating to lose {i}POSSIBLY{/i} come out with now?!?!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show beatrice_v001 normal at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Nao, what on earth could you be confessing to doing...?'
 show beatrice_v001 normal at inactive
 show nao_v002 normal_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I am Nao Houtani. ...I consider myself a normal human... but the truth is, I've had strange experiences that nobody would believe were real if I were to mention them."
 show beatrice_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I have physically encountered paranormal phenomena such as gods and {b}Tsukuyami{/b}, and know firsthand that this world doesn't just contain what Humans think it does."
 show nao_v002 normal at inactive
 show beatrice_v001 odoroki at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") '...What the... are you... a Voyager Witch...!?'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide nao_v002
 hide beatrice_v001
 hide fade onlayer curtain
 show erika_v001 sinken at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show erika_v001 sinken at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "There's no WAY that's truee!!! You're just a teensy, {i}tiny{/i}, little insignificant DUMPSTER DIVEEEEERRRRRRRR!!!!!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show nao_v002 normal at mei_left
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 show dlanor_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Dlanor-san, I am not lying. Please allow me to use the red truth.'
 show nao_v002 normal at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'What would you like to use it FOR...?'
 hide dlanor_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator "I whisper into Dlanor-san's ear."
 show dlanor_v001 odoroki at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show dlanor_v001 odoroki at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") '...I-I UNDERSTAND. ...However, in order to do that, I will need to see your HAND.'
 show dlanor_v001 odoroki at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'My hand?'
 hide nao_v002
 hide dlanor_v001
 with Dissolve(0.2)
 show beatrice_v001 normal_close at mei_center
 with Dissolve(0.5)
 show beatrice_v001 normal_close at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") '...Dlanor wants to see your Fragments.'
 hide beatrice_v001
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'Of course, I will only need to observe that which is involved with your red TRUTH. Furthermore, it is through my oath of confidentiality with the Great Court of Heaven that I shall never reveal any other truths I have LEARNED.'
 show dlanor_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...You mean she wants to look inside my head? I don't mind."
 show nao_v002 normal at inactive
 show dlanor_v001 sinken at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'With that... please excuse ME...'
 hide nao_v002
 hide dlanor_v001
 with Dissolve(0.2)
 narrator "Dlanor-san's eyes turned almost see-through as they emitted a faint light."
 narrator 'All she was doing was staring at me... but it gave me a strange, uncomfortable feeling.'
 narrator '...I see. That was what she meant when she said she wanted to look at my hand.'
 narrator 'The uncomfortable feeling was as though everything I had ever experienced in my life, my thoughts, my feelings, my emotions, and everything else, was all being watched by another person.'
 show dlanor_v001 normal_close at mei_left
 show beatrice_v001 normal at mei_right
 with Dissolve(0.5)
 show beatrice_v001 normal at inactive
 show dlanor_v001 normal_close at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") '...NAO. Thank you very MUCH. I am FINISHED.'
 show dlanor_v001 normal_close at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "And with that... Dlanor's verdict is..."
 show beatrice_v001 normal at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'EFFECTIVE.'
 show red_cover onlayer curtain as fade with Dissolve(0.16666666666666666)
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 hide fade onlayer curtain
 with Dissolve(0.16666666666666666)
 show beatrice_v001 normal at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") '{umi_red}I have confirmed that Nao Houtani has met and interacted with inhuman BEINGS.{/umi_red}'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide beatrice_v001
 hide dlanor_v001
 hide fade onlayer curtain
 show erika_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 sinken at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'W-... who the hell are you?! I thought you were just some bratty kid I happened to meet on the ferry...?!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show beatrice_v001 normal at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "Didn't your master once say that black tea is best enjoyed with monsters?"
 show nao_v002 normal at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") '...I see. If a witch opens up the game board, witches, monsters, and similar beings may be invited in...'
 show beatrice_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'All kinds of mysterious entities, such as ghosts and gods, exist in this world.'
 show beatrice_v001 normal at inactive
 show nao_v002 normal_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Because of that, I don't deny Beatrice's existence. Her being here is proof enough."
 show nao_v002 normal_close at inactive
 show beatrice_v001 odoroki at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "Y-You recognize my existence... Nao, I've never had a guest such as yourself..."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide nao_v002
 hide beatrice_v001
 hide fade onlayer curtain
 show nao_v002 normal at mei_center
 with Dissolve(0.08333333333333333)
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'In addition, I am going to repeat my claims as to the first and second magic circle incidents. '
 show nao_v002 normal_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "First, let's put the second magic circle incident on the chopping block."
 play audio 'audio/sfx/SE_391_ls_swing.wav'
 show white_cover as flash with Dissolve(0.1)
 pause 0.1
 hide flash with Dissolve(0.2)
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '{umi_blue}The suspect Shion-san is innocent.{/umi_blue}'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show erika_v001 odoroki at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 camera at screenshake_transform
 pause 0.0
 show nao_v002 normal at inactive
 show erika_v001 odoroki at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "That's impossible, totally impossible!!!!! Shion is the culprit!!!! She's definitely the culpriiiiiiiit!!!!!"
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.1
 pause 0.5
 play audio 'audio/sfx/SE_391_ls_swing.wav'
 show erika_v001 odoroki at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '{umi_blue}Erika-san put a "Bedmaking Not Necessary" tag on her doorknob so that the servants would not enter her room.{/umi_blue}'
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.2
 pause 0.5
 play audio 'audio/sfx/SE_391_ls_swing.wav'
 pause 0.3333333333333333
 play audio 'audio/sfx/SE_391_ls_swing.wav'
 show erika_v001 odoroki at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "{umi_blue}Because of this, the only person who would be able to get into the room would be Shion-san, who, despite Erika-san's traps, was able to prove her innocence.{/umi_blue}"
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
 show erika_v001 odoroki at inactive
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "{umi_blue}Therefore, the second magic circle was impossible for a Human to make, so it's clearly a witch's prank.{/umi_blue}"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide nao_v002
 hide erika_v001
 hide fade onlayer curtain
 show erika_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show erika_v001 odoroki at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "That's not clear at alllllllll!!! Who did it, and where did they come from!?!?!? Don't make a mockery of the blue truuuuuuuth!!!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show beatrice_v001 normal at mei_right
 show nao_v002 sinken at mei_left
 with Dissolve(0.5)
 show nao_v002 sinken at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "...Nao, you realize I'll benefit from this? Are you trying to lose...?"
 show beatrice_v001 normal at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Don't worry. I'm going to win, too."
 show beatrice_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Dlanor-san, is my blue truth effective?'
 hide beatrice_v001
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'It is EFFECTIVE. ...In return, Erika must submit either a red truth, equivalent evidence, or a REBUTTAL.'
 hide nao_v002
 show erika_v001 sinken_close at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal at inactive
 show erika_v001 sinken_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") '...............ay...'
 show erika_v001 sinken_close at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") '...I did not hear THAT. Please repeat YOURSELF.'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide dlanor_v001
 hide erika_v001
 hide fade onlayer curtain
 show erika_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show erika_v001 odoroki at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'No way... nowaynowaynowaaaaaaaaayy! Shion is absolutely, positively, certainly guilty... so why... so why is there no evidence... anywhere?!?!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 narrator 'It seemed that Erika-san went all in on her gambit with the fluorescent paint on the doorknob.'
 narrator 'She had lost the card that was supposed to be her ace in the hole... and was now waiting for the count-out. '
 show beatrice_v001 normal_close at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show beatrice_v001 normal_close at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Nao. Your turn is now over...'
 show nao_v002 normal at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "...I'm up next. By using the blue truth you have established, I will be able to claim victory... are you okay with this?"
 show beatrice_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I'd like to negotiate."
 show nao_v002 normal at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "Hoh? Since you're letting me win, I will listen to what you have to say."
 show beatrice_v001 smile at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'The next turn is yours, but before you declare your victory, I want you to make one move for me.'
 show beatrice_v001 smile at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "While the second magic circle is a witch's deed, Erika-san was the culprit for the first one. And just now, it finally occured to me why Shannon-san didn't feel anything strange when she found it."
 hide nao_v002
 hide beatrice_v001
 with Dissolve(0.2)
 narrator 'At last, the soup of logic, reasoning, and mystery... had finished thickening.'
 show nao_v002 normal at mei_left
 show beatrice_v001 normal at mei_right
 with Dissolve(0.5)
 show beatrice_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Beatrice. You are a witch, correct?'
 show nao_v002 normal at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Of course.'
 show beatrice_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Because of that, you're an expert in all sorts of spells and rituals, correct? Which of course would also include magic circles."
 show nao_v002 normal at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Mhm. I hold the title of Endless Witch. There is nothing I do not know.'
 show beatrice_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Since you just said that, I want you to look at both the first and second magic circles.'
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide beatrice_v001
 hide nao_v002
 with Dissolve(0.2)
 camera:
  parallel:
   linear 0.5 pos (960, 590)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show beatrice_v001 sinken at mei_center
 with Dissolve(0.5)
 camera at sepia_shader
 pause 0.0
 hide fade onlayer curtain
 with Dissolve(1.0)
 show beatrice_v001 sinken at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "...Even so, I don't understand this circle... I don't know what it's used for."
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
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
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator "That itself was an explanation. Perhaps it wasn't a magic circle at all."
 narrator "That line of reasoning explains... why Shannon-san didn't see it as strange, and why Mion-san and Shion-san didn't seem to be too shocked when they saw it...!!"
 show nao_v002 normal at mei_left
 show beatrice_v001 normal at mei_right
 with Dissolve(0.5)
 show beatrice_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Can you please give us a more detailed explanation?'
 show nao_v002 normal at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Mhm... The shapes of a magic circle can roughly describe things like its core and the flow of energy through it...'
 show nao_v002 normal at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "...This circle looks like it's gathering magical energy from outside of it, but in reality it just passes through the circle without being collected, so it doesn't look like it has any meaning in particular. "
 show beatrice_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "So, in the eyes of the Great Witch called Lady Beatrice... the magic circle doesn't make any sense at all?"
 show nao_v002 normal at inactive
 show beatrice_v001 normal_close at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Not slightly. ...This thing that appears to be a magic circle is an illegible fake.'
 hide beatrice_v001
 hide nao_v002
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'I am a Reader, so I have kept silent... but I have never seen the letters on the circumference of the summoning circle BEFORE.'
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'The Great Court of Heaven uses a vast number of languages... but I have never seen any like THIS.'
 hide dlanor_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_left
 show beatrice_v001 normal_close at mei_right
 with Dissolve(0.5)
 show beatrice_v001 normal_close at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Then from that conclusion... you could say that this magic circle was child's play?"
 show nao_v002 normal at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Mhm.'
 show nao_v002 normal at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'But these two magic circles must have been made by different people, correct?'
 show nao_v002 normal at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "While the spirals and overlapping circles vary, it's clear that both parties were trying to draw the same magic circle."
 show beatrice_v001 normal at inactive
 show nao_v002 normal_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "So, in essence, it's possible that this magic scribble was made by several people who had some sort of common knowledge..."
 show nao_v002 normal_close at inactive
 show beatrice_v001 fuan at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "...I-I don't understand what you mean. Can you simplify what you're saying...?"
 show beatrice_v001 fuan at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'I want to state this on your turn. This way, we can both be declared the victors. '
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide beatrice_v001
 hide nao_v002
 hide fade onlayer curtain
 show erika_v001 odoroki_close at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 odoroki_close at active
 show erika_v001 odoroki_close at chara_shake_transform
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") '...Nnnnnnnggghhh...... why... why do I always lose on Rokkenjimaaaaa...?!?!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show beatrice_v001 normal at mei_right
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Dlanor... In all honesty, I would like to attend to what Nao has to say. May I give my turn to her?'
 show beatrice_v001 normal at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'If that is your request, then it is FINE.'
 show beatrice_v001 normal at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'NAO. I would also like to hear how Shannon overlooked this magic CIRCLE.'
 hide dlanor_v001
 hide beatrice_v001
 with Dissolve(0.2)
 show nao_v002 smile at mei_left
 show erika_v001 odoroki_close at mei_right
 with Dissolve(0.5)
 show erika_v001 odoroki_close at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Sympathy as a detective, huh, Erika-san?'
 show nao_v002 smile at inactive
 show erika_v001 sinken at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Gh. ...I Iost, I lost, I lost...'
 show erika_v001 sinken at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'So, maybe that summoning circle...'
 call chapter_end
 jump event01_30_10