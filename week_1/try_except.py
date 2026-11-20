try:
    print("Let's divide some numbers")
    s = 2 / 0
    print("Cool!")
except ZeroDivisionError:
    print("You can't divide by zero")


"""
В данном примере, первый print() сработает, но когда произойдет 
2 / 0, появится исключение и мы перейдем в  блок exept

"""
