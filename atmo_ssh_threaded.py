from __future__ import division
import os
from Queue import Queue

import atmoEventThread
from animation import AnimThread

MESSAGE_POOL = Queue()

ae = atmoEventThread.AtmoEventStream(MESSAGE_POOL)
at = AnimThread.AnimThread(MESSAGE_POOL)

try:
    ae.start()
    at.start()
except KeyboardInterrupt:
    os._exit(0)
