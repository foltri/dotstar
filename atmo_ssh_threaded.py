from __future__ import division

import multiprocessing
import os
import unity_server as server
from Queue import Queue

import atmoEventThread
from animation import AnimThread

MESSAGE_POOL = multiprocessing.Queue()

ae = atmoEventThread.AtmoEventStream(MESSAGE_POOL)
at = AnimThread.AnimThread(MESSAGE_POOL)

try:
    ae.start()
    at.start()
except KeyboardInterrupt:
    server.close()
    os._exit(0)
