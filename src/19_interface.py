class AdvancedArithmetic(object):
    def divisorSum(n):
        raise ZeroDivisionError

class Calculator(AdvancedArithmetic):
    def __init__(self):
        AdvancedArithmetic.__init__(self)

    def divisorSum(self, n):
        sum_list = []
        for i in range(1, n):
            if n % i == 0:
                sum_list.append(i)
        return sum(sum_list) + n

n = 6
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)