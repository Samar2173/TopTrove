def pow(n1, n2):    
    return n1 ** n2

def root(n1, n2):    
    return (n1 ** (1/n2))

def main():
    print(pow(5, 2))
    print("Solution Acquired")
    print(root(100, 2))
    print("Root Acquired")

print(__name__,'\n')
if __name__ == '__main__': 
    main()