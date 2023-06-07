import random

CHARS = ' ABCDEFGHIJLKLMNOPQRSTUVWXYZ'
TARGET = 'METHINKS IT IS LIKE A WEASEL'
output = list('')

def generate():
    tes = list('')
    size = len(TARGET)
    while size > 0:
        i = random.randint(0,len(CHARS)-1)
        ap = CHARS[i]
        tes.append(ap)
        size-=1
    return tes

def mutate(TARGET,actual):
    tmp = actual
    it =0
    for i in TARGET:
        if tmp[it] != TARGET[it]:
            l = random.randint(0,len(CHARS)-1)
            ap = CHARS[l]
            tmp[it] = ap
            it+=1
        else:
            it+=1
    return tmp


def fitness(str_to_test,TARGET):
    matches = 0
    it = 0
    for i in str_to_test:
        if str_to_test[it] == TARGET[it]:
            matches +=1
        it+=1
    return matches

def main():
    tot = len(TARGET)
    itt = 0
    invalid = True
    parent = generate()
    mat = fitness(parent,TARGET)
    print("Iteration:",itt,''.join(parent),round(((100/tot)*mat),1),"%")
    itt+=1
    while invalid == True:
        tmp = mutate(TARGET,parent)
        parent = tmp
        mat = fitness(parent,TARGET)
        print("Iteration:",itt,''.join(parent),round(((100/tot)*mat),1),"%")
        itt+=1
        if ''.join(parent) == ''.join(TARGET):
            invalid = False

        
main()
