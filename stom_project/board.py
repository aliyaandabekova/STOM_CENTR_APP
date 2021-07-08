# # str1 = '                 fghj              '
# # print(str1.split())
# #
# #
# # print(list(range(10)))
# # print(dict(hours=10))
# #
# # import random
# # print(random.randint(1,10))
#
# # l1 = [1,2,3,4,5,6,7]
# #
# # def map1(elem):
# #     result = elem % 2
# #     return result
# #
# # l2 = map(map1,l1)
# # print(list(l2))
#
#
# import random
# l1 =[]
# for i in range(10000):
#     l1.append(random.randint(1,100000))
# # print(l1)
#
# def func1(elem):
#     if elem > 95000:
#         return True
#
# l2 = filter(func1,l1)
# print(len(list(l2)))
# print('%s, eggs, and %s'%('spam','SPAM1'))



class AgeDescriptor:
    def __init__(self,param):
        self.param = param

    def __get__(self, instance, owner):
        return instance.__dict__[self.param]

    def __set__(self, instance, value):
        if isinstance(value,int):
            if 0 < value <= 250:
                instance.__dict__[self.param] = value
            else:
                raise ValueError('Invalid number!')
        else:
            raise ValueError('Must be int!')



class NameDescriptor:
    def __init__(self,param):
        self.param = param

    def __set__(self, instance, value):
        if isinstance(value,str):
            if len(value) < 50:
                if value.isalpha():
                    instance.__dict__[self.param] = value
                else:
                    raise ValueError('Only alphas!')
            else:
                raise ValueError('Too long name!')
        else:
            raise ValueError('Must be str!')


class Human:
     age = AgeDescriptor('age')
     name = NameDescriptor('name')

     def __init__(self, name, age):
         self.name = name
         self.age = age
h1 = Human('john',18)
print(h1.__dict__)