label chara472001_02:
 show black_background onlayer black
 $ event_store.current_event='chara472001'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara472001_02'
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
 show expression 'images/bg/AdvBg_2190.png' as bg
 play music "<loop 0>audio/bgm/BGM_QUEST6_COLLAB2.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show dlanor_v001 normal at mei_left
 show nao_v001 normal at mei_right
 with Dissolve(0.5)
 show nao_v001 normal at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") '"Knox\'s Ten Commandments", or "Knox\'s Decalogue", promise to serve and protect MYSTERY. To say they are commandments is no EXAGGERATION.'
 show dlanor_v001 normal at inactive
 show nao_v001 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Commandments...?'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 hide nao_v001
 hide dlanor_v001
 with Dissolve(0.2)
 stop sound
 show expression 'images/card/Card_472001.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'YES. Knox\'s 1st: "It is forbidden for the culprit to be anyone not mentioned in the early part of the STORY."'
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'Knox\'s 2nd: "It is forbidden for supernatural agencies to be used as a detective TECHNIQUE."'
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'Knox\'s 3rd: "It is forbidden for hidden passages to EXIST."'
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'Knox\'s 4th: "It is forbidden for unknown drugs or hard to understand scientific devices to be USED."'
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'Knox\'s 6th: "It is forbidden for accident or intuition to be employed as a detective TECHNIQUE."'
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'Knox\'s 7th: "It is forbidden for the detective to be the CULPRIT."'
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'Knox\'s 8th: "It is forbidden for the case to be resolved with clues that are not PRESENTED."'
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'Knox\'s 9th: "It is permitted for observers to let their own conclusions and explanations be HEARD."'
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'Knox\'s 10th: "It is forbidden for a character to disguise themselves as another without CLUES."'
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'I see. Ten rules make up the Ten Commandments... wait, what happened to number 5?'
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'It is OMITTED. As such, please refrain from referencing IT.'
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'I sort of wanted to hear why it is omitted... but I understand.'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 stop sound
 show expression 'images/bg/AdvBg_2190.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 show beatrice_v001 normal at mei_left
 show nao_v001 normal_close at mei_right
 with Dissolve(0.5)
 show nao_v001 normal_close at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'So, Nao, after hearing about "Knox\'s Ten Commandments" for the first time, what are your thoughts?'
 show beatrice_v001 normal at inactive
 show nao_v001 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Right... if you want me to speak my thoughts openly, it gave me the impression that they\'re a bit strict. I was like, "Mystery really has those types of limitations?".'
 show nao_v001 fuan at inactive
 show beatrice_v001 futeki at active
 show beatrice_v001 futeki at updown_shake_transform
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "*cackle*cackle*! I guess that's because when you {i}have{/i} read mystery, you have only done it in the casual sense?"
 show beatrice_v001 futeki at inactive
 show nao_v001 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I'm not so sure about reading casually... because there were so many difficult expressions and settings, I would clearly be giving it my all just trying to read along with the story."
 show nao_v001 fuan at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Then, in the midst of reading a story, have you never tried to reason out on the spot who the culprit is?'
 show beatrice_v001 smile at inactive
 show nao_v001 fuan_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I've been surprised when I finally hear about the culprit or the trick, but I might not have done much reasoning... maybe."
 show beatrice_v001 smile at inactive
 show nao_v001 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'So when Beatrice reads mystery, I wonder if she reasons out who the culprit is?'
 play audio 'audio/sfx/SE_226_shine.wav'
 show nao_v001 normal at inactive
 show beatrice_v001 futeki at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'But of course! That is the true thrill behind mystery!'
 show beatrice_v001 futeki at inactive
 show nao_v001 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'I see... but turning the pages and following along just behind the detective in the story is so fun in and of itself though.'
 show nao_v001 smile at inactive
 show beatrice_v001 fuan at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Ah-, mmm... but is it not common courtesy to go into a mystery with the intention to solve it?'
 show beatrice_v001 fuan at inactive
 show nao_v001 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'With a novel, the moment you open the book, your very first "action" is to start reading.'
 show beatrice_v001 fuan at inactive
 show nao_v001 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "In the midst of the action of reading, however the reader decides to enjoy that process, be it by solving riddles or not, it's their liberty to do as they please, no?"
 show nao_v001 smile at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "...Hmm, we don't see eye to eye here. I've heard that you are a bookworm, but the ways in which we enjoy reading are dissimilar."
 hide beatrice_v001
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show nao_v001 smile at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") "...In this argument, the odds are against Lady Beatrice's SIDE. Pulling out of this would be wise for HER."
 show dlanor_v001 normal at inactive
 show nao_v001 odoroki at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Ah, but I wasn't particularly saying that I think Beatrice's method of having fun is absolutely wrong? I just wanted to say that my way was different."
 show dlanor_v001 normal at inactive
 show nao_v001 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'And anyways... I understood what she said earlier. If we were to use my reading style, even if mystery novels had no rules, there would be no issue.'
 show dlanor_v001 normal at inactive
 show nao_v001 normal_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "But then, for someone who tackles mystery novels with Beatrice's precise approach, rules are a prerequisite."
 show dlanor_v001 normal at inactive
 show nao_v001 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Even in games, if you play without rules, you lose both strategy and tactics... "Knox\'s Decalogue" is for that purpose.'
 show nao_v001 normal at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'AGREED. For people who let the story do the telling and for people who solve the riddle head-on, "Knox\'s Decalogue" is something necessary to balance the fairness between these two PARTIES.'
 hide dlanor_v001
 show beatrice_v001 normal at mei_left
 with Dissolve(0.5)
 show nao_v001 normal at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Mhm. If there were no rules, you would have complete freedom setting up the mystery, but then the detective who wants to tackle the mystery with reasoning loses his lifeline. He would not understand how to continue, nor be able to see his goal.'
 show nao_v001 normal at inactive
 show beatrice_v001 normal_close at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'By the way, when there is an inconsistency in the rules related to the story, we call this a "logic error".'
 show nao_v001 normal at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'In a logic battle, "logic errors" are essentially a foul... \nThis is a matter that should be avoided with certainty.'
 show beatrice_v001 normal at inactive
 show nao_v001 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...So it's kind of like how it's wrong when two people are playing a PvP game in an arcade and the loser hits the winner, right?"
 show nao_v001 normal at inactive
 show beatrice_v001 fuan at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Uh, mm...? I have no knowledge of what a PvP is, though, so I cannot really assign meaning to it...'
 show beatrice_v001 fuan at inactive
 show nao_v001 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Ah, but... returning to the question of how the structure of "Knox\'s Decalogue" was formed, what ultimately led to it being made?'
 hide beatrice_v001
 show dlanor_v001 normal_close at mei_left
 with Dissolve(0.5)
 show nao_v001 fuan at inactive
 show dlanor_v001 normal_close at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") '...That is due to the fact that the past was an era where mysteries with too much freedom REIGNED.'
 show dlanor_v001 normal_close at inactive
 show nao_v001 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Mysteries with too much freedom...?'
 show nao_v001 normal at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'Before "Knox\'s Decalogue" was structured, mysteries that were unsolvable by normal and fair means were a rampant issue... so this lowered the quality of the entire GENRE.'
 show nao_v001 normal at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'For example, culprits would suddenly appear towards the latter half of the story, detectives would use psychic powers to solve mysteries... and secret passageways would exist for locked-room MURDERS.'
 show nao_v001 normal at inactive
 show dlanor_v001 normal_close at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'Furthermore, unimaginable medicines and scientific devices that were unknown to readers would unfairly make their DEBUT...'
 show nao_v001 normal at inactive
 show dlanor_v001 normal_close at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'Detectives would solve incidents by coincidence or through the sixth SENSE. The culprit would be the detective in reality, and he would lie in his perspective as a TRICK.'
 show nao_v001 normal at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'And moreover, clues would appear out of nowhere with no explanation... a character Mrs. A would actually be Mrs. B in disguise, et CETERA...'
 show dlanor_v001 normal at inactive
 show nao_v001 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...I see. With those things being done, someone reading could never make a conjecture through normal means.'
 show dlanor_v001 normal at inactive
 show nao_v001 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...Oh? But if you really think about it, the logic in the 9th commandment is a bit different in nature, right?'
 show nao_v001 normal at inactive
 show dlanor_v001 odoroki at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'The difference... IS?'
 show dlanor_v001 odoroki at inactive
 show nao_v001 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Like, right next to it is the 10th one, and that one is listed as "something you shouldn\'t do", whereas the 9th is "something that you are permitted to do", right?'
 show dlanor_v001 odoroki at inactive
 show nao_v001 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Knox\'s 9th: "It is permitted for observers to let their own conclusions and explanations be heard."'
 show dlanor_v001 odoroki at inactive
 show nao_v001 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'The "observers" can be seen as characters in the story, right?'
 show nao_v001 normal at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'YES.'
 show dlanor_v001 normal at inactive
 show nao_v001 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "So basically, if I'm explaining this correctly, it makes me think that a character can tell a lie and it wouldn't matter, though...?"
 hide dlanor_v001
 show beatrice_v001 normal at mei_left
 with Dissolve(0.5)
 show nao_v001 fuan at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'If you only look at that rule, I see your point... \nHowever, the detective must not be the culprit.'
 show beatrice_v001 normal at inactive
 show nao_v001 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Rule 7 prevents it, right? But I wonder if that also prevents the detective from telling lies?'
 hide beatrice_v001
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show nao_v001 normal at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'It DOES, they must not tell LIES. Rule 9 impedes this from HAPPENING.'
 show dlanor_v001 normal at inactive
 show nao_v001 odoroki at active
 show nao_v001 odoroki at jump_transform
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Huh? But for it to be permitted for one's own conclusions and explanations to be heard... ah."
 hide dlanor_v001
 show beatrice_v001 futeki at mei_left
 with Dissolve(0.5)
 show nao_v001 odoroki at inactive
 show beatrice_v001 futeki at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") '*cackle*cackle*! She has finally realized.'
 show beatrice_v001 futeki at inactive
 show nao_v001 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Okay, so... the observers are permitted, but the {i}detective{/i} isn't."
 hide beatrice_v001
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show nao_v001 sinken at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") '...Exactly SO. You understood WELL.'
 show dlanor_v001 normal at inactive
 show nao_v001 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'I see... with that in place, the detective cannot tell a lie at all.'
 show nao_v001 normal at inactive
 show dlanor_v001 normal_close at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'Not NECESSARILY. There are EXCEPTIONS. In the case that the detective tells a lie unconsciously, "Knox\'s Decalogue" would allow IT.'
 show dlanor_v001 normal_close at inactive
 show nao_v001 odoroki at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'For example?'
 hide dlanor_v001
 show beatrice_v001 smile at mei_left
 with Dissolve(0.5)
 show nao_v001 odoroki at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Right. With you here as the detective... are you familiar with P??tiss?'
 show beatrice_v001 smile at inactive
 show nao_v001 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "No, I'm not. What is that?"
 show nao_v001 normal at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'It is a variety of black tea. It has a dark shade and a distinct smell of brandy.'
 show beatrice_v001 smile at inactive
 show nao_v001 odoroki at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Ohh...'
 hide beatrice_v001
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show nao_v001 odoroki at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'That was a LIE.'
 camera at screenshake_transform
 pause 0.0
 show dlanor_v001 normal at inactive
 show nao_v001 sinken at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Huhhh...?'
 hide dlanor_v001
 show beatrice_v001 futeki at mei_left
 with Dissolve(0.5)
 show nao_v001 sinken at inactive
 show beatrice_v001 futeki at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "*cackle*cackle*cackle*... It's actually something more along the lines of deep-fried gyoza, served as a tea party snack. It goes along tastily with Dinbura specifically."
 show beatrice_v001 futeki at inactive
 show nao_v001 fuan_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'I see. One time I was inside a huge supermarket, trying to search for whether or not they were selling that. ...After thinking of that, I understood this conversation.'
 show beatrice_v001 futeki at inactive
 show nao_v001 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'With me as the observer and as the detective, if I believe what Beatrice says and mention it to another person... It cannot be a lie.'
 show beatrice_v001 futeki at inactive
 show nao_v001 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "In this case, what's important is the definition of lie. What constitutes a lie... what could it be? Hm..."
 hide nao_v001
 hide beatrice_v001
 with Dissolve(0.2)
 show dlanor_v001 odoroki at mei_center
 with Dissolve(0.5)
 show dlanor_v001 odoroki at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") '...I am AMAZED. You have truly grasped this concept QUICKLY. Even as a young girl, your wisdom is truly AMUSING...'
 hide dlanor_v001
 with Dissolve(0.2)
 show beatrice_v001 smile at mei_left
 show nao_v001 smile at mei_right
 with Dissolve(0.5)
 show nao_v001 smile at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Nao seems to have a knack for mystery. But most of all, studying it from here on out is a must to keep that up.'
 show beatrice_v001 smile at inactive
 show nao_v001 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'My, really? If you say it to me like that, that makes me happy.'
 show beatrice_v001 smile at inactive
 show nao_v001 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'But yeah, if I had never met with you guys, I suppose I would have never known about "Knox\'s Decalogue".'
 show beatrice_v001 smile at inactive
 show nao_v001 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Thank you, Dlanor, for teaching me of such fun rules. If there was something like that all along, I wish I had known sooner.'
 hide beatrice_v001
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show nao_v001 smile at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") '............'
 show dlanor_v001 normal at inactive
 show nao_v001 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Dlanor?'
 hide dlanor_v001
 show beatrice_v001 futeki at mei_left
 with Dissolve(0.5)
 show nao_v001 fuan at inactive
 show beatrice_v001 futeki at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") '*cackle*cackle*! Lady Dlanor is quite surprised!'
 show nao_v001 fuan at inactive
 show beatrice_v001 futeki_close at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'To tell the truth, Lady Dlanor\'s father was the one who created "Knox\'s Decalogue".'
 show beatrice_v001 futeki_close at inactive
 show nao_v001 odoroki at active
 show nao_v001 odoroki at jump_transform
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Huh...? Dlanor's father made this?"
 hide beatrice_v001
 show dlanor_v001 normal_close at mei_left
 with Dissolve(0.5)
 show nao_v001 odoroki at inactive
 show dlanor_v001 normal_close at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") '...Yes, that is RIGHT.'
 show dlanor_v001 normal_close at inactive
 show nao_v001 normal at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'I see. I thought that some reader made "Knox\'s Decalogue", but... right, there are also people on the author\'s side.'
 hide dlanor_v001
 show beatrice_v001 normal at mei_left
 with Dissolve(0.5)
 show nao_v001 normal at inactive
 show beatrice_v001 normal at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'Hoh. What does that thought entail?'
 show beatrice_v001 normal at inactive
 show nao_v001 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Like, if an author declared he was following "Knox\'s Decalogue" at the beginning, people who know the decalogue would understand the mystery was designed to be solved, right?'
 show beatrice_v001 normal at inactive
 show nao_v001 smile_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '...I see. So that\'s why "Knox\'s Decalogue" was not discarded as a hindrance, but stuck as a rule for authors to adhere to.'
 show beatrice_v001 normal at inactive
 show nao_v001 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "It's like an important brand logo which guarantees that we're being fair to the readers."
 hide beatrice_v001
 show dlanor_v001 odoroki at mei_left
 with Dissolve(0.5)
 show nao_v001 smile at inactive
 show dlanor_v001 odoroki at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") '............'
 show dlanor_v001 odoroki at inactive
 show nao_v001 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "But it's hard to protect a brand; because if you have a fake product, it's bad for the reputation of the original."
 show dlanor_v001 odoroki at inactive
 show nao_v001 fuan_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "My mom has also worried about this. Even if a fake version is sold, the focal point of the anger would be on the original seller. It's such an unreasonable concept."
 hide dlanor_v001
 show beatrice_v001 smile at mei_left
 with Dissolve(0.5)
 show nao_v001 fuan_close at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "...What an interesting analogy. it's unreasonable for those who follow the rules to lose out."
 show nao_v001 fuan_close at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "Therefore, this person's job is to protect those who craft mysteries that follow the rules. All faulty mysteries are then cut down completely."
 show beatrice_v001 smile at inactive
 show nao_v001 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Ohh... is that so? How enviable of a story it is, hearing that people have a role to be on permanent lookout for this kind of stuff.'
 show beatrice_v001 smile at inactive
 show nao_v001 fuan_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Even in the fashion world, there are fake brands that make and sell clothes and bags, but I wonder if there are organizations who cut these bad guys down.'
 hide beatrice_v001
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show nao_v001 fuan_close at inactive
 show dlanor_v001 normal at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") '............'
 show dlanor_v001 normal at inactive
 show nao_v001 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "What's wrong, Dlanor?"
 show nao_v001 fuan at inactive
 show dlanor_v001 normal_close at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'Nothing... thank you so MUCH.'
 show dlanor_v001 normal_close at inactive
 show nao_v001 odoroki at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Huh...? Did you just thank me?'
 hide dlanor_v001
 show beatrice_v001 smile_close at mei_left
 with Dissolve(0.5)
 show nao_v001 odoroki at inactive
 show beatrice_v001 smile_close at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") 'I am getting tired. I should not think while exhausted, as I would end up dying permanently.'
 show beatrice_v001 smile_close at inactive
 show nao_v001 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...Following the rules in a mystery is tough work, isn't it?"
 hide beatrice_v001
 show dlanor_v001 smile at mei_left
 with Dissolve(0.5)
 show nao_v001 fuan at inactive
 show dlanor_v001 smile at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") '...Nonetheless, something I must say to you before we part, is that meeting with someone like you has made me incredibly HAPPY.'
 show nao_v001 fuan at inactive
 show dlanor_v001 smile_close at active
 Character('Dlanor',ctc="ctcArrow", ctc_position="fixed") 'I am glad to have been able to meet YOU.'
 show dlanor_v001 smile_close at inactive
 show nao_v001 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Thank you as well for teaching me. Thanks to you, this has piqued my interest in mysteries even more.'
 hide dlanor_v001
 show beatrice_v001 normal_close at mei_left
 with Dissolve(0.5)
 show nao_v001 smile at inactive
 show beatrice_v001 normal_close at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "Mhm... While I'm still having fun, we'll have to part soon."
 show beatrice_v001 normal_close at inactive
 show nao_v001 odoroki at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Eh-, we're already finished?"
 show nao_v001 odoroki at inactive
 show beatrice_v001 smile at active
 Character('Beatrice',ctc="ctcArrow", ctc_position="fixed") "That's right. Let us meet again, Nao."
 show beatrice_v001 smile at inactive
 show nao_v001 odoroki at active
 show nao_v001 odoroki at chara_shake_transform
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Eh, aahhh...!!'
 call chapter_end
 jump chara472001_03