label chara472001_02:
 show black_background onlayer black
 stop sound
 scene expression "#000"
 play music 'audio/bgm/BGM_QUEST6_COLLAB2.wav'
 show expression 'images/bg/AdvBg_2190.png' as bg
 with Dissolve(1.0)
 show nao_v001 normal at mei_right
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show nao_v001 normal at inactive
 dlanor '『ノックス十戒』とは、\nミステリーにおいて守るべき約束デス。\n戒律といっても過言ではないでショウ。'
 show nao_v001 normal at active
 show dlanor_v001 normal at inactive
 nao '戒律……？'
 show expression "#000" as fade with Dissolve(1.0)
 hide nao_v001
 hide dlanor_v001
 with Dissolve(0.2)
 stop sound
 scene expression "#000"
 show expression 'images/card/Card_472001.png' as bg
 with Dissolve(1.0)
 dlanor 'ハイ。ノックス第１条。\n『犯人は物語当初の登場人物以外を禁ズ』'
 dlanor 'ノックス第２条。\n『探偵方法に超自然能力の使用を禁ズ』'
 dlanor 'ノックス第３条。\n『秘密の通路の存在を禁ズ』'
 dlanor 'ノックス第４条。\n『未知の薬物、及び、難解な科学装置の\n使用を禁ズ』'
 dlanor 'ノックス第６条。\n『探偵方法に偶然と第六感の使用を禁ズ』'
 dlanor 'ノックス第７条。\n『探偵が犯人であることを禁ズ』'
 dlanor 'ノックス第８条。\n『提示されない手掛かりでの解決を禁ズ』'
 dlanor 'ノックス第９条。\n『観測者は自分の判断・解釈を\n主張することが許さレル』'
 dlanor 'ノックス第１０条。\n『手掛かりなき他の登場人物への変装を禁ズ』'
 nao 'なるほど。１０個あるから。十戒なのね……\nって、そういえば５条は？'
 dlanor '欠番デス。\nよって、こちらの言及はお控え下サイ。'
 nao 'どうして欠番なのか、その理由を\n聞いてみたかったんだけど……わかったわ。'
 show expression "#000" as fade with Dissolve(1.0)
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2190.png' as bg
 with Dissolve(1.0)
 show nao_v001 normal_close at mei_right
 show beatrice_v001 normal at mei_left
 with Dissolve(0.5)
 show beatrice_v001 normal at active
 show nao_v001 normal_close at inactive
 beatrice 'では、菜央。そなたは『ノックスの十戒』を\n最初に聞いた時、どう思った？'
 show nao_v001 fuan at active
 show beatrice_v001 normal at inactive
 nao 'そうね……素直な感想を言わせてもらうと、\nちょっと窮屈だなって印象があったわ。\nミステリーって制約があるものなの？\u3000って。'
 show beatrice_v001 futeki at updown_shake_transform,active
 show nao_v001 fuan at inactive
 beatrice 'くっくっくっ！\nそれは、そなたがミステリーを読む時\nただ漫然と読んでいたからであろう？'
 show nao_v001 fuan at active
 show beatrice_v001 futeki at inactive
 nao '漫然な読み方かどうかはわからないけど……\n色々と難しい表現や設定が多かったから、\n話を追うだけで精いっぱいだったのは確かね。'
 show beatrice_v001 smile at active
 show nao_v001 fuan at inactive
 beatrice 'では、読み進めながら物語内の犯人が誰か、\n推理して当ててみようと考えたことはないか？'
 show nao_v001 fuan_close at active
 show beatrice_v001 smile at inactive
 nao '犯人とトリックを聞いて驚くことはあったけど、\n推理はあんまりしたことがなかったかも……かも。'
 show nao_v001 normal at active
 show beatrice_v001 smile at inactive
 nao 'じゃあベアトリーチェはミステリーを読みながら、\n犯人を推理したりするのかしら？'
 play audio 'audio/sfx/SE_226_shine.wav'
 show beatrice_v001 futeki at active
 show nao_v001 normal at inactive
 beatrice '当然であろう！\nそれこそがミステリーの醍醐味であるからな！'
 show nao_v001 smile at active
 show beatrice_v001 futeki at inactive
 nao 'なるほど……でも、ページをめくりながら\n探偵から少し遅れて物語を追いかけていくのも、\nそれはそれで楽しいものだけどね。'
 show beatrice_v001 fuan at active
 show nao_v001 smile at inactive
 beatrice 'む、むむ……しかし、ミステリーに対しては\n挑む姿勢で臨むというのが通常の礼儀ではないのか？'
 show nao_v001 normal at active
 show beatrice_v001 fuan at inactive
 nao '媒体が小説だったら、本を開いた瞬間から\n真っ先に始まるのは読書という「行為」よ。'
 show nao_v001 smile at active
 show beatrice_v001 fuan at inactive
 nao 'その行為の中で謎解きをするかしないか、\nどうやって楽しむのかは読者の自由じゃないかしら。'
 show beatrice_v001 normal at active
 show nao_v001 smile at inactive
 beatrice '……ふむ、意見が合わぬな。\nそなたは読書家だと聞いていたが、楽しみ方が\n妾たちとは異なるわけか。'
 hide beatrice_v001
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show nao_v001 smile at inactive
 dlanor '……この戦い、ベアトリーチェ卿の方が\n分が悪いデスネ。\n今回は引くのが賢明デス。'
 show nao_v001 odoroki at active
 show dlanor_v001 normal at inactive
 nao 'あ、でも別に、ベアトリーチェの楽しみ方が\n間違ってるなんて絶対に思わないわよ？\nただ、あたしの今の楽しみ方がこうだってだけで。'
 show nao_v001 normal at active
 show dlanor_v001 normal at inactive
 nao 'それに……今の話でわかったわ。\nあたしの今の読書スタイルだったら、\nミステリー小説はルール無用でも構わない。'
 show nao_v001 normal_close at active
 show dlanor_v001 normal at inactive
 nao 'けど、ベアトリーチェのように\nきちんと誠実な姿勢でミステリー小説に\n挑もうとする人にとって、ルールは必須事項。'
 show nao_v001 normal at active
 show dlanor_v001 normal at inactive
 nao 'ゲームだって、ルールなしで遊んだら\n戦略も戦術も立てようがなくなっちゃうし……\n『ノックス十戒』は、そのためのものなのね。'
 show dlanor_v001 normal at active
 show nao_v001 normal at inactive
 dlanor 'ハイ。『ノックス十戒』は、\nミステリーを提示する者や挑む者……\n双方がフェアであるために必要なものデス。'
 hide dlanor_v001
 show beatrice_v001 normal at mei_left
 with Dissolve(0.5)
 show beatrice_v001 normal at active
 show nao_v001 normal at inactive
 beatrice 'うむ。ルールがなければ出題側は自由だが、\n挑む探偵は推理の指針がなくなる。\n進め方もわからぬし、ゴールも見えぬ。'
 show beatrice_v001 normal_close at active
 show nao_v001 normal at inactive
 beatrice 'ちなみに、このルールにひっかかり\n物語が矛盾することを、妾たちは\n「ロジックエラー」と呼んでおる。'
 show beatrice_v001 normal at active
 show nao_v001 normal at inactive
 beatrice '推理勝負において、\n「ロジックエラー」はまさに禁じ手……\n絶対に忌避すべき事項ということだな。'
 show nao_v001 normal at active
 show beatrice_v001 normal at inactive
 nao '……つまり、ゲーセンで対人戦に負けても\n相手を殴るのはダメってことね。'
 show beatrice_v001 fuan at active
 show nao_v001 normal at inactive
 beatrice 'う、うむ……？\n対人戦のゲームというものが何かわからぬゆえ、\n妾には是非をつけることができぬのだが……。'
 show nao_v001 fuan at active
 show beatrice_v001 fuan at inactive
 nao 'あ、でも……『ノックス十戒』の成り立ちが\nどうだったかって質問について戻るけど、\n結局それって、どうして作られることになったの？'
 hide beatrice_v001
 show dlanor_v001 normal_close at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal_close at active
 show nao_v001 fuan at inactive
 dlanor '……それは、過去に自由すぎるミステリーが\n跋扈した時代があったからデス。'
 show nao_v001 normal at active
 show dlanor_v001 normal_close at inactive
 nao '自由すぎるミステリー……？'
 show dlanor_v001 normal at active
 show nao_v001 normal at inactive
 dlanor '『ノックス十戒』が制定される前、市井には\n読者に解けるようになっていないミステリー作品が\n濫発していて……全体の質を下げておりマシタ。'
 show dlanor_v001 normal at active
 show nao_v001 normal at inactive
 dlanor 'たとえば、犯人が物語の後半に突然現れたり、\n探偵が超能力で解決したり……\n密室殺人に秘密の通路があったり、デス。'
 show dlanor_v001 normal_close at active
 show nao_v001 normal at inactive
 dlanor '他にも、読者の想像の及ばない\nアンフェアな未知の薬物や科学装置が登場……。'
 show dlanor_v001 normal_close at active
 show nao_v001 normal at inactive
 dlanor '探偵が偶然や第六感で、事件を解決。\n犯人が実は探偵で、視点を偽っていたトリック。'
 show dlanor_v001 normal at active
 show nao_v001 normal at inactive
 dlanor 'さらに、作中で説明がなかった手掛かりが\n突如出現……登場人物のＡさんが\n実はＢさんの変装デシタ、など……。'
 show nao_v001 fuan at active
 show dlanor_v001 normal at inactive
 nao '……なるほど。そんなことをやられちゃったら、\n読者は推理なんてまともにできないわね。'
 show nao_v001 normal at active
 show dlanor_v001 normal at inactive
 nao '……あれ？\u3000でもよく考えたら第９条は\n毛色がちょっと違うわね。'
 show dlanor_v001 odoroki at active
 show nao_v001 normal at inactive
 dlanor '違う……トハ？'
 show nao_v001 normal at active
 show dlanor_v001 odoroki at inactive
 nao 'だって１０条も含めて、それまでは\n「してはいけない」ことの羅列だったのに、\n９条は「許される」ってあるじゃない。'
 show nao_v001 normal at active
 show dlanor_v001 odoroki at inactive
 nao 'ノックス第９条。\n『観測者は自分の判断・解釈を\n主張することが許される』'
 show nao_v001 normal at active
 show dlanor_v001 odoroki at inactive
 nao 'この観測者って、作中の人物って\n認識でいいのよね。'
 show dlanor_v001 normal at active
 show nao_v001 normal at inactive
 dlanor 'ハイ。'
 show nao_v001 fuan at active
 show dlanor_v001 normal at inactive
 nao 'つまり、これをうまく解釈したら\n作中の人物は嘘をついても構わない、ってことに\nなったりすると思うんだけど……？'
 hide dlanor_v001
 show beatrice_v001 normal at mei_left
 with Dissolve(0.5)
 show beatrice_v001 normal at active
 show nao_v001 fuan at inactive
 beatrice 'その条文だけを見れば、そうだな。\n……だが、探偵は犯人であってはならない。'
 show nao_v001 normal at active
 show beatrice_v001 normal at inactive
 nao '７条に引っかかるものね。\nでも、探偵が嘘をついちゃダメってことは\nないんでしょ？'
 hide beatrice_v001
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show nao_v001 normal at inactive
 dlanor 'イイエ、嘘はいけマセン。\n９条に抵触しマス。'
 show nao_v001 odoroki at jump_transform,active
 show dlanor_v001 normal at inactive
 nao 'えっ？\u3000でも、自分の判断や解釈を\n主張することが許されるって……あ。'
 hide dlanor_v001
 show beatrice_v001 futeki at mei_left
 with Dissolve(0.5)
 show beatrice_v001 futeki at active
 show nao_v001 odoroki at inactive
 beatrice 'くっくっくっ！\nようやく気づいたようだな。'
 show nao_v001 sinken at active
 show beatrice_v001 futeki at inactive
 nao 'そうか……観測者は許される。\nけど、探偵は許されない。'
 hide beatrice_v001
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show nao_v001 sinken at inactive
 dlanor '……その通りデス。よく気付きマシタ。'
 show nao_v001 normal at active
 show dlanor_v001 normal at inactive
 nao 'なるほど……だとすると、嘘つきは\n探偵になっちゃダメってことね。'
 show dlanor_v001 normal_close at active
 show nao_v001 normal at inactive
 dlanor 'イイエ。例外はありマス。\n本人が嘘をついていると自覚がない場合、\n『ノックス十戒』には抵触しマセン。'
 show nao_v001 odoroki at active
 show dlanor_v001 normal_close at inactive
 nao 'たとえば？'
 hide dlanor_v001
 show beatrice_v001 smile at mei_left
 with Dissolve(0.5)
 show beatrice_v001 smile at active
 show nao_v001 odoroki at inactive
 beatrice 'そうだな。おぬしを探偵だとして……\nそなたはパティスを知っているか？'
 show nao_v001 normal at active
 show beatrice_v001 smile at inactive
 nao 'いえ、知らないわ。なに、それは。'
 show beatrice_v001 smile at active
 show nao_v001 normal at inactive
 beatrice '紅茶の種類だ。黒っぽい色合いと\nブランデーのような香りが特徴だ。'
 show nao_v001 odoroki at active
 show beatrice_v001 smile at inactive
 nao 'へー……。'
 hide beatrice_v001
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show nao_v001 odoroki at inactive
 dlanor '嘘デス。'
 camera at screenshake_transform
 pause 0.0
 show nao_v001 sinken at active
 show dlanor_v001 normal at inactive
 nao 'はぁっ……？'
 hide dlanor_v001
 show beatrice_v001 futeki at mei_left
 with Dissolve(0.5)
 show beatrice_v001 futeki at active
 show nao_v001 sinken at inactive
 beatrice 'くっくっくっ……実際のパティスは\nたとえるなら、揚げ餃子に近いお茶請けだ。\nディンブラによく合って、うまいぞ。'
 show nao_v001 fuan_close at active
 show beatrice_v001 futeki at inactive
 nao 'なるほど。一度どこかの大きなスーパーで、\n売ってるかどうか探してみるわね。\n……あと、たとえ話も理解できたわ。'
 show nao_v001 normal at active
 show beatrice_v001 futeki at inactive
 nao '探偵のあたしが観測者として、ベアトリーチェの\n言うことを信じてそれを別人に伝えても……\n嘘をついたことにはならない。'
 show nao_v001 normal at active
 show beatrice_v001 futeki at inactive
 nao 'この場合、重要なのは嘘の定義ね。\n何をもって嘘とするか……か。ふむ……。'
 hide nao_v001
 hide beatrice_v001
 with Dissolve(0.2)
 show dlanor_v001 odoroki at mei_center
 with Dissolve(0.5)
 show dlanor_v001 odoroki at active
 dlanor '……驚きマシタ。実に飲み込みが早いデス。\n少女ながら聡明、実に面白いデス……。'
 hide dlanor_v001
 with Dissolve(0.2)
 show nao_v001 smile at mei_right
 show beatrice_v001 smile at mei_left
 with Dissolve(0.5)
 show beatrice_v001 smile at active
 show nao_v001 smile at inactive
 beatrice '菜央には、ミステリーの才能がありそうだな。\nもっともそれは、今後の研鑽次第ではあるが。'
 show nao_v001 smile at active
 show beatrice_v001 smile at inactive
 nao 'あら、そう？\nそんなふうに言ってもらえると、嬉しいわ。'
 show nao_v001 normal at active
 show beatrice_v001 smile at inactive
 nao 'けど、あたしはあなたたちに出会わなければ\nきっと『ノックス十戒』を知ることも\nなかったでしょうね。'
 show nao_v001 smile at active
 show beatrice_v001 smile at inactive
 nao 'ありがとうドラノール、面白いルールを教えてくれて。\nこんなものがあるなら、もっと早く知りたかったわ。'
 hide beatrice_v001
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show nao_v001 smile at inactive
 dlanor '…………。'
 show nao_v001 fuan at active
 show dlanor_v001 normal at inactive
 nao 'ドラノール？'
 hide dlanor_v001
 show beatrice_v001 futeki at mei_left
 with Dissolve(0.5)
 show beatrice_v001 futeki at active
 show nao_v001 fuan at inactive
 beatrice 'くっくっく！\u3000ドラノール卿は\n驚いているのであろうよ。'
 show beatrice_v001 futeki_close at active
 show nao_v001 fuan at inactive
 beatrice '『ノックス十戒』を定めたのは、\n何を隠そうドラノール卿のお父上であるからな。'
 show nao_v001 odoroki at jump_transform,active
 show beatrice_v001 futeki_close at inactive
 nao 'えっ……？\nこれ、ドラノールのお父さんが作ったの？'
 hide beatrice_v001
 show dlanor_v001 normal_close at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal_close at active
 show nao_v001 odoroki at inactive
 dlanor '……ハイ、そうデス。'
 show nao_v001 normal at active
 show dlanor_v001 normal_close at inactive
 nao 'そう。『ノックス十戒』は\n読者が作ったのかと思ったけど……\nそうか、作者の味方でもあるのね。'
 hide dlanor_v001
 show beatrice_v001 normal at mei_left
 with Dissolve(0.5)
 show beatrice_v001 normal at active
 show nao_v001 normal at inactive
 beatrice 'ほぅ。何をもってそう思った？'
 show nao_v001 smile at active
 show beatrice_v001 normal at inactive
 nao 'だって、作者が『ノックス十戒』に従っているって\n最初に宣言すれば、このミステリーは解けるように\nできているってわかる人はわかってくれるでしょ？'
 show nao_v001 smile_close at active
 show beatrice_v001 normal at inactive
 nao '……なるほど。だから『ノックス十戒』は\n邪魔だって排除されず、作者が書く上での\nルールとして定着しているのね。'
 show nao_v001 smile at active
 show beatrice_v001 normal at inactive
 nao '自分たちは読者に対して\nフェアだって主張できる、\n大事なブランドロゴみたいなものだもの。'
 hide beatrice_v001
 show dlanor_v001 odoroki at mei_left
 with Dissolve(0.5)
 show dlanor_v001 odoroki at active
 show nao_v001 smile at inactive
 dlanor '…………。'
 show nao_v001 fuan at active
 show dlanor_v001 odoroki at inactive
 nao 'でもブランドを守るのって大変よね。\n偽物を出されたりしたら、本家の評判に響くし。'
 show nao_v001 fuan_close at active
 show dlanor_v001 odoroki at inactive
 nao 'うちのお母さんも、頭を悩ませてたわ。\nにしても、偽物を売られたら本家本元に\n怒りの矛先が向くって、理不尽な話よね。'
 hide dlanor_v001
 show beatrice_v001 smile at mei_left
 with Dissolve(0.5)
 show beatrice_v001 smile at active
 show nao_v001 fuan_close at inactive
 beatrice '……面白い例え話よ。\nだが、ルールを守った者が損をするのは\n実に理不尽といえよう。'
 show beatrice_v001 smile at active
 show nao_v001 fuan_close at inactive
 beatrice 'ゆえに、この御仁の仕事はルールを守り\nミステリーを構築する人を守る。\n粗悪なミステリーを切り捨てることなのだ。'
 show nao_v001 smile at active
 show beatrice_v001 smile at inactive
 nao 'へぇ……そうなんだ。\nそんな監視をしてくれる役割の人が\n常駐してるって、羨ましい話よね。'
 show nao_v001 fuan_close at active
 show beatrice_v001 smile at inactive
 nao 'ファッション業界にも、\n偽ブランド服やバッグを作って売る悪人を\n斬り捨てる組織とかないかしら。'
 hide beatrice_v001
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show nao_v001 fuan_close at inactive
 dlanor '…………。'
 show nao_v001 fuan at active
 show dlanor_v001 normal at inactive
 nao 'どうしたの、ドラノール。'
 show dlanor_v001 normal_close at active
 show nao_v001 fuan at inactive
 dlanor 'いえ……ありがとうございマス。'
 show nao_v001 odoroki at active
 show dlanor_v001 normal_close at inactive
 nao 'は……？\nあたし、お礼を言われるようなことを言った？'
 hide dlanor_v001
 show beatrice_v001 smile_close at mei_left
 with Dissolve(0.5)
 show beatrice_v001 smile_close at active
 show nao_v001 odoroki at inactive
 beatrice '疲れているのであろう。\n疲弊している時に考え事をするべきではないぞ。\n最終的に死ぬしかなくなってしまうからな。'
 show nao_v001 fuan at active
 show beatrice_v001 smile_close at inactive
 nao '……ミステリーのルールを守るのも、\n大変なことなのね。'
 hide beatrice_v001
 show dlanor_v001 smile at mei_left
 with Dissolve(0.5)
 show dlanor_v001 smile at active
 show nao_v001 fuan at inactive
 dlanor '……ですが、あなたのように\n必要だと言ってくれる人に出会えると、\nとても嬉しいデス。'
 show dlanor_v001 smile_close at active
 show nao_v001 fuan at inactive
 dlanor 'あなたに会えて、よかったデス。'
 show nao_v001 smile at active
 show dlanor_v001 smile_close at inactive
 nao 'こちらこそ、教えてくれてありがとう。\nおかげでミステリーに興味が湧いてきたわ。'
 hide dlanor_v001
 show beatrice_v001 normal_close at mei_left
 with Dissolve(0.5)
 show beatrice_v001 normal_close at active
 show nao_v001 smile at inactive
 beatrice 'ふむ……宴もたけなわだが、そろそろだな。'
 show nao_v001 odoroki at active
 show beatrice_v001 normal_close at inactive
 nao 'えっ、もうお開き？'
 show beatrice_v001 smile at active
 show nao_v001 odoroki at inactive
 beatrice 'そうだ。また会おうぞ、菜央よ。'
 show nao_v001 odoroki at chara_shake_transform,active
 show beatrice_v001 smile at inactive
 nao 'えっ、あっ……！！'
 return