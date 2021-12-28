label chara472001_02:
 show black_background onlayer black
 $ event_store.current_event='chara472001'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara472001_02'
 stop sound
 scene #000
 play music 'audio/bgm/BGM_QUEST6_COLLAB2.ogg'
 show expression 'images/bg/AdvBg_2190.png' as bg
 with Dissolve(1.0)
 show nao_v001 normal at mei_right
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show nao_v001 normal at inactive
 dlanor '"Knox\'s Ten Commandments", or "Knox\'s Decalogue", promise to serve and protect MYSTERY. To say they are commandments is no EXAGGERATION.'
 show nao_v001 normal at active
 show dlanor_v001 normal at inactive
 nao 'Commandments...?'
 show black_cover as fade with Dissolve(1.0)
 hide nao_v001
 hide dlanor_v001
 with Dissolve(0.2)
 stop sound
 scene black_cover
 show expression 'images/card/Card_472001.png' as bg
 with Dissolve(1.0)
 dlanor 'YES. Knox\'s 1st: "It is forbidden for the culprit to be anyone not mentioned in the early part of the STORY."'
 dlanor 'Knox\'s 2nd: "It is forbidden for supernatural agencies to be used as a detective TECHNIQUE."'
 dlanor 'Knox\'s 3rd: "It is forbidden for hidden passages to EXIST."'
 dlanor 'Knox\'s 4th: "It is forbidden for unknown drugs or hard to understand scientific devices to be USED."'
 dlanor 'Knox\'s 6th: "It is forbidden for accident or intuition to be employed as a detective TECHNIQUE."'
 dlanor 'Knox\'s 7th: "It is forbidden for the detective to be the CULPRIT."'
 dlanor 'Knox\'s 8th: "It is forbidden for the case to be resolved with clues that are not PRESENTED."'
 dlanor 'Knox\'s 9th: "It is permitted for observers to let their own conclusions and explanations be HEARD."'
 dlanor 'Knox\'s 10th: "It is forbidden for a character to disguise themselves as another without CLUES."'
 nao 'I see. 10 rules make up the Ten Commandments... wait, what happened to number 5?'
 dlanor 'It is OMITTED. As such, please refrain from referencing IT.'
 nao 'I sort of wanted to hear why it is omitted... but I understand.'
 show black_cover as fade with Dissolve(1.0)
 stop sound
 scene black_cover
 show expression 'images/bg/AdvBg_2190.png' as bg
 with Dissolve(1.0)
 show nao_v001 normal_close at mei_right
 show beatrice_v001 normal at mei_left
 with Dissolve(0.5)
 show beatrice_v001 normal at active
 show nao_v001 normal_close at inactive
 beatrice 'So, Nao, after hearing about "Knox\'s Ten Commandments" for the first time, what were your thoughts?'
 show nao_v001 fuan at active
 show beatrice_v001 normal at inactive
 nao 'Right... if you want me to speak my thoughts openly, it gave me the impression that they\'re a bit strict. I was like, "Mystery really has those types of limitations?"'
 show beatrice_v001 futeki at updown_shake_transform,active
 show nao_v001 fuan at inactive
 beatrice "*cackle*cackle*! I guess that's because when you {i}have{/i} read mystery, you have only done it in the casual sense?"
 show nao_v001 fuan at active
 show beatrice_v001 futeki at inactive
 nao "I'm not so sure about reading casually, but... because there were so many difficult expressions and settings, I would clearly be giving it my all just trying to read along with the story."
 show beatrice_v001 smile at active
 show nao_v001 fuan at inactive
 beatrice 'Then, in the midst of reading a story, have you never tried to reason out on the spot who the culprit is?'
 show nao_v001 fuan_close at active
 show beatrice_v001 smile at inactive
 nao "I've been surprised when I finally hear about the culprit or the trick, but I probably haven't really done much reasoning... maybe."
 show nao_v001 normal at active
 show beatrice_v001 smile at inactive
 nao 'So when Beatrice reads mystery, I wonder if she reasons out who the culprit is?'
 play audio 'audio/sfx/SE_226_shine.wav'
 show beatrice_v001 futeki at active
 show nao_v001 normal at inactive
 beatrice 'But of course! That is the true thrill behind mystery!'
 show nao_v001 smile at active
 show beatrice_v001 futeki at inactive
 nao 'I see... but turning the pages and following along just behind the detective in the story is so fun in and of itself though.'
 show beatrice_v001 fuan at active
 show nao_v001 smile at inactive
 beatrice 'Ah-, mmm... but is it not common courtesy to go into a mystery with the intention to solve it?'
 show nao_v001 normal at active
 show beatrice_v001 fuan at inactive
 nao 'With a novel, the moment you open the book, your very first "action" is to start reading.'
 show nao_v001 smile at active
 show beatrice_v001 fuan at inactive
 nao 'So, I wonder how you as the reader could willfully enjoy attempting to solve a riddle, or do any other action for that matter, while in the midst of the action of reading.'
 show beatrice_v001 normal at active
 show nao_v001 smile at inactive
 beatrice "...Hmm, we don't see eye to eye here. I have heard that you are a bookworm, but the ways in which we enjoy reading are dissimilar."
 hide beatrice_v001
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show nao_v001 smile at inactive
 dlanor "In this argument, Lady Beatrice's side is less UNDERSTANDABLE. Pulling out of this would be wise for YOU."
 show nao_v001 odoroki at active
 show dlanor_v001 normal at inactive
 nao "Ah, but I wasn't particularly saying that I think Beatrice's method of having fun is certainly wrong? I just wanted to say that my way was different."
 show nao_v001 normal at active
 show dlanor_v001 normal at inactive
 nao 'And anyways... I understood what she said earlier. If we were to use my reading style, even if mystery novels had no rules, there would be no issue.'
 show nao_v001 normal_close at active
 show dlanor_v001 normal at inactive
 nao "But then, for someone who tackles mystery novels with Beatrice's precise approach, rules are a prerequisite."
 show nao_v001 normal at active
 show dlanor_v001 normal at inactive
 nao 'Even in games, if you play without rules, you lose both stratagem and tact... "Knox\'s Decalogue" is for that purpose.'
 show dlanor_v001 normal at active
 show nao_v001 normal at inactive
 dlanor 'AGREED. For people who let the story do the telling and for people who solve the riddle head-on, "Knox\'s Decalogue" is something necessary to balance the fairness between these two PARTIES.'
 hide dlanor_v001
 show beatrice_v001 normal at mei_left
 with Dissolve(0.5)
 show beatrice_v001 normal at active
 show nao_v001 normal at inactive
 beatrice 'Mhm. If there were no rules, you would have complete freedom setting up the mystery, but then the detective who wants to tackle the mystery with reasoning loses his lifeline. He would not understand how to continue, nor be able to see his goal.'
 show beatrice_v001 normal_close at active
 show nao_v001 normal at inactive
 beatrice 'By the way, when there is an inconsistency in the rules related to the story, we call this a "logic error".'
 show beatrice_v001 normal at active
 show nao_v001 normal at inactive
 beatrice 'In a logic battle, "logic errors" are essentially a foul... This is a matter that should be avoided with certainty.'
 show nao_v001 normal at active
 show beatrice_v001 normal at inactive
 nao "...So, basically, it's similar to how wrong it is when two people are in PvP in an arcade and the loser hits the winner, right?"
 show beatrice_v001 fuan at active
 show nao_v001 normal at inactive
 beatrice 'Uh, mm...? I have no knowledge of what a PvP is, so I cannot really assign meaning to it, though...'
 show nao_v001 fuan at active
 show beatrice_v001 fuan at inactive
 nao 'Ah, but... returning to the question of how the structure of "Knox\'s Decalogue" was formed, what ultimately lead to it being made?'
 hide beatrice_v001
 show dlanor_v001 normal_close at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal_close at active
 show nao_v001 fuan at inactive
 dlanor '... That is due to the fact that the past was an era where mysteries with too much freedom REIGNED.'
 show nao_v001 normal at active
 show dlanor_v001 normal_close at inactive
 nao 'Mysteries with too much freedom...?'
 show dlanor_v001 normal at active
 show nao_v001 normal at inactive
 dlanor 'Before "Knox\'s Decalogue" was structured, mysteries that were unsolvable by normal and fair means were a rampant issue... so this completely lowered the quality of the GENRE.'
 show dlanor_v001 normal at active
 show nao_v001 normal at inactive
 dlanor 'For example, culprits would suddenly appear towards the latter half of the story, detectives would use psychic powers to solve mysteries... secret passageways would exist for locked-room murders, such things as THIS.'
 show dlanor_v001 normal_close at active
 show nao_v001 normal at inactive
 dlanor 'Furthermore, unimaginable medicines and scientific devices that were unknown to readers would unfairly make their DEBUT...'
 show dlanor_v001 normal_close at active
 show nao_v001 normal at inactive
 dlanor 'Detectives would solve incidents by coincidence or through the sixth SENSE. The culprit would be the detective in reality, and he would lie in his perspective as a TRICK.'
 show dlanor_v001 normal at active
 show nao_v001 normal at inactive
 dlanor 'And moreover, clues would appear out of nowhere with no explanation... a character Mrs. A would actually be Mrs. B in disguise, et CETERA...'
 show nao_v001 fuan at active
 show dlanor_v001 normal at inactive
 nao '...I see. With those things being done, someone reading could never make a conjecture through normal means.'
 show nao_v001 normal at active
 show dlanor_v001 normal at inactive
 nao '...Oh? But if you really think about it, the logic in the 9th commandment is a bit different in nature, right?'
 show dlanor_v001 odoroki at active
 show nao_v001 normal at inactive
 dlanor 'The difference... IS?'
 show nao_v001 normal at active
 show dlanor_v001 odoroki at inactive
 nao 'Like, right next to it is the 10th one, and that one is listed as "something you shouldn\'t do", whereas the 9th is "something that you are permitted to do", isn\'t it?'
 show nao_v001 normal at active
 show dlanor_v001 odoroki at inactive
 nao 'Knox\'s 9th: "It is permitted for observers to let their own conclusions and explanations be heard."'
 show nao_v001 normal at active
 show dlanor_v001 odoroki at inactive
 nao "It's okay for the observers in this rule to recognize characters in the story, right?"
 show dlanor_v001 normal at active
 show nao_v001 normal at inactive
 dlanor 'YES.'
 show nao_v001 fuan at active
 show dlanor_v001 normal at inactive
 nao "So basically, if I'm explaining this correctly, it makes me think that a character in the story can tell a lie and it wouldn't matter and such, but...?"
 hide dlanor_v001
 show beatrice_v001 normal at mei_left
 with Dissolve(0.5)
 show beatrice_v001 normal at active
 show nao_v001 fuan at inactive
 beatrice 'If you only look at that rule, I see your point... However, the detective must not be the culprit.'
 show nao_v001 normal at active
 show beatrice_v001 normal at inactive
 nao 'Rule 7 prevents it, right? But I wonder if that also prevents the detective from telling lies?'
 hide beatrice_v001
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show nao_v001 normal at inactive
 dlanor 'It DOES, they must not tell LIES. Rule 9 impedes this from HAPPENING.'
 show nao_v001 odoroki at jump_transform,active
 show dlanor_v001 normal at inactive
 nao 'Huh? But for it to be permitted for my own conclusions and explanations to be heard... ah.'
 hide dlanor_v001
 show beatrice_v001 futeki at mei_left
 with Dissolve(0.5)
 show beatrice_v001 futeki at active
 show nao_v001 odoroki at inactive
 beatrice '*cackle*cackle*! She has finally realized.'
 show nao_v001 sinken at active
 show beatrice_v001 futeki at inactive
 nao "Is that so... the observer is permitted, but the detective isn't."
 hide beatrice_v001
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show nao_v001 sinken at inactive
 dlanor '... Exactly SO. You understood WELL.'
 show nao_v001 normal at active
 show dlanor_v001 normal at inactive
 nao 'I see... with that in place, the detective cannot tell a lie at all.'
 show dlanor_v001 normal_close at active
 show nao_v001 normal at inactive
 dlanor 'Not NECESSARILY. There are EXCEPTIONS. In the case that the detective tells a lie unconsciously, "Knox\'s Decalogue" would allow it.'
 show nao_v001 odoroki at active
 show dlanor_v001 normal_close at inactive
 nao 'For example?'
 hide dlanor_v001
 show beatrice_v001 smile at mei_left
 with Dissolve(0.5)
 show beatrice_v001 smile at active
 show nao_v001 odoroki at inactive
 beatrice 'Right. With you here as the detective... are you familiar with Pâtiss?'
 show nao_v001 normal at active
 show beatrice_v001 smile at inactive
 nao "No, I'm not. What is that?"
 show beatrice_v001 smile at active
 show nao_v001 normal at inactive
 beatrice 'It is a variety of black tea.'
 show nao_v001 odoroki at active
 show beatrice_v001 smile at inactive
 nao 'Ohh...'
 hide beatrice_v001
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show nao_v001 odoroki at inactive
 dlanor 'That was a LIE.'
 camera at screenshake_transform
 pause 0.0
 show nao_v001 sinken at active
 show dlanor_v001 normal at inactive
 nao 'Huhhh...?'
 hide dlanor_v001
 show beatrice_v001 futeki at mei_left
 with Dissolve(0.5)
 show beatrice_v001 futeki at active
 show nao_v001 sinken at inactive
 beatrice "*cackle*cackle*cackle*... It's actually something more along the lines of deep-fried gyoza, served as a tea party snack. It goes along tastily with Dinbura specifically."
 show nao_v001 fuan_close at active
 show beatrice_v001 futeki at inactive
 nao 'I see. One time I was inside a huge supermarket, trying to search whether or not they were selling that. ...After thinking of that, I understood this conversation.'
 show nao_v001 normal at active
 show beatrice_v001 futeki at inactive
 nao 'With me as the spectator and as a detective, if I believe what Beatrice says and mention it to another person... It cannot be a lie.'
 show nao_v001 normal at active
 show beatrice_v001 futeki at inactive
 nao "In this case, what's important is the definition of lie. What does the lie entail... what could it? Hm..."
 hide nao_v001
 hide beatrice_v001
 with Dissolve(0.2)
 show dlanor_v001 odoroki at mei_center
 with Dissolve(0.5)
 show dlanor_v001 odoroki at active
 dlanor '...I am AMAZED. You have truly grasped this concept QUICKLY. Even as a young girl, your wisdom is truly AMUSING...'
 hide dlanor_v001
 with Dissolve(0.2)
 show nao_v001 smile at mei_right
 show beatrice_v001 smile at mei_left
 with Dissolve(0.5)
 show beatrice_v001 smile at active
 show nao_v001 smile at inactive
 beatrice 'Nao seems to have a knack for mystery. But most of all, studying it from here on out is a must to keep that up, however.'
 show nao_v001 smile at active
 show beatrice_v001 smile at inactive
 nao 'My, really? If you say it to me like that, that makes me happy.'
 show nao_v001 normal at active
 show beatrice_v001 smile at inactive
 nao 'But yeah, if I had never met with you guys, I suppose I would have never known about "Knox\'s Decalogue".'
 show nao_v001 smile at active
 show beatrice_v001 smile at inactive
 nao 'Thank you, Dlanor, for teaching me of such fun rules. If there was something like that all along, I wish I had known sooner.'
 hide beatrice_v001
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show nao_v001 smile at inactive
 dlanor '............'
 show nao_v001 fuan at active
 show dlanor_v001 normal at inactive
 nao 'Dlanor?'
 hide dlanor_v001
 show beatrice_v001 futeki at mei_left
 with Dissolve(0.5)
 show beatrice_v001 futeki at active
 show nao_v001 fuan at inactive
 beatrice '*cackle*cackle*! Lady Dlanor is quite surprised!'
 show beatrice_v001 futeki_close at active
 show nao_v001 fuan at inactive
 beatrice ' I wonder what Lady Dlanor\'s father was trying to hide when he created "Knox\'s Decalogue".'
 show nao_v001 odoroki at jump_transform,active
 show beatrice_v001 futeki_close at inactive
 nao "Huh...? Dlanor's father made this?"
 hide beatrice_v001
 show dlanor_v001 normal_close at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal_close at active
 show nao_v001 odoroki at inactive
 dlanor '...Yes, that is RIGHT.'
 show nao_v001 normal at active
 show dlanor_v001 normal_close at inactive
 nao 'I see. I thought that some reader made "Knox\'s Decalogue", but... right, there are also people on the author\'s side.'
 hide dlanor_v001
 show beatrice_v001 normal at mei_left
 with Dissolve(0.5)
 show beatrice_v001 normal at active
 show nao_v001 normal at inactive
 beatrice 'Hoh. What does that thought entail?'
 show nao_v001 smile at active
 show beatrice_v001 normal at inactive
 nao 'Like, if an author worked under "Knox\'s Decalogue" when it was first being announced, people who knew the decalogue would understand the mystery was designed to be solved, right?'
 show nao_v001 smile_close at active
 show beatrice_v001 normal at inactive
 nao '...I see. So, with "Knox\'s Decalogue" being in the way, and with no one getting rid of it, it stuck as a rule for authors to write in.'
 show nao_v001 smile at active
 show beatrice_v001 normal at inactive
 nao 'Us people who simply read the story were able to declare this as fair, seeing it as a brand logo of sorts.'
 hide beatrice_v001
 show dlanor_v001 odoroki at mei_left
 with Dissolve(0.5)
 show dlanor_v001 odoroki at active
 show nao_v001 smile at inactive
 dlanor '............'
 show nao_v001 fuan at active
 show dlanor_v001 odoroki at inactive
 nao 'But protecting it as a brand is dangerous. If a fake version were to be released, it would have an effect on the reputation of the original.'
 show nao_v001 fuan_close at active
 show dlanor_v001 odoroki at inactive
 nao "My mother has also worried about this. Even if a fake version is sold, the focal point of the anger would be on the original seller. It's such an unreasonable thought."
 hide dlanor_v001
 show beatrice_v001 smile at mei_left
 with Dissolve(0.5)
 show beatrice_v001 smile at active
 show nao_v001 fuan_close at inactive
 beatrice "... What an interesting example. However, let's say it would be truly unreasonable for the people following the rules to handicap themselves."
 show beatrice_v001 smile at active
 show nao_v001 fuan_close at inactive
 beatrice 'With this, the people crafting mysteries that follow the rules are protected. All faulty mysteries are then cut down completely.'
 show nao_v001 smile at active
 show beatrice_v001 smile at inactive
 nao 'Ohh... is that so? How envious of a story it is, hearing that people have a role to be on permanent lookout for this kind of stuff.'
 show nao_v001 fuan_close at active
 show beatrice_v001 smile at inactive
 nao 'Even in the fashion world, there are fake brands that make and sell clothes and bags, but I wonder if there are organizations who cut these bad guys down.'
 hide beatrice_v001
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show nao_v001 fuan_close at inactive
 dlanor '............'
 show nao_v001 fuan at active
 show dlanor_v001 normal at inactive
 nao "What's wrong, Dlanor?"
 show dlanor_v001 normal_close at active
 show nao_v001 fuan at inactive
 dlanor 'Nothing... thank you so MUCH.'
 show nao_v001 odoroki at active
 show dlanor_v001 normal_close at inactive
 nao 'Huh...? Did you just thank me?'
 hide dlanor_v001
 show beatrice_v001 smile_close at mei_left
 with Dissolve(0.5)
 show beatrice_v001 smile_close at active
 show nao_v001 odoroki at inactive
 beatrice 'I am getting tired. I should not think while I am getting exhausted, as I would die permanently.'
 show nao_v001 fuan at active
 show beatrice_v001 smile_close at inactive
 nao "... It's an important rule to protect mystery, right?"
 hide beatrice_v001
 show dlanor_v001 smile at mei_left
 with Dissolve(0.5)
 show dlanor_v001 smile at active
 show nao_v001 fuan at inactive
 dlanor '...Nonetheless, something I must say to you before then, is that meeting with someone like you has made me incredibly HAPPY.'
 show dlanor_v001 smile_close at active
 show nao_v001 fuan at inactive
 dlanor 'I am glad to have been able to meet YOU.'
 show nao_v001 smile at active
 show dlanor_v001 smile_close at inactive
 nao 'Thank you as well for teaching me. Thanks to you, this has piqued my interest in mysteries even more.'
 hide dlanor_v001
 show beatrice_v001 normal_close at mei_left
 with Dissolve(0.5)
 show beatrice_v001 normal_close at active
 show nao_v001 smile at inactive
 beatrice "Mhm... While I'm still having fun, we'll have to part soon."
 show nao_v001 odoroki at active
 show beatrice_v001 normal_close at inactive
 nao "Eh-, we're already finished?"
 show beatrice_v001 smile at active
 show nao_v001 odoroki at inactive
 beatrice "That's right. Let us meet again, Nao."
 show nao_v001 odoroki at chara_shake_transform,active
 show beatrice_v001 smile at inactive
 nao 'Eh, aahhh...!!'
 call chapter_end from _call_chapter_end_21
 jump chara472001_03