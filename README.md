
<h2>Usage</h2>

Run program with `python main.py`, the program takes `input.txt` file as an input 
(it is possible to modify `input.txt` file for other test cases).

No third party libraries were used, so standard Python setup is enough.


<h2>Design decisions</h2>

- Structure
  - `RobotWars` is an abstract class which describes interface described in problem description,
  it has two concrete implementations: `robotWarsNoCollision` and `robotWarsWithCollision`
  - `robotWarsNoCollision` implements the `RobotWars` class while ignoring collisions with other robots
  - `robotWarsWithCollision` implements the `RobotWars` class while blocking robot movement if it is going to collide
  with other robot

- Testing
  - Duplicating test cases with same expected results were identified, so extensible solution was made - test runner
  with ability to plug in new implementations.

- RobotWars abstract class
  - Inheritance can often be changed with composition, since the only variable point of RobotWars simulation was
  collisions I've decided to go with easier implementation of inheritance mixed with abstract methods.
  - The requirements file didn't specify how we should handle collisions so I proposed two ways: with ignoring 
  collisions and with blocking robot if other robot is on the way. To make it easier to test and to make it more
  easy for user to plug different implementations I have put RobotWars under interface (with public function move_robots)
  - There were other ideas how should collisions be handled (implementation of error on collision or one robot destroying 
  another on collision. It is Robot Wars after all), but I've decided to implement two of them which made most sense for me.

- Client code
  - Client code is only for starting up the program with right inputs, no design effort was put there as it is not
  essential.

- Private functions
  - Private functions were used a lot in this project, it is used to translate what is being done on each step,
  therefore making code more readable. It also eliminated high level nesting functions.

- Documentation
  - All documentation were done using Python docstrings

- Code duplication 
  - Some code duplication exists between robotWarsNoCollision and robotWarsWithCollision 
  (equal functions: __apply_command and __try_moving). This was kept due it's simplicity to implement (eliminating
  this duplication could require more complex code) and also because requirements are were abstract so quick solution
  is more preferable over complex one.

