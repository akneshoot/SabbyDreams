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
define pravotvet = 0
define nepravotvet = 0

define audio.allmusic = "music/allmusic.ogg"
define audio.shagimusic = "sound/Звуки шагов в подьезде.mp3"
define audio.shagipopolumusic = "sound/Звуки шагов по полу 2.mp3"
define audio.childrenmusic = "sound/Звук детей на площадке.mp3"
define audio.sunmusic = "sound/Звук солнечного дня.mp3"
define audio.roommusic = "sound/Звук комнаты.mp3"
define audio.restaurantmusic = "music/Ретро Джаз Вечеринка — Винтажный ресторанный джаз (www.lightaudio.ru).mp3"
define audio.obmorokmusic = "music/Звук Сэбби потеряла сознание после вскрытия альтушного.mp3"
define audio.palatamusic = "sound/Звук в палате.mp3"
define audio.monstermusic = "music/сцена с монстром 2.ogg"
define audio.govormonstramusic = "sound/Звук шепота монстра.mp3"
define audio.mainmenumusic = "music/main-menu-theme.ogg"
define audio.skorayamusic = "sound/Звук скорой помощи.mp3"


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
    play music allmusic volume 0.5
    # 1 frame
    scene glavnoe
    text "Глава первая."
    #2 frame
    play sound roommusic volume 0.9
    scene roomsabby
    with fade
    show happy mother:
        xalign 0.8 yalign 1.8
    mother "{cps=40}Доченька, пора просыпаться, папа уже уехал, а ты даже не пожелала ему удачного дня."
    #3 frame
    show sad sabby:
        xalign 0.1 yalign 3.4
    sabby "{cps=40}Да, мам, еще пять минут."
    #4 frame
    mother "{cps=40}Давай вставай, завтрак на столе, не забудь почистить зубы,а я побежала на работу, буду через 6 часов."
    #5 frame
    sabby "{cps=40}Да-да, встаю."
    stop sound
    #6 frame
    hide sad sabby
    hide happy mother
    text "..."
    #7 frame
    scene padik
    with fade
    play sound shagimusic volume 0.2
    show sabby
    sabby "{cps=40}Так, зубы почистила, завтрак съела, можно пойти гулять."
    stop sound 
    #8 frame 
    show sabby:
        xalign 0.1
    show nastya:
        xalign 0.8 yalign -1.0
    nastya "{cps=40}Ой, Сэбби, привет, как ты уже подросла."
    #9 frame 
    sabby "{cps=40}Здравствуйте, Анастасия Павловна."
    #10 frame
    hide nastya
    show serious_nastya:
        xalign 0.8 yalign -2.2
    nastya "{cps=40}Да какая я тебе Анастасия Павловна, просто Настя, мне 16, а не 40."
    #11 frame *update
    sabby "{cps=40}Извините, я не хотела вас обидеть."
    sabby "{cps=40}Как вы себя чувствуете, как ваши родители?"
    #12 frame
    nastya "..."
    nastya "{cps=40}Ты неисправима."
    nastya "{cps=40}Родители нормально, папа ходит на химотерапию, вроде, легче становится, мама, выплачивая долги, потеряла себя, завела кучу проблем со здоровьем, теперь с ногами проблемы…"
    nastya "{cps=40}Мне пришлось устроиться официанткой неподалеку, чтобы обеспечить семью."
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
    sabby "{cps=40}Ну, да."
    nastya "{cps=40}Тогда беги, не буду тебя задерживать, хорошей прогулки!"
    hide sad sabby
    show sabby:
        xalign 0.1 yalign 1.0
    sabby "{cps=40}Спасибо!"
    play sound shagimusic volume 0.2
    hide sabby
    text "..."
    stop sound
    nastya "{cps=40}Аня.."
    nastya "{cps=40}До сих пор никак не могу понять, как у таких самовлюбленных родителей могла родиться Аня."
    nastya "{cps=40}И почему при таком достатке они живут в таком районе, как наш?"
    hide serious_nastya
    #24 frame
    scene street
    with fade
    play sound childrenmusic volume 0.2
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
    annmother "{cps=40}Сколько раз тебе нужно повторять, чтобы ты с ней не общалась!"
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
    stop sound
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
    play sound shagipopolumusic volume 0.05
    text "..."
    show sabby:
        xalign 0.1 yalign 1.0
    stop sound
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
    play sound sunmusic volume 0.2
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
    stop sound
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
    mother "{cps=40}Не переживай, солнышко, всё будет хорошо."
    hide father
    hide sad sabby
    hide happy mother
    hide cake
    hide happy_father
    play sound sunmusic volume 0.2
    scene street2
    with fade
    text "{cps=40}Все начали собираться, мама красилась, Сэбби подражала ей, а папа пытался подобрать подходящий галстук."
    stop sound
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
    stop music fadeout 2
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
    play sound sunmusic volume 0.2
    scene street2
    with fade
    text "{cps=40}Все начали собираться, мама красилась, Сэбби подражала ей, а папа пытался подобрать подходящий галстук."
    stop sound
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
    stop music fadeout 2
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
    play sound sunmusic volume 0.2
    scene street2
    with fade
    text "{cps=40}Все начали собираться, мама красилась, Сэббиа подражала ей, а папа пытался подобрать подходящий галстук."
    stop sound
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
    stop music fadeout 2
    text "..."
    
    
    jump prodoljenie2
    return


label prodoljenie2:
    #69 frame
    
    
    scene restaurant 
    with fade
    play music restaurantmusic volume 0.1
    text "..."
    
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
    sabby "{cps=40}Здравствуйте, спасибо большое."
    mother "{cps=40}За какой столик мы можем присесть?"
    nastya "{cps=40}Специально для вас я заняла столик у окна, чтобы вы могли есть и смотреть на центральную площадь города."
    nastya "{cps=40}Прошу, присаживайтесь, вот меню."

    
          
    hide cafe_nastya
    hide happy_father
    hide happy mother
    show menu_cafe:
       xalign 0.8 yalign 0.3
    text "{cps=40}У сэбби разбегались глаза, все выглядело так заманчиво, но когда она кинула свой взгляд на цены, перехотелось есть вовсе."
    hide menu_cafe
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
    sabby "{cps=40}Пожалуй, закажу только одно блюдо."
    mother "{cps=40}Не забывай, мы празднуем твой день рождения, закажи столько, сколько съешь." 
    mother "{cps=40}Можешь даже чуть больше, заберем домой и оставим на ужин."
    hide sad sabby
    show sabby:
        xalign 0.2 yalign 1.0
    sabby "{cps=40}Хорошо."

    sabby "{cps=40}Тогда я буду роллы с креветкой."
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

    sabby "{cps=40}Тогда я буду лимонад и роллы с креветкой."
    father "{cps=40}Мне пиво и калифорнию, а жене лимонад и филадельфию."
    jump prodoljenie3
    return


    label home:
    hide happy_father
    show father:
        xalign 0.99 yalign -0.1
    sabby "{cps=40}Может, все-таки домой?"
    mother "{cps=40}Не забывай, мы празднуем твой день рождения, закажи столько, сколько съешь." 
    mother "{cps=40}Можешь даже чуть больше, заберем домой и оставим на ужин."
    hide sad sabby
    show sabby:
        xalign 0.2 yalign 1.0
    sabby "{cps=40}Хорошо."

    sabby "{cps=40}Тогда я буду лимонад, роллы с креветкой и один онигири с сёмгой."
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
nastya "{cps=40}Хорошо, ожидание заказа до 20 минут."
hide cafe_nastya
text "{cps=40}Семья просидела около часа в ресторане и наслаждалась как видом из окна, прекрасным звуковым сопровождением, так и замечательно приготовленной едой, которую они не так уж и часто ели."
show father:
    xalign 0.99 yalign -0.1
father "{cps=40}Ну всё, поели, попили, можем ехать домой."
father "{cps=40}А то Сэбби заскучала, смотрит уже минут десять в одну точку и ничего не говорит."
father "{cps=40}Подъем!"
show mother:
    xalign 0.1 yalign 1.8
stop music fadeout 5
mother "{cps=40}Сэбби, вставай..."
hide father
show angry_father:
    xalign 0.99 yalign -0.1
hide mother

show serious_mother:
    xalign 0.1 yalign -2.0
father "{cps=40}Хватит придуриваться!"
scene restaurant1
play music obmorokmusic volume 0.5
show angry_father:
    xalign 0.99 yalign -0.1
hide mother
show serious_mother:
    xalign 0.1 yalign -2.0
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
scene restaurant1
with fade
mother "{cps=40}Все будет хорошо!"
scene restaurant1
with fade
mother "{cps=40}Ты слышишь?"
scene restaurant1
with fade
mother "{cps=40}Только не беспокойся, сейчас приедут доктора!!!"
stop music fadeout 4
scene restaurant1
with fade
text "..."
play music allmusic volume 0.5
scene osnova
with fade
text "Конец второй главы."
scene osnova
with fade
text "Глава третья."
scene palata
with fade
play sound palatamusic volume 0.2
show father:
    xalign 0.1 yalign -0.1
show sad_mother:
    xalign 0.3 yalign -2.0
show doctor:
  xalign 0.9 yalign -0.2
doctor "{cps=40}Девочка сейчас находится в сложном состоянии, ее организму приходится нелегко." 
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
stop sound
stop music fadeout 2
scene astral
with fade
play music monstermusic volume 0.5
text "{cps=40}Сэбби не понимала кто она, где находится и что вообще нужно сделать, чтобы вернуться к своей обычной жизни."
text "{cps=40}Но тут что-то непонятное подало голос, если бы в этом страшном месте не было бы тишины, то Сэбби и не услышала ничего, но сейчас она отчетливо понимала, что с ней говорят."
scene astral
with fade
play sound govormonstramusic volume 0.2
ktoto "{cps=40}Сэбби..."
ktoto "{cps=40}Ты меня все-таки смогла увидеть, значит я знаю как забрать тебя."
ktoto "{cps=40}Я доберусь до тебя!"
ktoto "{cps=40}Ты слышишь?"
ktoto "{cps=40}Я заберу тебя с собой!"
stop sound
scene astral
with fade
text "{cps=40}После этих слов последовало тяжелое дыхание, оно отчетливо чувствовалось над ухом, хотелось просто закрыть уши и надеяться, что это скоро все закончится, но голос снова начал произносить свои трепещущие душу возгласы."
scene astral
with fade
play sound govormonstramusic volume 0.2
ktoto "{cps=40}Я доберусь до тебя!"
ktoto "{cps=40}Ты слышишь?"
ktoto "{cps=40}Я заберу тебя с собой!"
stop sound
jump start1


label simongame (difficulty=0, endgame=0,goquick=0):

    $ sequence=[] #последовательность ответа.
    $ nowpush=0#последовательности итератор
    $ thecolor=0#кнопку Вы должны нажать.

label turnsequence: #теперь вызовем рандомизатор, чтобы добавить знаки.
    python:
        for i in range (0,difficulty):
            added=renpy.random.randint(0,3)
            sequence.append(added)
    $nowpush=0

label showthesequence: #теперь показывают на экране, которые отображают последовательность
    if nowpush==len(sequence):
        jump theguessin#отскочить, если последовательность завершена
    show screen voidgame
    $ renpy.pause(0.5,hard=True)
    show screen displaysequence
    hide screen voidgame
    $ renpy.pause(0.5,hard=True)
    if nowpush< len(sequence):
        $ nowpush+=1
    jump showthesequence

label theguessin:#этот ярлык подготовить экран, скрывая то, что осталось от предыдущих
    $ nowpush=0
    hide screen displaysequence
  #Теперь вызовем на экране ввода данных
    $ nowpush=0
label guessthesequence: #сейчас ввод команд игрока, чтобы повторить последовательность
    if nowpush==len(sequence):
        jump turnsequence #если завершить, повторить сначала
    call screen inputcolor
    $ myguess=_return #вот нажатой кнопки
    $ theright =sequence[nowpush]#правильный кнопку, которую нужно нажать в данный момент
    if theright==myguess:
        $nowpush+=1
        if nowpush==(endgame):
            jump winner
        jump guessthesequence
    if theright!=myguess:
        jump looser
label winner:#в messagge для определения победы
    jump prodeljenie_scene1
    return
label looser: #сообщение
    jump start1

    return


screen displaysequence:
    grid 2 2:
        xalign 0.5
        yalign 0.5
        spacing 5
        if sequence[nowpush]==0:
            add "redon.png"
        else:
            add "buttonoff.png"
        if sequence[nowpush]==1:
            add "blueon.png"
        else:
            add "buttonoff.png"
        if sequence[nowpush]==2:
            add "greenon.png"
        else:
            add "buttonoff.png"
        if sequence[nowpush]==3:
            add "yellowon.png"
        else:
            add "buttonoff.png"
screen voidgame:
    grid 2 2:
        xalign 0.5
        yalign 0.5
        spacing 5
        add "buttonoff.png"
        add "buttonoff.png"
        add "buttonoff.png"
        add "buttonoff.png"

screen inputcolor:
    use racetheclock(goquick) #this is a moving bar, so techie!
    text "Ваша очередь" xalign 0.5 yalign 0.9
    grid 2 2:
        xalign 0.5
        yalign 0.5
        spacing 5
        imagebutton idle "buttonoff.png" hover "redon.png" action Return(0)
        imagebutton idle "buttonoff.png" hover "blueon.png" action Return(1)
        imagebutton idle "buttonoff.png" hover "greenon.png" action Return(2)
        imagebutton idle "buttonoff.png" hover "yellowon.png" action Return(3)


screen racetheclock(goquick):
    $ mytime=AnimatedValue(value=10.0, range=10.0, delay=goquick, old_value=0.0)
    bar value mytime xalign 0.5 yalign 0.1 xsize 500
    timer goquick action Jump("too_slow")

label too_slow:
    "Время вышло!"
    jump start1
    return




# Игра начинается здесь.
label start1:
    "Соберите воспоминания Сэбби, повторяя комбинации картинок, чтобы помочь выбраться Сэбби из сна."
    call simongame pass (difficulty=1,endgame=4,goquick=5) from _call_simongame
    return

label prodeljenie_scene1:
    scene astral
    with fade
    stop music fadeout 3
    text "..."
    scene palata
    with fade
    play music allmusic volume 0.5
    play sound palatamusic volume 0.2
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
stop sound
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
stop music fadeout 1
play sound govormonstramusic volume 2.0
text "..."
show very_sad_sabby:
    xalign 0.1 yalign 2.9
sabby "{cps=40}АААААААААА"
show angry_father:
    xalign 0.99 yalign -0.1
stop sound fadeout 1
play music allmusic volume 0.5
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
        $ bad_end += 1
        jump menu1
    "Его силуэт непонятный":
        $ happy_end += 1
        jump menu1
return

label menu1:
#menu
menu:
    psih "Понятно. Давай попробуем описать его."

    "Руки тянулись ко мне":
        $ bad_end += 1
        jump menu2
    "Он бежал за мной":
        $ happy_end += 1
        jump menu2
return

label menu2:
#menu
menu:
    psih "Понятно. Давай попробуем описать его."

    "Голос казался таким знакомым":
        $ happy_end += 1
        jump papa_monster
    "Глаза залиты кровью":
        $ bad_end += 1
        jump monster
return


label papa_monster:
$ renpy.notify("Ваши ответы повлияли на развитие событий")
psih "{cps=40}Надо объеденить все эти характеристики и получить картинку."
jump start2

#РАБОТА МАТВЕЯ!!! здесь нужно сделать игру-змейку
init python:

    # НАСТРОЙКИ ИГРЫ ПО УМОЛЧАНИЮ:

    # набор типов карточек по умолчанию
    all_cards = ['A', 'B', 'C']
    # ширина и высота поля
    ww = 3
    hh = 3
    # сколько карточек можно открыть за 1 ход
    max_c = 2
    # размер текста в карточке для текстового режима
    card_size = 48
    # время, выделенное на прохождение
    max_time = 25
    # пауза перед тем, как карточки исчезнут
    wait = 0.5
    # режим карточек с изображениями, а не с иекстом
    img_mode = True

    values_list = []
    temp = []
    # объявляем картинки-карточки
    # должны быть в формате "images/card_*.png"
    # обязательны "card_back.png" и "card_empty.png"
    for fn in renpy.list_files():
        if fn.startswith("images/card_") and fn.endswith((".png")):
            name = fn[12:-4]
            renpy.image("card " + name, fn)
            if name != "empty" and name != "back":
                temp.append(str(name))
    # если картинок найдено > 1,
    # то меняем набор типов карточек, но имена файлов
    if len(temp) > 1:
        all_cards = temp
    else:
        # иначе включаем текстовый режим,
        # так как картинок очень мало
        img_mode = False

    # функция инициализации игрового поля
    def cards_init():
        global values_list
        values_list = []
        while len(values_list) + max_c <= ww * hh:
            current_card = renpy.random.choice(all_cards)
            for i in range(0, max_c):
                values_list.append(current_card)
        renpy.random.shuffle(values_list)
        while len(values_list) < ww * hh:
            values_list.append('empty')

# экран игры
screen memo_scr:
    # таймер
    timer 1.0 action If (memo_timer > 1, SetVariable("memo_timer", memo_timer - 1), Jump("memo_game_lose") ) repeat True
    # поле
    grid ww hh:
        align (.5, .5) # в центре
        for card in cards_list:
            button:
                left_padding 0
                right_padding 0
                top_padding 0
                bottom_padding 0
                background None
                if card["c_value"] == 'empty':
                    if img_mode:
                        add "card empty"
                    else:
                        text " " size card_size
                else:
                    if card["c_chosen"]:
                        if img_mode:
                            add "card " + card["c_value"]
                        else:
                            text card["c_value"] size card_size
                    else:
                        if img_mode:
                            add "card back"
                        else:
                            text "#" size card_size
                # нажатие на кнопку-карточку
                action If ( (card["c_chosen"] or not can_click), None, [SetDict(cards_list[card["c_number"]], "c_chosen", True), Return(card["c_number"]) ] )
    text str(memo_timer) xalign .5 yalign 0.0 size card_size

# сама игра
label memoria_game:
    $ cards_init()
    $ cards_list = []
    python:
        for i in range (0, len(values_list) ):
            if values_list[i] == 'empty':
                cards_list.append ( {"c_number":i, "c_value": values_list[i], "c_chosen":True} )
            else:
                cards_list.append ( {"c_number":i, "c_value": values_list[i], "c_chosen":False} )
    $ memo_timer = max_time
    # показать экран с игрой
    show screen memo_scr
    # основной цикл игры
    label memo_game_loop:
        $ can_click = True
        $ turned_cards_numbers = []
        $ turned_cards_values = []
        $ turns_left = max_c
        label turns_loop:
            if turns_left > 0:
                $ result = ui.interact()
                $ memo_timer = memo_timer
                $ turned_cards_numbers.append (cards_list[result]["c_number"])
                $ turned_cards_values.append (cards_list[result]["c_value"])
                $ turns_left -= 1
                jump turns_loop
        # предотвращаем открытие лишних карточек
        $ can_click = False
        if turned_cards_values.count(turned_cards_values[0]) != len(turned_cards_values):
            $ renpy.pause (wait, hard = True)
            python:
                for i in range (0, len(turned_cards_numbers) ):
                    cards_list[turned_cards_numbers[i]]["c_chosen"] = False
        else:
            $ renpy.pause (wait, hard = True)
            python:
                for i in range (0, len(turned_cards_numbers) ):
                    cards_list[turned_cards_numbers[i]]["c_value"] = 'empty'
                for j in cards_list:
                    if j["c_chosen"] == False:
                        renpy.jump ("memo_game_loop")
                renpy.jump ("memo_game_win")
        jump memo_game_loop

# проигрыш
label memo_game_lose:
    hide screen memo_scr
    $ renpy.pause (0.1, hard = True)
    jump memoria_game

# выигрыш
label memo_game_win:
    hide screen memo_scr
    $ renpy.pause (0.1, hard = True)
    jump prodoljenie_scene2
    return


label start2:
    scene psihroom
    $ max_time = 40
    $ ww, hh = 4, 4
    call memoria_game from _call_memoria_game
    return

label prodoljenie_scene2:
    scene psihroom
    show psih:
        xalign 0.95 yalign -6.5
    show sad sabby:
        xalign 0.1 yalign 2.9
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
    stop music fadeout 4
    text "{cps=40}Сэбби продолжает ходить к психологу, мама вышла на двойную ставку, чтобы обеспечить семью. Но для них это был лучший вариант."
    play music mainmenumusic volume 0.5
    window hide
    scene osnova
    n '''Спасибо за прохождение нашей первой игры!

    Над ней работали Капустяшки:

    - Сидельникова Анастасия

    - Капустян Ева

    - Емельянов Матвей

    - Дашацыренов Лев'''
    stop music fadeout 1

    $ persistent.ending1 = True
    return

label monster:
$ renpy.notify("Ваши ответы повлияли на развитие событий")
psih "{cps=40}Надо объеденить все эти характеристики и получить картинку."
jump start3
#РАБОТА МАТВЕЯ!!! здесь нужно сделать игру-змейку
init python:

    # НАСТРОЙКИ ИГРЫ ПО УМОЛЧАНИЮ:

    # набор типов карточек по умолчанию
    all_cards = ['A', 'B', 'C']
    # ширина и высота поля
    ww = 3
    hh = 3
    # сколько карточек можно открыть за 1 ход
    max_c = 2
    # размер текста в карточке для текстового режима
    card_size = 48
    # время, выделенное на прохождение
    max_time = 25
    # пауза перед тем, как карточки исчезнут
    wait = 0.5
    # режим карточек с изображениями, а не с иекстом
    img_mode = True

    values_list = []
    temp = []
    # объявляем картинки-карточки
    # должны быть в формате "images/card_*.png"
    # обязательны "card_back.png" и "card_empty.png"
    for fn in renpy.list_files():
        if fn.startswith("images/card_") and fn.endswith((".png")):
            name = fn[12:-4]
            renpy.image("card " + name, fn)
            if name != "empty" and name != "back":
                temp.append(str(name))
    # если картинок найдено > 1,
    # то меняем набор типов карточек, но имена файлов
    if len(temp) > 1:
        all_cards = temp
    else:
        # иначе включаем текстовый режим,
        # так как картинок очень мало
        img_mode = False

    # функция инициализации игрового поля
    def cards_init():
        global values_list
        values_list = []
        while len(values_list) + max_c <= ww * hh:
            current_card = renpy.random.choice(all_cards)
            for i in range(0, max_c):
                values_list.append(current_card)
        renpy.random.shuffle(values_list)
        while len(values_list) < ww * hh:
            values_list.append('empty')

# экран игры
screen memo_scr:
    # таймер
    timer 1.0 action If (memo_timer > 1, SetVariable("memo_timer", memo_timer - 1), Jump("memo_game_lose") ) repeat True
    # поле
    grid ww hh:
        align (.5, .5) # в центре
        for card in cards_list:
            button:
                left_padding 0
                right_padding 0
                top_padding 0
                bottom_padding 0
                background None
                if card["c_value"] == 'empty':
                    if img_mode:
                        add "card empty"
                    else:
                        text " " size card_size
                else:
                    if card["c_chosen"]:
                        if img_mode:
                            add "card " + card["c_value"]
                        else:
                            text card["c_value"] size card_size
                    else:
                        if img_mode:
                            add "card back"
                        else:
                            text "#" size card_size
                # нажатие на кнопку-карточку
                action If ( (card["c_chosen"] or not can_click), None, [SetDict(cards_list[card["c_number"]], "c_chosen", True), Return(card["c_number"]) ] )
    text str(memo_timer) xalign .5 yalign 0.0 size card_size

# сама игра
label memoria_game1:
    $ cards_init()
    $ cards_list = []
    python:
        for i in range (0, len(values_list) ):
            if values_list[i] == 'empty':
                cards_list.append ( {"c_number":i, "c_value": values_list[i], "c_chosen":True} )
            else:
                cards_list.append ( {"c_number":i, "c_value": values_list[i], "c_chosen":False} )
    $ memo_timer = max_time
    # показать экран с игрой
    show screen memo_scr
    # основной цикл игры
    label memo_game_loop1:
        $ can_click = True
        $ turned_cards_numbers = []
        $ turned_cards_values = []
        $ turns_left = max_c
        label turns_loop1:
            if turns_left > 0:
                $ result = ui.interact()
                $ memo_timer = memo_timer
                $ turned_cards_numbers.append (cards_list[result]["c_number"])
                $ turned_cards_values.append (cards_list[result]["c_value"])
                $ turns_left -= 1
                jump turns_loop1
        # предотвращаем открытие лишних карточек
        $ can_click = False
        if turned_cards_values.count(turned_cards_values[0]) != len(turned_cards_values):
            $ renpy.pause (wait, hard = True)
            python:
                for i in range (0, len(turned_cards_numbers) ):
                    cards_list[turned_cards_numbers[i]]["c_chosen"] = False
        else:
            $ renpy.pause (wait, hard = True)
            python:
                for i in range (0, len(turned_cards_numbers) ):
                    cards_list[turned_cards_numbers[i]]["c_value"] = 'empty'
                for j in cards_list:
                    if j["c_chosen"] == False:
                        renpy.jump ("memo_game_loop1")
                renpy.jump ("memo_game_win1")
        jump memo_game_loop1

# проигрыш
label memo_game_lose1:
    hide screen memo_scr
    $ renpy.pause (0.1, hard = True)
    jump memoria_game1

# выигрыш
label memo_game_win1:
    hide screen memo_scr
    $ renpy.pause (0.1, hard = True)
    jump prodoljenie_scene3
    return


label start3:
    scene psihroom
    $ max_time = 40
    $ ww, hh = 4, 4
    call memoria_game1 from _call_memoria_game1

    return


label prodoljenie_scene3:
    scene psihroom
    show psih:
        xalign 0.95 yalign -6.5
    show sad sabby:
        xalign 0.1 yalign 2.9
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
    stop music fadeout 1.5
    scene black
    with fade
    play music obmorokmusic volume 0.5
    text "..."
    play sound skorayamusic volume 0.05
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
    stop sound fadeout 1
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
    hide mother
    show happy_father:
        xalign 0.3 yalign -0.1
    show mother:
        xalign 0.1 yalign 1.8
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
    stop music fadeout 1
    scene astral
    with fade
    play music monstermusic volume 0.5
    text "..."
    show sabby_vahue:
        xalign 0.8 yalign 1.3
    play sound govormonstramusic volume 0.2
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
    stop sound
    play sound govormonstramusic volume 5.0
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
    stop sound fadeout 1
    stop music fadeout 1
    window hide
    play music mainmenumusic volume 0.5
    scene osnova
    with fade
    n '''Спасибо за прохождение нашей первой игры!
    
    Над ней работали Капустяшки:
    
    - Сидельникова Анастасия
    
    - Капустян Ева
    
    - Емельянов Матвей
    
    - Дашацыренов Лев'''
    stop music fadeout 1
    $ persistent.ending1 = True
    return

else:
    stop sound fadeout 1
    stop music fadeout 1
    hide monster_nepon
    hide sabby_vahue
    scene hospital
    with fade
    text "..."
    play music allmusic volume 0.5
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
    stop music fadeout 1
    text "..."
    play music monstermusic volume 0.5
    scene astral
    with fade
    show sabby_vahue:
      xalign 0.8 yalign 1.3
    show monster:
       xalign 0.1 yalign -0.5
    sabby "{cps=40}Ты выдумка!"
    sabby "{cps=40}Тебя не существует!!!"
    play sound govormonstramusic volume 0.2
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

    menu:
        monster "Вопрос первый. Какой текстовый редактор используется по умолчанию в git?"

        "emacs":
            $ nepravotvet += 1
            jump menu01
        "vim":
            $ pravotvet += 1
            jump menu01
        "notepad":
            $ nepravotvet += 1
            jump menu01
    return
label menu01:
    menu:
        monster "Вопрос второй. Как удалить ветку night?"

        "git branch -d night":
            $ pravotvet += 1
            jump menu02
        "git delete night":
            $ nepravotvet += 1
            jump menu02
        "git checkout --delete night":
            $ nepravotvet += 1
            jump menu02
    return
label menu02:
    menu:
        monster "Вопрос третий. Сколько всего может быть веток в репозитории?"

        "Небольше двух":
            $ nepravotvet += 1
            jump menu03
        "Столько же, сколько участников в проекте":
            $ nepravotvet += 1
            jump menu03
        "Сколько угодно":
            $ pravotvet += 1
            jump menu03
    return
label menu03:
    menu:
        monster "Вопрос четвертый. Что делает команда git stash?"

        "Удаляет все измененные файлы":
            $ nepravotvet += 1
            jump menu04
        "Сохраняет все изменения в буфер":
            $ pravotvet += 1
            jump menu04
        "Отменяет все изменения":
            $ nepravotvet += 1
            jump menu04
    return
label menu04:
    menu:
        monster "Вопрос пятый. Какой командой можно загрузить с гитхаба репозиторий на свой компьютер?"

        "git pull":
            $ nepravotvet += 1
            jump menu05
        "git push":
            $ nepravotvet += 1
            jump menu05
        "git clone":
            $ pravotvet += 1
            jump menu05
    return
label menu05:
    menu:
        monster "Вопрос шестой. К какому типу систем контроля версий относится гит?"

        "Распределенная":
            $ pravotvet += 1
            jump proverkaotveta
        "Совместная":
            $ nepravotvet += 1
            jump proverkaotveta
        "Локальная":
            $ nepravotvet += 1
            jump proverkaotveta
    return
label proverkaotveta:
    if nepravotvet > pravotvet:
        stop sound
        play sound govormonstramusic volume 5.0
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
        stop sound fadeout 1
        stop music fadeout 1
        window hide
        play music mainmenumusic volume 0.5
        scene osnova
        with fade
        n '''Спасибо за прохождение нашей первой игры!
    
        Над ней работали Капустяшки:
    
        - Сидельникова Анастасия
    
        - Капустян Ева
    
        - Емельянов Матвей
    
        - Дашацыренов Лев'''
        stop music fadeout 1
        $ persistent.ending1 = True
        return

    else:
        hide monster
        show monster_nepon:
            xalign 0.1 yalign -0.5
        monster "{cps=40}Нет! Этого не может быть!"
        monster "{cps=40}Ты же девочка, откуда ты знаешь про гит?!"
        hide sad sabby
        show sabby:
            xalign 0.8 yalign 1.0
        sabby "{cps=40}Я просто ходила на семинары к Алексею Игоревичу и делала  практики"
        monster "{cps=40}Ну что ж, придется мне искать другую жертву....("
        stop sound fadeout 1
        stop music fadeout 1
        hide sabby
        hide monster_nepon
        scene osnova
        with fade
        play music allmusic volume 0.5
        text "{cps=40}Год спустя"
        play sound sunmusic volume 0.2
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
        stop sound fadeout 1
        stop music fadeout 1
        window hide
        play music mainmenumusic volume 0.5
        scene osnova
        with fade
        n '''Спасибо за прохождение нашей первой игры!
    
        Над ней работали Капустяшки:
    
        - Сидельникова Анастасия
    
        - Капустян Ева
    
        - Емельянов Матвей
    
        - Дашацыренов Лев'''
        stop music fadeout 1
        $ persistent.ending1 = True
        return










