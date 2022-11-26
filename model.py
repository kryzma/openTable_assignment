from __future__ import annotations

from enum import Enum
from typing import List
from abc import ABC, abstractmethod

from utils.utils import collides_with_wall

class Direction(Enum):
    """
    Enum describing 4 main directions,
    each direction has position difference representation,
    also values are ordered so that turn_left and turn_right
    functionality works
    """
    North = [0, 1]
    West = [-1, 0]
    South = [0, -1]
    East = [1, 0]

    def turn_left(self) -> Direction:
        members = list(self.__class__)
        new_index = (members.index(self) + 1) % len(members)
        return members[new_index]

    def turn_right(self) -> Direction:
        members = list(self.__class__)
        new_index = (members.index(self) - 1 + len(members)) % len(members)
        return members[new_index]


class Robot:
    """
    Class describing robot
    """
    x: int
    y: int
    dir: Direction
    commands: str

    def __init__(self, x: int, y: int, dir: str, commands: str):
        self.x = x
        self.y = y
        self.commands = commands
        if dir == "N":
            self.dir = Direction.North
        elif dir == "W":
            self.dir = Direction.West
        elif dir == "S":
            self.dir = Direction.South
        elif dir == "E":
            self.dir = Direction.East
        else:
            raise ValueError("Robot has unsupported direction!")

    def __eq__(self, other: Robot):
        return self.x == other.x and self.y == other.y and self.dir == other.dir and self.commands == other.commands

    def __str__(self):
        return "x = {0}, y = {1}, dir = {2}, commands = {3}".format(self.x, self.y, self.dir, self.commands)


class RobotWars(ABC):
    """
    Interface for RobotWars which simulates robot movements,
    modifiability comes from collision logic
    """

    width: int
    height: int
    robots: List[Robot]

    def __init__(self, w: int, h: int, robots: List[Robot]):
        self.width = w
        self.height = h
        self.robots = robots

    @abstractmethod
    def move_robots(self):
        """
        Simulates commands for each robot
        """

    def print_robots(self):
        """
        Prints current robots positions and directions
        """
        for robot in self.robots:
            print(robot.x, end=" ")
            print(robot.y, end=" ")
            if robot.dir == Direction.North:
                print("N")
            elif robot.dir == Direction.West:
                print("W")
            elif robot.dir == Direction.South:
                print("S")
            elif robot.dir == Direction.East:
                print("E")
            else:
                raise ValueError("Unsupported direction: {0}".format(robot.dir))

    def __robot_inside_grid(self):
        for robot in self.robots:
            if collides_with_wall(robot.x, robot.y, self.width, self.height):
                raise IndexError("Robot can't be outside the grid")