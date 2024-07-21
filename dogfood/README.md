# Mathematical modeling of Allocate dog food problem
1.	Yian Wang 2. Zhenxuan Gao 3. Ziyuan Wang
1.WLSA Shanghai Academy 2. 3.
 
Table of Contents
1.Introduction
1.1	Introduction of dog food
1.2	Composition of dog food
1.3	Why I choose this topic
2.Problem description

3.model establishment
3.1 Determine decision variables
3.2 Set
3.3 Develop an objective function
3.4 Determine the constraints
4.Discussion

5.Conclusion

6.Evaluation

7.Bibliography

 

## Introduction
### 1.1 Introduction of dog food
Dog food is a nutritious food specially provided for dogs, which is a high-grade animal food between human food and traditional livestock and poultry feed. Its function mainly provides animals and dogs the most basic life guarantee, growth, and health nutrients. It has the advantages of comprehensive nutrition, high digestion, and absorption rate, scientific formula, quality standard, convenient feeding, and prevention of some diseases. It can be roughly divided into two categories: puffed grain and steamed grain.

### 1.2 Composition of dog food
The main nutritional components of dog food include protein, fat, carbohydrates, minerals, vitamins, and water.
#### 1.2.1. carbohydrates
Carbohydrate is the main source of energy needed by pets. Pets need a lot of energy to ensure their physical survival, health, development, reproduction, heart beating, blood circulation, gastrointestinal peristalsis, muscle contraction, and other activities, and 80% of this required energy is provided by carbohydrates. Carbohydrates include sugar and fiber. The daily carbohydrate requirement of adult dogs is 10 grams per kilogram of body weight, and that of puppies is about 15.8 grams per kilogram.
#### 1.2.2. protein
Protein is an important source of body tissues and somatic cells of pets, and protein has many functions, such as conduction, transportation, support, protection, and exercise. Protein also plays a catalytic and regulatory role in pets' life and physiological metabolism activities and plays a major role in maintaining life activities.
#### 1.2.3. Fat
Fat is an important component of pet body tissue, which participates in almost all cell composition and repair, and contains fat in pet skin, bones, muscles, nerves, blood, and internal organs. The proportion of fat in pet dogs is as high as 10 ~ 20% of their weight.
Fat is the most important energy source.
#### 1.2.4. Minerals
Minerals are another kind of indispensable nutrient for pet dogs, including elements needed by the human body, such as calcium, phosphorus, zinc, copper, magnesium, potassium, and iron. Minerals are important raw materials for the collective organization of pet dogs, which help to regulate the acid-base balance, muscle contraction, and nerve reaction in the body.
#### 1.2.5. vitamins
Vitamins are low-molecular-weight organic compounds that are necessary for the metabolism of pets' physiques and require little. Generally, they can't be synthesized in the body, and they mainly depend on the provision of pet food and dog food. Except for a few vitamins, most of them require extra addition to dog food. They do not provide energy, nor are they the structural components of the body, but they are indispensable in the diet. For example, a long-term lack or deficiency of a certain vitamin can cause metabolic disorder and a pathological state to form vitamin deficiency.
### 1.3 Why I choose this topic
One of the reasons why I chose this project is because I am studying math modeling and I want to solve this problem in this way.

Low-priced dog food can reduce the economic burden of pet owners and facilitate the provision of high-quality food for pets. Although cheap, dog food provides essential nutrients for pets, including protein, carbohydrates, fats, vitamins and minerals. This kind of dog food generally uses easily available ingredients, and the manufacturing method is relatively simple, so it can be made at home. By controlling the ingredients and production technology, it can be ensured that the dog food does not contain harmful substances and additives, which is beneficial to the health and happiness of pets. If someone wants to do such a project, they may try to ensure the quality and nutritional value of dog food while controlling the cost, so as to provide reliable choices for pet owners.

## 2.Problem description:
Tom wants to produce their dog food products at the lowest possible cost, while ensuring that they meet the nutritional analysis requirements shown on the cans. The ingredients of dog food are Chicken Liver, Beef, Carrot, Corn Flower, Dried Vegetables and protein powder, and their costs are shown in the table. To meet the nutritional standards, every 100g of finished product must have at least 8g Protein, 6g fat and 2g of fiber, but not more than 0.4g of salt. The following is a table of nutrients.
 
## 3.Modeling representation:
In order to make it easier to change the data in other tests, we will define the problem in algebraic form.

Pulp is a Python library for linear programming (LP), integer linear programming (ILP) and mixed integer linear programming (MILP). The full name of Pulp is "Python for Mathematical Programming", which provides a simple and powerful tool for users to define optimization problems, build mathematical models and solve them with different solvers. 

One of the main characteristics of Pulp is its ease of use. It allows users to define optimization problems in a simple way without having to know the details of mathematical planning in depth. The grammatical design of Pulp aims to enable users to express the constraints and objective functions of the problem intuitively. This concise and clear grammar makes Pulp an ideal choice for solving linear programming problems, especially for those users who are not familiar with the field of mathematical programming. In Pulp, users can easily define variables, constraints and objective functions. 

Through simple API calls, users can specify the upper and lower bounds of variables, the coefficients of constraints and the coefficients of objective functions. Pulp also provides inspection and display of problem characteristics to help users verify the correctness of the model. The use of Pulp is not limited to linear programming, but also can deal with integer linear programming and mixed integer linear programming.

### 3.1 Determine decision variables:
The decision variable is the percentage of different ingredients we contain in dog food cans. Since the jar weighs 100 grams, these percentages also represent grams of each ingredient. Please note that these percentages must be between 0 and 100.

### 3.2 Set:
Y1y_1y1 = the percentage of Carrot in a can of dog food.
Y2y_2y2 = the percentage of Protein powder in a can of dog food.
Y3y_3y3 = the percentage of Corn flour in a can of dog food.
Y4y_4y4 = the percentage of Chicken liver in a can of dog food.
Y5y_5y5 = percentage of Dried vegetables in a can of dog food.
Y6y_6y6 = the percentage of Beef in a can of dog food.

### 3.3 Develop an objective function:
For our dog food formula, the goal is to minimize the total cost of each can of dog food ingredients. The cost function is:
minimize 0.060y1+0.200y2+0.050y3+0.130y4+0.130y5+0.150y6

### 3.4 Determine the constraints:
The constraint conditions of dog food formula include two aspects:
1. The total percentage of each component must be 100%.
2. Meet the prescribed nutritional requirements.
First, the total amount of components is constrained as follows:
y1+y2+y3+y4+y5+y6=100
To meet the nutritional requirements, every 100 grams of dog food must contain at least 8 grams of protein, 6 grams of fat, but not more than 2 grams of fiber and 0.4 grams of salt. According to the nutritional contribution of each component, we can formulate the following constraints:
Protein constraint:
0.040y1+0.300y2+0.100y3+0.150y4+0.001y5+0.200y6≥8.0
Fat constraint:
0.001y1+0.020y2+0.002y3+0.070y4+0.005y5+0.100y6≥6.0
Fiber constraint:
0.200y1+0.050y2+0.400y3+0.002y4+0.700y5+0.004y6≤2.0
Salt constraint:
0.002y1+0.005y2+0.006y3+0.001y4+0.010y5+0.005y6≤0.4

Through these constraints and objective functions, we can construct a linear programming model to optimize the formula of dog food. The advantage of linear programming is that it can accurately balance the relationship between nutritional requirements and production costs by mathematical methods. In the process of dog food production, different raw materials and ratios directly affect the nutritional value and cost-effectiveness of the products. Therefore, the use of linear programming model can ensure that dog food can meet the nutritional needs and reduce the production cost as much as possible.

This model can also be flexibly adjusted according to market demand and production conditions, which provides a powerful optimization scheme for production strategy. With the change of market environment, consumers' preference for dog food may also change constantly, so adjusting the formula is the key to maintain the competitiveness of products. The linear programming model can keep the product quality and adjust according to the real-time data, so as to ensure the efficient operation of the production line and the optimal utilization of resources.

In addition, linear programming can also help to make production plans and optimize the procurement of raw materials and production schedule. Through the precise control of the production process, the waste of resources and the idle time of the production line can be effectively reduced, thus improving the overall production efficiency and cost-effectiveness.

In a word, optimizing the formula of dog food by linear programming model can not only ensure the nutritional balance of products and effectively control the production cost, but also flexibly respond to the dynamic changes of market demand and production conditions, which provides scientific basis and operational guidance for the formulation and implementation of production strategies.


## 4. Discussion
We use the pulp package in python to solve the above linear programming model. 

According to the solution results of the model, we can get：
Welcome to the CBC MILP Solver 
Version: 2.10.3 
Build Date: Dec 15 2019 

command line - /Users/wangyian/Library/Python/3.12/lib/python/site-packages/pulp/solverdir/cbc/osx/64/cbc /var/folders/wy/1czbpv6934df0bjtwyqwp1500000gn/T/51575b5ef25c46aab980a1b87a3b371c-pulp.mps -timeMode elapsed -branch -printingOptions all -solution /var/folders/wy/1czbpv6934df0bjtwyqwp1500000gn/T/51575b5ef25c46aab980a1b87a3b371c-pulp.sol (default strategy 1)
At line 2 NAME          MODEL
At line 3 ROWS
At line 10 COLUMNS
At line 41 RHS
At line 47 BOUNDS
At line 48 ENDATA
Problem MODEL has 5 rows, 5 columns and 25 elements
Coin0008I MODEL read with 0 errors
Option for timeMode changed from cpu to elapsed
Presolve 5 (0) rows, 5 (0) columns and 25 (0) elements
0  Obj 0 Primal inf 207.14286 (4)
3  Obj 11265.403
Optimal - objective value 11265.403
Optimal objective 11265.40284 - 3 iterations time 0.002
Option for printingOptions changed from normal to all
Total time (CPU seconds):       0.00   (Wallclock seconds):       0.00

Status: Optimal
Ingr_BEEF = 36.492891
Ingr_CARROT = 0.0
Ingr_CHICKEN_LIVER = 32.701422
Ingr_CORN_FLOUR = 30.805687
Ingr_DRIED_VEGETABLES = 0.0

## 5. Conclusion
Low-priced dog food can reduce the economic burden of pet owners and facilitate the provision of high-quality food for pets. Although cheap, dog food provides essential nutrients for pets, including protein, carbohydrates, fats, vitamins and minerals. This kind of dog food generally uses easily available ingredients, and the manufacturing method is relatively simple, so it can be made at home. By controlling the ingredients and production technology, it can be ensured that the dog food does not contain harmful substances and additives, which is beneficial to the health and happiness of pets. If someone wants to do such a project, they may try to ensure the quality and nutritional value of dog food while controlling the cost, so as to provide reliable choices for pet owners.

## 6. Evaluation
In this project, our team chose to use programming technology to reduce the cost of dog food, and we encountered many problems and challenges in the process. For example, the programming code frequently makes errors and does not know how to set variables. I gained a lot of experience through this experience. In the future, you should do more checking after writing code, and you can validate variables more easily. And the confusion of choosing ingredients for dog food. The division of labor between the three people is not very clear, resulting in a slow progress. I think these are all tests for us. After going through this mathematical modeling project, the three of us not only gained academic improvement, but also gained experience in dealing with different challenges.
We learned a lot from doing this project, such as how to manage our time well, skills in writing, how to write source evaluations, and so on. 
In the next project, we will do differently because we have learned how to do this kind of project and we wonder how to do different projects. 
The experience of doing this project brings many advantages to us and they will be helpful in our future life. 

## 7. Bibliography

1. PMO and Project Management Dictionary [PMO与项目管理词典]. Pmhut.com. 2007-08-20. 
2. CEITON technologies "Manual planning",  Ceiton technologies Retrieved on 3 June 2014
3. Production planning "Algorithmic sequencing", Production planning Retrieved on 3 June 2014
4. Inteng "Planning manual and algorithm" , Inteng Retrieved on 3 June 2014
5. Samuel90. Resource allocation [资源分配], Slideshare.net. 2013-01-25 .
6. Wireless Channel Allocation Using An Auction Algorithm [以拍卖算法分配无线信道] (PDF). 
7. Tycoon: A Distributed Market-based Resource Allocation System [Tycoon：以市场为本的分散式资源分配系统], Citeulike.org. 2014-06-24. 
