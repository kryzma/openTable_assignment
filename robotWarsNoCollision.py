from model import RobotWars
from model import Robot

import utils.utils as utils


class RobotWarsNoCollisions(RobotWars):
    """
    Moves a single robot in O(N) time complexity, where N is length of commands
    Space complexity: O(N) where N is length of commands
    """

    def move_robots(self):
        for idx in range(len(self.robots)):
            self.__move_single_robot(self.robots[idx])

    def __move_single_robot(self, robot: Robot):
        for command in robot.commands:
            self.__apply_command(robot, command)

    def __apply_command(self, robot: Robot, command: str):
        if command == "R":
            robot.dir = robot.dir.turn_right()
        elif command == "L":
            robot.dir = robot.dir.turn_left()
        elif command == "M":
            self.__try_moving(robot)
        else:
            raise ValueError("Unsupported command found: {0}".format(command))

    def __try_moving(self, robot: Robot):
        new_x = robot.x + robot.dir.value[0]
        new_y = robot.y + robot.dir.value[1]
        if self.__can_move(new_x, new_y):
            robot.x = new_x
            robot.y = new_y

    def __can_move(self, x: int, y: int) -> bool:
        return not utils.collides_with_wall(x, y, self.width, self.height)
