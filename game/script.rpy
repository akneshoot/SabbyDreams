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
define n = Character(None, kind=nvl)


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
        xalign 0.85 yalign 0.7
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
    nastya "Сэбби, поздравляю тебя с днем рождения! Счастья, здоровья и всего самого наилучшего!"
    sabby "Здравствуйте, спасибо большое"
    mother "За какой столик мы можем присесть?"
    nastya "Специально для вас я заняла столик у окна, чтобы вы могли есть и смотреть на центральную площадь города."
    nastya "Прошу, присаживайтесь, вот меню"

    #РАБОТА МАТВЕЯ!!!сюда надо как-то впихнуть меню с едой. (сделать код так чтобы было написано не именно выбрать блюдо, а просто что сэбби приглянулось блюдо, которое пользователь тыкнет)

    hide happy_father
    hide happy mother
    text "У сэбби разбегались глаза, все выглядело так заманчиво, но когда она кинула свой взгляд на цены, перехотелось есть вовсе."
    show happy_father:
        xalign 0.99 yalign -0.1
    show happy mother:
        xalign 0.8 yalign 1.8
    hide sabby
    show sad sabby:
        xalign 0.1 yalign 2.9
    

    #menu
    menu:
        sabby "Как тут дорого!"

        "Пожалуй, закажу только одно блюдо":
            jump one
        "Хочу попробовать всё!":
            jump all
        "Может, все-таки домой?":
            jump home
    return

    
    label one:
    hide happy_father
    show father:
        xalign 0.99 yalign -0.1
    sabby "Пожалуй, закажу только одно блюдо"
    mother "Не забывай, мы празднуем твой день рождения, закажи столько, сколько съешь." 
    mother "Можешь даже чуть больше, заберем домой и оставим на ужин"
    hide sad sabby
    show sabby:
        xalign 0.2 yalign 1.0
    sabby "Хорошо"

    #РАБОТА МАТВЕЯ!!! здесь, если получится, когда пользователь выберет что будет в итоге кушать сэбби будет выводиться текст в зависимости от того что выбрали.

    sabby "Тогда я буду лимонад, роллы с креветкой и один онигири с сёмгой"
    father "Мне пиво и калифорнию, а жене лимонад и филадельфию."
    jump prodoljenie3
    return

    label all:
    hide happy_father
    hide sad sabby
    show sabby:
        xalign 0.2 yalign 1.0
    show angry_father:
        xalign 0.99 yalign -0.1
    sabby "Хочу попробовать всё!"
    father "Не забывай о финансах. Заказывай столько, сколько сможешь съесть."
    hide sabby
    show sad sabby:
        xalign 0.1 yalign 2.9
    sabby "Хорошо"

    #РАБОТА МАТВЕЯ!!! здесь, если получится, когда пользователь выберет что будет в итоге кушать сэбби будет выводиться текст в зависимости от того что выбрали.

    sabby "Тогда я буду лимонад, роллы с креветкой и один онигири с сёмгой"
    father "Мне пиво и калифорнию, а жене лимонад и филадельфию."
    jump prodoljenie3
    return


    label home:
    hide happy_father
    show father:
        xalign 0.99 yalign -0.1
    sabby "Может, все-таки домой?"
    mother "Не забывай, мы празднуем твой день рождения, закажи столько, сколько съешь." 
    mother "Можешь даже чуть больше, заберем домой и оставим на ужин"
    hide sad sabby
    show sabby:
        xalign 0.2 yalign 1.0
    sabby "Хорошо"

    #РАБОТА МАТВЕЯ!!! здесь, если получится, когда пользователь выберет что будет в итоге кушать сэбби будет выводиться текст в зависимости от того что выбрали.

    sabby "Тогда я буду лимонад, роллы с креветкой и один онигири с сёмгой"
    father "Мне пиво и калифорнию, а жене лимонад и филадельфию."
    jump prodoljenie3
    return


label prodoljenie3:
hide father
hide angry_father
hide happy mother
hide sabby
hide sad sabby
nastya "Хорошо, ожидание заказа до 20 минут"
text "Семья просидела около часа в ресторане и наслаждалась как видом из окна, прекрасным звуковым сопровождением, так и замеатльно приготовленной едой, которую они не так уж и часто ели."
show father:
    xalign 0.99 yalign -0.1
father "Ну всё, поели, попили, можем ехать домой"
father "А то Сэбби заскучала, смотрит уже минут десять в одну точку и ничего не говорит."
father "Подъем!"
show mother:
    xalign 0.1 yalign 1.8
mother "Сэбби, вставай..."
hide father
show angry_father:
    xalign 0.99 yalign -0.1
hide mother
show serious_mother:
    xalign 0.1 yalign -2.0
father "Хватит придуриваться!"
mother "Сэбби?.."
mother "Сэбби!"
hide angry_father
hide serious_mother
show sad_mother:
    xalign 0.1 yalign -2.0
mother "Она вся трясется!"
mother "У нее пена изо рта!"
mother "Вызовите скорую!"
hide sad_mother
mother "Все будет хорошо!"
mother "Ты слышишь?"
mother "Только не беспокойся, сейчас приедут доктора!!!"
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
doctor "Девочка сейчас находится в сложном стостоянии, ее организму приходится нелегко." 
doctor "Она не умрет, но шансы, что после реабилитации она будет ездить на инвалидной коляске, велики."
doctor "Будьте к этому готовы."
hide sad_mother
show sad_mother:
    xalign 0.8 yalign -2.0
mother "Неужели все так плохо..."
mother "Сэбби, дорогая, просыпайся скорее, ты нам очень нужна..."
mother "Мы любим тебя!"
father "Если на реабилитацию у нас нашлись деньги, учитывая, что ближайший месяц нам придется во многом себе отказывать"
father "То на новые ноги у нас нет средств."
mother "Моя милая доченька, как я могу тебе помочь?!"
father "Что-нибудь придумаем."
father "Она сильная, да и мы справимся."
father "Должны справиться."
hide sad_mother
hide father
text "Пока родители убивались в своем горе, никто не знал что могло происходить по ту сторону больничной палаты."
text "Шли дни, Сэбби так и оставалась в коме. Помимо ее физически плохого состояния, ей было тяжело морально."
text "Вы, вероятно, слышали где-то предположения и о том, что люди, выпадая из реальности, попадают в астрал и видят загробный мир, или же находятся на пути к нему?" 
scene astral
with fade
text "Сэбби не понимала кто она, где находится и что вообще нужно сделать, чтобы вернуться к своей обычной жизни."
text "Но тут что-то непонятное подало голос, если бы в этом страшном месте не было бы тишины, то Сэбби и не услышала ничего, но сейчас она отчетливо понимала, что с ней говорят."
scene astral
with fade
ktoto "Сэбби..."
ktoto "Ты меня все-таки смогла увидеть, значит я знаю как забрать тебя"
ktoto "Я доберусь до тебя!"
ktoto "Ты слышишь?"
ktoto "Я заберу тебя с собой!"
scene astral
with fade
text "После этих слов последовало тяжелое дыхание, оно отчетливо чувствовалось над ухом, хотелось просто закрыть уши и надеяться, что это скоро все закончится, но голос снова начал произносить свои трепещущие душу возгласы."
scene astral
with fade
ktoto "Я доберусь до тебя!"
ktoto "Ты слышишь?"
ktoto "Я заберу тебя с собой!"

#РАБОТА МАТВЕЯ!!! здесь нужно будет сделать лабиринт (типо сэбби убегает от монстра и находит выход в свой мир)


scene astral
with fade
text "..."
scene palata
with fade
show sad sabby:
    xalign 0.1 yalign 2.9
sabby "Где я?"
show sad_mother:
    xalign 0.8 yalign -2.0
mother "Дорогая, наконец-то ты очнулась! "
mother "Боже мой...."
mother "Эти недели были невыносимыми, я каждый день приходила к тебе и молилась за тебя!"
sabby "Что произошло?"
mother "Врачи так и не смогли понять что это было, но во время празднования твоего дня рождения ты просто смотрела в одну точку, а потом..."
mother "Как я рада, что ты очнулась!"
hide sad sabby
show very_sad_sabby:
    xalign 0.1 yalign 2.9
sabby "Мне снилось очень многое..."
sabby "Оно говорило со мной, оно хочет забрать меня!"
hide sad_mother
show serious_mother:
    xalign 0.8 yalign -2.0
mother "Что за оно?.."
sabby "Я не смогла его разглядеть, но оно кричало очень страшные вещи."
sabby "Нет..."
sabby "Оно заберет меня, мама!"
sabby "Оно найдет меня и заберет с собой!"
sabby "Я не хочу, мама!"

#menu
menu:
    mother "Не беспокойся, дорогая, никто тебя не тронет. Страшный сон закончился, теперь мы вместе, не переживай."

    "Но оно сказало, что заберет меня!":
        jump zaberet
    "Я хочу домой":
        jump want_home
    "А где папа?":
        jump where_father
return


label zaberet:
sabby "Но оно сказало, что заберет меня!"
mother "Хватит. Это просто сон!"
hide very_sad_sabby
show sad sabby:
    xalign 0.1 yalign 2.9
jump prodoljenie4
return

label want_home:
hide very_sad_sabby
show sad sabby:
    xalign 0.1 yalign 2.9
sabby "Я хочу домой"
jump prodoljenie4
return

label where_father:
hide very_sad_sabby
show sad sabby:
    xalign 0.1 yalign 2.9
sabby "А где папа?"
mother "Папа на работе, он сказал, что его срочно вызвали."
jump prodoljenie4
return

label prodoljenie4:
mother "Сейчас придет доктор и выпишет тебя, я пока пойду подышу на свежем воздухе, а то столько всего произошло."
hide serious_mother
doctor "Ну что, как ты себя чувствуешь?"
doctor "Все в порядке?"
sabby "Да, но мне снился очень жуткий сон!"
hide sad sabby
show very_sad_sabby:
    xalign 0.1 yalign 2.9
sabby "Оно придет за мной, я знаю!"
sabby "Мама мне не верит..."
sabby "Помогите!!!!"
doctor "Все в порядке, сны часто снятся."
sabby "Но это был необычный сон!"
doctor "Так, ладно."
doctor "Вижу, твое физическое состояние в порядке, позови маму, пожалуйста."
doctor "Подожди ее, пожалуйста, в коридоре."
hide very_sad_sabby
show sad sabby:
    xalign 0.1 yalign 2.9
sabby "Хорошо..."
hide sad sabby
show serious_mother:
    xalign 0.1 yalign -2.0
mother "Вы звали?"
doctor "Да, физическое состояние вашей дочери в порядке на удивление, но вот ее реакция на сон кажется мне странной"
doctor "Советую вам обратиться к специалисту."
mother "К специалисту?"
doctor "Да, думаю, ей нужен психолог после перенесенного стресса"
mother "Ох, мы никогда к психологам не обращались, но если это действительно ей поможет..."
mother "Хорошо."
mother "Мы запишемся на прием к психологу."
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
sabby "АААААААААА"
show angry_father:
    xalign 0.99 yalign -0.1
father "Да что опять стряслось?!"
father "Ты кричишь каждую ночь с тех пор, как вернулась из больницы!"
sabby "Оно заберет меня!"
sabby "Я не могу, мне страшно!"
sabby "Каждую ночь оно повторяет одно и то же!"
sabby "Оно меня убьет!"
father "Мне это надоело."
father "Света! Иди сюда!"
show serious_mother:
    xalign 0.8 yalign -2.0
mother "Что произошло?"
father "Она опять кричала во сне, разберись с этим!!!"
father "А я пошел спать, мне завтра рано вставать, мне некогда разбираться с ее дурацкими снами!"
hide angry_father
mother "Опять оно снилось?"
sabby "Да..."
mother "Ясно."
mother "Утром я позвоню психологу, он тебе поможет"
hide serious_mother
show mother:
    xalign 0.8 yalign 1.8
mother "А пока пошли попьем чай"
hide very_sad_sabby
show sad sabby:
    xalign 0.1 yalign 2.9
mother "Все равно уже проснулись..."
hide sad sabby
hide mother
scene osnova
with fade
text "Они пили чай, разговаривали, точнее мама Сэбби пыталась завести разговор, но каждая тема заходила в тупик. Девочка не могла до сих пор до конца отойти от тревоги и осознания, что все это не просто так и это очень сильно все походит на реальность."
text "Никто толком и не смог уснуть, кроме отца. Мама и Сэбби решили отвлечься с помощью просмотра любимой теле-передачи, на мгновение девушки забылись и время прошло до невозможности быстро. Пришло время выяснить причину кошмаров и покончить с ними."
scene psihroom
with fade
show psih:
   xalign 0.8 yalign -0.2
show serious_mother:
    xalign 0.1 yalign -2.0
show sad sabby:
    xalign 0.3 yalign 2.9
psih "Здравствуйте."
psih "Рассказывайте, что вас привело ко мне?"
mother "Мою дочь беспокоят кошмары с тех пор как она упала в обморок на свой день рождение."
mother "Это было три недели назад."
psih "Поняла."
psih "Не могли бы Вы выйти, я хочу пообщаться с Сэбби"
mother "Да, конечно."
mother "Доченька, я буду ждать тебя в коридоре"
psih "Ну что, рассказывай что с тобой"
hide serious_mother
hide sad sabby
hide psih
text "Сэбби рассказывает психологу обо всех кошмарах в ярчайших красках"
show psih:
   xalign 0.8 yalign -0.2
show sad sabby:
    xalign 0.1 yalign 2.9


#menu
menu:
    doctor "Понятно. Давай попробуем описать его."

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
    doctor "Понятно. Давай попробуем описать его."

    "Руки тянулись ко мне":
        jump menu2
    "Он бежал за мной":
        jump menu2
return

label menu2:
#menu
menu:
    doctor "Понятно. Давай попробуем описать его."

    "Голос казался таким знакомым":
        jump papa_monster
    "Глаза залиты кровью":
        jump monster
return


label papa_monster:
psih "Надо объеденить все эти характеристики и получить картинку."

#РАБОТА МАТВЕЯ!!! здесь нужно сделать игру-змейку

psih "Боже..."
psih "Мне так жаль, что ты видишь это каждую ночь..."
hide sad sabby
hide psih
show photo_papa at center:  
    yalign 0.4
text "*фото монстра, который доставал девочку в кошмарах*"
hide photo_papa
show psih:
   xalign 0.8 yalign -0.2
show sad sabby:
    xalign 0.1 yalign 2.9
psih "Мне нужно поговорить с твоей мамой, можешь позвать ее, пожалуйста, и подождать снаружи?"
sabby "Хорошо"
hide sad sabby
show serious_mother:
    xalign 0.1 yalign -2.0
mother "Что с ней?"
psih "Я пообщалась с Вашей дочерью и мы с ней кое-что нарисовали, посмотрите, пожалуйста"
mother "Это мой муж, я вижу, а что не так?"
psih "Сопоставляя ее рассказы о том как проживает ваша семья, о кошмарах и их точке отсчета, а также рисунок, у меня есть неутешительные выводы и я удивлена как ВЫ могли не заметить такое.."
psih "Ваш муж, отец Сэбби, насилует вашу дочь"
hide serious_mother
show sad_mother:
    xalign 0.1 yalign -2.0
mother "Но..."
mother "Как?!"
mother "Он клялся, что будет любить ее как родную, почему он так поступил?"
psih "Как родную?"
mother "Ее отец ушел как только узнал, что у нас будет ребенок, а этот..."
mother "Этот появился в моей жизни сразу после рождения Сэбби"
mother "Почему она мне не рассказывала об этом?!"
psih "У Вашего ребенка нестабильная психика, которая пытается защитить Сэбби, поэтому она забывает практически все негативные моменты, но подсознание не обманешь"
psih "Я обязана передать эту информацию в полицию"
mother "Да я сама напишу на него такое заявление!"
mother "Я зсасужу его!"
mother "Он не должен жить!"
hide sad_mother
hide psih
text "..."
scene osnova
with fade
text "Прошел месяц. Родители Сэбби развелись, был жуткий скандал. Отец оказался в тюрьме,а мама с дочерью пытаются продолжать жить обычной жизнью, что получается у них с трудностью."
text "Сэбби продолжает ходить к психологу, мама вышла на двойную ставку, чтобы обеспечить семью. Но для них это был лучший вариант."
window hide
n '''Спасибо за прохождение нашей первой игры!

Над ней работали Капустяшки:

- Сидельникова Анастасия

- Капустян Ева

- Емельянов Матвей

- Дашацыренов Лев'''
nvl hide
pause



