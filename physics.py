from random import choice


def area_of_circle():
    radius = float(input('Enter radius'))
    area = 2 * 22/7 * radius
    print(area)

#area_of_circle()

def calculate_velocity():
    distance = float(input('Enter your distance: '))
    time = int(input('Enter your time: '))
    velocity = distance/time
    print(velocity)

#calculate_velocity()

print('Welcome To Physics 101 Class')
print('We answer questions based on the topics: Projectile Motion')
print('(a) Calculate Time of Flight')
print('(b) Calculate Maximum height')
print('(c) Calculate Maximum Horizontal Range')
print('(d) Calculate Horizontal Range ')
print('(e) Calculate Time of Maximum Height')


def a():
    initial_velocity = float(input('Enter your initial velocity'))
    acceleration_due_to_gravity = float(input('Enter your acceleration due to gravity'))
    angle = int(input('Enter your angle'))
    a = 2*initial_velocity*angle/acceleration_due_to_gravity
    print(a)


def b():
    initial_velocity = float(input('Enter your initial velocity'))
    acceleration_due_to_gravity = float(input('Enter your acceleration_due_to_gravity'))
    angle = int(input('Enter your angle'))
    b= initial_velocity*angle/2*acceleration_due_to_gravity
    print(b)


def  c():
    initial_velocity = float(input('Enter your initial velocity'))
    acceleration_due_to_gravity = int(input('Enter your acceleration_due_to_gravity'))
    c= initial_velocity*2/acceleration_due_to_gravity
    print(c)


def d():
    initial_velocity = float(input('Enter your initial_velocity'))
    acceleration_due_to_gravity = float(input('Enter your acceleration_due_to_gravity'))
    angle = int(input('Enter your angle'))
    d = initial_velocity*2*(angle*2)/acceleration_due_to_gravity
    print(d)


def e():
    initial_velocity = float(input('Enter your initial velocity'))
    acceleration_due_to_gravity = float(input('Enter acceleration_due_to_gravity'))
    angle = int(input('Enter your angle'))
    e = initial_velocity*angle/acceleration_due_to_gravity
    print(e)

def main():
    choice  = input("Choose the option on what you want to work on")

    if choice == "a":
        a()

    if choice  == 'b':
        b()

    if choice == 'c':
        c()


    if choice == 'd':
        d()

    if choice == 'e':
        e()

if __name__ == '__main__':
       main()