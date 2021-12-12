label event01_30_99:
 play sound ['audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav'] fadeout 1.0
 stop sound
 scene expression "#000"
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
 narrator '\u3000物語は、第一の魔法陣が、あたしのベッドシーツに描かれていた\nのを発見した時に遡る。'
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
 play music 'audio/bgm/BGM_EVENT_TOP_COLLAB2.wav'
 hide nao_v002
 with Dissolve(0.2)
 narrator '\u3000あたしが、おぞましい魔法陣に絶句している時。\n\u3000園崎姉妹は言っていた。'
 narrator '\u3000ひッ？！？！\u3000お、お姉……！！\n\u3000……やって、……くれるねぇ………。'
 narrator '\u3000以下は園崎姉妹の二人にしか聞こえないやりとりである。\n\u3000恐怖で頭を真っ白にしていたあたしには、聞こえる訳もない。'
 show mion_v002 futeki at mei_right
 show shion_v002 sinken at mei_left
 with Dissolve(0.5)
 camera at screenshake_transform
 pause 0.0
 show shion_v002 sinken at active
 show mion_v002 futeki at inactive
 shion '……これ……、無頼人さまの魔法陣ですよッッ？！？！'
 show mion_v002 futeki at active
 show shion_v002 sinken at inactive
 mion 'や、……やるねぇ……。見事な再現度だよ……。'
 show shion_v002 sinken at active
 show mion_v002 futeki at inactive
 shion 'お姉、……気付いてます……？'
 show mion_v002 sinken at jump_transform,active
 show shion_v002 sinken at inactive
 mion 'もちろん……。……枕や毛布の乱れ方まで、……完全に映画を再現\nしているッ。'
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 narrator '\u3000あたしは、紗音さんがどうして魔法陣を気にしなかったのかわか\nらず、長く混乱した。'
 narrator '\u3000しかし、……魅音さんは光の速度で理解した。紗音さんもまた、\nワニャン沼にはまるひとりだと知っていたからだ。'
 narrator '\u3000紗音さんが窓の鍵を見に行くといって２階へ上がり、降りて来た\n時。ヱリカさんは彼女にこう尋ねたのを魅音さんは記憶していた。'
 show expression "#000" as fade with Dissolve(1.0)
 stop sound
 scene expression "#000"
 camera at sepia_shader
 pause 0.0
 show expression 'images/bg/AdvBg_2331.png' as bg
 show shannon_v001 smile at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(1.0)
 show erika_v001 normal at active
 show shannon_v001 smile at inactive
 erika '紗音さん、ご苦労様です。窓から泥棒が入って、部屋を荒らしたり\nはしていませんでしたか？'
 show shannon_v001 smile_close at active
 show erika_v001 normal at inactive
 shannon 'いいえ。ご安心を。'
 hide shannon_v001
 hide erika_v001
 with Dissolve(0.2)
 narrator '\u3000魅音さんは不思議な違和感を覚えた。'
 narrator '\u3000ヱリカさんのそれは、一種の厭味に聞こえるのだが、……だとし\nたら言う相手を間違えている。'
 narrator '\u3000なぜ、部屋が荒れていないか、聞く？'
 narrator '\u3000魅音さんはすぐに理解する。ヱリカさんは、紗音さんがワニャ\nラーだと知っていた。'
 narrator '\u3000あたしが夕食後に紗音さんと会話をしていて、彼女がワニャラー\nだとＣＯするのを聞いていたのだ。'
 narrator '\u3000なので、あの魔法陣を、ちゃんと、映画の魔法陣だと理解してく\nれたかどうか、確認したかったのだ。'
 show expression "#000" as fade with Dissolve(1.0)
 camera at reset_shader
 pause 0.0
 scene expression "#000"
 narrator '\u3000さて。本来ならば、紗音さんが２階の部屋に入るのはイレギュ\nラーだった。'
 narrator '\u3000あたしが窓の鍵の話を唐突に始めたので、紗音さんは２階へ上が\nることになってしまった。'
 narrator '\u3000だからその時点でのヱリカさんは、内心、しまったと思ったはず\nだ。'
 narrator '\u3000魔法陣の悪戯の第一発見者を私にして、驚かせてやろうと思って\nたに違いないから。'
 narrator '\u3000そして同時に、ワニャラー仲間である魅音さんと詩音さんには、\n仲間内で盛り上がれる“ネタ”にもなる。'
 narrator '\u3000ところが、紗音さんはディープなワニャラーだった為、魔法陣の\n意味をすぐに理解し、微笑んでスルーした。'
 narrator '\u3000その事実を、ヱリカさんは、降りて来た紗音さんに#p問#s・#r#pい#s・#r#p掛#s・#r#pけ#s・#r#pて#s・#r、\n確認を取ったのだ。'
 narrator '\u3000魅音さんはそれを瞬時に理解する。\n\u3000紗音さんがスルーできることがわかっているなら、犯人がヱリカ\nさんであることは、秒で導ける答えだ。'
 narrator '\u3000つまり、魔法陣を発見したその時点で、園崎姉妹は魔法陣の正体\nも、犯人がヱリカさんであることも、全て全て、あの時点で知って\nいたのだ。'
 narrator '\u3000あたしが魔法陣に怯えて足を竦ませているその背後では、……キ\nモい笑みを浮かべたワニャラー園崎姉妹がニヤニヤしていたという\n訳だ。'
 stop sound
 scene expression "#000"
 play music 'audio/bgm/BGM_BATTLE1_COLLAB2.wav'
 show expression 'images/bg/AdvBg_2281.png' as bg
 with Dissolve(1.0)
 narrator '\u3000……そして、……ここからがあたしの理解を超える世界。\n\u3000バケモノ同士は惹かれ合うとはいうけれど、まさにこれを言うの\nだろう……。'
 narrator '\u3000魅音さんは、そして詩音さんは、超高速で状況を理解した。\n\u3000この見事な、映画の完全再現の魔法陣を描いたヱリカさんは、何\nを欲しているだろう？'
 narrator '\u3000賛辞？\u3000あるいは驚きの声？\u3000……そう、オーディエンスだ。'
 narrator '\u3000そう。その時、壁一枚向こうのヱリカさんの部屋では……、もう\n１人のワニャラーが、めちゃくちゃキモい笑いを浮かべて、じっと\n聞いていたのだ。'
 camera at screenshake_transform
 pause 0.0
 narrator '\u3000ヱリカさんは……、自分の魔法陣に驚く声、同志の感嘆の声が聞\nきたくて……、コップを壁に押し当てて耳を当て、……ずっと聞き\n耳を立てていた！！'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 smile at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 smile at active
 erika '……ふっふっふ……。如何ですか、私の魔法陣は傑作でしょ\nう……？\u3000無頼人さまの魔法陣を完全再現ですよぉ……？'
 show erika_v001 smile at active
 erika 'さぁ、聞かせて下さいな、魅音さん、詩音さん！！\n未だに名探偵ワニャンを見ようともしない異教徒、\n菜央さんの悲鳴はたっぷりと楽しみました。'
 camera at screenshake_transform
 pause 0.0
 show erika_v001 fuan at active
 erika '次はッ、あなたたちの感嘆が聞きたイィイっひひっひっひッ！！！'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 narrator '\u3000ヱリカさんは耳を澄ます耳を澄ます。魅音さんと詩音さんの反応\nが知りたくて全神経を聴覚に集めて全ての音を聞き取ろうとす\nる……！！'
 play audio 'audio/sfx/SE_5046_scratch.wav'
 narrator '\u3000……ゴリリ…………。'
 narrator '\u3000それは、小さな、おかしな音だった。\n\u3000小さい音なのだけれど、……耳のすぐ近くに押し付けて来たよう\nな、小さいけれども#p近#s・#r#pく#s・#r#pて#s・#r#p触#s・#r#pる#s・#r、異音。'
 narrator '\u3000……まさか。………いや、そんなまさか……。'
 narrator '\u3000ヱリカさんの額に冷たい汗が一粒浮かぶ。\n\u3000……それがゆっくりと滴り落ちようとする時、……ヱリカさんの\nその形相は……、不気味なくらいの……歓喜に彩られていた。'
 camera at screenshake_transform
 pause 0.0
 narrator '\u3000こいつ、……こいつら、……まさか……ッッッ？！？！'
 narrator '\u3000そう。ヱリカさんがコップを押し付けて隣の部屋の声を\nうかがっている、その壁の反対側では……、'
 show expression "#fff" as flash with Dissolve(0.1)
 pause 0.1
 hide flash with Dissolve(0.2)
 narrator 'ヱリカさんの形相とまったく同じ不気味な笑みを浮かべた\n#p二#s・#r#p人#s・#r#pの#s・#r#pヱ#s・#r#pリ#s・#r#pカ#s・#rがいた……。'
 show erika_v001 futeki at mei_center
 with Dissolve(0.5)
 show erika_v001 futeki at active
 erika 'ハッ………ハハ……………ッッッ。'
 hide erika_v001
 with Dissolve(0.2)
 narrator '\u3000こいつら……、#p聞#s・#r#pい#s・#r#pて#s・#r#pや#s・#r#pが#s・#r#pる#s・#r……ッ！！！'
 narrator '\u3000私が完璧な魔法陣を描き上げて、その感嘆の声を聴こうとして壁\nに耳を当てている私の挙動を、……聞いてやがるッ！！！'
 play audio 'audio/sfx/SE_325_ls_thunderfall.wav'
 narrator '\u3000２つの客室を隔てる１枚の壁の両側で、……１人と２人の巨大ナ\nメクジが……、コップを壁に押し付け合い、互いに聞き耳を立て\n合っているッ！！'
 camera at screenshake_transform
 pause 0.0
 narrator '\u3000グ、グッド、グッダぁあぁぁぁ……、グッデストぉおおおおおぉ\nおおおおおッ！！！'
 narrator '\u3000翌日。今度はそちらの番ですよとでもいうかのように、ヱリカさ\nんは自分の部屋の鍵を、わざと掛け忘れた。'
 narrator '\u3000園崎姉妹は、罠とわかっていても、敢えてこの機会に便乗\nし、……荷物を取りに戻るといってゲストハウスに詩音さんが戻\nる。'
 narrator '\u3000そして、ヱリカさんの部屋に入り、魔法陣の悪戯をするのだ。'
 narrator '\u3000なお、魔法陣のシーツは予め、事前に用意してあったものだ。\n……あたしが睡眠薬で眠った後、園崎姉妹は夜なべして作ったの\nだ！'
 narrator '\u3000そしてまんまと詩音さんは、ドアノブの蛍光塗料の仕掛けに引っ\n掛かる。'
 narrator '\u3000詩音さんもある程度の注意はしていたが、さすがにヱリカさんが\n自分で調合したという薬物の存在にまでは、気付けなかった。'
 narrator '\u3000だから、詩音さんの手には確かに、蛍光塗料が付着したのだ。そ\nれでヱリカさんはチェックメイトしたはずだった！'
 narrator '\u3000だが、……園崎姉妹はやはり、甘くはなかったのだ。\n\u3000そう。帰ってきて二人は、争うようにして一緒にシャワー室に駆\nけ込んでいった。'
 narrator '\u3000あたしは、シャワーの順番を争うなんて、双子姉妹は仲がいい\nなぁと微笑ましく思っていたけれど。'
 narrator '\u3000……二人は、この上なく慎重だった。'
 narrator '\u3000あの時、入れ替わったのだ。ヱリカさんの悲鳴を聞いて、シャ\nワー室から飛び出してきた時には、姉妹は入れ替わっていたのだ。'
 narrator '\u3000二人はヱリカさんを侮らなかった。……自分たちには知覚できな\nい、何らかの仕掛けが付着しているかもしれないと疑った！'
 narrator '\u3000だからあのシャワーは、それを洗い流すことと、さらに慎重を期\nして、姉妹を入れ替わらせることが目的だったのだ。'
 narrator '\u3000だが、ヱリカさんだって、自分を名探偵などと呼ぶ程度にはイカ\nレてる。'
 narrator '\u3000ブラックライトで詩音さんの手を照らして、何の痕跡もないこと\nを見た瞬間彼女は、こんなはずはないと絶叫を始めたが、……あれ\nは絶望の狂乱ではなく、ある意味、歓喜だったのだ。'
 narrator '\u3000ヱリカさんが言うには、……ノックス第１０条。“手掛かりなき\n他の登場人物への変装を禁ず”。'
 narrator '\u3000ヱリカさんは園崎姉妹に会い、自己紹介を交わして、二人が瓜二\nつの双子姉妹であることを知っていた。'
 narrator '\u3000“瓜二つな双子姉妹”と、ヱリカさん自身が、六軒島へ向かう船\nの上でそう言っているのだ。'
 narrator '\u3000だから、有効デス。\n\u3000ノックス第１０条に抵触しない、他の登場人物への変装。いや、\n入れ替わり……！'
 narrator '\u3000ヱリカさんはあの時、即座に魅音さんの手をブラックライトで照\nらすことも出来たのだ。'
 narrator '\u3000そうすれば、魅音さんの手が蛍光塗料で浮かび上がるのを見るこ\nとが出来ただろう。'
 narrator '\u3000しなかった。……どうして？\u3000一流はタフじゃないの？'
 camera at screenshake_transform
 pause 0.0
 narrator '\u3000違う。これは敬意、畏敬、崇敬……！'
 narrator '\u3000ヱリカさんは、ワニャラーとしての愛だけでなく、探偵の自分と\nの知恵比べにおいても、全身全霊で応えてくれた園崎姉妹に心酔さ\nえしたのだ。'
 narrator '\u3000ドラノールさんも言っていた。ヱリカさんは、探偵も犯人も演じ\n分けられる、優れた俳優なのだと。'
 narrator '\u3000だからこそ、あれだけみっともなく、出し抜かれて狼狽える姿を\n見せて、園崎姉妹に応えて見せたのだ。'
 narrator '\u3000いや、恐らくはアレも、名探偵ワニャンに出てくる、犯人のひと\nりの、往生際の悪さの再現なのかもしれない。'
 narrator '\u3000六軒島の２泊３日は、あたしにとってだけは、ホラーとミステ\nリー。'
 narrator '\u3000他の３人にとっては、……巨大ナメクジ、ワニャンを愛する者た\nちの、ファンミーティングなのであった……。'
 stop music fadeout 2.0
 window hide None
 show expression "#000" as fade with Dissolve(1.0)
 stop sound
 scene expression "#000"
 play music 'audio/bgm/BGM_GACHA_COLLAB2.wav'
 show expression 'images/bg/AdvBg_2271.png' as bg
 with Dissolve(1.0)
 pause 2.0
 stop sound
 
 pause 2.0
 stop sound
 
 show jessica_v001 smile at mei_center
 with Dissolve(0.5)
 show jessica_v001 smile at active
 jessica 'ぜひ！\u3000また遊びに来てくれよな！！\u3000その時はオールでボドゲ勝\n負しようぜ！\u3000な！'
 hide jessica_v001
 with Dissolve(0.2)
 Character('Krauss Ushiromiya',ctc="ctcArrow", ctc_position="fixed") '君たちの滞在のお陰で、使用人たちも色々と勉強になったと言って\nいる。感謝するよ。'
 Character('Natsuhi Ushiromiya',ctc="ctcArrow", ctc_position="fixed") 'アンケートもありがとうございました。よく読んで、今後に役立て\nたいと思います。'
 show shion_v002 smile at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at active
 show shion_v002 smile at inactive
 mion 'ガッツリと書いておきましたんで！\u3000ぜひ、最後まで読んで下さい\nね！'
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion '私たちが責任を持って！\u3000六軒島を新しいリゾート地にコンサルタ\nントしていきますので！'
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 narrator '\u3000お別れの時には、右代宮家の人までお見送りに来てくれた。'
 narrator '\u3000もう一度、訪れる時には、……今度はのんびりしたい。さもな\nきゃ、……あたしもコスプレ、……挑戦してみてもいいか\nも、……かも。'
 show erika_v001 normal at mei_right
 show kanon_v001 normal_close at mei_left
 with Dissolve(0.5)
 show kanon_v001 normal_close at active
 show erika_v001 normal at inactive
 kanon '紗音から、お見送りが出来なくて申し訳ないと言付かっておりま\nす。'
 show erika_v001 normal at active
 show kanon_v001 normal_close at inactive
 erika '今日はお休みですからね。仕方ありません。よろしく伝えておいて\n下さい。私たちは、巨大ナメクジの下、同志ですから！'
 show kanon_v001 normal at active
 show erika_v001 normal at inactive
 kanon '……えっと、確か、……真実は、いつも二つ。'
 play audio 'audio/sfx/SE_226_shine.wav'
 show erika_v001 smile at active
 show kanon_v001 normal at inactive
 erika '真実は、いつも二つ！\u3000あなたも読んでおいてくださいね？'
 hide erika_v001
 hide kanon_v001
 with Dissolve(0.2)
 show nao_v002 smile at mei_left
 show jessica_v001 fuan_blush at mei_right
 with Dissolve(0.5)
 show jessica_v001 fuan_blush at active
 show nao_v002 smile at inactive
 jessica '私も～……、その、次に機会がある時は、コスプレ撮影って、やっ\nてみよっかなぁって。'
 show jessica_v001 smile_blush at jump_transform,active
 show nao_v002 smile at inactive
 jessica 'その時はさ。菜央ちゃんも一緒にやろうぜ？\u3000一緒ならきっと、\n恥ずかしくないって。'
 show nao_v002 smile at active
 show jessica_v001 smile_blush at inactive
 nao 'くす……。そうですね。……一緒に、コスプレデビューしましょ\nう。'
 hide nao_v002
 hide jessica_v001
 with Dissolve(0.2)
 narrator '\u3000見送りの人々の中に、あの魔女の姿も混じっている。\n\u3000もちろん、誰にも姿は見えてないだろうが。'
 show nao_v002 smile at mei_left
 show beatrice_v001 smile at mei_right
 with Dissolve(0.5)
 show beatrice_v001 smile at active
 show nao_v002 smile at inactive
 beatrice '誕生日を、そなたと共に過ごせてよかったぞ。菜央。'
 show nao_v002 smile at active
 show beatrice_v001 smile at inactive
 nao 'ありがとう。だけど、聞いていいかしら。……一体、何歳の誕生日\nなの？'
 show beatrice_v001 futeki at active
 show nao_v002 smile at inactive
 beatrice 'くっくっく！\u3000千から先は忘れたわ！'
 show beatrice_v001 futeki at active
 show nao_v002 smile at inactive
 beatrice 'また、いつでも遊びに来るがよい。次は、妾の黄金郷の、黄金の薔\n薇庭園を案内しようぞ！'
 show nao_v002 smile at active
 show beatrice_v001 futeki at inactive
 nao 'あたしもゲーム機でも持ってきてあげるわ。腕前を存分に見せてあ\nげるから。'
 hide beatrice_v001
 show dlanor_v001 normal at mei_right
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show nao_v002 smile at inactive
 dlanor '貴女の行く末に幸多からんことを祈りマス。お元気でお過ごし下サ\nイ。'
 show nao_v002 smile at active
 show dlanor_v001 normal at inactive
 nao 'ありがとう。あなたとはもっと、ゆっくりとお話をしたかったわ。\nまた会いましょう。'
 hide dlanor_v001
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show nao_v002 smile at inactive
 erika '私は探偵ですので、事件が起こる度にあちこちに引っ張り凧です。\nだからもう、あんたと会うことはないでしょう。'
 show nao_v002 smile at active
 show erika_v001 normal at inactive
 nao '大丈夫よ。名探偵ワニャンのコラボカフェ。多分、あたしも行くか\nらそこで会えるわ。'
 show erika_v001 smile at active
 show nao_v002 smile at inactive
 erika '…………ふっふふふふ。グッド。その時は、推しキャラについて存\n分に語り合いましょう。'
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 show shion_v002 smile at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at active
 show shion_v002 smile at inactive
 mion 'ヱリカさんも、ぜひ#p雛見沢#sひなみざわ#rに遊びに来てね。ヱリカさんなら、絶対\nに退屈しないからさ！'
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion '圭ちゃんと対決して欲しいですねぇ。口先の魔術師と名探偵。どっ\nちが勝つか見てみたいです。'
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika 'ほう？\u3000口先の魔術師？\u3000魔術師とはまた、如何にもカネダ少年の\n事件簿に出てくる犯人の二つ名みたいで素敵です！'
 show erika_v001 futeki at active
 erika '古戸ヱリカ、皆さんのところで事件ある時、必ずや参上することを\nお約束しましょう！'
 hide erika_v001
 with Dissolve(0.2)
 show mion_v002 smile at mei_right
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion 'もしくは、フツーにエンジェルモートで、デザート食べ放題しなが\nら、だらだらと長話をしましょーねぇ☆'
 show mion_v002 smile at active
 show shion_v002 smile at inactive
 mion 'あんたみたいな面白くてタフなヤツを、ぜひ雛見沢分校に招きたい\nよ。'
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao '確かに。……ヱリカさんのパワーと推理力は、\n魅音さんとレナちゃんが合体したみたいなものだわ。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide nao_v002
 scene expression 'images/bg/AdvBg_2251.png' as bg
 show erika_v001 normal_close at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 normal_close at active
 erika 'いつか。必ず。'
 show erika_v001 normal at active
 erika 'ふふっ。……ただ、別れを惜しむ友人たちがそこにいるだけで、古\n戸ヱリカにはこの程度の挨拶が可能です。如何です、皆様方？'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show nao_v002 futeki at mei_center
 with Dissolve(0.5)
 show nao_v002 futeki at active
 nao 'グッド！'
 show expression "#fff" as fade with Dissolve(2.5)
 window hide None
 hide nao_v002
 with Dissolve(0.2)
 pause 6.0
 play sound ['audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav','audio/sfx/SE_5043_wave.wav'] fadeout 1.0
 stop sound
 scene expression "#fff"
 play music 'audio/bgm/BGM_HOME_COLLAB2.wav'
 show expression 'images/bg/AdvBg_2101.png' as bg
 with Dissolve(1.0)
 show erika_v001 normal at mei_right
 show nao_v002 smile at mei_left
 with Dissolve(0.5)
 show nao_v002 smile at active
 show erika_v001 normal at inactive
 nao '……ヱリカさんがもらった手紙は、何なんですか？'
 show erika_v001 normal_close at active
 show nao_v002 smile at inactive
 erika '気にしないで下さい。私はただの使い。主への返書を預かったに過\nぎません。'
 show erika_v001 normal at active
 show nao_v002 smile at inactive
 erika 'ベアトリーチェは私のことを良く書いてくれたそうなので。中身が\n楽しみです。'
 show nao_v002 normal at active
 show erika_v001 normal at inactive
 nao '……そういえば。……ベアトリーチェはあたしにも何かプレゼント\nをくれるって言っていたけれど……。'
 hide erika_v001
 hide nao_v002
 with Dissolve(0.2)
 show shion_v002 fuan at mei_left
 show mion_v002 odoroki at mei_right
 with Dissolve(0.5)
 camera at screenshake_transform
 pause 0.0
 show mion_v002 odoroki at active
 show shion_v002 fuan at inactive
 mion 'えー？\u3000何々？！\u3000六軒島でプレゼントをもらったの？！'
 show shion_v002 fuan at active
 show mion_v002 odoroki at inactive
 shion 'いいなぁ。私たち、なーんにももらってないです。'
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika 'いえ。魔女が菜央さんに預けたプレゼントは、貴女たち３人に\n宛てたものだと思います。'
 show erika_v001 normal at active
 erika '荷物の中を、見てみたらどうです？'
 hide erika_v001
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_5037_getup.wav'
 narrator '\u3000そう言われ、あたしは自分の荷物を調べる。\n\u3000すると、まったく心当たりのない、小さなプレゼントボックスが\n入っているではないか。'
 narrator '\u3000メッセージカードが添えてある。……やっぱり、ベアトリーチェ\nからだ。'
 play audio 'audio/sfx/SE_006_WindowScroll.wav'
 narrator '“六軒島への来訪を記念して。――黄金の魔女より”'
 show shion_v002 smile at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at active
 show shion_v002 smile at inactive
 mion 'あー、あの肖像画のね！\u3000２００億円の金塊だっけ？'
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion '肖像画の前に、碑文みたいなのあったじゃないですか。あれ、謎が\n書いてあって、解くと金塊の場所がわかるらしいですよ？'
 camera at screenshake_transform
 pause 0.0
 show mion_v002 odoroki at active
 show shion_v002 smile at inactive
 mion 'ええぇぇええぇ！！\u3000そういうことは滞在中に言ってよぉ！\u3000碑文\nの謎解きに挑戦したかったなぁー！'
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 show nao_v002 normal at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show nao_v002 normal at inactive
 erika 'ふふ。まぁ、私は解いたことがありますけれど。'
 show nao_v002 fuan at active
 show erika_v001 normal at inactive
 nao 'さらりとすごいこと言ったわ。金塊は本当にあったの……？'
 show erika_v001 normal_close at active
 show nao_v002 fuan at inactive
 erika 'もちろん！\u3000……まぁ、私には興味がなかったので、右代宮家の皆\nさんにお任せしましたが。'
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 show shion_v002 smile at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at active
 show shion_v002 smile at inactive
 mion '菜央ちゃん、早くプレゼント、開けてみようよ！'
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion '純金のモールドが入ってたりして？'
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika '１ｇでも数千円。仮に１００ｇもあったら、なかなかの価値になり\nますね。'
 show erika_v001 normal at active
 erika 'でも、あのベアトリーチェが、意味もなく黄金を贈ってくれるとは\nちょっと思えませんが。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 show nao_v002 normal at mei_center
 with Dissolve(0.08333333333333333)
 show nao_v002 normal at active
 nao 'すごく軽いから、金じゃないかも。……空っぽみたいに軽いわ。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 narrator '\u3000とにかく、開けてみよう……。'
 stop music fadeout 0.5
 play audio 'audio/sfx/SE_325_ls_thunderfall.wav'
 show expression "#fff" as fade with Dissolve(1.0)
 erika 'な、……何？！\u3000……何事ですかッ……？！'
 stop sound
 scene expression "#fff"
 play music 'audio/bgm/BGM_EVENT_TOP_COLLAB2.wav'
 show expression 'images/bg/AdvBg_2101.png' as bg
 with Dissolve(1.0)
 show shion_v011 fuan at mei_left
 show mion_v012 fuan at mei_right
 with Dissolve(0.5)
 show mion_v012 fuan at active
 show shion_v011 fuan at inactive
 mion '何よ、今のすっごい雷……！\u3000こんなに晴れてるのに凄かった\nね……。'
 camera at screenshake_transform
 pause 0.0
 show shion_v011 odoroki at active
 show mion_v012 fuan at inactive
 shion 'お、お姉？！\u3000そ、その恰好は何です……？！'
 hide shion_v011
 hide mion_v012
 with Dissolve(0.2)
 show erika_v001 normal at mei_right
 show nao_v014 odoroki at mei_left
 with Dissolve(0.5)
 show nao_v014 odoroki at jump_transform,active
 show erika_v001 normal at inactive
 nao 'そ、それを言ったら、詩音さんだって。どういうこと？\u3000手品？\u3000\n早着替え？！'
 show erika_v001 normal at active
 show nao_v014 odoroki at inactive
 erika '……菜央さんも、なかなかの恰好ですよ。'
 show erika_v001 normal at active
 show nao_v014 odoroki at inactive
 erika 'それ、……確か、シエスタ姉妹兵の。'
 show nao_v014 odoroki_blush at chara_shake_transform,active
 show erika_v001 normal at inactive
 nao 'な、……なな、何ですか、この服っ？\u3000え、ちょ、スカート短い！\n\u3000というか前、丸見え？！'
 hide erika_v001
 hide nao_v014
 with Dissolve(0.2)
 show mion_v012 smile at mei_right
 show shion_v011 fuan at mei_left
 with Dissolve(0.5)
 show shion_v011 fuan at active
 show mion_v012 smile at inactive
 shion 'お姉、私たちのこの服……。'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 show mion_v012 smile at active
 show shion_v011 fuan at inactive
 mion '『中秋哀歌～兎たちの悲恋殺人事件～』に出て来た、月兎の衣装\nだぁあぁ！！'
 play audio 'audio/sfx/SE_311_ls_cutejump.wav'
 show shion_v011 smile at jump_transform,active
 show mion_v012 smile at inactive
 shion 'すごいじゃないですか！\u3000私とお姉で、月兎の舞踏合わせが出来ま\nすよ？！'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide mion_v012
 hide shion_v011
 hide fade with Dissolve(0.08333333333333333)
 show nao_v014 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show nao_v014 sinken at active
 nao '魅音さんと詩音さんは楽しそうだけど、あたしは訳が分からないで\nす！'
 camera at screenshake_transform
 pause 0.0
 show nao_v014 fuan at active
 nao 'これも、名探偵ワニャンに出てくる衣装なんですかぁ？！'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide nao_v014
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika 'いいえ、違いますね。シエスタ姉妹兵の制服です。'
 show erika_v001 normal at active
 erika '魔界のマニアの間では、すっごい高額で取引されてるとか。それの\n新品なんて、ある意味、すっごいプライスレスです。'
 hide erika_v001
 with Dissolve(0.2)
 show mion_v012 smile at mei_center
 with Dissolve(0.5)
 show mion_v012 smile at active
 mion 'まぁ、新品より使用済みの方が価値が出る業界もあるけどねー。'
 hide mion_v012
 with Dissolve(0.2)
 show erika_v001 normal at mei_right
 show nao_v014 sinken_blush at mei_left
 with Dissolve(0.5)
 show nao_v014 sinken_blush at chara_shake_transform,active
 show erika_v001 normal at inactive
 nao 'あたしには価値がよくわかりませんっ。寒いです、恥ずかしいで\nす！！'
 show erika_v001 normal at active
 show nao_v014 sinken_blush at inactive
 erika 'おや？\u3000先程のメッセージカードの文字が、変わっていますね。'
 hide erika_v001
 hide nao_v014
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_006_WindowScroll.wav'
 narrator '\u3000楽しんでいただけたかな？\n\u3000開けると即座に衣装が変わる、お着換え玉手箱であるぞ！'
 narrator '\u3000実はな、３人にそれぞれが最も欲しがっている衣装を贈ってやろ\nうと思い、少し、そなたらのカケラを覗かせてもらったのだ。'
 narrator '\u3000魅音と詩音については、欲しい衣装のイメージがはっきりしてい\nたのでよかったが、菜央については、わからなかったのだ。'
 show nao_v014 fuan at mei_center
 with Dissolve(0.5)
 show nao_v014 fuan at active
 nao '……服なんて、その時その時でニーズが変わりますし。一番欲しい\n１着なんてイメージ、普段は持ってないし……。'
 hide nao_v014
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_006_WindowScroll.wav'
 narrator '\u3000なのでな、考えた。\n\u3000魅音と詩音は、兎たちの悲恋殺人事件の月兎の衣装なのであろ\nう？'
 narrator '\u3000ならばそなたも兎合わせにしてやったら、３人で仲良くできるの\nではないかと思ってな！'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide fade with Dissolve(0.08333333333333333)
 show nao_v014 fuan_blush at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show nao_v014 fuan_blush at active
 nao '思わないわぁあぁぁ！！！\u3000返して！\u3000スカートの前の部分だけで\nも返してぇぇ！'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide nao_v014
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show erika_v001 normal_close at mei_center
 with Dissolve(0.5)
 show erika_v001 normal_close at active
 erika '……フロントオープンスカートって、どういう訳か魔界で流行って\nるんですよね。'
 hide erika_v001
 with Dissolve(0.2)
 show mion_v012 smile at mei_right
 show shion_v011 smile at mei_left
 with Dissolve(0.5)
 show shion_v011 smile at active
 show mion_v012 smile at inactive
 shion 'ちょっと、エンジェルモートっぽいですよね！'
 show mion_v012 smile at active
 show shion_v011 smile at inactive
 mion '菜央ちゃん、エンジェルモートで今度、その衣装でバイトしてみな\nい？！'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide mion_v012
 hide shion_v011
 hide fade with Dissolve(0.08333333333333333)
 show nao_v014 sinken at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show nao_v014 sinken at active
 nao 'ヒナミザワーッ！！！\u3000オ・コ・ト・ワ・リぃいいぃいい\nいぃッ！！！'
 camera at screenshake_transform
 pause 0.0
 show nao_v014 sinken at active
 nao 'っていうか、さっきまで着てたあたしの服はどこなの？！\u3000ど\nこ？！'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide nao_v014
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika 'あ、またメッセージカードに文字が。……何々？'
 hide erika_v001
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_006_WindowScroll.wav'
 narrator '\u3000追伸。'
 narrator '\u3000そなたらが着ていた元の服は、魔界クリーニングの超特急便に\nて、明日には新品同様になって自宅に届けられることになってい\nる。'
 narrator '\u3000クリーニング代は妾の奢りであるぞ！\u3000礼には及ばぬ。\n\u3000それではまた会おう！\u3000シーユーアゲイン。ハバナイスデーイ！'
 show nao_v014 odoroki at mei_center
 with Dissolve(0.5)
 show nao_v014 odoroki at active
 nao 'どういうこと？！\u3000家までこの恰好でいろってことなの？！'
 hide nao_v014
 with Dissolve(0.2)
 show shion_v011 smile at mei_left
 show mion_v012 smile at mei_right
 with Dissolve(0.5)
 show mion_v012 smile at active
 show shion_v011 smile at inactive
 mion 'おじさんたちはコスプレ衣装があるから、着替えられるねー。'
 show shion_v011 fuan at active
 show mion_v012 smile at inactive
 shion 'でもお姉？\u3000往来を歩くには、ちょっと露出の多い衣装ばっかりで\nすよ？'
 hide mion_v012
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show shion_v011 fuan at inactive
 erika '殺人現場再現の、あの血まみれ衣装にすればいいじゃないですか。'
 show shion_v011 fuan_close at active
 show erika_v001 normal at inactive
 shion 'ただし、職質は免れないと思いますけれどね……。'
 hide erika_v001
 show mion_v012 smile at mei_right
 with Dissolve(0.5)
 show mion_v012 smile at active
 show shion_v011 fuan_close at inactive
 mion 'まぁまぁ。ウェディングドレス姿で、泣きながらタクシーを停めれ\nば、ちょっとはオマケしてくれるかもしれないーって♪'
 hide shion_v011
 hide mion_v012
 with Dissolve(0.2)
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika 'たくましい人たちです。くす。'
 show nao_v014 sinken_blush at mei_left
 with Dissolve(0.5)
 show nao_v014 sinken_blush at active
 show erika_v001 normal at inactive
 nao 'こんな羞恥プレイ！\u3000聞いてないわ！！\u3000どうしてこんな目に！'
 show nao_v014 sinken_blush at chara_shake_transform,active
 show erika_v001 normal at inactive
 nao 'この恰好で帰るなんて、部活のコスプレ罰ゲームよりもサイアクだ\nわーッ！！'
 show erika_v001 futeki at active
 show nao_v014 sinken_blush at inactive
 erika 'くっくっくっく……。メイアイヘルプユー？'
 hide erika_v001
 hide nao_v014
 with Dissolve(0.2)
 show nao_v014 sinken at mei_center
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_311_ls_cutejump.wav'
 show nao_v014 sinken at jump_transform,active
 nao 'イエース！！\u3000アイニード、えっと、スカートのフロント！！'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.2
 pause 0.5
 show nao_v014 sinken at active
 nao 'このスカートの、切り取った前の部分を返して！！\u3000せめて下腹部\nだけ隠させて！'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.4
 pause 0.5
 camera at screenshake_transform
 pause 0.0
 show nao_v014 sinken at active
 nao '何よ、この衣装！！\u3000センスない！\u3000Ｈ！\u3000最低だわぁぁぁ！！！'
 show expression "#000" as fade with Dissolve(3.0)
 pause 3.0