if __name__ == "__main__": # why just like this??????
    numbers = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine"
    }


    you_number = input("Write a number ") # nice to know, that \n means new line
    result = ""
    for x in you_number:
        result += numbers[int(x)] + " "
    print(result)
