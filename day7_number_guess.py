n = 5
while n > 0:
    print(n)
    n = n - 1
print("Blast!")


secret = 69
guess = 0
while guess != secret:
    guess = int(input("Guess karo:"))
    if guess <secret: print("Bada socho")
    elif guess >secret: print("Chhota socho")
    else: print("Congratulations you did it")