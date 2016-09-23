#!/usr/bin/env python3
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# Import python modules
import multiprocessing

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# Import user modules
import server



#------------------------------------------------------------------------------#
class AtmoEventStream:

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def __init__(self, message_pool):
        # initialize the video camera stream and read the first frame
        # from the stream
        self.stream = server
        self._message_pool = message_pool

        # self.message = self.stream.receive()

        # initialize the variable used to indicate if the thread should
        # be stopped
        self.stopped = self.unread = False


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def start(self):
        # start the thread to read frames from the video stream
        # Thread(target=self.update, args=()).start()

        thread = multiprocessing.Process(target=self.update, args=())
        thread.daemon = False
        thread.start()



    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def update(self):
        # keep looping infinitely until the thread is stopped
        while True:
            # if the thread indicator variable is set, stop the thread
            if self.stopped:
                return self.stream.close()

            # otherwise, read the next frame from the stream
            self._message_pool.put(self.stream.receive())

            # print('NEW')
            self.unread = True


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def read(self):
        # return the frame most recently read
        if self.unread:
            self.unread = False
            # print('READ')
            return self.message


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def close(self):
        # indicate that the thread should be stopped
        self.stopped = True
