label event01_30_06:
 stop sound
 scene expression "#000"
 play music 'audio/bgm/BGM_QUEST1_COLLAB2.wav'
 show expression 'images/bg/AdvBg_2341.png' as bg
 with Dissolve(1.0)
 show erika_v001 normal at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show erika_v001 normal at inactive
 nao '紗音さんに濡れ衣を被せようとしてもダメです。あの悪戯の犯人は\nあなたです。ヱリカさん。'
 show erika_v001 normal at active
 show nao_v002 normal at inactive
 erika 'それ、気持ちいいでしょう？'
 show nao_v002 fuan at active
 show erika_v001 normal at inactive
 nao 'はい？'
 show erika_v001 normal at active
 show nao_v002 fuan at inactive
 erika '“犯人は、あなたです”。……その言葉を口にする瞬間こそが、探\n偵の悦楽の究極にして最高峰！'
 show erika_v001 normal at active
 show nao_v002 fuan at inactive
 erika 'もちろん、犯人がその言葉で簡単に屈することはありません。'
 show erika_v001 futeki at active
 show nao_v002 fuan at inactive
 erika 'それこそ、窮鼠猫を噛むの勢いで反論してくるでしょう。しかし、\nそれを崩すのがまたいい！'
 show nao_v002 normal at active
 show erika_v001 futeki at inactive
 nao '……つまり、ヱリカさんは模範的な犯人役を演じてくれる、という\nことですよね？'
 show erika_v001 normal_close at active
 show nao_v002 normal at inactive
 erika '貴女が探偵としての究極の悦楽を得られるか……。'
 show erika_v001 fuan at active
 show nao_v002 normal at inactive
 erika 'さもなくば、探偵の解決の直前に披露される、ナントカ警部のヘッ\nポコ推理の役になるのか。くっくっく！'
 show nao_v002 normal at active
 show erika_v001 fuan at inactive
 nao 'では、ヱリカさん。反論してもらいます。どうしてあなたは犯人で\nはないと？'
 show erika_v001 normal at active
 show nao_v002 normal at inactive
 erika '非常にシンプルな話です。私にはアリバイがあるからです。'
 show nao_v002 odoroki at active
 show erika_v001 normal at inactive
 nao 'アリバイ……？'
 show erika_v001 normal at active
 show nao_v002 odoroki at inactive
 erika 'お忘れですか？\u3000私は貴女たちと一緒に、郷田さんの素敵な創作ス\nペイン料理をいただいたではありませんか。'
 show erika_v001 normal at active
 show nao_v002 odoroki at inactive
 erika 'そして、食事を終えて、そのまま朱志香さんのボードゲームにも参\n加しました。'
 show erika_v001 normal at active
 show nao_v002 odoroki at inactive
 erika 'その後、遅くまで遊び、皆さんと一緒に２階へ上がったはずです。'
 show erika_v001 normal at active
 show nao_v002 odoroki at inactive
 erika 'その間、私はわずかの時間でも、皆さんの前から姿を消したことが\nありましたか？'
 show nao_v002 normal at active
 show erika_v001 normal at inactive
 nao '………………………。'
 hide erika_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator '\u3000確かに、それは鉄壁のアリバイだ。他ならぬ、あたしとずっと一\n緒にいたのだから。'
 show erika_v001 normal at mei_right
 show nao_v002 normal_close at mei_left
 with Dissolve(0.5)
 show nao_v002 normal_close at active
 show erika_v001 normal at inactive
 nao 'いや、………犯行のチャンスはあるわ。'
 show erika_v001 normal at active
 show nao_v002 normal_close at inactive
 erika 'おや。それはどのタイミングで？'
 show nao_v002 normal at active
 show erika_v001 normal at inactive
 nao '一番最初だわ。あなたは、髪が整わなくてと言って、夕食に来るの\nが遅れたじゃない。'
 show nao_v002 normal at active
 show erika_v001 normal at inactive
 nao 'それに、あなたはあたしたちの部屋の窓が、壊れて施錠出来なく\nなっていることを知ってたわ。'
 hide erika_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator '\u3000シーツの魔法陣も、用意には手間が掛かるが、予め準備する時間\nは十分にあった。'
 narrator '\u3000そして、夕食の時にあたしたちが先に下へ降りたのを確認した上\nで、窓から出て、１階の庇の上を歩き、あたしたちの部屋の窓から\n入った！'
 show nao_v002 normal at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show nao_v002 normal at inactive
 erika 'グッド。悪くはありません。'
 show erika_v001 normal_close at active
 show nao_v002 normal at inactive
 erika 'しかし、良くもない。'
 show nao_v002 normal at active
 show erika_v001 normal_close at inactive
 nao '反論があるかしら？'
 show erika_v001 normal at nod_transform,active
 show nao_v002 normal at inactive
 erika 'もちろん。……貴女の言う通りだとすると、私が魔法陣の悪戯をし\nたのは、夕食の早い段階だということになります。'
 show erika_v001 normal at active
 show nao_v002 normal at inactive
 erika 'つまり。紗音さんが入室するのは、その後と言う事です。'
 show erika_v001 normal at active
 show nao_v002 normal at inactive
 erika '貴女のベッドが、仰られるような壮絶な状況だったとしたら、彼女\nが何事もなく帰ってくると思いますか……？'
 show nao_v002 fuan at active
 show erika_v001 normal at inactive
 nao '……………………………。'
 show erika_v001 normal at active
 show nao_v002 fuan at inactive
 erika '私は紗音さんが戻ってきた時。ふざけて、窓から泥棒が入って部屋\nを荒らしたりはしていなかったかと聞いたのを覚えていますか？'
 show nao_v002 fuan at active
 show erika_v001 normal at inactive
 nao '……そんなこと……言ったような……。'
 show erika_v001 normal_close at active
 show nao_v002 fuan at inactive
 erika 'それに対する彼女の返事が、“いいえ、ご安心を”でした。'
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 narrator '\u3000魅音さんと詩音さんの心臓がタフ過ぎるから、あんな悪戯、下ら\nないもののように思える。'
 narrator '\u3000しかし。……普通のセンスの客たちだったなら、全員、絶叫して\n部屋から飛び出すほどの悪戯だった。'
 narrator '\u3000それを見て、“いいえ、ご安心を”という言葉が出るだろう\nか……？'
 show erika_v001 normal at mei_right
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at active
 show erika_v001 normal at inactive
 nao 'そ、それはきっと……、考えられることは、貴女と紗音さんが、'
 show expression "#e11" as fade with Dissolve(0.16666666666666666)
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 hide fade with Dissolve(0.16666666666666666)
 with Dissolve(0.16666666666666666)
 show erika_v001 normal at active
 show nao_v002 fuan at inactive
 erika '#ff0000私と紗音さんは、示し合わせてなどいません。#r'
 hide erika_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator '\u3000え？\u3000……今、ヱリカさんの声色が、何かとても……不思議だっ\nた。'
 narrator '\u3000根拠を示すことなく、真実を語る言葉に聞こえた……。'
 show nao_v002 fuan at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show nao_v002 fuan at inactive
 erika 'よって、私が紗音さんに予め因果を含め、魔法陣の悪戯を見て見ぬ\nフリをしろ、などと言い含めたことはあり得ないということです。'
 show nao_v002 fuan_close at active
 show erika_v001 normal at inactive
 nao '………ん……………。'
 show erika_v001 normal at active
 show nao_v002 fuan_close at inactive
 erika 'よって、私が犯人であるならば、犯行の機会は紗音さんが部屋を出\nてからしかない。'
 show erika_v001 normal at active
 show nao_v002 fuan_close at inactive
 erika 'しかしながら、その時間の全ては、貴女たちと一緒にゲームをして\n過ごしていたのですから、アリバイは完璧という訳です。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide nao_v002
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 show nao_v002 sinken at mei_center
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_510_sand_foot.wav'
 show nao_v002 sinken at chara_shake_transform,active
 nao 'あ、……あたし、紗音さんに直接、聞いてきますっ。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show erika_v001 normal_close at mei_center
 with Dissolve(0.5)
 show erika_v001 normal_close at active
 erika 'ちなみにですが、紗音さんは、今日からお休みだそうです。'
 show erika_v001 normal at active
 erika '右代宮家は、使用人の権利やプライバシーにも十分に配慮している\nそうですから、お休みの紗音さんに伝言を頼むことは出来ても、連\n絡を取ってもらうことは出来ませんよ？'
 hide erika_v001
 with Dissolve(0.2)
 narrator '\u3000つまり、……昨夜、本当に魔法陣の悪戯がなかったかどうかなど\nを、尋ねることが出来ないということ……？'
 show nao_v002 sinken at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show nao_v002 sinken at inactive
 erika '今日と明日がお休みだそうなので、明日の日曜には帰る菜央ちゃま\nにはもう、話を聞く機会はない、という訳です。'
 show nao_v002 sinken at active
 show erika_v001 normal at inactive
 nao 'く…………………。'
 stop music fadeout 2.0
 window hide None
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 pause 2.0
 play music 'audio/bgm/BGM_HOME_COLLAB2.wav'
 show shion_v008 smile at mei_left
 show mion_v014 smile at mei_right
 with Dissolve(0.5)
 show mion_v014 smile at active
 show shion_v008 smile at inactive
 mion 'はー、疲れたねぇ！\u3000ちょっと休憩しよっかぁ。'
 show shion_v008 smile at active
 show mion_v014 smile at inactive
 shion 'あれ？\u3000菜央さん、刺繍はしてないんですか？'
 hide shion_v008
 hide mion_v014
 with Dissolve(0.2)
 show erika_v001 normal at mei_right
 show nao_v002 normal_close at mei_left
 with Dissolve(0.5)
 show nao_v002 normal_close at active
 show erika_v001 normal at inactive
 nao '……ヱリカさんとのおしゃべりが盛り上がっちゃって。'
 show erika_v001 normal at active
 show nao_v002 normal_close at inactive
 erika 'ちょうど、今、盛り下がったところですので。'
 hide erika_v001
 hide nao_v002
 with Dissolve(0.2)
 show shion_v008 smile at mei_left
 show jessica_v001 smile_blush at mei_right
 with Dissolve(0.5)
 show jessica_v001 smile_blush at active
 show shion_v008 smile at inactive
 jessica '私もコスプレ、ちょっと興味が出て来たかなぁ……。嘉音くんが気\nに入ってくれるのってどんなカッコだろ……。'
 play audio 'audio/sfx/SE_215_heartgrow.wav'
 show shion_v008 smile at jumping_transform,active
 show jessica_v001 smile_blush at inactive
 shion 'そういう動機、大歓迎ですよぉ？\u3000美は、見てくれる人のことを想\nって養うものですから♪'
 show jessica_v001 odoroki_blush at active
 show shion_v008 smile at inactive
 jessica 'い、いやいやっ、べ、別に嘉音くんはそういう関係じゃ……、'
 show jessica_v001 smile_blush at active
 show shion_v008 smile at inactive
 jessica 'わわ私、そろそろお昼の時間か聞いてくるぜ！'
 play audio 'audio/sfx/SE_332_ls_fall.wav'
 show jessica_v001 smile_blush
 show jessica_v001 smile_blush:
  linear 0.16666666666666666 pos (2400,1200)
 pause 0.16666666666666666
 pause 2.0
 hide shion_v008
 hide jessica_v001
 with Dissolve(0.2)
 narrator '\u3000照れ隠しだと露骨にわかる仕草で、朱志香さんは踵を返して走り\n出す。'
 narrator '\u3000まだ１１時くらいだ。昼食を気にするにはさすがに少し早過ぎ\nる……。'
 narrator '\u3000その時、ヱリカさんが、ポンと手を打って、あ、と何かを思い出\nした仕草をした。'
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika 'あ、いけない。……私、昨日の魅音さんの窓の鍵の件、笑う資格が\nありませんでした。'
 hide erika_v001
 with Dissolve(0.2)
 show shion_v008 smile at mei_left
 show mion_v014 odoroki at mei_right
 with Dissolve(0.5)
 show mion_v014 odoroki at active
 show shion_v008 smile at inactive
 mion 'どしたの？\u3000ひょっとして、ヱリカさんも壊しちゃった？！'
 show shion_v008 fuan at active
 show mion_v014 odoroki at inactive
 shion 'お姉じゃあるまいし。何かあったんですか？'
 hide shion_v008
 hide mion_v014
 with Dissolve(0.2)
 show erika_v001 normal at mei_center
 with Dissolve(0.5)
 show erika_v001 normal at active
 erika 'マヌケな話です。私、自分の部屋に施錠をしてくるのを忘れたんで\nす。'
 hide erika_v001
 with Dissolve(0.2)
 show shion_v008 fuan at mei_left
 show mion_v014 smile at mei_right
 with Dissolve(0.5)
 show mion_v014 smile at updown_shake_transform,active
 show shion_v008 fuan at inactive
 mion 'それは酷いね！！\u3000窓はまぁ、なくもないけど、扉はまずいよ、う\nんうん、まずいね！'
 show shion_v008 fuan_close at active
 show mion_v014 smile at inactive
 shion '鍵をし忘れたのと、力加減を間違えて壊しちゃうのでは、だいぶ違\nうと思いますけれど？'
 hide shion_v008
 hide mion_v014
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_408_run.wav'
 narrator '\u3000お～～い、と朱志香さんが呼びながら戻ってくる。'
 show erika_v001 normal at mei_right
 show jessica_v001 smile at mei_left
 with Dissolve(0.5)
 show jessica_v001 smile at active
 show erika_v001 normal at inactive
 jessica 'お、お昼は１２時からだってさ！\u3000はぁ、はぁ！'
 show erika_v001 normal at active
 show jessica_v001 smile at inactive
 erika 'まぁ普通はそうだと思いますが、お伝え下さりありがとうございま\nす。'
 hide erika_v001
 hide jessica_v001
 with Dissolve(0.2)
 show shion_v008 smile at mei_left
 show mion_v014 smile at mei_right
 with Dissolve(0.5)
 show mion_v014 smile at active
 show shion_v008 smile at inactive
 mion '詩音～。次の撮影だけどさ。小道具、やっぱ換えない？'
 show shion_v008 smile at active
 show mion_v014 smile at inactive
 shion 'あー、ようやく気付きましたか。似合わないと思ってたんです。'
 camera at screenshake_transform
 pause 0.0
 show mion_v014 sinken at active
 show shion_v008 smile at inactive
 mion 'はぁ？！\u3000思ってたんなら何で言わなかったのさ！'
 hide shion_v008
 hide mion_v014
 with Dissolve(0.2)
 show erika_v001 normal_close at mei_center
 with Dissolve(0.5)
 show erika_v001 normal_close at active
 erika 'やれやれ。賑やかなことです。'
 hide erika_v001
 with Dissolve(0.2)
 show jessica_v001 smile at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show jessica_v001 smile at inactive
 nao '……あの、朱志香さん。少しいいですか？'
 show jessica_v001 smile at active
 show nao_v002 normal at inactive
 jessica 'ん？\u3000何？'
 window hide None
 show expression "#000" as fade with Dissolve(1.0)
 hide jessica_v001
 hide nao_v002
 with Dissolve(0.2)
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2221.png' as bg
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_530_walk_one.wav'
 narrator '\u3000あたしは朱志香さんを伴い、少しだけ東屋を離れる。'
 narrator '\u3000ただ、ヱリカさんは読書のふりをしながら、ずっと人の動向を監\n視してるような人だ。'
 narrator '\u3000あまり遠くまで行くと不審がられる。少しだけ離れて、話し声が\n聞こえない程度の距離を取る。'
 show jessica_v001 smile at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show jessica_v001 smile at inactive
 nao 'あの朱志香さん。……今日から、紗音さんはお休みなんですか？'
 show jessica_v001 smile at active
 show nao_v002 normal at inactive
 jessica 'え？\u3000あぁそうだぜ！\u3000次の出勤は確か、月曜だったかな？'
 show nao_v002 fuan at active
 show jessica_v001 smile at inactive
 nao '……あの、実は紗音さんに、どうしても急ぎでお伺いしたいことが\nありまして。'
 show jessica_v001 normal at active
 show nao_v002 fuan at inactive
 jessica '何？\u3000どうしたの？'
 show nao_v002 fuan at active
 show jessica_v001 normal at inactive
 nao 'それが、紗音さんだけに話したい話なんで……、せめて、電話で連\n絡を取るくらいは出来ませんか。'
 show jessica_v001 fuan at active
 show nao_v002 fuan at inactive
 jessica '………うーん。ウチさ、そういうのかなり厳しいんだぜ……。'
 hide jessica_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator '\u3000やはり、ヱリカさんの言っていた通りのようだ。'
 narrator '\u3000紗音さんは明日までお休み。\n\u3000そして、右代宮家では非番の使用人のプライバシーは最大限尊重\nし、一切の連絡を取らないらしい。'
 show nao_v002 fuan at mei_left
 show jessica_v001 fuan_close at mei_right
 with Dissolve(0.5)
 show jessica_v001 fuan_close at active
 show nao_v002 fuan at inactive
 jessica '仮に、どこかにいることを知っていても、話さない。そういうルー\nルなんだよ……。ゴメンな。'
 show nao_v002 fuan at active
 show jessica_v001 fuan_close at inactive
 nao 'あ、……いえ。こちらこそすみません……。'
 hide nao_v002
 hide jessica_v001
 with Dissolve(0.2)
 narrator '\u3000それでも連絡が取りたくなるような嘘が、ぱっと思い付けない。\n……連絡を取るのは無理なようだった。'
 stop music fadeout 0.5
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao '……仮に知っていても、話さない。…………あ。'
 play music 'audio/bgm/BGM_QUEST3_COLLAB2.wav'
 hide nao_v002
 with Dissolve(0.2)
 narrator '\u3000……見ても、見ていないというのが、使用人のお作法、……とい\nうことはないだろうか？'
 show jessica_v001 smile at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show jessica_v001 smile at inactive
 nao '朱志香さん。……とても当り前な話かもしれませんけど……。'
 show nao_v002 normal at active
 show jessica_v001 smile at inactive
 nao '例えばですよ？\u3000使用人の人がベッドメイクか何かで客室に入った\nとします。'
 show nao_v002 normal at active
 show jessica_v001 smile at inactive
 nao '……その時に、何かこう……プライベートなものを見てしまった場\n合、守秘義務というのはあるんでしょうか？'
 show jessica_v001 smile at nod_transform,active
 show nao_v002 normal at inactive
 jessica 'そりゃあるさ！\u3000源次さん曰く、使用人は家具なんだとさ。'
 hide jessica_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator '\u3000粛々と仕事を、黙して行なう。家具は喋らない。そして無意味に\n存在感を出すこともない。'
 narrator '\u3000だから、業務の合間にプライベートなものを見聞きしてしまって\nも、……決して口外しない。'
 show nao_v002 sinken at mei_center
 with Dissolve(0.5)
 show nao_v002 sinken at active
 nao 'た、例えばですよ？\u3000えっと、……そう、ハロウィン！\u3000宿泊客\nが、客室内でハロウィンの仮装撮影をしたとします。'
 show nao_v002 normal at active
 nao 'ハロウィンの仮装ってほら、ゾンビメイクとかあるじゃないです\nか？\u3000結構、血まみれな怖い感じの。'
 hide nao_v002
 with Dissolve(0.2)
 narrator '\u3000そういう血まみれのオバケ衣装が、無造作にベッドの上に放って\nあったとする。'
 narrator '\u3000しかし、それを知らずに入室した使用人は、事件か何かと勘違い\nして仰天して大騒ぎしたり、警察に連絡したりするようなこと\nは……。'
 show nao_v002 normal at mei_left
 show jessica_v001 normal at mei_right
 with Dissolve(0.5)
 show jessica_v001 normal at active
 show nao_v002 normal at inactive
 jessica '……本当の事件性のあるものなら、すぐに通報すると思うぜ？\u3000使\n用人としての義務以前に、市民としての義務だからな。'
 show jessica_v001 normal at active
 show nao_v002 normal at inactive
 jessica 'だから、判断に困るようなものだった場合、……使用人が触れて、\n見て判断することもあると思うぜ。'
 show nao_v002 normal at active
 show jessica_v001 normal at inactive
 nao '……ベッドの上が、血まみれの大惨事のような状態でも、納得でき\nたなら、スルーすると……。'
 show jessica_v001 smile at active
 show nao_v002 normal at inactive
 jessica '客のプライベートと判断するか、否かの問題だと思うぜ。'
 hide nao_v002
 hide jessica_v001
 with Dissolve(0.2)
 narrator '\u3000あたしはヱリカさんが犯人だと睨んでいる。\n\u3000でも、ヱリカさんには、紗音さんが入室した後には完璧なアリバ\nイがある。'
 narrator '\u3000魔法陣のシーツを仕込む時間は、紗音さんが入室する以前。……\nあたしたちが夕食に降りた直後しかありえない。'
 narrator '\u3000だが、その後に入室した紗音さんは、あの荒れ果てたベッドと不\n気味な魔法陣を見ても、事件性はないと判断した……。'
 narrator '\u3000毛布が乱れてるくらいならともかく、……あのおぞましい魔法陣\nを見て、その上で事件性はないと判断したのだ。'
 narrator '\u3000あれを見て、……プライベートだと思えるの？\u3000思える訳がな\nい……！'
 show nao_v002 normal at mei_left
 show jessica_v001 odoroki at mei_right
 with Dissolve(0.5)
 camera at screenshake_transform
 pause 0.0
 show jessica_v001 odoroki at active
 show nao_v002 normal at inactive
 jessica 'シーツの上に、血のようなもので描いた落書きがあったらぁ？！\u3000\nそりゃ、紗音は仰天するだろうぜ？！'
 show jessica_v001 fuan at active
 show nao_v002 normal at inactive
 jessica '紗音は落ち着いてる時はいいんだけど、取り乱すと冷静を失っちゃ\nうタイプなんだ……。'
 show jessica_v001 fuan_close at active
 show nao_v002 normal at inactive
 jessica 'もし、そんな不気味なものを見ちまったなら……。とても涼しそう\nに、異常なし、なんて言えないと思うぜ……。'
 show nao_v002 fuan at active
 show jessica_v001 fuan_close at inactive
 nao '……ですよ、ね。'
 hide nao_v002
 hide jessica_v001
 with Dissolve(0.2)
 narrator '\u3000あまりに園崎姉妹があっけらかんとした反応だったので、あたし\nもたまに自信が持てなくなるけれど……。'
 narrator '\u3000あの魔法陣の悪戯は、明らかに限度を超えている。悪戯で笑って\n済ませられる次元じゃなかった！'
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao 'なのに……、紗音さんは……、“いいえ、ご安心を”と、……涼し\nそうに言った……。'
 show nao_v002 normal_close at active
 nao 'そしてヱリカさんとも示し合わせていないというし……、\n……………。'
 hide nao_v002
 with Dissolve(0.2)
 camera at screenshake_transform
 pause 0.0
 narrator '\u3000待って待って待って。魅音さんが言ってた。テキストは徹底的に\n読み込め、って！\n\u3000ヱリカさんはこう言った！'
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 narrator '\u3000#ff0000私と紗音さんは、示し合わせてなどいません。#r'
 narrator '\u3000これ……、下らないトリックじゃないの？！\u3000間に仲介者を挟め\nばいい！'
 narrator '\u3000ヱリカさんが誰かと示し合わせる。その示し合わせた誰かが、紗\n音さんに、何らかの指示を与える。'
 narrator '\u3000例えば……、そう、コスプレ撮影！'
 narrator '\u3000撮影の為に、ちょっとショッキングな準備がしてあるから、見て\nも驚かないように、なんて風に予め言われていたとしたら……。'
 show nao_v002 sinken at mei_center
 with Dissolve(0.5)
 show nao_v002 sinken at active
 nao '……あの魔法陣のシーツも、……紗音さんにとっては、事件性のな\nい、プライベートなものとなる！'
 hide nao_v002
 with Dissolve(0.2)
 narrator '\u3000だが……、紗音さんに命令を出せそうな人物はかなり該当が多\nい。'
 narrator '\u3000右代宮家の人間は全員そうだろうし、使用人頭や目上の使用人も\n命令は可能だろう。'
 narrator '\u3000でも、……今はこれで十分。\n\u3000これで、紗音さんがあの魔法陣を見ても、何事もなかったかのよ\nうに振舞う可能性が見えてくる……！'
 show nao_v002 smile at mei_left
 show jessica_v001 fuan at mei_right
 with Dissolve(0.5)
 show jessica_v001 fuan at active
 show nao_v002 smile at inactive
 jessica '……何か、ウチの使用人がやらかしたりした……？'
 show nao_v002 smile at active
 show jessica_v001 fuan at inactive
 nao 'いえ、そんなことはありません。むしろ、多分、逆です。'
 hide nao_v002
 hide jessica_v001
 with Dissolve(0.2)
 narrator '\u3000紗音さんは、命令された通りに、使用人の仕事を全うしたに過ぎ\nないのだ。'
 show nao_v002 smile at mei_left
 show jessica_v001 smile at mei_right
 with Dissolve(0.5)
 show jessica_v001 smile at active
 show nao_v002 smile at inactive
 jessica 'じゃ、じゃあ、私はこれで失礼するぜ……！'
 show nao_v002 smile at nod_transform,active
 show jessica_v001 smile at inactive
 nao 'ありがとうございました。本当に何でもないので、気にしないで下\nさいね。'
 stop music fadeout 2.0
 hide nao_v002
 hide jessica_v001
 with Dissolve(0.2)
 narrator '\u3000朱志香さんが立ち去るのを見届け、振り返ると、\n東屋のヱリカさんと目が合う……。'
 play music 'audio/bgm/BGM_QUEST5_COLLAB2.wav'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 normal at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 normal at active
 erika '…………ふふん。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 narrator '\u3000あの顔は、何を朱志香さんと話していたのか、全てお見通しだと\n言いたいのだろう。'
 narrator '\u3000ヱリカさんは器用にも、魅音さんと談笑しながら、にもかかわら\nず、あたしをずっと監視していたのだ。'
 show expression "#000" as fade with Dissolve(1.0)
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2341.png' as bg
 with Dissolve(1.0)
 show mion_v014 smile at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show mion_v014 smile at inactive
 nao 'あれ、詩音さんは？'
 show mion_v014 smile at active
 show nao_v002 normal at inactive
 mion 'ちょっと別の小道具を探しに、ゲストハウスに戻ってるよ。すぐ戻\nるよ。'
 hide nao_v002
 show erika_v001 normal at mei_left
 with Dissolve(0.5)
 show erika_v001 normal at active
 show mion_v014 smile at inactive
 erika '……それにしても魅音さんは、……なかなかの切れ者じゃないです\nか。'
 show erika_v001 normal at active
 show mion_v014 smile at inactive
 erika 'こういっては失礼ですけど、怖い物知らずのただの田舎者かと思っ\nていたら、……なかなかです。'
 show mion_v014 smile at updown_shake_transform,active
 show erika_v001 normal at inactive
 mion 'あっはっは！\u3000ヱリカさんにそこまで言われると照れちゃうよぉ。'
 show mion_v014 smile_close at active
 show erika_v001 normal at inactive
 mion 'でも、ヱリカさんだってなかなかだよ～？\u3000でもひとつ勘違いがあ\nるかなぁ。'
 play audio 'audio/sfx/SE_226_shine.wav'
 show mion_v014 futeki at active
 show erika_v001 normal at inactive
 mion '真実は暴くものじゃない。作るものなのさ。さもなきゃ埋めるもの\nかな？\u3000園崎家の次期頭首を、舐めてもらっちゃあ困るねぇ？'
 hide mion_v014
 hide erika_v001
 with Dissolve(0.2)
 narrator '\u3000……朱志香さんと話している間に、二人でどんな会話をしていた\nか知らないが、……何だかバチバチしたものだったようだ。'
 narrator '\u3000でも、仮にそうだったにせよ、魅音さんにとっては、やるねぇの\n一言で済んでしまう程度なのだろう。'
 show mion_v014 futeki at mei_right
 show erika_v001 normal at mei_left
 with Dissolve(0.5)
 show erika_v001 normal at active
 show mion_v014 futeki at inactive
 erika '魅音さん。約束しましょう。いずれ必ず。#p雛見沢#sひなみざわ#rに探偵として訪れ\nることをお約束します。'
 show mion_v014 smile at nod_transform,active
 show erika_v001 normal at inactive
 mion 'うん！\u3000きっとだよ！\u3000部活メンバー全員で大歓迎しちゃうから\nね～！'
 hide mion_v014
 hide erika_v001
 with Dissolve(0.2)
 narrator '\u3000バチバチっと二人の交差する視線が火花を散らした気がしたが、\n気の置けない仲だからこそのじゃれ合いにも見えてしまう。'
 narrator '\u3000やっぱり魅音さんという人は、場数が違うというか、度胸が半端\nないというか。……大物だ。'
 show nao_v002 smile at mei_center
 with Dissolve(0.5)
 show nao_v002 smile at active
 nao 'あ、……詩音さん、帰ってきました。'
 hide nao_v002
 with Dissolve(0.2)
 show mion_v014 smile at mei_right
 show shion_v008 sinken at mei_left
 with Dissolve(0.5)
 camera at screenshake_transform
 pause 0.0
 show shion_v008 sinken at active
 show mion_v014 smile at inactive
 shion 'お姉ぇ！\u3000全然、違う場所に入れてありましたよ？\u3000勘弁して下さ\nいよねぇ！'
 show mion_v014 odoroki at active
 show shion_v008 sinken at inactive
 mion 'はぁ？！\u3000出発前に入れる場所を勝手に変えたのはあんたで\nしょー？！'
 hide mion_v014
 hide shion_v008
 with Dissolve(0.2)
 show erika_v001 normal_close at mei_right
 with Dissolve(0.5)
 show erika_v001 normal_close at active
 erika 'やれやれ。また賑やかになりました……。'
 show kanon_v001 normal at mei_left
 with Dissolve(0.5)
 show kanon_v001 normal at active
 show erika_v001 normal_close at inactive
 kanon '……ご歓談中、失礼致します。お昼の準備が整いました。'
 show erika_v001 normal at active
 show kanon_v001 normal at inactive
 erika 'だそうですよ、皆様方？\u3000参りましょうか。菜央ちゃま？'
 hide kanon_v001
 show nao_v002 sinken at mei_left
 with Dissolve(0.5)
 show nao_v002 sinken at active
 show erika_v001 normal at inactive
 nao '……ヱリカさん。あなたのアリバイ、崩せました。'
 show erika_v001 normal at active
 show nao_v002 sinken at inactive
 erika 'おや。それは、食後のデザートに取っておきませんか？'
 show nao_v002 normal at active
 show erika_v001 normal at inactive
 nao 'いいえ、オードブルで。今、説明するわ。'
 show erika_v001 fuan at active
 show nao_v002 normal at inactive
 erika 'それ、ちゃんとコースになるんですよねぇ？\u3000前菜で終わったら恥\nずかしいですよぉ？'
 show nao_v002 normal_close at active
 show erika_v001 fuan at inactive
 nao 'あなたは、紗音さんが異常を認めなかったから、犯行の余地はそれ\n以降だとしていました。'
 show nao_v002 normal at active
 show erika_v001 fuan at inactive
 nao 'その上、ご丁寧に、紗音さんとあなたは示し合わせていないとまで\n言い切ってくれました。でも'
 stop music fadeout 0.5
 show erika_v001 normal at active
 show nao_v002 normal at inactive
 erika '#ff0000私と紗音さんは、示し合わせてなどいません。#r'
 play sound ['audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav'] fadeout 1.0
 show expression "#e11" as fade with Dissolve(0.16666666666666666)
 play audio 'audio/sfx/SE_113_hit_flash.wav'
 hide fade with Dissolve(0.16666666666666666)
 with Dissolve(0.16666666666666666)
 show erika_v001 normal at active
 show nao_v002 normal at inactive
 erika '#ff0000私が何らかの人物を介し、もしくは手段を介して、紗音さんに根回#r\n#ff0000しをした事実はありません。#r'
 show nao_v002 fuan at active
 show erika_v001 normal at inactive
 nao '………え………。'
 show erika_v001 fuan at chara_shake_transform,active
 show nao_v002 fuan at inactive
 erika 'はぁぁぁ。残念無念、期待外れの的外れ。……ほらね？\u3000デザート\nにしておけばよかったんです。'
 show erika_v001 fuan at active
 show nao_v002 fuan at inactive
 erika '直接示し合わせていないなら、誰かを挟んで間接的に示し合わせれ\nばいい、これで赤き真実の間隙を縫った！って、……思ったんで\nしょお……？'
 show nao_v002 fuan_close at active
 show erika_v001 fuan at inactive
 nao '……ん、…………ぅ………。'
 play music 'audio/bgm/BGM_QUEST1_COLLAB2.wav'
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
 show erika_v001 fuan at inactive
 nao 'お、……思ってないわよ。そんな下らない言葉遊び、……あたしを\n子供扱いしないで欲しいわ。'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 show erika_v001 futeki at active
 show nao_v002 sinken at inactive
 erika 'くっくっくっく……。グッド。'
 show erika_v001 normal at active
 show nao_v002 sinken at inactive
 erika '探偵であれ、犯人であれ。……すぐに挫けるのは二流です。泣いて\nうずくまるのは戦人です。'
 show erika_v001 normal at active
 show nao_v002 sinken at inactive
 erika '一流は、タフでなければ。そして不敵でなければ。'
 hide erika_v001
 hide nao_v002
 with Dissolve(0.2)
 narrator '\u3000本当に嫌な人だけれど、不思議な人。\n\u3000ただの嫌な人というより、……何というか、……ライバルって感\nじ。'
 narrator '\u3000小馬鹿にしたり、挑発したり。腹立たしいけれど、敵であれ、見\n事ならば褒めるというところに、それを感じる。'
 show erika_v001 normal at mei_right
 show mion_v014 smile at mei_left
 with Dissolve(0.5)
 show mion_v014 smile at jumping_transform,active
 show erika_v001 normal at inactive
 mion 'ほらほら、お昼に行こうよ～！\u3000なぁにぃ？\u3000ウチの菜央ちゃん、\n口説いてんのぉ？'
 show erika_v001 normal at active
 show mion_v014 smile at inactive
 erika 'えぇ、そうです。こんな可愛らしくて小憎らしい子、殺人事件の被\n害者になる前に保護してあげないと。'
 show mion_v014 smile at active
 show erika_v001 normal at inactive
 mion 'お～っと、お触りは厳禁ですよ～？\u3000ウチの菜央ちゃんに御用の際\nは、マネージャーを通してもらわないとぉ♪'
 show erika_v001 normal at active
 show mion_v014 smile at inactive
 erika 'それで？\u3000貴女方の手番は十分ですか？'
 play audio 'audio/sfx/SE_211_electric.wav'
 show mion_v014 futeki at active
 show erika_v001 normal at inactive
 mion 'もちろん、ターンエンド。あんたに次の手、期待してるよ～？'
 hide erika_v001
 hide mion_v014
 with Dissolve(0.2)
 narrator '\u3000やっぱり、すっごいバチバチしてる。\n\u3000しかし、二人とも敵意を剥き出しのはずなのに、まるで映画の中\nの出来事のような、カッコよさも兼ね備えている。'
 narrator '\u3000……これが、一流はタフでなければ、ということなのね……。'
 show nao_v002 normal at mei_left
 show shion_v008 smile at mei_right
 with Dissolve(0.5)
 show shion_v008 smile at active
 show nao_v002 normal at inactive
 shion '菜央さん。昨夜は、あの悪戯、すっごいビックリしましたよねぇ？'
 show nao_v002 fuan at active
 show shion_v008 smile at inactive
 nao 'え？\u3000あ、はい……。'
 show shion_v008 normal_close at active
 show nao_v002 fuan at inactive
 shion 'あれが魔女の仕業だというのなら。'
 show shion_v008 futeki at active
 show nao_v002 fuan at inactive
 shion '……こっちは、オヤシロさまの#p祟#sたた#rりがあるかもしれませんねぇ？'
 hide nao_v002
 hide shion_v008
 with Dissolve(0.2)
 narrator '\u3000え、……何？\u3000どういう意味なの………？'
 narrator '\u3000詩音さんの笑みは、頼もしさが９割と、……１割の不敵さ、不気\n味さが含まれている気がした……。'