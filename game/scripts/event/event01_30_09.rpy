label event01_30_09:
 stop sound
 scene expression "#000"
 play music 'audio/bgm/BGM_QUEST1_COLLAB2.wav'
 show expression 'images/bg/AdvBg_2190.png' as bg
 with Dissolve(1.0)
 show erika_v001 normal at mei_left
 show beatrice_v001 normal at mei_right
 with Dissolve(0.5)
 show beatrice_v001 normal at active
 show erika_v001 normal at inactive
 beatrice 'それでは妾の手番であるな。お次はヱリカを攻めさせてもらうぞ。'
 show beatrice_v001 normal at active
 show erika_v001 normal at inactive
 beatrice 'ヱリカの主張は、詩音が犯人である、ということだったな？'
 show beatrice_v001 normal at active
 show erika_v001 normal at inactive
 beatrice '……それを確信できるものが何かあるなら、妾に示してはくれぬ\nか？'
 show erika_v001 normal at active
 show beatrice_v001 normal at inactive
 erika '受けてもいいですけれど……。致命傷になりますよ？'
 hide erika_v001
 hide beatrice_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao '確かにあの時、小道具を探しにゲストハウスへ戻っていた詩音さん\nだけが、アリバイを失ってるけれど……。'
 hide nao_v002
 with Dissolve(0.2)
 narrator '\u3000アリバイがないからというだけの理由で、詩音さんを犯人になん\nかさせない。'
 show nao_v002 normal at mei_left
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show nao_v002 normal at inactive
 dlanor 'ベアトリーチェ卿。貴女の手番はそれで構わないデスカ。'
 show nao_v002 normal at active
 show dlanor_v001 normal at inactive
 nao '……あたしも知りたいわ。ベアトリーチェ、お願い。'
 hide nao_v002
 hide dlanor_v001
 with Dissolve(0.2)
 show erika_v001 normal at mei_left
 show beatrice_v001 normal_close at mei_right
 with Dissolve(0.5)
 show beatrice_v001 normal_close at active
 show erika_v001 normal at inactive
 beatrice 'うむ。それでは切り込ませてもらう！'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show beatrice_v001 futeki at active
 show erika_v001 normal at inactive
 beatrice '示せ、ヱリカよ！\u3000詩音が犯人であるとする根拠をな！'
 show erika_v001 normal_close at active
 show beatrice_v001 futeki at inactive
 erika 'それでは、お受けいたします。'
 show erika_v001 futeki at active
 show beatrice_v001 futeki at inactive
 erika '詩音さんには、私の部屋に侵入したことを示す、明白な証拠が残っ\nているからです！'
 window hide None
 show expression "#000" as fade with Dissolve(1.0)
 stop sound
 scene expression "#000"
 hide beatrice_v001
 with Dissolve(0.3)
 show expression 'images/bg/AdvBg_2281.png' as bg
 with Dissolve(1.0)
 pause 2.0
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show shion_v007 odoroki at mei_center
 with Dissolve(0.5)
 show shion_v007 odoroki at jump_transform,active
 shion 'え？！\u3000な、何ですか、一体……！'
 hide shion_v007
 with Dissolve(0.2)
 narrator '\u3000自分の部屋に魔法陣が現れて、\nヱリカさんは恐怖に震えているものだとばかり思っていた。'
 narrator '\u3000その彼女が突然、罠にかかったな馬鹿めッ、と書いてあるかのよ\nうな表情で笑い出したのだ……。'
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika '茶番にお付き合いをありがとうございました。'
 show erika_v001 normal at active
 erika 'それでは、種明かしと参りましょう。'
 show erika_v001 normal at active
 erika '皆さんはたった今。私の悲鳴を聞き、開け放たれたままの扉より入\n室しました。'
 show erika_v001 normal at active
 erika 'つまり。皆さんは誰一人、この部屋の扉の、ドアノブに触れた人間\nはいないのです。'
 hide erika_v001
 with Dissolve(0.2)
 show shion_v007 sinken at mei_left
 show mion_v008 sinken at mei_right
 with Dissolve(0.5)
 show mion_v008 sinken at active
 show shion_v007 sinken at inactive
 mion '……どういうこと……？\u3000……まさか………。'
 show shion_v007 sinken at active
 show mion_v008 sinken at inactive
 shion '…………………………。'
 hide shion_v007
 hide mion_v008
 with Dissolve(0.2)
 narrator '\u3000園崎姉妹の顔が青ざめて見える。\n\u3000……じゃあやっぱり、この魔法陣は詩音さんの仕業……？！'
 show nao_v002 normal at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show nao_v002 normal at inactive
 erika 'それでは皆さん。その場で少しお待ちください。カーテンを閉めさ\nせてもらいます。'
 show nao_v002 normal at active
 show erika_v001 normal at inactive
 nao '……何を始める気？'
 show erika_v001 normal at active
 show nao_v002 normal at inactive
 erika '園崎詩音さん。こちらへ。'
 hide nao_v002
 show shion_v007 normal at mei_left
 with Dissolve(0.5)
 show shion_v007 normal at active
 show erika_v001 normal at inactive
 shion '……犯人扱いは心外ですけど、変に断っても疑われますし。'
 hide erika_v001
 hide shion_v007
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_229_grap.wav'
 narrator '\u3000詩音さんが歩み出ると、……まるで手錠のように、……ガシリと、\nヱリカさんは詩音さんの手首を掴んだ。'
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika 'チェックメイトですよ？\u3000詩音さん。'
 hide erika_v001
 with Dissolve(0.2)
 show nao_v002 sinken at mei_left
 show mion_v008 sinken at mei_right
 with Dissolve(0.5)
 show mion_v008 sinken at active
 show nao_v002 sinken at inactive
 mion 'ヱリカさんは、部屋の鍵を忘れたと言った後に、ゲストハウスに\n戻った為、アリバイがないからって詩音を疑ってるんでしょ？！'
 show nao_v002 sinken at active
 show mion_v008 sinken at inactive
 nao 'そうです。アリバイがないことが即ち、犯人を意味するものではな\nいはずです。'
 hide nao_v002
 hide mion_v008
 with Dissolve(0.2)
 show erika_v001 normal at mei_right
 show shion_v007 sinken at mei_left
 with Dissolve(0.5)
 show shion_v007 sinken at active
 show erika_v001 normal at inactive
 shion '私はこの部屋には入ってませんっ。入ったというなら、証拠を見せ\nて下さい！'
 show erika_v001 smile at active
 show shion_v007 sinken at inactive
 erika 'グッド！\u3000……その言葉を聞きたかったです♪'
 hide erika_v001
 hide shion_v007
 with Dissolve(0.2)
 narrator '\u3000ギリリと、小さく歯軋りの音が聞こえた。\n\u3000詩音さんの顔は、……苦々しく歪んでいた。'
 play audio 'audio/sfx/SE_5005_grab.wav'
 narrator '\u3000ヱリカさんの掴む手が、力強くて痛いのか。……それとも、証拠\nはもはや、致命的なのか。'
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika '菜央ちゃま。部屋の灯りを消してくれますか？\u3000大丈夫。ペンライ\nトは持ってますので。'
 hide erika_v001
 with Dissolve(0.2)
 narrator '\u3000ペンライトとは言うが、傍目には少し太めの万年筆にしか見えな\nい。'
 narrator '\u3000しかしヱリカさんが片手で操作すると、確かにライトの機能があ\nることがわかった……。'
 show nao_v002 normal at mei_left
 show mion_v008 sinken at mei_right
 with Dissolve(0.5)
 show mion_v008 sinken at active
 show nao_v002 normal at inactive
 mion 'ふん……。詩音がやったっていう証拠があるなら、見せてもらおう\nじゃない。'
 show mion_v008 normal at active
 show nao_v002 normal at inactive
 mion '菜央ちゃん。消してくれる？'
 show nao_v002 normal_close at active
 show mion_v008 normal at inactive
 nao '……わかりました。'
 play audio 'audio/sfx/SE_5004_lightoff.wav'
 show expression "#000" as fade with Dissolve(1.0)
 hide nao_v002
 hide mion_v008
 with Dissolve(0.2)
 play sound ['audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav'] fadeout 1.0
 stop music fadeout 2.0
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2283.png' as bg
 with Dissolve(1.0)
 narrator '\u3000この季節、だいぶ暗くなるのも早くなって来ている。\n\u3000カーテンを閉めて灯りを消せば、真の闇だった。'
 narrator '\u3000すぐにヱリカさんがペンライトを点灯する。'
 show mion_v008 normal at mei_center
 with Dissolve(0.5)
 show mion_v008 normal at active
 mion 'スパイ道具みたいだねぇ。一見、万年筆なのにライトになるなん\nて。'
 show mion_v008 normal at active
 mion '他にも秘密の機能が備わってそうだねぇ。'
 hide mion_v008
 with Dissolve(0.2)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika 'ご賢察です。もちろん、ペンライトの機能だけではありません。'
 show erika_v001 normal_close at active
 erika 'その機能を説明する前に、私がドアノブに仕掛けた秘密を、ご説明\nしましょう。'
 play music 'audio/bgm/BGM_QUEST3_COLLAB2.wav'
 show erika_v001 normal at active
 erika '私が自分の部屋の施錠を忘れ、それを皆さんの前で口にしたのも、\n全ては犯人を誘う為の罠でした。'
 show erika_v001 normal at active
 erika '犯人は、この千載一遇のチャンスを生かす為に、適当な口実を設け\nて、ゲストハウスへ戻ったのです。'
 hide erika_v001
 with Dissolve(0.2)
 show mion_v008 sinken at mei_right
 show shion_v007 sinken at mei_left
 with Dissolve(0.5)
 show shion_v007 sinken at active
 show mion_v008 sinken at inactive
 shion '私は撮影の為の道具を探しに戻っただけですっ。この部屋に入って\nなんかいません！'
 show mion_v008 sinken at active
 show shion_v007 sinken at inactive
 mion '……ドアノブに仕掛けた秘密って、……何さ。'
 hide mion_v008
 hide shion_v007
 with Dissolve(0.2)
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 nao 'あ、………ひょっとして………。'
 hide nao_v002
 with Dissolve(0.2)
 narrator '\u3000まさかだけど、……指紋？\n\u3000知識と道具があれば、出来ないことじゃない。'
 narrator '\u3000ましてや、探偵を自称するヱリカさんのこと。ドアノブに残った\n指紋から、詩音さんを特定したとか……！'
 show nao_v002 fuan at mei_left
 show erika_v001 normal_close at mei_right
 with Dissolve(0.5)
 show erika_v001 normal_close at active
 show nao_v002 fuan at inactive
 erika 'いえいえ。もっとシンプルでわかりやすく、そして明白にわかる仕\n掛けです。'
 show erika_v001 normal at active
 show nao_v002 fuan at inactive
 erika '菜央ちゃま。このペンライト、持ってくれます？'
 show nao_v002 fuan at active
 show erika_v001 normal at inactive
 nao 'え？\u3000はい……。'
 show erika_v001 normal at active
 show nao_v002 fuan at inactive
 erika 'そこのところを、クリッと手応えがあるまで捻って下さい。'
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 narrator '\u3000言われた通りにすると、ペンライトの灯りが消えた。\n\u3000変わって、薄っすらと青紫色の弱い光が放たれる。'
 show mion_v008 normal at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show mion_v008 normal at inactive
 nao 'これは………。'
 show mion_v008 normal at active
 show nao_v002 normal at inactive
 mion 'ブラックライト、……だね？'
 hide mion_v008
 hide nao_v002
 with Dissolve(0.2)
 show erika_v001 normal at mei_right
 show shion_v007 fuan at mei_left
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_5005_grab.wav'
 show shion_v007 fuan at chara_shake_transform,active
 show erika_v001 normal at inactive
 shion '……ちょ、痛い……。もう少し優しく握って下さいっ。'
 show erika_v001 normal at active
 show shion_v007 fuan at inactive
 erika '菜央ちゃま。そのブラックライトで、私の手の平を照らしてくれま\nすか？'
 hide erika_v001
 hide shion_v007
 with Dissolve(0.2)
 show nao_v002 odoroki at mei_center
 with Dissolve(0.5)
 show nao_v002 odoroki at active
 nao 'こうですか？\u3000…………あッ、'
 hide nao_v002
 with Dissolve(0.2)
 show erika_v001 normal at mei_right
 show shion_v007 sinken at mei_left
 with Dissolve(0.5)
 show shion_v007 sinken at active
 show erika_v001 normal at inactive
 shion '……チッ。……あんた、こんな道具を旅先に持ち歩いてんです\nか……。'
 show erika_v001 normal at active
 show shion_v007 sinken at inactive
 erika '探偵ですから。バカンス先でも、最低限の探偵道具は持ち込んでい\nます。'
 hide erika_v001
 hide shion_v007
 with Dissolve(0.2)
 show mion_v008 normal at mei_center
 with Dissolve(0.5)
 show mion_v008 normal at active
 mion '……蛍光塗料……か……。'
 hide mion_v008
 with Dissolve(0.2)
 narrator '\u3000ブラックライトに弱々しく照らされたヱリカさんの手の平\nは……、薄い黄緑色に、光っていた……。'
 show shion_v007 sinken at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show shion_v007 sinken at inactive
 erika 'これを、今朝、この部屋のドアノブに塗らせていただきました。'
 show erika_v001 normal at active
 show shion_v007 sinken at inactive
 erika '特殊な配合で、丸一日は、ドアノブに触れた人全員の手に付着しま\nす。'
 show erika_v001 normal at active
 show shion_v007 sinken at inactive
 erika 'さらに、一度、付着すれば、お風呂で洗ったくらいでは落ちませ\nん。'
 camera at screenshake_transform
 pause 0.0
 show shion_v007 sinken at active
 show erika_v001 normal at inactive
 shion '……くっ……………。'
 show erika_v001 normal_close at active
 show shion_v007 sinken at inactive
 erika '私が自分で作った、特別な配合の薬品です。落とすのにも特殊な薬\n品が必要ですが、もちろん持ってきていますのでご安心を。'
 show shion_v007 sinken at active
 show erika_v001 normal_close at inactive
 shion '……上等じゃないですか。つまり、いくらシャワーを浴びていよう\nと、私の手にはまだその蛍光塗料が残ってるって訳ですよね？'
 show erika_v001 normal at active
 show shion_v007 sinken at inactive
 erika 'そういうことです。今から、ブラックライトで、貴女の手の平を拝\n見します。'
 show erika_v001 normal at active
 show shion_v007 sinken at inactive
 erika 'ですが……、探偵の情けです。致命的な証拠を突きつけられる屈辱\nよりは、紳士的に自ら負けを認める機会を与えましょう。'
 show shion_v007 normal_close at active
 show erika_v001 normal at inactive
 shion '……貴女の探偵ごっこがどういうものかは知りませんが。……もし\nそれに、勝ち負けがあるものならば。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide shion_v007
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 show mion_v008 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show mion_v008 sinken at active
 mion '園崎姉妹は、……絶対に負けないよ。……園崎家次期頭首の血、二\n人に分かれてなお熱くて濃く受け継がれていること、証明してあげ\nるよ。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide mion_v008
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika '犯人は貴女です、詩音さん。にもかかわらず、私が負けになるとい\nう結果があるんですか？\u3000何を言ってるのかよくわかりません。'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 camera at screenshake_transform
 pause 0.0
 show erika_v001 fuan at active
 erika 'さぁ、情けの時間は終わりです！\u3000貴女の両手の手の平！！\u3000照ら\nし出させてもらいますううぅ！！\u3000うへへううぇっうぇっうぇえぇ\nえぇ！！！'
 stop music fadeout 0.5
 window hide None
 show expression "#000" as fade with Dissolve(1.0)
 hide erika_v001
 with Dissolve(0.2)
 pause 2.0
 stop sound
 scene expression "#000"
 play music 'audio/bgm/BGM_BOSS1_COLLAB2.wav'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 show expression 'images/bg/AdvBg_2190.png' as bg
 with Dissolve(1.0)
 show dlanor_v001 normal at mei_right
 show erika_v001 odoroki at mei_left
 with Dissolve(0.5)
 show erika_v001 odoroki at active
 show dlanor_v001 normal at inactive
 erika '何ですって？\u3000も、もう一度……！！'
 show dlanor_v001 normal at active
 show erika_v001 odoroki at inactive
 dlanor '園崎詩音の手に、蛍光塗料の付着はありマセン。'
 show erika_v001 sinken at active
 show dlanor_v001 normal at inactive
 erika 'だから何ですって？！\u3000もう一度ッ！！！'
 show dlanor_v001 normal at active
 show erika_v001 sinken at inactive
 dlanor '手に限りまセン。園崎詩音の身体には、蛍光塗料の付着は一切あり\nマセン。'
 camera at screenshake_transform
 pause 0.0
 show erika_v001 odoroki at active
 show dlanor_v001 normal at inactive
 erika 'ああぁああぁあッ、どぅわからぁア！！\u3000もう一度、はっきりと赤\nで言えッつってんだらあああぁああぁッ！！！'
 show dlanor_v001 normal at active
 show erika_v001 odoroki at inactive
 dlanor '繰り返しマス。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide dlanor_v001
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 show dlanor_v001 normal at mei_center
 with Dissolve(0.08333333333333333)
 show expression "#e11" as fade with Dissolve(0.16666666666666666)
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 hide fade with Dissolve(0.16666666666666666)
 with Dissolve(0.16666666666666666)
 show dlanor_v001 normal at active
 dlanor '#ff0000園崎詩音の身体には、蛍光塗料の付着は一切ありマセン。#r'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide dlanor_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show dlanor_v001 normal at mei_right
 show erika_v001 odoroki at mei_left
 with Dissolve(0.5)
 camera at screenshake_transform
 pause 0.0
 show erika_v001 odoroki at active
 show dlanor_v001 normal at inactive
 erika 'い、いやいやそんなそんなッ！！\u3000あッ、あり得ない、あり得ませ\nんッ！！'
 hide dlanor_v001
 show beatrice_v001 futeki at mei_right
 with Dissolve(0.5)
 show beatrice_v001 futeki at active
 show erika_v001 odoroki at inactive
 beatrice 'おやぁ？\u3000これはおかしいのではないか、ヱリカよ。これでは魔女\nの仕業になってしまうぞぉ？'
 camera at screenshake_transform
 pause 0.0
 show erika_v001 sinken at active
 show beatrice_v001 futeki at inactive
 erika 'うるさいうるさい！\u3000うっせえうっせぇッうっせえわああぁああ\nあッ！！'
 hide erika_v001
 hide beatrice_v001
 with Dissolve(0.2)
 narrator '\u3000これでベアトリーチェの手番は終わる。\n\u3000次のヱリカさんの手番は、この状況を挽回する為に費やされる\nだろう。'
 narrator '\u3000今、ヱリカさんは強烈な一撃を喰らって、ぐらついている。\n\u3000その次に来るあたしの手番が重要になってくる……！'
 show erika_v001 sinken at mei_left
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show erika_v001 sinken at inactive
 dlanor 'ヱリカ。紳士と淑女のゲームデス。品のない言葉遣いは慎んで下サ\nイ。'
 show erika_v001 sinken at chara_shake_transform,active
 show dlanor_v001 normal at inactive
 erika 'おッぉおおおおうるさいでございましてよッ、殺人人形ッ！！\u3000次\nは私の手番ですッ！'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide erika_v001
 hide dlanor_v001
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 sinken at active
 erika '青き真実！'
 play audio 'audio/sfx/SE_391_ls_swing.wav'
 show expression "#fff" as flash with Dissolve(0.1)
 pause 0.1
 hide flash with Dissolve(0.2)
 show erika_v001 sinken at active
 erika '#4169e1園崎詩音は、手袋を使ってドアノブに触れた！\u3000だから蛍光塗料が#r\n#4169e1手の平に付着しないのは当然のこと！！#r'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show dlanor_v001 normal_close at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal_close at active
 dlanor '……有効デス。'
 window hide None
 show expression "#000" as fade with Dissolve(1.0)
 hide dlanor_v001
 with Dissolve(0.2)
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2281.png' as bg
 with Dissolve(1.0)
 show erika_v001 futeki at mei_center
 with Dissolve(0.5)
 show erika_v001 futeki at active
 erika 'ね？！\u3000塗料が付かないように部屋に入るのは可能なんです！！'
 show erika_v001 fuan at active
 erika '詩音さん、貴女は本当に悪い人ですねぇ……！！！'
 camera at screenshake_transform
 pause 0.0
 show erika_v001 fuan at active
 erika '人の部屋に侵入する際に、そこまでの用心が出来るなんてッ。プ\nロ！！\u3000職業的泥棒ッ！！\u3000シューペリアルエクストリーム犯罪者\nああぁああぁあぁッ！！'
 hide erika_v001
 with Dissolve(0.2)
 show mion_v008 normal at mei_right
 show shion_v007 normal_close at mei_left
 with Dissolve(0.5)
 show shion_v007 normal_close at active
 show mion_v008 normal at inactive
 shion '何とでも仰ってください。ちなみに、今のどれもが、私には誉め言\n葉ですので。'
 show mion_v008 normal at active
 show shion_v007 normal_close at inactive
 mion '……詩音にアリバイがないことは間違いないけれど、……これで、\n詩音がこの部屋に入ったという証拠もない訳だね？'
 hide mion_v008
 hide shion_v007
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao 'それでも詩音さんが犯人だっていうなら、他の何かを示して欲しい\nわっ。'
 show expression "#000" as fade with Dissolve(1.0)
 hide nao_v002
 with Dissolve(0.2)
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2190.png' as bg
 with Dissolve(1.0)
 show erika_v001 odoroki at mei_center
 with Dissolve(0.5)
 show erika_v001 odoroki at active
 erika '他の何か、他の何か、あわあわあわ……あぁぁぁぁあぁッ。'
 show erika_v001 odoroki_close at chara_shake_transform,active
 erika '大丈夫です、我が主……！\u3000私の推理は完璧ですっ。あぁあぁあぁ\nだから怒らないで怒らないで……。'
 hide erika_v001
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_left
 show beatrice_v001 smile at mei_right
 with Dissolve(0.5)
 show beatrice_v001 smile at active
 show dlanor_v001 normal at inactive
 beatrice '次の手番は、菜央であるな。進めても問題はなかろう？'
 show dlanor_v001 normal at active
 show beatrice_v001 smile at inactive
 dlanor 'どうぞ、菜央。貴女の手番デス。'
 hide dlanor_v001
 hide beatrice_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao 'えっと、ＣＯします。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show erika_v001 odoroki at active
 erika 'はあ……ッ？！？！'
 show erika_v001 sinken at active
 erika 'ただのいけ好かない、負けず嫌い以外に何の取り柄もセンスもない\nお子ちゃまが、何をＣＯするってんですッ？！？！'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show nao_v002 normal at mei_left
 show beatrice_v001 normal at mei_right
 with Dissolve(0.5)
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice '菜央よ。一体、何を告白するというのか……？'
 show nao_v002 normal_close at active
 show beatrice_v001 normal at inactive
 nao 'あたしは鳳谷菜央。……普通の人間のつもりですが、……実は、\n言っても誰も信じてくれない不思議な経験をしてきました。'
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao 'あたしは実際に、神や『ツクヤミ』といった超常の存在と出会い、\nこの世がニンゲンの考える世界だけで構成されてはいないことを、\n身をもって体験しています。'
 show beatrice_v001 odoroki at active
 show nao_v002 normal at inactive
 beatrice '……なんと……。そなたは……航海者の魔女だというの\nか……ッ？！'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide nao_v002
 hide beatrice_v001
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 sinken at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show erika_v001 sinken at active
 erika 'んなワケねぇですぅ！！！\u3000お前はちっぽけな、居てもいなくても\nいい塵芥のガキンチョでしょおがあぁああ！！'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show dlanor_v001 normal at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show dlanor_v001 normal at inactive
 nao 'ドラノールさん。嘘を吐く気はありません。\nあたしに、赤き真実を使わせて下さい。'
 show dlanor_v001 normal at active
 show nao_v002 normal at inactive
 dlanor 'どのような内容をデスカ……。'
 hide dlanor_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator '\u3000ドラノールさんの耳元で、それを囁く。'
 show nao_v002 normal at mei_left
 show dlanor_v001 odoroki at mei_right
 with Dissolve(0.5)
 show dlanor_v001 odoroki at active
 show nao_v002 normal at inactive
 dlanor '……わ、わかりマシタ。……それには、貴女の手札を拝見させてい\nただかなくてはなりマセン……。'
 show nao_v002 normal at active
 show dlanor_v001 odoroki at inactive
 nao '手札って？'
 hide nao_v002
 hide dlanor_v001
 with Dissolve(0.2)
 show beatrice_v001 normal_close at mei_center
 with Dissolve(0.5)
 show beatrice_v001 normal_close at active
 beatrice '……そなたのカケラを、ドラノールが見たがっている。'
 hide beatrice_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_left
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show nao_v002 normal at inactive
 dlanor 'もちろん、貴女の赤き真実にかかわる範囲でしか拝見はしマセン。\nまた、それ以外に知った事実も、天界大法院の名にかけて、生涯の\n守秘義務を誓いマス。'
 show nao_v002 normal at active
 show dlanor_v001 normal at inactive
 nao '……頭の中を覗くということ？\u3000構わないわ。'
 show dlanor_v001 sinken at active
 show nao_v002 normal at inactive
 dlanor 'それでは、……失礼させていただきマス……。'
 hide nao_v002
 hide dlanor_v001
 with Dissolve(0.2)
 narrator '\u3000ドラノールさんの目が、透き通るように淡い光を放った気がし\nた。'
 narrator '\u3000ただあたしを見つめているだけに見えるけれど、……不思議な\n居心地の悪さを覚える。'
 narrator '\u3000……なるほど。これが、あたしの手札を見る、ということなの\nか。'
 narrator '\u3000あたしが人生で経験してきたことや、考えや想い、感情などの全\nてが、他人に覗き見されているという居心地の悪さだ。'
 show beatrice_v001 normal at mei_right
 show dlanor_v001 normal_close at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal_close at active
 show beatrice_v001 normal at inactive
 dlanor '……菜央。ありがとうございマス。終わりマシタ。'
 show beatrice_v001 normal at active
 show dlanor_v001 normal_close at inactive
 beatrice 'それで……。ドラノールの判定は……。'
 show dlanor_v001 normal at active
 show beatrice_v001 normal at inactive
 dlanor '有効デス。'
 show expression "#e11" as fade with Dissolve(0.16666666666666666)
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 hide fade with Dissolve(0.16666666666666666)
 with Dissolve(0.16666666666666666)
 show dlanor_v001 normal at active
 show beatrice_v001 normal at inactive
 dlanor '#ff0000……鳳谷菜央が、人ならざる存在との接触や交流を経て来た#r\n#ff0000事実を、確認しマシタ。#r'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide beatrice_v001
 hide dlanor_v001
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 sinken at active
 erika 'あ、あんた……ッ、何者なんですかッ！！\u3000フェリーでたまたま出\n会っただけの、ガキンチョだと思ってたのに……ッ？！'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show nao_v002 normal at mei_left
 show beatrice_v001 normal at mei_right
 with Dissolve(0.5)
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice '紅茶を飲むならバケモノとに限る、は……、そなたの主の言葉で\nあったか。'
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice '……なるほど。魔女がゲーム盤を広げれば、魔女かバケモノ、ある\nいはそれに近い存在が、招かれるということなのか……。'
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao '神も怪異も、あらゆる不思議な存在も、この世界には実在していま\nす。'
 show nao_v002 normal_close at active
 show beatrice_v001 normal at inactive
 nao 'だからあたしは、ベアトリーチェの存在を、否定しません。ここに\n居ることが、その証なのですから。'
 show beatrice_v001 odoroki at active
 show nao_v002 normal_close at inactive
 beatrice 'わ、妾の存在を認めてくれるとは……、菜央、そなたのような客人\nは初めてだ……。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide nao_v002
 hide beatrice_v001
 hide fade with Dissolve(0.08333333333333333)
 show nao_v002 normal at mei_center
 with Dissolve(0.08333333333333333)
 show nao_v002 normal at active
 nao 'その上で、第一と第二の魔法陣事件について、改めて主張します。'
 show nao_v002 normal_close at active
 nao 'まず、今、俎上に上がっている第二の魔法陣事件。'
 play audio 'audio/sfx/SE_391_ls_swing.wav'
 show expression "#fff" as flash with Dissolve(0.1)
 pause 0.1
 hide flash with Dissolve(0.2)
 show nao_v002 normal at active
 nao '#4169e1容疑者である詩音さんは無実でした。#r'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show nao_v002 normal at mei_left
 show erika_v001 odoroki at mei_right
 with Dissolve(0.5)
 camera at screenshake_transform
 pause 0.0
 show erika_v001 odoroki at active
 show nao_v002 normal at inactive
 erika 'そんなはずないそんなはずないッ！！！\u3000詩音が犯人ッ！！\u3000犯人\nだあぁあっちゅゆうてんだぎゃああぁあぁ！！'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.1
 pause 0.5
 play audio 'audio/sfx/SE_391_ls_swing.wav'
 show nao_v002 normal at active
 show erika_v001 odoroki at inactive
 nao '#4169e1ヱリカさんもまた、ドアノブにベッドメイク不要の札を出していま#r\n#4169e1した。つまり、使用人は誰もあの部屋には入りません。#r'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.2
 pause 0.5
 play audio 'audio/sfx/SE_391_ls_swing.wav'
 pause 0.6666666666666666
 play audio 'audio/sfx/SE_391_ls_swing.wav'
 show nao_v002 normal at active
 show erika_v001 odoroki at inactive
 nao '#4169e1そして、唯一、部屋に入れたかもしれない詩音さんも、ヱリカさん#r\n#4169e1の仕掛けが逆に、無実を証明することとなりました。#r'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 play audio 'audio/sfx/SE_5036_glass_break.wav'
 show expression "#fff" as flash with Dissolve(0.1)
 pause 0.1
 hide flash with Dissolve(0.2)
 show nao_v002 sinken at active
 show erika_v001 odoroki at inactive
 nao '#4169e1以上により、第二の魔法陣事件は、ニンゲンには不可能である、魔#r\n#4169e1女の悪戯であることが明白となりました。#r'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide nao_v002
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show erika_v001 odoroki at active
 erika 'ぜッんぜん明白じゃねぇだらッ！！！\u3000どこがッ、誰がッ！！\u3000ふ\nざけた青を使うんじゃねええぇええッ！！！'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show nao_v002 sinken at mei_left
 show beatrice_v001 normal at mei_right
 with Dissolve(0.5)
 show beatrice_v001 normal at active
 show nao_v002 sinken at inactive
 beatrice '……菜央よ。妾を利しても良いのか？\u3000そなたが負けになってしま\nうぞ……？'
 show nao_v002 smile at active
 show beatrice_v001 normal at inactive
 nao '御心配なく。ちゃんと、その上であたしも勝ちますので。'
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao 'ドラノールさん。青き真実は有効ですか？'
 hide beatrice_v001
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show nao_v002 normal at inactive
 dlanor '有効デス。………ヱリカは、赤き真実か、それに相当する反論か証\n拠の提出が必要デス。'
 hide nao_v002
 show erika_v001 sinken_close at mei_left
 with Dissolve(0.5)
 show erika_v001 sinken_close at active
 show dlanor_v001 normal at inactive
 erika '…………………ぇよ……。'
 show dlanor_v001 normal at active
 show erika_v001 sinken_close at inactive
 dlanor '……聞こえませんデシタ。もう一度お願いしマス。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide dlanor_v001
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show erika_v001 odoroki at active
 erika 'ねぇよ……、ねぇよねぇよ全然ねぇよおッ。詩音が絶対絶対に犯人\nなのに、何で証拠が……証拠がねぇ…よオ……ッ！！'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 narrator '\u3000ヱリカさんは、ドアノブの蛍光塗料の仕掛けに\nオールインしていたのだろう。'
 narrator '\u3000唯一にして究極のはずだった切り札が失われ、……テンカウント\nを待つのみだ。'
 show nao_v002 normal at mei_left
 show beatrice_v001 normal_close at mei_right
 with Dissolve(0.5)
 show beatrice_v001 normal_close at active
 show nao_v002 normal at inactive
 beatrice '菜央。これでそなたの手番は終わる……。'
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice '……次は妾の手番。妾が、そなたの打ち立てた青き真実を以て、勝\n利を宣言して終わりとなるが、……良いのか？'
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao 'なので、あなたと交渉がしたいです。'
 show beatrice_v001 smile at active
 show nao_v002 normal at inactive
 beatrice 'ほう？\u3000そなたは妾を勝たせてくれた。借りはある。話を聞こう\nぞ……。'
 show nao_v002 normal at active
 show beatrice_v001 smile at inactive
 nao '次はあなたの手番ですが、勝利宣言の前に、一手、あたしの為にお\n願いしたいんです。'
 show nao_v002 normal at active
 show beatrice_v001 smile at inactive
 nao '第二の魔法陣は魔女の仕業だけれど、……第一の魔法陣は、ヱリカ\nさんが犯人。そして今、ようやく、紗音さんが魔法陣を見ても異常\nを感じなかった理由が、閃きました。'
 hide nao_v002
 hide beatrice_v001
 with Dissolve(0.2)
 narrator '\u3000ようやく、謎と推理と思考のスープが……、とろりと仕上が\nる……。'
 show beatrice_v001 normal at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao 'ベアトリーチェ。あなたは魔女ですよね？'
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice '無論であるとも。'
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao '当然、様々な魔法や儀式に精通しているんですよね？\u3000もちろん、\n魔法陣にも。'
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice 'うむ。これでも無限の魔女を名乗っている。知らぬものはないつも\nりだ。'
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao 'そのあなたが、さきほど言いました。……第一と第二の魔法陣を見\nて。'
 window hide None
 show expression "#000" as fade with Dissolve(1.0)
 hide beatrice_v001
 hide nao_v002
 with Dissolve(0.2)
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 590)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 camera at sepia_shader
 pause 0.0
 hide fade with Dissolve(1.0)
 show beatrice_v001 sinken at mei_center
 with Dissolve(1.0)
 show beatrice_v001 sinken at active
 beatrice '……それにしても。……よくわからぬ魔法陣であるなぁ。……一\n体、何に使うのやら。'
 window hide None
 show expression "#000" as fade with Dissolve(1.0)
 hide beatrice_v001
 with Dissolve(0.2)
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 camera at reset_shader
 pause 0.0
 hide fade with Dissolve(1.0)
 with Dissolve(1.0)
 narrator '\u3000これで説明がつく。これは多分、本当の意味での魔法陣なんか\nじゃない。'
 narrator '\u3000この推理なら、……紗音さんが異常に思わず、そして、魅音さん\nと詩音さんも、あれを見てあまりショックを受けていなかった様子\nが説明できる……！'
 show beatrice_v001 normal at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao 'そこのところを、もう少し詳しく説明していただけませんか？'
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice 'うむ。……魔法陣の図形には、おおざっぱに言うと、エネルギーの\n流れや中心、渦などが記されているものなのだが……。'
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice '……この魔法陣は、外部から魔力を集めてるように見えつつ、素通\nりしておるし、このサークルに意味がまったくないし……。'
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao 'ベアトリーチェ卿と呼ばれる大魔女のあなたの目から見て、……\nまったく意味がない？'
 show beatrice_v001 normal_close at active
 show nao_v002 normal at inactive
 beatrice 'うむ。……これは魔法陣風の、よくわからぬ紛い物だ。'
 hide beatrice_v001
 hide nao_v002
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 dlanor '朗読役なので黙っていましたが、……魔法陣の周囲に記されている\n文字も、見たことのないものデス。'
 show dlanor_v001 normal at active
 dlanor '天界大法院では膨大な種類の言語を扱いますが、……こんなものは\n一度も見たことがないデス。'
 hide dlanor_v001
 with Dissolve(0.2)
 show beatrice_v001 normal_close at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show beatrice_v001 normal_close at inactive
 nao '結論から言うと、……子供騙しの、魔法陣風の何か、ってことね？'
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice 'うむ。'
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice 'しかし、この２つの魔法陣は、異なる人物が作ったのであろう？'
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice '渦巻と二重丸の違いはありつつも、明らかに双方とも、同じ魔法陣\nを描こうとしたことは明白だ。'
 show nao_v002 normal_close at active
 show beatrice_v001 normal at inactive
 nao 'つまり、この魔法陣風の落書きが、複数人によって共通認識になっ\nている可能性……。'
 show beatrice_v001 fuan at active
 show nao_v002 normal_close at inactive
 beatrice '……よ、よくわからぬぞ。もう少し噛み砕いてはくれぬか……。'
 show nao_v002 smile at active
 show beatrice_v001 fuan at inactive
 nao '今から言うことを、あなたの手番で発言してほしいの。それで、あ\nなたとあたしは、共に勝者になれる。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide beatrice_v001
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 odoroki_close at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 odoroki_close at chara_shake_transform,active
 erika '………くぅうううぅぅぅッ……、私はなんで……ッ、六軒島では\nいっつも負けンの……ッ……ッッ！！'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show dlanor_v001 normal at mei_left
 show beatrice_v001 normal at mei_right
 with Dissolve(0.5)
 show beatrice_v001 normal at active
 show dlanor_v001 normal at inactive
 beatrice 'ドラノール……。妾も素直に拝聴したい。妾の手番を、菜央に譲っ\nてやれぬか。'
 show dlanor_v001 normal at active
 show beatrice_v001 normal at inactive
 dlanor '貴女が望むのなら、構いマセン。'
 show dlanor_v001 normal at active
 show beatrice_v001 normal at inactive
 dlanor '菜央。私も聞きたいデス。……どうして紗音は、この魔法陣を見過\nごしたのデスカ。'
 hide dlanor_v001
 hide beatrice_v001
 with Dissolve(0.2)
 show erika_v001 odoroki_close at mei_right
 show nao_v002 smile at mei_left
 with Dissolve(0.5)
 show nao_v002 smile at active
 show erika_v001 odoroki_close at inactive
 nao 'ヱリカさん。探偵の情け、だったかしら。'
 show erika_v001 sinken at active
 show nao_v002 smile at inactive
 erika 'けっ。……負けです負けです、負けですよ……。'
 show nao_v002 normal at active
 show erika_v001 sinken at inactive
 nao '多分。この魔法陣は………、'