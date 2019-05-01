class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    # Add your code here
    def computeDifference(self):
        arr_len = len(self.__elements)

        for step in range(arr_len):
            if step == 0:
                pass
            else:
                self.__elements[0], self.__elements[step] = self.__elements[step], self.__elements[0]
                print(self.__elements)

            for i in self.__elements[1:]:
                calc = (abs(self.__elements[0] - i))
                if calc > self.maximumDifference:
                    self.maximumDifference = calc

# End of Difference class

_ = 5
a = [int(e) for e in "8 19 3 2 7".split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)