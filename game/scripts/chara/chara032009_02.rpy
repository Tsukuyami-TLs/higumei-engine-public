label chara032009_02:
 show black_background onlayer black
 stop sound
 scene expression "#000"
 play music 'audio/bgm/BGM_EVENT6.wav'
 show expression 'images/bg/AdvBg_2190.png' as bg
 with Dissolve(1.0)
 show beatrice_v001 smile at mei_right
 show nao_v002 odoroki at mei_left
 with Dissolve(0.5)
 show nao_v002 odoroki at active
 show beatrice_v001 smile at inactive
 nao 'えっ……？'
 show beatrice_v001 smile at active
 show nao_v002 odoroki at inactive
 beatrice '久しぶりよの、菜央。\nそちらに戻った後も元気そうでなによりだ。'
 show nao_v002 fuan at active
 show beatrice_v001 smile at inactive
 nao 'あ、あなたは誰……じゃ、なくて！'
 show nao_v002 sinken at active
 show beatrice_v001 smile at inactive
 nao 'あたし……あなたのこと、知ってる……？\n黄金の魔女、ベアトリーチェ……？！'
 show beatrice_v001 smile at active
 show nao_v002 sinken at inactive
 beatrice 'ほぅ、まだ妾の名前を憶えていたのか。'
 show nao_v002 fuan at nod_transform,active
 show beatrice_v001 smile at inactive
 nao 'えぇ。むしろ、なんで今まで忘れていたのか\nよくわからないわ。\nあんなに強烈な体験をしたってのに……。'
 show beatrice_v001 normal_close at active
 show nao_v002 fuan at inactive
 beatrice '……なるほど。そなたの記憶から、\n妾たちに関することを忘れるように\n魔法がかかっていたというわけか。'
 show nao_v002 odoroki at jump_transform,active
 show beatrice_v001 normal_close at inactive
 nao '……えっ？\u3000じゃあ、あたしの記憶が\n誰かに操作されてるってこと……？'
 show beatrice_v001 smile at active
 show nao_v002 odoroki at inactive
 beatrice 'そう嫌な顔をするでない。記憶を改変したのは\nそなたに害を与えようとしたのではなく、\nむしろ守るための措置なのだろう。'
 show beatrice_v001 smile at active
 show nao_v002 odoroki at inactive
 beatrice '此度のゲームはイレギュラーゆえ、\nゲームマスターはそなたが妾に関係する記憶を\n保持し続けることを良しとしなかったのであろう。'
 show beatrice_v001 futeki_close at active
 show nao_v002 odoroki at inactive
 beatrice 'ふむふむ…妾がここへそなたを招待したことで\nそれは効果が消えたようだ。くっくくくくくくくくくく！'
 show nao_v002 normal at active
 show beatrice_v001 futeki_close at inactive
 nao '……。別に、あなたのことを忘れるように\nしてくれなくてもよかったのに。'
 show nao_v002 normal_close at active
 show beatrice_v001 futeki_close at inactive
 nao '確かに、ベアトリーチェやヱリカさんとのバトルでは\n色々と頭を悩ませるものだったけど……\nあの程度の出来事であたしは変わらないわ。'
 show beatrice_v001 futeki at updown_shake_transform,active
 show nao_v002 normal_close at inactive
 beatrice 'くっくっくっ……言うではないか。\nその臆せぬ態度……ますます気に入ったぞ。'
 show nao_v002 normal at active
 show beatrice_v001 futeki at inactive
 nao '……ところで、今日ははいったい何の用？\nひょっとして、また推理バトルでも始まるのかしら。'
 show beatrice_v001 smile at active
 show nao_v002 normal at inactive
 beatrice '案ずるな、そう警戒しなくても良い。\n妾がそなたを招待したのはな、少々退屈がすぎたのでな。'
 show beatrice_v001 smile at active
 show nao_v002 normal at inactive
 beatrice '要するに、暇潰しというやつだ。'
 show nao_v002 fuan at active
 show beatrice_v001 smile at inactive
 nao '暇潰し……ね。たったそれだけのために\nこんな場所に呼びつけるなんて、\n魔女ってよくわからない存在ね……。'
 show beatrice_v001 futeki at active
 show nao_v002 fuan at inactive
 beatrice 'くっくっくっく、無理もない！\n魔女にとっては退屈とは毒……そなたにとっては\n大したことではなくとも、妾にとっては大事なことなのだ。'
 show beatrice_v001 normal at active
 show nao_v002 fuan at inactive
 beatrice 'それはともかくとして……\n菜央よ、妾の用意した物語を観劇する気はないか？'
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao '物語の、観劇……？'
 show beatrice_v001 normal_close at active
 show nao_v002 normal at inactive
 beatrice 'うむ。妾はこれまで、六軒島を舞台に\n様々なゲーム盤を用意してきたのだ。\nそれこそ、今回とは違う密室殺人事件というものだがな。'
 show beatrice_v001 smile at active
 show nao_v002 normal at inactive
 beatrice '……くっくくくく。妾のゲームは楽しいぞぉ。\n妾も駒を眺めてるだけじゃなく\nゲーム盤で駒として動くこともある位だ。'
 show nao_v002 odoroki at active
 show beatrice_v001 smile at inactive
 nao '六軒島……？\nその名前、どこかで聞いたような……あっ？！'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide beatrice_v001
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 show nao_v002 sinaken at mei_center
 with Dissolve(0.08333333333333333)
 show nao_v002 sinken at active
 nao 'そうだ、思い出したわ……！\n１９８６年の１０月頃、伊豆諸島のひとつで\n謎の爆発事故が起こって……。'
 show nao_v002 sinken at active
 nao '会合でそこを訪れていた、資産家の親族たちの\n多くが命を落としたという小さな島の名が、\n確か「六軒島」……っ……。'
 show nao_v002 normal at active
 nao '……なるほど。あの島って、\nそういう因縁のある場所だったのね。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show beatrice_v001 smile at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show beatrice_v001 smile at inactive
 nao 'それで……あなたの作ったゲーム盤って、\nどうやって遊べばいいのかしら？'
 show beatrice_v001 smile at active
 show nao_v002 normal at inactive
 beatrice 'おぉ、それは妾のゲームを楽しむ、という事だな？'
 show nao_v002 smile at nod_transform,active
 show beatrice_v001 smile at inactive
 nao 'えぇ。あたし、どんなゲームでも好きだから。\n……で、ルールは？\u3000目的は？'
 stop music fadeout 0.5
 show beatrice_v001 futeki at active
 show nao_v002 smile at inactive
 beatrice 'それはだな……ほれっ。'
 play music 'audio/bgm/BGM_EVENT5.wav'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide beatrice_v001
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 show nao_v002 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_230_charge.wav'
 show nao_v002 odoroki at chara_shake_transform,active
 nao 'えっ、ちょっ、なにこの大穴……！\nお、落ち……きゃぁあああああぁああっ！！'
 show nao_v002 odoroki
 show nao_v002 odoroki:
  linear 0.5 pos (960,2280)
 pause 0.5
 show expression "#000" as fade with Dissolve(1.0)
 hide nao_v002
 with Dissolve(0.2)
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2201.png' as bg
 with Dissolve(1.0)
 show nao_v014 odoroki at mei_center
 with Dissolve(0.5)
 show nao_v014 odoroki at active
 nao 'きゃぁ……っ、て、えっ？'
 show nao_v014 fuan at active
 nao 'う、浮いてる……？'
 play music 'audio/bgm/BGM_QUEST.wav'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide nao_v014
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show beatrice_v001 smile at mei_right
 show nao_v014 fuan at mei_left
 with Dissolve(0.5)
 show beatrice_v001 smile at active
 show nao_v014 fuan at inactive
 beatrice '今のそなたは、竜王ペンドラゴンの兵士――\nシエスタ姉妹を依り代としている。\n空を飛ぶ程度、赤子の手を捻るより簡単であろう。'
 show nao_v014 fuan at active
 show beatrice_v001 smile at inactive
 nao '……ベアトリーチェも、普通に浮いてるわね。\nいったいあなたは、どうやって飛んでるの？'
 show beatrice_v001 futeki at active
 show nao_v014 fuan at inactive
 beatrice 'くっくっくっ……妾は魔女だ！\n空を飛ぶことに何の不思議もないわ。'
 show nao_v014 normal at active
 show beatrice_v001 futeki at inactive
 nao '魔女って、箒がなくても飛べたのね……っと！'
 show expression "#000" as fade with Dissolve(1.0)
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2220.png' as bg
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_232_landing.wav'
 nao 'とりあえず、お庭には降り立ったけど……\nあたしはこれからどうすればいいの？'
 beatrice '今から、新島で船を待つ\n右代宮戦人のもとへそなたをつれて行く。'
 beatrice 'そこで、その男の背後から、\nこの六軒島で起きる出来事を見届けてもらおう。'
 nao 'なるほど。その「戦人」という男性の目線に立って、\nあなたの作ったゲーム盤上で行動しろってことね。'
 beatrice 'そうだ。なかなか聡い上に素直なのは良いぞ。\n……そして、菜央。そなたが着ているその制服は\n妾が契約を結んでいる武具のもの。'
 nao 'えっ……？'
 beatrice 'そう考えたら、そなたも我の武具になっている…\nというように考えられるとも思わないか？'
 nao 'そんなことを言われるなら、脱ぎたいわね…'
 beatrice 'くっくくくく、冗談冗談。\nほれほれ、これよりゲームが始まるぞ。'
 nao 'えっ……？ あ、あたしはどうすればいいの？'
 beatrice '何もせずとも良い。\n準備ができたところで向かう先は戦人の後ろだ。'
 beatrice '戦人と妾の戦いを特等席で楽しめるぞぉ。'
 nao 'ゲームを遊ぶんじゃないの？\nどっちかというと、他人がプレイしてるのを\nただ後ろで見てるだけ……？'
 beatrice 'これは妾と戦人のゲームゆえ\nそなたを対戦相手として呼んではおらぬ。'
 beatrice 'ただ、いままで観劇していたのは\n奇跡の魔女や絶対の魔女だったからな。\n少し趣向を変えてそなたの感想も聞いてみてたかったのよ。'
 nao '……ゲームだったら、自分で遊んだ方が\n楽しいと思うけどな。'
 beatrice '不服か？'
 nao 'ううん、そういうわけじゃないわ。\n……ただ、あたしは自分で遊ぶ以外の\nゲームの遊び方を知らなかっただけ。'
 nao 'でも、まぁ……そうね。\nそういう楽しみ方があるなら、\n試させてもらおうかしら。'
 beatrice 'くっくっくっ……\n柔軟で素直な思考と姿勢は、ゲームを楽しむ上で\n欠かせぬ要素だ。なかなか悪くないぞ。'
 nao '褒め言葉として受け取っておくわ。\nえっと、この物語の先には普通に人が待っているのよね……っ！'
 show expression "#000" as fade with Dissolve(1.0)
 hide beatrice_v001
 hide nao_v014
 with Dissolve(0.2)
 stop sound
 scene expression "#000"
 show expression 'images/card/Card_032009.png' as bg
 with Dissolve(1.0)
 nao 'えーっと……こほん。'
 nao '鳳谷菜央……魔女ベアトリーチェの、\nゲーム盤を観劇させていただきます。'
 nao 'どうぞ、お手柔らかにお願い致します……。'
 show expression "#000" as fade with Dissolve(1.0)
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2220.png' as bg
 with Dissolve(1.0)
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide fade with Dissolve(0.08333333333333333)
 show beatrice_v001 futeki at mei_center
 with Dissolve(0.08333333333333333)
 show beatrice_v001 futeki at updown_shake_transform,active
 beatrice 'ふ、はっはっはっはっはっは…。\n戦人がいると聞いて挨拶から始めるか！\nなかなかに面白いではないか！'
 show beatrice_v001 futeki_close at active
 beatrice 'しかしぎこちないぞ菜央よ。\n真里亞だったら勢いよく飛び込んでおるわ。くっくくくく！'
 show beatrice_v001 smile at active
 beatrice 'ほらほらそんな顔をするでない。\n物語はもう始まるぞ。\nせいぜい、振り落とされぬようにな。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide beatrice_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show nao_v014 fuan at mei_left
 show beatrice_v001 smile at mei_right
 with Dissolve(0.5)
 show nao_v014 fuan at active
 show beatrice_v001 smile at inactive
 nao 'ありがと……って、ちょっと待って。\nいったい何から「振り落とされる」って？'
 show beatrice_v001 futeki at active
 show nao_v014 fuan at inactive
 beatrice '無論、妾のゲーム盤からだッ！'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide nao_v014
 hide beatrice_v001
 hide fade with Dissolve(0.08333333333333333)
 show nao_v014 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_611_ls_wind.wav'
 camera at screenshake_transform
 pause 0.0
 show nao_v014 odoroki at active
 nao 'そ、そういう乗り物系だとは\nさすがに聞いてなっ……んきゃぁぁぁあぁっ？！'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide nao_v014
 hide fade with Dissolve(0.08333333333333333)
 show beatrice_v001 futeki at mei_center
 with Dissolve(0.08333333333333333)
 show beatrice_v001 futeki at updown_shake_transform,active
 beatrice 'くっひゃっひゃっひゃっひゃっ！\n琴線に触れる良い叫びだ！\n目一杯楽しんでこいよぉおおおぉぉっっ！！'
 return