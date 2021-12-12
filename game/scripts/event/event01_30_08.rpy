label event01_30_08:
 play sound ['audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav'] fadeout 1.0
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2331.png' as bg
 with Dissolve(1.0)
 narrator '\u3000六軒島で過ごす最後の夜……。'
 narrator '\u3000最高のディナーを心から満喫して、胸もお腹も幸せでいっぱいに\nして眠れるはずだったんだ……。'
 Character('Gohda',ctc="ctcArrow", ctc_position="fixed") '食後のお飲み物ですが、コーヒー、紅茶、塩昆布茶の用意がござい\nますが、如何なさいますか？'
 show erika_v001 sinken at mei_center
 with Dissolve(0.5)
 show erika_v001 sinken at active
 erika '……………………。'
 hide erika_v001
 with Dissolve(0.2)
 show mion_v002 sinken at mei_center
 with Dissolve(0.5)
 show mion_v002 sinken at active
 mion '………………………。'
 hide mion_v002
 with Dissolve(0.2)
 show nao_v002 fuan at mei_left
 show shion_v002 smile at mei_right
 with Dissolve(0.5)
 show shion_v002 smile at active
 show nao_v002 fuan at inactive
 shion '……あ、私は紅茶、ホットで。'
 show nao_v002 smile at active
 show shion_v002 smile at inactive
 nao 'それ以外の人も、みんな温かい紅茶をお願いします。'
 hide nao_v002
 hide shion_v002
 with Dissolve(0.2)
 Character('Gohda',ctc="ctcArrow", ctc_position="fixed") 'か、畏まりました……。'
 narrator '\u3000この重い空気は、魅音さんがヱリカさんの自作自演を疑ったから\nに他ならない。'
 narrator '\u3000少なくとも、昨日の悪戯の犯人は、ほぼ間違いなくヱリカさん\nだ。'
 narrator '\u3000そしてヱリカさんも、自分が一番に疑われていることをすでに\n知っている。'
 show erika_v001 sinken at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show erika_v001 sinken at inactive
 nao 'だから……、自作自演して、自分は犯人ではないとアピール……す\nるかしら……。'
 show erika_v001 sinken at active
 show nao_v002 normal at inactive
 erika 'そんなことしないですッ。あの魔法陣は私じゃありませんッ！'
 show nao_v002 normal at active
 show erika_v001 sinken at inactive
 nao 'わかってるわ。……これがあなたの自作自演なのだとしたら、……\nあまりにセンスがないわ。'
 show erika_v001 sinken_close at active
 show nao_v002 normal at inactive
 erika '…………ふん。'
 show expression "#000" as fade with Dissolve(1.0)
 scene expression "#000"
 hide erika_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator '\u3000……その時、少しだけ辺りが薄暗くなった気がした。'
 stop sound
 scene expression "#000"
 play music 'audio/bgm/BGM_QUEST1_COLLAB2.wav'
 show expression 'images/bg/AdvBg_2190.png' as bg
 with Dissolve(1.0)
 narrator '\u3000え？\u3000……魅音さんと詩音さんが、……すぅっと、蜃気楼か何か\nのように消えていく。'
 narrator '\u3000ヱリカさんとあたしはそのまま。\n\u3000そして、魅音さんと詩音さんが消えた席に、………あの、夢の中\nの魔女たちの姿が……。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide fade with Dissolve(0.08333333333333333)
 show beatrice_v001 futeki at mei_center
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_610_ls_plosive.wav'
 show beatrice_v001 futeki at active
 beatrice 'ハァッピーバースデー！！！\u3000おめでとう自分！\u3000ありがとうみん\nな！\u3000妾は幸せ者であるぞー！！'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide beatrice_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_381_ls_gaya.wav'
 play audio 'audio/sfx/SE_525_applause.wav'
 narrator '\u3000パチパチパチパチ！！！\u3000姿の見えない大観衆が祝福してくれる\nかのような音が響き渡った。'
 show nao_v002 fuan at mei_left
 show beatrice_v001 futeki at mei_right
 with Dissolve(0.5)
 show beatrice_v001 futeki at active
 show nao_v002 fuan at inactive
 beatrice 'どうだぁ、菜央ォ？！\u3000今夜でお別れだぜぇ？\u3000２つ目の魔法陣も\n楽しんで行ってくれよぉ！'
 show nao_v002 fuan at active
 show beatrice_v001 futeki at inactive
 nao '……いつの間にか、あたしは夢の中なの……？'
 show nao_v002 normal at active
 show beatrice_v001 futeki at inactive
 nao 'まぁ、そこを悩んでも仕方がないわ。あたしがいて、\nヱリカさんがいてベアトリーチェがいて、ドラノールさんがいる。\nそれが全てだわ。'
 hide nao_v002
 hide beatrice_v001
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 dlanor 'つくづく頭の切り替えの早い方デス。……航海者に必要な、異郷へ\nの適応力に優れていマス。'
 hide dlanor_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_left
 show erika_v001 smile at mei_right
 with Dissolve(0.5)
 show erika_v001 smile at active
 show nao_v002 normal at inactive
 erika 'さぁ、菜央ちゃま？\u3000楽しみましょう！\u3000頑張れば、ベアトから\nご褒美が出るそうじゃないですか。'
 show nao_v002 fuan at active
 show erika_v001 smile at inactive
 nao 'あたし、昨夜の謎だって解けてないのよ……。今夜のだって……。'
 hide erika_v001
 show beatrice_v001 smile at mei_right
 with Dissolve(0.5)
 show beatrice_v001 smile at active
 show nao_v002 fuan at inactive
 beatrice 'まぁまぁ。昨日のは小手調べということでよい。'
 show beatrice_v001 smile at active
 show nao_v002 fuan at inactive
 beatrice '今夜の、ヱリカの部屋の魔法陣の謎を解けたなら、それで褒美をく\nれてやろうぞ。'
 hide nao_v002
 hide beatrice_v001
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 dlanor '頑張ってください、菜央。私も、もっとサポートすることにしマ\nス。'
 hide dlanor_v001
 with Dissolve(0.2)
 show beatrice_v001 smile at mei_right
 show nao_v002 fuan_close at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan_close at active
 show beatrice_v001 smile at inactive
 nao 'もうごめんよ、こんなゲーム。……と、言いたいところだけれど。'
 show beatrice_v001 futeki at active
 show nao_v002 fuan_close at inactive
 beatrice 'うむ！\u3000朝が訪れるまで、終わることはないのだぞ。くっくっく！'
 hide beatrice_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator '\u3000はぁ……。\n\u3000覚悟を決めよう。'
 narrator '\u3000少なくとも、昨日のやりとりで、あたしを酷い目に遭わせようと\nいう訳ではないことがわかった。'
 narrator '\u3000魔女とヱリカさんは胡散臭いが、このドラノールさんという人は\n信頼できる気がする……。'
 show dlanor_v001 normal at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show dlanor_v001 normal at inactive
 nao 'ドラノールさん。……あたしはどうして、魔女とこんなゲームを？'
 show nao_v002 normal at active
 show dlanor_v001 normal at inactive
 nao 'まさか、魔女の誕生日プレゼントの生贄にされる、……とか言わな\nいでよ？'
 show dlanor_v001 normal_close at active
 show nao_v002 normal at inactive
 dlanor 'この島と黄金郷の主であるベアトリーチェ卿は、魔女であるならば\n逃れ難い、ある病を患っているのデス。'
 show nao_v002 normal at active
 show dlanor_v001 normal_close at inactive
 nao '……ある病……？'
 hide dlanor_v001
 show beatrice_v001 futeki_close at mei_right
 with Dissolve(0.5)
 show beatrice_v001 futeki_close at active
 show nao_v002 normal at inactive
 beatrice '退屈の病だ。くっくっく！\u3000突いても焼いても死なぬ魔女も、退屈\nの海に呑み込まれれば、海の藻屑よ。'
 hide nao_v002
 hide beatrice_v001
 with Dissolve(0.2)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika 'その為、魔女たちは時折、手紙やカケラを送り合います。互いに新\nしい刺激と、物語を送り合い、互いに病から逃れる為に。'
 show erika_v001 normal_close at active
 erika 'まぁ、今回はそれが、ベアトリーチェの誕生日祝いという形を取っ\nている訳ですが。'
 hide erika_v001
 with Dissolve(0.2)
 show beatrice_v001 smile at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show beatrice_v001 smile at inactive
 nao '……なぜ、魅音さんや詩音さんじゃなくてあたしなの。'
 show beatrice_v001 smile at active
 show nao_v002 normal at inactive
 beatrice 'それはほら、アレだ！\u3000そなたが一番、妾と馬が合ったからよ。'
 hide beatrice_v001
 hide nao_v002
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 dlanor 'それに他意はありマセン。私が保証しマス。'
 hide dlanor_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao 'じゃあ、あたしと魔女のゲームとやらで知恵比べをして、退屈を忘\nれる為に遊びたかったという訳？'
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show nao_v002 normal at inactive
 erika 'そういうことになりますね。魔女というのは、えてして孤独な生き\n物ですので。'
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 show beatrice_v001 normal_close at mei_center
 with Dissolve(0.5)
 show beatrice_v001 normal_close at active
 beatrice 'さりとて、慎ましく、遊んで下さいなとも頼めないのが、魔女の不\n器用さというものよ。'
 show beatrice_v001 smile at active
 beatrice '妾は、そなたとのゲームを大変に楽しんでいる。それで妾は十分に\n癒され、幸せになれた。'
 hide beatrice_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show nao_v002 normal at inactive
 erika '寛大なことに。勝敗は特に気にしていないのです。ゲームだけで十\n分に楽しかったのだそうです。'
 show nao_v002 normal at active
 show erika_v001 normal at inactive
 nao 'あたしが負けると魂が取られるとか、何かの企み事を密かに進めて\nいるとか、そういうのじゃないのね……？'
 hide erika_v001
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show nao_v002 normal at inactive
 dlanor 'そのようなことはありマセン。天界大法院の一等大司教、このドラ\nノール・Ａ・ノックスが保証しマス。'
 show nao_v002 normal_close at active
 show dlanor_v001 normal at inactive
 nao '………………………。'
 stop music fadeout 2.0
 hide nao_v002
 hide dlanor_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao 'わかったわ。そういうことならば、'
 play music 'audio/bgm/BGM_TITLE_COLLAB2.wav'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show nao_v002 smile at active
 nao 'お誕生日おめでとう。ミズ・ベアトリーチェ。'
 show nao_v002 normal at active
 nao 'お相手を謹んで引き受けるわ。……ただね、あたし、'
 hide nao_v002
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_5001_sitdown2.wav'
 narrator '\u3000あたしはちょっぴり行儀悪く、座ったまま椅子を引き、大きく足\nを組む。'
 narrator '\u3000ディナーの席では行儀よくだけれど。……退屈凌ぎのゲームとは\nいえ、勝負事だもの。'
 show nao_v002 sinken at mei_center
 with Dissolve(0.5)
 show nao_v002 sinken at active
 nao 'ものすごく負けず嫌いなの。あたしは、勝っても負けても楽しかっ\nたなんて言わないわ。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika 'グッド。やはり貴女は、私の期待を裏切りませんね。'
 show erika_v001 normal at active
 erika 'フェリーでお見掛けした時に感じた、私の直感は当たっていまし\nた。'
 hide erika_v001
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_left
 show beatrice_v001 futeki at mei_right
 with Dissolve(0.5)
 show beatrice_v001 futeki at active
 show dlanor_v001 normal at inactive
 beatrice '嬉しいぞ、菜央ォ！\u3000お前は本当にいいヤツだなぁ！\u3000さぁ、今宵\nは存分に楽しもう！！'
 show dlanor_v001 normal at active
 show beatrice_v001 futeki at inactive
 dlanor '菜央。……改めまして、状況を説明いたしマス。'
 show dlanor_v001 normal at active
 show beatrice_v001 futeki at inactive
 dlanor 'ヱリカの部屋に現れた、魔法陣の悪戯……。'
 show beatrice_v001 futeki at active
 show dlanor_v001 normal at inactive
 beatrice '妾はそれを、人間には不可能であるとして、魔女の仕業であると主\n張する！'
 hide dlanor_v001
 show nao_v002 sinken at mei_left
 with Dissolve(0.5)
 show nao_v002 sinken at active
 show beatrice_v001 futeki at inactive
 nao 'あたしは人間に可能な悪戯だと主張するわ。そして、犯人はヱリカ\nさんだと主張するわ！'
 hide beatrice_v001
 show erika_v001 futeki at mei_right
 with Dissolve(0.5)
 show erika_v001 futeki at active
 show nao_v002 sinken at inactive
 erika 'ふふッ、グッド。存分に掛かってきて下さいな。'
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 dlanor 'そして、ヱリカもまた、プレイヤーデス。'
 hide dlanor_v001
 with Dissolve(0.2)
 show beatrice_v001 futeki at mei_right
 show nao_v002 odoroki at mei_left
 with Dissolve(0.5)
 show nao_v002 odoroki at active
 show beatrice_v001 futeki at inactive
 nao 'どういうこと？\u3000あたしと魔女の、二人の戦いじゃないの？'
 show beatrice_v001 futeki at active
 show nao_v002 odoroki at inactive
 beatrice '今宵はひとつ、三つ巴の戦いと行こうではないか！\u3000妾も楽しみで\nあるぞ！'
 hide beatrice_v001
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show nao_v002 odoroki at inactive
 erika '私も菜央ちゃまと同じく、ニンゲンに可能な悪戯だと主張します。'
 show nao_v002 normal at active
 show erika_v001 normal at inactive
 nao '共闘？'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide nao_v002
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 futeki at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 futeki at active
 erika '違います。私は犯人を、詩音さんだと主張しますッ。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 narrator '\u3000なるほど。３人が全員、異なる主張をする。'
 camera at screenshake_transform
 pause 0.0
 narrator '\u3000今夜の魔法陣は、魔女の仕業か、ヱリカさんの自作自演か、さも\nなくば詩音さんの犯行か！'
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 dlanor 'それでは、今宵の朗読者は私が担当させていただきマス。'
 show dlanor_v001 normal at active
 dlanor 'それでは御三方。状況を説明いたしマス。\n御拝聴をよろしくお願い致しマス……。'
 stop music fadeout 2.0
 show expression "#000" as fade with Dissolve(1.0)
 hide dlanor_v001
 with Dissolve(0.2)
 stop sound
 scene expression "#000"
 play music 'audio/bgm/BGM_QUEST3_COLLAB2.wav'
 show expression 'images/bg/AdvBg_2371.png' as bg
 with Dissolve(1.0)
 pause 2.0
 stop sound
 
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 dlanor '今回の魔法陣は、ヱリカの客室で見つかりマシタ。'
 show dlanor_v001 normal at active
 dlanor '帰ってきたヱリカが、開錠して入室した後に、荒らされたベッドを\n発見。シーツに魔法陣があるのを発見しマシタ。'
 hide dlanor_v001
 with Dissolve(0.2)
 narrator '\u3000……まず、ここにひとつ、確認したいことがあるけれど、今は大\n人しく耳を傾けよう。'
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 dlanor 'ヱリカは本日、昼にゲストハウスに戻るまで、部屋の施錠を忘れて\nおりマシタ。'
 show dlanor_v001 normal at active
 dlanor 'よって、昼に施錠するまでの間は、誰でも入室が可能デシタ。'
 hide dlanor_v001
 with Dissolve(0.2)
 narrator '\u3000ここが肝。……ポイントは、昨夜の魔法陣と同じ。\n\u3000ヱリカさんは、室内に異常がないことを確認した上で施錠してい\nる。'
 narrator '\u3000普通に考えれば、犯行はこれ以降となるのだが、……施錠は完全\nな密室になってしまうのだ。'
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show expression "#e11" as fade with Dissolve(0.16666666666666666)
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 scene expression 'images/bg/AdvBg_2281.png' as bg
 with Dissolve(0.16666666666666666)
 show dlanor_v001 normal at active
 dlanor '#ff0000施錠後は、ヱリカが開錠するまで、室内は完全な密室デス。#r'
 show expression "#e11" as fade with Dissolve(0.16666666666666666)
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 hide fade with Dissolve(0.16666666666666666)
 with Dissolve(0.16666666666666666)
 show dlanor_v001 normal at active
 dlanor '#ff0000室内には誰も存在せず、また、仕掛けの類も存在しませんデシタ。#r'
 show expression "#e11" as fade with Dissolve(0.16666666666666666)
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 hide fade with Dissolve(0.16666666666666666)
 with Dissolve(0.16666666666666666)
 show dlanor_v001 normal at active
 dlanor '#ff0000魔法陣の悪戯は、入室した人物の手によってでしか、行なうことは#r\n#ff0000出来マセン。#r'
 show dlanor_v001 normal_close at active
 dlanor 'とりあえずは以上になりマス。……皆様、どうぞご考察ヲ……。'
 hide dlanor_v001
 with Dissolve(0.2)
 narrator '\u3000３人のプレイヤーのそれぞれに相手の表情を伺い合う。'
 narrator '\u3000皆、今さら考えるような段階にはないらしい。\n……ドラノールさんに質問や青き真実を投げ掛けたくて\nうずうずしている……。'
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 dlanor 'それでは、スタートプレイヤーには、ベアトリーチェ卿の誕生日を\n祝って、ベアトリーチェ卿を指名させていただきマス。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide dlanor_v001
 hide fade with Dissolve(0.08333333333333333)
 show beatrice_v001 futeki at mei_center
 with Dissolve(0.08333333333333333)
 show beatrice_v001 futeki at active
 beatrice 'ハピバ！\u3000妾！！\u3000それでは……、参ろうぞっ。'
 show beatrice_v001 normal at active
 beatrice '帰ったヱリカは施錠を開けて入室したが、菜央たちがヱリカの悲鳴\nを聞くには、少しの間があったはず。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide beatrice_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika 'そうですね。鍵穴にゴミが詰まってないか、確認してから入室しま\nしたので、多少は。'
 hide erika_v001
 with Dissolve(0.2)
 narrator '\u3000……ベアトリーチェが、どうしてそこに切り込むの？\n\u3000ヱリカさんの自作自演を疑うあたしが、そこを突いて追及しよう\nと思っていたのに……。'
 show dlanor_v001 normal at mei_left
 show beatrice_v001 normal at mei_right
 with Dissolve(0.5)
 show beatrice_v001 normal at active
 show dlanor_v001 normal at inactive
 beatrice 'まずは菜央の希望を絶とう。ドラノールよ。復唱要求。'
 show beatrice_v001 normal at active
 show dlanor_v001 normal at inactive
 beatrice '“ヱリカが入室してから悲鳴を聞いて菜央たちがやってくるまでの\n間に、魔法陣の悪戯をすることは時間的に不可能である”。'
 show dlanor_v001 normal at active
 show beatrice_v001 normal at inactive
 dlanor 'お受けしマス。'
 show expression "#e11" as fade with Dissolve(0.16666666666666666)
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 hide fade with Dissolve(0.16666666666666666)
 with Dissolve(0.16666666666666666)
 show dlanor_v001 normal at active
 show beatrice_v001 normal at inactive
 dlanor '#ff0000ヱリカが入室してから悲鳴を聞いて菜央たちがやってくるまでの間#r\n#ff0000に、魔法陣の悪戯をすることは時間的に不可能デス。#r'
 hide dlanor_v001
 hide beatrice_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao 'えっと、それって、ヱリカさん以外の人も含めてます？'
 hide nao_v002
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 dlanor 'ハイ。'
 show expression "#e11" as fade with Dissolve(0.16666666666666666)
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 hide fade with Dissolve(0.16666666666666666)
 with Dissolve(0.16666666666666666)
 show dlanor_v001 normal at active
 dlanor '#ff0000ヱリカが入室してからでは、如何なる方法を用いようとも、#r\n#ff0000魔法陣の悪戯をすることは出来マセン。#r'
 hide dlanor_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show nao_v002 normal at inactive
 erika '私の濡れ衣を晴らしてくれてありがとうございます。ね？\u3000自作自\n演ではないでしょう？\u3000時間が足りないんです。'
 show nao_v002 normal_close at active
 show erika_v001 normal at inactive
 nao '……まずいわ。これでまた、あたしのベッドの時と同じに……。'
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 narrator '\u3000これでヱリカさんの部屋に魔法陣を仕掛けるには、ヱリカさんが\n施錠する以前にしか不可能……。'
 narrator '\u3000昨日と同じだ。紗音さんが窓を施錠する以前にしか、魔法陣を仕\n掛けられないのと同じ。'
 narrator '\u3000しかし、どちらも、入室者が異常がないことを確認してい\nる……。'
 show beatrice_v001 futeki at mei_center
 with Dissolve(0.5)
 show beatrice_v001 futeki at active
 beatrice 'これで妾の手番を終わるぞ。くっくっく。'
 hide beatrice_v001
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 dlanor 'それでは、古式に則り時計回りで進行いたしマス。'
 show dlanor_v001 normal at active
 dlanor '次はヱリカの手番デス。'
 show erika_v001 normal_close at mei_right
 with Dissolve(0.5)
 show erika_v001 normal_close at active
 show dlanor_v001 normal at inactive
 erika 'それでは。コホン。'
 show erika_v001 normal at active
 show dlanor_v001 normal at inactive
 erika '争点が３つもあると、ややこしくてかないません。なので、手っ取\nり早く、菜央さんに脱落してもらおうと思います。'
 hide dlanor_v001
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show erika_v001 normal at inactive
 nao '……だろうと思ったわ。あたしがあなたでも、同じことをしたわ。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide erika_v001
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 normal at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 normal at active
 erika 'くすくすくす。……それでは私からは、昨日と今日の、２つの魔法\n陣の違いについて話をしようと思います。'
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
 beatrice 'ほう？\u3000違い、とな？'
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao '……２つとも同じ魔法陣を描いたものに思えたけど…………。'
 show expression "#000" as fade with Dissolve(1.0)
 hide nao_v002
 hide beatrice_v001
 with Dissolve(0.2)
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2320.png' as bg
 with Dissolve(1.0)
 dlanor 'こちらが、第一の魔法陣。そして、こちらが第二の魔法陣デス。ご\n確認ヲ。'
 beatrice '………ふーむ……？\u3000何が違うのか？'
 show expression "#000" as fade with Dissolve(1.0)
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2281.png' as bg
 with Dissolve(1.0)
 show erika_v001 normal at mei_right
 show nao_v002 sinken at mei_left
 with Dissolve(0.5)
 show nao_v002 sinken at jump_transform,active
 show erika_v001 normal at inactive
 nao '………あ、………ここ！'
 show erika_v001 normal at active
 show nao_v002 sinken at inactive
 erika 'グッド。菜央ちゃまがこれに気付くとは。その上、なかなか素早い\nです。'
 hide erika_v001
 hide nao_v002
 with Dissolve(0.2)
 show beatrice_v001 fuan at mei_center
 with Dissolve(0.5)
 show beatrice_v001 fuan at active
 beatrice 'え？\u3000何？\u3000……間違い探し？？？'
 hide beatrice_v001
 with Dissolve(0.2)
 show erika_v001 normal at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show erika_v001 normal at inactive
 nao 'あたし、見たものを記憶するのは得意なんです。'
 show erika_v001 normal at active
 show nao_v002 normal at inactive
 erika '写真記憶。……探偵には必須の能力です。'
 show nao_v002 normal_close at active
 show erika_v001 normal at inactive
 nao '昨日はショックで冷静じゃなかったし、今日も同じ魔法陣と思い込\nんでいたから気付き損ねたけど……。'
 show nao_v002 normal at active
 show erika_v001 normal at inactive
 nao 'ほら。魔法陣を丸く囲むように描かれた、……魔法文字？\u3000が、こ\nの１文字だけ違うわ。'
 hide erika_v001
 show beatrice_v001 sinken at mei_right
 with Dissolve(0.5)
 show beatrice_v001 sinken at active
 show nao_v002 normal at inactive
 beatrice 'むむ。確かに。……こっちは渦のような文字だが、こっちでは二重\n丸のような文字になっておるぞ？'
 show nao_v002 smile at active
 show beatrice_v001 sinken at inactive
 nao 'そういうこと。ここだけなら、書き間違いを疑うところだけれど。\nこの魔法陣に同じ文字は３ヶ所登場するわ。'
 show beatrice_v001 sinken at active
 show nao_v002 smile at inactive
 beatrice '３ヶ所とも、こっちは渦、こっちは二重丸になっておるぞ！\u3000……\nこれは一体？！'
 hide nao_v002
 hide beatrice_v001
 with Dissolve(0.2)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika 'より細かく観察すれば、他には小さな差異をいくつも発見すること\nが出来ます。'
 show expression "#000" as fade with Dissolve(1.0)
 hide erika_v001
 with Dissolve(0.2)
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2190.png' as bg
 with Dissolve(1.0)
 show dlanor_v001 normal at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show dlanor_v001 normal at inactive
 erika 'これらの手掛かりを総合した上で、ドラノールに復唱要求を求めま\nす。'
 show dlanor_v001 normal at active
 show erika_v001 normal at inactive
 dlanor 'どうぞ、ヱリカ。'
 hide dlanor_v001
 hide erika_v001
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_204_shot.wav'
 show expression "#fff" as flash with Dissolve(0.1)
 pause 0.1
 hide flash with Dissolve(0.2)
 narrator '\u3000復唱要求。“２枚のシーツに描かれた魔法陣は、それぞれ違う製\n作者によるものである”'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide fade with Dissolve(0.08333333333333333)
 show nao_v002 sinken at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show nao_v002 sinken at active
 nao '………？！？！'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show erika_v001 normal at mei_left
 show beatrice_v001 normal at mei_right
 with Dissolve(0.5)
 show beatrice_v001 normal at active
 show erika_v001 normal at inactive
 beatrice 'なるほど……。自作自演ではないことを完全に証明したい訳か。'
 show beatrice_v001 normal at active
 show erika_v001 normal at inactive
 beatrice 'しかし、だとすると……、認める必要が生じるぞ……？'
 show erika_v001 normal at active
 show beatrice_v001 normal at inactive
 erika 'ふふ。私はそういうのは、何も気にしませんので。'
 show erika_v001 normal at active
 show beatrice_v001 normal at inactive
 erika 'それで、ドラノール？\u3000復唱要求は応じられるのですか？'
 hide erika_v001
 hide beatrice_v001
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 dlanor '……ハイ。お待たせしマシタ。応じられマス。'
 play sound ['audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav'] fadeout 1.0
 show expression "#e11" as fade with Dissolve(0.16666666666666666)
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 hide fade with Dissolve(0.16666666666666666)
 with Dissolve(0.16666666666666666)
 show dlanor_v001 normal at active
 dlanor '#ff0000２枚のシーツに描かれた魔法陣は、それぞれ違う製作者によるもの#r\n#ff0000デス。#r'
 hide dlanor_v001
 with Dissolve(0.2)
 show erika_v001 normal_close at mei_center
 with Dissolve(0.5)
 show erika_v001 normal_close at active
 erika 'その上でＣＯします。'
 hide erika_v001
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_right
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at active
 show dlanor_v001 normal at inactive
 nao 'ＣＯって？'
 show dlanor_v001 normal at active
 show nao_v002 fuan at inactive
 dlanor 'カミングアウト。自分しか知り得ない情報の開示、告白デス。'
 hide dlanor_v001
 hide nao_v002
 with Dissolve(0.2)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika '第一の魔法陣の製作者は、私、古戸ヱリカです。'
 hide erika_v001
 with Dissolve(0.2)
 show erika_v001 normal at mei_right
 show nao_v002 sinken at mei_left
 with Dissolve(0.5)
 camera at screenshake_transform
 pause 0.0
 show nao_v002 sinken at active
 show erika_v001 normal at inactive
 nao 'ほら、やっぱりあなたが犯人だったじゃない！！'
 show erika_v001 normal at active
 show nao_v002 sinken at inactive
 erika 'まぁまぁ。ただの悪戯じゃないですか。それに、今回のゲーム以外\nの私怨を持ち込むのはノーマナーですよ？'
 hide nao_v002
 show beatrice_v001 normal at mei_left
 with Dissolve(0.5)
 show beatrice_v001 normal at active
 show erika_v001 normal at inactive
 beatrice '第一の魔法陣が、ヱリカが犯人なのは百も承知。だが、だとすると\n紗音がどうして魔法陣に気付かなかったのか、謎が残るぞ？'
 show beatrice_v001 normal at active
 show erika_v001 normal at inactive
 beatrice 'ヱリカが魔女を否定するならば、ヱリカがどのようにして紗音を欺\nいたかの提示が必要であるぞ。'
 show erika_v001 normal_close at active
 show beatrice_v001 normal at inactive
 erika 'それはいずれ、青き真実の形で提示いたしますので。……私の手番\nは以上です。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide erika_v001
 hide beatrice_v001
 hide fade with Dissolve(0.08333333333333333)
 show beatrice_v001 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show beatrice_v001 sinken at active
 beatrice '……それにしても。……よくわからぬ魔法陣であるなぁ。……一\n体、何に使うのやら。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide beatrice_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao '…………………？'
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show nao_v002 normal at inactive
 dlanor 'それではお待たせしマシタ。菜央の手番デス。'
 stop music fadeout 2.0
 show nao_v002 normal_close at active
 show dlanor_v001 normal at inactive
 nao '………………………。'
 hide nao_v002
 hide dlanor_v001
 with Dissolve(0.2)
 narrator '\u3000あたしの頭の中で、思考のドロドロスープが掻き回されて渦を作\nる。'
 narrator '\u3000……なかなか火が通らなかった具材が……、ようやく煮え始めて\n来たのを感じる……。\n\u3000ひょっとして…………。'
 show dlanor_v001 normal at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show dlanor_v001 normal at inactive
 nao '……ドラノールさん。確認が。'
 show dlanor_v001 normal at active
 show nao_v002 normal at inactive
 dlanor '伺いマス。'
 play music 'audio/bgm/BGM_QUEST7_COLLAB2.wav'
 show nao_v002 normal at active
 show dlanor_v001 normal at inactive
 nao 'さっきヱリカさんがＣＯして、第一の魔法陣の製作者は自分だと告\n白したわ。'
 show nao_v002 normal at active
 show dlanor_v001 normal at inactive
 nao 'あれは赤き真実と同等の告白なのかしら？'
 hide dlanor_v001
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show nao_v002 normal at inactive
 erika 'いいえ。赤き真実ではありませんから、偽りが含まれている可能性\nもあります。'
 show nao_v002 normal at active
 show erika_v001 normal at inactive
 nao 'えっと、それをヱリカさんに対し、復唱要求することは出来るの？'
 show erika_v001 normal at nod_transform,active
 show nao_v002 normal at inactive
 erika 'えぇ、可能ですよ？\u3000もちろん、お受けさせていただきます。'
 show nao_v002 normal at active
 show erika_v001 normal at inactive
 nao 'ならお願いするわ。復唱を要求。'
 show expression "#fff" as flash with Dissolve(0.1)
 pause 0.1
 hide flash with Dissolve(0.2)
 show nao_v002 normal at active
 show erika_v001 normal at inactive
 nao '“第一の魔法陣の製作者であり、それを設置したのはヱリカさんで\nある”。'
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 narrator '\u3000………ヱリカさんの目が、一瞬だけ逡巡した。\n\u3000どう答えれば、よりあたしを煙に巻けるか、思案している……。'
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika '応じます。'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show expression "#e11" as fade with Dissolve(0.16666666666666666)
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 hide fade with Dissolve(0.16666666666666666)
 with Dissolve(0.16666666666666666)
 show erika_v001 normal at active
 erika '#ff0000第一の魔法陣の製作者であり、それを設置したのは古戸ヱリカであ#r\n#ff0000る。#r'
 show erika_v001 normal at active
 erika 'ただし。いつ、どうやって設置し、紗音さんをどうやって欺いたか\nについては、答える気はありませんのでご容赦を。'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 hide erika_v001
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 dlanor '菜央の手番は以上になりマス。次はベアトリーチェ卿の手番デス。'
 hide dlanor_v001
 with Dissolve(0.2)
 narrator '\u3000……貴重な手番を、ほぼほぼ確信している内容を確定させる為だ\nけに使用してしまった。'
 narrator '\u3000あたしの敵は、魔女とヱリカさんの２人なの？\u3000……三つ巴の戦い\nは、相手方に組まれたら勝ち目はない。'
 show dlanor_v001 normal at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show dlanor_v001 normal at inactive
 nao '……ドラノールさん。ルールについて、また教えて下さい。'
 show nao_v002 normal at active
 show dlanor_v001 normal at inactive
 nao '今回の三つ巴の戦い。……勝者はひとりだけなんですか？'
 show dlanor_v001 normal at active
 show nao_v002 normal at inactive
 dlanor '２人が勝者になることもあり得マス。'
 show nao_v002 smile at active
 show dlanor_v001 normal at inactive
 nao '…………ありがとう。次はベアトリーチェね。'
 show nao_v002 normal at active
 show dlanor_v001 normal at inactive
 nao 'また、あたしを追い詰めてくるのかしら……？'
 hide dlanor_v001
 show beatrice_v001 smile at mei_right
 with Dissolve(0.5)
 show beatrice_v001 smile at active
 show nao_v002 normal at inactive
 beatrice '妾は勝ち負けでなく、ゲームそのものを楽しんでおる。よって、戦\nいは公平に行なうつもりでいる。'
 show beatrice_v001 smile at active
 show nao_v002 normal at inactive
 beatrice 'なので、先程は菜央を攻めた。次はヱリカを攻めさせてもらおう\nぞ。'
 hide nao_v002
 show erika_v001 normal at mei_left
 with Dissolve(0.5)
 show erika_v001 normal at active
 show beatrice_v001 smile at inactive
 erika 'どうぞ、ご自由に。'
 hide beatrice_v001
 hide erika_v001
 with Dissolve(0.2)
 narrator '\u3000……ヱリカさんは恐らく、確実にあたし狙いだ。\n\u3000自身の勝利は当然として、それ以上に、あたしを負けさせたいの\nだ。'
 narrator '\u3000だが、ベアトリーチェに、そういう悪意はまったくない。\n\u3000公平に戦うと言っている。……もちろんゲームの展開上、勝ちが\n見えたら畳みかけてくることもあるだろう。'
 narrator '\u3000……なら。あたしとヱリカさんがまだ均衡している内に、……ベ\nアトリーチェを、あたし側に引き込みたい……。'
 narrator '\u3000あたしの勝利条件は、ヱリカさんが行なった自作自演であること\nを証明すること。'
 narrator '\u3000ベアトリーチェの勝利条件は、人間には不可能な悪戯であること\nを証明すること。\n\u3000……………………。'
 show dlanor_v001 normal at mei_right
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at active
 show dlanor_v001 normal at inactive
 nao '……ドラノールさん、何度もすみません。もうひとつ確認が……。'
 show dlanor_v001 normal at active
 show nao_v002 fuan at inactive
 dlanor 'お気になさらズニ。どうぞ何でも聞いて下サイ。'
 show nao_v002 fuan at active
 show dlanor_v001 normal at inactive
 nao 'あの、……その。'
 hide dlanor_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator '\u3000あたしが、気まずそうな様子と、内緒話を意味する仕草を見せる\nと、ドラノールさんはすぐに理解してくれた。'
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 dlanor 'ウィスパーですね。問題ありマセン。'
 hide dlanor_v001
 with Dissolve(0.2)
 narrator '\u3000どんなゲームでも、時に、あるルールの確認行為そのものが、自\n分の手の内を明かしてしまうことがある。'
 narrator '\u3000特に、ヱリカさんに聞かれる訳にはいかないのだ……。'
 show erika_v001 normal at mei_left
 show beatrice_v001 smile at mei_right
 with Dissolve(0.5)
 show beatrice_v001 smile at active
 show erika_v001 normal at inactive
 beatrice 'ふむふむ。何の相談であろうな？'
 show erika_v001 normal at active
 show beatrice_v001 smile at inactive
 erika 'さぁ。……でも、初心者なんですから、私たちも胸を貸してあげな\nいといけません。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide erika_v001
 hide beatrice_v001
 hide fade with Dissolve(0.08333333333333333)
 show dlanor_v001 normal_close at mei_center
 with Dissolve(0.08333333333333333)
 show dlanor_v001 normal_close at active
 dlanor '……ふむフム。………なるホド。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide dlanor_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 narrator '\u3000ドラノールさんと顔を寄せ合って、小声で話し合う。'
 narrator '\u3000……いい匂い。今まで嗅いだことのない香りだ。……彼女の髪に\n鼻を押し付けて、スーハーしたくなるわ……。'
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika 'ドラノールって、生意気にすっごくいい匂いがするんですよねぇ。'
 show erika_v001 smile at active
 erika '私、鼻がいいんで、ドラノールの気配は匂いでわかります。うふふ\nふ。'
 hide erika_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_left
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show nao_v002 normal at inactive
 dlanor '……菜央。問題ありマセン。'
 show dlanor_v001 normal at active
 show nao_v002 normal at inactive
 dlanor '第一の魔法陣がニンゲンの仕業であると証明し、しかし第二の魔法\n陣がニンゲンには不可能であると証明できたナラ……。'
 show nao_v002 normal at active
 show dlanor_v001 normal at inactive
 nao 'あたしとベアトリーチェは、共に勝者になれる……。'
 show dlanor_v001 normal at active
 show nao_v002 normal at inactive
 dlanor 'ただ、ウィスパーは朗読者である私にしか出来マセン。'
 show dlanor_v001 normal at active
 show nao_v002 normal at inactive
 dlanor 'ベアトリーチェ卿に共闘を申し出ることは自由ですが、ヱリカの耳\nにも入ることを忘れないで下サイ。'
 hide nao_v002
 hide dlanor_v001
 with Dissolve(0.2)
 narrator '\u3000よし、グッド。…………でしたっけ？'
 narrator '\u3000ヱリカさん。あたし、負けず嫌いよ。\n\u3000絶対に勝つ。そして、魔法陣の２つの密室も暴いてみせる。'
 narrator '\u3000ヱリカさん。あなたに習ったわ。\n\u3000この、格闘的知恵比べは、……結局は殴り合いも同然。'
 narrator '\u3000あらゆる主張や推理、証拠で、徹底的に相手を打ちのめし\nて、……ダウンさせた方が勝者となる。'
 camera at screenshake_transform
 pause 0.0
 narrator '\u3000あたしは勝つ。そして、あなたを負かす！'
 show erika_v001 normal at mei_right
 show nao_v002 sinken at mei_left
 with Dissolve(0.5)
 show nao_v002 sinken at active
 show erika_v001 normal at inactive
 nao '……………………。'
 show erika_v001 futeki at active
 show nao_v002 sinken at inactive
 erika '……グッド。'