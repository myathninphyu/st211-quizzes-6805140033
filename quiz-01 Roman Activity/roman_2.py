import re
roman_map = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000
}

def roman_to_number(roman_string):
    total = 0
    for i in range(len(roman_string)):
        current_value = roman_map[roman_string[i]]
        if i + 1 < len(roman_string) and current_value < roman_map[roman_string[i + 1]]:
            total -= current_value
        else:
            total += current_value
    return total

def validate_roman_rules(s):
    # Check for invalid repetitions of V, L, D (cannot repeat)
    if re.search(r'V{2,}|L{2,}|D{2,}', s):
        return False, "Error: Invalid Roman numeral. Symbols V, L, and D cannot be repeated."
    
    # Check for more than 3 repetitions of I, X, C, M
    if re.search(r'I{4,}|X{4,}|C{4,}|M{4,}', s):
        return False, "Error: Invalid Roman numeral. Symbols I, X, C, and M cannot be repeated more than 3 times."
        
    # Check strict subtraction pairing and rule constraints
    for i in range(len(s) - 1):
        curr = s[i]
        nxt = s[i+1]
        curr_val = roman_map[curr]
        nxt_val = roman_map[nxt]
        
        if curr_val < nxt_val:
            # Rule: V, L, D can never be subtracted
            if curr in 'VLD':
                return False, f"Error: '{curr}' cannot be placed in front of a larger symbol to subtract."
            # Rule: I can only precede V or X
            if curr == 'I' and nxt not in 'VX':
                return False, "Error: 'I' can only be subtracted from 'V' or 'X'."
            # Rule: X can only precede L or C
            if curr == 'X' and nxt not in 'LC':
                return False, "Error: 'X' can only be subtracted from 'L' or 'C'."
            # Rule: C can only precede D or M
            if curr == 'C' and nxt not in 'DM':
                return False, "Error: 'C' can only be subtracted from 'D' or 'M'."
                
    return True, ""

if __name__ == "__main__":
    roman_number = "VVVV"
    print(f"Entered Roman numeral: {roman_number}")
    
    is_valid, error_message = validate_roman_rules(roman_number)
    if not is_valid:
        print(error_message)
    else:
        result = roman_to_number(roman_number)
        print(f"The integer value of {roman_number} is: {result}")

print (f"The integer value :", roman_to_number("VVVV"))  # Output: 14
print (f"The integer value is:", roman_to_number("MCMXCIV"))  # Output: 1994

