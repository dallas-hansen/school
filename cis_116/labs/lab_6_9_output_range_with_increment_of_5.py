int1 = int(input())
int2 = int(input())

if int1 > int2:
    print("Second integer can't be less than the first.")
else:
    # while int1 <= int2:
    #     print(int1, end=' ')
    #     int1 += 5
    # else:
    #     print()
    for i in range(int1, int2+1, 5):
        print(i, end=' ')
    print()