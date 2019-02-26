

def cake(input):
    if int(input) == 10:
        print("Happiness is here")
        return 55
    elif int(input) == 55:
        try:
            return 55
        except:
            print("I found an error, but I don't care")
    else:
        print("There is only sadness")
