# Using this as a starting point for my RoboDK project and Gen AI project as well 
# Mainly Object Oriented Programming
import random
from datetime import date
from enum import Enum
#Todo Add testing to confirm the number of joints and links are valid
#Todo Testing if the Payload is not out of max range
#Todo Calculation of Fkine in on separate thread
#Todo Calculation of IKine is on Separate Thread


class Robot:

    cloud_dir = 'amazon/bitbucket'
    count = 0
    curr_count = 0
    def __init__(self, name,  joints, links, Payload, weights, model_file=None):

        self.name = name
        self.joints = joints
        self.links = links
        self.Payload = Payload
        self.model_file = model_file
        
        self.robo_weigh = sum(weights)

        # Payload: int
        # Joint: list
        # Links: list
        # model_file:str #Simulation path
    #Additional Constructors, currently not blowing it up keeping it simple
    @classmethod
    def from_existing_or_create(cls,):



Class ENUM( )

    def current_joint_values(self):
        print("running")

        self.joints = [joint + random.randrange(-30,30) for joint in self.joints]
            # print(f" joint is :" ,joint )
        #Get currrent Time and enum with the Joint values



    def get_joint_values(self):

        # Send a request to the Terminal of Robot to get the joinnt values
        self.current_joint_values()
        for i in range(len(self.joints)):
            print(f" J{[i]} : {self.joints[i]} \n")

    def get_cartesian_values(self):
        pass

    def get_gripper_state(self):
        pass

        

Fanuc = Robot(name="AXL100", joints=[30,30,20,90,10,20], links=[10,20,20,30,40,10], Payload=350,weights= {10,20,30,1,2,3})
# ABB = Robot(name="AXL100",joints=[30,30,20,90,10,20], links=[10,20,20,30,40,10], Payload=300,weights)




######################### Learnings

# Don't want to initialize varibales all the time, 10 different robotics automation companies
# Thus we create __Init__init method

# if for example you change some functionality in the class let's say, 


# Data and Functions
# Attributese and Methods

#decorators are @classmethods

