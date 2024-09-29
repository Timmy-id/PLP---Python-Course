def large_power(base, exponent):
    if base ** exponent > 5000:
        return True
    else:
        return False
    
print(large_power(100, 6))