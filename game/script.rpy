# Определение персонажей игры.
define sabby = Character('Сэбби')
define mother = Character('Мама')
define text = ('...')
define nastya = ('Настя')
define anya = ('Аня')
define annmother = ('Мария Богова')
define father = ('Папа')
define mother_and_father = ('Мама и Папа')

image room sabby = 'Back/roomsabby.jpg'
image sabby = 'Role/Sb.png'
image glavnoe = 'Back/osnova.jpg'
image padik = 'Back/padik.png'
image sad sabby = 'Role/sad sb.png'
image happy mother = 'Role/mother.png'
image street = 'Back/street.png'
image living room = 'Back/livingroom.jpg'
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
    text "Глава первая"
    #2 frame
    scene roomsabby
    with fade
    show happy mother:
        xalign 0.8 yalign 1.8
    mother "Доченька, пора просыпаться, папа уже уехал, а ты даже не пожелала ему удачного дня."
    #3 frame
    show sad sabby:
        xalign 0.1 yalign 3.4
    sabby "Да, мам, еще пять минут"
    #4 frame
    mother "Давай вставай, завтрак на столе, не забудь почистить зубы,а я побежала на работу, буду через 6 часов."
    #5 frame
    sabby "Да-да, встаю"
    #6 frame
    hide sad sabby
    hide happy mother
    text "..."
    #7 frame
    scene padik
    with fade
    show sabby
    sabby "Так, зубы почистила, завтрак съела, можно пойти гулять"
    #8 frame 
    show sabby:
        xalign 0.1
    nastya "Ой, Сэбби, привет, как ты уже подросла"
    #9 frame 
    sabby "Здравствуйте, Анастасия Павловна"
    #10 frame
    nastya "Да какая я тебе Анастасия Павловна, просто Настя, мне 16, а не 40"
    #11 frame *update
    sabby "Извините, я не хотела вас обидеть."
    sabby "Как вы себя чувствуете, как ваши родители?"
    #12 frame
    nastya "..."
    nastya "Ты неисправима."
    nastya "Родители нормально, папа ходит на химотерапию, вроде, легче становится, мама, выплачивая долги, потеряла себя, завела кучу проблем со здоровьем, теперь с ногами проблемы…"
    nastya "Мне пришлось устроиться официанткой неподалеку, чтобы обеспечить семью"
    nastya "Черт, прости..."
    #15 frame
    sabby "За что ты(вы)извиняешься?" #спросить стоит ли дальше гнуть палку о том чтобы называть настю на вы или нет
    #16 frame
    nastya "За то, что нагружаю тебя своими проблемами."
    nastya "Мне просто.."
    nastya "Просто некому выговориться, понимаешь?"
    sabby "Ага..."
    #18 frame
    nastya "Ладно."
    nastya "Ты, наверное, торопишься, с Аней ведь гулять идешь?"
    sabby "Ну, да"
    nastya "Тогда беги, не буду тебя задерживать, хорошей прогулки!"
    sabby "Спасибо!"
    #22 frame
    hide sabby
    nastya "Аня.."
    nastya "До сих пор никак не могу понять, как у таких самовлюбленных родителей могла родиться Аня"
    nastya "И почему при таком достатке они живут в таком районе, как наш?"
    #23 frame
    text "..."
    #24 frame
    scene street
    with fade
    anya "Сэбби!!! Привет!!!"
    show sabby:
        xalign 0.8 yalign 1.0
    sabby "Аня!!!"
    sabby "У тебя все хорошо?"
    
    #menu
    menu:
        anya "Еле убежала от мамы погулять с тобой, она, как всегда, заладила, что не нужно мне общаться с соседями."

        "Странная она.":
            jump strange
        "Пошли поиграем?":
            jump poigrat
    return


label strange:
    
    sabby "Странная она."
    anya "Да. Говорит всем постоянно, что она хозяйка дома."
    #menu
    menu:
        anya "Но при этом из домашних обязанностей и воспитания на ней лежит только пару раз в день прочитать мне лекцию о том, что надо быть красивой и общаться с детьми, чьи родители на том же уровне, что и мои. 
        Все остальное делают уборщицы и няня."

        "Что значит на том же уровне?":
            jump level
        "Пошли поиграем?":
            jump poigrat
    return


label poigrat:
    sabby "Понятно."
    sabby "Пошли поиграем?"
    anya "Да, давай, это поможет мне отвлечься."
    hide sabby
    with fade
    text "И действительно, у Ани получилось на время забыться. 
    Забыть все, что происходит с ней за пределами этой площадки, забыть все, что происходит у нее дома.
    Но это не может длиться вечно. Когда-то все равно приходится возвращаться туда, откуда стоит бежать."
    #35 frame
    show sad sabby:
        xalign 0.8 yalign 2.9
    annmother "АНЯ!"
    annmother "Ты опять с этой девчонкой?!"
    annmother "Сколько раз тебе нужно повторять, чтобы ты с ней 
    не общалась!"
    anya "Ой, мама все-таки нашла меня."
    anya "Надо бежать."
    sabby "Эх, ладно, пока.."
    anya "Пока!"
    anya "Я постараюсь завтра тоже выйти, поиграть."
    sabby "Хорошо, буду тебя ждать."
    hide sad sabby
    text "..."
    jump prodoljenie

    return



label level:
    sabby "А что для твоих родителей считается таким же уровнем, как у них?"
    anya "Ну…"
    anya "Я не знаю…"
    anya "Если честно, я ее слушаю краем уха, потому что чаще всего 
    мама отходит от темы и говорит о том, какая она прекрасная и как много для всех делает."
    jump poigrat
    return



label prodoljenie:
    #40 frame
    scene living room
    with fade
    show sabby:
        xalign 0.1 yalign 1.0
    sabby "Привет, мам, пап."
    show father:
        xalign 0.99 yalign -0.1
    show happy mother:
        xalign 0.7 yalign 1.5
    father "Привет."
    father "Ты с Аней гуляла?"
    hide sabby
    show sad sabby:
        xalign 0.1 yalign 2.9
    sabby "Да. Только вот ее мама быстро забрала домой."
    mother "Ну хоть немного смогли проветриться."
    mother "Давай иди кушай, пока еда не остыла и стоит идти ложиться спать."
    mother "Уже достаточно поздно, тебе стоит отдохнуть, завтра тебя ждет особый день, подготовься к нему хорошо, милая."
    sabby "Да, хорошо, мам."
    hide sad sabby
    hide happy mother
    hide father
    text "..."
    #47 frame
    scene glavnoe
    with fade
    text "Конец первой главы."
    #48 frame
    text "Глава вторая."
    #49 frame
    scene street1
    with fade
    text "Представьте себе какую-нибудь точку мира, которая находится ближе всего к экватору. Лето там очень теплое, солнечное."
    #50 frame
    scene street2
    with fade
    text "Так вот и в городке, где живет Сэбби сегодня настолько жарко, что все люди выходят на улицу, чтобы погреться на таком долгожданном солнце."
    #51 frame
    scene street
    with fade
    text "А в нашем дворе сегодня особенный день не только из-за теплой погоды..."
    #52 frame
    scene roomsabby
    with fade
    text "..."
    show happy_father:
        xalign 0.99 yalign -0.1
    show happy mother:
        xalign 0.7 yalign 1.5
    show cake:
        xalign 0.55 yalign 0.6
    mother_and_father "С днем рождения, Сэбби!!!"
    show sad sabby:
        xalign 0.1 yalign 2.9
    sabby "Мам, пап, зачем так рано…"
    mother "Потому что мы на девятилетие нашей любимой доченьки подготовили сюрприз! Загадывай желание, задувай свечи и начинай одеваться."
    sabby "Куда?"
    mother "Как это куда? Конечно, же в ресторан!"
    sabby "Но мы ни разу не были даже в кафе, это слишком дорого, может, не пойдем?"
    sabby "Покушаем дома тортик, выпьем чай…"
    mother "Это даже не обсуждается."
    mother "Мы любим тебя радовать, пусть зачастую и мелочами. А сегодня такой день!"
    hide sad sabby
    show sabby:
        xalign 0.1 yalign 1.0
    mother "Ты же так хотела попробовать роллы, так что мы сейчас собираемся и едем осуществлять твою маленькую хотелку."
    mother "Да, папа?"
    hide happy_father
    show father:
        xalign 0.99 yalign -0.1
    
    #menu
    menu:
        father "Да."

        "Может, все-таки дома посидим?":
            jump maybe
        "Ура!!!":
            jump yes
        "Но я не хочу...":
            jump no
    return


label maybe:
    hide father
    show happy_father:
        xalign 0.99 yalign -0.1
    hide sabby
    show sad sabby:
        xalign 0.1 yalign 2.9
    sabby "Может, все-таки дома посидим?"
    mother "Не переживай, солнышко, всё будет хорошо"
    hide father
    hide sad sabby
    hide happy mother
    hide cake
    hide happy_father
    scene street
    with fade
    text "Все начали собираться, мама красилась, Вика подражала ей, а папа пытался подобрать подходящий галстук."
    scene living room
    with fade
    show happy_father:
        xalign 0.99 yalign -0.1
    show sad sabby:
        xalign 0.1 yalign 2.9
    show happy mother:
        xalign 0.8 yalign 1.8
    mother "Так, ну вроде все готовы, можем ехать!"
    hide happy mother
    hide sad sabby
    hide happy_father
    text "..."
    jump prodoljenie2
    return


label yes:
    hide father
    show happy_father:
        xalign 0.99 yalign -0.1
    sabby "Ура!!!"
    hide happy_father
    hide sabby
    hide happy mother
    hide cake
    scene street
    with fade
    text "Все начали собираться, мама красилась, Вика подражала ей, а папа пытался подобрать подходящий галстук."
    scene living room
    with fade
    show happy_father:
        xalign 0.99 yalign -0.1
    show sabby:
        xalign 0.1 yalign 1.0
    show mother:
        xalign 0.8 yalign 1.8
    mother "Так, ну вроде все готовы, можем ехать!"
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
        xalign 0.55 yalign 0.6
    show sad sabby:
        xalign 0.1 yalign 2.9
    sabby "Но я не хочу..."
    text "..."
    hide angry_father
    show father:
        xalign 0.99 yalign -0.1
    father "Это не обсуждается."
    father "Мы уже забронировали столик и внесли депозит, ты понимаешь, что часть денег уже заплачена?"
    hide father
    hide sad sabby
    hide serious_mother
    hide cake
    scene street
    with fade
    text "Все начали собираться, мама красилась, Вика подражала ей, а папа пытался подобрать подходящий галстук."
    scene living room
    with fade
    show happy_father:
        xalign 0.99 yalign -0.1
    show sabby:
        xalign 0.1 yalign 1.0
    show mother:
        xalign 0.8 yalign 1.8
    mother "Так, ну вроде все готовы, можем ехать!"
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
    #show nastya at right
    nastya "Здравствуйте! "
    nastya "Сегодня я буду вашим официантом."
    nastya "Вика, поздравляю тебя с днем рождения! Счастья, здоровья и всего самого наилучшего!"
    return





