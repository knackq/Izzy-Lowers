#Izzy Lowers

def encode(original):
    list = []
    string = [*original]
    for i in string:
        i = str(int(i)+3)
        list.append(i)
        continue
    encoded = (''.join(list))
    return encoded

def main():
    original = None
    loop = True


    print("Menu\n"
          "-------------\n"
          "1. Encode\n"
          "2. Decode\n"
          "3. Quit")

    while loop == True:

        menu = input("Please enter an option: ")

        if menu == "1":
            original = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
            print(encode(original))


        if menu == "2":
            encoded = input("Please enter your password to decode: ")
            decoded = decode(encoded)
            print(f"The decoded password is {decoded}, and the original password is {encoded}")


        if menu == "3":
            break


if __name__ == "__main__":
    main()