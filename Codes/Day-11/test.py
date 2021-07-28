import pkg1
from pkg1.pkg2 import mod1, mod2
from pkg1.pkg3.mod3 import listsq, listrt

def main():
    list = [23, 56, 891, 561, 457]

    ans = listsq(list)
    res = listrt(list)

    for i in range(len(res)):
        res.insert(i, mod2.root(res[i], 4))

    for i in range(len(ans)):
        res.insert(i, mod1.sub(ans[i], 15))

    print(res)
    print(ans)

if __name__ == '__main__': 
    main()
    print(__name__,'\n')