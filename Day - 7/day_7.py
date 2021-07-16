def calc(num1, num2, operator):
    num1 = int(num1)
    num2 = int(num2)
    if operator == '+':
        answer = num1 + num2
        return answer

    elif operator == '-':
        answer = num1 - num2
        return answer

    elif operator == '*':
        answer = num1 * num2
        return answer
        
    elif operator == '/':
        answer = num1 / num2
        return answer

    else:
        print("Invalid format")

def main():
    calc_input = input("Enter your Problem: ").split()
    result = calc(calc_input[0], calc_input[2], calc_input[1])
    print(result)
    while True:
        check = input("DO you want to continue (y/n): ")
        if check == 'y':
            main()
        elif check == 'n':
            quit()

if __name__ == '__main__':
    main()
