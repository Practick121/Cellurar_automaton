# инициализация
from initialization import *

ticks = 0
cnt_iter = 0


T = 1 / FPS
delay_run = Timer(DELAY)
timer1 = Timer(T)
timer2 = Timer(2)
cnt_frames = 0
while is_running:
    if timer1.is_out():
        rendering(global_display, sprites)  # отрисовка дисплея
        cnt_frames += 1
        timer1.wind_up()

    processing_own_events()
    processing_mouse_events()  # обработка событий курсора мыши
    processing_event()  # обработка общих событий

    for sprite in sprites:
        sprite.check()
        if Transmission.paintstop and sprite == button_stop:
            button_stop.get_active()
            Transmission.paintstop = False

    if timer2.is_out():
        print(cnt_frames / 2)
        timer2 = Timer(2)
        cnt_frames = 0

    clock_ips.tick(IPS)
    cnt_iter += 1
