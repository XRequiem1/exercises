#1
# class Point3D:
#
#     def __init__(self, x=0, y=0, z=0):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def info(self):
#         print(f'x = {self.x}, y = {self.y}, z = {self.z}')
#
#     def distance(self, a, b):
#         return b - a
#
#     def distance2(self):
#         return f'Расстояние от x до y: {self.distance(self.x, self.y)}.\nРасстояние между y и z: {self.distance(self.y, self.z)}'
#
#
# first = Point3D(2, 5, 8)
# second = Point3D(5, 8, 7)
# third = Point3D(8, 7, 3)
# print(first.x)
# print(first.distance2())

#1 квадрат
# class Square:
#
#     def __init__(self,x=0,y=0):
#         self.x = x
#         self.y = y
#
#     def xy(self):
#         print(f'x={self.x}, y={self.y}')
#
#     def one(self,a):
#         return a * a
#
#     def two(self,b):
#         return b * 4
#
#     def countt(self):
#         return f'Площадь = {self.one(self.x)}'
#
#     def countt2(self):
#         return f'Периметр = {self.one(self.y)}'
#
# info = Square(3,4)
# info.xy()
# print(info.countt())
# print(info.countt2())

#1 треугольник
#
# class Triangle:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#
#     def countS(self,a,b):
#         S = a * b / 2
#         print(S)
#
#     def countP(self,a,b):
#         P = a ** 2 + b ** 2 / a / b + a + b
#         print(P)
#
# S = Triangle(3,5)
# S.countS(3,5)
# S.countP(3,5)



#1
# class CPerson:
#
#
#     def __init__(self,name,surname,father,dob,pol):
#         self.name = name
#         self.surname = surname
#         self.father = father
#         self.dob = dob
#         self.pol = pol
#
#     def __del__(self):
#         print('deleted', self.name)
#
# tom = CPerson('Емельян','Пугачёв','Сергеевич','06.08.2007','муж')
# print(tom.name)
# print(tom.surname)
# print(tom.father)
# print(tom.dob)
# print(tom.pol)
# del tom

#2
# class Phone1:
#
#     model = 'nokia'
#     number = '+7-987-457-86-34'
#     weight = '0.2'
# class Phone2:
#
#     model = 'iphone'
#     number = '+7-987-456-12-30'
#     weight = '0.2'
#
# class Phone3:
#
#     model = 'xiaomi'
#     number = '+7-985-556-76-31'
#     weight = '0.2'
#
# print(Phone1.model, Phone1.number, Phone1.weight)
# print(Phone2.model, Phone2.number, Phone2.weight)
# print(Phone3.model, Phone3.number, Phone3.weight)
#
#
#
# class Phone:
#
#     def __init__(self,name,number,model,weight):
#         self.name = name
#         self.number = Phone1.number
#         self.model = Phone1.model
#         self.weight = Phone1.weight
#
#     def recieveCall(self, name):
#         self.name = name
#
#     def getNumber(self,number):
#         self.number = number
#
#     def say(self, message):
#         print(message)
#
#     def say_hello(self):
#         self.say(f'Звонит {self.name}. Номер {self.number}')
#
# alex = Phone('Alex','7-896-342-45-89','iphone','0.2')
# alex.say_hello()

#3
# class Reader:
#
#     fio = 'Петров Иван Александрович'
#     number = '33234586789'
#     fakultet = 'Филологический'
#     d_o_b = '06.08.2007'
#     phone_number = '7-890-234-67-59'
#
#
#     def __init__(self,took,returned,fio):
#         self.took = took
#         self.returned = returned
#         self.fio = fio
#
#
#     def takeBook(self,a):
#         print(a)
#
#     def returnBook(self,b):
#         print(b)
#
#     def say_books(self):
#         self.takeBook(f'{self.fio} взял {self.took} книги')
#
#     def say_book(self):
#         self.takeBook(f'{self.fio} вернул {self.returned} книги')
#
# read = Reader(5,3,'Петров Иван Александрович')
#
# read.say_books()
# read.say_book()




