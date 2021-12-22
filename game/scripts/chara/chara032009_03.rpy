label chara032009_03:
 show black_background onlayer black
 stop sound
 scene expression "#000"
 play music 'audio/bgm/BGM_QUEST.wav'
 show expression 'images/bg/AdvBg_2201.png' as bg
 with Dissolve(1.0)
 nao '（そしてあたしは、ベアトリーチェの\nゲーム盤へ降り立った）'
 nao '（タイトルは、\n『Legend of the golden witch』\n……黄金の魔女の伝説）'
 nao '（あたしはそこで、「右代宮戦人」さんの\n背後霊のように付きまとい、\n彼が見聞きする一部始終を観察させてもらった）'
 nao '（１９８６年１０月４日から、５日までの六軒島を\n彼の目と、耳を借りて……）'
 nao '（肖像画の下に掲げられた謎の碑文。\nそのメッセージになぞらえた密室殺人事件。\n魔女の黄金をめぐる様々な#p思惑#sおもわく#r……そして）'
 nao '（――島に隠された、黄金郷……）'
 window hide None
 show expression "#000" as fade with Dissolve(1.0)
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2190.png' as bg
 show beatrice_v001 normal_close at mei_right
 with Dissolve(1.0)
 pause 1.0
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show beatrice_v001 normal_close at inactive
 nao '……よい、しょっと。'
 show beatrice_v001 smile at jump_transform,active
 show nao_v002 normal at inactive
 beatrice 'おぉ、終わったか菜央！'
 show nao_v002 normal at active
 show beatrice_v001 smile at inactive
 nao 'えぇ、といっても物語の幕を閉じたのは\n戦人って人だけど……。'
 show nao_v002 fuan at active
 show beatrice_v001 smile at inactive
 nao 'ただ、あれは「幕を閉じた」という表現で\n正しいのかしら……？'
 show beatrice_v001 smile_close at active
 show nao_v002 fuan at inactive
 beatrice 'くっくっくっ、言いたいことはわかるぞォ。\nあれは要するに「タイムオーバー」……\n時間切れを迎えただけの結末だ。'
 show beatrice_v001 smile at active
 show nao_v002 fuan at inactive
 beatrice '物語を「終わらせた」と言うよりも、\nむしろ「終わってしまった」というべきであろう。'
 show beatrice_v001 normal at active
 show nao_v002 fuan at inactive
 beatrice 'それで……妾のゲーム盤、どうであったか？'
 show nao_v002 normal_close at active
 show beatrice_v001 normal at inactive
 nao 'そうね。一言で言うなら……。'
 show beatrice_v001 normal at active
 show nao_v002 normal_close at inactive
 beatrice '言うなら？'
 show nao_v002 sinken at active
 show beatrice_v001 normal at inactive
 nao '……悪趣味ね。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide beatrice_v001
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 show beatrice_v001 futeki at mei_center
 with Dissolve(0.08333333333333333)
 show beatrice_v001 futeki at updown_shake_transform,active
 beatrice 'く、く……くっくっひひひゃひゃっひゃっひゃっ！\nそうかそうか、悪趣味か！'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide beatrice_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show beatrice_v001 futeki at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show beatrice_v001 futeki at inactive
 nao 'だって、碑文に沿っての\n連続殺人が趣味の良いものだなんて、\nさすがに言えないと思うわ。'
 show nao_v002 normal_close at active
 show beatrice_v001 futeki at inactive
 nao 'ただ……センスが悪い、とは言わない。\nだって、悪趣味ってだけじゃないもの。'
 show beatrice_v001 normal at active
 show nao_v002 normal_close at inactive
 beatrice '……ん？'
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao 'あのお話ってどこまでが本当か、それとも嘘か\nわからないもの。だからあちこちに、読み手を\n騙そうという罠がばらまかれてる気がするの。'
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice '……ふむ、妾の存在が嘘であると申すか？'
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao 'そうとは思わないわ。\nけどあたしは、戦人さんの目を通して\nあのゲーム盤を観劇した……。'
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao 'つまり、自分の目じゃない。\n他人の主観やバイアスが入ってることになるわ。'
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice '自分の目で見なければ、全ての事実を\n真実とは認められず……\nまた魔女の存在も、信じられない……と？'
 show nao_v002 smile at active
 show beatrice_v001 normal at inactive
 nao '完全に否定してるわけじゃないわ。\nもしそうなら、今あたしと喋ってるのは\n誰って話になるでしょ。ただ……。'
 show nao_v002 normal_close at active
 show beatrice_v001 normal at inactive
 nao '他人の話を全部鵜呑みにするな。\nその情報が正しいかどうかは、\n自分でしっかり検証してから確かめる……。'
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao 'そうすることで情報は知識になり、\n教養として自らの糧になる……\nそう、お母さんに教えられたわ。'
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao 'だから、実際に自分がその場にいて\nこの目で見て、触ったものじゃないと\n判断の材料にはできないと思うのよ。'
 show beatrice_v001 fuan at active
 show nao_v002 normal at inactive
 beatrice '……疑りが深いのか思慮が深いのか、\nよくわからぬ娘よ。'
 show nao_v002 smile at active
 show beatrice_v001 fuan at inactive
 nao 'ごめんなさい、そういう性分なの。\n……けど、悪趣味だけでもないってのも\n正直な感想よ。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide beatrice_v001
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 show nao_v002 normal at mei_center
 with Dissolve(0.08333333333333333)
 show nao_v002 normal at active
 nao 'あの話は、島で起こったかもしれない\n何かの事実の可能性を伝えるため……。'
 show nao_v002 normal_close at active
 nao 'ううん、メッセージを伝える\n意図があるような気がするの。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show nao_v002 normal_close at mei_left
 show beatrice_v001 normal at mei_right
 with Dissolve(0.5)
 show beatrice_v001 normal at active
 show nao_v002 normal_close at inactive
 beatrice '……ほぅ。なぜ、そう思うのだ？'
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao 'あたしはまだ、\n『Legend of the golden witch』の\nテーマを見つけられていないからよ。'
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice 'テーマ？'
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao 'あたしが今まで読んだお話には、\n何かしらのテーマがあった。\nセンスに合うかどうかは別としてね。'
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao 'つまり、物語にテーマは必須ってことよね？'
 show nao_v002 fuan_close at active
 show beatrice_v001 normal at inactive
 nao 'でも、テーマが見つけられないってことは\nきっと巧妙に隠されてるってことで……\nそれを見抜けないのはあたしの力不足。'
 show nao_v002 smile at active
 show beatrice_v001 normal at inactive
 nao '何度かお話を読み直したら、わかるのかもね。\nあ、それとも続きがあるの？'
 show beatrice_v001 normal_close at active
 show nao_v002 smile at inactive
 beatrice '……テーマが隠されていると、なぜ断言できる？'
 show nao_v002 normal at active
 show beatrice_v001 normal_close at inactive
 nao 'そりゃ断言できるわよ。'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show nao_v002 smile at active
 show beatrice_v001 normal_close at inactive
 nao 'だって、このお話……本当に面白かったもの。'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 show beatrice_v001 normal at active
 show nao_v002 smile at inactive
 beatrice '…………。'
 show nao_v002 fuan at active
 show beatrice_v001 normal at inactive
 nao 'ベアトリーチェ？'
 camera at screenshake_transform
 pause 0.0
 show beatrice_v001 futeki at active
 show nao_v002 fuan at inactive
 beatrice 'くっくっ、……くっくくく！！！\nはははははは！\u3000あひゃはははははははは！！！'
 show nao_v002 fuan at active
 show beatrice_v001 futeki at inactive
 nao 'えっ……ちょっと、どうしたのよ。\nそんなにあたしの感想、不満だった？\n期待に添えられなかったのは悪かったけど……。'
 show beatrice_v001 smile_close at active
 show nao_v002 fuan at inactive
 beatrice 'いや、そうではない！\u3000そうではない！'
 show beatrice_v001 smile at active
 show nao_v002 fuan at inactive
 beatrice 'あの話を読んで、臆面もなく面白いと\n断言したそなたに感服した！'
 show beatrice_v001 smile at active
 show nao_v002 fuan at inactive
 beatrice 'なるほど！\n巫女を用意し、物語を朗読させるのが\nこれほどに楽しいこととは……！'
 show beatrice_v001 futeki_close at active
 show nao_v002 fuan at inactive
 beatrice '千年の歳を生きてなお、\n新しいものを発見できるとはな……くっくっくっ！！'
 show nao_v002 fuan at active
 show beatrice_v001 futeki_close at inactive
 nao 'ど、どうも……で、いいのかしら。'
 show beatrice_v001 smile at active
 show nao_v002 fuan at inactive
 beatrice 'ふふ……なかなかに楽しかったぞ、菜央よ。\n機会があれば、また妾の用意したゲーム盤を\n読みに来るがよい。'
 show beatrice_v001 smile_close at active
 show nao_v002 fuan at inactive
 beatrice 'そなたならば、大いに歓迎しよう。\n……ただ、これ以上そなたに関わるには、\nあの客人の許可が必要になるみたいだな。'
 show nao_v002 normal at active
 show beatrice_v001 smile_close at inactive
 nao '許可……？'
 show beatrice_v001 smile at active
 show nao_v002 normal at inactive
 beatrice 'ふむ……また暴れられぬうちに\nそなたの記憶を消す魔法でもかけるとするか。'
 show beatrice_v001 smile at active
 show nao_v002 normal at inactive
 beatrice '案ずるな。\n目が覚めたら、そなたは元の場所に戻っていよう。'
 show nao_v002 odoroki at jump_transform,active
 show beatrice_v001 smile at inactive
 nao '……えっ、これで終わりっ？！\n続きを読ませてくれるんじゃないの？！'
 show beatrice_v001 normal_close at active
 show nao_v002 odoroki at inactive
 beatrice 'さあさ、思い出してご覧なさい……。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide nao_v002
 hide beatrice_v001
 hide fade with Dissolve(0.08333333333333333)
 show nao_v002 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show nao_v002 sinken at active
 nao 'ちょっと……！'
 stop music fadeout 0.5
 show expression "#000" as fade with Dissolve(1.0)
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_351.png' as bg
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_528_unfold_cloth.wav'
 camera at screenshake_transform
 pause 0.0
 nao '続きが気になるじゃないのっっ！！'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 play music 'audio/bgm/BGM_EVENT1.wav'
 show rika_v002 odoroki at mei_center
 with Dissolve(0.5)
 show rika_v002 odoroki at active
 rika 'えっ？'
 hide rika_v002
 with Dissolve(0.2)
 show hanyuu_v002 odoroki at mei_right
 show satoko_v002 fuan at mei_left
 with Dissolve(0.5)
 show satoko_v002 fuan at active
 show hanyuu_v002 odoroki at inactive
 satoko 'ど、どうしましたの菜央さん。'
 show hanyuu_v002 sinken at active
 show satoko_v002 fuan at inactive
 hanyuu 'あぅあぅ、ここは図書館なのです。\n静かにしないとダメなのですよ～！'
 hide satoko_v002
 show rika_v002 fuan at mei_left
 with Dissolve(0.5)
 show rika_v002 fuan at active
 show hanyuu_v002 sinken at inactive
 rika '羽入も大声を出しているのですよ。'
 show hanyuu_v002 fuan at active
 show rika_v002 fuan at inactive
 hanyuu 'はっ？！\u3000ご、ごめんなさいなのです……。'
 hide rika_v002
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at active
 show hanyuu_v002 fuan at inactive
 nao 'あ、えっと……あたし、今、寝てた？'
 hide hanyuu_v002
 show rika_v002 smile at mei_right
 with Dissolve(0.5)
 show rika_v002 smile at active
 show nao_v002 fuan at inactive
 rika 'みー。沙都子に読書感想文の書き方を\n教えて書き上がるのを待っている間、\n菜央はうとうとしていたのですよ。'
 hide rika_v002
 show satoko_v002 fuan at mei_right
 with Dissolve(0.5)
 show satoko_v002 fuan at active
 show nao_v002 fuan at inactive
 satoko 'も、申し訳ありませんわ……\n私が時間をかけたせいで、\n菜央さんに退屈をさせてしまって……。'
 show nao_v002 fuan at active
 show satoko_v002 fuan at inactive
 nao 'あ、別に謝ることないと思うけど……。'
 hide satoko_v002
 show hanyuu_v002 normal at mei_right
 with Dissolve(0.5)
 show hanyuu_v002 normal at active
 show nao_v002 fuan at inactive
 hanyuu 'それにしても、続きが気になる……とは\n何のことですか？'
 show nao_v002 odoroki at active
 show hanyuu_v002 normal at inactive
 nao 'え？\u3000え、えっと……なんだったかしら。\n夢の中で面白い本を読んでいた気がするんだけど。'
 show nao_v002 normal at active
 show hanyuu_v002 normal at inactive
 nao '…………。'
 hide hanyuu_v002
 show satoko_v002 fuan at mei_right
 with Dissolve(0.5)
 show satoko_v002 fuan at active
 show nao_v002 normal at inactive
 satoko '菜央さん？'
 show nao_v002 normal at active
 show satoko_v002 fuan at inactive
 nao '……ね、沙都子。感想文を書くのに\n時間がかかるんだったら、\nちょっと本を借りてきていいかしら。'
 show satoko_v002 fuan at active
 show nao_v002 normal at inactive
 satoko '付き合っていただいているのは\nこちらですし、それは結構ですが……\n読みたい本でもありましたの？'
 show nao_v002 smile at nod_transform,active
 show satoko_v002 fuan at inactive
 nao 'えぇ、ミステリーが読みたいと思ってね。'
 hide satoko_v002
 show hanyuu_v002 odoroki at mei_right
 with Dissolve(0.5)
 show hanyuu_v002 odoroki at active
 show nao_v002 smile at inactive
 hanyuu 'あぅ……ミステリー、ですか？'
 show nao_v002 smile_close at active
 show hanyuu_v002 odoroki at inactive
 nao 'なんだか急に、ミステリーの勉強を\nしたくなってきちゃったのよ。'
 show nao_v002 smile at active
 show hanyuu_v002 odoroki at inactive
 nao 'とりあえず、有名なミステリー小説を\nいくつか借りてみようかしら……。'
 hide hanyuu_v002
 show rika_v002 odoroki at mei_right
 with Dissolve(0.5)
 show rika_v002 odoroki at active
 show nao_v002 smile at inactive
 rika 'みー、どういう風の吹き回しですか？'
 show nao_v002 smile at active
 show rika_v002 odoroki at inactive
 nao 'なんとなく、よ。\nただその方が、夢の続きを見た時に\n楽しめる気がするのよ。'
 show nao_v002 smile_close at active
 show rika_v002 odoroki at inactive
 nao '気がするだけだけど、ね。ふふっ。'
 return