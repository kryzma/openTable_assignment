import unittest
from typing import List
import copy

from robotWarsNoCollision import RobotWarsNoCollisions
from robotWarsWithCollision import RobotWarsWithCollisions
from model import RobotWars
from model import Robot


class TestCommonCases(unittest.TestCase):
    """
    This will test all implementations of robot movements, the function takes implementation of test
    """

    # Default parameters
    width: int = 3
    height: int = 3

    # Implementations of RobotWars
    implementations: List[type] = [RobotWarsNoCollisions, RobotWarsWithCollisions]

    def test_spin_720_degrees_left(self):
        robot_1 = Robot(0, 0, "E", "LLLLLLLL")
        robots = [robot_1]

        robots_results = self.__run_for_all_implementations(self.width, self.height, robots)

        robot_1_expected = Robot(0, 0, "E", "LLLLLLLL")
        robots_expected = [robot_1_expected]
        self.__validate(robots_results, robots_expected)

    def test_spin_720_degrees_right(self):
        robot_1 = Robot(0, 0, "N", "RRRRRRRR")
        robots = [robot_1]

        robots_results = self.__run_for_all_implementations(self.width, self.height, robots)

        robot_1_expected = Robot(0, 0, "N", "RRRRRRRR")
        robots_expected = [robot_1_expected]
        self.__validate(robots_results, robots_expected)

    def test_collide_with_wall(self):
        """ Colliding with wall 4 times """
        robot_1 = Robot(0, 0, "N", "MMMMRMMMMRMMMMRMMMM")
        robots = [robot_1]

        robots_results = self.__run_for_all_implementations(self.width, self.height, robots)

        robot_1_expected = Robot(0, 0, "W", "MMMMRMMMMRMMMMRMMMM")
        robots_expected = [robot_1_expected]
        self.__validate(robots_results, robots_expected)

    def __run_for_all_implementations(self, width: int, height: int, robots: List[Robot]) -> List[List[Robot]]:
        result: List[List[Robot]] = []
        for implementation in self.implementations:
            robot_wars_implementation: RobotWars = implementation(width, height, copy.deepcopy(robots))
            robot_wars_implementation.move_robots()
            result.append(robot_wars_implementation.robots)
        return result

    def __validate(self, results: List[List[Robot]], expected: List[Robot]):
        # for each implementation result
        for result in results:
            # for each robot index
            for idx in range(len(expected)):
                print(result[idx])
                print(expected[idx])
                try:
                    self.assertTrue(result[idx] == expected[idx])
                except AssertionError as e:
                    raise AssertionError("The problem came from implementation {0}. {1}"
                                         .format(self.implementations[0].__name__, e))


class TestRobotWarsNoCollisions(unittest.TestCase):

    def test_robots_overlap(self):
        robot_1 = Robot(0, 0, "E", "M")
        robot_2 = Robot(1, 0, "W", "M")
        robots: List[Robot] = [robot_1, robot_2]

        robot_wars: RobotWars = RobotWarsNoCollisions(w=1, h=1, robots=robots)
        robot_wars.move_robots()

        self.assertEqual(robot_wars.robots[0].x, 1)
        self.assertEqual(robot_wars.robots[1].x, 0)


class TestRobotWarsCollisions(unittest.TestCase):

    def test_robots_collide(self):
        robot_1 = Robot(0, 0, "E", "M")
        robot_2 = Robot(1, 0, "W", "M")
        robots: List[Robot] = [robot_1, robot_2]

        robot_wars: RobotWars = RobotWarsWithCollisions(w=1, h=1, robots=robots)
        robot_wars.move_robots()

        print(robot_1.x)

        self.assertEqual(robot_wars.robots[0].x, 0)
        self.assertEqual(robot_wars.robots[1].x, 1)

    def test_come_back_to_start(self):
        robot_1 = Robot(0, 0, "E", "MRRM")
        robots: List[Robot] = [robot_1]

        robot_wars: RobotWars = RobotWarsWithCollisions(w=1, h=1, robots=robots)
        robot_wars.move_robots()

        self.assertEqual(robot_wars.robots[0].x, 0)
        self.assertEqual(robot_wars.robots[0].y, 0)