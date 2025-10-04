def sort(width, height, length, mass):
    # Calculate volume
    volume = width * height * length
    
    # Determine bulky condition
    bulky = True if (volume >= 1000000 or width >= 150 or height >= 150 or length >= 150) else False
    
    # Determine heavy condition
    heavy = True if mass >= 20 else False

    # Decide stack (uses at least one ternary operator)
    return "REJECTED" if bulky and heavy else ("SPECIAL" if bulky or heavy else "STANDARD")


if __name__ == "__main__":
    print(sort(100, 100, 100, 10))   # SPECIAL
    print(sort(200, 50, 50, 10))     # SPECIAL
    print(sort(100, 100, 100, 25))   # SPECIAL
    print(sort(200, 200, 200, 25))   # REJECTED
    print(sort(50, 50, 50, 5))       # STANDARD
