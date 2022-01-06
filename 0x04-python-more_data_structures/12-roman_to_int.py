#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is not None:
        if type(roman_string) != str or roman_string is None:
            return 0
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        rom = roman_string
        for i in range(len(rom)):
            if i < len(rom) - 1 and dic[rom[i]] < dic[rom[i + 1]]:
                result -= dic[rom[i]]
            else:
                result += dic[rom[i]]
        return result
    else:
        return (0)
