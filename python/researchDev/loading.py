import itertools
import threading
import time
import sys

done = False
#loading animation
def load_analyzer():
    for f in itertools.cycle(['.','.','..','..','...','...','....','....','.....','.....']):
        if done:
            break
        sys.stdout.write('\rAnalyzing File ' + f)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')

t = threading.Thread(target=load_analyzer)
t.start()

#process timer
time.sleep(10)
done = True