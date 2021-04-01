import json

word = input("Ener word:=")
file = open("data.json",)
data = json.load(file)
try:
    for meaning in data[word]:
        print(meaning)
    file.close()
except:
    print("Wrong word")

    print(f"Do you mean {word}?")
    Y_N = input("Enter Y if Yes , or N if NO:-")
    if Y_N == 'N':
        print("Please doble check it and try again:")
    elif Y_N == 'Y':
        try:
            file1 = open("data.json", )
            data1 = json.load(file)
            for meaning in data1[word]:
                print(meaning)
            file.close()
        except:
            print("The word doesnt exist. Please double check it")
    else:
        print("We didnt understand your entry.")




