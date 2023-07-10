#!/usr/bin/env python
# import obd

gear_ratio_map = {1: 5.0867, 2: 2.991, 3: 2.035, 4: 1.594, 5: 1.286, 6: 1.000}
final_drive_ratio = 2.866

def calculate_rpm(mph, gear, tyre_width_mm, tyre_sidewall_in, rim_diameter_in):
    # Ratios
    transmission_gear_ratio = gear_ratio_map.get(gear)
    final_gear_ratio = gear_ratio_map.get(6)

    # Wheel/Tyre specs
    tyre_width_in = convert_to_inches(tyre_width_mm)
    tyre_sidewall_height_in = (tyre_sidewall_in / 100) * tyre_width_in
    tyre_diameter_in = rim_diameter_in + (2 * tyre_sidewall_height_in)
    tyre_circumference = 3.14159 * round(tyre_diameter_in, 1)
    inches_per_ft = 12
    ft_per_mi = 5280
    tyre_rev_per_mi = (inches_per_ft * ft_per_mi) / tyre_circumference
    min_per_hr = 60

    # Calculate RPM
    rpm = mph / (final_gear_ratio / transmission_gear_ratio) / (final_gear_ratio / final_drive_ratio) / (final_gear_ratio / tyre_rev_per_mi) / min_per_hr
    print(rpm)

def convert_to_inches(mm):
    return mm / 25.4

def conenct_to_obd2():
    ports = obd.scan_serial()      # return list of valid USB or RF ports
    connection = obd.OBD(ports[0]) # connect to the first port in the list
    if connection.status() == OBDStatus.CAR_CONNECTED:
        query = connection.query(obd.commands.RPM) # current RPM. TODO : Need to calculate differential and display on LCD

if __name__ == "__main__":
    calculate_rpm(36.2, 1, 205, 45, 17)
