label chara032009_01:
 show black_background onlayer black
 $ event_store.current_event='chara032009'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara032009_01'
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
 show expression 'images/bg/AdvBg_341.png' as bg
 hide fade onlayer curtain
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_543_bird.wav'
 pause 1.0
 call wipeout_routine
 stop sound
 show expression 'images/bg/AdvBg_351.png' as bg
 play music "<loop 2.36>audio/bgm/BGM_EVENT1.ogg"
 call wipein_routine
 show rika_v002 smile at mei_left
 show satoko_v002 fuan at mei_right
 with Dissolve(0.5)
 show satoko_v002 fuan at inactive
 show rika_v002 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep. Satoko, did you find the book assigned for your book report?'
 show rika_v002 smile at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "...Hmm, I can't find it, but I think I did catch a glimpse of the title around this area."
 hide rika_v002
 show hanyuu_v002 fuan at mei_left
 with Dissolve(0.5)
 show satoko_v002 fuan at inactive
 show hanyuu_v002 fuan at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Au au. Maybe somebody else checked it out and is reading it now?'
 show hanyuu_v002 fuan at inactive
 show satoko_v002 fuan_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "If that's so, it can't be helped. It was the thinnest book, so I thought it would be an easy read... hm?"
 hide satoko_v002
 hide hanyuu_v002
 with Dissolve(0.2)
 show nao_v002 smile at mei_center
 with Dissolve(0.5)
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Ah, Satoko, Rika, Hanyuu. What a concidence that I found you all here on my day off, huh?'
 hide nao_v002
 with Dissolve(0.2)
 show nao_v002 smile at mei_left
 show satoko_v002 smile at mei_right
 with Dissolve(0.5)
 show nao_v002 smile at inactive
 show satoko_v002 smile at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Hello, Nao-san. Are you also here to get a book for your book report?'
 show satoko_v002 smile at inactive
 show nao_v002 smile at active
 show nao_v002 smile at nod_transform
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Yeah. They say the book reports will also be screened for a prefecture-sponsored contest, so that seems a bit interesting.'
 hide satoko_v002
 show rika_v002 odoroki at mei_right
 with Dissolve(0.5)
 show nao_v002 smile at inactive
 show rika_v002 odoroki at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Meep. Nao must be very enthusiastic to aim for something like applying for a prefecture contest.'
 show rika_v002 odoroki at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Well, it'd be nice if I had that level of work ethic. It's more of a goal for me. I'm not actually thinking about applying or anything."
 show nao_v002 fuan at inactive
 show rika_v002 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Don't say that. I think that with Nao's usual skills, you'd have a good chance."
 show rika_v002 smile at inactive
 show nao_v002 smile_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Ahaha, thanks. ...But in my case, I think I\'d get wound up in other issues applying to a contest in "this era" even before my work ethic would come into play...'
 show nao_v002 smile_close at inactive
 show rika_v002 normal at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") '...? What did you just say, Nao?'
 show rika_v002 normal at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Oh, nothing. By the way, didn't you guys come here with Satoko to search for your books for the assignment today?"
 hide rika_v002
 show satoko_v002 fuan at mei_right
 with Dissolve(0.5)
 show nao_v002 smile at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Yes... It's just, the book that I was relying on is apparently still being borrowed."
 hide satoko_v002
 show hanyuu_v002 fuan at mei_right
 with Dissolve(0.5)
 show nao_v002 smile at inactive
 show hanyuu_v002 fuan at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") "Au au, I don't know how much longer we'll be waiting for your book to come back, so I guess we'll have to check something else out."
 play audio 'audio/sfx/SE_556_netdown.wav'
 show hanyuu_v002 fuan at inactive
 show nao_v002 odoroki at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "...Is the book you're talking about, perhaps, this?"
 hide hanyuu_v002
 show satoko_v002 odoroki at mei_right
 with Dissolve(0.5)
 show nao_v002 odoroki at inactive
 show satoko_v002 odoroki at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Wh-, yeah... that's it! So it was Nao-san who was borrowing it. You beat me to it..."
 show satoko_v002 odoroki at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Ah-, but I just finished reading this book, so I was thinking I needed to return it to the bookshelf. You can have it if you'd like."
 hide satoko_v002
 show rika_v002 smile at mei_right
 with Dissolve(0.5)
 show nao_v002 smile at inactive
 show rika_v002 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") 'Is that really okay? Thank youuu, nipah♪'
 hide rika_v002
 show satoko_v002 fuan at mei_right
 with Dissolve(0.5)
 show nao_v002 smile at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "You saved me, Nao-san... ah, but won't this be an inconvenience since you'll have to write your book report without this?"
 show satoko_v002 fuan at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "It's alright. There are other works that I enjoyed, so I can write the book report on one of those."
 show nao_v002 smile at inactive
 show satoko_v002 odoroki at active
 show satoko_v002 odoroki at jump_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Huh... then, why did you even read this book?'
 show satoko_v002 odoroki at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "I thought I'd pick out a book to recommend to Kazuho and Miyuki. It seems like those two haven't chosen anything yet."
 show satoko_v002 odoroki at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "But for reference... coming from an underclassman level book, I carelessly got absorbed in reading this. It's one of my favorites that I've recently finished."
 hide satoko_v002
 show hanyuu_v002 odoroki at mei_right
 with Dissolve(0.5)
 show nao_v002 fuan at inactive
 show hanyuu_v002 odoroki at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") "Aah-, now that you say it, Nao's book mountain at home has upperclassman level books mixed in~!"
 hide hanyuu_v002
 show rika_v002 odoroki at mei_right
 with Dissolve(0.5)
 show nao_v002 fuan at inactive
 show rika_v002 odoroki at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "And she's finished reading all of those? ...What an amazing reading level. Nao is such a bookworm, inch inch~."
 show rika_v002 odoroki at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "You say bookworm, but wasn't that more like an inchworm? \nWell, anyways... here you go, Satoko."
 hide rika_v002
 show satoko_v002 fuan at mei_right
 with Dissolve(0.5)
 show nao_v002 smile at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "Thank you. At any rate... I'm jealous of Nao-san. I'm quite awful at reading books."
 show nao_v002 smile at inactive
 show satoko_v002 fuan_close at active
 show satoko_v002 fuan_close at deepbreath_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'Just skimming the lines with my eyes makes me sleepy like someone hypnotized me. Thanks to that, I get depressed every time... *sigh*...'
 hide nao_v002
 show hanyuu_v002 smile at mei_left
 with Dissolve(0.5)
 show satoko_v002 fuan_close at inactive
 show hanyuu_v002 smile at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Au au, all it takes is having an open book in her hands for Satoko to let out a yawn~.'
 show hanyuu_v002 smile at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") 'My curse has no chance of lifting... \nIf each page has at least three pictures... no, five pictures, I suppose I can put up with reading it, though.'
 hide hanyuu_v002
 show rika_v002 fuan at mei_left
 with Dissolve(0.5)
 show satoko_v002 fuan at inactive
 show rika_v002 fuan at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Meep. That isn't even a novel. That's no different from a manga."
 hide rika_v002
 show nao_v002 smile at mei_left
 with Dissolve(0.5)
 show satoko_v002 fuan at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Ahaha. I'm sure that negative mindset towards books is causing you to having no interest in the first place."
 hide satoko_v002
 show hanyuu_v002 normal at mei_right
 with Dissolve(0.5)
 show nao_v002 smile at inactive
 show hanyuu_v002 normal at active
 Character('Hanyuu Furude',ctc="ctcArrow", ctc_position="fixed") 'Au au? What does that mean?'
 show hanyuu_v002 normal at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Book reports were originally an assignment made for children who had no interest in reading normally, so that they would experience a book and enjoy it, it seems.'
 show hanyuu_v002 normal at inactive
 show nao_v002 fuan_close at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "But now teachers and adults just assign specifc books to them, so getting to read has incidentally taken shape as something they're forced to do..."
 show hanyuu_v002 normal at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'As a result, I fear the agony that kids feel while reading has multiplied.'
 hide hanyuu_v002
 show satoko_v002 fuan at mei_right
 with Dissolve(0.5)
 show nao_v002 fuan at inactive
 show satoko_v002 fuan at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "That is... definitely a thing. Especially for me. I get a pessimistic feeling whenever I'm told to do an assignment or study."
 show nao_v002 fuan at inactive
 show satoko_v002 fuan_close at active
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "If I'm told that it's okay to read my own favorite book and write what I think about it as I please, I feel like that would make reading much more fun."
 show satoko_v002 fuan_close at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'In that case, how about you choose a book completely unrelated to the contest and write a book report on that?'
 show satoko_v002 fuan_close at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Chie-sensei is a really understanding person, so I'm sure she'd understand if you discussed it with her, right?"
 show nao_v002 smile at inactive
 show satoko_v002 smile at active
 show satoko_v002 smile at nod_transform
 Character('Satoko Houjou',ctc="ctcArrow", ctc_position="fixed") "That's a great idea! I'm going to try talking to her as soon as possible tomorrow!"
 hide satoko_v002
 show rika_v002 smile at mei_right
 with Dissolve(0.5)
 show nao_v002 smile at inactive
 show rika_v002 smile at active
 Character('Rika Furude',ctc="ctcArrow", ctc_position="fixed") "Meep, at any rate, Nao is awesome. I hadn't even considered that book reports had that kind of meaning behind them."
 show rika_v002 smile at inactive
 show nao_v002 fuan at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") "Huh? Ah... I'm sorry, I kind of spoke in a conceited way, didn't I? I'm really just repeating what my school advisor told me."
 show rika_v002 smile at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") '"You become good at what you like doing," right? \nBecause the advisor said that to me, I started to like reading and such...'
 show rika_v002 smile at inactive
 show nao_v002 smile at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Rather than being assignments, I think of book reports as being pleasantly fun to write.'
 hide nao_v002
 hide rika_v002
 with Dissolve(0.2)
 stop music fadeout 0.5
 Character('????',ctc="ctcArrow", ctc_position="fixed") '..."{b}Hmm, how interesting. In that case, allow me to hear your thoughts on my works{/b}."'
 show nao_v002 odoroki at mei_center
 with Dissolve(0.5)
 show nao_v002 odoroki at active
 Character('Nao Houtani',ctc="ctcArrow", ctc_position="fixed") 'Huh...?'
 call chapter_end
 jump chara032009_02