print("This is mod3")
print(__name__,'\n')

def listsq(list):
    l = [i ** 2 for i in list]
    return l

def listrt(list):
    l = [i ** 0.5 for i in list]
    return l

def main():
    list = [4, 25, 64, 81]
    print(listsq(list))
    print(listrt(list))

if __name__ == '__main__': 
    main()
    