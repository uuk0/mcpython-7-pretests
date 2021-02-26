import math
import typing
from abc import ABC


class AbstractBoundingPart(ABC):
    # todo: add draw() method, add affected_normal_coords() returning a iterator over normal points inside the box
    #  for later faster lookup (if they have NO common point, they cannot be the same), especially in BoundingGroup

    def intersects(self, other: "AbstractBoundingPart"):
        raise NotImplementedError


class BoundingGroup(AbstractBoundingPart):
    # todo: maybe use one of these in each section of the world?

    def __init__(self):
        # todo: sort out in advance what we need and what not by using a normalized position -> parts[] dict,
        #  and looking up only affected positions
        self.parts: typing.List["AbstractBoundingPart"] = []

    def add_part(self, part):
        self.parts.append(part)

    def intersects(self, other: "AbstractBoundingPart"):
        return any(part.intersects(other) for part in self.parts)


class Point(AbstractBoundingPart):
    def __init__(self, position: typing.Tuple):
        self.position = position

    def intersects(self, other: "AbstractBoundingPart"):
        return (
            other.position == self.position
            if isinstance(other, Point)
            else other.intersects(self)
        )


class AABB(AbstractBoundingPart):
    def __init__(self, start: typing.Tuple, end: typing.Tuple):
        self.start = start
        self.end = end

    def intersects(self, other: "AbstractBoundingPart"):
        if isinstance(other, Point):
            return all(
                self.start[i] <= other.position[i] <= self.end[i] for i in range(3)
            )
        elif isinstance(other, AABB):
            return all(
                self.start[i] <= other.end[i] and self.end[i] >= other.start[i]
                for i in range(3)
            )
        return other.intersects(self)


class Sphere(AbstractBoundingPart):
    def __init__(self, center: typing.Tuple, radius: float):
        self.center = center
        self.radius = radius

    def intersects(self, other: "AbstractBoundingPart"):
        if isinstance(other, Point):
            return math.dist(self.center, other.position) <= self.radius
        elif isinstance(other, Sphere):
            return math.dist(self.center, other.center) <= self.radius + other.radius
        elif isinstance(other, AABB):
            return (
                math.dist(
                    [
                        max(other.start[i], min(self.center[i], other.end[i]))
                        for i in range(3)
                    ],
                    self.center,
                )
                <= self.radius
            )
