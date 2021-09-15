''' 
    This is simple example program for solve problem by Black Hole Optimization Algorithm (BH) 
    Author: Mr.Chanon Sattrupinat
    Date  : 2021/9/15
'''
import random as rd
import numpy as np

#SET GLOBAL VARIABLES
n=300;
iteration=150;
Upper_x1=50;
Upper_x2=50;
Lower_x1=-50;
Lower_x2=-50;
delta_x1=Upper_x1-Lower_x1;
delta_x2=Upper_x2-Lower_x2;

#SET CONSTANT
positions=np.array([[]]);
velocity=np.array([[]]); 
Black_hole=np.array([[]]); 
New_positions=np.array([[]]);
index_Black_hole=0;
rad_event=0;

# SET OBJECTIVE FUNCTION
def Objective_function(x1,x2):
  obj_point=((((x1)**2)+x2-11)**2)+((x1+(x2**2)-7)**2)#(x1**2)+(x2**2)
  return obj_point


# GENERATION INITIAL SOLUTIONS 
def Gen_init_solution():
  global n,positions,delta_x1,delta_x2,Lower_x1,Lower_x2
  positions=np.array([[((rd.uniform(0,1))*delta_x1)+Lower_x1,((rd.uniform(0,1))*delta_x2)+Lower_x2]])
  for i in range(n-1):
    p_append=np.array([[((rd.uniform(0,1))*delta_x1)+Lower_x1,((rd.uniform(0,1))*delta_x2)+Lower_x2]])
    positions=np.concatenate((positions,p_append),axis=0)


# FIND Black_hole
def Find_Black_hole():
  global n,positions,Black_hole,index_Black_hole
  point=[]
  for i in range(n):
    point_add=Objective_function(positions[i][0],positions[i][1])
    point.append(point_add)
  index_Black_hole=0
  for j in range(n):
    if point[j] == min(point):
      index_Black_hole=j
  Black_hole=np.array([[positions[index_Black_hole][0],positions[index_Black_hole][1]]])

# CALCULATE NEW POSITION STARS
def Update_position():
  global positions,Black_hole
  c=rd.uniform(0,1)
  positions=(positions)+(c*(Black_hole-positions))

#CALCULATE EVENT HORIZON
def Cal_event_horizon():
  global n,positions,Black_hole,rad_event
  sum_fitness_star=0
  fitness_blackhole=0
  for i in range(n):
    sum_fitness_star=sum_fitness_star+Objective_function(positions[i][0],positions[i][1])
  fitness_blackhole=Objective_function(Black_hole[0][0],Black_hole[0][1])
  rad_event=fitness_blackhole/sum_fitness_star

#STAR COLLAPSING INTO BLACK HOLE
def collap2bh():
  global n,positions,Black_hole,rad_event,delta_x1,delta_x2,Lower_x1,Lower_x2
  for i in range(n):
    dist=np.linalg.norm(Black_hole[0]-positions[i])
    if (dist<=rad_event) and (Black_hole[0][0] != positions[i][0]) and (Black_hole[0][1] != positions[i][1]):
      positions[i][0]=((rd.uniform(0,1))*delta_x1)+Lower_x1
      positions[i][1]=((rd.uniform(0,1))*delta_x2)+Lower_x2

#MAIN
if __name__=='__main__':
    Gen_init_solution()
    for i in range(iteration):
        Find_Black_hole()
        Update_position()
        Cal_event_horizon()
        collap2bh()
        print(Black_hole)