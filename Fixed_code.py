def find_cube_pairs(target):  # Added colon at the end of function definition
    solutions = []  # removed ';' to proper Python syntax
    max_num = round(target ** (1/3))  # Corrected 'targ' to 'target' and '***' to '**' as '**' is valid power operator in Python

    for a in range(1, max_num + 1):  # Changed 'ranges' to 'range' and added colon
        for b in range(a, max_num + 1):  # Changed 'ranges' to 'range' and added colon
            if a**3 + b**3 == target:  # Changed '***' to '**' and 'targ' to 'target'
                solutions.append((a, b))  # Changed 'sol' to 'solutions' and corrected syntax by brackets
    return solutions  # Changed 'sol' to 'solutions'

pairs = find_cube_pairs(1729)  # removed ending ,
print("Valid cube pairs for 1728:")  # Changed 'printf' to 'print' and corrected string
for a, b in pairs:  # Changed 'pair' to 'pairs' and added colon
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1728")  # Changed 'printf' to 'print' and corrected 'a**2' to 'a**3' and 'b**2' to 'b**3'
