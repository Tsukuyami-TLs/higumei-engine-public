label chara462001_03:
 show black_background onlayer black
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_262.png' as bg
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_501_crow.wav'
 pause 1.0
 call wipeout_routine
 stop sound
 scene expression "#000"
 play music 'audio/bgm/BGM_QUEST5_COLLAB2.flac'
 show expression 'images/bg/AdvBg_782.png' as bg
 call wipein_routine
 show erika_v001 sinken_close at mei_center
 with Dissolve(0.5)
 show erika_v001 sinken_close at active
 erika 'つ、疲れました……。'
 window hide None
 show expression "#000" as fade with Dissolve(1.0)
 hide erika_v001
 with Dissolve(0.2)
 stop sound
 scene expression "#000"
 camera at sepia_shader
 pause 0.0
 show expression 'images/bg/AdvBg_161.png' as bg
 show satoko_v002 sinken at mei_left
 show rika_v002 fuan at mei_right
 with Dissolve(1.0)
 show rika_v002 fuan at active
 show satoko_v002 sinken at inactive
 rika '……ですから、ボクは古手梨花。\nあなたのご主人様ではないのです。'
 show rika_v002 fuan at active
 show satoko_v002 sinken at inactive
 rika 'ボクはあなたのこと、知らないのですよ。'
 show satoko_v002 sinken at active
 show rika_v002 fuan at inactive
 satoko 'どれだけそっくりかわかりませんが、\n梨花とあなたのご主人様は全くの別人！\n違う人！\u3000ですわ！'
 hide satoko_v002
 hide rika_v002
 with Dissolve(0.2)
 show kazuho_v002 fuan at mei_center
 with Dissolve(0.5)
 show kazuho_v002 fuan at active
 kazuho 'というより、あなたのご主人様って\nちょっと……話を聞く限り、その……。'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show kazuho_v002 fuan at active
 kazuho '……優しさって言葉、知ってますか？'
 window hide None
 show expression "#000" as fade with Dissolve(1.0)
 hide kazuho_v002
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
 camera at reset_shader
 pause 0.0
 show expression 'images/bg/AdvBg_782.png' as bg
 with Dissolve(1.0)
 show erika_v001 sinken_close at mei_center
 with Dissolve(0.5)
 show erika_v001 sinken_close at chara_shake_transform,active
 erika 'うぅ、神社をピカピカにする前に\n気づいていれば、こんな余計な\n苦労をしなくてすんだのに……！'
 show erika_v001 sinken at active
 erika 'しかも、おまけに！\nそう言ったら、あのボサボサ頭の小娘！'
 show erika_v001 sinken at active
 erika '「むしろ終わるまで、どうして\n気がつかなかったんですか？」……とか、\n可哀想なものを見る目で言い放ちやがって！！！'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.1
 pause 0.5
 show erika_v001 sinken at jump_transform,active
 erika 'だって仕方ないじゃないですか！\n万が一どころか、億が一、\nいや兆が一、京が一、垓が一！'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.2
 pause 0.5
 show erika_v001 sinken at active
 erika '砂塵のように小さくとも、\n古手梨花が我が主の可能性があるなら！'
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
 show erika_v001 sinken at active
 erika '神社を掃除しないわけには\nいかないじゃないですかぁぁあぁあああ！！！'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 show erika_v001 sinken_close at active
 erika 'はー、はー、はー……。'
 show erika_v001 normal_close at active
 erika 'ふー……。'
 show erika_v001 normal at active
 erika 'しかし、勢い余って飛び出したせいで\n肝心のターゲットの居場所を\n聞くのを忘れてしまいました。'
 show erika_v001 sinken at active
 erika 'あてどなく歩いても、山！\u3000森！\u3000田んぼ！\n本ッ当にこれだから田舎は嫌なんです！'
 show erika_v001 normal_close at active
 erika '……はぁ。というかあの小娘、誰の許可を取って\n我が主に似た姿を取っていたんでしょうか。\n今度会ったら、キッチリと問いたださねば。'
 show erika_v001 normal at active
 erika 'ん？\u3000あそこを歩いているのは……。'
 hide erika_v001
 with Dissolve(0.2)
 Character('Furude Rika',ctc="ctcArrow", ctc_position="fixed") '…………。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 sinken at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show erika_v001 sinken at active
 erika 'ちょっと、古手梨花！'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 Character('Furude Rika',ctc="ctcArrow", ctc_position="fixed") '…………？'
 show erika_v001 sinken at mei_center
 with Dissolve(0.5)
 show erika_v001 sinken at active
 erika 'なんですか、その不思議そうな間抜け面は。\nあんたのことですよ。'
 show erika_v001 normal_close at active
 erika 'さっきは言い忘れていましたが、\n私は人を探していたんです。'
 show erika_v001 normal at active
 erika 'とても生意気な小娘で、名前は……ん？'
 stop music fadeout 0.5
 hide erika_v001
 with Dissolve(0.2)
 Character('Furude Rika',ctc="ctcArrow", ctc_position="fixed") 'くす……くすくす。'
 show erika_v001 sinken at mei_center
 with Dissolve(0.5)
 show erika_v001 sinken at active
 erika 'なにがおかしいんですか、古手梨花。'
 play music 'audio/bgm/BGM_QUEST1_COLLAB2.flac'
 show erika_v001 sinken_close at active
 erika 'ん？\u3000……古手梨花？\nフルデ……ん？\u3000んんっ？'
 hide erika_v001
 with Dissolve(0.2)
 Character('Furude Rika',ctc="ctcArrow", ctc_position="fixed") 'くすくす……おかしいに決まっているじゃない。'
 Character('Furude Rika',ctc="ctcArrow", ctc_position="fixed") 'あんたの姿が見えないから、\nわざわざこの姿になって\n様子を見に来てあげたのよ。'
 Character('Furude Rika',ctc="ctcArrow", ctc_position="fixed") '恩を仇で返すことにしたってわけね。\nいい趣味じゃない。'
 Character('Furude Rika',ctc="ctcArrow", ctc_position="fixed") 'あんたにしてはなかなか面白いことするわね。\n悪くない、えぇ悪くないわ……ふふふふ……。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 odoroki at active
 erika 'えっ、あっ……えっ？\nま、まさか……？！'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 Character('Furude Rika',ctc="ctcArrow", ctc_position="fixed") 'ピクニックだって、クマが\n出る場所にいくのは馬鹿がすることだわ？\nそれと同じよ……くすくす。'
 Character('Furude Rika',ctc="ctcArrow", ctc_position="fixed") 'でも、駄目よ？あんたは私の駒。\n歯向かっていい相手は選ぶべきだったわね……？'
 show erika_v001 odoroki at mei_center
 with Dissolve(0.5)
 show erika_v001 odoroki at chara_shake_transform,active
 erika 'あ、あんた……い、いえ……！\nあなたは、あなた様は……！'
 hide erika_v001
 with Dissolve(0.2)
 Character('Furude Rika',ctc="ctcArrow", ctc_position="fixed") 'あんたがいつまでたっても戻ってこないから、\n何をしているのか暇潰しがてら、この私が\nわざわざ見に来てあげたっていうのに……。'
 Character('Furude Rika',ctc="ctcArrow", ctc_position="fixed") 'あんたが珍しいことをするから、最初は\n面白かったけど、目に余るわね。別に私はあんたなんて\nいらなくてもいいのよ……くすくすくすくす！！'
 show erika_v001 odoroki at mei_center
 with Dissolve(0.5)
 camera at screenshake_transform
 pause 0.0
 show erika_v001 odoroki at active
 erika 'あ、あぁっ、ぁっ……\nあなた様は、我が、主……？'
 hide erika_v001
 with Dissolve(0.2)
 Character('????',ctc="ctcArrow", ctc_position="fixed") '正解よ…………くすくす。\nまぁ、タイムオーバーだけど？'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show erika_v001 odoroki at active
 erika 'あ、あぁ、…………あ。\nぁぁああーーーーーーーっ？！？！！？！'
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
 play music 'audio/bgm/BGM_QUEST11_COLLAB2.flac'
 show expression 'images/bg/AdvBg_2190.png' as bg
 with Dissolve(1.0)
 show beatrice_v001 smile at mei_left
 with Dissolve(0.5)
 show beatrice_v001 smile at active
 beatrice 'うーむ、派手にやっておるなぁ。'
 show beatrice_v001 smile at active
 beatrice 'しかし、ヱリカも\n疲弊から来る思考能力の低下への抵抗力は\n持ち合わせていなかったようであるな。'
 show beatrice_v001 smile_close at active
 beatrice 'それにしても、貴殿には助けられたな……\nドラノール。'
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show beatrice_v001 smile_close at inactive
 dlanor 'イイエ。たいしたことはしていマセン。'
 show beatrice_v001 normal at active
 show dlanor_v001 normal at inactive
 beatrice '謙遜だな。そなたからの連絡がなければ、\nあやつの「目標」を先回りして我が領土に避難、\n保護することはできなかった。'
 show beatrice_v001 smile at active
 show dlanor_v001 normal at inactive
 beatrice '今頃、あの人物は忘れているであろうが……\nなかなか楽しいティーパーティーであったぞ。'
 show dlanor_v001 normal_close at active
 show beatrice_v001 smile at inactive
 dlanor '一方的に戦うことを強制するのは、\n私の立場からも友の立場からも\n許容できることではありマセン。'
 show dlanor_v001 normal at active
 show beatrice_v001 smile at inactive
 dlanor '……お茶、ごちそうさまデシタ。\nミステリー談義も、大変有意義デシタ。'
 show beatrice_v001 smile at active
 show dlanor_v001 normal at inactive
 beatrice 'うむ。満足のいく時間を過ごせたなら何よりだ。'
 show beatrice_v001 fuan at active
 show dlanor_v001 normal at inactive
 beatrice 'にしても、ヱリカはいいのか？\nなかなかの仕置きを受けているようであるが。'
 show dlanor_v001 normal_close at active
 show beatrice_v001 fuan at inactive
 dlanor '大丈夫デス。おそらくですが、あのまま\nヱリカが見捨てられることはないデショウ。'
 show beatrice_v001 futeki at active
 show dlanor_v001 normal_close at inactive
 beatrice 'くっくっくっ……ドラノールもそう思うか。'
 show dlanor_v001 normal at active
 show beatrice_v001 futeki at inactive
 dlanor 'ハイ。きっと戻って来るでショウ。'
 show dlanor_v001 normal at active
 show beatrice_v001 futeki at inactive
 dlanor 'それに、「彼女」との再戦は……\nもっときちんとしたルールの下で\n行われるべきデス。'
 show dlanor_v001 normal at active
 show beatrice_v001 futeki at inactive
 dlanor 'あの存在の出自がどうであれ、\nミステリーに対して真摯かつ虚心な姿勢で\n臨まれる姿勢、好感が持てマシタ。'
 show beatrice_v001 futeki at active
 show dlanor_v001 normal at inactive
 beatrice 'くっくっくっ、その通りだ……！'
 show beatrice_v001 normal at active
 show dlanor_v001 normal at inactive
 beatrice 'それにしても、そなたがヱリカの\n友である理由は何だ？\nやはり、自分にはないものに惹かれると？'
 show dlanor_v001 normal_close at active
 show beatrice_v001 normal at inactive
 dlanor '……どう取っていただいてもかまいマセン。\nでは、私はこれで失礼しようと思いマス。'
 show beatrice_v001 smile at active
 show dlanor_v001 normal_close at inactive
 beatrice '迎えに行くのか？'
 show dlanor_v001 normal at active
 show beatrice_v001 smile at inactive
 dlanor 'ハイ。どうもこちらの盤に\n戻っているようなノデ。'
 show dlanor_v001 normal_close at active
 show beatrice_v001 smile at inactive
 dlanor '…………。'
 show beatrice_v001 normal at active
 show dlanor_v001 normal_close at inactive
 beatrice 'ドラノール？\u3000いかがしたか？'
 show dlanor_v001 smile at active
 show beatrice_v001 normal at inactive
 dlanor '……クッキー、おいしかったデス。\nまた、来てもいいデスカ？'
 show beatrice_v001 smile at active
 show dlanor_v001 smile at inactive
 beatrice '無論。次はヱリカを誘って来るがいい。'
 show beatrice_v001 smile at active
 show dlanor_v001 smile at inactive
 beatrice '妾はいつだって、そなたらを歓迎しようぞ。'
 show dlanor_v001 smile_close at active
 show beatrice_v001 smile at inactive
 dlanor '……感謝します、ベアトリーチェ。'
 hide dlanor_v001
 with Dissolve(0.6)
 show beatrice_v001 smile_close at active
 beatrice 'ふっ。ヱリカが恵まれているとは\nとても言えぬが……。'
 show beatrice_v001 smile at active
 beatrice 'どうやら、友には恵まれたようであるな。'
 return