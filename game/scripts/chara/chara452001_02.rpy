label chara452001_02:
 show black_background onlayer black
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2190.png' as bg
 with Dissolve(1.0)
 show nao_v002 normal at mei_right
 show beatrice_v001 normal_close at mei_left
 with Dissolve(0.5)
 show beatrice_v001 normal_close at active
 show nao_v002 normal at inactive
 beatrice 'そろそろ時間のようだ。……また会おうぞ、迷い子よ。'
 show nao_v002 odoroki at jump_transform,active
 show beatrice_v001 normal_close at inactive
 nao 'えっ……あっ、ちょっと……？！'
 play audio 'audio/sfx/SE_230_charge.wav'
 show expression "#000" as fade with Dissolve(1.0)
 hide beatrice_v001
 with Dissolve(0.3)
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_287.png' as bg
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_543_bird.wav'
 play music 'audio/bgm/BGM_QUEST2_COLLAB2.ogg'
 nao 'っ……ここは、興宮……？'
 nao 'あれ、あたし今まで何をしてたんだっけ……？\nというか、そもそもなんのために興宮に……。'
 show rena_v002 odoroki at mei_left
 with Dissolve(0.5)
 show rena_v002 odoroki at active
 rena '……あれ、菜央ちゃん？'
 show rena_v002 odoroki at inactive
 nao 'あっ、レナちゃん！'
 show rena_v002 smile at active
 rena 'あははは、こんにちは。\n……買い物の途中？'
 show rena_v002 smile at inactive
 nao 'えっ？\u3000あ、う、うん！'
 show rena_v002 smile at inactive
 nao '（そっか、あたし買い物の途中だったのね）'
 show rena_v002 smile at active
 rena 'はぅ……１人で運ぶには荷物多そうだね。\nよかったら少し持ってあげようか？'
 show rena_v002 smile at inactive
 nao 'ううん、平気。\n……そっか、あたしは夕飯の食材の\n買い出しに来たんだった。'
 show rena_v002 fuan at active
 rena 'そういえば、今日は一穂ちゃんたちと\n一緒じゃないのかな……かな？'
 show rena_v002 fuan at inactive
 nao '一穂は家でお掃除。\n美雪は１人で散歩に出かけてるわ。'
 show rena_v002 fuan at inactive
 nao '（……うん、ようやく思い出してきた。\nそう、そのはず……だと、思う）'
 show rena_v002 fuan at active
 rena '菜央ちゃん……？'
 show rena_v002 fuan at inactive
 nao 'あ、ごめんなさい。\nレナちゃんこそ、興宮にはお買い物で？'
 show rena_v002 smile at nod_transform,active
 rena 'うん。ちょうど終わったところだから、\nこれから帰るところなの。\nよかったら菜央ちゃんも、一緒に戻らない？'
 show rena_v002 smile at inactive
 nao 'うんっ。ありがとう、レナちゃん。'
 stop music fadeout 0.5
 window hide None
 show expression "#000" as fade with Dissolve(1.0)
 stop sound
 scene expression "#000"
 pause 1.0
 show expression 'images/bg/AdvBg_1352.png' as bg
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_501_crow.wav'
 play music 'audio/bgm/BGM_GACHA_COLLAB2.ogg'
 rena '日の暮れるのが早くなってきたね……。\n暗い道は危ないから、そろそろお買い物は\n誰かと一緒の方がいいと思うよ。'
 nao 'えぇ、そうするわ。'
 rena '……？\u3000どうしたの、菜央ちゃん。'
 nao 'えっ……な、何が？'
 rena 'なんだか、いつもより口数が少ないから……\n何か心配事でもあったりするのかな、かな？'
 nao 'ううん。そういうわけじゃないんだけど……。'
 nao '……。あの、レナちゃん。'
 rena 'なに、菜央ちゃん？'
 nao 'レナちゃんは、どんなに頑張って、頑張っても\nできないって思い知らされて、落ち込んだ時……\nなんて言葉をかけられたら元気になってくれる？'
 rena 'はぅ、えっと……\n菜央ちゃんの近くに、そういう悩みを\n持っている人がいるってことなのかな、かな？'
 nao '……えぇ。'
 nao '（名前と顔は思い出せないけど……そうだ。\nあたしにはそういう人がいる……そんな気がする）'
 rena '美雪ちゃんか、一穂ちゃん……じゃなさそうだね。'
 nao 'うん。あの２人が相手なら、\nどうすればいいかわかってるもの。\nだから、こんなに悩まなかったと思うわ。'
 rena 'でも、大事な人なんだね。'
 nao '大事……そうね。たぶんそうだわ。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide nao_v002
 hide rena_v002
 hide fade with Dissolve(0.08333333333333333)
 show nao_v002 normal at mei_center
 with Dissolve(0.08333333333333333)
 show nao_v002 normal at active
 nao 'その人、すごくプライドが高くて、\n簡単には本音を見せてくれないんだけど……。'
 show nao_v002 normal at active
 nao '本当はすごく繊細で、\n傷つきやすい人じゃないかって感じるの。'
 show nao_v002 fuan at active
 nao 'だから、詳しい事情も理解してないのに\n変に慰めの言葉をかけても傷つけそうで、\nなんて言えばいいのかわかんなくて……。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show rena_v002 normal_close at mei_left
 show nao_v002 fuan at mei_right
 with Dissolve(0.5)
 show rena_v002 normal_close at active
 show nao_v002 fuan at inactive
 rena '…………。'
 show nao_v002 fuan at active
 show rena_v002 normal_close at inactive
 nao 'ごめんね、レナちゃん。\nあたしの変な悩みに巻き込んじゃったりして。'
 show rena_v002 smile at active
 show nao_v002 fuan at inactive
 rena 'ううん、そんなことないよ。\n……そうだね。レナの意見でよければ\n聞いてくれる？'
 show nao_v002 smile at nod_transform,active
 show rena_v002 smile at inactive
 nao 'う、うん、もちろんよ！\u3000聞かせて！'
 show rena_v002 smile_close at active
 show nao_v002 smile at inactive
 rena 'あはは、ありがとう。\nえっと、そうだね……。'
 show rena_v002 smile at active
 show nao_v002 smile at inactive
 rena '確かに慰めたり、励まされたりするのって\n嬉しい時もあるけど……。'
 show rena_v002 smile at active
 show nao_v002 smile at inactive
 rena '自分で立ち上がりたいと頑張っている時に\n励まされたら、その時の気持ち次第では\nその応援が邪魔に感じちゃうこともあるかもね。'
 show nao_v002 fuan at active
 show rena_v002 smile at inactive
 nao '勉強しようとしてる時に\n勉強しろって言われると、\n逆に反発する……みたいな？'
 show rena_v002 smile at nod_transform,active
 show nao_v002 fuan at inactive
 rena 'そうそう、そんな感じ。'
 show nao_v002 fuan at active
 show rena_v002 smile at inactive
 nao 'だとしたら、どうしたらいいのかしら……。'
 show rena_v002 smile_close at active
 show nao_v002 fuan at inactive
 rena '……別に、立ち上がらせようと考えなくても\nいいと思うよ。'
 show nao_v002 odoroki at active
 show rena_v002 smile_close at inactive
 nao '……どういうこと？'
 show rena_v002 smile at active
 show nao_v002 odoroki at inactive
 rena '立ち上がるための力じゃなくて、\n立ち上がるための力が出るように、\n明るく楽しい気分になれるよう協力する……。'
 show rena_v002 smile at active
 show nao_v002 odoroki at inactive
 rena 'なんて、どうかな？\u3000かな？'
 show nao_v002 fuan at active
 show rena_v002 smile at inactive
 nao 'ごめんなさい、レナちゃん。\nその説明だと、ちょっと想像しにくくて……\nよかったら具体例を教えてくれる？'
 show rena_v002 smile at active
 show nao_v002 fuan at inactive
 rena 'うーん、そうだね……。\n勉強のやる気を出そうとした人に、\nお菓子を差し入れする、なんてどうかな？\u3000かな？'
 show nao_v002 normal at active
 show rena_v002 smile at inactive
 nao '……差し入れ。'
 show rena_v002 smile at active
 show nao_v002 normal at inactive
 rena 'その人が好きなものって、知ってる？'
 show nao_v002 smile at nod_transform,active
 show rena_v002 smile at inactive
 nao 'えぇ、わかるわ。\nそっか、差し入れか……。'
 show nao_v002 smile at active
 show rena_v002 smile at inactive
 nao 'ありがとう、レナちゃん。\n相手にどう思ってもらえるかわからないけど、\nあたし……やってみるわ。'
 show rena_v002 smile at nod_transform,active
 show nao_v002 smile at inactive
 rena 'うんっ、頑張って。\n菜央ちゃんがうまくいくよう、\nレナは応援しているからね……！'
 return