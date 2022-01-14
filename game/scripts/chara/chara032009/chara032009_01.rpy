label chara032009_01:
 show black_background onlayer black
 $ event_store.current_event='chara032009'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara032009_01'
 $ persistent.menu_return='chara'
 camera:
  anchor (0.5, 0.5)
  pos (960, 540)
 scene
 stop music
 stop sound
 show expression 'images/bg/AdvBg_341.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_543_bird.wav'
 pause 1.0
 call wipeout_routine from _call_wipeout_routine_5
 stop sound
 show expression 'images/bg/AdvBg_351.png' as bg
 play music "<loop 2.36>audio/bgm/BGM_EVENT1.ogg"
 call wipein_routine from _call_wipein_routine_5
 show satoko_v002 fuan at mei_right
 show rika_v002 smile at mei_left
 with Dissolve(0.5)
 show rika_v002 smile at active
 show satoko_v002 fuan at inactive
 rika 'Meep. Satoko, did you find the book assigned for your book report?'
 show satoko_v002 fuan at active
 show rika_v002 smile at inactive
 satoko "...Hmm, I can't find it, but I think I did catch a glimpse of the title around this area."
 hide rika_v002
 show hanyuu_v002 fuan at mei_left
 with Dissolve(0.5)
 show hanyuu_v002 fuan at active
 show satoko_v002 fuan at inactive
 hanyuu 'Au au. Maybe somebody else checked it out and is reading it now?'
 show satoko_v002 fuan_close at active
 show hanyuu_v002 fuan at inactive
 satoko "If that's so, it can't be helped. It was the thinnest book, so I thought it would be an easy read... hm?"
 hide satoko_v002
 hide hanyuu_v002
 with Dissolve(0.2)
 show nao_v002 smile at mei_center
 with Dissolve(0.5)
 show nao_v002 smile at active
 nao 'Ah, Satoko, Rika, Hanyuu. What a concidence that I found you all here on my day off, huh?'
 hide nao_v002
 with Dissolve(0.2)
 show satoko_v002 smile at mei_right
 show nao_v002 smile at mei_left
 with Dissolve(0.5)
 show satoko_v002 smile at active
 show nao_v002 smile at inactive
 satoko 'Hello, Nao-san. Are you also here to get a book for your book report?'
 show nao_v002 smile at nod_transform,active
 show satoko_v002 smile at inactive
 nao 'Yeah. They say the book reports will also be screened for a prefecture-sponsored contest, so that seems a bit interesting.'
 hide satoko_v002
 show rika_v002 odoroki at mei_right
 with Dissolve(0.5)
 show rika_v002 odoroki at active
 show nao_v002 smile at inactive
 rika 'Meep. Nao must be very enthusiastic to aim for something like applying for a prefecture contest.'
 show nao_v002 fuan at active
 show rika_v002 odoroki at inactive
 nao "Well, it'd be nice if I had that level of work ethic. It's more of a goal for me. I'm not actually thinking about applying or anything."
 show rika_v002 smile at active
 show nao_v002 fuan at inactive
 rika "Don't say that. I think that with Nao's usual skills, you'd have a good chance."
 show nao_v002 smile_close at active
 show rika_v002 smile at inactive
 nao 'Ahaha, thanks. ...But in my case, I think I\'d get wound up in other issues applying to a contest in "this era" even before my work ethic would come into play...'
 show rika_v002 normal at active
 show nao_v002 smile_close at inactive
 rika '...? What did you just say, Nao?'
 show nao_v002 smile at active
 show rika_v002 normal at inactive
 nao "Oh, nothing. By the way, didn't you guys come here with Satoko to search for your books for the assignment today?"
 hide rika_v002
 show satoko_v002 fuan at mei_right
 with Dissolve(0.5)
 show satoko_v002 fuan at active
 show nao_v002 smile at inactive
 satoko "Yes... It's just, the book that I was relying on is apparently still being borrowed."
 hide satoko_v002
 show hanyuu_v002 fuan at mei_right
 with Dissolve(0.5)
 show hanyuu_v002 fuan at active
 show nao_v002 smile at inactive
 hanyuu "Au au, I don't know how much longer we'll be waiting for your book to come back, so I guess we'll have to check something else out."
 play audio 'audio/sfx/SE_556_netdown.wav'
 show nao_v002 odoroki at active
 show hanyuu_v002 fuan at inactive
 nao "...Is the book you're talking about, perhaps, this?"
 hide hanyuu_v002
 show satoko_v002 odoroki at mei_right
 with Dissolve(0.5)
 show satoko_v002 odoroki at active
 show nao_v002 odoroki at inactive
 satoko "Wh-, yeah... that's it! So it was Nao-san who was borrowing it. You beat me to it..."
 show nao_v002 smile at active
 show satoko_v002 odoroki at inactive
 nao "Ah-, but I just finished reading this book, so I was thinking I needed to return it to the bookshelf. You can have it if you'd like."
 hide satoko_v002
 show rika_v002 smile at mei_right
 with Dissolve(0.5)
 show rika_v002 smile at active
 show nao_v002 smile at inactive
 rika 'Is that really okay? Thank youuu, nipah♪'
 hide rika_v002
 show satoko_v002 fuan at mei_right
 with Dissolve(0.5)
 show satoko_v002 fuan at active
 show nao_v002 smile at inactive
 satoko "You saved me, Nao-san... ah, but won't this be an inconvenience since you'll have to write your book report without this?"
 show nao_v002 smile at active
 show satoko_v002 fuan at inactive
 nao "It's alright. There are other works that I enjoyed, so I can write the book report on one of those."
 show satoko_v002 odoroki at jump_transform,active
 show nao_v002 smile at inactive
 satoko 'Huh... then, why did you even read this book?'
 show nao_v002 smile at active
 show satoko_v002 odoroki at inactive
 nao "I thought I'd pick out a book to recommend to Kazuho and Miyuki. It seems like those two haven't chosen anything yet."
 show nao_v002 fuan at active
 show satoko_v002 odoroki at inactive
 nao "But for reference... coming from an underclassman level book, you'll carelessly get absorbed in reading this. It's one of my favorites that I've recently finished."
 hide satoko_v002
 show hanyuu_v002 odoroki at mei_right
 with Dissolve(0.5)
 show hanyuu_v002 odoroki at active
 show nao_v002 fuan at inactive
 hanyuu "Aah-, now that you say it, Nao's book mountain at home has upperclassman level books mixed in~!"
 hide hanyuu_v002
 show rika_v002 odoroki at mei_right
 with Dissolve(0.5)
 show rika_v002 odoroki at active
 show nao_v002 fuan at inactive
 rika "And she's finished reading all of those? ...What an amazing reading level. Nao is such a bookworm, inch inch~."
 show nao_v002 smile at active
 show rika_v002 odoroki at inactive
 nao "You say bookworm, but wasn't that more like an inchworm? Well anyway... here you go, Satoko."
 hide rika_v002
 show satoko_v002 fuan at mei_right
 with Dissolve(0.5)
 show satoko_v002 fuan at active
 show nao_v002 smile at inactive
 satoko "Thank you. At any rate... I'm jealous of Nao-san. I'm quite awful at reading books."
 show satoko_v002 fuan_close at deepbreath_transform,active
 show nao_v002 smile at inactive
 satoko 'Just skimming the lines with my eyes makes me sleepy like someone hypnotized me. Thanks to that, I get depressed every time... *sigh*...'
 hide nao_v002
 show hanyuu_v002 smile at mei_left
 with Dissolve(0.5)
 show hanyuu_v002 smile at active
 show satoko_v002 fuan_close at inactive
 hanyuu 'Au au, all it takes is having an open book in her hands for Satoko to let out a yawn~.'
 show satoko_v002 fuan at active
 show hanyuu_v002 smile at inactive
 satoko 'My curse has no chance of lifting... \nIf each page has at least three pictures... no, five pictures, I suppose I can put up with reading it, though.'
 hide hanyuu_v002
 show rika_v002 fuan at mei_left
 with Dissolve(0.5)
 show rika_v002 fuan at active
 show satoko_v002 fuan at inactive
 rika "Meep. That isn't even a novel. That's no different from a manga."
 hide rika_v002
 show nao_v002 smile at mei_left
 with Dissolve(0.5)
 show nao_v002 smile at active
 show satoko_v002 fuan at inactive
 nao "Ahaha. I'm sure that negative mindset towards books is causing you to having no interest in the first place."
 hide satoko_v002
 show hanyuu_v002 normal at mei_right
 with Dissolve(0.5)
 show hanyuu_v002 normal at active
 show nao_v002 smile at inactive
 hanyuu 'Au au? What does that mean?'
 show nao_v002 smile at active
 show hanyuu_v002 normal at inactive
 nao 'Book reports were originally an assignment made for children who had no interest in reading normally, so that they would experience a book and enjoy it, it seems.'
 show nao_v002 fuan_close at active
 show hanyuu_v002 normal at inactive
 nao "But now teachers and adults just assign specifc books to them, so getting to read has incidentally taken shape as something they're forced to do..."
 show nao_v002 fuan at active
 show hanyuu_v002 normal at inactive
 nao 'As a result, I fear the agony that kids feel while reading has multiplied.'
 hide hanyuu_v002
 show satoko_v002 fuan at mei_right
 with Dissolve(0.5)
 show satoko_v002 fuan at active
 show nao_v002 fuan at inactive
 satoko "That is... definitely a thing. Especially for me. I get a pessimistic feeling whenever I'm told to do an assignment or study."
 show satoko_v002 fuan_close at active
 show nao_v002 fuan at inactive
 satoko "If I'm told that it's okay to read my own favorite book and write what I think about it as I please, I feel like that would make reading much more fun."
 show nao_v002 smile at active
 show satoko_v002 fuan_close at inactive
 nao 'In that case, how about you choose a book completely unrelated to the contest and write a book report on that?'
 show nao_v002 smile at active
 show satoko_v002 fuan_close at inactive
 nao "Chie-sensei is a really understanding person, so I'm sure she'd understand if you discussed it with her, right?"
 show satoko_v002 smile at nod_transform,active
 show nao_v002 smile at inactive
 satoko "That's a great idea! I'm going to try talking to her as soon as possible tomorrow!"
 hide satoko_v002
 show rika_v002 smile at mei_right
 with Dissolve(0.5)
 show rika_v002 smile at active
 show nao_v002 smile at inactive
 rika "Meep, at any rate, Nao is awesome. I hadn't even considered that book reports had that kind of meaning behind them."
 show nao_v002 fuan at active
 show rika_v002 smile at inactive
 nao "Huh? Ah... I'm sorry, I kind of spoke in a conceited way, didn't I? I'm really just repeating what my school advisor told me."
 show nao_v002 smile at active
 show rika_v002 smile at inactive
 nao '"You become good at what you like doing," right? \nBecause the advisor said that to me, I started to like reading and such...'
 show nao_v002 smile at active
 show rika_v002 smile at inactive
 nao 'Rather than being assignments, I think of book reports as being pleasantly fun to write.'
 hide nao_v002
 hide rika_v002
 with Dissolve(0.2)
 stop music fadeout 0.5
 beatrice '..."{b}Hmm, how interesting. In that case, allow me to hear your thoughts on my works{/b}."'
 show nao_v002 odoroki at mei_center
 with Dissolve(0.5)
 show nao_v002 odoroki at active
 nao 'Huh...?'
 call chapter_end from _call_chapter_end_10
 jump chara032009_02