#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    if not isinstance(roman_string, str):
        return 0
    rimap = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    r_s = roman_string.upper()
    roman_string_len = len(roman_string)
    i = 0
    final_val = 0
    while i < roman_string_len:
        if i+1 < roman_string_len and rimap[r_s[i + 1]] > rimap[r_s[i]]:
            final_val += (rimap[r_s[i + 1]] - rimap[r_s[i]])
            i += 2
            continue
        elif i+1 < roman_string_len and rimap[r_s[i + 1]] == rimap[r_s[i]]:
            final_val += (2 * rimap[r_s[i]])
            i += 2
            if i < roman_string_len and rimap[r_s[i]] == rimap[r_s[i - 1]]:
                final_val += rimap[r_s[i]]
                i += 1
                continue
            continue
        else:
            final_val += rimap[r_s[i]]
            i += 1
    return final_val
