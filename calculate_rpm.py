#!/usr/bin/env python

gear_ratio_map = {1: 5.0867, 2: 2.991, 3: 2.035, 4: 1.594, 5: 1.286, 6: 1.000}

def calculate_rpm(mph, gear):
    final_drive_ratio = 2.866
    transmission_ratio = gear_ratio_map.get(gear)
    tyre_rev_per_mi = 830
    min_per_hr = 60

    rpm = mph / (1 / transmission_ratio) / (1 / final_drive_ratio) / (1 / tyre_rev_per_mi) / min_per_hr
    print(rpm)


if __name__ == "__main__":
    calculate_rpm(36.2, 2)