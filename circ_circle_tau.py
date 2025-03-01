#!/usr/bin/env python3
# Created by Dylan Mutabazi
# Date :23-02-2025
# This program calculates the circumference of a circle

import math
import constants

def main():
    radius = float(input("What is the radius of your circle: "))
    print("")

    print("The circumference of the circle is: {}" .format(radius * constants.TAU))

if __name__ == "__main__":
    main()