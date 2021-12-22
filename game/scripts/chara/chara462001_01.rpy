label chara462001_01:
 show black_background onlayer black
 stop sound
 scene expression "#000"
 play music 'audio/bgm/BGM_QUEST6_COLLAB2.wav'
 show expression 'images/bg/AdvBg_2220.png' as bg
 with Dissolve(1.0)
 show erika_v001 smile at mei_center
 with Dissolve(0.5)
 show erika_v001 smile at chara_shake_transform,active
 erika 'あぁっ、ようこそお越しくださいました！\n我が主におかれましては、ご機嫌麗しくっ――。'
 hide erika_v001
 with Dissolve(0.2)
 Character('????',ctc="ctcArrow", ctc_position="fixed") '…………。'
 show erika_v001 odoroki at mei_center
 with Dissolve(0.5)
 show erika_v001 odoroki at active
 erika '……あ、あの……我が主？\nなんだかとても、お顔の色がよろしくないように\nお見受けいたしましたが……。'
 hide erika_v001
 with Dissolve(0.2)
 Character('????',ctc="ctcArrow", ctc_position="fixed") 'あら……そう？\n私はとても健康だし、心は深淵の闇のように\n澄み渡っているんだけど……。'
 show erika_v001 odoroki at mei_center
 with Dissolve(0.5)
 show erika_v001 odoroki at active
 erika 'そ……それは、とても重畳に存じますが……\nひょっとしてあの、……怒っておられますか？'
 hide erika_v001
 with Dissolve(0.2)
 Character('????',ctc="ctcArrow", ctc_position="fixed") '……怒る？\u3000私が？\u3000あらあら、それは心外ね。\nこの胸のうちで溶岩が煮えくり返るくらいに\n不機嫌になる理由が、まるで思い当たらないんだけれど。'
 Character('????',ctc="ctcArrow", ctc_position="fixed") 'それとも……もしかしてあんたには\n何か心当たりでもあるのかしら？'
 Character('????',ctc="ctcArrow", ctc_position="fixed") 'ああ…あるわよね。私の駒にしながら\n一人だけ敗者なんてみっともない姿を\nさらしてきたんだもの…。'
 show erika_v001 odoroki at mei_center
 with Dissolve(0.5)
 camera at screenshake_transform
 pause 0.0
 show erika_v001 odoroki at active
 erika 'ひっ……ひいいいぃぃぃいぃっっ？\nま、まさか先日の、あの小娘との一件を\nお聞き及びになって……？！'
 show erika_v001 odoroki_close at active
 erika 'い……いやその、あのっ！\nあ、あれは生意気なガキのお遊びに\n軽く付き合ってやっただけと申しますか……！'
 show erika_v001 sinken at jump_transform,active
 erika 'け、決して負けたわけではありませんッ！\nあのままゲームを続けていれば、私の勝利は\n確実で絶対！\u3000小揺るぎもしませんでしたッ！'
 hide erika_v001
 with Dissolve(0.2)
 Character('????',ctc="ctcArrow", ctc_position="fixed") 'あらそう？\nそれなら待ってあげてもよかったかしらね……\nなんていうとでも思った？'
 Character('????',ctc="ctcArrow", ctc_position="fixed") '一度別の駒に勝って、調子に乗ってんじゃないの。\nあんた私の駒のくせに思い上がるなんて\n情けなくて笑えるわ。'
 show erika_v001 sinken at mei_center
 with Dissolve(0.5)
 show erika_v001 sinken at active
 erika 'え？\u3000あの、別の駒とは……？'
 hide erika_v001
 with Dissolve(0.2)
 Character('????',ctc="ctcArrow", ctc_position="fixed") '……話を聞いていないようね？\n私は今、思い上がったかどうか聞いているのだけれど。'
 show erika_v001 odoroki at mei_center
 with Dissolve(0.5)
 show erika_v001 odoroki at chara_shake_transform,active
 erika 'いっ、いいえっっ！\nお、思い上がるなど決して、そんな……！！'
 hide erika_v001
 with Dissolve(0.2)
 Character('????',ctc="ctcArrow", ctc_position="fixed") '……あら、そう。でも、油断したスキをつかれて\n手ひどくしっぺ返しを食らったらしいじゃない。\n『青』でも相手を仕留めきれずに……。'
 show erika_v001 sinken at mei_center
 with Dissolve(0.5)
 camera at screenshake_transform
 pause 0.0
 show erika_v001 sinken at active
 erika 'んなっ？！\u3000だ、誰がバラし……じゃないっ！\nそのような世迷いし戯言を、あなた様のお耳に\n入れたのはどなたですかっ？！'
 hide erika_v001
 with Dissolve(0.2)
 Character('????',ctc="ctcArrow", ctc_position="fixed") '説明の必要はないわ。負けるにしても、\nもう少し面白いものが見られるかと思っていたのだけれど…。'
 Character('????',ctc="ctcArrow", ctc_position="fixed") 'あんたにそんな器用な真似が\nできるはずなんてなかったわね……くすくす。'
 Character('????',ctc="ctcArrow", ctc_position="fixed") 'とりあえず、主人である私の顔に\n泥を塗ってくれたご褒美は\nちゃんとしてあげないとね……'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 odoroki at active
 erika 'お、おおおお、お待ちください我が主っ？\nせめて私の話をお聞き届け下さい！\nそしてご再考を――？！'
 play audio 'audio/sfx/SE_335_ls_magmafire.wav'
 show erika_v001 odoroki_close at chara_shake_transform,active
 erika '……んぎゃっばぶりぎげらぁん、\nごはへががががぁぁっっ？！'
 stop music fadeout 0.5
 window hide None
 show expression "#000" as fade with Dissolve(1.0)
 hide erika_v001
 with Dissolve(0.2)
 stop sound
 scene expression "#000"
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 play music 'audio/bgm/BGM_QUEST5_COLLAB2.wav'
 show expression 'images/bg/AdvBg_2190.png' as bg
 with Dissolve(1.0)
 show erika_v001 sinken at mei_left
 with Dissolve(0.5)
 camera at screenshake_transform
 pause 0.0
 show erika_v001 sinken at active
 erika 'どぉぉおぉるあぁぁぁのおぉぉぉるぅぅぅっっ！！\nいたら返事しなさい、どらのーーーるぅぅ！！'
 show dlanor_v001 normal at mei_right
 with Dissolve(1.0)
 show dlanor_v001 normal at active
 show erika_v001 sinken at inactive
 dlanor '……お呼びデスカ、ヱリカ。\n真っ黒な顔で、ドレスが焦げてマス。\nまるで火か何かに炙られたようデス。'
 show erika_v001 sinken at active
 show dlanor_v001 normal at inactive
 erika '「ように」じゃなくて、実際に炙られたんです！\n本気で白い灰にされて、地上にばら撒かれるかと\n思いました……！'
 show dlanor_v001 normal at active
 show erika_v001 sinken at inactive
 dlanor '……山に散ったら、\n春には綺麗な花が咲きマスカ？'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show erika_v001 smile at active
 show dlanor_v001 normal at inactive
 erika 'えぇ、ばっちりです。その桜の木の下で\n杯を傾けながら、私の推理ショーの\nはじまりはじまり――。'
 camera at screenshake_transform
 pause 0.0
 show erika_v001 fuan at active
 show dlanor_v001 normal at inactive
 erika 'なワケねェえぇええええぇええだらァ\nあああぁアぁああああぁ！！'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 show dlanor_v001 smile_close at active
 show erika_v001 fuan at inactive
 dlanor '冗談デス。'
 show erika_v001 sinken at updown_shake_transform,active
 show dlanor_v001 smile_close at inactive
 erika 'はぁ、はぁ、はぁ……ってあなた、\n冗談を言うなんて妙にご機嫌のようですね。\n何かいいことでもあったんですか？'
 show dlanor_v001 normal at active
 show erika_v001 sinken at inactive
 dlanor 'イイエ。特にありマセン……ヱリカは、\nベルンカステル卿にお仕置きされたのデスカ？'
 play audio 'audio/sfx/SE_226_shine.wav'
 show erika_v001 futeki at active
 show dlanor_v001 normal at inactive
 erika 'その通りッ！\nこの私にここまでの罰を与えることができるのは、\n世界で我が主だけに決まっていますッ！'
 show dlanor_v001 fuan at active
 show erika_v001 futeki at inactive
 dlanor '……なぜヱリカが誇らしげなのでショウ。'
 show expression "#000" as fade with Dissolve(1.0)
 hide erika_v001
 hide dlanor_v001
 with Dissolve(0.2)
 stop sound
 scene expression "#000"
 show expression 'images/card/Card_462001.png' as bg
 with Dissolve(1.0)
 erika 'とにかくっ！\u3000我が主のご不興を少しでも\n鎮めるためにも、ここは第２回戦しかありません！'
 erika '先日はベアトリーチェの誕生日だったから\n華を持たせましたが…'
 erika '別れを惜しんだ友人とはいえ、我が主のために\nあらためて菜央さんには私の優位を見せなければなりません！'
 erika '菜央さんのもとへのルートはベアトリーチェが\n確保していますが、\n幸いヤツらは移動のための準備を整えている真っ最中。'
 erika '今なら邪魔が入る心配もありません……。\nというわけでドラノール、あなたも向かいますよ！'
 erika 'くっくっく……今度こそパーフェクトゲームで、\n探偵としても、ワニャラーとしても徹底的に\n叩き潰してやりますよッ！！'
 show expression "#000" as fade with Dissolve(1.0)
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2190.png' as bg
 with Dissolve(1.0)
 show dlanor_v001 normal_close at mei_right
 show erika_v001 smile at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal_close at active
 show erika_v001 smile at inactive
 dlanor '――お断りしマス。'
 camera at screenshake_transform
 pause 0.0
 show erika_v001 odoroki at active
 show dlanor_v001 normal_close at inactive
 erika 'んなっ？\u3000ど、どうしてですか？！'
 show dlanor_v001 normal at active
 show erika_v001 odoroki at inactive
 dlanor '大法院は私的な決闘を認めマセン。\n個人的な鬱憤晴らしに判決を下そうなど、\nミステリーに対する冒涜の極みデス。'
 show dlanor_v001 normal at active
 show erika_v001 odoroki at inactive
 dlanor '前回は、奇跡により生まれたゲーム盤デシタ。\n内容を吟味するため、あなたに同行しただけデス。'
 show dlanor_v001 fuan_close at active
 show erika_v001 odoroki at inactive
 dlanor '……それに、私は片づけるべき\n仕事が山積みデス。行くのはヱリカ、\nあなたお一人でお願いしマス。'
 show erika_v001 sinken at chara_shake_transform,active
 show dlanor_v001 fuan_close at inactive
 erika 'っ……わかりましたよっ！\n友人のあなたなら、私のこの気持ちを\n理解してくれると思っていましたのに……！'
 show erika_v001 sinken at active
 show dlanor_v001 fuan_close at inactive
 erika 'では、菜央さんの所在を\n我が主にお借りしたこちらのアイテムで……。'
 show erika_v001 odoroki at active
 show dlanor_v001 fuan_close at inactive
 erika 'あれ？\u3000とっくに自分の盤に\n戻っているはずなのに、いない……？\nいや、見つからない……？'
 show erika_v001 sinken at active
 show dlanor_v001 fuan_close at inactive
 erika 'これも、『迷い子』であるせいでしょうか。\nはぁ、面倒くさい……こうなったら直接行って、\nこっちの空間に呼びつけるとしましょう。'
 hide erika_v001
 with Dissolve(0.6)
 show dlanor_v001 fuan at active
 dlanor '……行かれマシタカ。\nあの感情の大きなブレさえなければ、\nとても優秀な方なのデスガ……。'
 show dlanor_v001 fuan_close at active
 dlanor '……。仕方ありマセン。'
 return