def check_integers(lst):
    if len(lst) == 0:
        return True
    elif isinstance(lst[0], int):
        return check_integers(lst[1:]) 
    else:
        return False

def arithmetic_sequence(start, step, count):
    if not check_integers([start, step, count]) or count < 1:
        return "Error: all numbers must be integers, and count must be greater than 0."
    if count == 1:
        return [start] 
    else:
        return arithmetic_sequence(start, step, count - 1) + [start + (count - 1) * step]

print(arithmetic_sequence(2, 3, 5)) 
print(arithmetic_sequence(0, 10, 4))  
print(arithmetic_sequence(1, 1, 6))

