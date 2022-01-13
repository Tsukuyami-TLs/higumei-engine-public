label chara452001_01:
 show black_background onlayer black
 $ event_store.current_event='chara452001'
 $ event_store.current_progress=0
 $ event_store.current_chapter='chara452001_01'
 $ persistent.menu_return='chara'
 camera:
  anchor (0.5, 0.5)
  pos (960, 540)
 scene
 stop music
 stop sound
 show expression 'images/bg/AdvBg_2190.png' as bg
 play music "<loop 0>audio/bgm/BGM_EVENT_TOP_COLLAB2.ogg"
 hide fade onlayer curtain
 with Dissolve(1.0)
 show nao_v002 fuan at mei_right
 show beatrice_v001 smile at mei_left
 with Dissolve(0.5)
 show beatrice_v001 smile at active
 show nao_v002 fuan at inactive
 beatrice "Don't be shy. Now, drink it before it gets cold."
 show nao_v002 fuan at active
 show beatrice_v001 smile at inactive
 nao 'Um... uhh... what is this?'
 show beatrice_v001 normal at active
 show nao_v002 fuan at inactive
 beatrice "Mm... what's the matter; do you dislike black tea? If so, why not try the cookies? Ronove said he was proud of how they came out."
 show nao_v002 fuan at active
 show beatrice_v001 normal at inactive
 nao "No, that's not what I meant. I love black tea... But..."
 show nao_v002 normal_close at active
 show beatrice_v001 normal at inactive
 nao '(...refusing would be rude, so I guess I should just try it...)'
 play audio 'audio/sfx/SE_5049_cup.wav'
 show nao_v002 smile at active
 show beatrice_v001 normal at inactive
 nao "Down the hatch, then... Woooow... it's delicious...! "
 play audio 'audio/sfx/SE_215_heartgrow.wav'
 show nao_v002 smile_blush at jumping_transform,active
 show beatrice_v001 normal at inactive
 nao "The smell is sophisticated and wonderful, there isn't any tartness, and it's just a little sweet...♪"
 show beatrice_v001 smile at active
 show nao_v002 smile_blush at inactive
 beatrice "It's true, it's true. By the way, as of late, this tea has been a personal favorite of mine!"
 show beatrice_v001 smile_close at active
 show nao_v002 smile_blush at inactive
 beatrice "You could say I'm obsessed with it."
 show nao_v002 fuan at active
 show beatrice_v001 smile_close at inactive
 nao "Ah... but since black tea is supposed to have more caffeine than coffee, if I drink too much of it, won't I have trouble sleeping?"
 show beatrice_v001 smile at active
 show nao_v002 fuan at inactive
 beatrice '*cackle* Humans truly are delicate creatures.'
 show nao_v002 smile at active
 show beatrice_v001 smile at inactive
 nao "(*giggle*. During that logic battle, she was incredibly dignified and frightening, but she seems to be friendlier than you'd think, maybe... maybe.)"
 show beatrice_v001 smile at active
 show nao_v002 smile at inactive
 beatrice 'In addition, the aroma of the tea is improved if you eat tea cakes in between sips. I would recommend those scones and such over there, as they would compliment it well. '
 show nao_v002 smile at active
 show beatrice_v001 smile at inactive
 nao "Ah... that's right. If that's the case, you could perhaps try putting jam or something on it."
 show beatrice_v001 smile at nod_transform,active
 show nao_v002 smile at inactive
 beatrice 'Of course, it pairs well with Russian tea. Perhaps you can try that next.'
 hide nao_v002
 hide beatrice_v001
 with Dissolve(0.2)
 narrator '............'
 show black_cover onlayer curtain as fade with Dissolve(1.0)
 pause 1.0
 hide fade onlayer curtain
 with Dissolve(1.0)
 show beatrice_v001 smile at mei_left
 show nao_v002 normal at mei_right
 with Dissolve(0.5)
 show nao_v002 normal at active
 show beatrice_v001 smile at inactive
 nao '...By the way, Beatrice. Why did you call me here today?'
 show beatrice_v001 smile at active
 show nao_v002 normal at inactive
 beatrice 'No reason in particular. I just wanted to drink tea with you.'
 show nao_v002 fuan at active
 show beatrice_v001 smile at inactive
 nao '...Just that?'
 show beatrice_v001 normal at active
 show nao_v002 fuan at inactive
 beatrice 'Just calling you here for this... is there a problem with that?'
 show nao_v002 smile at active
 show beatrice_v001 normal at inactive
 nao "No. I'm simply glad to enjoy a delicious cup of tea."
 show nao_v002 normal at active
 show beatrice_v001 normal at inactive
 nao '(...I wonder about this. Did the witch Beatrice really call me here just to drink tea with her?)'
 show nao_v002 sinken at active
 show beatrice_v001 normal at inactive
 nao "(I'm doubtful of that. She might be planning something... maybe.)"
 show beatrice_v001 normal_close at active
 show nao_v002 sinken at inactive
 beatrice "...I know what you're thinking."
 show nao_v002 odoroki at jump_transform,active
 show beatrice_v001 normal_close at inactive
 nao 'Huh...?'
 show beatrice_v001 normal at active
 show nao_v002 odoroki at inactive
 beatrice 'You have been summoned to have tea with me as someone originally not meant to be here. Does that feel strange to you?'
 show nao_v002 normal at nod_transform,active
 show beatrice_v001 normal at inactive
 nao "...Yes. To be honest, I'm already on guard. I'm wondering when you're going to pull out my shirikodama. "
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide beatrice_v001
 hide nao_v002
 hide fade onlayer curtain
 show beatrice_v001 futeki at mei_center
 with Dissolve(0.08333333333333333)
 show beatrice_v001 futeki at updown_shake_transform,active
 beatrice 'Pfff... Khhahahahahaha!!! Out of all the metaphors you could have chosen, you went with... shirikodama!?!'
 show beatrice_v001 futeki_close at active
 beatrice "I'm not anything like a kappa, so don't anticipate me doing something like that! *cackle*cackle*cackle*!!!"
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide beatrice_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show nao_v002 normal at mei_center
 with Dissolve(0.5)
 show nao_v002 normal at active
 nao "How can I know you won't? After all, I don't know very much about witches."
 show nao_v002 normal at active
 nao "It's entirely possible that there is a witch whose hobby is collecting shirikodama. "
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 590)
  zoom 1.3
 hide nao_v002
 hide fade onlayer curtain
 show beatrice_v001 futeki_close at mei_center
 with Dissolve(0.08333333333333333)
 show beatrice_v001 futeki_close at chara_shake_transform,active
 beatrice 'Heehehehehehehehehe!!! Hilarious, truly hilarious! '
 show beatrice_v001 futeki_close at active
 beatrice 'I never thought a little girl like you would say that... *giggle*giggle*, *cackle*cackle*cackle*!!'
 show black_cover onlayer curtain as fade with Dissolve(0.3333333333333333)
 camera:
  pos (960, 540)
  zoom 1.0
 hide beatrice_v001
 hide fade onlayer curtain
 with Dissolve(0.08333333333333333)
 show nao_v002 fuan at mei_center
 with Dissolve(0.5)
 show nao_v002 fuan at active
 nao '(That was a powerful roar of laughter. I think I hit her funny bone?)'
 hide nao_v002
 with Dissolve(0.2)
 show beatrice_v001 smile_close at mei_left
 show nao_v002 fuan at mei_right
 with Dissolve(0.5)
 show beatrice_v001 smile_close at active
 show nao_v002 fuan at inactive
 beatrice '*cackle*cackle*cackle*! Ha, hahaha... haaah, hoooh... hoo. You got me good. The fact you have the bravery to joke back at me is wonderful.'
 show nao_v002 normal at active
 show beatrice_v001 smile_close at inactive
 nao "You got me too. I didn't expect you to laugh that hard."
 show nao_v002 normal at active
 show beatrice_v001 smile_close at inactive
 nao 'I just realized... that witches are quite emotional.'
 show beatrice_v001 smile at active
 show nao_v002 normal at inactive
 beatrice "It's only natural. Like humans, witches will laugh if they are amused, and retaliate if they are being ridiculed."
 show beatrice_v001 smile_close at active
 show nao_v002 normal at inactive
 beatrice "Although, if you want me to be fearsome, then I can't help but meet that expectation... *cackle*cackle*."
 show nao_v002 fuan at active
 show beatrice_v001 smile_close at inactive
 nao "No kidding. I still have many things I want and need to do. I apologize, but I don't want to go to hell at this age."
 show beatrice_v001 futeki at active
 show nao_v002 fuan at inactive
 beatrice '...Hoh? And yet when you first stepped into that "World", it seemed you quickly wanted to fall into despair and die...?'
 show nao_v002 fuan_close at active
 show beatrice_v001 futeki at inactive
 nao "...You can see through that, even. I'm no match for you."
 show beatrice_v001 futeki at updown_shake_transform,active
 show nao_v002 fuan_close at inactive
 beatrice "*cackle*cackle*cackle*... I've been thinking how we'll never be able to compete on equal footing. Oh, how it's a shame, it really is too bad!"
 show beatrice_v001 smile at active
 show nao_v002 fuan_close at inactive
 beatrice 'The experience and knowledge you have is nothing compared to mine as a thousand-year-old Golden Witch.'
 show nao_v002 normal at active
 show beatrice_v001 smile at inactive
 nao "It's fine. You don't need to intimidate me like that; I know the difference in our rank. I'm not going to oppose you."
 show nao_v002 normal at active
 show beatrice_v001 smile at inactive
 nao "I'm sure you can reach for far more stars than I can."
 show beatrice_v001 normal at active
 show nao_v002 normal at inactive
 beatrice 'Ah... yes, that is true. And yet, there are things that even I cannot do.'
 show beatrice_v001 normal_close at active
 show nao_v002 normal at inactive
 beatrice 'Perhaps it is from this strange coincidence of us meeting that I can enjoy the changes that it sparked, as well as understand its irregularity...'
 show nao_v002 normal at active
 show beatrice_v001 normal_close at inactive
 nao "...It seems even the witch Beatrice has memories of being frustrated and sad over things she couldn't do."
 show beatrice_v001 smile at active
 show nao_v002 normal at inactive
 beatrice 'Hmm... you truly are fearless. Other witches would have immediately sent your severed head flying across the room out of disrespect for that single inquiry.'
 show nao_v002 fuan at chara_shake_transform,active
 show beatrice_v001 smile at inactive
 nao '......Wh-...'
 show beatrice_v001 normal at active
 show nao_v002 fuan at inactive
 beatrice 'Don\'t be so tense. It\'s not like I\'m angry. I have always been aware of your "past". I commend you for reaching this point.'
 show beatrice_v001 normal_close at active
 show nao_v002 fuan at inactive
 beatrice "Wishing you were never born...huh? And yet, despite feeling all that despair, you wriggled through it. That's quite significant."
 show nao_v002 normal at active
 show beatrice_v001 normal_close at inactive
 nao 'Beatrice...?'
 show beatrice_v001 smile at active
 show nao_v002 normal at inactive
 beatrice 'Hmm... please forget that nonsense. It seems I am getting a little sentimental.'
 call chapter_end
 jump chara452001_02