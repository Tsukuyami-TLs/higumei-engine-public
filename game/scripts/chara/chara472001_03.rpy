label chara472001_03:
 show black_background onlayer black
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_103.png' as bg
 with Dissolve(1.0)
 show nao_v001 sinken at mei_center
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_528_unfold_cloth.wav'
 camera at screenshake_transform
 pause 0.0
 show nao_v001 sinken at active
 nao '待って！'
 hide nao_v001
 with Dissolve(0.2)
 play music 'audio/bgm/BGM_HOME_COLLAB2.flac'
 show kazuho_v001 normal at mei_left
 show miyuki_v001 normal at mei_right
 with Dissolve(0.5)
 show miyuki_v001 normal at active
 show kazuho_v001 normal at inactive
 miyuki 'ん、どうしたの菜央。'
 show kazuho_v001 normal at active
 show miyuki_v001 normal at inactive
 kazuho 'お昼寝から、目が覚めたの？'
 hide miyuki_v001
 show nao_v001 normal_close at mei_right
 with Dissolve(0.5)
 show nao_v001 normal_close at active
 show kazuho_v001 normal at inactive
 nao 'えぇ……目が覚めたわ。'
 show kazuho_v001 fuan at active
 show nao_v001 normal_close at inactive
 kazuho 'どうしたの、まだ眠い？'
 show nao_v001 fuan at active
 show kazuho_v001 fuan at inactive
 nao 'そうじゃない……けど。\nもう少しだけ、眠っていたかった気がするわ。'
 show nao_v001 smile_close at active
 show kazuho_v001 fuan at inactive
 nao 'なんだか、\nとっても楽しい夢を見ていた気がするの。'
 window hide None
 show expression "#000" as fade with Dissolve(1.0)
 hide kazuho_v001
 hide nao_v001
 with Dissolve(0.2)
 stop sound
 scene expression "#000"
 pause 1.0
 play music 'audio/bgm/BGM_QUEST6_COLLAB2.flac'
 show expression 'images/bg/AdvBg_2190.png' as bg
 with Dissolve(1.0)
 show beatrice_v001 normal_close at mei_right
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show beatrice_v001 normal_close at inactive
 dlanor '法律のために人がいるのではありマセン。\n人のために法律がありマス。'
 show dlanor_v001 normal at active
 show beatrice_v001 normal_close at inactive
 dlanor 'ですが、人を守るための法律を悪用し、\n人を傷つける悪人が生まれる場合もありマス。'
 show dlanor_v001 normal at active
 show beatrice_v001 normal_close at inactive
 dlanor '……ルールとは常に、ある一方を守ると同時に、\nもう片方を傷つける刃にもなりえマス。'
 show beatrice_v001 normal at active
 show dlanor_v001 normal at inactive
 beatrice 'だが、ドラノール卿たちが守り続けていなければ\nミステリー自体が崩壊していたやもしれぬ。'
 show dlanor_v001 fuan_close at active
 show beatrice_v001 normal at inactive
 dlanor 'ハイ。……とはいえ、『ノックス十戒』などの\nルールが原因で、ミステリーに窮屈さを覚える人が\nいるのも事実デス。'
 show beatrice_v001 normal_close at active
 show dlanor_v001 fuan_close at inactive
 beatrice 'それも真理だ。しかし、ルールがあるからこそ\nミステリーというものは迷い子本来の時代にも\n存在し続けているとも言える。'
 show beatrice_v001 normal at active
 show dlanor_v001 fuan_close at inactive
 beatrice 'ミステリーが一時的に衰退したとしても、\n消滅することはないだろう。'
 show beatrice_v001 smile at active
 show dlanor_v001 fuan_close at inactive
 beatrice '……その証拠に、あの少女はきっと\n目が覚めた後にミステリー小説を手に取る。\nそしてまた、相まみえることが叶うだろう。'
 show dlanor_v001 normal at active
 show beatrice_v001 smile at inactive
 dlanor 'ただ……その時にはここでのことを、\n菜央は忘れているのデハ？'
 show beatrice_v001 normal_close at active
 show dlanor_v001 normal at inactive
 beatrice 'あぁ、忘れているだろうな。\nもし思い出したとしても、\n夢を見たで、済ませるやもしれぬ。'
 show beatrice_v001 normal at active
 show dlanor_v001 normal at inactive
 beatrice 'だが、面白いという感情は\n心の奥底に深く根付く。'
 show beatrice_v001 smile at active
 show dlanor_v001 normal at inactive
 beatrice '『ノックス十戒』を\n面白いと思ったあの迷い子ならば、\nきっとミステリーに手を伸ばすであろう。'
 show dlanor_v001 normal_close at active
 show beatrice_v001 smile at inactive
 dlanor 'そうだといいデスネ。\n……では、私も失礼しようと思いマス。'
 show beatrice_v001 smile at active
 show dlanor_v001 normal_close at inactive
 beatrice '迎えにいくのか？'
 show dlanor_v001 normal at active
 show beatrice_v001 smile at inactive
 dlanor 'ハイ。今頃、ゴロゴロと部屋で\n転がり回っていると思いマス。\n……ミス・ベアトリーチェ。'
 show beatrice_v001 normal at active
 show dlanor_v001 normal at inactive
 beatrice 'なんだ？'
 show dlanor_v001 smile at active
 show beatrice_v001 normal at inactive
 dlanor 'この残ったクッキー、\n持ち帰っても良いデスカ？'
 stop music fadeout 0.5
 window hide None
 show expression "#000" as fade with Dissolve(1.0)
 hide beatrice_v001
 hide dlanor_v001
 with Dissolve(0.2)
 stop sound
 scene expression "#000"
 play music 'audio/bgm/BGM_QUEST5_COLLAB2.flac'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show expression 'images/bg/AdvBg_2180.png' as bg
 with Dissolve(1.0)
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 odoroki_close at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 odoroki_close at active
 erika 'うぅうう、まさか#p雛見沢#sひなみざわ#rに\n我が主とうり二つの別人がいただなんて……！'
 show erika_v001 odoroki_close at chara_shake_transform,active
 erika 'うぅ、もう二度と間違えません！\nうぅ、うぅぅううぅうぅぅぅっ……！'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show erika_v001 odoroki_close at mei_right
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show erika_v001 odoroki_close at inactive
 dlanor 'ヱリカ卿。'
 show erika_v001 sinken at active
 show dlanor_v001 normal at inactive
 erika '……ドラノールですか。\nなんですか、我が主からお叱りを受けた私を\n笑いに来たんですか？'
 show dlanor_v001 normal_close at active
 show erika_v001 sinken at inactive
 dlanor 'イイエ。そのようなことはありマセン。'
 show erika_v001 sinken at active
 show dlanor_v001 normal_close at inactive
 erika 'じゃあなんで……\nって、なんですかそのクッキーは。'
 show dlanor_v001 smile at active
 show erika_v001 sinken at inactive
 dlanor 'いただきものデス。\nよかったら、一緒に食べマショウ。'
 show erika_v001 sinken_close at active
 show dlanor_v001 smile at inactive
 erika '……じゃあ、もらいます。'
 show erika_v001 normal at active
 show dlanor_v001 smile at inactive
 erika 'ふぅん……悪くありませんね。\nもうすこし甘い方が脳の栄養補給には\n良さそうですが。'
 show dlanor_v001 smile_close at active
 show erika_v001 normal at inactive
 dlanor '口に合ったなら良かったデス。'
 show erika_v001 normal at active
 show dlanor_v001 smile_close at inactive
 erika '……なんだか機嫌が良いですね。\n良いことでもありました？'
 show dlanor_v001 smile at active
 show erika_v001 normal at inactive
 dlanor 'ハイ。新しいミステリーの読者が、\nまたひとり増えたかもしれマセン。'
 show erika_v001 normal at active
 show dlanor_v001 smile at inactive
 erika 'ふぅん？\u3000いいことじゃないですか。\nミステリーの話ができる人が増えるのは、\n私も大歓迎です。'
 show erika_v001 futeki at active
 show dlanor_v001 smile at inactive
 erika 'ちょっとかじった程度で、わかった気になった\n半端モノの心を叩き折るのが楽しみです……。'
 show dlanor_v001 normal at active
 show erika_v001 futeki at inactive
 dlanor 'そう簡単に折れる相手ではないかも\nしれマセン。'
 show erika_v001 normal at active
 show dlanor_v001 normal at inactive
 erika 'へぇ……珍しく自信ありげですね。\nあんたが見込んだそいつと戦うのが楽しみです。'
 show dlanor_v001 smile at active
 show erika_v001 normal at inactive
 dlanor 'ハイ。……私も、楽しみデス。'
 return