Game:
- Goal are to destroy enemy's airport and come back to your airport safely.
- You will start at a random airport.
- Your enemy's main airport will also be selected randomly.
- You will be provided a fighter and an amount of gasoline.
- Fuel consumption something like 1 litre = 2 km.
- Choose 40 large airports from Europe.
- When you arrive an airport, you have 2 choices:
	+ Destroy this airport.
	+ Land to get more gasoline.
- One airport can have either enemy (500 - 1000 soldiers) or gasoline (500 - 1000 liters) or nothing except the enemy's main airport and your base. 
- Every time you kill 1000 enemy's soldiers, you will get more than 20% gasoline from the airport.
- When you land in an airport with enemy's soldiers, you will not be killed by the enemy, but you will be stolen 50% gasoline left in your fuel storage.
- If you land in an airport with gasoline, all of them will be added to your fuel storage.
- You cannot destroy an airport that you decide to land. But you can come back later to destroy it.
- Bonus can be added up.
- When you arrive the enemy's main airport, you have only one choice: destroy this airport.
- After you destroy the enemy's airport, you will get more than 50% gasoline.
- There will be 15 airports with enemy, 15 airports with gasoline, 5 airports with nothing, one airport which is your base, and one is enemy's base.
- If you fail to destroy enemy's airport, you will lose!
- If you destroy the enemy's airport, but you run out of gasoline, you will die and lose. 
- If you can come back to your airport safely, you will win!

Changes in the new game:
- Goals are still same to the old ones.
- Instead of starting at a random airport, now you can choose where you want to start.
- Your target will be chosen based on your selection of your base.
- The fighters will have 3 functions and each function has 5 levels:
	+ Function 1: Fuel consumption
  		* Level 1: 1 litre = 2km
    	* Level 2: 1 litre = 2.2 km
        * Level 3: 1 litre = 2.4 km
        * Level 4: 1 litre = 2.6 km
        * Level 5: 1 litre = 3 km
    + Function 2: Weapon consumption
  		* Level 1: 1 litre = 1 rocket
    	* Level 2: 0.9 litre = 1 rocket
        * Level 3: 0.8 litre = 1 rocket
        * Level 4: 0.7 litre = 1 rocket
        * Level 5: 0.5 litre = 1 rocket
    + Function 3: Weapon damage
  		* Level 1: 1 rocket will kill 200 enemies.
    	* Level 2: 1 rocket will kill 300 enemies.
        * Level 3: 1 rocket will kill 400 enemies.
        * Level 4: 1 rocket will kill 500 enemies.
        * Level 5: 1 rocket will kill 600 enemies.
- You can use the coins you obtained from killing your enemies.
- You will be provided a level 1 fighter and an limited amount of gasoline.
- Choose 40 large airports from Europe.
- When you arrive at an airport, you have 2 choices:
	+ Destroy the airport.
    + Land.
- Instead of 20% like the previous version, now you can only get 10% bonus after killing 1000 enemies.
- There are 3 types of airports:
    + Type 1: Only enemies stay here
    + Type 2: Only gasoline in the storage
    + Type 3: Both enemies stay here and the gasoline is in the storage.
- When you land in a type 1 airport, you will have to fight with enemies, and you will lose fuel base on the weapon consumption and weapon damage.
- The gasoline you lose = total_enemies / enemies_each_rocket_kills * weapon_consumption
- When you land in a type 2 airport, you can get all fuels in the storage.
- When you land in a type 3 airport, you will have to fight against the enemy.
    + If you win (when you killed all enemies and still have fuel left), you will get the bonus and the fuels in the storage.
    + If you lose (when you run out of fuel while fighting), you will be killed by the enemies.
- If you choose to destroy an airport before landing, you still can get the bonus but can get the fuel in the storage.
- There will be 10 type 1 airports, 10 type 2 airports and 15 type 3 airports and 5 airports with nothing, include your base and your target.
- New system: Spy system
- After you chose your base, the countries that your spies can obtain specific details will be calculated using the bfs algorithm
min_dist = 1 => can get both details about enemies and fuels
- min_dist = 2 => can get either enemies or fuels
- min_dist > 3 => cant get any details