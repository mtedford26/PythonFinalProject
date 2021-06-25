
#code set-up for MCU Bechdel Test

import pandas as pd
import re

# male gendered language = mgl
mgl = ['loki', 'odin', 'winter soldier', 'buck', 'bucky', 'barnes', \
       'james', 'killmonger', 'arnim', 'zolaf', 'captain america', \
       'cap', 'steve', 'rogers', 'clint', 'clint barton',  'hawkeye', \
       'fury', 'nick', 'coulson', 'phil', 'banner', 'he', 'him', 'his', \
       'tony', 'stark', 'bruce', 'jarvis', 'strucker', 'chala', 'chaka', \
       'man', 'sir', 'mr', 'thor', 'panther', 'cat', 'pietro', 'ultron', \
       'rhodes', 'rhodey', 'wilson', 'sam', 'falcon', 'klaue', 'ulysses', \
       'heimdall', 'erik', 'selvig', 'vision', 'thanos', 'bron-char', \
       'ronan', 'korath', 'director', 'supereme intelligence', 'talos', \
       'yon-rogg']

# named women = nw
nw = ['maria', 'natasha', 'romanoff', 'peggy', 'carter', 'danvers', 'hill', \
      'shuri', 'laura', 'wanda', 'friday', 'helen', 'cho', 'minn-erva', \
      'wendy', 'lawson', 'rambeau', 'monica', 'mon', 'maria', 'carol']
    
# giving variable names to the above dataframes
df = pd.DataFrame(mgl)
df2 = pd.DataFrame(nw)

index = 0
# open text files that include entire scripts for 3 MCU films
inputfile = open('captain_america_movie_script.txt', 'r')
outputfile = open('captain_america_movie_script2.txt', 'w')
#caw = captain america write
caw = inputfile.lower()
print(caw, file=outputfile)


# this for loop is an attempt at removing all non-dialogue lines
for line in 'caw':
    dummy_file = re.search('caw', '^[')
    del dummy_file
print(caw)

inputfile2 = open('captain_marvel text file movie script.txt', 'r')
outputfile2 = open('captain_marvel text file movie script2.txt', 'w')
#cmw = captain marvel write
cmw = inputfile2.lower()
print(cmw, file=outputfile2)

inputfile3 = open('age_of_ultron text file movie script.txt', 'r')
outputfile3 = open('age_of_ultron text file movie script2.txt', 'w')
#aouw = age of ultron write
aouw = inputfile3.lower()
print(aouw, file=outputfile3)


lines = 


#for line in 
#    for quotes, [in string(variable.remove)]
                         
