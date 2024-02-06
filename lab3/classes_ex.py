#1.
class String:
    def getString(self):
        self.string = input();
    def printString(self):
        self.string.upper();
        print(self.string);

"""
stri = String();
stri.getString();
stri.printString();
"""

#2.
class Shape:    
    def area(self):
        print(0);

class Square(Shape):
    def __init__(self, length):
        self.length = length;

    def area(self):
        print(self.length * self.length);

"""
shape = Shape();
shape.area();

square = Square(4);
square.area();
"""

#3.
class Rectangle(Square):
    def __init__(self, length, width):
        self.length = length;
        self.width = width;

    def area(self):
        return self.length * self.width;

"""
rectangle = Rectangle(4, 5);
print(rectangle.area());
"""

#4.
class Point:
    def __init__(self, x, y):
        self.x = x;
        self.y = y;
    
    def show(self):
        print(self.x, self.y);
    
    def move(self, newx, newy):
        self.x = newx;
        self.y = newy;

    def dist(self, otp):
        return ((self.x - otp.x) ** 2 + (self.y - otp.y) ** 2) ** (1/2);

'''
p1 = Point(1, 3);
p1.show();
p1.move(5, 4);

p2 = Point(4, 5);
print(p1.dist(p2));
'''

#5.
class Account:
    def __init__(self, owner, balance):
        self.own = owner;
        self.bln = balance;

    def deposite(self, money):
        self.bln += money;
        print(self.own, "fill account", money, '. Deposite now', self.bln, end = '.\n');

    def withdraw(self, money):
        if money > self.bln:
            print(self.own, "dont have enough money.");
        else:
            self.bln -= money;
            print(self.own, "take", money, "from deposite. Now balance is", self.bln, end = '.\n');

    def seebln(self):
        print(self.own, "have in deposite", self.bln);

"""
mybank = Account("Nursultan", 40000);

mybank.deposite(20000);
mybank.seebln();
mybank.withdraw(70000);
mybank.withdraw(60000);
"""

#6.

class PrimeFilter:
    def __init__(self, numbers):
        self.numbers = numbers;

    def is_prime(self, n):
        if n < 2:
            return True;
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return True;
        return False;

    def filter_primes(self):
        return list(filter(lambda x: self.is_prime(x), self.numbers));

"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
prime_filter = PrimeFilter(numbers);
prime_numbers = prime_filter.filter_primes();

print("Prime numbers:", prime_numbers);
"""