label event01_30_05:
 stop sound
 scene expression "#000"
 play music 'audio/bgm/BGM_QUEST2_COLLAB2.wav'
 show expression 'images/bg/AdvBg_2281.png' as bg
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_543_bird.wav'
 pause 2.0
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 nao '…………え…………。……朝…………。'
 hide nao_v002
 with Dissolve(0.2)
 narrator '\u3000んご～～～、すぴ～～～。\n\u3000……園崎姉妹のいびきだ。すごい。寝相までまったく同じだ。'
 show nao_v002 fuan_close at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan_close at active
 nao 'すごく……、変な夢を見た………。'
 hide nao_v002
 with Dissolve(0.2)
 narrator '\u3000明らかに夢の中の出来事だったが、……今でも細部を思い出せる\nほどに明晰な夢だった……。'
 narrator '\u3000あたしは、肖像画の魔女、ベアトリーチェに招かれ、……魔法陣\nの悪戯が人間には可能か否か、思考を戦わせたのだ。'
 narrator '\u3000昨夜のことを、おさらいしよう。\n\u3000客室に戻ったら、あたしのベッドが荒らされ、……シーツに魔法\n陣の落書きがされていた。'
 narrator '\u3000魔女を信じない者にベアトリーチェがするという、悪戯だ。'
 narrator '\u3000あたしは夢の中では、窓の鍵の様子を見に行った紗音さんを、\n疑っていた。'
 narrator '\u3000……あんなにも甲斐甲斐しく、お世話をしてくれた人を疑うなん\nて、今思うと申し訳ない。'
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao '……ベアトリーチェが言った、赤き真実……。'
 hide nao_v002
 with Dissolve(0.2)
 narrator '\u3000夢の中の話を真に受けるなど、他人が聞けば馬鹿馬鹿しいことだ\nと思うだろう。\n\u3000でも、あたしは信じることにする。'
 narrator '\u3000魔女が夢の中に出て来たことは、信じることにする。\n\u3000でも、あたしのベッドに、魔法陣の悪戯をしたことは、信じてな\nんかやるものか……。'
 narrator '\u3000ちなみに。魔法陣のシーツは昨夜、使用人室に連絡して交換して\nもらった。\n\u3000さすがにあんなシーツで眠れる図太さはない……。'
 narrator '\u3000連絡したら、源次さんという老いた使用人頭の人が新しいシーツ\nを持ってきてくれた。'
 narrator '\u3000汚れているのでと、丸めて渡した魔法陣のシーツを受け取って\n帰っていったが、……広げてみて、あの人はどう思っただろ\nう……？'
 play audio 'audio/sfx/SE_5037_getup.wav'
 Character('Sonozaki Sisters',ctc="ctcArrow", ctc_position="fixed") 'ふぅん……。ふぁああぁぁぁぁぁ………。'
 narrator '\u3000その時、園崎姉妹が二人そろって目を覚ます。\n\u3000すごい。録画しておきたいほどにシンクロした起床だ。'
 show shion_v002 fuan_close at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at active
 show shion_v002 fuan_close at inactive
 mion 'あれ、菜央ちゃん、早いね。おはよ～。'
 show shion_v002 fuan at active
 show mion_v002 smile at inactive
 shion 'ふああぁぁぁぁ……。今日は撮影だってのに、ちょっと寝足りない\nですよ……。'
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 show nao_v002 smile at mei_center
 with Dissolve(0.5)
 show nao_v002 smile at active
 nao '昨夜は睡眠薬を下さってありがとうございます。あれがなかった\nら、興奮して眠れなかったかもです。'
 hide nao_v002
 with Dissolve(0.2)
 show mion_v002 smile at mei_right
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion '旅先は枕が違うから、案外、熟睡できないんですよね。役に立って\nよかったです。'
 show mion_v002 smile at jump_transform,active
 show shion_v002 smile at inactive
 mion 'よっしゃああーー！！\u3000今日は最高にいいお天気！\u3000撮影日和\nだぁぁ！！'
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion '菜央さんは、ゆっくり刺繍をして過ごすんでしたよね？\u3000私たちの\nことは放っておいて、のんびりして下さいね。'
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show nao_v002 normal_close at mei_center
 with Dissolve(0.5)
 show nao_v002 normal_close at active
 nao '…………はい。'
 hide nao_v002
 with Dissolve(0.2)
 narrator '\u3000昨夜。……不気味な魔法陣に、あたしたち３人は驚いた。'
 narrator '\u3000……だが、それよりも驚いたことは、いつまでも驚いていたの\nが、あたしだけだったということだ。'
 narrator '\u3000なんと。魅音さんは唐突に、カラカラと笑い出したのだ。\n\u3000あの時は、突然の笑いに、魔女が憑依したのかと絶句してしまっ\nた。'
 narrator '\u3000だが違う。恐らく魅音さんは、魔女の#p祟#sたた#rりを装った悪戯であるこ\nとを、瞬時に見抜いたのだ。'
 narrator '\u3000……当然だ。魔女も魔法もある訳がない。ならば、誰かの悪戯で\nある以外に考えつくことはない。'
 narrator '\u3000あたしは血で描いた魔法陣だと勝手に思い込んだけれど。魅音さ\nんはすぐに絵の具によるものだと見破った。'
 narrator '\u3000予め、魔法陣を描いたシーツを用意しておき、隙を見て侵入し\nて、シーツを張り替えたのだ、と。'
 narrator '\u3000じゃあ……、それを誰がやったのか？\n\u3000昨夜の時点では、魅音さんも詩音さんも、それを断定することは\nなかった。'
 narrator '\u3000しかし。誰であろうとも、人間の仕業であることに疑問の余地は\nない、という強い意思があった。'
 narrator '\u3000だから魅音さんは、笑いながら「やってくれるねぇ」という言葉\nを口に出来る。'
 narrator '\u3000魅音さんのあの笑いは、見事な悪戯に、してやられたと笑う小学\n生のような気持ちだったのだ。'
 narrator '\u3000それを聞き、詩音さんもまた、笑い出し、園崎姉妹は、誰である\nにせよ、タイムリーなこの悪戯を面白がりさえしたのだ。'
 narrator '\u3000あたしは怖がりだから、ひょっとしたら本当に魔女の仕業かもと\n思って、怯えてしまっていた。'
 narrator '\u3000……いや、でも。あんな性質の悪い悪戯をされたら、誰だって絶\n句して当然だと思うけれど……。'
 narrator '\u3000……………うーーん……。'
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 nao '……あたしも二人を見習って、もっと打たれ強くならないといけな\nいかしら……。'
 hide nao_v002
 with Dissolve(0.2)
 narrator '\u3000だから。その怯えを魔女に付け込まれて、あんな夢を見る……。'
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao 'あの……。お二人は……、何か夢を見ましたか？'
 hide nao_v002
 with Dissolve(0.2)
 show mion_v002 smile at mei_right
 show shion_v002 fuan at mei_left
 with Dissolve(0.5)
 show shion_v002 fuan at active
 show mion_v002 smile at inactive
 shion '素敵な夢を見られるかと期待しましたが、私はさっぱりでした。お\n姉は、何か夢を見ました？'
 show mion_v002 smile_close at active
 show shion_v002 fuan at inactive
 mion '全然。快眠過ぎて、何の夢も見てないねぇ。'
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_526_door_open.wav'
 narrator '\u3000魅音さんは、今度は慎重に鍵を開け、窓を広げて、海と薔薇庭園\nを同時に眺められる絶景を満喫する。'
 narrator '\u3000………あの窓が、鍵になると思うのだ。\n\u3000紗音さんはマスターキーがあるから入室出来るけれど、……魔法\n陣のシーツには一切、関わっていない。'
 narrator '\u3000となれば、紗音さんが窓の鍵を直すまで、施錠されていなかった\n窓が怪しいのは当然のこと。'
 narrator '\u3000しかし、窓だろうと階段だろうと、……２階へは誰も行っていな\nいと赤き真実で言われている……。'
 show shion_v002 smile at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at jump_transform,active
 show shion_v002 smile at inactive
 mion 'さ、朝ごはん行こ！\u3000中日の今日が、この島へ来た一番の目的だか\nらね！'
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion 'そうですね！\u3000こんなすごいところで撮影できる機会なんて、そう\nそうないですから。'
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 show nao_v002 smile at mei_center
 with Dissolve(0.5)
 show nao_v002 smile at active
 nao 'お二人は、この島に撮影に来ていたんですね。'
 hide nao_v002
 with Dissolve(0.2)
 show nao_v002 smile at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at updown_shake_transform,active
 show nao_v002 smile at inactive
 mion '菜央ちゃんも一緒に撮るぅ？\u3000記念になるよ～？\u3000いっひっひっ\nひ。'
 show nao_v002 fuan at active
 show mion_v002 smile at inactive
 nao '……その笑いが気になるので遠慮します。'
 window hide None
 show expression "#000" as fade with Dissolve(1.0)
 hide nao_v002
 hide mion_v002
 with Dissolve(0.2)
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2371.png' as bg
 with Dissolve(1.0)
 show shion_v002 normal at mei_center
 with Dissolve(0.5)
 show shion_v002 normal at active
 shion 'ヱリカさんは……、おや、まだ寝てるみたいですねぇ？'
 hide shion_v002
 with Dissolve(0.2)
 narrator '\u3000ヱリカさんの部屋のドアノブには、ホテルでお馴染みの\n「起こさないで下さい」の札が掛けられていた。'
 show shion_v002 normal at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at active
 show shion_v002 normal at inactive
 mion 'ふふ～ん？\u3000実は中で、死体になってたりして……。'
 show shion_v002 fuan at active
 show mion_v002 smile at inactive
 shion 'お姉、さすがに不謹慎が過ぎます。'
 show expression "#000" as fade with Dissolve(1.0)
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 stop sound
 scene expression "#000"
 play music 'audio/bgm/BGM_GACHA_COLLAB2.wav'
 show expression 'images/bg/AdvBg_2331.png' as bg
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_515_tableware.wav'
 narrator '\u3000１階では郷田さんと嘉音さんが朝食の支度をしてくれていた。'
 show kanon_v001 normal at mei_center
 with Dissolve(0.5)
 show kanon_v001 normal at active
 kanon '……おはようございます。昨夜はよく眠れましたか。'
 hide kanon_v001
 with Dissolve(0.2)
 Character('Gohda',ctc="ctcArrow", ctc_position="fixed") 'さぁさぁ、御着席を。古戸さまは、まだお休みでしょうか？'
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao 'ドアノブに、起こさないで下さいって札を掛けてました。'
 hide nao_v002
 with Dissolve(0.2)
 show kanon_v001 normal_目閉じ at mei_right
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_215_heartgrow.wav'
 show shion_v002 smile at jump_transform,active
 show kanon_v001 normal_目閉じ at inactive
 shion 'わ～、このポーチドエッグ、すっごい可愛らしいですよ～！'
 show kanon_v001 normal at active
 show shion_v002 smile at inactive
 kanon '当家のシェフ、郷田が腕を振るいました。'
 hide shion_v002
 show nao_v002 smile at mei_left
 with Dissolve(0.5)
 show nao_v002 smile at active
 show kanon_v001 normal at inactive
 nao '本当、見事なセンスですよね。'
 hide kanon_v001
 hide nao_v002
 with Dissolve(0.2)
 Character('Gohda',ctc="ctcArrow", ctc_position="fixed") 'いえいえ、これしき。んなっはっはっは……。'
 narrator '\u3000若い娘たちに褒められて、郷田さんは赤面して照れる。……可愛\nい人だ。'
 narrator '\u3000配膳を済ませると、御用がありましたらベルでお呼びくださいと\n言い残し、使用人たちは退出する。'
 narrator '\u3000あたしはまだ……、昨夜の魔法陣のショックと、夢の中での魔女\nとの推理バトルの影響が抜けなくて、ぼんやりしている。'
 narrator '\u3000一方、園崎姉妹は、昨日のことなんかなかったかのように元気全\n開。朝食から全力で食いまくりだ。'
 show shion_v002 smile at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at active
 show shion_v002 smile at inactive
 mion 'いやぁ、それにしても昨夜のボドゲは楽しかったねぇ！'
 show shion_v002 fuan at active
 show mion_v002 smile at inactive
 shion 'お姉のアレ。絶対に次のルール改定でエラッタが出ますよ。あんな\nの許される訳がないです。'
 show mion_v002 normal at active
 show shion_v002 fuan at inactive
 mion 'いい？\u3000ゲームも現実もね、とにかく徹底的にテキストを読み込む\nの。どこに罠があるかわからない！'
 show mion_v002 smile at active
 show shion_v002 fuan at inactive
 mion '逆に、決定的なチャンスを自分だけが見付けたなら、それは大きな\n武器になる！\u3000昨日の私みたいにねぇ！'
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao '……………………。'
 hide nao_v002
 with Dissolve(0.2)
 show mion_v002 smile at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show mion_v002 smile at inactive
 nao '……あの、魅音さん。ちょっと、あたしの話を聞いてもらってもい\nいですか？'
 show mion_v002 smile at active
 show nao_v002 normal at inactive
 mion 'ん？\u3000何？'
 stop music fadeout 2.0
 hide mion_v002
 hide nao_v002
 with Dissolve(0.2)
 narrator '\u3000話してみよう。……あの夢の中の、魔女との推理バトルのこと\nを。'
 play music 'audio/bgm/BGM_QUEST5_COLLAB2.wav'
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao '実は昨夜、こんな夢を見たんです。……すごく鮮明に覚えてい\nて……。'
 hide nao_v002
 with Dissolve(0.2)
 narrator '\u3000最初は、魔女の夢を見たとの話に、昨夜のことを怖がり過ぎだ\nよ～と、ちょっと小馬鹿にもされた。'
 narrator '\u3000……いやいや、魅音さん。あの魔法陣は、普通のセンスの人な\nら、引っ繰り返って当然です。'
 narrator '\u3000だが、魔女とのゲームの話になり、青と赤の、２つの真実を使っ\nた戦いの話になると、魅音さんは目付きを鋭くして話に聞き入って\nくれた……。'
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao 'こんな感じです。……お二人はやっぱり、紗音さんを疑っています\nか？'
 show nao_v002 normal at active
 nao 'あたしもそうだったんですが、夢の中の魔女は、紗音さんは一切関\nわっていないと赤き真実で言いました。'
 hide nao_v002
 with Dissolve(0.2)
 show shion_v002 normal at mei_left
 show mion_v002 normal at mei_right
 with Dissolve(0.5)
 show mion_v002 normal at active
 show shion_v002 normal at inactive
 mion 'ふぅん。なるほどなるほど……。菜央ちゃんは夢の中でも頑張って\n考えてたんだねぇ。'
 play audio 'audio/sfx/SE_006_WindowScroll.wav'
 show shion_v002 normal at active
 show mion_v002 normal at inactive
 shion 'ベアトリーチェが言ったという、赤き真実。メモったんですけど、\nこれで合ってますか？'
 hide shion_v002
 hide mion_v002
 with Dissolve(0.2)
 narrator '\u3000詩音さんは、ゲームの要となる赤き真実を、ペーパーナプキンに\n書き留めていた。'
 narrator '\u3000確認する。……うん。ベアトリーチェが言ったことと、一言一\n句、同じだと思う。'
 show shion_v002 normal at mei_left
 show mion_v002 normal at mei_right
 with Dissolve(0.5)
 show mion_v002 normal at active
 show shion_v002 normal at inactive
 mion 'まぁ、普通に考えると、やっぱり紗音さんが怪しいよねぇ。'
 show shion_v002 normal at active
 show mion_v002 normal at inactive
 shion '#ff0000紗音は、魔法陣のシーツを菜央のベッドに敷く行為には、直接的に#r\n#ff0000も間接的にも一切、関わっていない、#r'
 show shion_v002 fuan at active
 show mion_v002 normal at inactive
 shion 'っていうのが結構、効いてますね。'
 show mion_v002 fuan at active
 show shion_v002 fuan at inactive
 mion '間接的の範囲が、かなり広いからね。……紗音さんの入室行為をト\nリックに絡めようとしたら、間接的って部分に抵触しちゃうよ？'
 show mion_v002 smile at active
 show shion_v002 fuan at inactive
 mion 'というか、元々、おじさんは紗音さんを疑ってなんかないし。'
 hide shion_v002
 show nao_v002 odoroki at mei_left
 with Dissolve(0.5)
 show nao_v002 odoroki at active
 show mion_v002 smile at inactive
 nao 'え？\u3000何かその根拠、あるんですか？'
 play audio 'audio/sfx/SE_326_ls_spacestop.wav'
 show mion_v002 smile at active
 show nao_v002 odoroki at inactive
 mion 'やらなさそうだから。'
 hide mion_v002
 hide nao_v002
 with Dissolve(0.2)
 narrator '\u3000ババーン。魅音さん空間だったら、何の根拠もなく赤き真実で言\nえてしまいそうだ……。'
 show nao_v002 normal at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at active
 show nao_v002 normal at inactive
 mion '紗音さんは昨夜。菜央ちゃんが窓の鍵の話をする直前に、“本日は\nこれで失礼させていただきます”って言ったんだよ。'
 show mion_v002 smile at active
 show nao_v002 normal at inactive
 mion 'あれは、今日はこれで仕事をあがる、って意味だよ。つまり、あの\nまま、宿直室か何かに帰るつもりだったんだよ。'
 show nao_v002 normal at active
 show mion_v002 smile at inactive
 nao '……あたしが窓の話をしたから２階に上がっただけで、それは予定\nにない行為……。'
 show mion_v002 smile_close at nod_transform,active
 show nao_v002 normal at inactive
 mion 'そゆこと。そして私たちの部屋に立ち入った時間もわずかだった。'
 show mion_v002 smile at active
 show nao_v002 normal at inactive
 mion '予定にない行為と、わずかな時間。普通に考えて、紗音さんにあの\n悪戯をする時間的余裕はないね。'
 hide nao_v002
 show shion_v002 normal at mei_left
 with Dissolve(0.5)
 show shion_v002 normal at active
 show mion_v002 smile at inactive
 shion 'さらに赤き真実で、紗音さんは魔法陣の有無に関わらず、シーツに\nさえ触っていないと明言されていますし。'
 show mion_v002 smile at updown_shake_transform,active
 show shion_v002 normal at inactive
 mion 'それにさ、あんな儚い感じの可愛い子が、あんな悪趣味な悪戯をす\nるなんて、おじさんはちょっと思えないもんね～！'
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao '………………………。'
 hide nao_v002
 with Dissolve(0.2)
 narrator '\u3000すごい。……赤き真実は一切ないけれど、すごい説得力だ。'
 narrator '\u3000確かに、昨夜のあたしはショックで冷静さを欠いていたけれど。\n\u3000魅音さんの言う通りに冷静に思考を巡らせれば、……初見で紗音\nさんを疑いから外せるのだ。'
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao 'じゃあ、紗音さんに無理なら……、誰に可能だったんですか？'
 hide nao_v002
 with Dissolve(0.2)
 show mion_v002 smile at mei_right
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion 'うふふふ。紗音さん以外の誰も２階に行っていないという赤き真実\nが邪魔になるんですよね？'
 play audio 'audio/sfx/SE_226_shine.wav'
 show mion_v002 futeki at active
 show shion_v002 smile at inactive
 mion 'そこがさっきおじさんが言ったことだよ。テキストは、よ～く読み\n込まなくちゃねぇ。'
 show shion_v002 normal at active
 show mion_v002 futeki at inactive
 shion '#ff0000そなたたちが施錠してから、再び開錠するまでの間、紗音を除い#r\n#ff0000て、ゲストハウス２階に訪れた者はいない、#r'
 show shion_v002 smile at active
 show mion_v002 futeki at inactive
 shion 'でしたよね？'
 show mion_v002 futeki at active
 show shion_v002 smile at inactive
 mion '訪れた者はいなくても、待機していた者はいるかもねぇ？'
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show nao_v002 odoroki at mei_center
 with Dissolve(0.5)
 show nao_v002 odoroki at active
 nao 'え、待機………。'
 hide nao_v002
 with Dissolve(0.2)
 show mion_v002 futeki at mei_right
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at active
 show mion_v002 futeki at inactive
 shion '施錠から開錠までの間、２階に行っちゃいけない訳ですよね？'
 show mion_v002 smile at active
 show shion_v002 smile at inactive
 mion 'それ以前に、２階に行っちゃってればいい。'
 show mion_v002 smile at active
 show shion_v002 smile at inactive
 mion 'つまり。施錠から開錠までの間に、すでに２階に滞在してれば、\nなぁんの問題もないワケ！'
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show nao_v002 odoroki at mei_center
 with Dissolve(0.5)
 show nao_v002 odoroki at active
 nao 'あ、……あ、…………。'
 hide nao_v002
 with Dissolve(0.2)
 narrator '\u3000何て下らない言葉遊び……！！\u3000まんまとやられたわ。\n\u3000犯人はこの悪戯の為に、ずっと２階に潜み、……機会を伺ってい\nたのだ……！'
 show mion_v002 smile at mei_right
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at active
 show mion_v002 smile at inactive
 nao 'で、でも。紗音さんは間接的にも一切、関わっていないんですよ\nね？'
 show nao_v002 fuan at active
 show mion_v002 smile at inactive
 nao 'つまり、紗音さんが鍵を開け閉めした隙を突けば、紗音さんは間接\n的に幇助したことになってしまう……。'
 show mion_v002 smile at active
 show nao_v002 fuan at inactive
 mion '窓は、入れたでしょ？'
 show nao_v002 odoroki at active
 show mion_v002 smile at inactive
 nao 'じゃあ……、犯人は、２階の他の部屋に潜み……、外壁を伝うか何\nかして、窓から侵入したってことですか……？！'
 show mion_v002 smile at active
 show nao_v002 odoroki at inactive
 mion '昨夜は真っ暗だったからわからなかったけれど。おじさんは朝、窓\nを開けて、外壁を確認したんだよ。'
 show mion_v002 smile at active
 show nao_v002 odoroki at inactive
 mion '露骨な痕跡はなかったけれど、下の階の庇がいい感じの足場になっ\nてた。'
 hide nao_v002
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion 'まぁ、これが部活だったなら、お姉どころか、部活メンバーなら誰\nでも足場に使うでしょうねぇ。'
 show mion_v002 futeki at updown_shake_transform,active
 show shion_v002 smile at inactive
 mion '犯人もやるねぇ。くっくっく。部活に誘ってやりたいくらいだよ。'
 hide shion_v002
 show nao_v002 sinken at mei_left
 with Dissolve(0.5)
 show nao_v002 sinken at active
 show mion_v002 futeki at inactive
 nao 'じゃ、じゃあ、犯人は一体……？！'
 show mion_v002 futeki at active
 show nao_v002 sinken at inactive
 mion 'おじさんたち以外に、昨夜、ゲストハウスの２階に滞在してた\n人、ってことになるねぇ……？'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide mion_v002
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 normal at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 normal at active
 erika 'おはようございます。のんびり、朝寝坊をさせていただきました。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 narrator '\u3000その時。ヱリカさんが降りて来た。清々しい笑顔で微笑みかけて\nくる。'
 narrator '\u3000ヱリカさんがベルを鳴らすと、やや遅れて、嘉音さんがやってき\nた。'
 play audio 'audio/sfx/SE_515_tableware.wav'
 narrator '\u3000朝食の用意を頼むと、ナイフやフォークをざらりと避けて、自慢\nのマイ箸を準備するのだった。'
 show erika_v001 normal at mei_right
 show mion_v002 smile at mei_left
 with Dissolve(0.5)
 show mion_v002 smile at active
 show erika_v001 normal at inactive
 mion 'ヱリカさん、おはよー。今日もその髪、バッチリ決まってるねぇ！'
 show erika_v001 normal at active
 show mion_v002 smile at inactive
 erika 'ありがとうございます。今日は最高のお日和ですね。'
 show erika_v001 normal at active
 show mion_v002 smile at inactive
 erika '私も、薔薇庭園の東屋で、のんびり読書でもしようかと思っていま\nす。'
 show erika_v001 normal at active
 show mion_v002 smile at inactive
 erika 'そういえば菜央ちゃまは、薔薇庭園を眺めながら刺繍をするんでし\nたっけ？'
 hide erika_v001
 hide mion_v002
 with Dissolve(0.2)
 narrator '\u3000清々しい笑顔？\u3000……違うわ、この笑みは。\n\u3000昨日のアレ、お楽しみいただけました？\u3000という問い掛けの笑み\nだ。'
 narrator '\u3000……ヱリカさん、……あなたですね、あの性質の悪い悪戯をした\nのは……。'
 window hide None
 show expression "#000" as fade with Dissolve(1.0)
 stop music fadeout 0.5
 pause 4.0
 stop sound
 scene expression "#000"
 play music 'audio/bgm/BGM_GACHA_COLLAB2.wav'
 show expression 'images/bg/AdvBg_2281.png' as bg
 with Dissolve(1.0)
 narrator '\u3000朝食を先に終えたあたしたちは、一度部屋に戻る。'
 show expression "#000" as fade with Dissolve(1.0)
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2371.png' as bg
 with Dissolve(1.0)
 narrator '\u3000そして、今日を過ごす為のそれぞれの持ち物を手に、再び階段を\n降りた。'
 narrator '\u3000あたしは、刺繍の道具と、読みかけの本をバッグに入れて。\n\u3000園崎姉妹は、あのバカでかいトランクを持って。'
 show mion_v002 smile at mei_center
 with Dissolve(0.5)
 show mion_v002 smile at active
 mion 'あと、これは御守りね。'
 hide mion_v002
 with Dissolve(0.2)
 narrator '\u3000魅音さんは、ベッドメイク不要の札をドアノブに掛けていた。\n\u3000……何の御守りになるのか、よくわからない。'
 play audio 'audio/sfx/SE_5056_toy.wav'
 narrator '\u3000しばらくの間、ドアノブで何かゴソゴソやっていたが、何をして\nるのかよくわからなかった。'
 show shion_v002 smile at mei_center
 with Dissolve(0.5)
 show shion_v002 smile at active
 shion 'くす。今は忘れてくれて大丈夫ですよ。さ、お姉も終わりました。\n下に降りましょう！'
 window hide None
 show expression "#000" as fade with Dissolve(1.0)
 hide shion_v002
 with Dissolve(0.2)
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2331.png' as bg
 with Dissolve(1.0)
 narrator '\u3000３人で階段を降り、１階広間に戻ると、ヱリカさんがちょうど、\n朝食を終えたところだった。'
 show erika_v001 normal at mei_right
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at active
 show erika_v001 normal at inactive
 shion '私たちは今日は、薔薇庭園のあちこちで、色々と撮影をしますの\nで。'
 show erika_v001 normal at active
 show shion_v002 smile at inactive
 erika 'どうぞお好きなようにお過ごしを。私を写さないでさえくれれば、\n何も気にしませんので。'
 hide shion_v002
 show mion_v002 smile at mei_left
 with Dissolve(0.5)
 show mion_v002 smile at active
 show erika_v001 normal at inactive
 mion 'ヱリカさんは何をして過ごすの？'
 show erika_v001 normal at active
 show mion_v002 smile at inactive
 erika '今日は変わり種のミステリーの本を持ってきてますので、薔薇庭園\nでのんびりと読書の予定です。'
 show mion_v002 smile at active
 show erika_v001 normal at inactive
 mion 'へー！\u3000何て本？'
 show erika_v001 normal_close at active
 show mion_v002 smile at inactive
 erika 'いえいえ。一般的な分類では、ラブロマンスというジャンルなんで\nすが。私にはとてもミステリーなんです。'
 show erika_v001 smile at active
 show mion_v002 smile at inactive
 erika 'どうして、それが恋をする動機になるのか？\u3000とか、どうして、リ\nスクヘッジもせずに恋愛の地雷原に踏み込むのか？\u3000とか。'
 show erika_v001 normal at active
 show mion_v002 smile at inactive
 erika '恋愛至上主義者たちの行動理念は、私にとっては、並のミステリー\nよりも読み応えがあるんです。'
 show mion_v002 smile at updown_shake_transform,active
 show erika_v001 normal at inactive
 mion 'はははは。おじさんもちょっとわかるよ。下手な推理小説よりも、\n女心はミステリーかもしれない。'
 show erika_v001 normal at active
 show mion_v002 smile at inactive
 erika '探偵たる者、殺人の動機として古来より代表格に数えられる“恋愛\n感情”というものを、勉強しておいて損はありませんので。'
 hide mion_v002
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at active
 show erika_v001 normal at inactive
 shion 'ヱリカさん？\u3000恋は理屈じゃない。ビビーンと来たら、ドキュー\nン、バキューン♪\u3000ですよ。'
 hide erika_v001
 hide shion_v002
 with Dissolve(0.2)
 narrator '\u3000ドキューン、バキューン？？\u3000やっぱり、殺人の動機になり得る\nわね……。'
 narrator '\u3000ヱリカさんは、もう読みたい本を持ってきているようで、部屋に\n戻らず、このまま出るつもりのようだ。'
 narrator '\u3000あたしたちは４人で、ぞろぞろとゲストハウスを出るのだっ\nた……。'
 window hide None
 show expression "#000" as fade with Dissolve(1.0)
 stop sound
 scene expression "#000"
 play music 'audio/bgm/BGM_HOME_COLLAB2.wav'
 show expression 'images/bg/AdvBg_2221.png' as bg
 with Dissolve(1.0)
 show shion_v004 smile at mei_left
 show mion_v005 smile at mei_right
 with Dissolve(0.5)
 show mion_v005 smile at active
 show shion_v004 smile at inactive
 mion 'じゃー、適当にどんどん、ポーズとってみよっかぁ！'
 play audio 'audio/sfx/SE_562_ls_mahouball1.wav'
 show shion_v004 smile at jumping_transform,active
 show mion_v005 smile at inactive
 shion 'ハァイ♪\u3000お姉に私の可愛さ、撮り切れますかぁ？？'
 play audio 'audio/sfx/SE_201_shutter.wav'
 pause 0.6666666666666666
 play audio 'audio/sfx/SE_201_shutter.wav'
 pause 0.6666666666666666
 play audio 'audio/sfx/SE_201_shutter.wav'
 pause 0.6666666666666666
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide shion_v004
 hide mion_v005
 hide fade with Dissolve(0.08333333333333333)
 show jessica_v001 odoroki at mei_center
 with Dissolve(0.08333333333333333)
 show jessica_v001 odoroki at active
 jessica '……うお！\u3000何やってんだよッ？！\u3000これってアレだろ？\u3000コスプ\nレ撮影ってヤツだろー？！'
 show jessica_v001 fuan_blush at chara_shake_transform,active
 jessica 'うわーうわーうわー、ろ、露出多くない？\u3000セクシー過ぎない？！'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide jessica_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 narrator '\u3000と言いながら、朱志香さんは興味津々だ。'
 show jessica_v001 fuan_blush at mei_right
 show shion_v004 smile at mei_left
 with Dissolve(0.5)
 show shion_v004 smile at active
 show jessica_v001 fuan_blush at inactive
 shion '朱志香さんもご一緒にどうですぅ？\u3000やってみるとクセになります\nよ～♪'
 show jessica_v001 smile at active
 show shion_v004 smile at inactive
 jessica 'い、いやいや！\u3000私は見てるだけでいーぜ！\u3000っていうか、カメラ\n変わろっか？\u3000二人を撮るぜ？'
 hide shion_v004
 show mion_v005 odoroki at mei_left
 with Dissolve(0.5)
 show mion_v005 odoroki at active
 show jessica_v001 smile at inactive
 mion 'え？\u3000ホント？！\u3000それは助かるなぁ！\u3000一眼レフ、扱えるぅ？'
 show jessica_v001 smile at nod_transform,active
 show mion_v005 odoroki at inactive
 jessica '任せろよ！\u3000親父のカメラ、一時は親父よりいじってたんだぜ。'
 hide jessica_v001
 hide mion_v005
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao '……てっきり、薔薇の写真を撮るのだと思ってました。まさか、コ\nスプレ撮影とは。'
 hide nao_v002
 with Dissolve(0.2)
 show mion_v005 smile at mei_right
 show shion_v004 smile at mei_left
 with Dissolve(0.5)
 show shion_v004 smile at active
 show mion_v005 smile at inactive
 shion 'ロケーションもすっごい大事なんですよ？\u3000白ホリで撮るのと、こ\nこで撮るのじゃ、全然違ってきますから。'
 show mion_v005 smile at active
 show shion_v004 smile at inactive
 mion 'これもね、叔父さんに頼まれた仕事なんだよねぇ。エンジェルモー\nトの次のキャンペーンに使うんだってさ！'
 show shion_v004 smile at active
 show mion_v005 smile at inactive
 shion 'キャンペーン対象メニューを頼むと、ランダムで魅惑のエンジェル\nモートウェイトレスの写真がもらえるんだそうです。'
 hide mion_v005
 hide shion_v004
 with Dissolve(0.2)
 show jessica_v001 smile_blush at mei_center
 with Dissolve(0.5)
 show jessica_v001 smile_blush at active
 jessica 'じゃあ撮るぜー！\u3000好きなポーズで頼むぜ！\u3000わ、大胆っ、せく\nしぃ……。'
 hide jessica_v001
 with Dissolve(0.2)
 narrator '\u3000六軒島で孤独に生きて来た朱志香さんにとって、魅音さんたちの\n世界は、まさに異世界なのだろう。'
 narrator '\u3000今回のバカンスで、一番楽しんでいる人は誰か挙げろと言われた\nら、あたしは朱志香さんを推すだろう。'
 narrator '\u3000……さて。彼女たちは彼女たち。あたしも、自分の時間を過ごさ\nなきゃ。'
 narrator '\u3000薔薇に囲まれて、のんびりと刺繍に没頭できるのはどこだろ\nう……？'
 stop music fadeout 2.0
 show expression "#000" as fade with Dissolve(1.0)
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2341.png' as bg
 with Dissolve(1.0)
 show nao_v002 fuan_close at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan_close at active
 nao 'となれば、……同じところに行きつく訳ね。'
 play music 'audio/bgm/BGM_QUEST5_COLLAB2.wav'
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show nao_v002 fuan_close at inactive
 erika 'おや、菜央ちゃま。……貴女も如何です？\u3000ここは最高ですよ。'
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 narrator '\u3000薔薇庭園の絶景に囲まれた、最高のロケーション。………東屋。'
 narrator '\u3000そこに洒落たテーブルと椅子があるのだが、……サイアクの先客\nがいた……。'
 show nao_v002 fuan_close at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show nao_v002 fuan_close at inactive
 erika '別に話し掛けたりしませんので。座ったらどうです？'
 show nao_v002 normal at active
 show erika_v001 normal at inactive
 nao '……お邪魔でしょうから、別の場所を探すわ。'
 show erika_v001 normal_close at active
 show nao_v002 normal at inactive
 erika 'この薔薇庭園に出てからの貴女の行動は全て観察しています。'
 show erika_v001 normal at active
 show nao_v002 normal at inactive
 erika '貴女はすでに、この場所以外には、刺繍をするのに最適な場所がな\nいことを、ご存知のはずですよ？'
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 narrator '\u3000気持ち悪い……。読書じゃなくて、あたしをずっと観察してた\nの？'
 narrator '\u3000やっぱり、この人とは馬が合わない。というか、はっきりと敵意\nを感じるのだ。'
 narrator '\u3000そう思ったら、ここで背中を向けるのは、負けを認めるような気\n持ちになる。……逃げたりするものか。'
 show erika_v001 normal at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_528_unfold_cloth.wav'
 show nao_v002 normal at active
 show erika_v001 normal at inactive
 nao '……ありがとうございます。……じゃあ、お向かいの席、失礼しま\nす。'
 show erika_v001 normal at active
 show nao_v002 normal at inactive
 erika 'グッド。'
 hide erika_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator '\u3000いい度胸です、……とでも言ったところだろうか。'
 narrator '\u3000もう。……何で、こんな素敵な薔薇庭園でのバカンスなのに、苦\n手なクラスメートと二人組を作らされたような気分にならなきゃい\nけないのよ……。'
 narrator '\u3000うぅん。あたしは、すでに喧嘩を売られているのよ。買うか、逃\nげるかの２つに１つ。'
 narrator '\u3000だって彼女は、あたしのベッドに、あんなに酷い悪戯を……！'
 show erika_v001 normal at mei_right
 show nao_v002 normal_close at mei_left
 with Dissolve(0.5)
 show nao_v002 normal_close at active
 show erika_v001 normal at inactive
 nao '……昨夜は、やってくれましたね。'
 show erika_v001 normal at active
 show nao_v002 normal_close at inactive
 erika 'ハイ？\u3000何の話でしょう？'
 hide erika_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator '\u3000セリフは惚けているが、そのニヤリという表情は明白なイエス\nだ。'
 show nao_v002 normal_close at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show nao_v002 normal_close at inactive
 erika '昨夜、あったらしい何かについて、私との議論をお望みとお見受け\nします。'
 show erika_v001 normal at active
 show nao_v002 normal_close at inactive
 erika 'ただ、私は昨夜、貴女の身に何があったのかをよく存じません。'
 show nao_v002 sinken at chara_shake_transform,active
 show erika_v001 normal at inactive
 nao 'し、白々しい……。'
 show erika_v001 smile at active
 show nao_v002 sinken at inactive
 erika 'なので、私にもわかるように、丁寧にお教え願えますか？\u3000うっ\nふっふっふ……。'
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 narrator '\u3000喧嘩の売買成立。もうこうなったらやってやるわ。鳳谷菜央、\n買った喧嘩は値切らないわよ……。'