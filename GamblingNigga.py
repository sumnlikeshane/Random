import random
dic = {1:"@",2:"$",3:"&"}
s = True

while s:
    f = dic.get(random.randint(1,3))
    s = dic.get(random.randint(1,3))
    t = dic.get(random.randint(1,3))

    print(f"{f}:{s}:{t}")
    if f == t and f == s:
        print("you win")
        s = False
    else:
        print("you loose")
