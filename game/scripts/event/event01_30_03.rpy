label event01_30_03:
 stop sound
 scene expression "#000"
 play music 'audio/bgm/BGM_QUEST2_COLLAB2.wav'
 show expression 'images/bg/AdvBg_2281.png' as bg
 with Dissolve(1.0)
 narrator '\u3000ほんの１０分くらい目を瞑るだけ……、と思っていたのに、案の\n定、かなり眠ってしまっていたようだ。'
 play audio 'audio/sfx/SE_5037_getup.wav'
 narrator '\u3000魅音さんと詩音さんも眠っていたが、あたしがもぞもぞと起き上\nがる気配で目が覚めたようだった。'
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 nao '……いっけない。さすがに寝すぎたかも。……かも。'
 hide nao_v002
 with Dissolve(0.2)
 show shion_v002 fuan_close at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at deepbreath_transform,active
 show shion_v002 fuan_close at inactive
 mion 'ふぁ～～あぁ！\u3000よっく寝たぁ。おじさん、元気チャージ\n１２０％！'
 show shion_v002 odoroki at active
 show mion_v002 smile at inactive
 shion '今、何時ですか？\u3000え、もう午後６時過ぎなんですか。'
 show mion_v002 smile at active
 show shion_v002 odoroki at inactive
 mion '雨も止んでるね。これは明日は、最高の撮影日和になるよ！'
 hide shion_v002
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show mion_v002 smile at inactive
 nao '……窓の鍵。直ったんですか？'
 show mion_v002 smile at active
 show nao_v002 normal at inactive
 mion 'ん？\u3000えへへ～………。'
 hide nao_v002
 show shion_v002 fuan at mei_left
 with Dissolve(0.5)
 show shion_v002 fuan at active
 show mion_v002 smile at inactive
 shion '無理でした。後で使用人さんに謝って下さい。'
 show mion_v002 fuan_close at active
 show mion_v002 fuan_close:
  linear 0.5 pos (1440,1250)
 show shion_v002 fuan at inactive
 pause 0.5
 mion 'はあい……。'
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 narrator '\u3000その時、部屋に置かれた内線電話が鳴った。'
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_521_phone_pickup.wav'
 show nao_v002 normal at active
 nao 'あ、えっと、はい、もしもしっ。'
 hide nao_v002
 with Dissolve(0.2)
 Character('Phone',ctc="ctcArrow", ctc_position="fixed") '『お寛ぎ中、失礼致します。お夕食の準備が整いました。下の広間\nにお越し下さいませ』'
 show nao_v002 smile at mei_center
 with Dissolve(0.5)
 show nao_v002 smile at active
 nao 'はい。すぐにお伺いします。'
 hide nao_v002
 with Dissolve(0.2)
 show mion_v002 smile at mei_right
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion '行きますよ、お姉。ディナーは少しは上品にして下さいよ？'
 show mion_v002 smile at active
 show shion_v002 smile at inactive
 mion 'ハイハイ。じゃないと、魔女に祟られちゃうからね～。'
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao '…………………。'
 window hide None
 show expression "#000" as fade with Dissolve(1.0)
 hide nao_v002
 with Dissolve(0.2)
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2371.png' as bg
 with Dissolve(1.0)
 narrator '\u3000せっかく忘れてたのに。……魔女の怪談を、また思い出してしま\nう。\n\u3000でも、昼寝できて頭もスッキリした。'
 narrator '\u3000自慢のディナーをいただけば、あたしも元気チャージ１２０％\nで、明日からは気分を入れ替えて機嫌よく過ごせそうだ。'
 play audio 'audio/sfx/SE_5034_knock.wav'
 narrator '\u3000下へ降りる前に、隣のヱリカさんの部屋もノックする。'
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao 'ヱリカさん。お夕食だそうですけど、一緒に降りませんか？'
 hide nao_v002
 with Dissolve(0.2)
 erika '……先に行っててください。髪の毛が整わなくって……。'
 narrator '\u3000扉越しに、あの長いツインテールと格闘しているだろう唸り声が\n聞こえる。'
 narrator '\u3000あれだけの長さの髪って、ちょっと憧れるけど、やっぱりお手入\nれは大変ね……。'
 show shion_v002 smile at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at active
 show shion_v002 smile at inactive
 mion 'うわ、もういい匂いがするよ～！'
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion '#p雛見沢#sひなみざわ#rではなかなか嗅げない匂いですねぇ。'
 hide shion_v002
 show nao_v002 smile at mei_left
 with Dissolve(0.5)
 show nao_v002 smile at active
 show mion_v002 smile at inactive
 nao 'ランチの時点で期待値が最高だから、ディナーもすっごく楽しみで\nす。'
 show mion_v002 smile at jump_transform,active
 show nao_v002 smile at inactive
 mion 'やっぱり、ご飯は大事だよねぇ！'
 window hide None
 show expression "#000" as fade with Dissolve(1.0)
 hide mion_v002
 hide nao_v002
 with Dissolve(0.2)
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2331.png' as bg
 with Dissolve(1.0)
 show shannon_v001 smile at mei_center
 with Dissolve(0.5)
 show shannon_v001 smile at active
 shannon '皆様。お待たせいたしました。お席へご案内致します。'
 hide shannon_v001
 with Dissolve(0.2)
 narrator '\u3000純白のテーブルクロスの上には、見るだけでも満たされそうな、\n美しい盛り付けのフランス料理が……。'
 show shannon_v001 smile at mei_center
 with Dissolve(0.5)
 show shannon_v001 smile at active
 shannon '当家の料理長、郷田が腕によりを掛けました、創作スペイン料理で\nございます。'
 hide shannon_v001
 with Dissolve(0.2)
 show nao_v002 fuan_close at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan_close at active
 nao '……スペインはフランスの隣よね。……セーフセーフ……。'
 hide nao_v002
 with Dissolve(0.2)
 Character('Gohda',ctc="ctcArrow", ctc_position="fixed") 'はて。……ヱリカさまは、まだお部屋でしょうか？'
 narrator '\u3000郷田さんにとっては、自分の作った料理の紹介をする時が最高の\nひと時なのだろう。'
 narrator '\u3000その最高のひと時には、全員が着席していて欲しい。ヱリカさん\nがまだ来ていないのが気になっているようだった。'
 narrator '\u3000だが、ヱリカさんを待っていたら、料理の一番の食べ頃を逃して\nしまう。'
 narrator '\u3000郷田さんは咳払いをしてから、今夜の料理の説明を始めるのだっ\nた。'
 narrator '\u3000繊細な前菜、そして優しい味のスープを味わい終えた頃、ようや\nくヱリカさんが階段を降りて来た。'
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika 'お待たせして申し訳ありません。'
 hide erika_v001
 with Dissolve(0.2)
 Character('Gohda',ctc="ctcArrow", ctc_position="fixed") 'いえいえ、とんでもない！\u3000さぁ、どうぞ。御着席を！'
 show shannon_v001 smile at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show shannon_v001 smile at inactive
 erika 'あ、私、マイ箸があるので、シルバーは下げてもらって結構です。'
 show shannon_v001 fuan at active
 show erika_v001 normal at inactive
 shannon 'し、しかし……。スープをお箸では……。'
 show erika_v001 smile at active
 show shannon_v001 fuan at inactive
 erika 'ヱリカ流お箸術を見くびっていますね？\u3000箸でスープをいただく秘\n技！\u3000ご披露させていただきますっ。'
 hide shannon_v001
 hide erika_v001
 with Dissolve(0.2)
 narrator '\u3000何それ。超見たい。'
 narrator '\u3000ヱリカさんという人は、直接の関わりなく遠くから見ている分に\nは、とても面白い人なのかもしれない。'
 window hide None
 stop music fadeout 2.0
 pause 6.0
 play music 'audio/bgm/BGM_GACHA_COLLAB2.wav'
 narrator '\u3000食後は、そのままテレビの前のソファーに移り、みんなでのんび\nりした。'
 narrator '\u3000心地よい満腹感は、今日一日、大したことはしていないはずなの\nに、今日もがんばったかのような不思議な気持ちにさせてくれる。'
 narrator '\u3000テレビはもちろん『名探偵ワニャン』。\n\u3000あたしが見てた頃から、ずいぶん登場人物が増えている。'
 narrator '\u3000というか、この世界の警察は、どうして殺人事件の現場に、小学\n生やら巨大ナメクジやらを自由に立ち入らせるのだろう？？'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide fade with Dissolve(0.08333333333333333)
 show mion_v002 sinken at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show mion_v002 sinken at active
 mion 'いやいやいやいや！\u3000まだ言い逃れは出来たでしょ！\u3000犯人、屈す\nるの早ぁい！'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide mion_v002
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika 'ミステリーは、知的パズルではありますが、時に肉体的な格闘技の\n一面もあります。'
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at active
 show erika_v001 normal at inactive
 shion '確かに。結局のところ、証拠の数々はパンチみたいなもんですし\nね。いくら突きつけられても、堪えることは可能ですし。'
 hide erika_v001
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at active
 show shion_v002 smile at inactive
 mion '詩音、昔っからそういうのの往生際、悪いもんねぇ。'
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 show erika_v001 normal_close at mei_center
 with Dissolve(0.5)
 show erika_v001 normal_close at active
 erika 'くす。まぁ、往生際の悪い犯人というのは、ミステリー的に、見て\nいて愉快ではありませんが。'
 show erika_v001 normal at active
 erika '私くらいになると、……多少はタフな方が、打ち込み甲斐があると\nいうものです。くすくす。'
 hide erika_v001
 with Dissolve(0.2)
 narrator '\u3000ちぇ。……みんなも『カネダ少年の事件簿』、見て欲しいものだ\nわ。すっごい面白いのに。'
 narrator '\u3000疎外感というか、天邪鬼な気分というか。……みんなの輪に入り\n損ねる。'
 narrator '\u3000あたしはソファーを立つ。\n\u3000カウンターテーブルの向こうで、後片付けをしている紗音さんが\nいた。'
 play audio 'audio/sfx/SE_515_tableware.wav'
 show nao_v002 smile at mei_left
 show shannon_v001 smile at mei_right
 with Dissolve(0.5)
 show shannon_v001 smile at active
 show nao_v002 smile at inactive
 shannon '何か、お飲み物をお作りしましょうか……？'
 show nao_v002 smile at active
 show shannon_v001 smile at inactive
 nao 'あ、いえ。もうたくさんいただきましたので。'
 show shannon_v001 smile at active
 show nao_v002 smile at inactive
 shannon '名探偵ワニャン、面白いですよね。'
 show shannon_v001 fuan at active
 show nao_v002 smile at inactive
 shannon '私も他の使用人の人にも勧めてるんですけど、みんな読んでくれな\nくて……。'
 show nao_v002 fuan at active
 show shannon_v001 fuan at inactive
 nao '……あなたもワニャン派ですか。……映画は見ましたか？'
 show shannon_v001 smile at active
 show nao_v002 fuan at inactive
 shannon 'もちろん！\u3000東京の大きな映画館で観ました♪'
 show nao_v002 normal at active
 show shannon_v001 smile at inactive
 nao '……カネダ少年の事件簿は読んでる？'
 show shannon_v001 smile at nod_transform,active
 show nao_v002 normal at inactive
 shannon 'えぇ、そちらも大好きです。結構、ハードだけど、そこがいいです\nよね。'
 hide nao_v002
 hide shannon_v001
 with Dissolve(0.2)
 narrator '\u3000しゃ、紗音さん………。'
 show shannon_v001 smile at mei_right
 show nao_v002 smile at mei_left
 with Dissolve(0.5)
 show nao_v002 smile at active
 show shannon_v001 smile at inactive
 nao '……一杯もらえるかしら。赤コーラ、炭酸砂糖マシマシで。'
 show shannon_v001 smile_close at active
 show nao_v002 smile at inactive
 shannon 'くす。かしこまりました。'
 show nao_v002 normal at active
 show shannon_v001 smile_close at inactive
 nao '……………………。'
 show nao_v002 normal at active
 show shannon_v001 smile_close at inactive
 nao '……えっと、……紗音さん。ここだけの話なんだけれど、……いい\nですか？'
 show shannon_v001 smile at active
 show nao_v002 normal at inactive
 shannon 'はい………？'
 play sound ['audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav'] fadeout 1.0
 stop music fadeout 2.0
 show nao_v002 fuan at active
 show shannon_v001 smile at inactive
 nao '……朱志香さんたちに、この島には魔女のオバケが出るって脅され\nたんですけど。'
 show shannon_v001 normal at active
 show nao_v002 fuan at inactive
 shannon '魔女の、オバケ……、ですか……？'
 hide shannon_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator '\u3000きょとんとした顔。……うん、その反応でいいの。'
 narrator '\u3000ベアトリーチェという魔女は“い”ると、みんなに寄ってたかっ\nて言われた。'
 narrator '\u3000普段なら、あたしだって空気は読む。サンタクロースの存在を、\nむやみやたらに否定したりはしない。'
 narrator '\u3000……でも、天邪鬼な自分の性分というか。\n\u3000寄ってたかって、ベアトリーチェは“い”る、なんて言われる\nと、じゃあ証拠を見せろと言いたくなってしまうのだ。'
 narrator '\u3000……証拠？\u3000………冗談じゃない。\n\u3000あたしはこの島でのんびりしたいだけなのに、……どうしてこん\nなことに。'
 show shannon_v001 smile at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show shannon_v001 smile at inactive
 nao 'やっぱり紗音さんも、……信じてるんですか？\u3000ベアトリーチェ。'
 show shannon_v001 smile_close at active
 show nao_v002 normal at inactive
 shannon 'はい。……“い”ますよ。ベアトリーチェさまは。'
 show nao_v002 normal at active
 show shannon_v001 smile_close at inactive
 nao 'いるって、どこに？'
 show shannon_v001 smile at active
 show nao_v002 normal at inactive
 shannon '今、ここにも、きっと“い”ますよ。'
 play music 'audio/bgm/BGM_QUEST7_COLLAB2.wav'
 hide shannon_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator '\u3000紗音さんはにっこりと微笑みながら答えるのだが……、むしろ薄\n気味悪く感じられた。'
 show shannon_v001 smile at mei_right
 show nao_v002 sinken at mei_left
 with Dissolve(0.5)
 show nao_v002 sinken at active
 show shannon_v001 smile at inactive
 nao 'いるなら、堂々と出て来ればいいんだわ。'
 show nao_v002 normal at active
 show shannon_v001 smile at inactive
 nao '勿体ぶって、姿を見せるのを出し惜しみするから、薄気味悪くなっ\nちゃうんです。'
 show shannon_v001 normal_close at active
 show nao_v002 normal at inactive
 shannon '……反魔法の毒素、というものがあるそうです。'
 show nao_v002 odoroki at active
 show shannon_v001 normal_close at inactive
 nao '反魔法の、毒素って……？'
 show shannon_v001 normal at active
 show nao_v002 odoroki at inactive
 shannon '何でも、魔法や魔女を信じないニンゲンからは、……魔女にとって\n有害な、毒素が出ているのだとか。'
 show nao_v002 normal at active
 show shannon_v001 normal at inactive
 nao 'つまり……、ベアトリーチェを信じない人間には、ベアトリーチェ\nは近付けないということ？'
 show nao_v002 smile at active
 show shannon_v001 normal at inactive
 nao 'それならかえって安心だわ。信じない人の前には現れないんだも\nの。'
 hide shannon_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator '\u3000信じる人の前にしか現れないというなら、サンタと同じだ。会い\nたくない人は、会わずに済む……。'
 show nao_v002 smile at mei_left
 show shannon_v001 fuan at mei_right
 with Dissolve(0.5)
 show shannon_v001 fuan at active
 show nao_v002 smile at inactive
 shannon 'それが、むしろ逆なんです。'
 show nao_v002 fuan at active
 show shannon_v001 fuan at inactive
 nao 'え……？'
 show shannon_v001 normal_close at active
 show nao_v002 fuan at inactive
 shannon 'ベアトリーチェさまは、自分の存在を信じてくれない人には、敵意\nを持ちます。'
 show shannon_v001 normal at active
 show nao_v002 fuan at inactive
 shannon '自分が確かに存在することを示そうと、不思議な悪戯をしたり、脅\nかせたり……。'
 show nao_v002 normal at active
 show shannon_v001 normal at inactive
 nao '嘉音さんに聞いたわ。誰も入れないはずの部屋に、不気味な魔法陣\nを描いたりするんでしょう？'
 hide nao_v002
 hide shannon_v001
 with Dissolve(0.2)
 narrator '\u3000紗音さんの顔が一瞬、曇った。\n\u3000唐突に不謹慎なことを言われて驚いた、というようにも見えた\nし、……口にした私を咎めるというようにも見えた。'
 show shannon_v001 fuan at mei_center
 with Dissolve(0.5)
 show shannon_v001 fuan at active
 shannon '菜央さま……。そのようなことはあまり口に、'
 play audio 'audio/sfx/SE_5029_slap_back.wav'
 pause 1.0
 play music 'audio/bgm/BGM_HOME_COLLAB2.wav'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide shannon_v001
 hide fade with Dissolve(0.08333333333333333)
 show jessica_v001 smile at mei_center
 with Dissolve(0.08333333333333333)
 show jessica_v001 smile at active
 jessica 'こんばんは～～！！\u3000あっそびに来たぜ～～！！'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide jessica_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 narrator '\u3000元気よく、何かを抱えた朱志香さんがやってきた。'
 narrator '\u3000私たちにとってのバカンスも、朱志香さんには、友達が泊まりに\n来てくれたようなものなのだろう。'
 show jessica_v001 smile at mei_right
 show mion_v002 odoroki at mei_left
 with Dissolve(0.5)
 show mion_v002 odoroki at active
 show jessica_v001 smile at inactive
 mion 'あれ？！\u3000その小脇に抱えてるのはひょっとしてぇ？！'
 show jessica_v001 futeki at active
 show mion_v002 odoroki at inactive
 jessica 'いつか、こんな日も来るかと思ってさぁ！\u3000何年も前に買ったの\nに、ようやく遊べる日が来たぜ……！'
 hide mion_v002
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at active
 show jessica_v001 futeki at inactive
 shion 'おやまぁ。お姉の前にボドゲを持ってくるなんて、大変なことにな\nりますよ？'
 hide jessica_v001
 hide shion_v002
 with Dissolve(0.2)
 show erika_v001 normal at mei_right
 show mion_v002 smile at mei_left
 with Dissolve(0.5)
 show mion_v002 smile at updown_shake_transform,active
 show erika_v001 normal at inactive
 mion 'やろうやろう、みんなでやろう！\u3000ヱリカさんも一緒にどう？'
 show erika_v001 normal_close at active
 show mion_v002 smile at inactive
 erika '私は部屋でのんびりと過ごそうかと。'
 show mion_v002 futeki at active
 show erika_v001 normal_close at inactive
 mion 'あれぇ？\u3000逃げちゃうぅ？\u3000ボードゲームはね、人と人の頭脳のぶ\nつかり合い！'
 show mion_v002 futeki_close at active
 show erika_v001 normal_close at inactive
 mion 'まぁ、私の頭脳には勝ち目がないだろうからね。逃げちゃうのもア\nリかもねぇ～？'
 show erika_v001 normal at active
 show mion_v002 futeki_close at inactive
 erika '……ふっ。安い挑発ですが、そこまで言われては受けて立たない訳\nにはいきませんね。'
 hide mion_v002
 show shion_v002 fuan at mei_left
 with Dissolve(0.5)
 show shion_v002 fuan at active
 show erika_v001 normal at inactive
 shion 'いいんですか？\u3000お姉との勝負には一切の言い訳は通用しません\nよ？'
 hide erika_v001
 hide shion_v002
 with Dissolve(0.2)
 show nao_v002 normal at mei_left
 show jessica_v001 smile at mei_right
 with Dissolve(0.5)
 show jessica_v001 smile at active
 show nao_v002 normal at inactive
 jessica '魅音さんって、ボドゲに詳しいの？'
 show nao_v002 fuan at active
 show jessica_v001 smile at inactive
 nao '……ボドゲに限らず、勝負事となれば、水を得た魚も同然です。'
 play audio 'audio/sfx/SE_226_shine.wav'
 show jessica_v001 futeki at jump_transform,active
 show nao_v002 fuan at inactive
 jessica 'そりゃいいぜ！\u3000私も、こう見えても右代宮金蔵の孫だ！\u3000勝負\n事、大いに望むところだぜ！'
 hide nao_v002
 hide jessica_v001
 with Dissolve(0.2)
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at active
 mion 'みんなでやろうよ！\u3000私、詩音、ヱリカさんに朱志香さん。菜央\nちゃんも紗音さんも一緒にやろうよ！'
 show shannon_v001 smile at mei_left
 with Dissolve(0.5)
 show shannon_v001 smile at active
 show mion_v002 smile at inactive
 shannon 'お気持ちだけ頂戴させていただきます。お屋敷の方で、まだお仕事\nがありますので……。'
 show shannon_v001 smile_close at active
 show mion_v002 smile at inactive
 shannon 'それでは、本日は失礼させていただきます……。'
 hide mion_v002
 hide shannon_v001
 with Dissolve(0.2)
 narrator '\u3000紗音さんはペコリと会釈してから踵を返そうとする。'
 show mion_v002 smile at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show mion_v002 smile at inactive
 nao '魅音さん。窓の鍵の話、しました？'
 show mion_v002 fuan at chara_shake_transform,active
 show nao_v002 normal at inactive
 mion 'ぎくぅ。'
 hide nao_v002
 show shion_v002 normal at mei_left
 with Dissolve(0.5)
 show shion_v002 normal at active
 show mion_v002 fuan at inactive
 shion 'お姉。こういうのは先に謝るのが筋ですよ？'
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show shannon_v001 normal at mei_left
 with Dissolve(0.5)
 show shannon_v001 normal at active
 shannon '何の話でしょう……？'
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show shannon_v001 normal at inactive
 erika 'あぁ、……窓の。くす。'
 show erika_v001 normal at active
 show shannon_v001 normal at inactive
 erika '外界から隔離された島ではありますが、窓とはいえ、女子の部屋の\n鍵がかからないのは気持ちのよいことではありませんね。'
 hide shannon_v001
 show jessica_v001 smile at mei_left
 with Dissolve(0.5)
 show jessica_v001 smile at active
 show erika_v001 normal at inactive
 jessica 'あぁ、ひょっとして窓の鍵？\u3000あれ、古いからちょっとコツがいる\nんだぜ。'
 hide erika_v001
 show mion_v002 fuan at mei_right
 with Dissolve(0.5)
 show mion_v002 fuan at active
 show jessica_v001 smile at inactive
 mion 'いやぁ……、素敵なお部屋に興奮して、思い切り窓を開ける\n時、……ちょっと鍵を強引に……。'
 hide jessica_v001
 hide mion_v002
 with Dissolve(0.2)
 show nao_v002 fuan at mei_left
 show shion_v002 fuan_close at mei_right
 with Dissolve(0.5)
 show shion_v002 fuan_close at active
 show nao_v002 fuan at inactive
 shion '田舎者のお姉で本当にすみません。'
 show nao_v002 fuan at active
 show shion_v002 fuan_close at inactive
 nao '田舎者の魅音さんで本当にすみません。……見てもらうことは出来\nますでしょうか。'
 hide nao_v002
 hide shion_v002
 with Dissolve(0.2)
 show shannon_v001 smile at mei_left
 show jessica_v001 smile at mei_right
 with Dissolve(0.5)
 show jessica_v001 smile at active
 show shannon_v001 smile at inactive
 jessica '紗音、ちょっと見てきてよ。'
 show shannon_v001 smile at active
 show jessica_v001 smile at inactive
 shannon '畏まりました……。'
 hide shannon_v001
 hide jessica_v001
 with Dissolve(0.2)
 show mion_v002 smile at mei_center
 with Dissolve(0.5)
 show mion_v002 smile at active
 mion 'よおッし、やろやろやろ！！\u3000このゲームはね、要は最後まで生き\n残った人が勝ちってタイプでぇ！'
 hide mion_v002
 with Dissolve(0.2)
 show jessica_v001 smile at mei_right
 show nao_v002 smile at mei_left
 with Dissolve(0.5)
 show nao_v002 smile at active
 show jessica_v001 smile at inactive
 nao '魅音さんとゲームをする時には、まず罰ゲームの確認が必要ですよ\nね。'
 show jessica_v001 smile at active
 show nao_v002 smile at inactive
 jessica 'え？！\u3000何々？！\u3000罰ゲームとか賭けちゃう？！\u3000リスクがある方\nが燃えるのが右代宮の血だぜ！'
 hide jessica_v001
 hide nao_v002
 with Dissolve(0.2)
 show shion_v002 smile at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show shion_v002 smile at inactive
 erika 'どうせ勝つのは私ですから。せいぜい、自分が被ってもマシな罰ゲ\nームに決めて下さいね。'
 show shion_v002 smile at active
 show erika_v001 normal at inactive
 shion 'ヱリカさん、あまりお姉を舐めない方がいいですよ？\u3000この人は、\n勝つ為なら何でもありですので。'
 hide shion_v002
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at active
 show erika_v001 normal at inactive
 nao '……とりあえず、爆発とかトラップとか、身体に危害が及ばないゲ\nームだと嬉しいわ。'
 show erika_v001 normal_close at active
 show nao_v002 fuan at inactive
 erika 'おやおや。罰ゲーム以前に、スリリングなゲームになりそうです\nね。くっくっくっく！'
 hide erika_v001
 hide nao_v002
 with Dissolve(0.2)
 show jessica_v001 odoroki at mei_center
 with Dissolve(0.5)
 show jessica_v001 odoroki at active
 jessica 'お、おかしーぜ。このゲームって、そんなヤバイゲームだったっ\nけ……。'
 hide jessica_v001
 with Dissolve(0.2)
 narrator '\u3000魅音さんにかかれば、どんな遊びも即座に闇のゲームに早変わり\nだ……。'
 narrator '\u3000初日の夜から屈辱の涙で枕を濡らしたくなどない。みんなで真剣\nにルールを確認するのだった。'
 play audio 'audio/sfx/SE_526_door_open.wav'
 pause 1.0
 show shannon_v001 smile at mei_center
 with Dissolve(0.5)
 show shannon_v001 smile at active
 shannon '鍵、直しておきました。'
 hide shannon_v001
 with Dissolve(0.2)
 show nao_v002 odoroki at mei_left
 show mion_v002 odoroki at mei_right
 with Dissolve(0.5)
 show mion_v002 odoroki at active
 show nao_v002 odoroki at inactive
 mion 'え！\u3000すごいあっさり！\u3000今、上に行ったと思ったら、もう！'
 show nao_v002 smile at active
 show mion_v002 odoroki at inactive
 nao 'ですね。でも、これで安心です。ずいぶん簡単に直せましたね。'
 hide nao_v002
 hide mion_v002
 with Dissolve(0.2)
 show shannon_v001 smile at mei_center
 with Dissolve(0.5)
 show shannon_v001 smile at active
 shannon 'コツがあるんです。明日以降は、優しくお取り扱いをいただけます\nと助かります。'
 hide shannon_v001
 with Dissolve(0.2)
 show mion_v002 fuan at mei_right
 show shion_v002 normal at mei_left
 with Dissolve(0.5)
 show shion_v002 normal at active
 show mion_v002 fuan at inactive
 shion 'ですってよ、お姉？\u3000反省して下さいな。'
 show mion_v002 fuan at chara_shake_transform,active
 show shion_v002 normal at inactive
 mion 'お、おじさんはね、力の強いお客のつもりで、モニターでやったん\nだからね！\u3000ホントだからね！！'
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show jessica_v001 smile at mei_right
 show shannon_v001 smile at mei_left
 with Dissolve(0.5)
 show shannon_v001 smile at active
 show jessica_v001 smile at inactive
 shannon 'ふふ。それでは失礼致します。'
 show jessica_v001 smile at active
 show shannon_v001 smile at inactive
 jessica 'ありがとな、紗音！\u3000私がこっちで遊んでること、親には内緒\nな……！'
 show shannon_v001 smile at active
 show jessica_v001 smile at inactive
 shannon 'くす。心得ております。'
 hide jessica_v001
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show shannon_v001 smile at inactive
 erika '紗音さん、ご苦労様です。窓から泥棒が入って、部屋を荒らしたり\nはしていませんでしたか？'
 show shannon_v001 smile_close at active
 show erika_v001 normal at inactive
 shannon 'いいえ。ご安心を。'
 hide shannon_v001
 hide erika_v001
 with Dissolve(0.2)
 narrator '\u3000紗音さんは深々とお辞儀をしてから、屋敷に戻っていった。'
 show mion_v002 smile at mei_right
 show jessica_v001 smile at mei_left
 with Dissolve(0.5)
 show jessica_v001 smile at jump_transform,active
 show mion_v002 smile at inactive
 jessica 'さあ！！\u3000始めようぜ！！'
 play audio 'audio/sfx/SE_226_shine.wav'
 show mion_v002 futeki at active
 show jessica_v001 smile at inactive
 mion 'いいね、その気合、気に入ったぁ！\u3000私たちと朱志香さんで、\n六軒島出張部活ッ五凶爆闘だぁ！！！'
 stop music fadeout 2.0
 window hide None
 hide mion_v002
 hide jessica_v001
 with Dissolve(0.2)
 pause 4.0
 play music 'audio/bgm/BGM_QUEST2_COLLAB2.wav'
 narrator '\u3000初めてプレイするボドゲは、ルールの確認などが伴い、かなりの\n長時間になることが少なくない。'
 show jessica_v001 fuan at mei_center
 with Dissolve(0.5)
 show jessica_v001 fuan at chara_shake_transform,active
 jessica 'ふぁぁあぁぁぁぁ……ぁぁ。'
 hide jessica_v001
 with Dissolve(0.2)
 narrator '\u3000朱志香さんが欠伸をすると、つられてあたしも詩音さんも欠伸を\nする。'
 show mion_v002 normal at mei_right
 show erika_v001 sinken at mei_left
 with Dissolve(0.5)
 show erika_v001 sinken at active
 show mion_v002 normal at inactive
 erika '待ってください。これは“してもよい”、ですよね？\u3000“しなくて\nもよい”訳ですよね？'
 show mion_v002 normal at active
 show erika_v001 sinken at inactive
 mion 'えっとね、待って待って。まず時計回りで徴収を解決してから、次\nに収入の処理を……。'
 hide erika_v001
 show shion_v002 sinken at mei_left
 with Dissolve(0.5)
 show shion_v002 sinken at active
 show mion_v002 normal at inactive
 shion 'お姉、さっき、私の収入を先に処理してから、そこから徴収しまし\nたよね？'
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show jessica_v001 fuan at mei_right
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at active
 show jessica_v001 fuan at inactive
 nao '………何だかすみません。魅音さんたち、ゲームには絶対に手を抜\nけないんです。'
 show jessica_v001 fuan_close at active
 show nao_v002 fuan at inactive
 jessica 'いやぁ……たはは。もっと短く遊べるゲームを持って来ればよかっ\nたぜ……。'
 hide jessica_v001
 hide nao_v002
 with Dissolve(0.2)
 show shion_v002 fuan at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show shion_v002 fuan at inactive
 erika 'あらあら。菜央ちゃまが大あくびをしていますよ。'
 show erika_v001 normal at active
 show shion_v002 fuan at inactive
 erika '確かにもう、お子様が起きているには、少々、遅い時間ですね。'
 show shion_v002 fuan at active
 show erika_v001 normal at inactive
 shion 'ゲームは結果じゃなくて、過程を楽しむものですし。今日はこれで\nお開きにしませんか？'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide shion_v002
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 show mion_v002 sinken at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show mion_v002 sinken at active
 mion 'あーーッ、何それ何それ！！\u3000おじさんが電力を買い占めた途端に\nお開きとか、ずーるーいーッ！！'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide mion_v002
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show jessica_v001 smile at mei_right
 show nao_v002 fuan_close at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan_close at active
 show jessica_v001 smile at inactive
 nao 'もう眠いわ。……シャワーも浴びたいし。'
 show jessica_v001 smile at active
 show nao_v002 fuan_close at inactive
 jessica 'じゃあ、今日はこれでお開き、ってことで！'
 hide jessica_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator '\u3000このまま行くと魅音さんの圧勝になりそうだったので、みんなさ\nりげなくノーゲームにして解散の流れにする。'
 narrator '\u3000何しろ、２位以下に課せられる罰ゲームがあまりに苛烈だったか\nら……。\n\u3000雛見沢っ子でも、……アレは……ちょっと………。'
 window hide None
 show expression "#000" as fade with Dissolve(1.0)
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2371.png' as bg
 with Dissolve(1.0)
 narrator '\u3000朱志香さんは屋敷に帰る。\n\u3000あたしたちは、ぞろぞろと２階へ上がっていく。'
 show erika_v001 normal at mei_right
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at active
 show erika_v001 normal at inactive
 shion 'どうです？\u3000少しは楽しめましたか？\u3000部活式ゲーム。'
 show erika_v001 normal_close at active
 show shion_v002 smile at inactive
 erika 'やはり私には、ダイス等の運がかかわるゲームは苦手なようです。'
 show erika_v001 normal at active
 show shion_v002 smile at inactive
 erika '我が主と違って。望む目が出るまで、永遠に振り直すようなこと\nは、私には出来ませんので。'
 hide erika_v001
 hide shion_v002
 with Dissolve(0.2)
 show nao_v002 fuan at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at active
 show nao_v002 fuan at inactive
 mion '菜央ちゃんも楽しめた？'
 show nao_v002 fuan at active
 show mion_v002 smile at inactive
 nao '……あれが楽しく感じる頃には、実弾入りロシアンルーレットも、\nへらへら笑って出来る気がします。'
 show mion_v002 futeki at active
 show nao_v002 fuan at inactive
 mion '朱志香さんも言ってたでしょ？\u3000リスクの狂気の中にこそハイリ\nターンが潜むって。'
 show mion_v002 smile at updown_shake_transform,active
 show nao_v002 fuan at inactive
 mion 'ここの当主の金蔵さんは、おじさんの部活の狂気を、楽しんでくれ\nるような気がするね。'
 hide nao_v002
 show shion_v002 normal at mei_left
 with Dissolve(0.5)
 show shion_v002 normal at active
 show mion_v002 smile at inactive
 shion 'えっと、鍵は誰が持ってたんでしたっけ？'
 show mion_v002 smile at active
 show shion_v002 normal at inactive
 mion 'おじさんが持ってるよー。今、開けるね～。'
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show nao_v002 smile at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show nao_v002 smile at inactive
 erika 'それでは皆さん。おやすみなさい。'
 show nao_v002 smile at active
 show erika_v001 normal at inactive
 nao 'おやすみなさい。ヱリカさん。'
 play sound ['audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav'] fadeout 1.0
 show erika_v001 normal at active
 show nao_v002 smile at inactive
 erika 'そうそう。菜央ちゃま。'
 show nao_v002 fuan at active
 show erika_v001 normal at inactive
 nao 'その、菜央ちゃまっての、やめてくれませんか……。'
 stop music fadeout 2.0
 show erika_v001 normal at active
 show nao_v002 fuan at inactive
 erika '聞いてましたよ。……さっき、紗音さんと話していたでしょう？'
 show erika_v001 normal at active
 show nao_v002 fuan at inactive
 erika 'ベアトリーチェは、自分を信じない人に、悪戯をするのが大好きだ\nとか……。'
 show erika_v001 normal at active
 show nao_v002 fuan at inactive
 erika '黄金の魔女のことを、あれだけ堂々と、馬鹿馬鹿しいと言い放った\nんですもの。'
 show erika_v001 fuan at active
 show nao_v002 fuan at inactive
 erika '……何か、不気味な悪戯でも、されないといいですねぇ……？'
 show nao_v002 normal_close at active
 show erika_v001 fuan at inactive
 nao 'やっぱりヱリカさんは性悪ですね。……人のこと、子供扱いして。'
 show nao_v002 normal at active
 show erika_v001 fuan at inactive
 nao 'あたし、あんな怪談話に、怯えたりなんかしませんから。'
 show erika_v001 normal_close at active
 show nao_v002 normal at inactive
 erika 'グッド。'
 show erika_v001 normal at active
 show nao_v002 normal at inactive
 erika 'その覚悟、がんばって持ち続けて下さいね？\u3000くすくすくす……。'
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_526_door_open.wav'
 narrator '\u3000ヱリカさんは嫌味な笑いを最後まで向けながら、自分の部屋に消\nえる。'
 narrator '\u3000魅音さんは、ようやくどのポケットにしまっていたか思い出し、\n鍵を開けたところだった。'
 show expression "#000" as fade with Dissolve(1.0)
 mion 'シャワー、誰から使う？'
 shion '菜央さんからでいいんじゃないですか？'
 nao '嬉しいですけど、あたし、ちゃんと湯船にお湯を張りたいです。'
 play audio 'audio/sfx/SE_5004_lightoff.wav'
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2281.png' as bg
 with Dissolve(1.0)
 narrator '\u3000灯りのスイッチを入れる。\n\u3000洋館らしい雰囲気を壊さない、暗めの証明が部屋を照らした。'
 window hide None
 
 show expression "#000" as fade with Dissolve(1.0)
 stop sound
 scene expression "#000"
 play music 'audio/bgm/BGM_QUEST7_COLLAB2.wav'
 show expression 'images/bg/AdvBg_2320.png' as bg
 with Dissolve(2.0)
 pause 2.0
 show expression "#000" as fade with Dissolve(1.0)
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2281.png' as bg
 with Dissolve(1.0)
 show nao_v002 sinken at mei_center
 with Dissolve(0.5)
 camera at screenshake_transform
 pause 0.0
 show nao_v002 sinken at active
 nao 'ッッッ………………………、'
 hide nao_v002
 with Dissolve(0.2)
 show mion_v002 sinken at mei_right
 show shion_v002 odoroki at mei_left
 with Dissolve(0.5)
 show shion_v002 odoroki at jump_transform,active
 show mion_v002 sinken at inactive
 shion 'どうしたんです？\u3000………ひッ？！？！\u3000お、お姉……！！'
 show mion_v002 futeki at active
 show shion_v002 odoroki at inactive
 mion '……やって、……くれるねぇ………。'
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 narrator '\u3000これが……、魔女の存在を認めぬ者への、悪戯。'
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 nao 'ど、………どういうこと…………。'
 hide nao_v002
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_017_TragedyStart.wav'
 narrator '\u3000魅音さんと詩音さんのベッドは、……何事もないのに。\n\u3000あたしのベッドだけが……、#p殺#s・#r#pさ#s・#r#pれ#s・#r#pて#s・#r#pい#s・#r#pる#s・#r……。'
 narrator '\u3000毛布は乱雑に剥ぎ取られて散乱し……、まるで肌のように露出し\nたシーツが……、鮮血に染まっている……。'
 narrator '\u3000違う。ただ染まっているんじゃない。それは………鮮血のような\n赤で描かれていた………。'
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 nao 'ま………………魔法陣………………。'
 play audio 'audio/sfx/SE_325_ls_thunderfall.wav'
 pause 4.0