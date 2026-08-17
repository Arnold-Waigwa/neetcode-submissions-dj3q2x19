class CountSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        p = tuple(point)
        self.points[p] = 1 + self.points.get(p, 0)

    def count(self, point: List[int]) -> int:
        res = 0
        x, y = point

        for px, py in self.points:
            if abs(x - px) != abs(y - py):
                continue

            if x == px:
                continue

            res += (
                self.points[(px, py)]
                * self.points.get((px, y), 0)
                * self.points.get((x, py), 0)
            )

        return res