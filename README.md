# IE 201 – TERM PROJECT – PART 2

 ### GROUP 15

 - AHMET EMRE GOKALP
 - SUDE FILIZ
 - NECDET SINAN PARLAR




### CONTENTS
- BUSTED!
- CLASS DIAGRAM
- USE CASE DIAGRAM
- COLLABORATION DIAGRAMS

### BUSTED!
Drive your vehicle through heavy traffic, avoid hitting obstacles and crashing other cars. Most importantly DON’T GET BUSTED! How long will you last?


Game Controls

- Push "W" and "S" keys to move up or down, respectively.
- Push "J" to use shield.
- Push "K" to use regular bullet.
- Push "L" to use strong bullet.
- Pause the game by pushing "P" key, push "Enter" to resume.
- When the game is over, push "Escape" to exit the game.

Game Dynamics
- Everytime the car hits a road object, it moves backwards (towards the left of the screen) a certain amount. If the car reaches to the left of the screen, thus gets caught by the cops, the game ends.

- There are randomly spawned coins in the road. Coins are collected by driving through them. With these coins you can purchase and use shields, bullets, or strong bullets. If the car hits a big obstacle, all coins will be lost.
	- Shield lets you be immune for a few seconds. You can pass through any road object without getting hurt.
	- Regular bullets let you explode the object in front of you.
	- Strong bullets let you explode all the objects in front of you.

- The speed of the car in the horizontal axis is determined by the system. As time passes away, it gets faster and thus making the game much harder.
- The score is determined by how long can you last without getting caught by the police.

### CLASS DIAGRAM
![](/assets/clasSSDIAGRAMLAST.png )



RoadGame class is the primary class that has aggregation relationships with UserCar, PoliceCar, and RoadObject classes. In this class, the game loop has functions that enable the player to stop/start the game. The total time and score are kept.

We defined a Car class since we have PoliceCar and UserCar classes which share many properties. 

RoadObject is the class that we formed, we determine the coordinates and create the path, and this class is connected to the RoadGame class with its relation to the aggregate. The RoadObject class is inherited by the  Coin, OtherCar, and Obstacle classes. 

We considered two different obstacles. BigObstacle class will inherit from the Obstacle class, while the Obstacle class will inherit the move function from RoadObject class.

Finally, we defined two different bullet types, RegularBullet and StrongBullet. While these will inherit the Bullet class, the Bullet class will use the move function that we will create in the MovingRoadObject class.


### USE-CASE DIAGRAM
![](/assets/use_case_diagram.png)

1. Start:  When the user presses “Enter”, the game starts.
2. Pause: While the user is playing the game, if the key “P” is pressed, the game pauses.
3. Resume: When the user is on the pause screen, if "Enter" is pressed, the game resumes.
4. Move the Car: If the player presses one of the keys that moves the car, the game notifies the car to update the coordinates according to the direction, then redraws the car on screen with new coordinates. 
5. Fire Regular Bullet: If the user presses the key “K”, a regular bullet is created. 
6. Fire Strong Bullet: If the user presses the key “L”, a strong bullet is created. 
7. Use Shield: If the user has enough to purchase a shild and presses "Shift", a shield will be created around the user car.
8. Exit: After the game is lost, s/he waits on the ending screen, where s/he can view his/her scores. If the pressed key is “Escape”, the game screen closes.

### COLLABORATION DIAGRAMS
![](/assets/collab_diagram_1.jpeg )
![](/assets/collab_diagram_2.jpeg )
![](/assets/collab_diagram_3.jpeg )
1. FireRegularBullet: UserCar first check if there is enough coin to use bullet by asking Coin. If there is enough coin UserCarcreates bullet from the coordinates it has and Coin reduces amount of coin by price.
2. FireStrongBullet: Same logic with the above diagram.
3. UseShield:  UserCar first check if there is enough coin to use bullet by asking Coin. If there is enough coin UserCar acivates shield and Coin reduces amount of coin by price.
4. MoveUserCar: UserCar checks if it is possible to move. If it is then UserCar moves itself with the keypresses.
5. Start: The game waits for a key press, when the user presses “Enter”, the game starts.
6. Pause: While the user is playing the game, if he presses the key “P”, the game pauses.
7. Resume: If the user is on the pause screen, the game listens to input. If the pressed key is key “ENTER”, the game resumes.
8. Exit: After a player loses the game, she waits on the ending screen, where she sees her scores. The game is still listening the key presses, if the pressed key is “E”, the game screen closes.
9. TimeTick:
- As time passes;
	+ RoadGame checks if any regular bullet hit any obstacles. If so, deletes bullet and the obstacle.
	+ RoadGame checks if any strong bullet hit any obstacles. If so deletes obstacles and the bullet destroys any obstacles on the path that have same y-axis coordinates. 
	+ RoadGame generates coins(Coin), cars(OtherCars) and obstacles(Obstacle) at possible random points.
	+ Roadgame checks if any UserCar object is collided to any object of another classes, if so sends signal to UserCar to take appropriate actions. If the collision happens with the police car, the game is over.
	+ UserCar asks the particular object if they are collided and sends its coordinates. Other object compares it with his own coordinates and returns True if collided returns False otherwise to take appropriate actions.
	+ RoadGame increases speed of the UserCar and PoliceCar objects.