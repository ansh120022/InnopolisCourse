# Задание 1 - наследование от TestCase в юнит-тестах

# Задание 2

class Child(list):

    def __truediv__(self, d):
        l = len(self)
        step, ost = divmod(l, d)
        new_list = list()
        for i in range(d):
            new_list.append(self[i*step:step + i*step])
        if (ost > 0):
            new_list[-1] = self[(l - ost-step):]
        return new_list


obj = Child([1,2,3,4,5,6,7,8,9,10,11,12])
print(obj/3)

