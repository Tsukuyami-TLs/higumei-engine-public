label chara032009_01:
 show black_background onlayer black
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_341.png' as bg
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_543_bird.wav'
 pause 1.0
 call wipeout_routine
 stop sound
 scene expression "#000"
 play music 'audio/bgm/BGM_EVENT1.ogg'
 show expression 'images/bg/AdvBg_351.png' as bg
 call wipein_routine
 show satoko_v002 fuan at mei_right
 show rika_v002 smile at mei_left
 with Dissolve(0.5)
 show rika_v002 smile at active
 show satoko_v002 fuan at inactive
 rika 'Meep. Satoko, did you find the book for your book report?'
 show satoko_v002 fuan at active
 show rika_v002 smile at inactive
 satoko "...Well, I don't see it here, but I remember seeing the cover of it around here somewhere."
 hide rika_v002
 show hanyuu_v002 fuan at mei_left
 with Dissolve(0.5)
 show hanyuu_v002 fuan at active
 show satoko_v002 fuan at inactive
 hanyuu 'Au au. Maybe somebody else checked it out and is reading it now?'
 show satoko_v002 fuan_close at active
 show hanyuu_v002 fuan at inactive
 satoko "If that's the case, it can't be helped. It was the thinnest book, so I thought it was reasonable."
 hide satoko_v002
 hide hanyuu_v002
 with Dissolve(0.2)
 show nao_v002 smile at mei_center
 with Dissolve(0.5)
 show nao_v002 smile at active
 nao 'Ah, Satoko, Rika, Hanyuu. What a concidence that I found you all here on our day off.'
 hide nao_v002
 with Dissolve(0.2)
 show satoko_v002 smile at mei_right
 show nao_v002 smile at mei_left
 with Dissolve(0.5)
 show satoko_v002 smile at active
 show nao_v002 smile at inactive
 satoko 'Hello, Nao. Are you also here to get a book for your book report?'
 show nao_v002 smile at nod_transform,active
 show satoko_v002 smile at inactive
 nao "Yes. I've heard that it was previously selected for a prefecture-sponsored contest, so it looked a bit interesting."
 hide satoko_v002
 show rika_v002 odoroki at mei_right
 with Dissolve(0.5)
 show rika_v002 odoroki at active
 show nao_v002 smile at inactive
 rika 'Meep. Nao must have lots of enthusiasm to aim for something like applying for the prefecture contest.'
 show nao_v002 fuan at active
 show rika_v002 odoroki at inactive
 nao "Well, If I had that level of workmanship it would be nice. It's more so like a goal for me. I'm not actually thinking about applying or anything."
 show rika_v002 smile at active
 show nao_v002 fuan at inactive
 rika "It's not really like that. I think that with Nao's usual strength, it would become a fair fight."
 show nao_v002 smile_close at active
 show rika_v002 smile at inactive
 nao 'Ahaha, thanks. ...But in my case, it seems like I would run into issues with workmanship among other things in the face of "this era\'s" contest application.'
 show rika_v002 normal at active
 show nao_v002 smile_close at inactive
 rika '...? What did you just say, Nao?'
 show nao_v002 smile at active
 show rika_v002 normal at inactive
 nao "Oh, it's nothing. By the way, didn't you guys come here with Satoko to search for your books for the assignment today?"
 hide rika_v002
 show satoko_v002 fuan at mei_right
 with Dissolve(0.5)
 show satoko_v002 fuan at active
 show nao_v002 smile at inactive
 satoko "Yes... It's just, the book that I was relying on is apparently still being loaned."
 hide satoko_v002
 show hanyuu_v002 fuan at mei_right
 with Dissolve(0.5)
 show hanyuu_v002 fuan at active
 show nao_v002 smile at inactive
 hanyuu "Au au, I don't know how much longer we'll be waiting for your book to come back, so I guess we'll have to borrow someone else's."
 play audio 'audio/sfx/SE_556_netdown.wav'
 show nao_v002 odoroki at active
 show hanyuu_v002 fuan at inactive
 nao "...Is the book you're talking about, perhaps, this?"
 hide hanyuu_v002
 show satoko_v002 odoroki at mei_right
 with Dissolve(0.5)
 show satoko_v002 odoroki at active
 show nao_v002 odoroki at inactive
 satoko "Wh-, yeah... that's it! So it was Nao-san who started borrowing it. That's finally done with..."
 show nao_v002 smile at active
 show satoko_v002 odoroki at inactive
 nao "Ah-, but I just finished reading this book, so I needed to return it to the bookshelf, or so I thought. You can have it if you'd like."
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
 satoko "You saved me, Nao-san... ah, but won't this be an inconvenience somehow since Nao-san will write her book report with this?"
 show nao_v002 smile at active
 show satoko_v002 fuan at inactive
 nao "It's alright. Since there was another work that I enjoyed, I'll make it so I write the book report on that."
 show satoko_v002 odoroki at jump_transform,active
 show nao_v002 smile at inactive
 satoko 'Huh... then, why is it that you even read this book?'
 show nao_v002 smile at active
 show satoko_v002 odoroki at inactive
 nao "I thought I'd pick out a book that Kazuho and Miyuki recommended to me. It seems like those two haven't chosen yet even so."
 show nao_v002 fuan at active
 show satoko_v002 odoroki at inactive
 nao "Just... as a reference, going from an underclassman level book to this, I subconsciously got carelessly absorbed in reading it. It's almost one of my favorites that I've finished reading."
 hide satoko_v002
 show hanyuu_v002 odoroki at mei_right
 with Dissolve(0.5)
 show hanyuu_v002 odoroki at active
 show nao_v002 fuan at inactive
 hanyuu "Aah-, now that you say it, Nao's book mountain at home has a underclassman level assignment books mixed in~!"
 hide hanyuu_v002
 show rika_v002 odoroki at mei_right
 with Dissolve(0.5)
 show rika_v002 odoroki at active
 show nao_v002 fuan at inactive
 rika 'Are you completely done reading that? ...What an amazing reading level. Nao is such a bookworm, inch inch~.'
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
 satoko 'Just from following along the lines with my eyes, it makes me sleepy like someone hypnotized me. Thanks to that, I get depressed every time... haaah...'
 hide nao_v002
 show hanyuu_v002 smile at mei_left
 with Dissolve(0.5)
 show hanyuu_v002 smile at active
 show satoko_v002 fuan_close at inactive
 hanyuu 'Au au, Satoko just has to have it in her hands and open it for her to let out a yawn~.'
 show satoko_v002 fuan at active
 show hanyuu_v002 smile at inactive
 satoko 'My curse has no chance to lift...  If each page has at least 3 pictures, no, 5 pictures, I suppose I can put up with reading it.'
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
 nao "Ahaha. I'm sure it's due to you having that negative mindset towards books that leads you to having no interest going into it."
 hide satoko_v002
 show hanyuu_v002 normal at mei_right
 with Dissolve(0.5)
 show hanyuu_v002 normal at active
 show nao_v002 smile at inactive
 hanyuu 'Au au? What does that mean?'
 show nao_v002 smile at active
 show hanyuu_v002 normal at inactive
 nao 'Book reports originally were an assignment made for children who had no interest in reading normally, so that they could hold a book and enjoy it, it seems.'
 show nao_v002 fuan_close at active
 show hanyuu_v002 normal at inactive
 nao "But now, teachers and adults consciously choose these assignment books, and now making kids read has incidentally taken shape as something they're forced to do."
 show nao_v002 fuan at active
 show hanyuu_v002 normal at inactive
 nao 'Contrarily, I fear the agony that kids feel while reading has multiplied.'
 hide hanyuu_v002
 show satoko_v002 fuan at mei_right
 with Dissolve(0.5)
 show satoko_v002 fuan at active
 show nao_v002 fuan at inactive
 satoko "Clearly... that is a thing. Especially for me, I get pessimistic feeling whenever I'm told to do an assignment or study."
 show satoko_v002 fuan_close at active
 show nao_v002 fuan at inactive
 satoko "If I'm told that it's okay to read my own favorite book and write what I think about it as I please, I feel like that would make reading much more fun."
 show nao_v002 smile at active
 show satoko_v002 fuan_close at inactive
 nao 'In that case, how about you choose a book completely unrelated from the contest and write a book report on that?'
 show nao_v002 smile at active
 show satoko_v002 fuan_close at inactive
 nao 'Chie-sensei is really understanding and such, so she would surely understand if you discussed that with her, I suppose.'
 show satoko_v002 smile at nod_transform,active
 show nao_v002 smile at inactive
 satoko "That's a great idea! As soon as tomorrow hits, I'm going to talk with her!"
 hide satoko_v002
 show rika_v002 smile at mei_right
 with Dissolve(0.5)
 show rika_v002 smile at active
 show nao_v002 smile at inactive
 rika "Meep, at any rate, Nao is awesome. I hadn't even considered that book reports had that kind of meaning behind them."
 show nao_v002 fuan at active
 show rika_v002 smile at inactive
 nao "Huh? Ah... I'm sorry, I kind of spoke in a conceited way, didn't I? I'm really just repeating what my advisor told me."
 show nao_v002 smile at active
 show rika_v002 smile at inactive
 nao '"You become good at what you like doing", right? Because that teacher said that to me, I started to like reading and such...'
 show nao_v002 smile at active
 show rika_v002 smile at inactive
 nao 'With book reports, instead of them being assignments, I think of them as being pleasantly fun to write.'
 hide nao_v002
 hide rika_v002
 with Dissolve(0.2)
 stop music fadeout 0.5
 beatrice '... {i}Hmm, how interesting. If that is the case, allow me to hear your thoughts on my works{/i}.'
 show nao_v002 odoroki at mei_center
 with Dissolve(0.5)
 show nao_v002 odoroki at active
 nao 'Huh...?'
 return