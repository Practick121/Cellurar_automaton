# инициализация
from initialization import *

timer1 = Timer(1 / FPS)
while is_running:
    if timer1.is_out():
        rendering(global_display, sprites)  # отрисовка дисплея
        timer1.wind_up()

    processing_own_events()
    processing_event()  # обработка общих событий

    for sprite in sprites:
        sprite.check()
        if Transmission.paint_stop and sprite == button_stop:
            button_stop.get_active()
            Transmission.paint_stop = False

    clock_ips.tick(IPS)
