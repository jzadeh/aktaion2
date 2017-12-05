import itertools
import threading
import time
import sys

done = False
#loading animation
def load_analyzer():
    for f in itertools.cycle(['ᗧ*Analyzing*File*','*Aᗧnalyzing*File*','*Anᗧalyzing*File*','*Anaᗧlyzing*File*',
                              '*Analᗧyzing*File*','*Analyᗧzing*File*','*Analyzᗧing*File*','*Analyziᗧng*File*',
                              '*Analyzinᗧg*File*','*AnalyzingᗧFile*','*Analyzing*Fᗧile*','*Analyzing*Fiᗧle*',
                              '*Analyzing*Filᗧe*','*Analyzing*Fileᗧ*']):
    #for f in itertools.cycle(['ᗧ','ᗧ*','*ᗧ*','**ᗧ*','***ᗧ*','****ᗧ*','*****ᗧ*','****ᗧ']):
        if done:
            break
        sys.stdout.write('\r' + f)
        #sys.stdout.write('\rAnalyzing File ' + f)
        sys.stdout.flush()
        time.sleep(0.3)
    sys.stdout.write('\rCompleted!')

t = threading.Thread(target=load_analyzer)
t.start()

#process timer
time.sleep(10)
done = True