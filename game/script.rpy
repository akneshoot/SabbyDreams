# Определение персонажей игры.
define sabby = Character('Сэбби')
define mother = Character('Мама')
define text = ('...')
define nastya = ('Настя')
define anya = ('Аня')
define annmother = ('Мария Богова')
define father = ('Папа')
define mother_and_father = ('Мама и Папа')
define doctor= ('Врач')
define ktoto= ('Кто-то')
define psih = ('Психолог')
define monster = ('Монстр')
define n = Character(None, kind=nvl)
define bad_end = 0
define happy_end = 0


image room sabby = 'Back/roomsabby.jpg'
image sabby = 'Role/Sb.png'
image glavnoe = 'Back/osnova.jpg'
image padik = 'Back/padik.png'
image sad sabby = 'Role/sad sb.png'
image happy mother = 'Role/mother.png'
image street = 'Back/street.png'
image living room = 'Back/livingroom.png'
image father = 'Role/father.png'
image street1 = 'Back/street1.png'
image street2 = 'Back/street2.png'
image street3 = 'Back/street3.png'



#image annmother = ''
#image anya = ''
#image nastya = ''


label start:
    # 1 frame
    scene glavnoe
    if persistent.ending1:
        "Вы уже прошли игру, если хотите перепройти, то нажмите на экран."
    text "Глава первая"
    #2 frame
    scene roomsabby
    with fade
    show happy mother:
        xalign 0.8 yalign 1.8
    mother "{cps=40}Доченька, пора просыпаться, папа уже уехал, а ты даже не пожелала ему удачного дня."
    #3 frame
    show sad sabby:
        xalign 0.1 yalign 3.4
    sabby "{cps=40}Да, мам, еще пять минут"
    #4 frame
    mother "{cps=40}Давай вставай, завтрак на столе, не забудь почистить зубы,а я побежала на работу, буду через 6 часов."
    #5 frame
    sabby "{cps=40}Да-да, встаю"
    #6 frame
    hide sad sabby
    hide happy mother
    text "..."
    #7 frame
    scene padik
    with fade
    show sabby
    sabby "{cps=40}Так, зубы почистила, завтрак съела, можно пойти гулять"
    #8 frame 
    show sabby:
        xalign 0.1
    show nastya:
        xalign 0.8 yalign -1.0
    nastya "{cps=40}Ой, Сэбби, привет, как ты уже подросла"
    #9 frame 
    sabby "{cps=40}Здравствуйте, Анастасия Павловна"
    #10 frame
    hide nastya
    show serious_nastya:
        xalign 0.8 yalign -2.2
    nastya "{cps=40}Да какая я тебе Анастасия Павловна, просто Настя, мне 16, а не 40"
    #11 frame *update
    sabby "{cps=40}Извините, я не хотела вас обидеть."
    sabby "{cps=40}Как вы себя чувствуете, как ваши родители?"
    #12 frame
    nastya "..."
    nastya "{cps=40}Ты неисправима."
    nastya "{cps=40}Родители нормально, папа ходит на химотерапию, вроде, легче становится, мама, выплачивая долги, потеряла себя, завела кучу проблем со здоровьем, теперь с ногами проблемы…"
    nastya "{cps=40}Мне пришлось устроиться официанткой неподалеку, чтобы обеспечить семью"
    hide serious_nastya
    show sad_nastya:
      xalign 0.8 yalign -1.0
    nastya "{cps=40}Черт, прости..."
    #15 frame
    hide sabby
    show sad sabby:
        xalign 0.1 yalign 2.9

    sabby "{cps=40}За что ты извиняешься?" 
    #16 frame
    nastya "{cps=40}За то, что нагружаю тебя своими проблемами."
    nastya "{cps=40}Мне просто.."
    nastya "{cps=40}Просто некому выговориться, понимаешь?"
    sabby "{cps=40}Ага..."
    #18 frame
    hide sad_nastya
    show serious_nastya:
        xalign 0.8 yalign -2.2
    nastya "{cps=40}Ладно."
    nastya "{cps=40}Ты, наверное, торопишься, с Аней ведь гулять идешь?"
    sabby "{cps=40}Ну, да"
    nastya "{cps=40}Тогда беги, не буду тебя задерживать, хорошей прогулки!"
    hide sad sabby
    show sabby:
        xalign 0.1 yalign 1.0
    sabby "{cps=40}Спасибо!"
    #22 frame
    hide sabby
    nastya "{cps=40}Аня.."
    nastya "{cps=40}До сих пор никак не могу понять, как у таких самовлюбленных родителей могла родиться Аня"
    nastya "{cps=40}И почему при таком достатке они живут в таком районе, как наш?"
    hide serious_nastya
    #24 frame
    scene street
    with fade
    text "..."
    show serious_anya:
        xalign 0.2 yalign 15.4
    anya "{cps=40}Сэбби!!! Привет!!!"
    show sabby:
        xalign 0.8 yalign 1.0
    sabby "{cps=40}Аня!!!"
    sabby "{cps=40}У тебя все хорошо?"
    hide serious_anya
    show sad_anya:
      xalign 0.2 yalign 6.4
    #menu
    menu:
        anya "{cps=40}Еле убежала от мамы погулять с тобой, она, как всегда, заладила, что не нужно мне общаться с соседями."

        "Странная она.":
            $ happy_end += 1
            $ renpy.notify("Ваш ответ повлиял на развитие событий")
            jump strange
            
        "Пошли поиграем?":
            $ bad_end += 1
            $ renpy.notify("Ваш ответ повлиял на развитие событий")
            jump poigrat
    return


label strange:
    hide sabby
    show sad sabby:
        xalign 0.8 yalign 2.9
    sabby "{cps=40}Странная она."
    anya "{cps=40}Да. Говорит всем постоянно, что она хозяйка дома."
    #menu
    menu:
        anya "{cps=40}Но при этом из домашних обязанностей и воспитания на ней лежит только пару раз в день прочитать мне лекцию о том, что надо быть красивой и общаться с детьми, чьи родители на том же уровне, что и мои. Все остальное делают уборщицы и няня."

        "Что значит на том же уровне?":
            $ bad_end += 1
            $ renpy.notify("Ваш ответ повлиял на развитие событий")
            jump level
            
        "Пошли поиграем?":
            $ happy_end += 1
            $ renpy.notify("Ваш ответ повлиял на развитие событий")
            jump poigrat
            
    return


label poigrat:
    hide serious_anya
    hide sad_anya
    show anya:
      xalign 0.2 yalign 6.4
    sabby "{cps=40}Понятно."
    sabby "{cps=40}Пошли поиграем?"
    anya "{cps=40}Да, давай, это поможет мне отвлечься."
    hide sabby
    hide sad sabby
    hide anya
    scene street
    with fade
    text "{cps=40}И действительно, у Ани получилось на время забыться. Забыть все, что происходит с ней за пределами этой площадки, забыть все, что происходит у нее дома. Но это не может длиться вечно. Когда-то все равно приходится возвращаться туда, откуда стоит бежать."
    #35 frame
    show sabby:
        xalign 0.8 yalign 1.0
    show anya:
      xalign 0.2 yalign 6.4
    annmother "{cps=40}АНЯ!"
    hide anya
    hide sabby
    show sad_anya:
      xalign 0.2 yalign 6.4
    show very_sad_sabby:
       xalign 0.8 yalign 2.9
    annmother "{cps=40}Ты опять с этой девчонкой?!"
    annmother "{cps=40}Сколько раз тебе нужно повторять, чтобы ты с ней 
    не общалась!"
    anya "{cps=40}Ой, мама все-таки нашла меня."
    anya "{cps=40}Надо бежать."
    sabby "{cps=40}Эх, ладно, пока.."
    anya "{cps=40}Пока!"
    hide sad_anya
    show serious_anya:
      xalign 0.2 yalign 15.4
    anya "{cps=40}Я постараюсь завтра тоже выйти, поиграть."
    hide very_sad_sabby
    show sad sabby:
      xalign 0.8 yalign 3.4
    sabby "{cps=40}Хорошо, буду тебя ждать."
    hide sad sabby
    hide serious_anya
    hide sad_anya
    hide anya
    text "..."
    jump prodoljenie

    return



label level:
    hide sabby
    show sad sabby:
        xalign 0.8 yalign 2.9
    hide sad_anya
    show serious_anya:
      xalign 0.2 yalign 15.4
    sabby "{cps=40}А что для твоих родителей считается таким же уровнем, как у них?"
    anya "{cps=40}Ну…"
    anya "{cps=40}Я не знаю…"
    anya "{cps=40}Если честно, я ее слушаю краем уха, потому что чаще всего мама отходит от темы и говорит о том, какая она прекрасная и как много для всех делает."
    jump poigrat
    return



label prodoljenie:
    #40 frame
    scene living room
    with fade
    show sabby:
        xalign 0.1 yalign 1.0
    sabby "{cps=40}Привет, мам, пап."
    show father:
        xalign 0.99 yalign -0.1
    show happy mother:
        xalign 0.7 yalign 1.5
    father "{cps=40}Привет."
    father "{cps=40}Ты с Аней гуляла?"
    hide sabby
    show sad sabby:
        xalign 0.1 yalign 2.9
    sabby "{cps=40}Да. Только вот ее мама быстро забрала домой."
    mother "{cps=40}Ну хоть немного смогли проветриться."
    mother "{cps=40}Давай иди кушай, пока еда не остыла и стоит идти ложиться спать."
    mother "{cps=40}Уже достаточно поздно, тебе стоит отдохнуть, завтра тебя ждет особый день, подготовься к нему хорошо, милая."
    sabby "{cps=40}Да, хорошо, мам."
    hide sad sabby
    hide happy mother
    hide father
    text "..."
    #47 frame
    scene glavnoe
    with fade
    text "Конец первой главы."
    scene glavnoe
    with fade
    text "Глава вторая."
    #49 frame
    scene street1
    with fade
    text "{cps=40}Представьте себе какую-нибудь точку мира, которая находится ближе всего к экватору. Лето там очень теплое, солнечное."
    #50 frame
    scene street2
    with fade
    text "{cps=40}Так вот и в городке, где живет Сэбби сегодня настолько жарко, что все люди выходят на улицу, чтобы погреться на таком долгожданном солнце."
    #51 frame
    scene street3
    with fade
    text "{cps=40}А в нашем дворе сегодня особенный день не только из-за теплой погоды..."
    #52 frame
    scene roomsabby
    with fade
    text "..."
    show happy_father:
        xalign 0.99 yalign -0.1
    show happy mother:
        xalign 0.7 yalign 1.5
    show cake:
        xalign 0.85 yalign 0.7
    mother_and_father "{cps=40}С днем рождения, Сэбби!!!"
    show sad sabby:
        xalign 0.1 yalign 2.9
    sabby "{cps=40}Мам, пап, зачем так рано…"
    mother "{cps=40}Потому что мы на девятилетие нашей любимой доченьки подготовили сюрприз! Загадывай желание, задувай свечи и начинай одеваться."
    sabby "{cps=40}Куда?"
    mother "{cps=40}Как это куда? Конечно, же в ресторан!"
    sabby "{cps=40}Но мы ни разу не были даже в кафе, это слишком дорого, может, не пойдем?"
    sabby "{cps=40}Покушаем дома тортик, выпьем чай…"
    mother "{cps=40}Это даже не обсуждается."
    mother "{cps=40}Мы любим тебя радовать, пусть зачастую и мелочами. А сегодня такой день!"
    hide sad sabby
    show sabby:
        xalign 0.1 yalign 1.0
    mother "{cps=40}Ты же так хотела попробовать роллы, так что мы сейчас собираемся и едем осуществлять твою маленькую хотелку."
    mother "{cps=40}Да, папа?"
    hide happy_father
    hide cake
    show father:
        xalign 0.99 yalign -0.1
    show cake:
        xalign 0.85 yalign 0.7
    
    
    #menu
    menu:
        father "{cps=40}Да."

        "Может, все-таки дома посидим?":
            $ happy_end += 1
            $ renpy.notify("Ваш ответ повлиял на развитие событий")
            jump maybe
            
        "Ура!!!":
            $ happy_end += 1
            $ renpy.notify("Ваш ответ повлиял на развитие событий")
            jump yes
            
        "Но я не хочу...":
            $ bad_end += 1
            $ renpy.notify("Ваш ответ повлиял на развитие событий")
            jump no
            
    return


label maybe:
    hide father
    hide cake
    show happy_father:
        xalign 0.99 yalign -0.1
    show cake:
        xalign 0.85 yalign 0.7
    hide sabby
    show sad sabby:
        xalign 0.1 yalign 2.9
    sabby "{cps=40}Может, все-таки дома посидим?"
    mother "{cps=40}Не переживай, солнышко, всё будет хорошо"
    hide father
    hide sad sabby
    hide happy mother
    hide cake
    hide happy_father
    scene street2
    with fade
    text "{cps=40}Все начали собираться, мама красилась, Вика подражала ей, а папа пытался подобрать подходящий галстук."
    scene living room
    with fade
    show happy_father:
        xalign 0.99 yalign -0.1
    show sad sabby:
        xalign 0.1 yalign 2.9
    show happy mother:
        xalign 0.8 yalign 1.8
    mother "{cps=40}Так, ну вроде все готовы, можем ехать!"
    hide happy mother
    hide sad sabby
    hide happy_father
    text "..."
    jump prodoljenie2
    return


label yes:
    hide cake
    hide father
    show happy_father:
        xalign 0.99 yalign -0.1
    show cake:
        xalign 0.85 yalign 0.7
    sabby "{cps=40}Ура!!!"
    hide happy_father
    hide sabby
    hide happy mother
    hide cake
    scene street2
    with fade
    text "{cps=40}Все начали собираться, мама красилась, Вика подражала ей, а папа пытался подобрать подходящий галстук."
    scene living room
    with fade
    show happy_father:
        xalign 0.99 yalign -0.1
    show sabby:
        xalign 0.1 yalign 1.0
    show mother:
        xalign 0.8 yalign 1.8
    mother "{cps=40}Так, ну вроде все готовы, можем ехать!"
    hide mother
    hide sabby
    hide happy_father
    text "..."
    jump prodoljenie2
    return

label no:
    hide sabby
    hide father
    show angry_father:
        xalign 0.99 yalign -0.1
    hide happy mother
    show serious_mother:
        xalign 0.7 yalign -2.0
    hide cake
    show cake:
        xalign 0.85 yalign 0.7
    show sad sabby:
        xalign 0.1 yalign 2.9
    sabby "{cps=40}Но я не хочу..."
    text "..."
    hide angry_father
    hide cake
    show father:
        xalign 0.99 yalign -0.1
    show cake:
        xalign 0.85 yalign 0.7
    father "{cps=40}Это не обсуждается."
    father "{cps=40}Мы уже забронировали столик и внесли депозит, ты понимаешь, что часть денег уже заплачена?"
    hide father
    hide sad sabby
    hide serious_mother
    hide cake
    scene street2
    with fade
    text "{cps=40}Все начали собираться, мама красилась, Вика подражала ей, а папа пытался подобрать подходящий галстук."
    scene living room
    with fade
    show happy_father:
        xalign 0.99 yalign -0.1
    show sabby:
        xalign 0.1 yalign 1.0
    show mother:
        xalign 0.8 yalign 1.8
    mother "{cps=40}Так, ну вроде все готовы, можем ехать!"
    hide mother
    hide sabby
    hide happy_father
    text "..."
    jump prodoljenie2
    return


label prodoljenie2:
    #69 frame
    scene restaurant 
    with fade
    
    show happy_father:
        xalign 0.1 yalign -0.1
    show happy mother:
        xalign 0.3 yalign 1.8
    show sabby:
        xalign 0.2 yalign 1.0
    show cafe_nastya:
      xalign 0.9 yalign -1.0
    nastya "{cps=40}Здравствуйте! "
    nastya "{cps=40}Сегодня я буду вашим официантом."
    nastya "{cps=40}Сэбби, поздравляю тебя с днем рождения! Счастья, здоровья и всего самого наилучшего!"
    sabby "{cps=40}Здравствуйте, спасибо большое"
    mother "{cps=40}За какой столик мы можем присесть?"
    nastya "{cps=40}Специально для вас я заняла столик у окна, чтобы вы могли есть и смотреть на центральную площадь города."
    nastya "{cps=40}Прошу, присаживайтесь, вот меню"

    #РАБОТА МАТВЕЯ!!!сюда надо как-то впихнуть меню с едой. (сделать код так чтобы было написано не именно выбрать блюдо, а просто что сэбби приглянулось блюдо, которое пользователь тыкнет)
    hide cafe_nastya
    hide happy_father
    hide happy mother
    text "{cps=40}У сэбби разбегались глаза, все выглядело так заманчиво, но когда она кинула свой взгляд на цены, перехотелось есть вовсе."
    show happy_father:
        xalign 0.99 yalign -0.1
    show happy mother:
        xalign 0.8 yalign 1.8
    hide sabby
    show sad sabby:
        xalign 0.1 yalign 2.9
    

    #menu
    menu:
        sabby "{cps=40}Как тут дорого!"

        "Пожалуй, закажу только одно блюдо":
            $ happy_end += 1
            $ renpy.notify("Ваш ответ повлиял на развитие событий")
            jump one
            
        "Хочу попробовать всё!":
            $ bad_end += 1
            $ renpy.notify("Ваш ответ повлиял на развитие событий")
            jump all
            
        "Может, все-таки домой?":
            $ bad_end += 1
            $ renpy.notify("Ваш ответ повлиял на развитие событий")
            jump home
            
    return

    
    label one:
    hide happy_father
    show father:
        xalign 0.99 yalign -0.1
    sabby "{cps=40}Пожалуй, закажу только одно блюдо"
    mother "{cps=40}Не забывай, мы празднуем твой день рождения, закажи столько, сколько съешь." 
    mother "{cps=40}Можешь даже чуть больше, заберем домой и оставим на ужин"
    hide sad sabby
    show sabby:
        xalign 0.2 yalign 1.0
    sabby "{cps=40}Хорошо"

    #РАБОТА МАТВЕЯ!!! здесь, если получится, когда пользователь выберет что будет в итоге кушать сэбби будет выводиться текст в зависимости от того что выбрали.

    sabby "{cps=40}Тогда я буду лимонад, роллы с креветкой и один онигири с сёмгой"
    father "{cps=40}Мне пиво и калифорнию, а жене лимонад и филадельфию."
    jump prodoljenie3
    return

    label all:
    hide happy_father
    hide sad sabby
    show sabby:
        xalign 0.2 yalign 1.0
    show angry_father:
        xalign 0.99 yalign -0.1
    sabby "{cps=40}Хочу попробовать всё!"
    father "{cps=40}Не забывай о финансах. Заказывай столько, сколько сможешь съесть."
    hide sabby
    show sad sabby:
        xalign 0.1 yalign 2.9
    sabby "{cps=40}Хорошо"

    #РАБОТА МАТВЕЯ!!! здесь, если получится, когда пользователь выберет что будет в итоге кушать сэбби будет выводиться текст в зависимости от того что выбрали.

    sabby "{cps=40}Тогда я буду лимонад, роллы с креветкой и один онигири с сёмгой"
    father "{cps=40}Мне пиво и калифорнию, а жене лимонад и филадельфию."
    jump prodoljenie3
    return


    label home:
    hide happy_father
    show father:
        xalign 0.99 yalign -0.1
    sabby "{cps=40}Может, все-таки домой?"
    mother "{cps=40}Не забывай, мы празднуем твой день рождения, закажи столько, сколько съешь." 
    mother "{cps=40}Можешь даже чуть больше, заберем домой и оставим на ужин"
    hide sad sabby
    show sabby:
        xalign 0.2 yalign 1.0
    sabby "{cps=40}Хорошо"

    #РАБОТА МАТВЕЯ!!! здесь, если получится, когда пользователь выберет что будет в итоге кушать сэбби будет выводиться текст в зависимости от того что выбрали.

    sabby "{cps=40}Тогда я буду лимонад, роллы с креветкой и один онигири с сёмгой"
    father "{cps=40}Мне пиво и калифорнию, а жене лимонад и филадельфию."
    jump prodoljenie3
    return


label prodoljenie3:
hide father
hide angry_father
hide happy mother
hide sabby
hide sad sabby
show cafe_nastya:
 xalign 0.55 yalign -1.0
nastya "{cps=40}Хорошо, ожидание заказа до 20 минут"
hide cafe_nastya
text "{cps=40}Семья просидела около часа в ресторане и наслаждалась как видом из окна, прекрасным звуковым сопровождением, так и замеатльно приготовленной едой, которую они не так уж и часто ели."
show father:
    xalign 0.99 yalign -0.1
father "{cps=40}Ну всё, поели, попили, можем ехать домой"
father "{cps=40}А то Сэбби заскучала, смотрит уже минут десять в одну точку и ничего не говорит."
father "{cps=40}Подъем!"
show mother:
    xalign 0.1 yalign 1.8
mother "{cps=40}Сэбби, вставай..."
hide father
show angry_father:
    xalign 0.99 yalign -0.1
hide mother
show serious_mother:
    xalign 0.1 yalign -2.0
father "{cps=40}Хватит придуриваться!"
mother "{cps=40}Сэбби?.."
mother "{cps=40}Сэбби!"
hide angry_father
hide serious_mother
show sad_mother:
    xalign 0.1 yalign -2.0
mother "{cps=40}Она вся трясется!"
mother "{cps=40}У нее пена изо рта!"
mother "{cps=40}Вызовите скорую!"
hide sad_mother
mother "{cps=40}Все будет хорошо!"
mother "{cps=40}Ты слышишь?"
mother "{cps=40}Только не беспокойся, сейчас приедут доктора!!!"
scene osnova
with fade
text "Конец второй главы"
scene osnova
with fade
text "Глава третья"
scene palata
with fade
show father:
    xalign 0.1 yalign -0.1
show sad_mother:
    xalign 0.3 yalign -2.0
show doctor:
  xalign 0.9 yalign -0.2
doctor "{cps=40}Девочка сейчас находится в сложном стостоянии, ее организму приходится нелегко." 
doctor "{cps=40}Она не умрет, но шансы, что после реабилитации она будет ездить на инвалидной коляске, велики."
doctor "{cps=40}Будьте к этому готовы."
hide doctor
hide sad_mother
show sad_mother:
    xalign 0.8 yalign -2.0
mother "{cps=40}Неужели все так плохо..."
mother "{cps=40}Сэбби, дорогая, просыпайся скорее, ты нам очень нужна..."
mother "{cps=40}Мы любим тебя!"
father "{cps=40}Если на реабилитацию у нас нашлись деньги, учитывая, что ближайший месяц нам придется во многом себе отказывать"
father "{cps=40}То на новые ноги у нас нет средств."
mother "{cps=40}Моя милая доченька, как я могу тебе помочь?!"
father "{cps=40}Что-нибудь придумаем."
father "{cps=40}Она сильная, да и мы справимся."
father "{cps=40}Должны справиться."
hide sad_mother
hide father
text "{cps=40}Пока родители убивались в своем горе, никто не знал что могло происходить по ту сторону больничной палаты."
text "{cps=40}Шли дни, Сэбби так и оставалась в коме. Помимо ее физически плохого состояния, ей было тяжело морально."
text "{cps=40}Вы, вероятно, слышали где-то предположения и о том, что люди, выпадая из реальности, попадают в астрал и видят загробный мир, или же находятся на пути к нему?" 
scene astral
with fade
text "{cps=40}Сэбби не понимала кто она, где находится и что вообще нужно сделать, чтобы вернуться к своей обычной жизни."
text "{cps=40}Но тут что-то непонятное подало голос, если бы в этом страшном месте не было бы тишины, то Сэбби и не услышала ничего, но сейчас она отчетливо понимала, что с ней говорят."
scene astral
with fade
ktoto "{cps=40}Сэбби..."
ktoto "{cps=40}Ты меня все-таки смогла увидеть, значит я знаю как забрать тебя"
ktoto "{cps=40}Я доберусь до тебя!"
ktoto "{cps=40}Ты слышишь?"
ktoto "{cps=40}Я заберу тебя с собой!"
scene astral
with fade
text "{cps=40}После этих слов последовало тяжелое дыхание, оно отчетливо чувствовалось над ухом, хотелось просто закрыть уши и надеяться, что это скоро все закончится, но голос снова начал произносить свои трепещущие душу возгласы."
scene astral
with fade
ktoto "{cps=40}Я доберусь до тебя!"
ktoto "{cps=40}Ты слышишь?"
ktoto "{cps=40}Я заберу тебя с собой!"

#РАБОТА МАТВЕЯ!!! здесь нужно будет сделать лабиринт (типо сэбби убегает от монстра и находит выход в свой мир)


scene astral
with fade
text "..."
scene palata
with fade
show sad sabby:
    xalign 0.1 yalign 2.9
sabby "{cps=40}Где я?"
show sad_mother:
    xalign 0.8 yalign -2.0
mother "{cps=40}Дорогая, наконец-то ты очнулась! "
mother "{cps=40}Боже мой...."
mother "{cps=40}Эти недели были невыносимыми, я каждый день приходила к тебе и молилась за тебя!"
sabby "{cps=40}Что произошло?"
mother "{cps=40}Врачи так и не смогли понять что это было, но во время празднования твоего дня рождения ты просто смотрела в одну точку, а потом..."
mother "{cps=40}Как я рада, что ты очнулась!"
hide sad sabby
show very_sad_sabby:
    xalign 0.1 yalign 2.9
sabby "{cps=40}Мне снилось очень многое..."
sabby "{cps=40}Оно говорило со мной, оно хочет забрать меня!"
hide sad_mother
show serious_mother:
    xalign 0.8 yalign -2.0
mother "{cps=40}Что за оно?.."
sabby "{cps=40}Я не смогла его разглядеть, но оно кричало очень страшные вещи."
sabby "{cps=40}Нет..."
sabby "{cps=40}Оно заберет меня, мама!"
sabby "{cps=40}Оно найдет меня и заберет с собой!"
sabby "{cps=40}Я не хочу, мама!"

#menu
menu:
    mother "{cps=40}Не беспокойся, дорогая, никто тебя не тронет. Страшный сон закончился, теперь мы вместе, не переживай."

    "Но оно сказало, что заберет меня!":
        $ happy_end += 1
        $ renpy.notify("Ваш ответ повлиял на развитие событий")
        jump zaberet
        
    "Я хочу домой":
        $ bad_end += 1
        $ renpy.notify("Ваш ответ повлиял на развитие событий")
        jump want_home
        
    "А где папа?":       
        $ happy_end += 1
        $ renpy.notify("Ваш ответ повлиял на развитие событий")
        jump where_father
       
return


label zaberet:
sabby "{cps=40}Но оно сказало, что заберет меня!"
mother "{cps=40}Хватит. Это просто сон!"
hide very_sad_sabby
show sad sabby:
    xalign 0.1 yalign 2.9
jump prodoljenie4
return

label want_home:
hide very_sad_sabby
show sad sabby:
    xalign 0.1 yalign 2.9
sabby "{cps=40}Я хочу домой"
jump prodoljenie4
return

label where_father:
hide very_sad_sabby
show sad sabby:
    xalign 0.1 yalign 2.9
sabby "{cps=40}А где папа?"
mother "{cps=40}Папа на работе, он сказал, что его срочно вызвали."
jump prodoljenie4
return

label prodoljenie4:
mother "{cps=40}Сейчас придет доктор и выпишет тебя, я пока пойду подышу на свежем воздухе, а то столько всего произошло."
hide serious_mother
text "..."
show doctor:
  xalign 0.9 yalign -0.2
doctor "{cps=40}Ну что, как ты себя чувствуешь?"
doctor "{cps=40}Все в порядке?"
sabby "{cps=40}Да, но мне снился очень жуткий сон!"
hide sad sabby
show very_sad_sabby:
    xalign 0.1 yalign 2.9
sabby "{cps=40}Оно придет за мной, я знаю!"
sabby "{cps=40}Мама мне не верит..."
sabby "{cps=40}Помогите!!!!"
doctor "{cps=40}Все в порядке, сны часто снятся."
sabby "{cps=40}Но это был необычный сон!"
doctor "{cps=40}Так, ладно."
doctor "{cps=40}Вижу, твое физическое состояние в порядке, позови маму, пожалуйста."
doctor "{cps=40}Подожди ее, пожалуйста, в коридоре."
hide very_sad_sabby
show sad sabby:
    xalign 0.1 yalign 2.9
sabby "{cps=40}Хорошо..."
hide sad sabby
text "..."
show serious_mother:
    xalign 0.1 yalign -2.0
mother "{cps=40}Вы звали?"
doctor "{cps=40}Да, физическое состояние вашей дочери в порядке на удивление, но вот ее реакция на сон кажется мне странной"
doctor "{cps=40}Советую вам обратиться к специалисту."
mother "{cps=40}К специалисту?"
doctor "{cps=40}Да, думаю, ей нужен психолог после перенесенного стресса"
mother "{cps=40}Ох, мы никогда к психологам не обращались, но если это действительно ей поможет..."
mother "{cps=40}Хорошо."
mother "{cps=40}Мы запишемся на прием к психологу."
hide doctor
hide serious_mother
scene osnova
with fade
text "Конец третьей главы"
scene osnova
with fade
text "Глава четвертая"
scene roomsabby
with fade
show very_sad_sabby:
    xalign 0.1 yalign 2.9
sabby "{cps=40}АААААААААА"
show angry_father:
    xalign 0.99 yalign -0.1
father "{cps=40}Да что опять стряслось?!"
father "{cps=40}Ты кричишь каждую ночь с тех пор, как вернулась из больницы!"
sabby "{cps=40}Оно заберет меня!"
sabby "{cps=40}Я не могу, мне страшно!"
sabby "{cps=40}Каждую ночь оно повторяет одно и то же!"
sabby "{cps=40}Оно меня убьет!"
father "{cps=40}Мне это надоело."
father "{cps=40}Света! Иди сюда!"
show serious_mother:
    xalign 0.8 yalign -2.0
mother "{cps=40}Что произошло?"
father "{cps=40}Она опять кричала во сне, разберись с этим!!!"
father "{cps=40}А я пошел спать, мне завтра рано вставать, мне некогда разбираться с ее дурацкими снами!"
hide angry_father
mother "{cps=40}Опять оно снилось?"
sabby "{cps=40}Да..."
mother "{cps=40}Ясно."
mother "{cps=40}Утром я позвоню психологу, он тебе поможет"
hide serious_mother
show mother:
    xalign 0.8 yalign 1.8
mother "{cps=40}А пока пошли попьем чай"
hide very_sad_sabby
show sad sabby:
    xalign 0.1 yalign 2.9
mother "{cps=40}Все равно уже проснулись..."
hide sad sabby
hide mother
scene osnova
with fade
text "{cps=40}Они пили чай, разговаривали, точнее мама Сэбби пыталась завести разговор, но каждая тема заходила в тупик. Девочка не могла до сих пор до конца отойти от тревоги и осознания, что все это очень сильно все походит на реальность."
text "{cps=40}Никто толком и не смог уснуть, кроме отца. Мама и Сэбби решили отвлечься с помощью просмотра любимой теле-передачи, на мгновение девушки забылись и время прошло быстро. Пришло время выяснить причину кошмаров и покончить с ними."
scene psihroom
with fade
show psih:
   xalign 0.95 yalign -6.5
show serious_mother:
    xalign 0.1 yalign -2.0
show sad sabby:
    xalign 0.3 yalign 2.9
psih "{cps=40}Здравствуйте."
psih "{cps=40}Рассказывайте, что вас привело ко мне?"
mother "{cps=40}Мою дочь беспокоят кошмары с тех пор как она упала в обморок на свой день рождение."
mother "{cps=40}Это было три недели назад."
psih "{cps=40}Поняла."
psih "{cps=40}Не могли бы Вы выйти, я хочу пообщаться с Сэбби"
mother "{cps=40}Да, конечно."
mother "{cps=40}Доченька, я буду ждать тебя в коридоре"
psih "{cps=40}Ну что, рассказывай что с тобой"
hide serious_mother
hide sad sabby
hide psih
text "{cps=40}Сэбби рассказывает психологу обо всех кошмарах в ярчайших красках"
show psih:
   xalign 0.95 yalign -6.5
show sad sabby:
    xalign 0.1 yalign 2.9


#menu
menu:
    psih "{cps=40}Понятно. Давай попробуем описать его."

    "Его тело похоже на человеческое":
        jump menu1
    "Он черный":
        jump menu1
    "Его силуэт непонятный":
        jump menu1
return

label menu1:
#menu
menu:
    psih "Понятно. Давай попробуем описать его."

    "Руки тянулись ко мне":
        jump menu2
    "Он бежал за мной":
        jump menu2
return

label menu2:
#menu
menu:
    psih "Понятно. Давай попробуем описать его."

    "Голос казался таким знакомым":
        jump papa_monster
    "Глаза залиты кровью":
        jump monster
return


label papa_monster:
$ renpy.notify("Ваши ответы повлияли на развитие событий")
psih "{cps=40}Надо объеденить все эти характеристики и получить картинку."

#РАБОТА МАТВЕЯ!!! здесь нужно сделать игру-змейку

psih "{cps=40}Боже..."
psih "{cps=40}Мне так жаль, что ты видишь это каждую ночь..."
hide sad sabby
hide psih
show photo_papa at center with dissolve:  
    yalign 0.4
text "*фото монстра, который доставал девочку в кошмарах*"
hide photo_papa with dissolve
show psih:
   xalign 0.95 yalign -6.5
show sad sabby:
    xalign 0.1 yalign 2.9
psih "{cps=40}Мне нужно поговорить с твоей мамой, можешь позвать ее, пожалуйста, и подождать снаружи?"
sabby "{cps=40}Хорошо"
hide sad sabby
show serious_mother:
    xalign 0.1 yalign -2.0
mother "{cps=40}Что с ней?"
psih "{cps=40}Я пообщалась с Вашей дочерью и мы с ней кое-что нарисовали, посмотрите, пожалуйста"
mother "{cps=40}Это мой муж, я вижу, а что не так?"
psih "{cps=40}Сопоставляя ее рассказы о том как проживает ваша семья, о кошмарах и их точке отсчета, а также рисунок, у меня есть неутешительные выводы и я удивлена как ВЫ могли не заметить такое.."
psih "{cps=40}Ваш муж, отец Сэбби, насилует вашу дочь"
hide serious_mother
show sad_mother:
    xalign 0.1 yalign -2.0
mother "{cps=40}Но..."
mother "{cps=40}Как?!"
mother "{cps=40}Он клялся, что будет любить ее как родную, почему он так поступил?"
psih "{cps=40}Как родную?"
mother "{cps=40}Ее отец ушел как только узнал, что у нас будет ребенок, а этот..."
mother "{cps=40}Этот появился в моей жизни сразу после рождения Сэбби"
mother "{cps=40}Почему она мне не рассказывала об этом?!"
psih "{cps=40}У Вашего ребенка нестабильная психика, которая пытается защитить Сэбби, поэтому она забывает практически все негативные моменты, но подсознание не обманешь"
psih "{cps=40}Я обязана передать эту информацию в полицию"
mother "{cps=40}Да я сама напишу на него такое заявление!"
mother "{cps=40}Я засужу его!"
mother "{cps=40}Он не должен жить!"
hide sad_mother
hide psih
text "..."
scene osnova
with fade
text "{cps=40}Прошел месяц. Родители Сэбби развелись, был жуткий скандал. Отец оказался в тюрьме,а мама с дочерью пытаются продолжать жить обычной жизнью, что получается у них с трудностью."
text "{cps=40}Сэбби продолжает ходить к психологу, мама вышла на двойную ставку, чтобы обеспечить семью. Но для них это был лучший вариант."
window hide
scene osnova
pause
n '''Спасибо за прохождение нашей первой игры!

Над ней работали Капустяшки:

- Сидельникова Анастасия

- Капустян Ева

- Емельянов Матвей

- Дашацыренов Лев'''

$ persistent.ending1 = True
return

label monster:
$ renpy.notify("Ваши ответы повлияли на развитие событий")
psih "{cps=40}Надо объеденить все эти характеристики и получить картинку."

#РАБОТА МАТВЕЯ!!! здесь нужно сделать игру-змейку

psih "{cps=40}Боже...{/cps}"
psih "{cps=40}Мне так жаль, что ты видишь это каждую ночь..."
hide sad sabby
hide psih
show photo_monster at center with dissolve:  
    yalign 0.4
text "*фото монстра, который доставал девочку в кошмарах*"
hide photo_monster with dissolve
show psih:
   xalign 0.95 yalign -6.5
show sad sabby:
    xalign 0.1 yalign 2.9
psih "{cps=40}Мне нужно поговорить с твоей мамой, можешь позвать ее, пожалуйста, и подождать снаружи?"
sabby "{cps=40}Хорошо"
hide sad sabby
show serious_mother:
    xalign 0.1 yalign -2.0
mother "{cps=40}Что с ней?"
psih "{cps=40}Я пообщалась с вашей дочерью и мы с ней кое-что нарисовали, посмотрите, пожалуйста"
mother "{cps=40}Что это?"
psih "{cps=40}Это то, что ваша дочь видит постоянно, не только во снах."
psih "{cps=40}Есть подозрения на психическое расстройство, но я не ставлю диагнозы, вам надо обратиться ко врачу"
mother "{cps=40}Можете подсказать нам хорошего психиатра?"
psih "{cps=40}Да, конечно"
psih "{cps=40}Записывайте номер телефона..."
hide serious_mother
hide psih
text "..."
scene osnova
with fade
text "{cps=40}Мама Сэбби осозновала на сколько все может быть серьезным, если не обратиться к хорошему специалисту, поэтому поспешно записала номер телефона и вышла из кабинета психолога. Они с Сэбби вернулись домой."
scene livingroom
with fade
show serious_mother:
    xalign 0.1 yalign -2.0
show sad sabby:
    xalign 0.3 yalign 2.9
show happy_father:
    xalign 0.9 yalign -0.1
father "{cps=40}Вот вы и дома!"
father "{cps=40}Я тут уже стол успел накрыть!"
father "{cps=40}Долго же вас не было!"
father "{cps=40}Чего такие грустные?"
father "{cps=40}Как все прошло?"
mother "{cps=40}Сэбби, покушай и иди спать, нам с папой надо поговорить"
sabby "{cps=40} Хорошо, мам"
hide sad sabby
hide serious_mother
hide happy_father
text "..."
show sad_mother:
    xalign 0.1 yalign -2.0
show father:
    xalign 0.9 yalign -0.1
mother "{cps=40}Психолог сказал, что нам необходимо обратиться к психиатру, так как есть подозрения на расстройство..."
father "{cps=40}Расстройство?"
father "{cps=40}Ты уже нашла специалиста?"
mother "{cps=40}Мне посоветовали одного, но он стоит очень недешево..."
mother "{cps=40}Я не знаю как оплачивать сеансы..."
father "{cps=40}Я устроюсь на подработку"
father "{cps=40}Мы потянем"
father "{cps=40}Должны потянуть."
scene osnova
with fade
text "Конец четвертой главы."
scene osnova
with fade
text "Глава пятая."
scene black
with fade
text "..."
scene skoraya
with fade
show blood_mother:
    xalign 0.5 yalign -2.0
show blood_father:
    xalign 0.1 yalign -0.1
text "..."
hide blood_father
hide blood_mother
scene black
with fade
text "{cps=40}Что происходит..."
scene black
with fade
doctor "{cps=40}Она теряет кровь!"
doctor "{cps=40}Едь быстрее, ей срочно нужна операционная!"
scene pole
with fade
sabby "{cps=40}Где я?"
scene pole
with fade
show mother:
    xalign 0.1 yalign 1.8
show sad sabby:
    xalign 0.8 yalign 2.9
mother "{cps=40}Ура! Я догнала тебя, теперь ты водишь!"
sabby "{cps=40}Вожу?"
sabby "{cps=40}О чем ты?"
sabby "{cps=40}Где я?"
show happy_father:
    xalign 0.3 yalign -0.1
father "{cps=40}Ты чего?"
father "{cps=40}Мы на даче играем в догонялки!"
sabby "{cps=40}В догонялки?"
sabby "{cps=40}На даче??"
sabby "{cps=40}У нас же нет дачи!"
mother "{cps=40}Как это нет"
mother "{cps=40}Мы сейчас прямо на ней)"
mother "{cps=40}Не придуривайся!"
mother "{cps=40}Ты водишь!!!"
hide happy_father
hide mother
text "..."
hide sad sabby
show very_sad_sabby:
    xalign 0.8 yalign 2.9
text "..."
hide very_sad_sabby
scene astral
with fade
show sabby_vahue:
    xalign 0.8 yalign 1.3
ktoto "{cps=40}Сэбби"
ktoto "{cps=40}Вот ты и оказалась в моих руках"
ktoto "{cps=40}Я же говорил, что доберусь до тебя"
sabby "{cps=40}Ты выдумка!"
sabby "{cps=40}Тебя не существует!!!"
show monster:
    xalign 0.1 yalign -0.5
monster "{cps=40}Как это не существует, если я здесь"
hide monster
show monster_nepon:
   xalign 0.1 yalign -0.5
sabby "{cps=40}НЕТ, СПАСИТЕ!"

if bad_end > happy_end:
    hide monster_nepon
    show monster: 
      xalign 0.1 yalign -0.5
    monster "{cps=40}Не переживай, никто тебя не спасет"
    hide monster
    hide sabby_vahue
    window hide
    scene final
    with fade
    pause
    window hide
    scene osnova
    with fade
    n '''Спасибо за прохождение нашей первой игры!
    
    Над ней работали Капустяшки:
    
    - Сидельникова Анастасия
    
    - Капустян Ева
    
    - Емельянов Матвей
    
    - Дашацыренов Лев'''
    $ persistent.ending1 = True
    return

else:
    hide monster_nepon
    hide sabby_vahue
    scene hospital
    with fade
    show blood_father:
      xalign 0.1 yalign -0.1
    show blood_mother:
      xalign 0.3 yalign -2.0
    show doctor:
       xalign 0.9 yalign -0.2
    doctor "{cps=40}Она находится в тяжелом состоянии."
    doctor "{cps=40}Мы смогли остановить кровь, но ее потери были велики."
    doctor "{cps=40}Что произошло?"
    mother "{cps=40}Мы..."
    mother "{cps=40}Мы..."
    father "{cps=40}Ночью я проснулся и пошел в ванную, она у нас совмещена с сан узлом, открыв дверь, я увидел, как Сэбби сидит в ванной."
    father "{cps=40}В ее руках был кухонный нож, а тело кровоточило от множества порезов."
    father "{cps=40}Она уже была без сознания."
    father "{cps=40}Я сразу закричал, чтобы разбудить жену..."
    father "{cps=40}Когда она пришла, я сразу начал звонить в скорую. Что произошло дальше Вы сами знаете."
    doctor "{cps=40}Девочка наблюдалась у психиатра?"
    father "{cps=40}Нет, но недавно нам все же пришлось посетить психолога."
    father "{cps=40}Но это был единоразовый случай."
    father "{cps=40}Ей снились кошмары, они не давали дочурке спать."
    father "{cps=40}Она описала нам какого-то монстра, который ее посещает каждую ночь, и мы со Светланой решили обратиться к психологу."
    hide doctor
    hide blood_father
    hide blood_mother
    scene black
    with fade
    text "..."
    scene astral
    with fade
    show sabby_vahue:
      xalign 0.8 yalign 1.3
    show monster:
       xalign 0.1 yalign -0.5
    sabby "{cps=40}Ты выдумка!"
    sabby "{cps=40}Тебя не существует!!!"
    monster "{cps=40}АХАХАХХАХАХАХАХАХА"
    hide monster
    show monster_nepon:
       xalign 0.1 yalign -0.5
    monster "{cps=40}Ладно, ты мне надоела."
    monster "{cps=40}Я могу дать тебе шанс спастись, но лишь при условии, что ты отгадаешь все правильные ответы на мои вопросы!"
    hide sabby_vahue
    show sad sabby:
      xalign 0.8 yalign 2.9
    hide monster_nepon
    show monster:
      xalign 0.1 yalign -0.5
    monster "{cps=40}Будем считать, что ты готова начать."
    #РАБОТА МАТВЕЯ!!! здесь нужно сделать опрос (по темам трпп и если пользователь отвечает все правильно то наступает продолжение и хорошая концовка если нет то нужно перейти к плохой концовке)
    hide monster
    show monster_nepon:
        xalign 0.1 yalign -0.5
    monster "{cps=40}Нет! Этого не может быть!"
    monster "{cps=40}Ты же девочка, откуда ты знаешь про докер и гит?!"
    hide sad sabby
    show sabby:
      xalign 0.8 yalign 1.0
    sabby "{cps=40}Я просто ходила на семинары к Алексею Игоревичу и делала  практики"
    monster "{cps=40}Ну что ж, придется мне искать другую жертву....("
    hide sabby
    hide monster_nepon
    scene black
    with fade
    text "{cps=40}Год спустя"
    scene pole
    with fade
    show happy_father:
      xalign 0.1 yalign -0.1
    show mother:
      xalign 0.3 yalign 1.8
    show sabby:
       xalign 0.8 yalign 1.0
    father "{cps=40}Ну что, как вам этот участок для дачи?"
    sabby "{cps=40}Он великолепен!"
    mother "{cps=40}Теперь мы можем начать жизнь с нового листа и с нового участка!"
    window hide
    scene osnova
    with fade
    n '''Спасибо за прохождение нашей первой игры!
    
    Над ней работали Капустяшки:
    
    - Сидельникова Анастасия
    
    - Капустян Ева
    
    - Емельянов Матвей
    
    - Дашацыренов Лев'''
    $ persistent.ending1 = True
    return










