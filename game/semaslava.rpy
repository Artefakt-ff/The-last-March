init:
    image slavasema = "images/korm_mant.png"
    image vpiska I = "images/vpiska/1.jpg"
    image vpiska II = "images/vpiska/2.jpg"
    image vpiska III = "images/vpiska/3.jpg"
    $ korm = Character(u'Кормильцев')
    $ mant = Character(u'Манторов')
label semaslava_branch:
    scene bg IV toilet
    show slavasema at center
    korm "Слышь, сюда подошел быстро!"
    mant "Сиги есть?"
    g "Эй, ребят, полегче"
    $ surname = u'Бог'
    if surname == 'Бог' or surname == 'Осипкина' or surname == 'Новоселова' or surname == 'Хазина' or surname == 'Михайлова' or surname == 'Горбач':
        $ cond = True
    menu:
        "Попробовать пройти мимо":
            mant 'Это наш туалет'
            korm 'Мы тут хозяева'
            g "Санава, санава бич... Заново жить научи..."
            mant 'Оооо, свой человек'
            korm 'Можешь воспользоваться нашими апартаментами!'
            "Делаешь свои дела под пристальными взглядами"
            hide slavasema with dissolve            
            scene bg II hall
            jump leo
        "Попробовать убежать":
            mant "Стой, кучерявый!"
            korm "Я тебя на своей девятке прокачу!"
            hide slavasema with dissolve
            scene bg II hall
            jump leo
        "Предложить выпить" if cond:
                g 'А не выпить ли нам за знакомство?'
                korm 'Деловой разговор!'
                hide slavasema with dissolve
                play music "sounds/kaif.mp3"
                show vpiska I with dissolve 
                $ renpy.pause(1.5)
                show vpiska II with dissolve 
                $ renpy.pause(1.5)
                show vpiska III with dissolve 
                g "Кто я..? Где я..?"
                g 'Какое сегодня число?'
                "В кармане находится календарик с иконой на другой стороне"
                g 'ЧЁРТ! 9...'
                g '...апреля'
                jump fail




