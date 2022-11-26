from typing import List

from model import RobotWars
from model import Robot
import utils.utils as utils


class RobotWarsWithCollisions(RobotWars):
    """
    Moves a single robot in O(N) time complexity, where N is length of commands.
    Space complexity: O(N+M) where N is length of commands and M is number of robots
    """

    # robot_locations stores positions where robot is present, used to optimize speed of detecting collisions
    robot_locations: set[str]

    def __init__(self, w: int, h: int, robots: List[Robot]):
        super().__init__(w, h, robots)
        self.robot_locations = set()
        self.__form_robot_locations()

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
            old_x, old_y = robot.x, robot.y
            self.__try_moving(robot)
            self.__update_robot_locations(old_x, old_y, robot.x, robot.y)
        else:
            raise ValueError("Unsupported command found: {0}".format(command))

    def __try_moving(self, robot: Robot):
        new_x = robot.x + robot.dir.value[0]
        new_y = robot.y + robot.dir.value[1]
        if self.__can_move(new_x, new_y):
            robot.x = new_x
            robot.y = new_y

    def __can_move(self, new_x: int, new_y: int) -> bool:
        return not utils.collides_with_wall(new_x, new_y, self.width, self.height) and \
               not self.__collides_with_other_robot(new_x, new_y)

    def __collides_with_other_robot(self, new_x: int, new_y: int):
        hashable_position: str = self.__hashable_position(new_x, new_y)
        return hashable_position in self.robot_locations

    def __form_robot_locations(self):
        for robot in self.robots:
            hashable_position: str = self.__hashable_position(robot.x, robot.y)
            # if robot is already there
            if hashable_position in self.robot_locations:
                raise ValueError("Two robots can't exist in single cell. Position:({0},{1})".format(robot.x, robot.y))
            self.robot_locations.add(hashable_position)

    @staticmethod
    def __hashable_position(x: int, y: int) -> str:
        return "{0}|{1}".format(x, y)

    def __update_robot_locations(self, old_x: int, old_y: int, new_x: int, new_y: int):
        self.robot_locations.remove(self.__hashable_position(old_x, old_y))
        self.robot_locations.add(self.__hashable_position(new_x, new_y))
