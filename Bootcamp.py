my_age=30
my_name="Vijay"
print("Hello",my_age)

print("Hello",my_name)
import sys
print(sys.maxsize)
print(sys.float_info.max)

print("Cast",type(int(5.5)))
print("Cast 2",type(str(5.43)))
print("Cast 3",type(chr(97)))
print("Cast 4",type(ord("a")))
print("Cast 5",type(float(2)))

num_1="1"
num_2="2"
print("1+2=",(int(num_1)+int(num_2)))

num_1=input("Enter first Numbers :")
num_2=input("Enter Second Number")


num_1=int(num_1)
num_2=int(num_2)
sum_1=num_1+num_2
difference=num_1-num_2
product=num_1*num_2
quotient=num_1/num_2
remainder=num_1 % num_2

print("{} + {}={}".format(num_1,num_2,sum_1))
print("{} - {}={}".format(num_1,num_2,difference))
print("{} * {}={}".format(num_1,num_2,product))
print("{} / {}={}".format(num_1,num_2,quotient))
print("{} % {}={}".format(num_1,num_2,remainder))

miles=int(input("Enter Miles"))
Kilometers=miles * 1.60934
print("{} miles equal {} kilometers".format(miles,Kilometers))
import math
print("ceil(4.4)=",math.ceil(4.4))
print("floor(4.4)=",math.floor(4.4))
print("fabs(-4.4)=",math.fabs(-4.4))
print("factorial(4)=",math.factorial(4))
print("fmod(5,4)=",math.fmod(5,4))
print("trunc(4.2)=",math.trunc(4.2))
print("pow(2,2)=",math.pow(2,2))

drink=input("Pick One(Coke or Pepsi:")if drink=="Coke":
    print("Here is your Coke")
elif drink=="Pepsi":
    print("Here is your pepsi")
else:
    print("Here is your water")

num_1,operator,num_2=input("Enter Calculation:").split()
num_1=int(num_1)
num_2=int(num_2)
if operator=="+":
    print("{} + {} = {}".format(num_1,num_2,num_1+num_2))
elif operator=="-":
    print("{}-{}={}".format(num_1,num_2,num_1-num_2))
elif operator=="*":
    print("{}*{}={}".format(num_1,num_2,num_1*num_2))
elif operator=="/":
    print("{}/{}={}".format(num_1,num_2,num_1/num_2))

age=int(input("Enter Age: "))
if (age>=1) and (age<=18):
     print("Important Birthday")
elif(age==21) or (age==50):
    print("Important Birthday")
elif not age<65:
    print("Important Birthday")
else:
    print("Sorry Not IMportant Birthday")

age=int(input("Enter Age: "))
if age==5:
    print("Go to Kindergarten")
elif age>5 and age<=17:
    print("Go to Grade 6")
else:
    print("Go to College")


age=int(input("What is your age?"))
can_vote=True if age>=18 else False
print("You can vote:",can_vote)

for i in [2,4,6,8,10]:
    print("i=",i)


for i in range(2,7):
    print("i=",i)


your_float=input("Enter a float: ")
your_float=float(your_float)
print("Rounded to 2 Decimals: {:.2f}".format(your_float))

investment=float(input("Enter your investment amount: "))
interest=10
for i in range(1,11):
    investment=investment+(investment*interest*i)/100
    print(investment)

money=input("How much to invest:")
interest=input("Interest Rate:")

money=float(money)
interest=float(interest)*.01

for i in range(10):
    money=money+(money*interest*i)

print("Investment after 10 years: ${:.2f}".format(money))
     
import random
rand_num=random.randrange(1,51)
i=1
while i!=rand_num:
    i+=1
print("The random value is :",rand_num)

i=1
while i<=20:
    if (i%2)==0:
        i+=1
        continue
    if i==15:
        break
    print("Odd:",i)
    i+=1
r="#"
for i in range(1,6):
    r+=str(i)
    print(r)
for i in range(1,6):
    r.append("#")
    print(r)

while True:
    try:
        number=int(input("Please enter a number:"))
        break
    except ValueError:
        print("You didn't enter a number")
    except:
        print("An unknown error occurred")
print("Thank you for entering a number")


secret_number=7

while True:
    Guess=int(input("Enter a number:"))
    if Guess==secret_number:
        print("You guess it right")
        break

samp_string="This is a very important string"
print("Length :", len(samp_string))
print(samp_string[0])
print(samp_string[-1])
print(samp_string[0:4])
print(samp_string[8:])
print("Every Other", samp_string[0:-1:2])


print("Green","Eggs")
print("Hello"*5)



samp_string="This is a very important string"
for char in samp_string:
    print(char)



samp_string="This is a very important string"
for i in range(0,len(samp_string)-1,2):
    print(samp_string[i]+samp_string[i+1])

samp_string="This is a very imporant string"

print("A=",ord("A"))

norm_string=input("Enter a string to hide in uppercase:")
secret_string=""
for char in norm_string:
    secret_string+=str(ord(char))
print("Secret Message:",secret_string)
norm_string=""
for i in range(0,len(secret_string)-1,2):
    char_code=secret_string[i]+secret_string[i+1]
    norm_string+=chr(int(char_code))
print("Original Message:",norm_string)



rand_string="        this is an important string        "

rand_string=rand_string.lstrip()
rand_string=rand_string.rstrip()
print(rand_string)

rand_string="        this is an important string        "
rand_string=rand_string.strip()
print(rand_string)


rand_string="        this is an important string        "
print(rand_string.strip().upper().lower().capitalize())

rand_string="This is an important string"
print("Where is:",rand_string.replace(" an"," a kind of"))
a_list=["Bunch","of","random","words"]
print(",".join(a_list))

orig_string=input("Convert fo Acronym:")
orig_string=orig_string.upper()
list_of_words=orig_string.split()
for word in list_of_words:
    print(word[0],end="")

letter_z="z"
print("Is z a letter or number:",letter_z.islower())
print("Is z a letter or number:",letter_z.isdigit())
print("Is z a letter or number:",letter_z.isupper())
print("Is z a letter or number:",letter_z.isnumeric())



while True:
    message=input("Enter you message:")
    key=int(input("how many characters should we shift (1-26):"))
    secret_message=""

    for char in message:
        if char.isalpha():
            char_code=ord(char)
            char_code+=key

            if char.isupper():
                if char_code>ord("Z"):
                    char_code-=26
                elif char_code<ord("A"):
                    char_code+=26
            else:
                if char_code>ord("z"):
                    char_code-=26
                elif char_code<ord("a"):
                    char_code+=26
            secret_message+=chr(char_code)
        else:
            secret_message+=char
    print("Encrpyted:",secret_message)

    key=-key
    original_message=""
    for char in secret_message:
        if char.isalpha():
            char_code=ord(char)
            char_code+=key

            if char.isupper():
                if char_code>ord("Z"):
                    char_code-=26
                elif char_code<ord("A"):
                    char_code+=26
            else:
                if char_code>ord("z"):
                    char_code-=26
                elif char_code<ord("a"):
                    char_code+=26
            original_message+=chr(char_code)
        else:
            original_message+=char
    print("Decrpyted:",original_message)



def add_numbers(num_1,num_2):
    return num_1+num_2

print("5+4=",add_numbers(5,6))

def assign_name(name):
    name="Mark"

name="Tom"
change_name(name)
print(name)


def is_float(str_val):
    try:
        float(str_val)
        return True
    except valueError:
        return False
pi=3.14

print("Is Pi a float:",is_float(pi))


def solve_eq(equation):
    x,add,num_1,equal,num_2=equation.split()
    num_1,num_2=int(num_1),int(num_2)
    return "x= "+str(num_2-num_1)

print(solve_eq("x + 7 = 9"))



def mult_divide(num_1,num_2):
    return (num_1*num_2),(num_1/num_2)

mult,divide=mult_divide(5,6)
print("5*4=",mult)
print("5/4=",divide)


def is_prime(num):
    for i in range(2,num):
        if(num%i)==0:
            return False
    return True

print(is_prime(6))


def get_primes(max_number):
    list_of_primes=[]
    for num_1 in range(2,)



def sum_all(*args):
    sum_1=0
    for i in args:
        sum_1+=i
    return sum_1

print("Sum:",sum_all(1,2,3,4))
import math


    def get_area(shape):
        shape=shape.lower()
        if shape=="rectangle":
            rectangle_area()
        elif shape=="circle":
            circle_area()
        else:
            print("Please enter rectangle or circle")

    def rectangle_area():
        length=float(input("Enter the length"))
        width=float(input("Enter the width"))
        area=length*width
        print("The area of the rectangle is",area)

    def circle_area():
        radius=float(input("Enter the radius:"))
        area=math.pi*(math.pow(radius,2))
        print("The area of the cirlce is{:.2f}".format(area))

    def main():
        shape_type=input("Get area for what shape:")
        get_area(shape_type)

    main()

def is_prime():
    value=int(input("Enter the  number:"))
    for i in range(2,value):
        if(value%i)==0:
            return False
    return True
    
print(is_prime())

rand_list=["string",1.234,28]
one_to_ten=list(range(11))
rand_list=rand_list+one_to_ten
print(rand_list[0])
print("List length",len(rand_list))
first_3=rand_list[0:3]
print(first_3)

for i in first_3:
    print("{}:{}".format(first_3.index(i),i))
print(first_3[0]*3)
print("string" in first_3)


print("Index of string",first_3.index("string"))

import random
num_list=[]
for i in range(5):
    num_list.append(random.randrange(1,9))

i=len(num_list)-1
while i>1:
    j=0
    while j<i:
        print("\nIs {}>{}".format(num_list[j])

my_list=[5,2,9,1]
total=0
for i in my_list:
    if i==2:
        total+=1
print(total)
        

import math
even_list=[i*2 for i in range(10)]
for k in even_list:
    print(k,end=",")
print()
import math
num_list=[1,2,3,4,5]
list_of_values=[[math.pow(m,2),math.pow(m,3),math.pow(m,4)] for m in num_list]
for k in list_of_values:
    print(k)
print()


mult_d_list=[[0]*10 for i in range(10)]
print(mult_d_list)

for i in range(10):
    for j in range(10):
        mult_d_list[i][j]="{}:{}".format(i,j)
print(mult_d_list)

for i in range(10):
    for j in range(10):
        print(mult_d_list[i][j],end="||")
        print()

mult_table=[[0]*10 for i in range(10)]
for i in range(1,10):
    for j in range(1,10):
        mult_table[i][j]=i*j


derek_dict={"f_name":"Derek","l_name":"Banas","address":"123 Main St"}
print(derek_dict)

print("My Name:",derek_dict["f_name"])
derek_dict["address"]="215 North St"
derek_dict["city"]="Pittsburgh"
print("Is there a city:","city" in derek_dict)
print(derek_dict.values())
print(derek_dict.keys())



derek_dict={"f_name":"Derek","l_name":"Banas","address":"123 Main St"}
for k,v in derek_dict.items():
    print(k,v)

derek_dict={"f_name":"Derek","l_name":"Banas","address":"123 Main St"}
print(derek_dict.get("m_name","Not Here"))
del derek_dict["f_name"]
print(derek_dict)

employees=[]
f_name,l_name=input("Enter Employee Name: ").split()
employees.append({"f_name":f_name,"l_name":l_name})
print(employees)

customers=[]
while True:
    create_entry=input("Enter Customer(Yes/No):")
    create_entry=create_entry[0].lower()
    if create_entry=="n":
        break
    else:
        f_name,l_name=input("Enter customer name: :").split()
        customers.append({"f_name":f_name,"l_name":l_name})

for cust in customers:
    print(cust['f_name'],cust['l_name'])

def factorial(num):
    if num<=1:
        return 1
    else:
        result=num*factorial(num-1)
        return result
print(factorial(4))

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        result=fib(n-1)+fib(n-2)
        return result


num_fib_vals=int(input("How many Fibonacci values should be found: "))
i=1
while i<num_fib_vals:
    fib_value=fib(i)
    print(fib_value)
    i+=1
 import OSError
 with open("mydata.txt",mode="w",encoding="utf=8") 
 as my_file:
     myFile.write("Some random text/nMore random text\nAnd some more")
with open("mydata.txt",encoding="utf-8")
as my_file:
print

class Dog:
    def __init__(self,name="",height=0,weight=0):
        self.name=name
        self.height=height
        self.weight=weight
    
    def run(self):
        print("{} the dog runs".format(self.name))
    def eat(self):
        print("{} the dog eats".format(self.name))
    def bark(self):
        print("{} the dog barks".format(self.name))

def main():
    spot=Dog("Spot",66,26)
    spot.bark()
main()


class Square:
    def __init__(self,height="0",width="0"):
        self.height=height
        self.width=width
    @property
    def height(self):
        print("Retrieving the height")
        return (self.__height)
    @height.setter
    def height(self,value):
        if value.isdigit():
            self.__height=value
        else:
            print("Please only enter numbers for height")
    @property
    def width(self):
        print("Retrieving the width")
        return self.__width

    @width.setter
    def width(self,value):
        if value.isdigit():
            self.__width=value
        else:
            print("Please only enter numbers for height")
    def get_area(self):
        return int(self.__width)* int(self.__height)


def main():
    square=Square()
    height=input("Enter Height:")
    width=input("Enter width:")
    square.height=height
    square.width=width
    print("Height :",square.height)
    print("Width:",square.width)
    print("The area is:",square.get_area())

main()


import random 
import math

class Warrior:
    def __init__(self,name="Warrior",health=0,attk_max=0,block_max=0):
        self.name=name
        self.health=health
        self.attk_max=attk_max
        self.block_max=block_max

    def attack(self):
        attk_amt=self.attk_max*(random.random()+.5)
        return attk_amt
    def block(self):
        block_amt=self.block_max*(random.random()+.5)
        return block_amt

class Battle:
    def start_fight(self,warrior1,warrior2):
        while True:
            if self.get_attack_result(warrior1,warrior2)=="Game Over":
                break
            if self.get_attack_result(warrior2,warrior1)=="Game Over":
                break
    def get_attack_result(self,warriorA,warriorB):
        warrior_a_attk_amt=warriorA.attack()
        warrior_b_block_amt=warriorB.block()
        damage_2_warrior_b=math.ceil(warrior_a_attk_amt-warrior_b_block_amt)
        warriorB.health=warriorB.health-damage_2_warrior_b
        print("{} attacks{} and deals{} damage".format(warriorA.name,warriorB.name,damage_2_warrior_b))
        print("{} is down to {} health".format(warriorB.name,warriorB.health))
        if warriorB.health<=0:
            print("{} has died and {} is Victorious".format(warriorB.name,warriorA.name))
            return "Game Over"
        else:
            return "Fight Again"

def main():
    thor=Warrior("Thor",50,20,10)
    loki=Warrior("Loki",50,20,10)
    battle=Battle()
    battle.start_fight(thor,loki)

main()

class Animal:
    def __init__(self,birth_type="Unknown",appearance="Unknown",blooded="Unknown"):
        self._birth_type=birth_type
        self._appearance=appearance
        self._blooded=blooded

    @property
    def birth_type(self):
        return self._birth_type
    @birth_type.setter
    def birth_type(self,birth_type):
        self._birth_type=birth_type
    
    
    @property
    def appearance(self):
        return self._appearance
    @appearance.setter
    def appearance(self,appearance):
        self._appearance=appearance
    
    @property
    def blooded(self):
        return self._blooded
    @blooded.setter
    def blooded(self,blooded):
        self._blooded=blooded
    
    def __str__(self):
        return "A {} is {} it is {} it is {}".format(
            type(self).__name__,self.birth_type,self.appearance,self.blooded)

class Mammal(Animal):
    def __init__(self,birth_type="born alive",appearance="hair or fur",blooded="warm blood",nurse_young=True):
        Animal.__init__(self,birth_type,appearance,blooded)
        self._nurse_young=nurse_young


    @property
    def nurse_young(self):
        return self._nurse_young
    @nurse_young.setter
    def nurse_young(self,nurse_young):
        self._nurse_young=nurse_young

    def __str__(self):
        return super().__str__() + " and it is {} they nurse their young".format(self.nurse_young)
    

class Reptile(Animal):
    def __init__(self,birth_type="born in an egg or born alive",appearance="dry scales",blooded="cold blooded"):
        Animal.__init__(self,birth_type,appearance,blooded)

def main():
    animal1=Animal("born alive")
    print(animal1.birth_type)
    print(animal1)
    mammal1=Mammal()
    print(mammal1)
    print(mammal1.birth_type)
    print(mammal1.appearance)
    print(mammal1.blooded)
    print(mammal1.nurse_young)
    print()
main()







class Time:
    def __init__(self,hour=0,minute=0,second=0):
        self.hour=hour
        self.minute=minute
        self.second=second
    
    def __str__(self):
        return "{}:{:02d}:{:02d}".format(self.hour,self.minute,self.second)
    
    def __add__(self,other_time):
        new_time=Time()
        if(self.second+other_time.second)>=60:
            self.minute+=1
            new_time.second=(self.second+other_time.second)-60
        else:
            new_time.second=self.second+other_time.second
        
        if(self.minute+other_time.minute)>=60:
            self.hour+=1
            new_time.minute=(self.minute+other_time.minute)-60
        else:
            new_time.minute=self.minute+other_time.minute

        if(self.hour+other_time.hour)>=24:
               new_time.hour=(self.hour+other_time.hour)-24
            
        else:
            new_time.hour=self.hour+other_time.hour

        return new_time

def main():
    time1=Time(1,20,30)
    print(time1)
    time2=Time(24,41,30)
    print(time1+time2)

main()

class Sum:
    @staticmethod
    def get_sum(*args):
        sum_1=0
        for i in args:
            sum_1+=i
        return sum_1

def main():
    print ("Sum :",Sum.get_sum(1,2,3,4,5))

main()

class Dog:
    num_of_dogs=0
    
    def __init__(self,name="Unknown"):
        self.name=name 
        Dog.num_of_dogs+=1
    @staticmethod

    def get_num_of_dogs():
        print("There are currently {} dogs".format(Dog.num_of_dogs))

def main():
    spot=Dog("Spot")
    doug=Dog("Doug")
    spot.get_num_of_dogs()

main()

class DogNameError(Exception):
    def __init__(self,*args,**kwargs):
        Exception.__init__(self,*args,**kwargs)
try:
    dog_name=input("What is your dogs name: ")

    if any(char.isdigit() for char in dog_name):
        raise DogNameError
except DogNameError:
    print("Your dogs name can't contain a number")
    
num1,num2=input("Enter two values to divide:").split()
try:
    quotient=int(num1)/int(num2)
    print("{}/{}={}".format(num1,num2,quotient))


try:
    my_file=open("mydata3.txt",encoding="utf-8")

except FileNotFoundError as ex:
    print("That file was not found")
    print(ex.args)
else:
    print("File :",my_file.read())
    my_file.close()
finally:
    print("Finished Working with File")

def mult_by_2(num):
    return num*2

time_two=mult_by_2
print("4*2=",time_two(4)
)
    


def do_math(func,num):
    return func(num)

print("8*2=",do_math(mult_by_2,2))



time_two=mult_by_2
print("4*2=",time_two(4)
)

def get_func_mult_by_num(num):
    def mult_by(value):
        return num*value
    return mult_by
generated_func=get_func_mult_by_num(5)
print("5*9=",generated_func(9))



list_of_func=[time_two,generated_func]
print("5*9=",list_of_funcs[1][9])




def is_it_odd(num):
    if num%2==0:
        return False
    else:
        return True





def mult_by_2(num):
    return num*2

time_two=mult_by_2
print("4*2=",time_two(4))

def do_math(func,num):
    return func(num)

print("8*2=",do_math(mult_by_2,8))


def get_func_mult_by_num(num):
    def mult_by(value):
        return num*value
    return mult_by

generated_func=get_func_mult_by_num(5)
print("5*9=",generated_func(9))

list_of_funcs=[time_two,generated_func]

print("5*9=",list_of_funcs[1](9))


def is_it_odd(num):
    if num%2==0:
        return False
    else:
        return True

def change_list(list,func):
    odd_list=[]
    for i in list:
        if func(i):
            odd_list.append(i)
    return odd_list

a_list=range(1,20)
print(change_list(a_list,is_it_odd))


def random_func(name:str,age:int,weight:float)->str:
    print("Name:",name)
    print("Age:",age)
    print("Weight:",weight)
    return "{} is {} years old and weighs {}".format(name,age,weight)
print(random_func("Derek",41,165.1))

    

sum_1=lambda x,y:x+y
print("Sum:",sum_1(4,5)

can_vote=lambda age: True if age>=18 else False
print("Can Vote:",can_vote(16))


power_list=[lambda x: x**2,
            lambda x:x**3,
            lambda x:x**4
]

for func in power_list:
    print(func(4))

attack={'quick':(lambda:print("Quick Attack")),
        'power':(lambda:print("PowerAttack")),
        "miss":(lambda:print("The Attack Missed"))
}

attack['quick']()

import random
attack_key=random.choice(list(attack.keys()))
attack[attack_key]()

import random
flip_list=[]
for i in range(1,101):
    flip_list+=random.choice(['H','T'])

print("Head:",flip_list.count('H'))
print("Tails:",flip_list.count('T'))

one_to_10=range(1,11)
def dbl_num(num):
    return num*2

print(list(map(dbl_num,one_to_10)))
print(list(map((lambda x:x*3),one_to_10)))

a_list=list(map((lambda x,y:x+y),[1,2,3],[1,2,3]))

print(a_list)

import random
rand_list=list(random.randint(1,1001) for i in range(100))
print(rand_list)
print(list(filter((lambda x:x%9==0),rand_list)))


class Alphabet:
    def __init__(self):
        self.letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.index=-1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index>=len(self.letters)-1:
            raise StopIteration
        self.index+=1
        return self.letters[self.index]
    
alpha=Alphabet()

for letter in alpha:
    print(letter)


derek={"f_name":"Derek","l_name":"Banas"}


for key in derek:
    print(key,derek[key])


class Fib_Generator:
    def __init__(self):
        self.first=0
        self.second=1
    def __iter__(self):
        return self

    def __next__(self):
        fib_num=self.first+self.second
        self.first=self.second
        self.second=fib_num
        return fib_num

fib_seq=Fib_Generator()

for i in range(10):
    print("Fib:",next(fib_seq))    

print(list(map((lambda x:x*2),range(1,11))))

print([2*x for x in range(1,11)])

print(list(filter((lambda x: x%2!=0),range(1,11))))

print([x for x  in range(1,11) if x%2!=0])

print([i**2 for i in range(50) if i%8==0])

print([x*y for x in range(1,3) for y in range(11,16)])

print([x for x in [i*2 for i in range(10)] if x%8==0])

import random

print([x for x in [random.randint(1,1001) for i in range(50)] if x%9==0])


multi_list=[[1,2,3],[4,5,6],[7,8,9]]

print([col[1] for col in multi_list])

print([multi_list[i][i] for i in range(len(multi_list))])

def is_prime(num):
    for i in range(2,num):
        if num%i==0:
            return False
        return True
def gen_prime(max_number):
    for num1 in range(2,max_number):
        if is_prime(num1):
            yield num1

prime=gen_prime(50)

print("Prime:",next(prime))
print("Prime:",next(prime))

print("Prime:",next(prime))
print("Prime:",next(prime))

double=(x*2 for x in range(10))
print("Double:",next(double))
print("Double:",next(double))

for num in double:
    print(num)

import threading
import time
import random

def execute_thread(i):
    print("Thread {} sleeps at {}".format(i,time.strftime("%H:%M:%S",time.gmtime())))
    rand_sleep_time=random.randint(1,4)
    time.sleep(rand_sleep_time)
    print("Thread {} stops sleeping at {}".format(i,time.strftime("%H:%M:%S",time.gntime())))

for i in range(10):
    thread=threading.Thread(
    target=execute_thread,args=(i,))
    thread.start()

    print("Active Threds:",threading.activeCount())
    print("Thread Objects:",threading.enumerate())


import threading 
import time 
import random

import re 
all_apes=re.findall("ape","The ape was at the apex")
for i in all_apes:
    print(i)

import re 
the_str="The ape was at the apex"
for i in re.finditer("ape.",the_str):
    loc_tuple=i.span()
    print(loc_tuple)
    print(the_str[loc_tuple[0]:loc_tuple[1]])

import re

animal_str="Cat rat mat fat pat"
some_animals=re.findall("[crmfp]at",animal_str)

for i in some_animals:
    print(i)


import re

animal_str="Cat rat mat fat pat"

some_animals=re.findall("[c-mC-M]at",
    animal_str)

for i in some_animals:
    print(i)

import re
owl_food="rat cat mat pat"
regex=re.compile("[cr]at")
owl_food=regex.sub("owl",owl_food)
print(owl_food)



import re
rand_str="Here is \\stuff"

print("Find \\stuff:",re.search("\\stuff",rand_str))


import re
rand_str="F.B.I. I.R.S. CIA"
print("Matches :",len(re.findall(".\..\..",rand_str)))

import re
rand_str="""This is a long string that goes on for many lines"""

print(rand_str)
regex=re.compile("\n")
rand_str=regex.sub(" ",rand_str)
print(rand_str)

import re
rand_str="12345"
if re.search("\d{5}",rand_str):
    print("It is a zip code")

import re
rand_str="123 12345 123456 1234567"
print("MatchesZ:",len(re.findall("\d{5,7}",rand_str)))

import re
ph.num="412-555-1212"

if re.search("w{2,20}"\s\w{2,20}","Toshio Muramatsu"):
    print("It is a valid name")


import re
print("Matches:",len(re.findall("a+","a as ape bug")))

email_list="db@aol.com m@"

import re

rand_str="cat cats"
regex=re.compile("[cat]+s?")
matches=re.findall(regex,rand_str)
for i in matches:
    print(i)

import re
rand_str="doctor doctors doctor's"
regex=re.compile("[doctor]+['s]*")
matches=re.findall(regex,rand_str)
print("Matches:",len(matches))

import re
long_str="""Just some words and some more and more"""

print("Matches:",len(re.findall(r"[\w\s]+[\r]?\n",long_str)))

matches=re.findall("[\w\s]+\r]?\n",long_str)

for i in matches:
    print(i)

import re

rand_str="<name>Life On Mars</name><name>Freaks and Geeks</name>"
regex=re.compile(r"<name>.*?</name>")
matches=re.findall(regex,rand_str)

print("Matches:",len(matches))
for i in matches:
    print(i)


import re
rand_str="ape at the apex"
regex=re.compile(r"ape")
regex_2=re.compile(r"\bape\b")
matches=re.findall(regex,rand_str)
matches_2=re.findall(regex_2,rand_str)
print("Matches 1:",len(matches))
print("Matches 2:",len(matches_2))

import re
rand_str="cat cats"
regex=re.compile("[cat]+s?")
matches=re.findall(regex,rand_str)
for i in matches:
    print(i)


import re
rand_str="doctor doctors doctor's"
regex=re.compile("doctor]+['s]*")
matches=re.findall(regex,rand_str)
print("Matches:",len(matches))


import re
long_str="""Just some words and some mor and more"""

print("Matches:",len(re.findall(r"[\w\s"]+[\r]?\n",long_str)))
matches=re.findall("[")


import re
rand_str="<name>Life on Mars</name><name>Freaks and Geeks</name>"
regex=re.compile(r"<name>.*?</name>")
matches=re.findall(regex,rand_str)
print("Matches:",len(matches))
for i in matches:
    print(i)



import re
rand_str="ape at the apex"
regex=re.compile(r"ape")
regex_2=re.compile(r"\bape\b")
matches=re.findall(regex,rand_str)
matches_2=re.findall(regex_2,rand_str)
print("Matches 1:",len(matches))
print("Matches 2:",len(matches_2))


import re
rand_str="Matches everything up to @"
regex=re.compile(r"^.*[^@]")

rand_str="""Ape is big 
Turtle is slow
 Cheetah is fast"""
regex=re.compile(r"(?m)^.*?\s")
matches=re.findall(regex,rand_str)
print("Matches:",len(matches))
for i in matches:
    print(i)

import re
rand_str="My number is 412-555-1212"
regex=re.compile(r"412-(.*)")
matches=re.findall(regex,rand_str)
print("Matches:",len(matches))
for i in matches:
    print(i)

import re
rand_str="412-555-1212 412-555-1213 412-555-1214"
regex=re.compile(r"412-(.*)")
matches=re.findall(regex,rand_str)
print("Matches :",len(matches))
for i in matches:
    print(i)


import re
rand_str="The cat cat fell out the window"
regex=re.compile(r"(\b\w+)\s+\1")
matches=re.findall(regex,rand_str)
print("Matches:",len(matches))
for i in matches:
    print(i)
    