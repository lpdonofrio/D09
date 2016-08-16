def fizzbuzz():
    for n in range(1, 101):
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else:
            print(n)

fizzbuzz()


def fizzbuzz_two():
    for n in range(1, 101):
        msg = ""
        if n % 3 == 0:
            msg += "Fizz"
        if n % 5 == 0:
            msg += "Buzz"
        print(msg or n)

fizzbuzz_two()