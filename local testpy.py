import random
import json
import re

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
 
with open(r'dict.json', encoding='utf-8') as json_file:
    dict_text = json.load(json_file)
    
text = dict_text['translate']    

def ogerfy(arg):
    arg = arg.splitlines()
    text_bytes = b""

    for line in arg:
        trans = line
        for key, item in text.items():
            word = re.escape(key)
            trans = re.sub(word, lambda m: re.escape(random.choice(item)), trans)

        text_bytes += trans.encode() + b'\n'
        output = text_bytes.decode("utf-8").replace("\\", "")
        print('\n\n')
        print(f'{bcolors.OKGREEN}{output}{bcolors.ENDC}' )
        
      
      
def lüge():
    lüge = random.choice(open("lügen.txt").readlines()) 
    print(lüge)           
ogerfy(input(f'{bcolors.WARNING}Ogerfy einen Text: {bcolors.ENDC}') ) 


