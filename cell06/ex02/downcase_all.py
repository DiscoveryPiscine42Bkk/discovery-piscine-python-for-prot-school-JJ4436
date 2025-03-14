
import sys

def downcase_it(text):
    return text.lower()
i=0

if len(sys.argv) <= 1 :
    print("none")
else:
    while i < len(sys.argv): 
        print(downcase_it(sys.argv[i]))
        i += 1



