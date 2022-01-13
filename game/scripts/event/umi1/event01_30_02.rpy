label event01_30_02:
 show black_background onlayer black
 $ event_store.current_event='umi1'
 $ event_store.current_progress=3
 $ event_store.current_chapter='event01_30_02'
 $ persistent.menu_return='event'
 camera:
  anchor (0.5, 0.5)
  pos (960, 540)
 scene
 stop music
 stop sound
 show expression 'images/bg/AdvBg_2291.png' as bg
 play music "<loop 0>audio/bgm/BGM_GACHA_COLLAB2.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show mion_v002 smile at mei_right
 show kanon_v001 normal at mei_left
 with Dissolve(0.5)
 show kanon_v001 normal at active
 show mion_v002 smile at inactive
 kanon 'After meals, we usually prepare either tea or coffee. Which would you prefer?'
 show mion_v002 smile at active
 show kanon_v001 normal at inactive
 mion 'The taste inside my mouth is so sweet after that! Some salted plum kelp tea would wrap things up nicely. You got that here?'
 hide mion_v002
 hide kanon_v001
 with Dissolve(0.2)
 show shion_v002 fuan at mei_right
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at active
 show shion_v002 fuan at inactive
 nao 'This... this is perfection at its finest...'
 show shion_v002 fuan at active
 show nao_v002 fuan at inactive
 shion "Sorry about my older sister. She's quite a country bumpkin..."
 hide shion_v002
 hide nao_v002
 with Dissolve(0.2)
 show mion_v002 smile at mei_right
 show kanon_v001 normal_close at mei_left
 with Dissolve(0.5)
 show kanon_v001 normal_close at active
 show mion_v002 smile at inactive
 kanon '... Maybe it is available at the mansion. If you allow me some time, I can go check.'
 show mion_v002 smile at jump_transform,active
 show kanon_v001 normal_close at inactive
 mion "Ah, really!? Thanks! I'll be counting on you, then."
 show kanon_v001 normal at active
 show mion_v002 smile at inactive
 kanon "...If I'm not wrong, Kumasawa-san had mackerel kelp tea of her own..."
 play audio 'audio/sfx/SE_530_walk_one.wav'
 hide kanon_v001
 with Dissolve(0.3)
 pause 1.0
 show erika_v001 normal at mei_left
 with Dissolve(0.5)
 show erika_v001 normal at active
 show mion_v002 smile at inactive
 erika "Mion-san, you're quite good. You're not just spending the night here, but you're properly doing your job too."
 play audio 'audio/sfx/SE_226_shine.wav'
 show mion_v002 futeki at active
 show erika_v001 normal at inactive
 mion "I guess! Although I've got a little sister who doesn't get that and calls me a country bumpkin and stuff!"
 hide mion_v002
 hide erika_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_left
 show shion_v002 odoroki at mei_right
 with Dissolve(0.5)
 camera at screenshake_transform
 pause 0.0
 show shion_v002 odoroki at active
 show nao_v002 normal at inactive
 shion "Ehhh!? Don't tell me that was you reviewing their services just now!?"
 show nao_v002 normal at active
 show shion_v002 odoroki at inactive
 nao "For, for sure... If they're going to make it into a resort, high profile guests might come too."
 show nao_v002 normal_close at active
 show shion_v002 odoroki at inactive
 nao "If they aren't able to fulfill such a small request for the guests in a natural manner, they won't be able to have anyone satisfied..."
 hide nao_v002
 hide shion_v002
 with Dissolve(0.2)
 show mion_v002 smile at mei_right
 show erika_v001 normal at mei_left
 with Dissolve(0.5)
 show erika_v001 normal at active
 show mion_v002 smile at inactive
 erika 'Although this time, they happened to be prepared for that...'
 show erika_v001 normal at active
 show mion_v002 smile at inactive
 erika "I presume what Mion-san wanted to see the most was how they could come up with an excuse so beautiful that even after failing to be prepared for them, it wouldn't ruin the guest's mood."
 show mion_v002 smile at active
 show erika_v001 normal at inactive
 mion "Still, Kanon-kun's conduct is definitely deserving of a good score."
 hide erika_v001
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion "Right... Had he taken too long to take action, the guest could've felt bad for troubling them."
 show mion_v002 smile_close at active
 show shion_v002 smile at inactive
 mion 'No matter how unreasonable of a situation it is, working in a consistent flow without making a single mistake is true professionalism!'
 hide shion_v002
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show mion_v002 smile_close at inactive
 nao "What's important is being able to handle that situation smoothly, even if it's something that was not written in the manual..."
 hide mion_v002
 show erika_v001 normal_close at mei_right
 with Dissolve(0.5)
 show erika_v001 normal_close at active
 show nao_v002 normal at inactive
 erika 'Being flexible. In other words, acting as if that itself is the expectation.'
 show erika_v001 normal at active
 show nao_v002 normal at inactive
 erika 'It also means that bluffing can be important, to some extent.'
 hide nao_v002
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at active
 show erika_v001 normal at inactive
 shion 'Definitely, in the same way that a clerk who appears to be a senior seems more competent.'
 hide erika_v001
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at nod_transform,active
 show shion_v002 smile at inactive
 mion "Yep, yep. In contrast, if a clerk appears anxious while performing their duties, even though they are performing the same tasks as the senior, you can't help but feel that you can't rely on them."
 hide shion_v002
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show mion_v002 smile at inactive
 nao '...A dignified attitude is essential for building a sense of trust with the guest, and that itself is the first step in proving the excellency in your services.'
 hide mion_v002
 hide nao_v002
 with Dissolve(0.2)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika "To put it simply, mess around too much and it's all over."
 show erika_v001 normal at active
 erika "It's the same for the greatest detectives all over; because of how dignified and respected they are, there lies an overwhelming absoluteness in their reasoning."
 show erika_v001 normal_close at active
 erika 'Well, there {i}are{/i} also cases in which the culprit gave in just because the detective was very dignified, even while their reasoning was full of holes.'
 hide erika_v001
 with Dissolve(0.2)
 show shion_v002 smile at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at active
 show shion_v002 smile at inactive
 mion "True! If you pressure the culprit enough, there are times they'll give in on their own."
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion "My sister's specialty is pretending she understood everything, when in actuality she didn't get anything at all."
 show mion_v002 sinken at jumping_transform,active
 show shion_v002 smile at inactive
 mion "No, it's a specialty of Wanyan's! Even when you have zero hints, act as if you've grasped the truth and aim for the blind spot!"
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika "It is always essential for a detective to have the aura of someone who's seen through everything."
 hide erika_v001
 with Dissolve(0.2)
 narrator 'As the flow of the conversation went on, it was unavoidable that the main topic would become great detectives and mysteries.'
 narrator 'At that time, Jessica-san arrived with Kanon-san, who just returned. As Kanon-san served the tea, Jessica-san joined our talk.'
 narrator 'By then, the topic had went from unresolved cases to urban legends, and at the very end, we even ended up talking about the occult.'
 show mion_v002 smile at mei_right
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion "That's true. When you're able to solve it, it's considered a mystery, but unresolved ones often become part of the occult."
 show mion_v002 smile at active
 show shion_v002 smile at inactive
 mion 'Since ancient times, things once assumed to be divine miracles have been successfully explained through science.'
 show mion_v002 smile at active
 show shion_v002 smile at inactive
 mion "Divine miracles cannot be explained. The theory here being, whatever you can't explain suddenly gets written off as a divine miracle."
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao "It's the battle between science and the occult, right?"
 show erika_v001 normal_close at mei_right
 with Dissolve(0.5)
 show erika_v001 normal_close at active
 show nao_v002 normal at inactive
 erika "More gracefully put, it's <Mystery versus Fantasy>."
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 show jessica_v001 fuan_close at mei_center
 with Dissolve(0.5)
 show jessica_v001 fuan_close at active
 jessica "Well, the theory of the unexplained isn't see all end all. Take it too far and you crush the dreams of children."
 hide jessica_v001
 with Dissolve(0.2)
 show shion_v002 smile at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show shion_v002 smile at inactive
 nao "...Since Oyashiro-sama's curse is unexplained too, I wonder if maybe science will expose its true form someday?"
 show shion_v002 fuan at active
 show nao_v002 normal at inactive
 shion "With religious faith, it's a bit harder. There are some things in the world you shouldn't try to disprove."
 hide shion_v002
 hide nao_v002
 with Dissolve(0.2)
 show jessica_v001 sinken at mei_center
 with Dissolve(0.5)
 show jessica_v001 sinken at active
 jessica "What? Oyashiro-sama's curse!?"
 hide jessica_v001
 with Dissolve(0.2)
 narrator 'Oh, I\'ll bite. Well, for someone not from Hinamizawa, hearing the phrase "Oyashiro-sama\'s curse" clearly might be a bit silly...'
 show jessica_v001 normal at mei_left
 show erika_v001 normal_close at mei_right
 with Dissolve(0.5)
 show erika_v001 normal_close at active
 show jessica_v001 normal at inactive
 erika '... Every year, on the day of the village festival, one person dies, and then one person disappears... right?'
 show jessica_v001 fuan at chara_shake_transform,active
 show erika_v001 normal_close at inactive
 jessica "What the hell, that's mad creepy...?! I won't {i}bother{/i} going to the bathroom alone tonight thinking about footsteps following me like that...!!"
 hide jessica_v001
 hide erika_v001
 with Dissolve(0.2)
 show shion_v002 normal at mei_left
 show mion_v002 normal at mei_right
 with Dissolve(0.5)
 show mion_v002 normal at active
 show shion_v002 normal at inactive
 mion 'From the beginning, the "Sono" (園) kanji in "Sonozaki" (園崎)... has depicted human organs, while the "Zaki" (崎) kanji... '
 show shion_v002 sinken at active
 show mion_v002 normal at inactive
 shion 'If there are twins born within the Sonozaki family, the family rule is to strangle the younger child. Since I was born afterwards, they had me by the neck like... gyeeeeehhh!'
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 show jessica_v001 odoroki at mei_right
 with Dissolve(0.5)
 show jessica_v001 odoroki at active
 jessica 'Wait, for real!? Hold up, the world outside the island is freaky too!! Maybe I should spend my whole life here...'
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at active
 show jessica_v001 odoroki at inactive
 nao '...Hinamizawa was... just a bit {i}too{/i} blessed with such a story.'
 hide jessica_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator 'All over Japan, turbulent legends like this overflow with misunderstandings.'
 narrator 'Even so, having a creepy occult mystery from your hometown became something cool to talk about.'
 play sound ['audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav'] fadeout 1.0
 show erika_v001 normal at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show erika_v001 normal at inactive
 nao "...Speaking of which, Erika-san. ...Didn't you say something about a witch doing this and that?"
 show erika_v001 normal at active
 show nao_v002 normal at inactive
 erika '*giggle*. ...You should have that conversation with someone who lives on this island, like Jessica-san.'
 hide erika_v001
 hide nao_v002
 with Dissolve(0.2)
 show mion_v002 smile at mei_right
 show shion_v002 normal at mei_left
 with Dissolve(0.5)
 show shion_v002 normal at active
 show mion_v002 smile at inactive
 shion 'Could the "witch" be the lady in the portrait from earlier?'
 show mion_v002 smile at active
 show shion_v002 normal at inactive
 mion 'Ahh, I like that! That really puts the "Western" in Western occult mystery, huh?'
 show mion_v002 futeki at active
 show shion_v002 normal at inactive
 mion "But that's why I shared the secret behind the name of Watanagashi, and how it links the bloodshed in the dam war to Oyashiro-sama's curse."
 show shion_v002 futeki at active
 show mion_v002 futeki at inactive
 shion "Isn't the intensity of that a bit different than a lady in a portrait blinking in the middle of the night~?"
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show jessica_v001 futeki at mei_left
 with Dissolve(0.5)
 show jessica_v001 futeki at active
 jessica "Say that much and even I can't keep quiet about it. She's gonna show you the ace up her sleeve!"
 show kanon_v001 normal at mei_right
 with Dissolve(0.5)
 show kanon_v001 normal at active
 show jessica_v001 futeki at inactive
 kanon '...My lady. Are you fine with saying that?'
 show jessica_v001 fuan at active
 show kanon_v001 normal at inactive
 jessica 'Eh, ah, umm...'
 show jessica_v001 fuan_close at active
 show kanon_v001 normal at inactive
 jessica 'The conversation that we had here absolutely stays between us, alright? Mother would be terrifying if she found out. '
 hide jessica_v001
 hide kanon_v001
 with Dissolve(0.2)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika '*giggle*giggle*giggle*.'
 stop music fadeout 0.5
 hide erika_v001
 with Dissolve(0.2)
 narrator 'Just a Beethoven picture being in a music classroom can create a ghost story, never mind an enormous portrait like that one in a completely westernized home.'
 narrator "What's more, it's of a beautiful woman bearing the title of family alchemist. It would be weirder if a ghost story {i}didn't{/i} come out of it."
 play music "<loop 0>audio/bgm/BGM_QUEST3_COLLAB2.ogg"
 show kanon_v001 normal at mei_right
 show jessica_v001 normal at mei_left
 with Dissolve(0.5)
 show jessica_v001 normal at active
 show kanon_v001 normal at inactive
 jessica "I think I've seen her before too... but our mansion is huge. Huge enough that it doesn't match with the size of my family."
 show kanon_v001 normal at active
 show jessica_v001 normal at inactive
 kanon '...I have heard that the many rooms were made to accommodate many relatives, and the mansion was intentionally built large to encourage the prosperity of the family.'
 show jessica_v001 fuan at active
 show kanon_v001 normal at inactive
 jessica 'Grandfather is superstitious on his own, though. ...Having an impossibly large mansion is, needless to say, pretty uncanny.'
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
 mion 'Those unused rooms... might have something other than people settling in them...'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide mion_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at chara_shake_transform,active
 nao 'S-... stop it, please. Your face is getting too close.'
 hide nao_v002
 with Dissolve(0.2)
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika 'Is anyone familiar with the story of the Winchester house mystery?'
 show shion_v002 normal at mei_left
 with Dissolve(0.5)
 show shion_v002 normal at active
 show erika_v001 normal at inactive
 shion 'When you say Winchester, do you mean the Winchester gun?'
 show erika_v001 normal at active
 show shion_v002 normal at inactive
 erika 'The widowed wife of the late multimillionaire and owner of the Winchester gun company believed that she had been cursed by the spirits of those killed by his guns.'
 hide shion_v002
 show mion_v002 normal at mei_left
 with Dissolve(0.5)
 show mion_v002 normal at active
 show erika_v001 normal at inactive
 mion "A fortune teller told her that the ghosts residing in the rooms in her home would threaten to curse her to death if she didn't continue to renovate it. And she believed."
 hide erika_v001
 hide mion_v002
 with Dissolve(0.2)
 narrator 'The widowed wife then continued to add more and more extensions to the house until her death, resulting in a massively distorted mansion: the Winchester mystery house...'
 show erika_v001 normal at mei_right
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at active
 show erika_v001 normal at inactive
 nao '...Huh. ...Then, the mansion with too many rooms to fit the amount of family members is...'
 show erika_v001 normal_close at active
 show nao_v002 fuan at inactive
 erika 'The head of the Ushiromiya family, Kinzo-san, succeeded in some business with Beatrice before accepting the loan of 100 tons of gold.'
 show erika_v001 normal at active
 show nao_v002 fuan at inactive
 erika "It isn't just a success story either... I feel as though there is something important hidden within it."
 hide erika_v001
 hide nao_v002
 with Dissolve(0.2)
 show shion_v002 fuan at mei_left
 show mion_v002 normal at mei_right
 with Dissolve(0.5)
 show mion_v002 normal at active
 show shion_v002 fuan at inactive
 mion "100 tons of gold doesn't just grow on trees."
 show mion_v002 normal_close at active
 show shion_v002 fuan at inactive
 mion 'That lady, Beatrice, creating it through alchemy also sounds a bit like a fairytale, though...'
 show shion_v002 fuan at active
 show mion_v002 normal_close at inactive
 shion "Thinking about it... an unfathomable amount of greed and hatred, as well as the involvement of dead people, isn't unusual. After all, it's a large sum of money..."
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 show jessica_v001 fuan at mei_left
 show kanon_v001 normal_close at mei_right
 with Dissolve(0.5)
 show kanon_v001 normal_close at active
 show jessica_v001 fuan at inactive
 kanon '.....................'
 show jessica_v001 fuan at chara_shake_transform,active
 show kanon_v001 normal_close at inactive
 jessica "H-he-hey, you'd better stop with that...! This is my family you're talking about. I'm really not gonna be able to go to the bathroom at night..."
 hide jessica_v001
 hide kanon_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao '...This guesthouse is way too big, even.'
 show nao_v002 fuan at active
 nao 'The mansion already has all of those guest rooms in it too, so needing to go out of your way to make this is...'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide nao_v002
 hide fade onlayer curtain
 show erika_v001 fuan at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 fuan at active
 erika 'Perhaps the 20 billion yen worth of gold is still being used to welcome... ghosts... here...?'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 narrator 'Ugh, this is scary. ...Wait, stop for second. Do I really have to stay here for two nights...?'
 show kanon_v001 normal at mei_right
 show jessica_v001 normal_close at mei_left
 with Dissolve(0.5)
 show jessica_v001 normal_close at active
 show kanon_v001 normal at inactive
 jessica 'Well, with that, the conversation comes full circle...'
 show jessica_v001 normal at active
 show kanon_v001 normal at inactive
 jessica 'Anyway, other than Grandfather, no one in this mansion knows who Beatrice is.'
 show kanon_v001 normal at active
 show jessica_v001 normal at inactive
 kanon 'Other than the fact that she is to whom the master is greatly indebted... no one...'
 show jessica_v001 normal at active
 show kanon_v001 normal at inactive
 jessica "Is she alive or is she dead? If she's alive, how old is she? Where could she be living...?"
 show jessica_v001 fuan_close at active
 show kanon_v001 normal at inactive
 jessica 'None of us know...'
 hide kanon_v001
 hide jessica_v001
 with Dissolve(0.2)
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 nao '...A portrait of an unknown person... being boldly hung up in such a wide space might be kind of... uncanny... maybe.'
 hide nao_v002
 with Dissolve(0.2)
 narrator 'When did the portrait get named? ...She eventually went on to be called the Golden Witch, Beatrice, after all.'
 narrator "The massive portrait hung in that wide space in the mansion isn't drawn of the family head Kinzo either; it's a drawing of the Golden Witch."
 narrator "...This means that the mansion and the island's... real master... is the Golden Witch, Beatrice, isn't it?"
 show kanon_v001 normal at mei_right
 show jessica_v001 normal at mei_left
 with Dissolve(0.5)
 show jessica_v001 normal at active
 show kanon_v001 normal at inactive
 jessica 'At night... the rumor of a mysterious figure wandering around inside the mansion while the servants are working has gotten pretty popular. ...Right?'
 show kanon_v001 normal_close at active
 show jessica_v001 normal at inactive
 kanon '...Yes.'
 show kanon_v001 normal at active
 show jessica_v001 normal at inactive
 kanon 'If... in the middle of the night in the mansion, you do see this mysterious figure... never chase after it, let alone call after it.'
 show kanon_v001 normal at active
 show jessica_v001 normal at inactive
 kanon "On multiple occasions... someone who couldn't have been in the Ushiromiya family, nor a servant... that mysterious form of a woman... I've come into contact with her as well."
 show jessica_v001 normal at active
 show kanon_v001 normal at inactive
 jessica 'Sometimes, windows unlock at night without the servants touching them, and it terrifies Mom.'
 show jessica_v001 fuan_close at active
 show kanon_v001 normal at inactive
 jessica 'But everyone keeps saying how they definitely did rounds making sure the windows are locked.'
 hide kanon_v001
 hide jessica_v001
 with Dissolve(0.2)
 show shion_v002 smile at mei_left
 show mion_v002 normal at mei_right
 with Dissolve(0.5)
 show mion_v002 normal at active
 show shion_v002 smile at inactive
 mion 'This {i}is{/i} a massive mansion. ...Someone named Beatrice could be lurking about, hidden somewhere.'
 show shion_v002 smile at active
 show mion_v002 normal at inactive
 shion "Still, the window locks opening as a prank isn't very cute."
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao '...Clearly.'
 hide nao_v002
 with Dissolve(0.2)
 show jessica_v001 normal at mei_left
 show kanon_v001 normal at mei_right
 with Dissolve(0.5)
 show kanon_v001 normal at active
 show jessica_v001 normal at inactive
 kanon 'The people who do believe in and respect the existence of \nBeatrice-sama say she is generous.'
 show jessica_v001 normal at active
 show kanon_v001 normal at inactive
 jessica "So... asserting something that makes a fool out of Beatrice, like saying she couldn't exist... seems to result in you being cursed."
 hide jessica_v001
 hide kanon_v001
 with Dissolve(0.2)
 narrator 'Not a small number of servants come in and out for the Ushiromiya family, and at times, new employees come in their stead.'
 narrator "Because it's a massive and eerie mansion... the newer servants generally believe the ghost story of Beatrice right away."
 show jessica_v001 normal at mei_left
 show kanon_v001 normal_close at mei_right
 with Dissolve(0.5)
 show kanon_v001 normal_close at active
 show jessica_v001 normal at inactive
 kanon "However... sometimes there are people who don't believe."
 show jessica_v001 normal at active
 show kanon_v001 normal_close at inactive
 jessica '...One time at night while doing the rounds, there was a servant who misstepped and fell down the stairs, getting injured horribly before quitting.'
 show jessica_v001 fuan_close at active
 show kanon_v001 normal_close at inactive
 jessica 'Shannon later heard... that the servant said, "If Beatrice does exist, I\'d like to see her.", and appeared to have been targeted...'
 show kanon_v001 normal at active
 show jessica_v001 fuan_close at inactive
 kanon "...I, too, didn't believe in her at first."
 show kanon_v001 fuan_close at active
 show jessica_v001 fuan_close at inactive
 kanon 'But then... I had a certain job to do... and since then, I stopped doubting her existence.'
 hide jessica_v001
 hide kanon_v001
 with Dissolve(0.2)
 show nao_v002 fuan at mei_left
 show shion_v002 normal at mei_right
 with Dissolve(0.5)
 show shion_v002 normal at active
 show nao_v002 fuan at inactive
 shion "...Meaning... that job led you to believe in Beatrice's existence afterwards...?"
 show nao_v002 fuan at active
 show shion_v002 normal at inactive
 nao 'What happened... during that job?'
 hide nao_v002
 hide shion_v002
 with Dissolve(0.2)
 show kanon_v001 normal_close at mei_center
 with Dissolve(0.5)
 show kanon_v001 normal_close at active
 kanon '...........................'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide kanon_v001
 with Dissolve(0.2)
 play sound ['audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav'] fadeout 1.0
 show black_cover as bg
 play audio 'audio/sfx/SE_5020_key.wav'
 narrator 'One day, Kanon was appointed to trim the roses. After locking up the garden shed, he left the key in his pocket, and retired for the day.'
 narrator 'Normally, the key gets used during a job, and then after that job is done, it must be returned to the keybox in the servant room. '
 narrator 'That day, Kanon-san finished the job without returning the key.'
 narrator 'The garden shed can only be opened with that one key. It cannot even be opened with the master key.'
 narrator 'So, in essence... since after the garden shed was locked, until the next morning, no one was able to open it until he unlocked it, making it a closed room...'
 jessica "The next morning... when Kanon-kun opened the shutters to the garden shed... something that couldn't have been there, was..."
 nao "Something that couldn't have been... there...?"
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
 kanon '...A creepy... magic circle... was drawn there.'
 hide kanon_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show nao_v002 normal at inactive
 erika 'If I reason this out simply... I suppose we can doubt that the one person who had the key to the locked room, Kanon-san, did all of this on his own.'
 show erika_v001 normal_close at active
 show nao_v002 normal at inactive
 erika 'But then, on the other hand...'
 show nao_v002 normal at active
 show erika_v001 normal_close at inactive
 nao "...To Kanon-san... this wasn't the doing of someone human... I can understand that..."
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 show kanon_v001 normal_close at mei_center
 with Dissolve(0.5)
 show kanon_v001 normal_close at active
 kanon '..............................'
 show kanon_v001 normal at active
 kanon '...As soon as I reported it to Genji-sama... he told me that I must never reveal this information to anyone.'
 hide kanon_v001
 with Dissolve(0.2)
 show jessica_v001 sinken at mei_center
 with Dissolve(0.5)
 show jessica_v001 sinken at active
 jessica 'That magic circle was... a greeting from Beatrice.'
 show jessica_v001 sinken_close at active
 jessica "Beatrice... left that magic circle there for those of us who didn't believe..."
 hide jessica_v001
 with Dissolve(0.2)
 show mion_v002 normal at mei_right
 show shion_v002 normal at mei_left
 with Dissolve(0.5)
 show shion_v002 normal at active
 show mion_v002 normal at inactive
 shion "...If it's just a warning, then it's nothing to worry about, though."
 show mion_v002 normal at active
 show shion_v002 normal at inactive
 mion "Notwithstanding, if you deny Beatrice's existence, or rather make her out to be a fool... they said there have been people that tumbled down the stairs and were injured badly... "
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show erika_v001 normal_close at mei_right
 with Dissolve(0.5)
 show erika_v001 normal_close at active
 erika 'I am the detective. I am confident that everything in this world can be explained with reasoning.'
 show erika_v001 normal at active
 erika 'However, on occasion... even I may come across "something" that would be blasphemous to reason about.'
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at active
 show erika_v001 normal at inactive
 nao 'That might be a little... no... really... scary... maybe...'
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
 show nao_v002 smile at jump_transform,active
 nao '...Hahahahahaha, aaahahahahahahahaha...'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 narrator 'Anyways, if I fake laugh like this, everyone will laugh with me, and then I can change the mood.'
 narrator "But nothing is funny at the moment, so I'm just laughing out of place."
 camera at screenshake_transform
 pause 0.0
 narrator 'But... why does it have to be like that?! No one is laughing with me...!'
 show nao_v002 smile at mei_center
 with Dissolve(0.5)
 show nao_v002 smile at active
 nao 'This is ridiculous. Halloween has been over since last month.'
 show nao_v002 smile at active
 nao "I thought I had specifically gone here to enjoy myself, but all I've done up until now is get scared by a cheap ghost story. It's absurd."
 show nao_v002 smile at active
 nao 'Besides, in our world today, whatever strange thing it is, it can absolutely be explained!'
 show nao_v002 smile at active
 nao "Hey, Erika-san. Aren't I right?"
 hide nao_v002
 with Dissolve(0.2)
 show erika_v001 normal_close at mei_center
 with Dissolve(0.5)
 show erika_v001 normal_close at active
 erika '.....................'
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
 nao "Let's suppose that Beatrice's ghost walks along the halls of the mansion at night, and someone witnesses that!"
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.2
 pause 0.5
 show nao_v002 sinken at active
 nao "There's a possibility that the evidence was falsified, there was a problem with their eyesight, or even a problem with their head, right? All of these possibilities can deny this! "
 camera:
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 camera at screenshake_transform
 pause 0.0
 show nao_v002 sinken at active
 nao "Aren't I right, Erika-san?!"
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
 erika "...You're right. It was when we met on the ferry. I definitely said that then."
 show erika_v001 normal at active
 erika 'Plus, I must have also mentioned this some time ago.'
 hide erika_v001
 with Dissolve(0.2)
 narrator '"However, on occasion..."'
 narrator '"...even I may come across \'something\' that would be blasphemous to reason about..." ...she said.'
 show nao_v002 sinken at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show nao_v002 sinken at inactive
 erika '...I am the detective. As long as a Human caused this incident, I am confident that I can gather evidence to expose the truth without fail.'
 show erika_v001 normal at active
 show nao_v002 sinken at inactive
 erika "However... if something inhuman caused this incident, that's a different story."
 show nao_v002 fuan at active
 show erika_v001 normal at inactive
 nao '...No way......'
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 narrator "I believed that a person like Erika-san wouldn't acknowledge a witch from a silly ghost story, though..."
 show mion_v002 normal at mei_right
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at active
 show mion_v002 normal at inactive
 shion "Nao-san, let's calm down. It's just a chat over tea, yeah?"
 show mion_v002 normal at active
 show shion_v002 smile at inactive
 mion 'Just like Oyashiro-sama "exists", the witch "exists" on this island.'
 show mion_v002 normal_close at active
 show shion_v002 smile at inactive
 mion "Denying something without letting the other person explain is... something this ol' man isn't too fond of."
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 narrator "Even Mion-san, who's always messing around and poking fun at people...! Yet just until a bit ago, the others were getting riled up having that impudent conversation about the mansion!"
 narrator 'And Shion-san, who came up to me as if she was trying to pacify an irritable child.'
 narrator 'As Jessica-san and Kanon-san looked at each other... they surely were thinking that, very much so.'
 narrator "...That they wish this brat of a visitor wouldn't have a fit over a witch's curse... and...!"
 play sound ['audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav'] fadeout 1.0
 stop music fadeout 0.5
 show jessica_v001 smile at mei_left
 show kanon_v001 normal at mei_right
 with Dissolve(0.5)
 show kanon_v001 normal at active
 show jessica_v001 smile at inactive
 kanon '... Milady. You have your next task to do still.'
 show jessica_v001 smile at active
 show kanon_v001 normal at inactive
 jessica "Th-that's right. Thanks, Kanon-kun."
 show jessica_v001 smile at active
 show kanon_v001 normal at inactive
 jessica "I'm gonna head out in a bit, then."
 show jessica_v001 fuan at active
 show kanon_v001 normal at inactive
 jessica 'Nao-chan, can you forgive me? It was a boring conversation. I want you to forget it. ...All right, see ya!'
 hide jessica_v001
 hide kanon_v001
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_530_walk_one.wav'
 narrator 'Jessica-san and Kanon walked off with perturbed looks. Erika-san simply stood there while shrugging her shoulders.'
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika 'I do think I will return to my room, but what will everyone else do?'
 hide erika_v001
 with Dissolve(0.2)
 show mion_v002 smile at mei_right
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion 'I think since we have to prepare for tomorrow, we should go back to our rooms too to get some work done.'
 show shion_v002 fuan at active
 show mion_v002 smile at inactive
 shion "Sis suddenly got a bunch of requests coming in, so the arrangements didn't get done in time at all. It {i}sucks{/i}."
 show mion_v002 smile at active
 show shion_v002 fuan at inactive
 mion "I'm also gonna go back to my room to help prepare the clothes. ...I wonder if I can fit a little nap in."
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
 nao '...I might be a little tired too... maybe...'
 hide nao_v002
 with Dissolve(0.2)
 narrator "I'll nap a bit. And when I wake up, the freshly rained on rose garden will likely make a lovely sight from the window."
 narrator "No, on the flipside, the power could cut out unexpectedly while I'm sleeping..."
 narrator 'When morning goes by this fast, you get sleepy and nap your precious day away... I guess I can owe that to being on vacation.'
 show nao_v002 smile at mei_left
 with Dissolve(0.5)
 show nao_v002 smile at active
 nao "I'm glad the windows are shut for now. But I do think I want to properly lock them while I'm sleeping."
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show nao_v002 smile at inactive
 erika '...Why is that? Are the locks on the windows breaking?'
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 show mion_v002 fuan at mei_right
 show shion_v002 fuan at mei_left
 with Dissolve(0.5)
 show shion_v002 fuan at active
 show mion_v002 fuan at inactive
 shion "They aren't breaking. They {i}were{/i} broken... by someone."
 show mion_v002 fuan at active
 show shion_v002 fuan at inactive
 mion "I can still try at it... I told you there's still time before I have to apologize."
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
 narrator 'The four of us went up to the second floor. And so, we unlocked each of our rooms with our respective keys and entered.'
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
 erika '...........................'
 show dlanor_v001 normal at mei_left
 with Dissolve(1.0)
 show dlanor_v001 normal at active
 show erika_v001 normal at inactive
 dlanor 'I SEE. The occasional sunshower does also HAPPEN.'
 show dlanor_v001 normal_close at active
 show erika_v001 normal at inactive
 dlanor 'For someone like you, who lives to tear fantasy apart, siding with Lady Beatrice IS...'
 show erika_v001 normal_close at active
 show dlanor_v001 normal_close at inactive
 erika "Seriously. It's going to give me hives."
 show erika_v001 normal at active
 show dlanor_v001 normal_close at inactive
 erika "That's why I was appointed as my master's messenger in delivering Beato's present. That's more or less my understanding of it."
 show dlanor_v001 smile at active
 show erika_v001 normal at inactive
 dlanor "At any rate, today's lunch was quite MAGNIFICENT."
 show erika_v001 smile at active
 show dlanor_v001 smile at inactive
 erika 'With a plate heaping with that much omurice, I simply {i}had{/i} to slurp it up voraciously with chopsticks.'
 show dlanor_v001 normal at active
 show erika_v001 smile at inactive
 dlanor 'By the way, that IS...?'
 show erika_v001 normal at active
 show dlanor_v001 normal at inactive
 erika "This is my birthday present for Beatrice. See? I do wonder if she'll come to like it?"
 call chapter_end
 jump event01_30_03