#!/usr/bin/env python3
# Created by Dylan Mutabazi
# Date :23-02-2025
# This program calculates the circumference of a circle

import math
import constants


def main():
# assigns user input to variable radius 
    radius = float(input("What is the radius of your circle: "))
    print("")

# calculates circumference using variable radius and constant TAU
    print("The circumference of the circle is: {}".format(radius * constants.TAU))


if __name__ == "__main__":
    main()
