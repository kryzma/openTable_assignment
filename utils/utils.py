

def collides_with_wall(x: int, y: int, width: int, height: int) -> bool:
    return 0 > x > width and 0 > y > height
