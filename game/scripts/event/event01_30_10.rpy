label event01_30_10:
 stop sound
 scene expression "#000"
 play music 'audio/bgm/BGM_QUEST6_COLLAB2.wav'
 show expression 'images/bg/AdvBg_2190.png' as bg
 with Dissolve(1.0)
 show beatrice_v001 normal at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao '……漫画かアニメに登場したものだと思います。'
 show beatrice_v001 fuan at active
 show nao_v002 normal at inactive
 beatrice '何？\u3000も、もう一度頼む……。'
 show nao_v002 normal at active
 show beatrice_v001 fuan at inactive
 nao '多分。この魔法陣は、漫画かアニメに登場したものだと思います。'
 camera at screenshake_transform
 pause 0.0
 show beatrice_v001 odoroki at active
 show nao_v002 normal at inactive
 beatrice '何と？！\u3000漫画……ッ？！？！'
 hide nao_v002
 show erika_v001 sinken_close at mei_left
 with Dissolve(0.5)
 show erika_v001 sinken_close at active
 show beatrice_v001 odoroki at inactive
 erika 'ベアトは見てないんですかー？\u3000……名探偵ワニャン。'
 show beatrice_v001 futeki at updown_shake_transform,active
 show erika_v001 sinken_close at inactive
 beatrice 'え？！\u3000わっはははは、妾はカネダ少年の事件簿派でなぁ。'
 show beatrice_v001 futeki at active
 show erika_v001 sinken_close at inactive
 beatrice 'ワニャンは子供っぽいから見ておらぬのだ。そういえば、紗音は面\n白いと言っていて勧めてきたことがあったなぁ。'
 show erika_v001 odoroki at active
 show beatrice_v001 futeki at inactive
 erika '……マジで本当に面白いから見て下さいぃって。'
 show erika_v001 odoroki_close at chara_shake_transform,active
 show beatrice_v001 futeki at inactive
 erika '我が主も、私がこんなにも勧めているのに、ちーーーーっとも見て\nくれないんですよ……。'
 hide beatrice_v001
 hide erika_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao '何も知らない人が見たら、とてもグロテスクな魔法陣に見えるで\nしょうね。'
 show nao_v002 normal at active
 nao 'でも、……知っている人には、むしろ微笑ましく思えるかもしれな\nい。'
 hide nao_v002
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 dlanor 'この魔法陣が……、名探偵ワニャンの中に登場するから、……デス\nカ。'
 show erika_v001 odoroki at mei_right
 with Dissolve(0.5)
 show erika_v001 odoroki at active
 show dlanor_v001 normal at inactive
 erika 'まだ見てない人は見て下さいよぉ。大人気で上映期間も延長中なん\nですよぉ……。'
 hide dlanor_v001
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show erika_v001 odoroki at inactive
 nao '……劇場版アニメ、名探偵ワニャン『中秋哀歌～兎たちの悲恋殺人\n事件～』……。'
 show erika_v001 sinken at active
 show nao_v002 normal at inactive
 erika 'この中に出てくる連続殺人犯が、現場に残す魔法陣なんです\nよぉぉ……。'
 show nao_v002 normal at active
 show erika_v001 sinken at inactive
 nao '……その連続殺人犯は、……人気あるの？'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide erika_v001
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 sinken at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show erika_v001 sinken at active
 erika 'ありますよぉおおおおぉおぉお！！\u3000巷じゃ、無頼人（ブライト）\nさまは、１００億の男なんて言われてるんですよぉおぉ！！'
 show erika_v001 smile at active
 erika 'すっごい儚くて美しくて、死でしか結ばれえない悲しき愛の貫き\n方……！！\u3000あぁあぁ、無頼人さまぁあぁぁ……！！'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show beatrice_v001 fuan at mei_center
 with Dissolve(0.5)
 show beatrice_v001 fuan at active
 beatrice 'つ、……つまり。映画に登場する、イケメン犯人が現場に残すサイ\nン、という訳なのか……。'
 hide beatrice_v001
 with Dissolve(0.2)
 show erika_v001 fuan at mei_center
 with Dissolve(0.5)
 show erika_v001 fuan at active
 erika '魔女から見て、魔法陣がおかしいのはご愛敬ですよぉお！！\u3000作者\nの代官山剛先生はミステリーの専門家で、魔法陣の専門家じゃない\nんですからぁ！'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.1
 pause 0.5
 show erika_v001 smile at active
 erika 'それでね？\u3000それでね？！\u3000詩音が持ってきた魔法陣、ちょいちょ\nい細かいとこが間違ってんですよぉおぉ！！'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.2
 pause 0.5
 camera at screenshake_transform
 pause 0.0
 show erika_v001 fuan at active
 erika '愛が足りない、愛がないから視えてないッ！\u3000とりあえず、１日３\n公演で１ヶ月は映画館に通わなきゃあ！！'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 play audio 'audio/sfx/SE_226_shine.wav'
 show erika_v001 futeki at active
 erika '私が描いた方は完璧です！\u3000代官山剛先生のチーフアシの人を３日\nも監禁して教えてもらったんです！！'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.0
 pause 0.5
 hide erika_v001
 with Dissolve(0.2)
 show dlanor_v001 fuan at mei_left
 show beatrice_v001 fuan at mei_right
 with Dissolve(0.5)
 show beatrice_v001 fuan at active
 show dlanor_v001 fuan at inactive
 beatrice 'さらーりと犯罪をＣＯしてるなぁー。'
 show dlanor_v001 fuan at active
 show beatrice_v001 fuan at inactive
 dlanor 'つまり。……名探偵ワニャンの映画を見ていた紗音や魅音詩音\nは、……一目見ただけで、この魔法陣の意味が、わかっていたとい\nうことデスネ……。'
 hide dlanor_v001
 hide beatrice_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao '魅音さんたちが、コスプレ撮影をしていることは、紗音さんもご存\n知だったはずです。'
 show nao_v002 normal at active
 nao 'そして、窓の鍵を直しに入室したら、……映画と同じ、イケメン犯\n人の魔法陣を描いたシーツが。'
 hide nao_v002
 with Dissolve(0.2)
 show nao_v002 normal at mei_left
 show beatrice_v001 fuan at mei_right
 with Dissolve(0.5)
 show beatrice_v001 fuan at active
 show nao_v002 normal at inactive
 beatrice '……はぁぁぁぁぁ……。それは……、怖がるどころか、むしろ同じ\n作品のファンとして、微笑ましくなってしまうなぁ……。'
 show nao_v002 normal_close at active
 show beatrice_v001 fuan at inactive
 nao 'ヱリカさんが、意味ありげな笑みを浮かべながら、部屋は荒らされ\nてなかったかと聞いてきたなら……。'
 hide beatrice_v001
 show dlanor_v001 fuan_close at mei_right
 with Dissolve(0.5)
 show dlanor_v001 fuan_close at active
 show nao_v002 normal_close at inactive
 dlanor '……紗音が涼し気に、いいえ、ご安心を、という気持ちも、少しは\nわかるというものデス。'
 show nao_v002 normal at active
 show dlanor_v001 fuan_close at inactive
 nao '映画は見ていませんが、恐らく、ベッドの荒れ方も、かなり映画に\n準拠していたでしょう。'
 show nao_v002 normal at active
 show dlanor_v001 fuan_close at inactive
 nao '思えば、ヱリカさんのベッドの毛布や枕の乱れ方は、……まるでお\n手本があるかのように、あたしのベッドの時と瓜二つでした。'
 hide dlanor_v001
 show beatrice_v001 futeki at mei_right
 with Dissolve(0.5)
 show beatrice_v001 futeki at active
 show nao_v002 normal at inactive
 beatrice '……これは、……名探偵ワニャンを読んでみるしかないなぁ……。'
 show nao_v002 smile at active
 show beatrice_v001 futeki at inactive
 nao 'あたしも、今回の事件で興味を持ったわ。……本屋で単行本を探し\nてみるわ。'
 show nao_v002 normal at active
 show beatrice_v001 futeki at inactive
 nao 'そんな訳で、第一の魔法陣事件は、ヱリカさんの手による、えぇ\nと……、'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide nao_v002
 hide beatrice_v001
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 sinken_close at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 sinken_close at chara_shake_transform,active
 erika 'はいはぁい、リザインですよぉおぉぉ……。私が悪かったです\nよぉぉ……。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show erika_v001 sinken_close at mei_right
 show dlanor_v001 normal at mei_left
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 show erika_v001 sinken_close at inactive
 dlanor 'リザインで、よろしいデスカ。'
 show erika_v001 sinken_close at active
 show dlanor_v001 normal at inactive
 erika '参りましたぁ、負けましたぁ。大人しくお家に帰って、ワニャンの\n単行本、また１巻から全読破しまぁす……。'
 hide erika_v001
 hide dlanor_v001
 with Dissolve(0.2)
 show beatrice_v001 smile at mei_center
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_311_ls_cutejump.wav'
 show beatrice_v001 smile at jumping_transform,active
 beatrice '妾にも単行本を貸してくれぬか。そなたをそこまで虜にするとは、\n実に興味深いぞ！'
 hide beatrice_v001
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_center
 with Dissolve(0.5)
 show dlanor_v001 normal at active
 dlanor 'それでは、ヱリカのリザインにより、勝者はベアトリーチェと菜央\nデス。おめでとうございマス。'
 hide dlanor_v001
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_5040_handclap.wav'
 pause 2.6666666666666665
 play audio 'audio/sfx/SE_5040_handclap.wav'
 narrator '\u3000ドラノールさんが拍手を始めると、あたしとベアトリーチェも\nそれに倣う。'
 narrator '\u3000くらげみたいな軟体動物と化してグネグネしているヱリカさん\nも、投げ遣りではあるが共に拍手をしてくれた……。'
 show beatrice_v001 futeki at mei_center
 with Dissolve(0.5)
 show beatrice_v001 futeki at active
 beatrice 'うむ！！\u3000妾は大満足であるぞッ。実に楽しい誕生日であった！'
 show beatrice_v001 futeki at jump_transform,active
 beatrice '菜央よ、ヱリカよ！！\u3000そなたたちは、見事、妾の退屈の病を癒し\nてくれた。'
 show beatrice_v001 smile at active
 beatrice 'ヱリカには褒美として、そなたが素晴らしい贈り物を届けてくれ\nた、素晴らしい使者であったと記したベルンカステル卿宛ての親書\nを授けよう。'
 show beatrice_v001 smile at active
 beatrice 'さらに追伸にて、名探偵ワニャンは面白いらしいぞと、妾からもお\n勧めしておく！'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide beatrice_v001
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 smile at mei_center
 with Dissolve(0.08333333333333333)
 show erika_v001 smile at chara_shake_transform,active
 erika 'ベ、ベアトリーチェ卿……！！\u3000有り難きお言葉！\u3000\nははぁぁぁ！！'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show nao_v002 normal at mei_left
 show dlanor_v001 normal_close at mei_right
 with Dissolve(0.5)
 show dlanor_v001 normal_close at active
 show nao_v002 normal at inactive
 dlanor '菜央。ヱリカを誤解しないで下サイ。……ヱリカは優れた探偵も、\n憐れな犯人も同時に演じられる、素晴らしい俳優なのデス。'
 show nao_v002 smile at active
 show dlanor_v001 normal_close at inactive
 nao '……わかってるわ。彼女は普段、悪役を演じているだけで、本当は\nそうじゃないってこと。'
 show dlanor_v001 smile at active
 show nao_v002 smile at inactive
 dlanor '…………菜央。やはり貴女は、航海者の魔女に並ぶ、特別な人のよ\nうデス。'
 hide dlanor_v001
 show beatrice_v001 smile at mei_right
 with Dissolve(0.5)
 show beatrice_v001 smile at active
 show nao_v002 smile at inactive
 beatrice 'そして菜央よ！\u3000そなたも我が六軒島へ来て、よく最後まで妾と\nゲームに付き合ってくれた！'
 show nao_v002 fuan at active
 show beatrice_v001 smile at inactive
 nao '……薔薇を眺めながら、のんびり刺繍をするつもりだったのにね。\nサイアクのバカンスになったわ。'
 show nao_v002 smile at active
 show beatrice_v001 smile at inactive
 nao 'でも。………あたしも、ちょっと楽しかったかも、かも……。'
 show beatrice_v001 normal_close at active
 show nao_v002 smile at inactive
 beatrice 'もうじき、夜が明ける。それでお別れだ。'
 show beatrice_v001 smile at active
 show nao_v002 smile at inactive
 beatrice '妾からの、心ばかりのプレゼントを贈っておく。楽しみにして目覚\nめるがよい。'
 show nao_v002 smile at active
 show beatrice_v001 smile at inactive
 nao 'ありがとう。……あなたとまたゲームが出来るなら、……また六軒\n島に来るのも、悪くないわ。'
 show beatrice_v001 futeki at active
 show nao_v002 smile at inactive
 beatrice '待っておるぞ！\u3000いつでも来るがよい！'
 hide nao_v002
 hide beatrice_v001
 with Dissolve(0.2)
 show dlanor_v001 normal at mei_left
 show erika_v001 normal at mei_right
 with Dissolve(0.5)
 show erika_v001 normal at active
 show dlanor_v001 normal at inactive
 erika '島の近くで船から落っこちれば、勝手に島に流れ着きますから。'
 show dlanor_v001 normal_close at active
 show erika_v001 normal at inactive
 dlanor '……菜央。貴女のカケラを覗いた時。……貴女がこれから巡るだろ\nう数奇な運命を垣間見マシタ。'
 show dlanor_v001 normal at active
 show erika_v001 normal at inactive
 dlanor '強く、生きて下サイ。貴女なら、どのようなカケラもつかみ取れる\nはずデス。'
 hide dlanor_v001
 hide erika_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao 'あたしは、ただのお姉ちゃん大好きっ子だし。……運命なんて、な\nるようになるわ。あたしは、恐れも期待もしない。'
 hide nao_v002
 with Dissolve(0.2)
 show expression "#000" as fade with Dissolve(1.0)
 hide fade with Dissolve(1.0)
 with Dissolve(1.0)
 narrator '\u3000……あ。\n\u3000ゆっくりと……、視界が暗くなっていくのを感じる。'
 narrator '\u3000朝を迎え、あたしは起床するのだろう。'
 narrator '\u3000……楽しかったわ、六軒島。\n\u3000次に来る時は、……今度こそのんびり、刺繍をさせてね……。'
 stop music fadeout 2.0
 window hide None
 show expression "#000" as fade with Dissolve(3.0)
 play music 'audio/bgm/BGM_GACHA_COLLAB2.wav'
 show expression "#fff" as fade with Dissolve(2.0)
 stop sound
 scene expression "#fff"
 show expression 'images/bg/AdvBg_2221.png' as bg
 with Dissolve(1.0)
 pause 2.0
 stop sound
 
 pause 2.0
 stop sound
 
 play audio 'audio/sfx/SE_543_bird.wav'
 narrator '\u3000……雀の囀りが聞こえて来た。\n\u3000ゆっくりと目を開けば、……朝日で満たされた温かな部屋の天井\nが見えてくる……。'
 narrator '\u3000今日で、六軒島ともお別れか……。'
 narrator '\u3000そういえばベアトリーチェは、何かプレゼントがあると言ってな\nかったっけ。'
 narrator '\u3000楽しみにして目覚めるがよい、とか言っていたような………。'
 stop music fadeout 0.5
 
 narrator '\u3000こんな島、来なければよかった……。'
 play music 'audio/bgm/BGM_QUEST7_COLLAB2.wav'
 nao 'ひ、……ひ、'
 nao '嫌ああぁああぁあぁぁああぁぁぁあッ！！'
 show expression "#000" as fade with Dissolve(1.0)
 stop sound
 scene expression "#000"
 play audio 'audio/sfx/SE_346_ls_blood.wav'
 show expression 'images/bg/AdvBg_1270.png' as bg
 with Dissolve(1.0)
 play sound ['audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav','audio/sfx/SE_5053_wind.wav'] fadeout 1.0
 narrator '\u3000哀れな犠牲者たちは、……ベッドの上で、血まみれだった。'
 narrator '\u3000魅音さんのネグリジェは、本当はとても可愛らしいものだったの\nだろう。'
 narrator '\u3000しかし、刃物か何かで執拗に切りつけられて、ズタズタにされて\nしまっている。'
 narrator '\u3000そこから溢れ出しただろう鮮血が、ネグリジェもシーツも、元が\n何色だったか思い出せないほどに染めてしまっている。'
 narrator '\u3000詩音さんはガウン姿だった。……もちろん、真っ赤な鮮血に染め\nられている。'
 narrator '\u3000こちらも同様に、ズタズタに切り裂かれ……、見るも無残な有様\nだ……。'
 narrator '\u3000３つのベッドの内、２つは鮮血に染まるが、１つは、昨晩から変\nわらず清潔なままだ。\n\u3000それが、……あたしのベッド。'
 narrator '\u3000そしてあたしだけが、……血の一滴も浴びずに、彼女たちと同じ\n部屋で、……熟睡していた……。'
 narrator '\u3000だ、大丈夫ですか……。そう言おうと思った。\n\u3000しかし、あたしの口から出たのは、か細くて弱々しい、悲鳴と呼\nぶにも頼りない、かすれ声だけであった。'
 show expression "#000" as fade with Dissolve(1.0)
 scene expression "#000"
 play audio 'audio/sfx/SE_527_door_close.wav'
 narrator '\u3000あたしは部屋を飛び出し、隣室の扉を激しくノックしながら、同\n時にドアノブも捻る。'
 nao 'ヱリカさんッ、ヱリカさんッ！！\u3000た、大変です大変です、たた、\n助けて……ッ！！'
 stop sound
 scene expression "#000"
 play audio 'audio/sfx/SE_526_door_open.wav'
 show expression 'images/bg/AdvBg_2281.png' as bg
 with Dissolve(1.0)
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 nao 'え……？\u3000開いた………？'
 hide nao_v002
 with Dissolve(0.2)
 narrator '\u3000ドアノブを捻ったって、鍵が掛けられているのだから、開く訳は\nない。'
 narrator '\u3000ドアノブをガチャガチャさせるのが、自分の混乱と状況の異常を\n知らせる、無意識の方法だったからに過ぎない。'
 narrator '\u3000……だから、扉が開いてしまうことは、まったく想定しなかった\nのだ。'
 narrator '\u3000その異常が……、あたしの心を瞬時に凍らせ、……ナイフのよう\nに鋭く尖らせる。'
 narrator '\u3000極限の恐怖は、感情の全てを殺し、五感を限界まで研ぎ澄ます。\n\u3000だが、所詮は氷のナイフ。\n\u3000……どんなに鋭くても、脆く、砕け散る……。'
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 nao 'ヱリカ……さん………？'
 show expression "#000" as fade with Dissolve(1.0)
 hide nao_v002
 with Dissolve(0.2)
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_1270.png' as bg
 with Dissolve(1.0)
 play audio 'audio/sfx/SE_017_TragedyStart.wav'
 narrator '\u3000染められていた……。\n\u3000ヱリカさんもまた、ベッドの上で……、真っ赤に、血まみれ\nに………。'
 camera at screenshake_transform
 pause 0.0
 nao '嫌あああぁあぁぁあぁあぁあぁぁぁぁぁッ！！！'
 window hide None
 show expression "#000" as fade with Dissolve(2.0)
 scene expression "#000"
 pause 4.0
 stop music
 nao '…………ヱリカさん。おはようございます。'
 narrator '\u3000当然、死体が喋ることはない。'
 play music 'audio/bgm/BGM_QUEST6_COLLAB2.wav'
 narrator '\u3000なら、死体が呼吸をする必要もないわね。'
 play audio 'audio/sfx/SE_5005_grab.wav'
 erika 'ふがッ……………。'
 erika '…………………………………。'
 erika '……………………………………………………ッ。'
 stop sound
 scene expression "#000"
 show expression 'images/bg/AdvBg_2281.png' as bg
 with Dissolve(1.0)
 show nao_v002 normal at mei_left
 show erika_v001 odoroki at mei_right
 with Dissolve(0.5)
 camera at screenshake_transform
 pause 0.0
 show erika_v001 odoroki at active
 show nao_v002 normal at inactive
 erika 'ゲハッ！！\u3000こッ、殺す気ですか、ハアハア、ゼエゼエ！！！'
 show nao_v002 normal at active
 show erika_v001 odoroki at inactive
 nao 'おはようございます、ヱリカさん。'
 show nao_v002 normal at active
 show erika_v001 odoroki at inactive
 nao 'これもきっと、ワニャンの映画の中のワンシーンの再現なんですよ\nね？'
 show erika_v001 futeki at active
 show nao_v002 normal at inactive
 erika 'ふっふっふ！\u3000完璧だったでしょう？！\u3000特に、死に顔にほのかに\n残る未練と慕情の再現は、究極的だったと思いますッ！'
 show erika_v001 smile at active
 show nao_v002 normal at inactive
 erika 'ただ、名探偵ワニャンへの愛があるだけで、古戸ヱリカにはこの程\n度のコスプレが可能です！\u3000如何ですか、魅音さん詩音さんッ？！'
 show nao_v002 fuan_close at active
 show erika_v001 smile at inactive
 nao '……向こうも死体だわ。あなたとどちらが完璧か、採点をお願いす\nるわ……。'
 hide nao_v002
 hide erika_v001
 with Dissolve(0.2)
 play audio 'audio/sfx/SE_408_run.wav'
 narrator '\u3000ヱリカさんは、ズタズタの血塗れゾンビの姿で、不敵に笑いなが\nら、あたしたちの部屋に飛び込んでいく。'
 pause 4.0
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 smile at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show erika_v001 smile at active
 erika 'おおッ！！！\u3000……なかなかの再現度です！\u3000これは確か劇場版\nの……３２分１８秒の……。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show nao_v002 sinken at mei_center
 with Dissolve(0.5)
 show nao_v002 sinken at active
 nao 'これ……映画館で隠し撮りしたの……？\u3000それ犯罪よ。映画泥棒\nよ。頭からポップコーンぶちまけるわよ。'
 hide nao_v002
 with Dissolve(0.2)
 narrator '\u3000ヱリカさんがどこからともなく取り出した、秘密探偵道具の小さ\nな画面には、……この部屋の惨状とそっくりなシーンが映し出され\nていた……。'
 show erika_v001 smile at mei_center
 with Dissolve(0.5)
 show erika_v001 smile at active
 erika 'まず、詩音さんから！\u3000強打者（スラッガ）くんの再現、お見事で\nす！'
 play audio 'audio/sfx/SE_215_heartgrow.wav'
 show erika_v001 smile at jumping_transform,active
 erika 'いいですね、衣装が完璧なのは当然として、この感じ！\u3000心から\nキャラになり切らないとなかなか出来ません！'
 show erika_v001 smile at chara_shake_transform,active
 erika '一番大事なのはこの儚い死に顔！！\u3000実にいい表情ですッ！\u3000これ\nは満点を出しましょう！'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 show shion_v002 smile_blush at mei_center
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_311_ls_cutejump.wav'
 show shion_v002 smile_blush at jump_transform,active
 shion 'ヒョオウ！\u3000さっすがワニャラー！！\u3000細かいところまでよく見て\n下さりましたね！'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide shion_v002
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 nao 'すごいわ。……惨殺死体が上機嫌に跳ね起きたわ……。'
 hide nao_v002
 with Dissolve(0.2)
 show erika_v001 smile at mei_center
 with Dissolve(0.5)
 show erika_v001 smile at active
 erika '続きまして魅音さんですね。こちらは町留田（マチルダ）さんの再\n現、これもまたお見事です！！'
 show erika_v001 smile at active
 erika 'もはや、言うまでもなく完璧なのですが、……ダブルパーフェクト\nが出るかどうかは、ここに掛かってます！！'
 hide erika_v001
 with Dissolve(0.2)
 show nao_v002 fuan at mei_left
 show shion_v002 smile at mei_right
 with Dissolve(0.5)
 show shion_v002 smile at active
 show nao_v002 fuan at inactive
 shion '菜央さん、わかりますぅ？\u3000この細かいこだわり。'
 show nao_v002 fuan_close at active
 show shion_v002 smile at inactive
 nao '……だから全然わかりません。'
 hide nao_v002
 hide shion_v002
 with Dissolve(0.2)
 show erika_v001 smile at mei_center
 with Dissolve(0.5)
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.1
 pause 0.5
 show erika_v001 smile at active
 erika 'このネグリジェの裾！\u3000ほら、少しだけ膨らんでいるでしょう？\u3000\nここ！\u3000指輪ケースが隠れてるんです！'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.2
 pause 0.5
 show erika_v001 fuan at active
 erika 'どうせ見えない部分だからと、適当に誤魔化しちゃうレイヤーさん\nも多いんですが、……さてさて魅音さんは……ッ？！'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.3
 pause 0.5
 play audio 'audio/sfx/SE_5037_getup.wav'
 pause 4.0
 camera at screenshake_transform
 pause 0.0
 show erika_v001 smile at active
 erika 'ありましたぁ！！\u3000しかもすごい原作再現度！！\u3000投げ返された時\nについた傷跡まで完璧！！'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show nao_v002 fuan at mei_left
 with Dissolve(0.5)
 show nao_v002 fuan at active
 nao '……もう全然意味がわかりません。'
 show mion_v002 futeki at mei_right
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_226_shine.wav'
 show mion_v002 futeki at active
 show nao_v002 fuan at inactive
 mion 'くっくっく！\u3000細部にこそ神は宿る、見えないところにまでこだ\nわってこそ真のワニャラー！'
 show nao_v002 fuan_close at active
 show mion_v002 futeki at inactive
 nao '……ホントごめんなさい。帰ったら必ず映画館いきます。'
 hide nao_v002
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at jump_transform,active
 show mion_v002 futeki at inactive
 shion 'ヱリカさんの衣装を見る限り、どうやら、未来（ミライ）さんの死\n亡現場を再現してたみたいですね！'
 play audio 'audio/sfx/SE_215_heartgrow.wav'
 show mion_v002 smile at jumping_transform,active
 show shion_v002 smile at inactive
 mion 'ちょっとヱリカさんの部屋に戻ろうよ！\u3000ヱリカさん、見るからも\nう１回死んで死んで！！'
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show nao_v002 fuan_close at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan_close at active
 nao '……ホント皆さん、１回死んで下さい……。'
 hide nao_v002
 with Dissolve(0.2)
 narrator '\u3000このワニャラーどもは、すっごく和気藹々と楽しんでいる。'
 narrator '\u3000昨日、何だかギスギスした言葉を交わし合っていた気がするけ\nど、あれもきっと、ワニャンに出てくる劇中の掛け合いの真似なの\nだろう。'
 narrator '\u3000魅音さんと詩音さん、そしてヱリカさんは、共通の趣味を持つ者\nとして、かなり早い段階から意気投合していたのだ……。'
 narrator '\u3000それで、劇中の洋館ミステリーっぽい、ギスギスとした会話を交\nわし合い、わかる人にしかわからない会話を楽しんでいた………？'
 show erika_v001 smile at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show erika_v001 smile at inactive
 nao 'ストップ。……すると、とても当然な疑問に行きつくわ。'
 show erika_v001 normal at active
 show nao_v002 normal at inactive
 erika '疑問？\u3000何でしょうか？'
 hide erika_v001
 hide nao_v002
 with Dissolve(0.2)
 show mion_v002 smile at mei_right
 show shion_v002 smile at mei_left
 with Dissolve(0.5)
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion 'あー、映画を楽しむには、やはり漫画を読了してないとダメか、っ\nてことでしょうか。'
 show mion_v002 smile at active
 show shion_v002 smile at inactive
 mion 'さすがに全巻読了は厳しいからね！\u3000６８巻以降でいいんじゃない\nかな。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide mion_v002
 hide shion_v002
 hide fade with Dissolve(0.08333333333333333)
 show erika_v001 sinken at mei_center
 with Dissolve(0.08333333333333333)
 play audio 'audio/sfx/SE_341_ls_WhistleShort.wav'
 pause 0.3333333333333333
 play audio 'audio/sfx/SE_341_ls_WhistleLong.wav'
 camera at screenshake_transform
 pause 0.0
 show erika_v001 sinken at active
 erika 'ぴぴぴー！\u3000ダメですダメです！\u3000ワニャンを取り巻く人間関係の\n深みを知らなければ、面白さは激減です！'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide erika_v001
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show shion_v002 smile at mei_center
 with Dissolve(0.5)
 show shion_v002 smile at updown_shake_transform,active
 shion 'ですよねー！\u3000やっぱり菜央さんには全巻を読んでいただかない\nと！'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide shion_v002
 hide fade with Dissolve(0.08333333333333333)
 show nao_v002 sinken at mei_center
 with Dissolve(0.08333333333333333)
 show nao_v002 sinken at active
 nao 'いい加減にして下さい。切り刻みますよ。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 narrator '\u3000ワニャラーどもは、ヒッと短い悲鳴をあげて、正座した……。'
 window hide None
 show expression "#000" as fade with Dissolve(1.0)
 pause 2.0
 play music 'audio/bgm/BGM_QUEST5_COLLAB2.wav'
 hide fade with Dissolve(1.0)
 with Dissolve(1.0)
 show mion_v002 fuan at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show mion_v002 fuan at inactive
 nao '今から、皆さんに質問します。'
 show nao_v002 normal at active
 show mion_v002 fuan at inactive
 nao '返答如何では、ホントに殺人事件になりますので、心してお返事下\nさい。'
 show mion_v002 fuan at chara_shake_transform,active
 show nao_v002 normal at inactive
 mion 'な、何よぉ～……、凄んじゃって、菜央ちゃんの可愛い顔が台無し\nだよぉ。ねぇ？'
 camera:
  anchor (0.5,0.5)
  pos (960,540)
  parallel:
   linear 0.5 pos (960, 540)
  parallel:
   linear 0.5 zoom 1.2
 pause 0.5
 show nao_v002 sinken at active
 show mion_v002 fuan at inactive
 nao '教えてくれても、よかったじゃないですか。'
 hide mion_v002
 show shion_v002 fuan at mei_right
 with Dissolve(0.5)
 show shion_v002 fuan at active
 show nao_v002 sinken at inactive
 shion '教えてって、何を……。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 590)
  zoom 1.3
 hide nao_v002
 hide shion_v002
 hide fade with Dissolve(0.08333333333333333)
 show nao_v002 sinken at mei_center
 with Dissolve(0.08333333333333333)
 camera at screenshake_transform
 pause 0.0
 show nao_v002 sinken at active
 nao 'あたしのベッドに魔法陣が現れた時！\u3000教えてくれればよかった\nじゃないですかッ！'
 camera at screenshake_transform
 pause 0.0
 show nao_v002 sinken at active
 nao 'これは名探偵ワニャンの映画に出てくるワンシーンで云々！\u3000教え\nてくれれば、あたしは怯えずに済んだんですッ。'
 show expression "#000" as fade with Dissolve(0.3333333333333333)
 camera:
  anchor (0.5,0.5)
  pos (960, 540)
  zoom 1.0
 hide nao_v002
 hide fade with Dissolve(0.08333333333333333)
 with Dissolve(0.08333333333333333)
 show mion_v002 fuan at mei_right
 show shion_v002 normal at mei_left
 with Dissolve(0.5)
 show shion_v002 normal at active
 show mion_v002 fuan at inactive
 shion 'それはぁ……、ねぇ………？'
 show mion_v002 fuan_close at active
 show shion_v002 normal at inactive
 mion '菜央ちゃんの驚きようが……、あんまりに可愛かったもので……つ\nいつい……。'
 hide mion_v002
 hide shion_v002
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao 'ハイ、……“あんまりに可愛かったもので、ついつい”。１７文字\nですね。'
 show nao_v002 normal_close at active
 nao '魅音さんと詩音さんは１７分割に切り刻みます。'
 hide nao_v002
 with Dissolve(0.2)
 show erika_v001 normal_close at mei_right
 show nao_v002 normal at mei_left
 with Dissolve(0.5)
 show nao_v002 normal at active
 show erika_v001 normal_close at inactive
 nao '続きまして、ヱリカさん。……あなたは本当は、見ていたんですよ\nね？'
 show erika_v001 smile at active
 show nao_v002 normal at inactive
 erika 'え？\u3000何を？\u3000ワニャンの放送はもちろん全部……、'
 camera at screenshake_transform
 pause 0.0
 show nao_v002 sinken at active
 show erika_v001 smile at inactive
 nao 'あなたの部屋の魔法陣です！\u3000詩音さんの悪戯はお昼前にはもう行\nわれていたわ！'
 show nao_v002 normal at active
 show erika_v001 smile at inactive
 nao 'あなたは施錠前に室内を確認したけれど、異常はなかったと言いま\nした。……嘘ですよね？'
 show erika_v001 normal at active
 show nao_v002 normal at inactive
 erika '……紗音さんが魔法陣を気にしなかった件で混乱しているようだっ\nたので、ちょっとからかっちゃおうと思いまして……♪'
 show nao_v002 normal_close at active
 show erika_v001 normal at inactive
 nao '“紗音さんが魔法陣………っちゃおうと思いまして”……。４９文\n字ですね。サービスで切り上げて５０文字です。'
 show nao_v002 normal at active
 show erika_v001 normal at inactive
 nao 'さすがに５０分割は面倒臭いので、ヱリカさんはフードプロセッ\nサーに放り込んだ方が楽そうです。'
 hide erika_v001
 hide nao_v002
 with Dissolve(0.2)
 camera at screenshake_transform
 pause 0.0
 narrator '\u3000ひーーッ、猟奇的ぃ！！\u3000３人は悲鳴を上げる。'
 narrator '\u3000あたしから見れば、あんな惨殺体の格好をして互いに写真を撮り\n合うアンタらの方が、ずっと猟奇的だ。'
 show nao_v002 normal_close at mei_center
 with Dissolve(0.5)
 show nao_v002 normal_close at active
 nao 'まぁ、３人とも素直に謝りましたので、切り刻むのは今回は保留し\nます。'
 hide nao_v002
 with Dissolve(0.2)
 show shion_v002 smile at mei_left
 show mion_v002 smile at mei_right
 with Dissolve(0.5)
 show mion_v002 smile at chara_shake_transform,active
 show shion_v002 smile at inactive
 mion 'はーーッ。よかったぁ！\u3000菜央ちゃんも、ワニャンを見てたらいい\nよ！'
 show shion_v002 smile at active
 show mion_v002 smile at inactive
 shion 'ぜーったい、映画見たら、ワニャン沼にズブズブ入りますからぁ。'
 hide mion_v002
 show erika_v001 smile at mei_right
 with Dissolve(0.5)
 play audio 'audio/sfx/SE_215_heartgrow.wav'
 show erika_v001 smile at jumping_transform,active
 show shion_v002 smile at inactive
 erika 'ワニャン沼、いいですねぇ。今度、コラボカフェがあるそうです\nよぉ！\u3000一緒に行きましょおー！！'
 hide shion_v002
 hide erika_v001
 with Dissolve(0.2)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao '……今、最後の謎が浮かんだわ。'
 show nao_v002 normal at active
 nao 'あなたたちがそれぞれ、熱狂的な名探偵ワニャンのファンであるこ\nとは理解しました。'
 show nao_v002 normal_close at active
 nao 'しかしそれにしたって……、あなたたちの意気投合っぷりは、\nちょっと考え難いほどです。'
 show nao_v002 fuan at active
 nao 'あなたたちは、いつの間にそんなに仲良くなっていたんですか？'
 hide nao_v002
 with Dissolve(0.2)
 narrator '\u3000あぁ……、いよいよ明かされる。\n\u3000あたしにとっての六軒島は、魔女と魔法陣と謎解きのミステリア\nスな２泊３日だった。'
 narrator '\u3000しかし。'
 narrator '\u3000あたしが魔法陣に怯え、不可解な謎に頭を悩ませている間\nに……、彼女たちは、#pと#s・#r#pて#s・#r#pつ#s・#r#pも#s・#r#pな#s・#r#pい#s・#r暗闘を繰り広げていたの\nだ………。'