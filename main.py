from __future__ import annotations
from typing import List

from model import Robot
from model import RobotWars
from robotWarsNoCollision import RobotWarsNoCollisions


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = [line.rstrip() for line in f]

    r, c = map(int, data[0].split())
    robots: List[Robot] = []

    # parse every robots data
    for idx in range(1, len(data), 2):
        x, y, d = data[idx].split()
        # means robot didn't move at all
        if " " in data[idx + 1]:
            idx -= 1
            continue
        walk = data[idx + 1]
        robots.append(Robot(int(x), int(y), d, walk))

    # we can swap solver logic here
    solver: RobotWars = RobotWarsNoCollisions(r, c, robots)
    solver.move_robots()
    solver.print_robots()
