# Dice sum probability calculator
# Författare:
# Datum:
from collections import Counter


def main():
    user_input = input().split(" ")
    # for i in range(len(user_input)):
    #     user_input[i] = int(user_input[i])
    # results = []
    # for i in range(user_input[0]):
    #     for j in range(user_input[1]):
    #         results.append(i+j+2)
    # x = 0
    # top_num = []
    # for i in range(user_input[0]*user_input[1]):
    #     if x < results.count(i+1):
    #         x = results.count(i+1)
    #         top_num = [i+1]
    #     elif x == results.count(i+1):
    #         top_num.append(i+1)
    # for i in range(len(top_num)):
    #     print(top_num[i])
    for i in range(len(user_input)):
        user_input[i] = int(user_input[i])
    results = []
    for i in range(user_input[0]):
        for j in range(user_input[1]):
            results.append(i+j+2)
    count = Counter(results).most_common()
    most_times_appeared = count[0][1]
    for i in range(len(count)):
        if most_times_appeared == count[i][1]:
            print(count[i][0])
        else:
            break


if __name__ == "__main__":
    main()
