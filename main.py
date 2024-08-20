# Dice sum probability calculator
# Författare:
# Datum:

def main():
    user_input = input().split(" ")
    for i in range(len(user_input)):
        user_input[i] = int(user_input[i])
    results = []
    for i in range(user_input[0]):
        for j in range(user_input[1]):
            results.append(i+j)
    print(results)


if __name__ == "__main__":
    main()
