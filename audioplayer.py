import simpleaudio as sa
import time

import atexit
from threading import Thread

class AudioPlayer:
    """ Audio player which give simple methods to handle the audio player. 
        The audio player is provided by simpleaudio library.
    """
    def __init__(self, filename=None, timeSlice=0.3):
        """ Constructor to create audio player. 
        """
        self.filename = filename
        self.timeSlice = timeSlice
        self.play_obj = None 
            
    def setFile(self, filename):
        """ Set file for this player. 
        """
        self.filename = filename

    def setTimeSlice(self, timeSlice):
        """ Set timeslice for current player. 
        """
        self.timeSlice = timeSlice

    def play(self):
        """ Method to play the file. 
        """
        wave_obj = sa.WaveObject.from_wave_file(self.filename)
        self.play_obj = wave_obj.play()
    
    def stop(self):
        """ Method to stop current playback. 
        """
        if self.play_obj:
            self.play_obj.stop()

def play_sound():
    pass


all_threads = []

def sound_alert(filename="1.wav"):
    player = AudioPlayer(filename=filename)
    th = Thread(target=player.play)
    all_threads.append(th)
    th.start()


@atexit.register
def _cleanup_threads():
    for t in all_threads:
        t.join(timeout=2)


if __name__ == '__main__':
    import time
    sound_alert("1.wav")
    time.sleep(2)
