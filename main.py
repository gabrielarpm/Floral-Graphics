"""
Author: Gabriela Ramirez 
Date: February 2022
Class: BTT CS 111

Description: This program shows an image of beautiful random flowers 

It does/does not implement the following features:    
     1. Header: yes   
     2. Meaningful variable and function names: yes 
     3. Documentation: yes 
     4. Functions with parameters: yes    
     5. Seven objects that include randomness: yes    
     Extra credit: yes/no
"""

import turtle    # For turtle graphics
import random    # For random number selection

# The following function draw_petal draws one instance of a petal of a flower. It takes in following things as parameters 
# 1. t => It is the turtle that draws the petal
# 2. angle => It specifies the angle from horizontal(x-axis) of the center of the petal
# 3. size => It specifies the radius of the half-circle that makes up the petal. Higher the size bigger the petal
# 4. theta => It specifies the angle of the half-circle that makes up the petal. Higher the theta rounder the petal
def draw_petal(t,angle,size,theta):
     t.lt(angle-theta/2)
     t.circle(size,theta) # First half of the petal
     t.lt(180-theta)
     t.circle(size,theta) # Second half of the petal
     t.lt(180-angle-theta/2) # Going back to initial angle

# The following function draw_flower draws one instance of a flower. It takes in following things as parameters 
# 1. t => It is the turtle that draws the petal
# 2. center => It specifies the coordinates of the center of the flower 
def draw_flower (t, center):
     t.penup()
     t.goto(center[0],center[1])
     t.pendown()
     color_tuple = (random.random(),random.random(),random.random()) # Random Color of flower is decided here
     t.color(color_tuple)
     petals = random.randint(6,15) # Number of petals are randomly decided here
     init_angle = random.randint(0,90) # Random Initial orientation of the flower is decided here 
     size = random.randint(5,25) # Random size of the flower is decided here
     theta = random.randint(20,70) # Random roundness of the flower petals is decided here
     for i in range(petals):
          for j in range(petals):
               draw_petal(t,init_angle+(360/petals)*i,size*(j+0.5),theta)

random.seed(10) #Setting the seed for consistent results. Change for different image
t = turtle.Turtle()
t.speed(0) # Higher number is faster, except 0 is fastest
flowers = random.randint(7,12) #Deciding the number of flowers to be drawn randomly(currently between 7 to 12)
for i in range(flowers):
     center = [random.randint(-400,400),random.randint(-400,400)] # The random center coordinates are decided here. (Namely, x-coordinate from -400 to 400 and y-coordinate from -400 to 400)
     draw_flower(t,center)
turtle.done()
