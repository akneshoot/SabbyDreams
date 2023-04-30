# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define sabby = Character('Сэбби')
define mother = Character('Мама')
define nachalo = ('...')
define nastya = ('Настя')

image room sabby = 'Back/roomsabby.jpg'
image sabby = 'Role/Sb.png'
image glavnoe = 'Back/osnova.jpg'
image padik = 'Back/padik.png'
image sad sabby = 'Role/sad sb.png'
image mother = 'Role/mother.png'
#image nastya = ''

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.


label start:
    # 1 frame
    scene glavnoe
    nachalo "Глава первая"
    #2 frame
    scene roomsabby
    with fade
    show mother:
        xalign 0.8 yalign 1.8
    mother "Доченька, пора просыпаться, папа уже уехал, а ты даже не пожелала ему удачного дня."
    #3 frame
    show sad sabby:
        xalign 0.1 yalign 3.4
    sabby "Да, мам, еще пять минут"
    #4 frame
    mother "Давай вставай, завтрак на столе, не забудь почистить зубы,а я побежала на работу, буду через 6 часов"
    #5 frame
    sabby "Хорошо, встаю"
    #6 frame
    hide sad sabby
    hide mother
    nachalo "..."
    #7 frame
    scene padik
    with fade
    show sabby
    sabby "Так, зубы почистила, завтрак съела, можно пойти гулять"
    #8 frame 
    show sabby:
        xalign 0.1
    nastya "Ой, Сэбби, привет, как ты уже подросла"
    return

