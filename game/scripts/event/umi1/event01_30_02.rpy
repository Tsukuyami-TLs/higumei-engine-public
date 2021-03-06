label event01_30_02:
 show black_background onlayer black
 $ event_store.current_event='umi1'
 $ event_store.current_progress=4
 $ event_store.current_chapter='event01_30_02'
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
 show expression 'images/bg/AdvBg_2291.png' as bg
 play music "<loop 0>audio/bgm/BGM_GACHA_COLLAB2.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show kanon_v001 normal at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at inactive
 show kanon_v001 normal at active
 Character('Kanon',ctc="ctcArrow", ctc_position="fixed") 'After meals, we usually prepare either tea or coffee. Which would you prefer?'
 show kanon_v001 normal at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'The taste inside my mouth is so sweet! Some salted plum kelp tea would wrap things up nicely. You got that here?'
 hide mion_v002
 hide kanon_v001
 with Dissolve(0.2)
 show nao_v002 fuan at mei_left
 show shion_v002 fuan at mei_right
 with Dissolve(0.5)
 show shion_v002 fuan at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'S-Sophistication is rare with this one...'
 show nao_v002 fuan at inactive
 show shion_v002 fuan at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Sorry about my older sister. She's a country bumpkin..."
 hide shion_v002
 hide nao_v002
 with Dissolve(0.2)
 show kanon_v001 normal_close at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at inactive
 show kanon_v001 normal_close at active
 Character('Kanon',ctc="ctcArrow", ctc_position="fixed") '...Maybe it is available at the mansion. If you allow me some time, I can go check.'
 show kanon_v001 normal_close at inactive
 show mion_v002 smile at active
 show mion_v002 smile at jump_transform
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Ah, really!? Thanks! I'll be counting on you, then."
 show mion_v002 smile at inactive
 show kanon_v001 normal at active
 Character('Kanon',ctc="ctcArrow", ctc_position="fixed") "...If I'm not wrong, Kumasawa-san had mackerel kelp tea of her own..."
 play audio 'audio/sfx/SE_530_walk_one.wav'
 hide kanon_v001
 with Dissolve(0.3)
 pause 1.0
 show erika_v001 normal at mei_left
 with Dissolve(0.5)
 show mion_v002 smile at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Mion-san, you're quite good. You're not just spending the night here, but you're properly doing your job too."
 play audio 'audio/sfx/SE_226_shine.wav'
 show erika_v001 normal at inactive
 show mion_v002 futeki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "I guess! Although I've got a little sister who doesn't get that and calls me a country bumpkin and stuff!"
 hide mion_v002
 hide erika_v001
 with Dissolve(0.2)
 show shion_v002 odoroki at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 camera at screenshake_transform
 pause 0.0
 show nao_v002 normal at inactive
 show shion_v002 odoroki at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Ehhh!? Don't tell me that was you reviewing their services just now!?"
 show shion_v002 odoroki at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "C-Clearly... if they're going to make it into a resort, high profile guests might come too."
 show shion_v002 odoroki at inactive
 show nao_v002 normal_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "If they aren't able to fulfill such a small request for the guests in a natural manner, they won't be able to have anyone satisfied..."
 hide nao_v002
 hide shion_v002
 with Dissolve(0.2)
 show erika_v001 normal at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Although this time, they happened to be prepared for that...'
 show mion_v002 smile at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "I presume what Mion-san wanted to see the most was how they could come up with an excuse so beautiful that even after failing to be prepared for them, it wouldn't ruin the guest's mood."
 show erika_v001 normal at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Still, Kanon-kun's conduct is definitely deserving of a good score."
 hide erika_v001
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show mion_v002 smile at inactive
 show shion_v002 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Definitely. ...Had he taken too long to take action, the guest could've felt bad for troubling them."
 show shion_v002 smile at inactive
 show mion_v002 smile_close at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'No matter how unreasonable of a situation it is, working in a consistent flow without making a single mistake is true professionalism!'
 hide shion_v002
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show mion_v002 smile_close at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "What's important is being able to handle the situation smoothly, even if it's something not written in the manual..."
 hide mion_v002
 show erika_v001 normal_close at mei_right
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Being flexible. In other words, acting as if that itself is the expectation.'
 show nao_v002 normal at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'It also means that bluffing can be important, to some extent.'
 hide nao_v002
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show shion_v002 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'For sure, in the same way that a clerk who appears to be experienced seems more competent.'
 hide erika_v001
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show shion_v002 smile at inactive
 show mion_v002 smile at active
 show mion_v002 smile at nod_transform
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Yep, yep. In contrast, if a clerk appears anxious while performing their duties, even though they are performing the same tasks as the experienced one, you can't help but feel that you can't rely on them."
 hide shion_v002
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show mion_v002 smile at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...A dignified attitude is essential for building a sense of trust with the guest, and that itself is the first step in proving the excellency in your services.'
 hide mion_v002
 hide nao_v002
 with Dissolve(0.2)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "To put it simply, mess around too much and it's all over."
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "It's the same for the greatest detectives all over; because of how dignified and respected they are, there lies an overwhelming absoluteness in their reasoning."
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Well, there {i}are{/i} also cases in which the detective was dignified enough to make the culprit give in on their own, even while their reasoning was full of holes.'
 hide erika_v001
 with Dissolve(0.2)
 show mion_v002 smile at mei_right
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "True! If you pressure the culprit enough, there are times they'll give in on their own."
 show mion_v002 smile at inactive
 show shion_v002 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "My sister's specialty is pretending she understood everything, when in actuality she didn't get anything at all."
 show shion_v002 smile at inactive
 show mion_v002 sinken at active
 show mion_v002 sinken at jumping_transform
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "No, it's a specialty of Wanyan's! Even when you have zero hints, act as if you've grasped the truth and aim for the blind spot!"
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "It is always essential for a detective to have the aura of someone who's seen through everything."
 hide erika_v001
 with Dissolve(0.2)
 narrator 'As the flow of the conversation went on, it was unavoidable that the main topic would become great detectives and mysteries.'
 narrator 'At that time, Jessica-san arrived with Kanon-san, who just returned. As Kanon-san served the tea, Jessica-san joined our talk.'
 narrator 'By then, the topic had went from unresolved cases to urban legends, and at the very end, we even ended up talking about the occult.'
 show shion_v002 smile at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at inactive
 show shion_v002 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "That's true. When you're able to solve it, it's considered a mystery, but unresolved ones often become part of the occult."
 show shion_v002 smile at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Since ancient times, things once assumed to be divine miracles have successfully been explained through science.'
 show shion_v002 smile at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Divine miracles cannot be explained. The idea here being, whatever you can't explain gets written off as a divine miracle."
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "It's the battle between science and the occult, right?"
 show erika_v001 normal_close at mei_right
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "More gracefully put, it's <Mystery versus Fantasy>."
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 show jessica_v001 fuan_close at mei_center
 with Dissolve(0.5)
 show jessica_v001 fuan_close at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Well, the theory of the unexplained isn't see all end all. Take it too far and you crush the dreams of children."
 hide jessica_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_left
 show shion_v002 smile at mei_right
 with Dissolve(0.5)
 show shion_v002 smile at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...Since Oyashiro-sama's curse is unexplained too, I wonder if maybe science will expose its true form someday?"
 show nao_v002 normal at inactive
 show shion_v002 fuan at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "With religious faith, it's a bit harder. There are some things in the world you shouldn't try to disprove."
 hide shion_v002
 hide nao_v002
 with Dissolve(0.2)
 show jessica_v001 sinken at mei_center
 with Dissolve(0.5)
 show jessica_v001 sinken at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "What? Oyashiro-sama's curse!?"
 hide jessica_v001
 with Dissolve(0.2)
 narrator 'Oh, I\'ll bite. Well, for someone not from Hinamizawa, hearing the phrase "Oyashiro-sama\'s curse" clearly might be a bit silly...'
 show erika_v001 normal_close at mei_right
 show jessica_v001 normal at mei_left
 with Dissolve(0.5)
 show jessica_v001 normal at inactive
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") '...Every year, on the day of the village festival, one person dies, and then one person disappears... right?'
 show erika_v001 normal_close at inactive
 show jessica_v001 fuan at active
 show jessica_v001 fuan at chara_shake_transform
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "What the hell, that's mad creepy...?! I won't {i}bother{/i} going to the bathroom alone tonight thinking about footsteps following me like that...!!"
 hide jessica_v001
 hide erika_v001
 with Dissolve(0.2)
 show mion_v002 normal at mei_right
 show shion_v002 normal at mei_left
 with Dissolve(0.5)
 show shion_v002 normal at inactive
 show mion_v002 normal at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'From the beginning, the "Sono" (???) kanji in "Sonozaki" (??????)... has depicted human organs, while the "Zaki" (???) kanji... '
 show mion_v002 normal at inactive
 show shion_v002 sinken at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'If there are twins born within the Sonozaki family, the family rule is to strangle the younger child. Since I was born afterwards, they had me by the neck like... gyeeeeehhh!'
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 show jessica_v001 odoroki at mei_right
 with Dissolve(0.5)
 show jessica_v001 odoroki at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Wait, for real!? Hold up, the world outside the island is freaky too!! Maybe I should spend my whole life here...'
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show jessica_v001 odoroki at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Hinamizawa was... just a bit {i}too{/i} blessed with such a story.'
 hide jessica_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator 'All over Japan, turbulent legends like this overflow with misunderstandings.'
 narrator 'Even so, having a creepy occult mystery from your hometown became something cool to talk about.'
 play sound ['audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav'] fadeout 1.0
 show nao_v002 normal at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...Speaking of which, Erika-san. ...Didn't you say something about a witch doing this and that?"
 show nao_v002 normal at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") '*giggle*. ...You should have that conversation with someone who lives on this island, like Jessica-san.'
 hide erika_v001
 hide nao_v002
 with Dissolve(0.2)
 show shion_v002 normal at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at inactive
 show shion_v002 normal at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Could the "witch" be the lady in the portrait from earlier?'
 show shion_v002 normal at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Ooo, nice! That really does put the "Western" in Western occult mystery, huh?'
 show shion_v002 normal at inactive
 show mion_v002 futeki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "But that's why I shared the secret behind the name of Watanagashi, and how it links the bloodshed in the dam war to Oyashiro-sama's curse."
 show mion_v002 futeki at inactive
 show shion_v002 futeki at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Isn't the intensity of that a bit different than a lady in a portrait blinking in the middle of the night~?"
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show jessica_v001 futeki at mei_left
 with Dissolve(0.5)
 show jessica_v001 futeki at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Say that much and even I can't keep quiet about it. She's gonna show you the ace up her sleeve!"
 show kanon_v001 normal at mei_right
 with Dissolve(0.5)
 show jessica_v001 futeki at inactive
 show kanon_v001 normal at active
 Character('Kanon',ctc="ctcArrow", ctc_position="fixed") '...My lady. Are you fine with saying that?'
 show kanon_v001 normal at inactive
 show jessica_v001 fuan at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Eh, ah, umm...'
 show kanon_v001 normal at inactive
 show jessica_v001 fuan_close at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'The conversation that we had here absolutely stays between us, alright? Mom would be terrifying if she found out. '
 hide jessica_v001
 hide kanon_v001
 with Dissolve(0.2)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") '*giggle*giggle*giggle*.'
 stop music fadeout 0.5
 hide erika_v001
 with Dissolve(0.2)
 narrator 'Just a Beethoven picture being in a music classroom can create a ghost story, never mind an enormous portrait like that one in a completely westernized home.'
 narrator "What's more, it's of a beautiful woman bearing the title of family alchemist. It would be weirder if a ghost story {i}didn't{/i} come out of it."
 play music "<loop 0>audio/bgm/BGM_QUEST3_COLLAB2.ogg"
 show jessica_v001 normal at mei_left
 show kanon_v001 normal at mei_right
 with Dissolve(0.5)
 show kanon_v001 normal at inactive
 show jessica_v001 normal at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "I think I've seen her before too... but our mansion is huge. Huge enough that it doesn't match with the size of my family."
 show jessica_v001 normal at inactive
 show kanon_v001 normal at active
 Character('Kanon',ctc="ctcArrow", ctc_position="fixed") '...I have heard that the many rooms were made to accommodate many relatives, and the mansion was intentionally built large to encourage the prosperity of the family.'
 show kanon_v001 normal at inactive
 show jessica_v001 fuan at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Grandfather is superstitious on his own, though. ...Having an impossibly large mansion is, needless to say, pretty uncanny.'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.4
 hide kanon_v001
 hide jessica_v001
 hide fade onlayer curtain
 show mion_v002 futeki at mei_center
 with Dissolve(0.08333333333333333)
 show mion_v002 futeki at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Those unused rooms... might have something other than people settling in them...'
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
 show nao_v002 fuan at chara_shake_transform
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'S-... stop it, please. Your face is getting too close.'
 hide nao_v002
 with Dissolve(0.2)
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Is anyone familiar with the story of the Winchester house mystery?'
 show shion_v002 normal at mei_left
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show shion_v002 normal at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'When you say Winchester, do you mean the Winchester gun?'
 show shion_v002 normal at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'The widowed wife of the late multimillionaire and owner of the Winchester gun company believed that she had been cursed by the spirits of those killed by his guns.'
 hide shion_v002
 show mion_v002 normal at mei_left
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show mion_v002 normal at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "A fortune teller told her that the ghosts residing in the rooms in her home would threaten to curse her to death if she didn't continue to renovate it. And she believed."
 hide erika_v001
 hide mion_v002
 with Dissolve(0.2)
 narrator 'The widowed wife then continued to add more and more extensions to the house until her death, resulting in a massively distorted mansion: the Winchester mystery house...'
 show nao_v002 fuan at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Huh. ...Then, the mansion with too many rooms to fit the amount of family members is...'
 show nao_v002 fuan at inactive
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'The head of the Ushiromiya family, Kinzo-san, succeeded in some business with Beatrice before accepting the loan of 100 tons of gold.'
 show nao_v002 fuan at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "It isn't just a success story either... I feel as though there is something important hidden within it."
 hide erika_v001
 hide nao_v002
 with Dissolve(0.2)
 show mion_v002 normal at mei_right
 show shion_v002 fuan at mei_left
 with Dissolve(0.5)
 show shion_v002 fuan at inactive
 show mion_v002 normal at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "100 tons of gold doesn't just grow on trees."
 show shion_v002 fuan at inactive
 show mion_v002 normal_close at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'That lady, Beatrice, creating it through alchemy also sounds a bit like a fairytale, though...'
 show mion_v002 normal_close at inactive
 show shion_v002 fuan at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Thinking about it... an unfathomable amount of greed and hatred, as well as the involvement of dead people, isn't unusual. After all, it's a large sum of money..."
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 show kanon_v001 normal_close at mei_right
 show jessica_v001 fuan at mei_left
 with Dissolve(0.5)
 show jessica_v001 fuan at inactive
 show kanon_v001 normal_close at active
 Character('Kanon',ctc="ctcArrow", ctc_position="fixed") '.....................'
 show kanon_v001 normal_close at inactive
 show jessica_v001 fuan at active
 show jessica_v001 fuan at chara_shake_transform
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "H-he-hey, you'd better stop with that...! This is my family you're talking about. I'm really not gonna be able to go to the bathroom at night..."
 hide jessica_v001
 hide kanon_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...This guesthouse is way too big, even.'
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'The mansion already has all of those guest rooms in it too, so needing to go out of your way to make this is...'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide nao_v002
 hide fade onlayer curtain
 show erika_v001 fuan at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 fuan at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Perhaps the 20 billion yen worth of gold is still being used to welcome... ghosts... here...?'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 narrator 'Ugh, this is scary. ...Wait, stop for second. Do I really have to stay here for two nights...?'
 show jessica_v001 normal_close at mei_left
 show kanon_v001 normal at mei_right
 with Dissolve(0.5)
 show kanon_v001 normal at inactive
 show jessica_v001 normal_close at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Well, with that, the conversation comes full circle...'
 show kanon_v001 normal at inactive
 show jessica_v001 normal at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Anyways, other than Grandfather, no one in this mansion knows who Beatrice is.'
 show jessica_v001 normal at inactive
 show kanon_v001 normal at active
 Character('Kanon',ctc="ctcArrow", ctc_position="fixed") 'Other than the fact that she is to whom the master is greatly indebted... no one...'
 show kanon_v001 normal at inactive
 show jessica_v001 normal at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Is she alive or is she dead? If she's alive, how old is she? Where could she be living...?"
 show kanon_v001 normal at inactive
 show jessica_v001 fuan_close at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'None of us know...'
 hide kanon_v001
 hide jessica_v001
 with Dissolve(0.2)
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...A portrait of an unknown person... being boldly hung up in such a wide space might be kind of... uncanny... maybe.'
 hide nao_v002
 with Dissolve(0.2)
 narrator 'When did the portrait get named? ...She eventually went on to be called the Golden Witch, Beatrice, after all.'
 narrator "The massive portrait hung in that wide space in the mansion isn't drawn of the family head Kinzo either; it's a drawing of the Golden Witch."
 narrator "...This means that the mansion and the island's... real master... is the Golden Witch, Beatrice, isn't it?"
 show jessica_v001 normal at mei_left
 show kanon_v001 normal at mei_right
 with Dissolve(0.5)
 show kanon_v001 normal at inactive
 show jessica_v001 normal at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'The rumor... of a mysterious figure wandering around inside the mansion while the servants are working at night has gotten pretty popular. ...Right?'
 show jessica_v001 normal at inactive
 show kanon_v001 normal_close at active
 Character('Kanon',ctc="ctcArrow", ctc_position="fixed") '...Yes.'
 show jessica_v001 normal at inactive
 show kanon_v001 normal at active
 Character('Kanon',ctc="ctcArrow", ctc_position="fixed") 'If... in the middle of the night in the mansion, you do see this mysterious figure... never chase after it, let alone call after it.'
 show jessica_v001 normal at inactive
 show kanon_v001 normal at active
 Character('Kanon',ctc="ctcArrow", ctc_position="fixed") "On multiple occasions... someone who couldn't have been in the Ushiromiya family, nor a servant... that mysterious form of a woman... I've come into contact with her as well."
 show kanon_v001 normal at inactive
 show jessica_v001 normal at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Sometimes, windows unlock at night without the servants touching them, and it terrifies Mom.'
 show kanon_v001 normal at inactive
 show jessica_v001 fuan_close at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'But everyone keeps saying how they definitely did rounds making sure the windows are locked.'
 hide kanon_v001
 hide jessica_v001
 with Dissolve(0.2)
 show mion_v002 normal at mei_right
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at inactive
 show mion_v002 normal at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'This {i}is{/i} a massive mansion. ...Someone named Beatrice could be lurking about, hidden somewhere.'
 show mion_v002 normal at inactive
 show shion_v002 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Still, the window locks opening as a prank isn't very cute."
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Clearly.'
 hide nao_v002
 with Dissolve(0.2)
 show kanon_v001 normal at mei_right
 show jessica_v001 normal at mei_left
 with Dissolve(0.5)
 show jessica_v001 normal at inactive
 show kanon_v001 normal at active
 Character('Kanon',ctc="ctcArrow", ctc_position="fixed") 'The people who do believe in and respect the existence of Beatrice-sama say she is generous.'
 show kanon_v001 normal at inactive
 show jessica_v001 normal at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "So... asserting something that makes a fool out of Beatrice, like saying she couldn't exist... seems to result in you being cursed."
 hide jessica_v001
 hide kanon_v001
 with Dissolve(0.2)
 narrator 'Not a small number of servants come in and out for the Ushiromiya family, and at times, new employees come in their stead.'
 narrator "Because it's a massive and eerie mansion... the newer servants generally believe the ghost story of Beatrice right away."
 show kanon_v001 normal_close at mei_right
 show jessica_v001 normal at mei_left
 with Dissolve(0.5)
 show jessica_v001 normal at inactive
 show kanon_v001 normal_close at active
 Character('Kanon',ctc="ctcArrow", ctc_position="fixed") "However... sometimes there are people who don't believe."
 show kanon_v001 normal_close at inactive
 show jessica_v001 normal at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '...One time at night while doing the rounds, there was a servant who misstepped and fell down the stairs, getting injured horribly before quitting.'
 show kanon_v001 normal_close at inactive
 show jessica_v001 fuan_close at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Shannon later heard... that the servant said, "If Beatrice does exist, I\'d like to see her.", and appeared to have been targeted...'
 show jessica_v001 fuan_close at inactive
 show kanon_v001 normal at active
 Character('Kanon',ctc="ctcArrow", ctc_position="fixed") "...I, too, didn't believe in her at first."
 show jessica_v001 fuan_close at inactive
 show kanon_v001 fuan_close at active
 Character('Kanon',ctc="ctcArrow", ctc_position="fixed") 'But then... I had a certain job to do... and since then, I stopped doubting her existence.'
 hide jessica_v001
 hide kanon_v001
 with Dissolve(0.2)
 show shion_v002 normal at mei_right
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at inactive
 show shion_v002 normal at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...Meaning... that job led you to believe in Beatrice's existence afterwards...?"
 show shion_v002 normal at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'What happened... during that job?'
 hide nao_v002
 hide shion_v002
 with Dissolve(0.2)
 show kanon_v001 normal_close at mei_center
 with Dissolve(0.5)
 show kanon_v001 normal_close at active
 Character('Kanon',ctc="ctcArrow", ctc_position="fixed") '...........................'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide kanon_v001
 with Dissolve(0.2)
 play sound ['audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav'] fadeout 1.0
 show black_cover as bg
 play audio 'audio/sfx/SE_5020_key.wav'
 narrator 'One day, Kanon-san was appointed to trim the roses. After locking up the garden shed, he left the key in his pocket, and retired for the day.'
 narrator 'Normally, the key gets used during a job, and then after that job is done, it must be returned to the keybox in the servant room. '
 narrator 'That day, Kanon-san finished the job without returning the key.'
 narrator 'The garden shed can only be opened with that one key. It cannot even be opened with the master key.'
 narrator 'So, in essence... since after the garden shed was locked, until the next morning, no one was able to open it until he unlocked it, making it a closed room...'
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "The next morning... when Kanon-kun opened the shutters to the garden shed... something that couldn't have been there, was..."
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Something that couldn't have been... there...?"
 window hide None
 stop sound
 show expression 'images/bg/AdvBg_2320.png' as bg
 play music "<loop 0>audio/bgm/BGM_QUEST7_COLLAB2.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 pause 3.0
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_2291.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 show kanon_v001 normal_close at mei_center
 with Dissolve(0.5)
 show kanon_v001 normal_close at active
 Character('Kanon',ctc="ctcArrow", ctc_position="fixed") '...A creepy... magic circle... was drawn there.'
 hide kanon_v001
 with Dissolve(0.2)
 show erika_v001 normal at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'If I reason this out simply... I suppose we can doubt that the one person who had the key to the locked room, Kanon-san, did all of this on his own.'
 show nao_v002 normal at inactive
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'But then, on the other hand...'
 show erika_v001 normal_close at inactive
 show nao_v002 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...To Kanon-san... this wasn't the doing of someone human... I can understand that..."
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 show kanon_v001 normal_close at mei_center
 with Dissolve(0.5)
 show kanon_v001 normal_close at active
 Character('Kanon',ctc="ctcArrow", ctc_position="fixed") '..............................'
 show kanon_v001 normal at active
 Character('Kanon',ctc="ctcArrow", ctc_position="fixed") '...As soon as I reported it to Genji-sama... he told me that I must never reveal this information to anyone.'
 hide kanon_v001
 with Dissolve(0.2)
 show jessica_v001 sinken at mei_center
 with Dissolve(0.5)
 show jessica_v001 sinken at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'That magic circle was... a greeting from Beatrice.'
 show jessica_v001 sinken_close at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Beatrice... left that magic circle there for those of us who didn't believe..."
 hide jessica_v001
 with Dissolve(0.2)
 show shion_v002 normal at mei_left
 show mion_v002 normal at mei_right
 with Dissolve(0.5)
 show mion_v002 normal at inactive
 show shion_v002 normal at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "...If it's just a warning, then it's nothing to worry about, though."
 show shion_v002 normal at inactive
 show mion_v002 normal at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Notwithstanding, if you deny Beatrice's existence, or rather make her out to be a fool... they said there have been people that tumbled down the stairs and were injured badly... "
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show erika_v001 normal_close at mei_right
 with Dissolve(0.5)
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'I am the detective. I am confident that everything in this world can be explained with reasoning.'
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'However, on occasion... even I may come across "something" that would be blasphemous to reason about.'
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show erika_v001 normal at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'That might be a little... no... really... scary... maybe...'
 hide erika_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator 'The sun is still high, but I feel a cold presence tingling down my spine.'
 narrator "Yeah. That's my one saving grace here. It's not even past noon yet. And the weather is a bit too good for telling ghost stories."
 narrator '...I wanted a change of atmosphere. I just wanted to spend my time relaxing in the rose garden while reading a book or doing embroidery or something.'
 narrator "I didn't come here to panic while counting my remaining days here on my fingers."
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide fade onlayer curtain
 show nao_v002 smile at mei_center
 with Dissolve(0.08333333333333333)
 show nao_v002 smile at active
 show nao_v002 smile at jump_transform
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Hahahahahaha, aaahahahahahahahaha...'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 narrator 'Anyway, if I fake laugh like this, everyone will laugh with me, and then I can change the mood.'
 narrator "But nothing is funny at the moment, so I'm just laughing out of place."
 camera at screenshake_transform
 pause 0.0
 narrator 'But... why does it have to be like that?! No one is laughing with me...!'
 show nao_v002 smile at mei_center
 with Dissolve(0.5)
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'This is ridiculous. Halloween has been over since last month.'
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I thought I had specifically gone here to enjoy myself, but all I've done up until now is get scared by a cheap ghost story. It's absurd."
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Besides, in our world today, whatever strange thing it is, it can absolutely be explained!'
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Hey, Erika-san. Aren't I right?"
 hide nao_v002
 with Dissolve(0.2)
 show erika_v001 normal_close at mei_center
 with Dissolve(0.5)
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") '.....................'
 hide erika_v001
 with Dissolve(0.2)
 show nao_v002 sinken at mei_center
 with Dissolve(0.5)
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.1
 pause 0.5
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Let's suppose that Beatrice's ghost walks along the halls of the mansion at night, and someone witnesses that!"
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.2
 pause 0.5
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "There's a possibility that the evidence was falsified, there was a problem with their eyesight, or even a problem with their head, right? All of these possibilities can deny this! "
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 camera at screenshake_transform
 pause 0.0
 show nao_v002 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Aren't I right, Erika-san?!"
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 hide nao_v002
 with Dissolve(0.2)
 show erika_v001 normal_close at mei_center
 with Dissolve(0.5)
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "...You're right. It was when we met on the ferry. I definitely said that then."
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'Plus, I must have also mentioned this some time ago.'
 hide erika_v001
 with Dissolve(0.2)
 narrator '"However, on occasion..."'
 narrator '"...even I may come across \'something\' that would be blasphemous to reason about..." ...she said.'
 show erika_v001 normal at mei_right
 show nao_v002 sinken at mei_left
 with Dissolve(0.5)
 show nao_v002 sinken at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") '...I am the detective. As long as a Human caused this incident, I am confident that I can gather evidence to expose the truth without fail.'
 show nao_v002 sinken at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "However... if something inhuman caused this incident, that's a different story."
 show erika_v001 normal at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...No way......'
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 narrator "I believed that a person like Erika-san wouldn't acknowledge a witch from a silly ghost story, though..."
 show shion_v002 smile at mei_left
 show mion_v002 normal at mei_right
 with Dissolve(0.5)
 show mion_v002 normal at inactive
 show shion_v002 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Nao-san, let's calm down. It's just a chat over tea, yeah?"
 show shion_v002 smile at inactive
 show mion_v002 normal at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'Just like Oyashiro-sama "exists", the witch "exists" on this island.'
 show shion_v002 smile at inactive
 show mion_v002 normal_close at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Denying something without letting the other person explain is... something this ol' man isn't too fond of."
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 narrator "Even Mion-san, who's always messing around and poking fun at people...! Yet just until a bit ago, the others were getting riled up having that impudent conversation about the mansion!"
 narrator 'And Shion-san, who came up to me as if she was trying to pacify an irritable child.'
 narrator 'As Jessica-san and Kanon-san looked at each other... they surely were thinking that, very much so.'
 narrator "...That they wish this brat of a visitor wouldn't have a fit over a witch's curse... and...!"
 play sound ['audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav'] fadeout 1.0
 stop music fadeout 0.5
 show kanon_v001 normal at mei_right
 show jessica_v001 smile at mei_left
 with Dissolve(0.5)
 show jessica_v001 smile at inactive
 show kanon_v001 normal at active
 Character('Kanon',ctc="ctcArrow", ctc_position="fixed") '... Milady. You have your next task to do still.'
 show kanon_v001 normal at inactive
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "Th-that's right. Thanks, Kanon-kun."
 show kanon_v001 normal at inactive
 show jessica_v001 smile at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") "I'm gonna head out in a bit, then."
 show kanon_v001 normal at inactive
 show jessica_v001 fuan at active
 Character('Jessica Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'Nao-chan, can you forgive me? It was a dumb conversation. I want you to forget it. ...Alright, see ya!'
 hide jessica_v001
 hide kanon_v001
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_530_walk_one.wav'
 narrator 'Jessica-san and Kanon-san walked off with perturbed looks. Erika-san simply stood there while shrugging her shoulders.'
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'I do think I will return to my room, but what will everyone else do?'
 hide erika_v001
 with Dissolve(0.2)
 show shion_v002 smile at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at inactive
 show shion_v002 smile at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") 'I think since we have to prepare for tomorrow, we should go back to our rooms too to get some work done.'
 show mion_v002 smile at inactive
 show shion_v002 fuan at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "Sis suddenly got a bunch of requests coming in, so the arrangements didn't get done in time at all. It {i}sucks{/i}."
 show shion_v002 fuan at inactive
 show mion_v002 smile at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "I'm also gonna go back to my room to help prepare the clothes. ...I wonder if I can fit a little nap in."
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 narrator 'I just realized that at some point, it had started drizzling outside.'
 narrator "Since the sky is still light, it might stop soon anyway, but it isn't worth it pulling out an umbrella just to set out for the rose garden."
 narrator '...This is a vacation. Relaxation is the goal. This is completely different from the tight scheduling of overseas travel, having to catch buses all over to sightsee.'
 narrator 'Plus, just like Mion-san was saying, morning went by pretty fast.'
 show nao_v002 fuan_close at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...I might be a little tired too... maybe...'
 hide nao_v002
 with Dissolve(0.2)
 narrator "I'll nap a bit. And when I wake up, the freshly rained on rose garden will likely make a lovely sight from the window."
 narrator "No, on the flipside, the power could cut out unexpectedly while I'm sleeping..."
 narrator 'When morning goes by this fast, you get sleepy and nap your precious day away... I guess I can owe that to being on vacation.'
 show nao_v002 smile at mei_left
 with Dissolve(0.5)
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I'm glad the windows are shut for now. But I do think I want to properly lock them while I'm sleeping."
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show nao_v002 smile at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") '...Why is that? Are the locks on the windows breaking?'
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 show shion_v002 fuan at mei_left
 show mion_v002 fuan at mei_right
 with Dissolve(0.5)
 show mion_v002 fuan at inactive
 show shion_v002 fuan at active
 Character('Shion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "They aren't breaking. They {i}were{/i} broken... by someone."
 show shion_v002 fuan at inactive
 show mion_v002 fuan at active
 Character('Mion Sonozaki',ctc="ctcArrow", ctc_position="fixed") "I can still try at it... I told you there's still time before I have to apologize."
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 stop sound
 show expression 'images/bg/AdvBg_2371.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_536_up_stairs.wav'
 pause 2.5
 play audio 'audio/sfx/SE_5007_keyroll.wav'
 narrator 'The four of us went up to the second floor. \nThen, we unlocked each of our rooms with our respective keys and entered.'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_2281.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 narrator "Shion-san began spreading clothing garments from the trunk onto the beds in bunches. It seems like some of the garments haven't been finished in time for the photo shoots."
 narrator 'After Mion-san fought for a bit with the window lock, she realized it was impossible and stuck her tongue out at it.'
 play audio 'audio/sfx/SE_5037_getup.wav'
 narrator 'I was laid up on my bed, taking off my socks. With just that, I started feeling relaxed.'
 play audio 'audio/sfx/SE_528_unfold_cloth.wav'
 narrator 'Even thinking about reading a book is making me... sleepy...'
 narrator "Even on this wonderful island, even in this wonderful guesthouse, even with such a wonderful and expansive rose garden... I'm napping."
 narrator 'Yeah. This is true vacationing. This might be true luxury... maybe.'
 narrator "With the Sonozaki sisters' busy chatting serving as a lullaby, my eyelids grew heavier."
 narrator '...The odd atmosphere from the witch ghost story seemed like a lie now. I wonder if it was an absent-minded daydream...'
 narrator "What I did was akin to saying I didn't believe in Oyashiro-sama while on the Furude shrine grounds. Surely, I had ruined the mood on the island."
 narrator "...And the master of the island's too... surely..."
 narrator '...........................'
 play sound ['audio/sfx/SE_5054_rain.wav','audio/sfx/SE_5054_rain.wav'] fadeout 1.0
 window hide None
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 show black_cover as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") '...........................'
 show dlanor_v001 normal at mei_left
 with Dissolve(1.0)
 show erika_v001 normal at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'I SEE. The occasional sunshower does also HAPPEN.'
 show erika_v001 normal at inactive
 show dlanor_v001 normal_close at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'For someone like you, who lives to tear fantasy apart, siding with Lady Beatrice IS...'
 show dlanor_v001 normal_close at inactive
 show erika_v001 normal_close at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "Seriously. It's going to give me hives."
 show dlanor_v001 normal_close at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "That's why I was appointed as my master's messenger in delivering Beato's present. That's more or less my understanding of it."
 show erika_v001 normal at inactive
 show dlanor_v001 smile at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") "At any rate, today's lunch was quite MAGNIFICENT."
 show dlanor_v001 smile at inactive
 show erika_v001 smile at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") 'With a plate heaping with that much omurice, I simply {i}had{/i} to slurp it up voraciously with chopsticks.'
 show erika_v001 smile at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'By the way, that IS...?'
 show dlanor_v001 normal at inactive
 show erika_v001 normal at active
 Character('Erika Furudo',ctc="ctcArrow", ctc_position="fixed") "This is my birthday present for Beatrice. See? I do wonder if she'll come to like it?"
 call chapter_end
 jump event01_30_03