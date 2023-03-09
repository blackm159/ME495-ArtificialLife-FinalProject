# **ME495-Assignment8**
 
## **Information**
#### 
The goal of this assignment is to grow and evolve a creature with randomized links.

Leg links are grown from a "torso" link on each side face.  Each leg can have 0 to 4 links, growing either downward or outward to the side.  Between 1 and 5 "torsos" are created.

Joints are centered on the face of attachment.  Each joint has a randomized axis of rotation.  Each joint is motorized.

<p align="center">
    <img src="./TorsoFigure.jpg" width="40%" height="40%"/>
</p>

This figure shows how torso vertebrae are grown and include an outward leg on 0 to 2 side faces.  Starting at the origin, a random number of vertebrae are grown in the +x direction.

<p align="center">
    <img src="./LegFigure.jpg" width="45%" height="45%"/>
</p>

This figure shows how leg links are grown outward (+/-y direction) and downward (-z direction).  Quantity, growth direction, and axis of rotation are chosen randomly for each link.

 A random number of links between 3 and the total number of links are sensorized.  These links are represented with green.  Links without sensors are blue.

 A random link is chosen and its sensor status is flipped during evolution.  If that link is originally sensorized, it will no longer have a sensor.  Link color is updated to reflect this change.  If the link is added to the sensor list, weight contributions to motor motion is randomly generated.

Motor neurons react based on random weights of sensor neurons.  During evolution, 1 randomly chosen weight is changed.  

The joint axis for 1 joint is randomly changed each generation.

Fitness for these creatures is determined by the largest distance in the -y direction.

<p align="center">
    <img src="./FitnessPlot.png" width="100%" height="100%"/>
</p>

This figure shows how the fitness changes with each generation for 5 random seeds.  Evolution examined a population size of 10 for 100 generations.


[Video example including several creatures](https://youtu.be/YYA4Wkm1kpI) 



 

## **How to run**
#### 
1) Clone this repository
2) Install [pybullet](https://pybullet.org/wordpress/).  More information on getting started avaiable at the [Ludobots MOOC Installation](https://www.reddit.com/r/ludobots/wiki/installation/) page 
3) Navigate to this repository in command prompt
4) Run ```py mainTemp.py```


## **Sources**
#### 
- This project is a part of ME495 Artificial Life at Northwestern University.
- This course uses the [Ludobots MOOC](https://www.reddit.com/r/ludobots/) for coding projects