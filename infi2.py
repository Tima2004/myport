s = int(input())
if s%3 == 0 and s%4 == 0:
        print("Divisible by 3 and 4")
elif s%3 == 0:
        print("Divisible by 3")
elif s%4 == 0:
        print("Divisible by 4")
else:
        print("Not divisible by 3 or 4")
