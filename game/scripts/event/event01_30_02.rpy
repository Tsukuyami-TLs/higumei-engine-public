label event01_30_02:
 stop sound
 scene expression "#000"
 play music 'audio/bgm/BGM_GACHA_COLLAB2.wav'
 show expression 'images/bg/AdvBg_2291.png' as bg
 with Dissolve(1.0)
 show mion_v002 smile at mei_right
 show kanon_v001 normal at mei_left
 with Dissolve(0.5)
 show kanon_v001 normal at active
 show mion_v002 smile at inactive
 kanon '食後は、コーヒーか紅茶のご用意がありますが、如何いたします\nか……？'
 show mion_v002 smile at active
 show kanon_v001 normal at inactive
 mion '口の中が甘ったるくなったからね！\u3000ここは梅塩昆布茶でキュッと\n締めたいんだけど、あるかなぁ？'
 hide mion_v002
 hide kanon_v001
 with Dissolve(0.2)
 show shion_v002 fuan at mei_right
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at active
 show shion_v002 fuan at inactive
 nao 'て、天衣無縫、ここに極まれりだわ……。'
 show shion_v002 fuan at active
 show nao_v002 fuan at inactive
 shion 'ウチの姉が本当にすみません。田舎者なもので……。'
 hide shion_v002
 hide nao_v002
 with Dissolve(0.2)
 show mion_v002 smile at mei_right
 show kanon_v001 normal_close at mei_left
 with Dissolve(0.5)
 show kanon_v001 normal_close at active
 show mion_v002 smile at inactive
 kanon '……お屋敷の方に準備があるかもしれません。お時間をいただけれ\nば、確認いたします。'
 show mion_v002 smile at jump_transform,active
 show kanon_v001 normal_close at inactive
 mion 'あ、ホント？！\u3000ありがと！\u3000じゃあ、お願いしちゃおっかなぁ。'
 show kanon_v001 normal at active
 show mion_v002 smile at inactive
 kanon '……確か、熊沢さんが私物で鯖昆布茶を持っていたような……。'
 play audio 'audio/sfx/SE_530_walk_one.wav'
 hide kanon_v001
 with Dissolve(0.3)
 pause 2.0
 show erika_v001 normal at mei_left
 with Dissolve(0.5)
 show erika_v001 normal at active
 show mion_v002 smile at inactive
 erika '魅音さん、なかなかやりますね。タダで泊まらせてもらう分、きっ\nちりとお仕事をしているようで。'
 play audio 'audio/sfx/SE_226_shine.wav'
 show mion_v002 futeki at active
 show erika_v001 normal at inactive
 mion 'まぁね！\u3000私のこと、さんざん田舎者とか言ってくる、わかってな\nい妹もいるけどさぁ？'
 hide mion_v002
 hide erika_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_left
 show shion_v002 odoroki at mei_right
 with Dissolve(0.5)
 camera at screenshake_transform
 pause 0.0
 show shion_v002 odoroki at active
 show nao_v002 normal at inactive
 shion 'えーーッ？！\u3000今の、モニターとしてサービスを試してたっていう\nんですかぁ？！'
 show nao_v002 normal at active
 show shion_v002 odoroki at inactive
 nao 'た、確かに……。リゾート地にするなら、それなりの賓客が来る\nこともあるわ。'
 show nao_v002 normal_close at active
 show shion_v002 odoroki at inactive
 nao '賓客のささやかな要望に、杓子定規で対応しているようでは、彼ら\nの満足は得られない……。'
 hide nao_v002
 hide shion_v002
 with Dissolve(0.2)
 show mion_v002 smile at mei_right
 show erika_v001 normal at mei_left
 with Dissolve(0.5)
 show erika_v001 normal at active
 show mion_v002 smile at inactive
 erika '今回はたまたま、用意が出来ましたが……。'
 show erika_v001 normal at active
 show mion_v002 smile at inactive
 erika '恐らく、魅音さんが一番、見たかったのは、どうしても用意が出来\nず、客の気分を害さないように、如何に美しく断って見せるか、\nだったのでしょうね。'
 show mion_v002 smile at active
 show erika_v001 normal at inactive
 mion 'でも、嘉音くんの所作は十分、及第点以上だったと思うよ。'
 hide erika_v001
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion '確かに。……少しでも言い淀みがあったら、お客は、困らせてし\nまったと申し訳なく感じてしまいますものね。'
 show mion_v002 smile_close at active
 show shion_v002 smile at inactive
 mion 'どんな無茶ぶりにも、淀みなく、清流のように対応するのがプロ\nフェッショナルってもんなのさ！'
 hide shion_v002
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show mion_v002 smile_close at inactive
 nao '大事なのは、マニュアル外のことが起こっても、涼やかに対応でき\nることって訳ね……。'
 hide mion_v002
 show erika_v001 normal_close at mei_right
 with Dissolve(0.5)
 show erika_v001 normal_close at active
 show nao_v002 normal at inactive
 erika '臨機応変。あるいは、さも想定内の事態であるかのように振舞う。'
 show erika_v001 normal at active
 show nao_v002 normal at inactive
 erika 'ある種のハッタリが大事、ということでもありますね。'
 hide nao_v002
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at active
 show erika_v001 normal at inactive
 shion '確かに、ベテラン感のある店員さんだと、何があっても安心感があ\nりますよね。'
 hide erika_v001
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at nod_transform,active
 show shion_v002 smile at inactive
 mion 'そうそう。逆に、いつもあわあわしている店員さんだと、例えベテ\nランと同じことをしていても、頼りなく感じられてしまう。'
 hide shion_v002
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show mion_v002 smile at inactive
 nao '……堂々とした態度は、お客に信頼感を与え、それ自体が、優れた\nサービスのひとつになるのね。'
 hide mion_v002
 hide nao_v002
 with Dissolve(0.2)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika 'ま。平たく言えば、舐められたらおしまい、ってことです。'
 show erika_v001 normal at active
 erika '古今東西の名探偵たちも、貫禄とリスペクトがあるからこそ、その\n推理に圧倒的な絶対性が宿るのです。'
 show erika_v001 normal_close at active
 erika 'まぁ、十分な貫禄さえあれば、穴だらけの推理でも、犯人が勝手に\n観念することもありますので。'
 hide erika_v001
 with Dissolve(0.2)
 show shion_v002 smile at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at active
 show shion_v002 smile at inactive
 mion '確かにね！\u3000犯人にプレッシャーを与えれば、勝手に自滅してくれ\nることもある！'
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion '何もわかってないのに、さもわかっているかのように振舞うのはお\n姉の得意技ですしね。'
 show mion_v002 sinken at jumping_transform,active
 show shion_v002 smile at inactive
 mion '違うよ、ワニャンの得意技なんだよぅ！\u3000手掛かりゼロでさもわ\nかっているかのように振舞い、隙を誘う！'
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika '探偵たるもの、常日頃から、何もかもお見通しのようなオーラを\n纏っていなくてはなりませんね。'
 hide erika_v001
 with Dissolve(0.2)
 narrator '\u3000そういう話の流れになれば、あとはもう、名探偵だのミステリー\nだの、そういう話題になるのは火を見るより明らかだ。'
 narrator '\u3000そこに、嘉音さんと一緒に朱志香さんも戻ってくる。\n\u3000嘉音さんがお茶の準備をしている間に、朱志香さんも話に加わる\nのだった。'
 narrator '\u3000この頃には、ミステリーから未解決事件、都市伝説と話題は移\nり、最後にはオカルトにまで至っていた……。'
 show mion_v002 smile at mei_right
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion '確かに一理ありますね。解決できればミステリーだけれど、解決で\nきないなら、オカルトになることもありえる。'
 show mion_v002 smile at active
 show shion_v002 smile at inactive
 mion '太古の昔から、神の奇跡とされていたものが、次々に科学で解明さ\nれたからね。'
 show mion_v002 smile at active
 show shion_v002 smile at inactive
 mion '神の奇跡は解明できない。イコール、解明できなければ神の奇跡と\nも言えちゃう訳だ。'
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao '科学とオカルトの、戦いなんですね。'
 show erika_v001 normal_close at mei_right
 with Dissolve(0.5)
 show erika_v001 normal_close at active
 show nao_v002 normal at inactive
 erika 'そこは優雅に、ミステリー、バーサス、ファンタジーと言って頂き\nたいです。'
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 show jessica_v001 fuan_close at mei_center
 with Dissolve(0.5)
 show jessica_v001 fuan_close at active
 jessica 'まぁ、未解明が何でもかんでも悪いって訳じゃねぇからな。\nやり過ぎれば、子供の夢を壊しちまうこともあるぜ。'
 hide jessica_v001
 with Dissolve(0.2)
 show shion_v002 smile at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show shion_v002 smile at inactive
 nao '……オヤシロさまの#p祟#sたた#rりも、未解明なだけで、いつかは科学的に正\n体が暴かれるのでしょうか？'
 show shion_v002 fuan at active
 show nao_v002 normal at inactive
 shion '信仰は難しいですね。暴いちゃまずいものも、世の中にはあるって\nことです。'
 hide shion_v002
 hide nao_v002
 with Dissolve(0.2)
 show jessica_v001 sinken at mei_center
 with Dissolve(0.5)
 show jessica_v001 sinken at active
 jessica '何？\u3000オヤシロさまの祟りって！'
 hide jessica_v001
 with Dissolve(0.2)
 narrator '\u3000おや、食い付きがいい。\n\u3000まぁ、確かに、オヤシロさまの祟りなんてフレーズ、#p雛見沢#sひなみざわ#rの人\n以外には、ちょっと面白そうに聞こえるかもしれない……。'
 show jessica_v001 normal at mei_left
 show erika_v001 normal_close at mei_right
 with Dissolve(0.5)
 show erika_v001 normal_close at active
 show jessica_v001 normal at inactive
 erika '……毎年、村の祭の日に、１人が死に、１人が行方不明にな\nる、……ですか。'
 show jessica_v001 fuan at chara_shake_transform,active
 show erika_v001 normal_close at inactive
 jessica '何それ、めちゃめちゃ怖ぇぜ……？！\u3000足音が付けてくるなんて、\n私、今夜、ひとりでトイレ行けねぇぜぇ……！！'
 hide jessica_v001
 hide erika_v001
 with Dissolve(0.2)
 show shion_v002 normal at mei_left
 show mion_v002 normal at mei_right
 with Dissolve(0.5)
 show mion_v002 normal at active
 show shion_v002 normal at inactive
 mion 'そもそも園崎の園という字は……、人間の内臓を示していて、崎と\nいう字は……、'
 show shion_v002 sinken at active
 show mion_v002 normal at inactive
 shion '園崎家には双子が生まれたら、片方はくびり殺せという家訓があり\nまして。生まれたばかりの私の首を……、ぎええぇえぇえぇ！'
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 show jessica_v001 odoroki at mei_right
 with Dissolve(0.5)
 show jessica_v001 odoroki at active
 jessica 'マジかよ、おいおいッ、島の外も怖ぇなぁ！！\u3000私ゃ、一生、六軒\n島でもいいかもだぜ……。'
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at active
 show jessica_v001 odoroki at inactive
 nao '……雛見沢がちょっと、そういう話に恵まれ過ぎているだけです。'
 hide jessica_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator '\u3000日本中のあちこちが、こんなにも物騒な昔話で溢れていると勘違\nいされたら気の毒過ぎる。'
 narrator '\u3000それに何だか、地元に恐ろしいミステリーやオカルトがあるとス\nゴイ、みたいな流れになっていた。'
 play sound ['audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav'] fadeout 1.0
 show erika_v001 normal at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show erika_v001 normal at inactive
 nao '……そういえば、ヱリカさん。……魔女がどうのこうのって、言っ\nていませんでしたか？'
 show erika_v001 normal at active
 show nao_v002 normal at inactive
 erika 'くす。……その話は、この島の住人である朱志香さんがされるべき\nでしょう。'
 hide erika_v001
 hide nao_v002
 with Dissolve(0.2)
 show mion_v002 smile at mei_right
 show shion_v002 normal at mei_left
 with Dissolve(0.5)
 show shion_v002 normal at active
 show mion_v002 smile at inactive
 shion '魔女って、ひょっとしてさっきの肖像画のご婦人のこと、です\nか？'
 show mion_v002 smile at active
 show shion_v002 normal at inactive
 mion 'いいねいいねぇ、やっぱり洋館のオカルトは洋風じゃないとねぇ。'
 show mion_v002 futeki at active
 show shion_v002 normal at inactive
 mion 'でも、こっちは流血のダム戦争から連なるオヤシロさまの祟りに、\n秘祭、#p綿流#sわたなが#rしの秘密まで話したんだからねぇ。'
 show shion_v002 futeki at active
 show mion_v002 futeki at inactive
 shion '肖像画のご婦人が夜中に瞬きした、って程度では、ちょっと釣り合\nいませんよ～？'
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show jessica_v001 futeki at mei_left
 with Dissolve(0.5)
 show jessica_v001 futeki at active
 jessica 'そこまで言われちゃあ、こっちも黙ってる訳にはいかねぇぜ。取っ\nて置きを披露しちまうぜ！'
 show kanon_v001 normal at mei_right
 with Dissolve(0.5)
 show kanon_v001 normal at active
 show jessica_v001 futeki at inactive
 kanon '……お嬢様。よろしいのですか？'
 show jessica_v001 fuan at active
 show kanon_v001 normal at inactive
 jessica 'ぇ、あ、えーと……。'
 show jessica_v001 fuan_close at active
 show kanon_v001 normal at inactive
 jessica '私がここでこんな話をしたってのは、絶対に内緒で頼むぜ？\u3000母さ\nんに知られたら怒られるぜ……。'
 hide jessica_v001
 hide kanon_v001
 with Dissolve(0.2)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika 'くすくすくす。'
 stop music fadeout 0.5
 hide erika_v001
 with Dissolve(0.2)
 narrator '\u3000音楽室に、ベートーベンの絵があるだけで、怪談が生まれるの\nだ。\n\u3000ましてや、雰囲気たっぷりの洋館に、あれだけの巨大な肖像画。'
 narrator '\u3000その上、錬金術師を名乗るミステリアスな美女。……これで怪談\nが生まれない方がおかしい。'
 play music 'audio/bgm/BGM_QUEST3_COLLAB2.wav'
 show kanon_v001 normal at mei_right
 show jessica_v001 normal at mei_left
 with Dissolve(0.5)
 show jessica_v001 normal at active
 show kanon_v001 normal at inactive
 jessica 'さっきも見たと思うけど。……ウチの屋敷は広いんだ。家族の人数\nに合ってないくらいに。'
 show kanon_v001 normal at active
 show jessica_v001 normal at inactive
 kanon '……たくさんの部屋が、一族で満たされるような子孫繁栄を願っ\nて、意図的に広く作られたと聞いたことがあります。'
 show jessica_v001 fuan at active
 show kanon_v001 normal at inactive
 jessica '祖父さまの縁起担ぎは勝手だけどさ。……無駄に広い屋敷っての\nは、言うまでもなく、薄気味悪ぃんだよな。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.4
 hide kanon_v001
 hide jessica_v001
 hide fade with Dissolve(0.08333333333333333)
 show mion_v002 futeki at mei_center
 with Dissolve(0.08333333333333333)
 show mion_v002 futeki at active
 mion '使わない部屋には、……人ならざる者が住み着くっていうから\nねぇ……。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide mion_v002
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at chara_shake_transform,active
 nao 'や、……止めて下さい。顔が近いです。'
 hide nao_v002
 with Dissolve(0.2)
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika 'ウィンチェスターミステリーハウスの話をご存知ですか？'
 show shion_v002 normal at mei_left
 with Dissolve(0.5)
 show shion_v002 normal at active
 show erika_v001 normal at inactive
 shion 'ウィンチェスターって、銃のウィンチェスターですか？'
 show erika_v001 normal at active
 show shion_v002 normal at inactive
 erika 'ウィンチェスター銃のビジネスで大富豪となったウィンチェスター\n氏の未亡人は、夫の銃で殺された人々の霊が自分を祟っていると信\nじていたそうです。'
 hide shion_v002
 show mion_v002 normal at mei_left
 with Dissolve(0.5)
 show mion_v002 normal at active
 show erika_v001 normal at inactive
 mion '占い師に、亡霊たちを住まわせる空き部屋を増築し続けないと、呪\nわれて死ぬって脅されて、それを信じたんだってさ。'
 hide erika_v001
 hide mion_v002
 with Dissolve(0.2)
 narrator '\u3000それが、ウィンチェスター氏の未亡人が死ぬまで増築を続けたと\nいう、歪なる巨大邸宅、ウィンチェスターミステリーハウスであ\nる……。'
 show erika_v001 normal at mei_right
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at active
 show erika_v001 normal at inactive
 nao '……え……。……じゃあ、家族の人数に見合わない、部屋の多過ぎ\nるお屋敷は……。'
 show erika_v001 normal_close at active
 show nao_v002 fuan at inactive
 erika '右代宮家の当主、金蔵さんは、ベアトリーチェより借り受けた\n１００ｔの金塊を元に、ビジネスを成功させたとか。'
 show erika_v001 normal at active
 show nao_v002 fuan at inactive
 erika 'それだけなら、サクセスストーリーですが。……私には何か、大切\nなことが伏せられている気がします。'
 hide erika_v001
 hide nao_v002
 with Dissolve(0.2)
 show shion_v002 fuan at mei_left
 show mion_v002 normal at mei_right
 with Dissolve(0.5)
 show mion_v002 normal at active
 show shion_v002 fuan at inactive
 mion '１００ｔの金塊が、草っ原から生えてくる訳もない。'
 show mion_v002 normal_close at active
 show shion_v002 fuan at inactive
 mion '錬金術で、あのベアトリーチェってご婦人が生み出した、なんてお\n伽話にはしてるけれど……。'
 show shion_v002 fuan at active
 show mion_v002 normal_close at inactive
 shion '普通に考えて。……桁違いの欲望や怨念、そして死者が関わってい\nてもおかしくないような、莫大な金塊ですよね……。'
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 show jessica_v001 fuan at mei_left
 show kanon_v001 normal_close at mei_right
 with Dissolve(0.5)
 show kanon_v001 normal_close at active
 show jessica_v001 fuan at inactive
 kanon '…………………。'
 show jessica_v001 fuan at chara_shake_transform,active
 show kanon_v001 normal_close at inactive
 jessica 'お、おいおい、よしてくれよ……！\u3000自分の家なのに、夜、トイレ\nに行けなくなっちまうぜ……。'
 hide jessica_v001
 hide kanon_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao '……このゲストハウスだって、広過ぎです。'
 show nao_v002 fuan at active
 nao 'お屋敷にあれだけ客室が余ってるのに、わざわざ作る必要があると\nは……。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 fuan at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 fuan at active
 erika '２００億円の金塊に、未だに集まってくる怨霊たちを、……迎える\n為かもしれませんねぇ……？'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 narrator '\u3000嫌だ、怖い。……ちょっと止めてほしいわ。あたし、ここにこれ\nから２泊するのよ……？'
 show kanon_v001 normal at mei_right
 show jessica_v001 normal_close at mei_left
 with Dissolve(0.5)
 show jessica_v001 normal_close at active
 show kanon_v001 normal at inactive
 jessica 'まぁそれで、話を戻すぜ……。'
 show jessica_v001 normal at active
 show kanon_v001 normal at inactive
 jessica 'とにかく、ベアトリーチェってのが何者なのか、祖父さま以外、こ\nの屋敷の誰も知らねぇんだ。'
 show kanon_v001 normal at active
 show jessica_v001 normal at inactive
 kanon 'お館様の大恩人である、とのこと以上は、誰も……。'
 show jessica_v001 normal at active
 show kanon_v001 normal at inactive
 jessica '生きてるのか死んでいるのか。生きていたら何歳なのか。どこに住\nんでいるのか……。'
 show jessica_v001 fuan_close at active
 show kanon_v001 normal at inactive
 jessica '私たちは誰も知らねぇんだ……。'
 hide kanon_v001
 hide jessica_v001
 with Dissolve(0.2)
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 nao '……誰だかわからない人の肖像画が、……大広間に、あんなにも堂\n々と飾られているなんて、何だか薄気味悪いかも。……かも。'
 hide nao_v002
 with Dissolve(0.2)
 narrator '\u3000いつ誰が名付けたのか。……やがて彼女は、黄金の魔女、ベアト\nリーチェと呼ばれるようになる。'
 narrator '\u3000屋敷の大広間に飾られた巨大な肖像画は、当主の金蔵を描いたも\nのではなく、黄金の魔女を描いたもの。'
 narrator '\u3000……つまりは、屋敷も、この島も、……真の主は、黄金の魔女、\nベアトリーチェなのではないか。'
 show kanon_v001 normal at mei_right
 show jessica_v001 normal at mei_left
 with Dissolve(0.5)
 show jessica_v001 normal at active
 show kanon_v001 normal at inactive
 jessica '夜。……不思議な人影が、屋敷の中を徘徊しているって噂は、……\n使用人の間では、結構、有名だったんだ。……な？'
 show kanon_v001 normal_close at active
 show jessica_v001 normal at inactive
 kanon '………はい。'
 show kanon_v001 normal at active
 show jessica_v001 normal at inactive
 kanon 'もし。……夜の屋敷の中で、不思議な人影を見ても、……決して後\nを追ったり、ましてや、声を掛けてもならないと。'
 show kanon_v001 normal at active
 show jessica_v001 normal at inactive
 kanon '僕も何度か、……右代宮家の誰かでも、使用人の誰かでもあるはず\nのない、……不思議な女性の人影を、見たことがあります。'
 show jessica_v001 normal at active
 show kanon_v001 normal at inactive
 jessica '時折。窓の施錠がされてなくて使用人が母さんに怒られてた。'
 show jessica_v001 fuan_close at active
 show kanon_v001 normal at inactive
 jessica 'でも、みんな言うんだ。確かに見回りの時に施錠を確認した、っ\nて。'
 hide kanon_v001
 hide jessica_v001
 with Dissolve(0.2)
 show shion_v002 smile at mei_left
 show mion_v002 normal at mei_right
 with Dissolve(0.5)
 show mion_v002 normal at active
 show shion_v002 smile at inactive
 mion 'あれだけの広い屋敷だからね。……ベアトリーチェを名乗る何者か\nが、隠れ潜んでいたとか。'
 show shion_v002 smile at active
 show mion_v002 normal at inactive
 shion 'でも、窓の鍵を開けるくらいの悪戯なら、可愛いもんじゃないです\nか。'
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao '……確かに。'
 hide nao_v002
 with Dissolve(0.2)
 show jessica_v001 normal at mei_left
 show kanon_v001 normal at mei_right
 with Dissolve(0.5)
 show kanon_v001 normal at active
 show jessica_v001 normal at inactive
 kanon 'ベアトリーチェさまは、その存在を信じて敬う者には、寛大だと言\nわれています。'
 show jessica_v001 normal at active
 show kanon_v001 normal at inactive
 jessica 'だから。……ベアトリーチェのことを馬鹿にして、いる訳がないな\nんて言い張ると、……祟られるらしいんだ。'
 hide jessica_v001
 hide kanon_v001
 with Dissolve(0.2)
 narrator '\u3000右代宮家には、少なくない人数の使用人が出入りしており、時\nに、新しい使用人と入れ替わることもある。'
 narrator '\u3000何しろ広大で、そして薄気味悪さも伴う屋敷だ。……大抵の新人\nは、ベアトリーチェという怪談を神妙に受け容れる。'
 show jessica_v001 normal at mei_left
 show kanon_v001 normal_close at mei_right
 with Dissolve(0.5)
 show kanon_v001 normal_close at active
 show jessica_v001 normal at inactive
 kanon 'でも。……たまに、信じない人もおりました。'
 show jessica_v001 normal at active
 show kanon_v001 normal_close at inactive
 jessica '……以前、夜の見回りの時に、階段を踏み外して転げ落ちて、大怪\n我をして辞めた使用人がいたんだよ。'
 show jessica_v001 fuan_close at active
 show kanon_v001 normal_close at inactive
 jessica '後で紗音に聞いたら、……その人、ベアトリーチェがいるなら現れ\nてみろなんて、言ってた矢先だったらしい……。'
 show kanon_v001 normal at active
 show jessica_v001 fuan_close at inactive
 kanon '…………僕も、最初は信じていませんでした。'
 show kanon_v001 fuan_close at active
 show jessica_v001 fuan_close at inactive
 kanon 'しかし、……ある出来事があり、……それ以来、存在を疑うのを止\nめました。'
 hide jessica_v001
 hide kanon_v001
 with Dissolve(0.2)
 show nao_v002 fuan at mei_left
 show shion_v002 normal at mei_right
 with Dissolve(0.5)
 show shion_v002 normal at active
 show nao_v002 fuan at inactive
 shion '……つまり。……その出来事を境に、ベアトリーチェの存在を信じ\nるようになった、と……？'
 show nao_v002 fuan at active
 show shion_v002 normal at inactive
 nao 'その出来事って、……何があったんですか。'
 hide nao_v002
 hide shion_v002
 with Dissolve(0.2)
 show kanon_v001 normal_close at mei_center
 with Dissolve(0.5)
 show kanon_v001 normal_close at active
 kanon '………………………。'
 show expression "#000" as fade with Dissolve(1.0)
 hide kanon_v001
 with Dissolve(0.2)
 play sound ['audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav'] fadeout 1.0
 scene expression "#000"
 play audio 'audio/sfx/SE_5020_key.wav'
 narrator '\u3000ある日。薔薇の手入れを主な仕事とする嘉音さんは、園芸倉庫に\n施錠した後、鍵をポケットに入れたまま、就寝してしまったとい\nう。'
 narrator '\u3000本来は、勤務時間中に使用した鍵は、勤務が終わる時に、使用人\n室のキーボックスに戻さなければならない。'
 narrator '\u3000それを戻さずに、嘉音さんは一日を終えてしまったのだという。'
 narrator '\u3000園芸倉庫の鍵は、それ１つしかない。マスターキーでは開けるこ\nとは出来ない。'
 narrator '\u3000つまり。……園芸倉庫は、彼が施錠してから、翌朝に開錠するま\nで、誰にも開けることが出来ない、密室だったということにな\nる……。'
 jessica '翌朝。……嘉音くんが園芸倉庫のシャッターを開けると……、そこ\nにはありえないものがあったんだ……。'
 nao 'ありえないもの、って………？'
 window hide None
 stop sound
 scene expression "#000"
 play music 'audio/bgm/BGM_QUEST7_COLLAB2.wav'
 show expression 'images/bg/AdvBg_2320.png' as bg
 with Dissolve(1.0)
 pause 6.0
 show expression "#000" as fade with Dissolve(1.0)
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2291.png' as bg
 with Dissolve(1.0)
 show kanon_v001 normal_close at mei_center
 with Dissolve(0.5)
 show kanon_v001 normal_close at active
 kanon '……不気味な、……魔法陣が、描かれていました。'
 hide kanon_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show nao_v002 normal at inactive
 erika 'シンプルに推理するならば、……密室の唯一の鍵を持っていた、嘉\n音さんの自作自演が疑えるでしょう。'
 show erika_v001 normal_close at active
 show nao_v002 normal at inactive
 erika 'ですが、だからこそ逆に……。'
 show nao_v002 normal at active
 show erika_v001 normal_close at inactive
 nao '……嘉音さんには、……これが人間の仕業でないと、……わか\nる……。'
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 show kanon_v001 normal_close at mei_center
 with Dissolve(0.5)
 show kanon_v001 normal_close at active
 kanon '…………………………。'
 show kanon_v001 normal at active
 kanon '……源次さまにこのことをお伝えしたところ、……決して誰にも、\n口外してはならぬと。'
 hide kanon_v001
 with Dissolve(0.2)
 show jessica_v001 sinken at mei_center
 with Dissolve(0.5)
 show jessica_v001 sinken at active
 jessica '魔法陣が、……ベアトリーチェの挨拶なのさ。'
 show jessica_v001 sinken_close at active
 jessica 'ベアトリーチェは……、自分を信じない者のところに訪れ、魔法陣\nを残すんだ……。'
 hide jessica_v001
 with Dissolve(0.2)
 show mion_v002 normal at mei_right
 show shion_v002 normal at mei_left
 with Dissolve(0.5)
 show shion_v002 normal at active
 show mion_v002 normal at inactive
 shion '……それが、警告で済んでいる内はいいけれど。'
 show mion_v002 normal at active
 show shion_v002 normal at inactive
 mion 'それでもなお、ベアトリーチェの存在を否定したり、あるいは馬鹿\nにしたりすると、……階段を転げ落ちて大怪我する人もいる、\nと……。'
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show erika_v001 normal_close at mei_right
 with Dissolve(0.5)
 show erika_v001 normal_close at active
 erika '私は探偵です。この世の全ては、推理で暴けると確信しています。'
 show erika_v001 normal at active
 erika 'しかし、だからこそ。時に。……私でさえ、推理することが冒涜で\nあるかもしれない“何か”に、出くわすことはあります。'
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at active
 show erika_v001 normal at inactive
 nao 'ちょっと……、……いや本当に……、………怖いかも、………か\nも……。'
 hide erika_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator '\u3000まだ日も高いのに、あたしの背中は冷たい気配でぞわぞわしてい\nる。'
 narrator '\u3000そう。それが唯一の幸運だ。まだ昼過ぎではないか。怪談を楽し\nむには、あまりに外はいいお天気過ぎるのだ。'
 narrator '\u3000……あたしは空気を変えたかった。\n\u3000美しい薔薇庭園で、本を読んだり刺繍をしたりしてのんびり過ご\nす為にやってきたのだ。'
 narrator '\u3000早く、帰る日が来ないかと怯えながら指を折って数える為に来た\nんじゃない……。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide fade with Dissolve(0.08333333333333333)
 show nao_v002 smile at mei_center
 with Dissolve(0.08333333333333333)
 show nao_v002 smile at jump_transform,active
 nao '……はははははは、あっははははははは。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 narrator '\u3000とにかく、誤魔化すかのように笑えば、誰かも一緒に笑ってくれ\nて、場の空気を換えられるのだ。'
 narrator '\u3000だから、何も面白くないのに、あたしはケタケタと笑い続けるの\nだ。'
 camera at screenshake_transform
 pause 0.0
 narrator '\u3000でも、………どうして？！\u3000誰も、あたしと一緒に笑ってはくれ\nない……！'
 show nao_v002 smile at mei_center
 with Dissolve(0.5)
 show nao_v002 smile at active
 nao '馬鹿馬鹿しいわ。ハロウィンはもう、ひと月も前に終わってるって\nいうのに。'
 show nao_v002 smile at active
 nao 'せっかく楽しく過ごそうと思って、ここまでやってきたのに、こん\nなチープな怪談で怖がらせられるなんて、滑稽よ。'
 show nao_v002 smile at active
 nao 'それに、今の世の中、どんな不思議なことだって、必ず解明できる\nもの！'
 show nao_v002 smile at active
 nao 'ねぇ、ヱリカさん。そうでしょう？'
 hide nao_v002
 with Dissolve(0.2)
 show erika_v001 normal_close at mei_center
 with Dissolve(0.5)
 show erika_v001 normal_close at active
 erika '…………………。'
 hide erika_v001
 with Dissolve(0.2)
 show nao_v002 sinken at mei_center
 with Dissolve(0.5)
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.1
 pause 0.5
 show nao_v002 sinken at active
 nao '仮に、ベアトリーチェの亡霊が夜の屋敷を歩いているのを見たって\nいう、目撃者が現れたとしても！'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.2
 pause 0.5
 show nao_v002 sinken at active
 nao '偽証の可能性があるし、視力の問題だって、あと、知性の問題だっ\nけ？\u3000あらゆる可能性が否定することが出来る！'
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
 show nao_v002 sinken at active
 nao 'そうでしたよね？！\u3000ヱリカさん！'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 hide nao_v002
 with Dissolve(0.2)
 show erika_v001 normal_close at mei_center
 with Dissolve(0.5)
 show erika_v001 normal_close at active
 erika '……そうですね。フェリーでお会いした時。私は確かにそう言いま\nした。'
 show erika_v001 normal at active
 erika 'でもその上で。先ほど、申し上げたはずです。'
 hide erika_v001
 with Dissolve(0.2)
 narrator '\u3000しかし、だからこそ。時に。'
 narrator '\u3000私でさえ、推理することが冒涜であるかもしれない“何か”に、\n出くわすことはあります、………と。'
 show nao_v002 sinken at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show nao_v002 sinken at inactive
 erika '……私は探偵です。それがニンゲンの引き起こした事件である限\nり、必ず、証拠を集めて、真相を暴く自信があります。'
 show erika_v001 normal at active
 show nao_v002 sinken at inactive
 erika 'しかし。……人ならざる者が引き起こした事件であるならば、話は\n別です。'
 show nao_v002 fuan at active
 show erika_v001 normal at inactive
 nao '……そんな…………。'
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 narrator '\u3000ヱリカさんという人なら、おかしな怪談の魔女など認めたりし\nないと、信じていたのに……。'
 show mion_v002 normal at mei_right
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at active
 show mion_v002 normal at inactive
 shion '菜央さん、落ち着きましょう。ただの、茶飲み話ですよ？'
 show mion_v002 normal at active
 show shion_v002 smile at inactive
 mion '……オヤシロさまが“い”るように。この島には魔女が“い”るん\nだよ。'
 show mion_v002 normal_close at active
 show shion_v002 smile at inactive
 mion 'あまり、頭ごなしに否定するのは、……おじさんはあんまり、感心\nしないなぁ。'
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 narrator '\u3000いつも、ふざけて茶化す魅音さんまで……！\u3000ついさっきまで、\n人様の屋敷で不謹慎な話で盛り上がっていたのに！'
 narrator '\u3000詩音さんは、まるで癇癪を起した子供を宥めるかのような様子\nで、あたしに接する。'
 narrator '\u3000朱志香さんと嘉音さんに至っては、互いに顔を見合わせながら、\n……きっと思っているのだ。'
 narrator '\u3000……この小さな客人が、魔女の祟りに遭わないといいのだけれ\nど、と………！'
 play sound ['audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav'] fadeout 1.0
 stop music fadeout 0.5
 show jessica_v001 smile at mei_left
 show kanon_v001 normal at mei_right
 with Dissolve(0.5)
 show kanon_v001 normal at active
 show jessica_v001 smile at inactive
 kanon '……お嬢様。次のお勤めがありますので。'
 show jessica_v001 smile at active
 show kanon_v001 normal at inactive
 jessica 'そ、そうだね。嘉音くん、ありがと。'
 show jessica_v001 smile at active
 show kanon_v001 normal at inactive
 jessica 'じゃあ、私もそろそろ行くよ。'
 show jessica_v001 fuan at active
 show kanon_v001 normal at inactive
 jessica '菜央ちゃん、ごめんね？\u3000つまらない話だったよな。忘れて欲しい\nぜっ。……じゃ、じゃあな！'
 hide jessica_v001
 hide kanon_v001
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_530_walk_one.wav'
 narrator '\u3000朱志香さんたちは、気まずそうにしながら退出していく。\n\u3000ヱリカさんも、肩を竦めながら立ち上がる。'
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika '私は部屋へ戻ろうと思いますが、皆さんは？'
 hide erika_v001
 with Dissolve(0.2)
 show mion_v002 smile at mei_right
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion '私たちは明日の準備があるので、同じく部屋に戻って、ちょっと仕\n事をしようと思います。'
 show shion_v002 fuan at active
 show mion_v002 smile at inactive
 shion 'お姉が突然、色々と注文するもんだから、全然用意が間に合わな\nかったんですよ。サイアクです。'
 show mion_v002 smile at active
 show shion_v002 fuan at inactive
 mion '私も、部屋に戻って服の準備、手伝って。……ちょっとだけお昼寝\nしたいかな。'
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 narrator '\u3000気付けば、外はいつの間にか、小雨が降っていた。'
 narrator '\u3000空は明るいので、すぐに止むだろうが、傘を差してまで薔薇庭園\nに出ようという気持ちはない。'
 narrator '\u3000……これはバカンスなのだ。のんびりくつろぐのが目的なのだ。\n\u3000昭和の海外旅行みたいに、分刻みでバスであちこちに移動して観\n光するようなのとは、まったく違う。'
 narrator '\u3000それに、魅音さんも言っているが、あたしたちは結構、朝が早\nかった。'
 show nao_v002 fuan_close at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan_close at active
 nao '……あたしも、ちょっと眠いかも……かも。'
 hide nao_v002
 with Dissolve(0.2)
 narrator '\u3000ちょっと仮眠して。目が覚めたら、小雨に濡れた薔薇庭園を窓か\nら眺めるのも素敵かもしれない。'
 narrator '\u3000いや、案外、横になったら、電源が切れるみたいに眠ってしまう\nかも……。'
 narrator '\u3000貴重な一日を、朝が早かったので眠いから昼寝する、で費やして\nしまうのも、……バカンスなら有りだ。'
 show nao_v002 smile at mei_left
 with Dissolve(0.5)
 show nao_v002 smile at active
 nao '取りあえず、窓が閉まってよかったです。でも、やっぱり、寝る時\nはちゃんと施錠したいです。'
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show nao_v002 smile at inactive
 erika '……どうしたんです？\u3000窓の施錠、壊れてるんですか？'
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 show mion_v002 fuan at mei_right
 show shion_v002 fuan at mei_left
 with Dissolve(0.5)
 show shion_v002 fuan at active
 show mion_v002 fuan at inactive
 shion '壊れてるんじゃないです。壊したんです。どっかの誰かが。'
 show mion_v002 fuan at active
 show shion_v002 fuan at inactive
 mion 'もうちょっと試してみるよ……。謝るのはそれからでも間に合うっ\nて。'
 window hide None
 show expression "#000" as fade with Dissolve(1.0)
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2371.png' as bg
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_536_up_stairs.wav'
 pause 5.0
 play audio 'audio/sfx/SE_5007_keyroll.wav'
 narrator '\u3000あたしたち４人は、ぞろぞろと２階へあがる。\n\u3000そして、それぞれの部屋の施錠を、それぞれの鍵で開き、入っ\nた。'
 show expression "#000" as fade with Dissolve(1.0)
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2281.png' as bg
 with Dissolve(1.0)
 narrator '\u3000詩音さんは、トランクから、たくさんの衣装を取り出してベッド\nの上に広げ始める。\n\u3000撮影の時に使うお手製の衣装の一部が、まだ未完成らしい。'
 narrator '\u3000魅音さんは、窓の鍵としばらく格闘したが、やっぱり無理だった\nと、けろりと言って舌を出した。'
 play audio 'audio/sfx/SE_5037_getup.wav'
 narrator '\u3000あたしは、自分のベッドに横になり、靴下を脱ぐ。\n\u3000……これだけで、だいぶ体が楽になった。'
 play audio 'audio/sfx/SE_528_unfold_cloth.wav'
 narrator '\u3000本でも読もうと、頭は思っていても、体は拒否する。………眠\nい……。'
 narrator '\u3000こんなにも素敵な島で、こんなにも素敵なゲストハウスで、こん\nなにも素敵な薔薇庭園が広がっているのに、……昼寝。'
 narrator '\u3000うん。これぞ真のバカンス、真の贅沢かも。かも。'
 narrator '\u3000園崎姉妹の賑やかなおしゃべりを子守歌にしながら、瞼がとろん\nと重くなる。'
 narrator '\u3000……さっきの、魔女の怪談話の異様な雰囲気が嘘のよう。\n\u3000あれは、あたしがぼんやりしていた白昼夢ということに、ならな\nいかな……。'
 narrator '\u3000あたしのしたことは、古手神社の境内で、オヤシロさまなんか信\nじないと言ったのと同じようなもの。\n\u3000きっと、島の人の気を害した。'
 narrator '\u3000……島の、真の主の気も、……きっと。'
 narrator '\u3000………………………。'
 play sound ['audio/sfx/SE_5054_rain.wav','audio/sfx/SE_5054_rain.wav'] fadeout 1.0
 window hide None
 show expression "#000" as fade with Dissolve(1.0)
 scene expression "#000"
 show expression "#000" as bg
 with Dissolve(1.0)
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika '………………………。'
 show dlanor_v001 normal at mei_left
 with Dissolve(1.0)
 show dlanor_v001 normal at active
 show erika_v001 normal at inactive
 dlanor 'なるほど。天気雨にもなる訳デス。'
 show dlanor_v001 normal_close at active
 show erika_v001 normal at inactive
 dlanor 'ファンタジーの腸を引き摺り出すことを生き甲斐とする貴女が、ベ\nアトリーチェ卿の肩を持つトハ。'
 show erika_v001 normal_close at active
 show dlanor_v001 normal_close at inactive
 erika 'まったくです。蕁麻疹が出ちゃいますね。'
 show erika_v001 normal at active
 show dlanor_v001 normal_close at inactive
 erika '私は、ベアトの誕生祝いを託された、我が主の使いなのですから。\n立場は、一応、弁えているつもりです。'
 show dlanor_v001 smile at active
 show erika_v001 normal at inactive
 dlanor 'それにしても、今日のランチはお見事だったデス。'
 show erika_v001 smile at active
 show dlanor_v001 smile at inactive
 erika 'プレートに盛られたオムライスであろうとも。私はお箸で美味しく\nいただけてしまうのですっ。'
 show dlanor_v001 normal at active
 show erika_v001 smile at inactive
 dlanor 'ところで、それは……？'
 show erika_v001 normal at active
 show dlanor_v001 normal at inactive
 erika 'これが、ベアトへの誕生祝いです。ね？\u3000気に入ってくれそうで\nしょう？'