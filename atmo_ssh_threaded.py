import os

import atmoEventThread
from animation import AnimThread
# import server
from animation.ShotAnim import ShotAnim

# needs connection

# a = atmoEventThread.AtmoEventStream()
# a.start()

at = AnimThread.AnimThread()
at.start()
at.add(ShotAnim(1))

exit = False

# pygame.init()
# window = pygame.display.set_mode((100, 100))

try:
    while True:
        m = a.read()
        if m:
            print(m)
        if m == 'shot1':
            at.add(ShotAnim(1))
            # atmo_dotstar.gunShot(3)
            #     elif m == 'gatling':
            #         atmo_dotstar.gGunShot(3)
            #
            #     elif m == 'arrow':
            #         atmo_dotstar.arrowShot(2)
            #     elif m == 'arrow1':
            #         atmo_dotstar.arrowShot(3)
            #     elif m == 'arrow2':
            #         atmo_dotstar.arrowShot(2)
            #     elif m == 'arrow3':
            #         atmo_dotstar.arrowShot(1)
            #     elif m == 'arrow4':
            #         atmo_dotstar.arrowShot(4)
            #     elif m == 'beer':
            #         atmo_dotstar.beerDrink(3)
            #
            #     elif m == 'tnt_on':
            #         on = True
            #         i = 0
            #         os.system('mpg123 -q testimages/tnt2.mp3 &')
            #         while on:
            #             if a.read() == 'tnt_off':
            #                 on = False
            #                 os.system('pkill mpg123')
            #                 atmo_dotstar.setPixelRange([0], atmo_dotstar.numpixels, atmo_dotstar.bgColor)
            #             else:
            #                 i += 1
            #                 atmo_dotstar.tntEffect()
            #             if i == 22:
            #                 i = 0
            #                 os.system('mpg123 -q testimages/tnt2.mp3 &')
            #
            #
            #     elif m == 'exit':
            #         a.close()
            #         break
            #
except KeyboardInterrupt:
    os._exit(0)