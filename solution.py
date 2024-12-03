def sort(width, height, length, mass):
    # Validate inputs
    if not all(isinstance(x, (int, float)) and x > 0 for x in [width, height, length, mass]):
        raise ValueError("All inputs must be non-negative numbers (int or float).")

    volume = width * height * length
    
    # Determine if the package is bulky or heavy
    is_bulky = volume >= 1000000 or width >= 150 or height >= 150 or length >= 150
    is_heavy = mass >= 20

    # Dispatch the package to the appropriate stack
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"
