label chara452001_01:
 show black_background onlayer black
 stop sound
 scene expression "#000"
 play music 'audio/bgm/BGM_EVENT_TOP_COLLAB2.wav'
 show expression 'images/bg/AdvBg_2190.png' as bg
 with Dissolve(1.0)
 show nao_v002 fuan at mei_right
 show beatrice_v001 smile at mei_left
 with Dissolve(0.5)
 show beatrice_v001 smile at active
 show nao_v002 fuan at inactive
 beatrice '遠慮はいらぬ。\nさぁ、そなたも冷めないうちに飲むといい。'
 show nao_v002 fuan at active
 show beatrice_v001 smile at inactive
 nao 'あの……えっと、これは……？'
 show beatrice_v001 normal at active
 show nao_v002 fuan at inactive
 beatrice 'ん……どうした、紅茶は嫌いか？\nなら、このクッキーはどうだ？\nロノウェが自信作と言っていたぞ。'
 show nao_v002 fuan at active
 show beatrice_v001 normal at inactive
 nao 'いや、紅茶は好きだけど\nそういうことじゃなくて……その……。'
 show nao_v002 normal_close at active
 show beatrice_v001 normal at inactive
 nao '（……。断るのも失礼だから、\n素直にいただいたほうがよさそうね……）'
 play audio 'audio/sfx/SE_5049_cup.wav'
 show nao_v002 smile at active
 show beatrice_v001 normal at inactive
 nao 'じゃあ、いただきます……って、\nほわぁ……おいしい……！'
 play audio 'audio/sfx/SE_215_heartgrow.wav'
 show nao_v002 smile_blush at jumping_transform,active
 show beatrice_v001 normal at inactive
 nao '香りも上品で素敵だけど、\n渋みが全然なくて少し甘いくらい……♪'
 show beatrice_v001 smile at active
 show nao_v002 smile_blush at inactive
 beatrice 'そうであろう、そうであろう？\n実は妾も最近この紅茶がお気に入りでなぁ！'
 show beatrice_v001 smile_close at active
 show nao_v002 smile_blush at inactive
 beatrice 'マイブームと言うやつよ。'
 show nao_v002 fuan at active
 show beatrice_v001 smile_close at inactive
 nao 'あ……でも紅茶ってカフェインが\nコーヒー以上に入ってるはずだから、\n飲みすぎると夜眠れなくなりそう？'
 show beatrice_v001 smile at active
 show nao_v002 fuan at inactive
 beatrice 'くっくっくっ、まったくニンゲンとは繊細なものだ。'
 show nao_v002 smile at active
 show beatrice_v001 smile at inactive
 nao '（ふふっ。あの推理バトルの時は\n威厳と怖さを兼ね備えたすごい魔女だったけど、\n案外親しみやすいところがあるのかも……かも）'
 show beatrice_v001 smile at active
 show nao_v002 smile at inactive
 beatrice 'あと、この紅茶は茶菓子を合間に食べると\n香りがより引き立つ。\nそこのスコーンなどは、相性的にもおすすめだ。'
 show nao_v002 smile at active
 show beatrice_v001 smile at inactive
 nao 'あ……ほんとだ。\nそれに、この味わいだったらジャムとかを\n入れてみてもいいかもね。'
 show beatrice_v001 smile at nod_transform,active
 show nao_v002 smile at inactive
 beatrice 'もちろん、ロシアンティにも合うぞ。\n次は試すが良い。'
 hide nao_v002
 hide beatrice_v001
 with Dissolve(0.2)
 narrator '…………。'
 show expression "#000" as fade with Dissolve(1.0)
 pause 1.0
 hide fade with Dissolve(1.0)
 with Dissolve(1.0)
 show beatrice_v001 smile at mei_left
 show nao_v002 normal at mei_right
 with Dissolve(0.5)
 show nao_v002 normal at active
 show beatrice_v001 smile at inactive
 nao '……ところで、ベアトリーチェ。\n今日あたしをここにまた呼び出したのは、\nどういうご用件なの？'
 show beatrice_v001 smile at active
 show nao_v002 normal at inactive
 beatrice 'どうも何もない、そなたと茶を飲みたいと思っただけだ。'
 show nao_v002 fuan at active
 show beatrice_v001 smile at inactive
 nao '……それだけ？'
 show beatrice_v001 normal at active
 show nao_v002 fuan at inactive
 beatrice 'それだけだが……何の問題があるというのだ？'
 show nao_v002 smile at active
 show beatrice_v001 normal at inactive
 nao 'ううん。おいしい紅茶が飲めるのは、\n単純に嬉しいからあたしは嬉しいわ。'
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao '（……どうしたのかしら。\nあの魔女ベアトリーチェが、\nただお茶を飲むだけのためにあたしを呼んだ？）'
 show nao_v002 sinken at active
 show beatrice_v001 normal at inactive
 nao '（ちょっと考えにくいわね。\n何か企んでいるのかも……かも）'
 show beatrice_v001 normal_close at active
 show nao_v002 sinken at inactive
 beatrice '……そなたの考えていること、妾にはわかるぞ。'
 show nao_v002 odoroki at jump_transform,active
 show beatrice_v001 normal_close at inactive
 nao 'えっ……？'
 show beatrice_v001 normal at active
 show nao_v002 odoroki at inactive
 beatrice '本来交わることのなかったそなたが\nここに呼ばれ、こうして妾と茶を交わす。\nそれに奇異を感じているのであろう？'
 show nao_v002 normal at nod_transform,active
 show beatrice_v001 normal at inactive
 nao '……えぇ。正直言って身構えてるわ。\nいつあたしの尻子玉を抜こうとしてくるのか、って。'
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
 beatrice 'ぷっ……くっくくははははははっ！\nよりにもよって喩えが尻子玉……とな？！'
 show beatrice_v001 futeki_close at active
 beatrice '河童でもあるまいし、妾がそのような真似を\nするはずがなかろうっ！\nくっくくくっくく！'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide beatrice_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao 'しないとは言えないでしょ？\nだってあたし、魔女に詳しくないもの。'
 show nao_v002 normal at active
 nao '尻子玉コレクションを趣味にしてる\n魔女がいるかも知れないじゃない。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 show beatrice_v001 futeki_close at mei_center
 with Dissolve(0.08333333333333333)
 show beatrice_v001 futeki_close at chara_shake_transform,active
 beatrice 'ひーっひひっひひひひひひひひ！！！\n面白いぞ、実に面白い！'
 show beatrice_v001 futeki_close at active
 beatrice '妾がこんな小娘にひぃひぃ言わせられるとはな……\nふっふふふふふふ、くーっくっくっく！'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide beatrice_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 nao '（すごい大爆笑してるわね。\nよっぽどツボだったのかしら？）'
 hide nao_v002
 with Dissolve(0.2)
 show beatrice_v001 smile_close at mei_left
 show nao_v002 fuan at mei_right
 with Dissolve(0.5)
 show beatrice_v001 smile_close at active
 show nao_v002 fuan at inactive
 beatrice 'くっくっくっく！くは、ははは……はぁ、ふぅ……ふー。\n笑わせてもらったぞ。\n妾に冗談で返せる度胸、なかなかやるではないか。'
 show nao_v002 normal at active
 show beatrice_v001 smile_close at inactive
 nao 'あたしもよ。\nまさか、ここまで笑ってもらえるなんて\nさすがに思わなかったわ。'
 show nao_v002 normal at active
 show beatrice_v001 smile_close at inactive
 nao '今思ったことだけど……魔女って感情豊かなのね。'
 show beatrice_v001 smile at active
 show nao_v002 normal at inactive
 beatrice '当然であろう。\n魔女も面白ければ笑い、馬鹿にされたなら報復もする。'
 show beatrice_v001 smile_close at active
 show nao_v002 normal at inactive
 beatrice 'まぁ、そなたが妾に恐怖を求めるというならば\nその期待に応えなくもないがな……くっくっくっ。'
 show nao_v002 fuan at active
 show beatrice_v001 smile_close at inactive
 nao 'それこそ冗談じゃないわ。あたしはまだまだ、\nやりたいこととやるべきことがあるんだから……。\nこんな年で地獄行きだなんてまっぴら御免よ。'
 show beatrice_v001 futeki at active
 show nao_v002 fuan at inactive
 beatrice '……ほぉ？\u3000そのわりに、あの「世界」に\n足を踏み入れた当初は早急なる死と絶望を\n望んでいたようだが……？'
 show nao_v002 fuan_close at active
 show beatrice_v001 futeki at inactive
 nao '……そんなことまでお見通しなのね。\nとてもかなわないわ。'
 show beatrice_v001 futeki at updown_shake_transform,active
 show nao_v002 fuan_close at inactive
 beatrice 'くっくっくっくっく…。\nまさか互角の勝負ができると思っていたとはな、\n残念、お生憎様だ。'
 show beatrice_v001 smile at active
 show nao_v002 fuan_close at inactive
 beatrice '妾はそなたが持つ小さな経験や知識なぞ比べるに値しない、\n千年を生きる黄金の魔女よ。'
 show nao_v002 normal at active
 show beatrice_v001 smile at inactive
 nao '大丈夫。\nそんなふうに脅さなくても、格の違いくらいは\nわかってるつもりよ。反抗する気なんてないわ。'
 show nao_v002 normal at active
 show beatrice_v001 smile at inactive
 nao 'あたしにできなくて、あなたにならできることは\nそれこそ星の数以上でしょうしね。'
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice 'あぁ……その通りだ。\nだが、妾にも出来ぬことはある。'
 show beatrice_v001 normal_close at active
 show nao_v002 normal at inactive
 beatrice '妾とそなたが出会うという奇縁、\nそれをきっかけに生まれた変化をこうして楽しむのも、\nその歪を理解しているからなのかもしれぬな……。'
 show nao_v002 normal at active
 show beatrice_v001 normal_close at inactive
 nao '……。魔女のベアトリーチェにも、\nできなかったことで悔しかったり\n悲しかったりした思い出があるのね。'
 show beatrice_v001 smile at active
 show nao_v002 normal at inactive
 beatrice 'ふっ……そなたは本当に、怖いもの知らずというものだ。\n他の魔女だと、その質問ひとつで不敬だと\n即座に首が宙を舞うこともあるのだぞ。'
 show nao_v002 fuan at chara_shake_transform,active
 show beatrice_v001 smile at inactive
 nao '……っ……。'
 show beatrice_v001 normal at active
 show nao_v002 fuan at inactive
 beatrice 'そう身を固くするでないぞ。別に怒ったわけではない。\nそもそも妾はそなたの「過去」を知っておる。\n今に至った経緯について賞賛も感じているのだ。'
 show beatrice_v001 normal_close at active
 show nao_v002 fuan at inactive
 beatrice '生まれてこなければよかった……か。\nそこまでの絶望を味わいながらも\nそなたは這い上がってきた、大したものよ……。'
 show nao_v002 normal at active
 show beatrice_v001 normal_close at inactive
 nao 'ベアトリーチェ……？'
 show beatrice_v001 smile at active
 show nao_v002 normal at inactive
 beatrice 'ふっ……戯言だったな、忘れて良い。\n妾は少々感傷的になっているのかもしれんな。'
 return