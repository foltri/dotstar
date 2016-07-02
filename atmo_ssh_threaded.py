import os

import atmoEventThread
import random
from animation.AnimThread import AnimThread
from animation.ShotAnim import ShotAnim
import server as stream
# needs connection
from animation.TestAnim import TestAnim
from animation.dynamite_anim import DynamiteAnim

at = AnimThread()
at.start()
# at.add(ShotAnim(1))

options = {'test'    : lambda: at.add(TestAnim(random.randint(0, 0xFFFFFF))),
           'shot1'   : lambda: at.add(ShotAnim(1)),
           'shot2'   : lambda: at.add(ShotAnim(2)),
           'shot3'   : lambda: at.add(ShotAnim(3)),
           'shot4'   : lambda: at.add(ShotAnim(4)),
           'tnt_on'  : lambda: at.add(DynamiteAnim()),
           'tnt_off' : lambda: at.remove(DynamiteAnim),
           None      : lambda: None}

try:
    while True:
        m = stream.receive()

        if m:
            print(m)
            options.get(m)()
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
        #       tnt
        #
except KeyboardInterrupt:
    os._exit(0)


