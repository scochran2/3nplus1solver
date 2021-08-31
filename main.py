count = 0
num = input("Enter any real number: ")
num = float(num)
while num != 1 and num != -1:
    count += 1
    if (num % 2) == 0:
        num = (num / 2)
        print("{:,.0f}".format(num))
    else:
        num = (num * 3) + 1
        print("{:,.0f}".format(num))
print("It took " + str(count) + " steps")
