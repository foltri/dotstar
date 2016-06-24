# import the necessary packages
from threading import Thread
import server


class AtmoEventStream:
    def __init__(self):
        # initialize the video camera stream and read the first frame
        # from the stream
        self.stream = server

        self.message = self.stream.receive()

        # initialize the variable used to indicate if the thread should
        # be stopped
        self.stopped = False
        self.unread = True

    def start(self):
        # start the thread to read frames from the video stream
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        # keep looping infinitely until the thread is stopped
        while True:
            # if the thread indicator variable is set, stop the thread
            if self.stopped:
                self.stream.close()
                return

            # otherwise, read the next frame from the stream
            self.message = self.stream.receive()
            # print('NEW')
            self.unread = True

    def read(self):
        # return the frame most recently read

        if self.unread:
            self.unread = False
            # print('READ')
            return self.message
        else:
            pass

    def close(self):
        # indicate that the thread should be stopped
        self.stopped = True

