label chara462001_02:
 stop sound
 scene expression "#000"
 play music 'audio/bgm/BGM_QUEST5_COLLAB2.wav'
 show expression 'images/bg/AdvBg_204.png.png' as bg
 with Dissolve(1.0)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika 'と、やって来たのはいいですけど……\nほんとになーんにもないところですね。'
 show erika_v001 normal at active
 erika '寂れた寒村、ほとんどいない人間。\n景色ぐらいしか取り柄がなさそう……。'
 show erika_v001 normal_close at active
 erika '一昔前なら、頭からふけを落とす\n探偵がやって来そうな感じですが、\nさすがに時代が違っていそうですし。'
 show erika_v001 normal at active
 erika 'せめて連続殺人事件とか怪奇事件とか、\n灰色の脳細胞を刺激してくれるようなことが\n起こったりしないですかねぇ……はーあ。'
 show erika_v001 normal at active
 erika 'しかし……菜央さんはいったい\nどこにいるのでしょう？'
 show erika_v001 normal at active
 erika '推理してみましょう……\n寂れた田舎で子供が集まる場所は限られます。'
 show erika_v001 normal_close at active
 erika '学校……は、時間から考えて下校した後。\n公園……は、この村にあるとは思えませんね。\n予算もなければ遊具の管理すら難しいでしょうし。'
 show erika_v001 normal at active
 erika 'だとしたら、一番可能性の高い場所は\n遊び場の代わりとなる……神社。'
 show erika_v001 normal at active
 erika 'よしんばいなかったとしても、この寒村。\n子どもの数はそう多くないはず。'
 show erika_v001 normal at active
 erika 'となれば、あの小娘の居場所や家を聞き出すのは\n造作もないこと――。'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 play audio 'audio/sfx/SE_226_shine.wav'
 show erika_v001 smile at active
 erika 'ただ村を一瞥しただけで、\n古戸ヱリカはこの程度の推理が可能です。\nいかがですか、皆さん。'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 show erika_v001 normal_close at active
 erika '……やはり聴衆がいないと張り合いが\nいまひとつですね。やっぱりドラノールを\n無理やりにでも連れてくればよかったです。'
 show erika_v001 normal at active
 erika 'まぁいいでしょう。\nとりあえず、あの小娘を見つけて\nとっとと引きずり込むことにしますか。'
 show erika_v001 normal at active
 erika '神社は災害時の避難所を兼ねますから、\n高い場所にあると相場は決まっています。\n……さて、推理の結果を確認しに行くとしますか。'
 window hide None
 show expression "#000" as fade with Dissolve(1.0)
 hide erika_v001
 with Dissolve(0.2)
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_161.png' as bg
 with Dissolve(1.0)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika 'おや、子どもの声がしますね。\nどうやら推理は的中していたようです。\n……まぁ、当然ですが。'
 show erika_v001 normal at active
 erika 'さて、あの小娘の居場所を聞き出すとしましょう。'
 stop music fadeout 0.5
 window hide None
 show expression "#000" as fade with Dissolve(1.0)
 hide erika_v001
 with Dissolve(0.2)
 stop sound
 scene expression "#000"
 play music 'audio/bgm/BGM_HOME_COLLAB2.wav'
 show expression 'images/bg/AdvBg_1101.png' as bg
 with Dissolve(1.0)
 show kazuho_v002 smile at mei_left
 show rika_v002 smile at mei_right
 with Dissolve(0.5)
 show rika_v002 smile at active
 show kazuho_v002 smile at inactive
 rika 'はい、一穂。沙都子。\nお茶をどうぞなのです。'
 show kazuho_v002 smile at active
 show rika_v002 smile at inactive
 kazuho 'ありがとう、梨花ちゃん\n……はぁ、おいしい。'
 show rika_v002 smile at active
 show kazuho_v002 smile at inactive
 rika 'ありがとうはこちらの台詞なのです。\nボクの代わりに、一穂がお茶っ葉を\n買ってきてくれて助かったのですよ。'
 show kazuho_v002 smile at active
 show rika_v002 smile at inactive
 kazuho 'この程度のお遣い、お安い御用だよ。\n……けど、神社の清掃をお願いした\n業者さんって、遅いね？'
 show rika_v002 fuan at active
 show kazuho_v002 smile at inactive
 rika 'みー。もう来る時間だから\n不在はまずいと思って、一穂に\nお遣いを頼みましたのですが……。'
 hide rika_v002
 show satoko_v002 fuan at mei_right
 with Dissolve(0.5)
 show satoko_v002 fuan at active
 show kazuho_v002 smile at inactive
 satoko 'こんなことになるのでしたら、\n私が用事を終わらせてから買いに行っても、\n全然間に合いましたわね。'
 show kazuho_v002 fuan at active
 show satoko_v002 fuan at inactive
 kazuho 'うーん、きっと前の仕事が\n長引いているんだと思うよ。'
 show satoko_v002 fuan_close at active
 show kazuho_v002 fuan at inactive
 satoko 'そうかもしれませんが、それなら連絡の\n一本くらいあってもバチが当たらないと\n思いますわ……。'
 hide kazuho_v002
 hide satoko_v002
 with Dissolve(0.2)
 show rika_v002 fuan at mei_right
 show satoko_v002 normal at mei_left
 with Dissolve(0.5)
 show satoko_v002 normal at active
 show rika_v002 fuan at inactive
 satoko 'でも梨花、どうして一穂さんに\nお遣いをお願いしましたの？'
 show rika_v002 smile at active
 show satoko_v002 normal at inactive
 rika 'みー。お茶がなくて困っている時に\nたまたま一穂に電話をもらったのですよ。'
 hide satoko_v002
 show kazuho_v002 smile at mei_left
 with Dissolve(0.5)
 show kazuho_v002 smile at active
 show rika_v002 smile at inactive
 kazuho 'うん。前に梨花ちゃんからもらったりんごで、\n美雪ちゃんがコンポート？\u3000ってお菓子を\n作ったから、お裾分けしようと思ってね。'
 show kazuho_v002 smile at active
 show rika_v002 smile at inactive
 kazuho 'それを持ってくるついでに、\nお茶っ葉のお遣いをしてきたんだよ。'
 show rika_v002 smile at active
 show kazuho_v002 smile at inactive
 rika 'コンポートは冷やした方がおいしいそうなので、\n今夜のデザートにいただきましょうなのです。'
 hide rika_v002
 show satoko_v002 smile at mei_right
 with Dissolve(0.5)
 show satoko_v002 smile at active
 show kazuho_v002 smile at inactive
 satoko 'あら、それは楽しみですわね。\n……ですが、美雪さんは？'
 show kazuho_v002 fuan_close at active
 show satoko_v002 smile at inactive
 kazuho '今も鍋につきっきりでコンポートを作ってるよ。\n家の中、全部甘い香りでいっぱいでね……。'
 show satoko_v002 fuan at active
 show kazuho_v002 fuan_close at inactive
 satoko '羽入さんは今、家でお昼寝しているんでしたっけ？\nもしここにいてその話を聞いたら、美雪さんの家へ\n一目散に駆け出して行きそうですわ～。'
 show kazuho_v002 fuan at active
 show satoko_v002 fuan at inactive
 kazuho 'う、うん。\n羽入ちゃんだったら好きな匂いだと思うけど……\n私はちょっと、頭が痛くなってきちゃって。'
 hide satoko_v002
 show rika_v002 fuan at mei_right
 with Dissolve(0.5)
 show rika_v002 fuan at active
 show kazuho_v002 fuan at inactive
 rika 'みー。匂いは好き嫌いが出やすいのです。'
 hide kazuho_v002
 hide rika_v002
 with Dissolve(0.2)
 show kazuho_v002 smile at mei_center
 with Dissolve(0.5)
 show kazuho_v002 smile at active
 kazuho '菜央ちゃんは大丈夫みたいなんだけどね。\nあの匂いの中でも、ぐっすりお昼寝……あれ？'
 show kazuho_v002 normal at active
 kazuho 'あの鳥居の下にいる人って……\nもしかして業者さんじゃない？'
 hide kazuho_v002
 with Dissolve(0.2)
 show rika_v002 normal at mei_right
 show satoko_v002 odoroki at mei_left
 with Dissolve(0.5)
 show satoko_v002 odoroki at active
 show rika_v002 normal at inactive
 satoko 'えっ？\nですがあの方、お掃除をする格好には\nとても見えませんが……。'
 show rika_v002 normal at active
 show satoko_v002 odoroki at inactive
 rika 'みー……\nドレスみたいな服を着てるのです。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide rika_v002
 hide satoko_v002
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show erika_v001 odoroki at active
 erika 'あ、ぁ、あ、ぁああぁあああああああ……！'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show rika_v002 odoroki at mei_center
 with Dissolve(0.5)
 show rika_v002 odoroki at active
 rika 'えっ？！'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide rika_v002
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show erika_v001 odoroki at active
 erika 'あぁーーーーーーーっ！！'
 play audio 'audio/sfx/SE_408_run.wav'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show kazuho_v002 odoroki at mei_center
 with Dissolve(0.5)
 show kazuho_v002 odoroki at chara_shake_transform,active
 kazuho 'こ、こっちに向かって全力ダッシュ？！'
 hide kazuho_v002
 with Dissolve(0.2)
 show rika_v002 fuan at mei_right
 show satoko_v002 odoroki at mei_left
 with Dissolve(0.5)
 show satoko_v002 odoroki at jump_transform,active
 show rika_v002 fuan at inactive
 satoko 'りっ、梨花ぁ！\nあの方って、あなたの知っている人ですの？！'
 show rika_v002 fuan at active
 show satoko_v002 odoroki at inactive
 rika 'し、知らない人なのです！'
 hide satoko_v002
 show kazuho_v002 fuan at mei_left
 with Dissolve(0.5)
 show kazuho_v002 fuan at active
 show rika_v002 fuan at inactive
 kazuho 'でもあの人、ミサイルみたいな勢いで\nこっちに向かってくるよ……？！'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide rika_v002
 hide kazuho_v002
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_224_sliding.wav'
 camera at screenshake_transform
 pause 0.0
 show erika_v001 odoroki at active
 erika '我が主ぃいいいぃいいいいいぃいいいい！！！'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show rika_v002 odoroki at mei_center
 with Dissolve(0.5)
 show rika_v002 odoroki at jump_transform,active
 rika 'みーっ？！'
 hide rika_v002
 with Dissolve(0.2)
 show kazuho_v002 fuan at mei_left
 show satoko_v002 odoroki at mei_right
 with Dissolve(0.5)
 show satoko_v002 odoroki at chara_shake_transform,active
 show kazuho_v002 fuan at inactive
 satoko 'ふわぁぁぁあぁっっ？\n見知らぬ方が、梨花の足元へ流れるように\nスライディング土下座？！'
 show kazuho_v002 fuan at active
 show satoko_v002 odoroki at inactive
 kazuho 'すごい、芸術的な土下座……！'
 hide kazuho_v002
 hide satoko_v002
 with Dissolve(0.2)
 show rika_v002 fuan at mei_right
 show erika_v001 odoroki at mei_left
 with Dissolve(0.5)
 show erika_v001 odoroki at active
 show rika_v002 fuan at inactive
 erika 'なななな、何故我が主がこのような\n寂れた場所にいらっしゃるのですか？！'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.1
 pause 0.5
 show erika_v001 sinken at active
 show rika_v002 fuan at inactive
 erika 'はっ……！？\nもしや、私がどのような働きを見せるか、\nわざわざ見学にいらっしゃったと……？！'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show erika_v001 smile at active
 show rika_v002 fuan at inactive
 erika 'あ、ありがとうございます！\nそこまでご期待いただけていたことを\n理解できず、本当に申し訳ございません！！'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 show rika_v002 fuan at active
 show erika_v001 smile at inactive
 rika 'あ、あの……。'
 play audio 'audio/sfx/SE_311_ls_cutejump.wav'
 show erika_v001 smile at jump_transform,active
 show rika_v002 fuan at inactive
 erika 'はい、なんでしょうか！'
 show rika_v002 fuan at active
 show erika_v001 smile at inactive
 rika 'ど、どちらさまですか？'
 show erika_v001 odoroki at active
 show rika_v002 fuan at inactive
 erika 'えっ？……我が主、ですよね？'
 show rika_v002 normal at active
 show erika_v001 odoroki at inactive
 rika '違うのです。'
 show erika_v001 odoroki at chara_shake_transform,active
 show rika_v002 normal at inactive
 erika 'は？！\u3000い、いや、そんなご冗談を……。'
 hide rika_v002
 hide erika_v001
 with Dissolve(0.2)
 show satoko_v002 fuan at mei_right
 show kazuho_v002 normal at mei_left
 with Dissolve(0.5)
 show kazuho_v002 normal at active
 show satoko_v002 fuan at inactive
 kazuho 'ねぇ、梨花ちゃん。もしかしてこの方が\n清掃業者の人……じゃないの？'
 show satoko_v002 fuan at active
 show kazuho_v002 normal at inactive
 satoko '我が主とか、言ってますわよ？'
 show kazuho_v002 fuan at active
 show satoko_v002 fuan at inactive
 kazuho 'えっと……そ、そういうサービス、とか？'
 show kazuho_v002 sinken at active
 show satoko_v002 fuan at inactive
 kazuho 'ほ、ほら！\u3000エンジェルモートみたいに\nかわいい制服の店員さんがお客さんを\nご主人様として扱う……みたいな？！'
 show satoko_v002 fuan at active
 show kazuho_v002 sinken at inactive
 satoko '一穂さん……それ、本気で言っておりますの？'
 show kazuho_v002 fuan_close at active
 show kazuho_v002 fuan_close:
  linear 0.5 pos (480,1250)
 show satoko_v002 fuan at inactive
 pause 0.5
 kazuho '……ごめんなさい。\n自分で言っててなんだけど、\nあんまり自信ない……うぅっ。'
 show kazuho_v002 fuan_close
 show kazuho_v002 fuan_close:
  linear 0.5 pos (480,1200)
 pause 0.5
 show kazuho_v002 sinken at active
 show satoko_v002 fuan at inactive
 kazuho 'け、けど一度、ちゃんと確かめた方が\n良いと思うよ！'
 hide satoko_v002
 hide kazuho_v002
 with Dissolve(0.2)
 show erika_v001 smile at mei_left
 show rika_v002 fuan at mei_right
 with Dissolve(0.5)
 show rika_v002 fuan at active
 show erika_v001 smile at inactive
 rika 'みー。ボクも違うとは思いますが、\n一穂の言うことにも一理あるのです……。'
 show rika_v002 normal at active
 show erika_v001 smile at inactive
 rika 'あの……もしかして喜一郎がお願いした、\n清掃業者の方ですか？'
 show erika_v001 sinken at active
 show rika_v002 normal at inactive
 erika '清掃業者？'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide erika_v001
 hide rika_v002
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 odoroki at active
 erika '…………はっ？！'
 show erika_v001 smile at active
 erika 'なるほど、そういうことですか。\nこれも我が主の暇潰し。いえ、慈悲！'
 show erika_v001 smile at active
 erika 'つまり不快にさせてしまったリベンジに\nこの古ぼけた神社の掃除ができたら\n少しは見直してやろうという我が主のお心遣い！！'
 camera at screenshake_transform
 pause 0.0
 show erika_v001 smile at active
 erika 'つまり！\u3000これはある意味ボーナスステージ？！？！'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show kazuho_v002 fuan at mei_left
 show satoko_v002 fuan at mei_right
 with Dissolve(0.5)
 show satoko_v002 fuan at active
 show kazuho_v002 fuan at inactive
 satoko '……何を言ってるのか、全然わかりませんわ。'
 show kazuho_v002 fuan at active
 show satoko_v002 fuan at inactive
 kazuho 'わ、私もわかんない……。'
 hide kazuho_v002
 hide satoko_v002
 with Dissolve(0.2)
 show erika_v001 smile at mei_left
 show rika_v002 fuan at mei_right
 with Dissolve(0.5)
 show rika_v002 fuan at active
 show erika_v001 smile at inactive
 rika 'みー……。'
 show erika_v001 smile at active
 show rika_v002 fuan at inactive
 erika '大変申し訳ございません！\nではこれより、古戸ヱリカの\n華麗な掃除術をお見せ致しましょう！'
 show erika_v001 smile at jump_transform,active
 show rika_v002 fuan at inactive
 erika 'さて、掃除道具はどちらにありますか？'
 show rika_v002 fuan_close at active
 show erika_v001 smile at inactive
 rika 'みー。てっきり業者の人が専門の掃除道具を\n持ってくると思って……。'
 hide erika_v001
 show satoko_v002 fuan at mei_left
 with Dissolve(0.5)
 show satoko_v002 fuan at active
 show rika_v002 fuan_close at inactive
 satoko '特に、何も……。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide rika_v002
 hide satoko_v002
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 smile at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 smile at active
 erika '……はっ！\nふ、ふふふ、なるほど。わかりましたよ。'
 show erika_v001 smile at active
 erika '文字通り舌で舐めるように\n掃除しろと言うことですね！\n了解致しました、我が主！'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show rika_v002 fuan at mei_right
 show kazuho_v002 sinken at mei_left
 with Dissolve(0.5)
 camera at screenshake_transform
 pause 0.0
 show kazuho_v002 sinken at active
 show rika_v002 fuan at inactive
 kazuho 'ちっ、違うと思います！'
 show rika_v002 fuan at active
 show kazuho_v002 sinken at inactive
 rika '……むしろ逆に汚いと思うのですよ。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide rika_v002
 hide kazuho_v002
 hide fade with Dissolve(0.08333333333333333)
 show satoko_v002 fuan at mei_center
 with Dissolve(0.08333333333333333)
 show satoko_v002 fuan at chara_shake_transform,active
 satoko 'い、今すぐ掃除道具を準備しますわ！\nだから、早まらないで下さいまし！\nお願いですからぁぁぁ！'