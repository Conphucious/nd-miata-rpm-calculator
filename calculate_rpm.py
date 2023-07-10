#!/usr/bin/env python

gear_ratio_map = {1: 5.0867, 2: 2.991, 3: 2.035, 4: 1.594, 5: 1.286, 6: 1.000}

def calculate_rpm(mph, gear):
    rpm = mph / (1 / gear_ratio_map.get(gear)) / (1 / 2.866) / (1 / 830) / (60)
    print(rpm)


if __name__ == "__main__":
    calculate_rpm(36.2, 2)