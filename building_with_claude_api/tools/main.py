"""
Module to calculate pi to a specified number of digits.
"""

def calculate_pi(digits=5):
    """
    Calculate pi to the specified number of decimal digits using the Chudnovsky algorithm.
    
    The Chudnovsky algorithm is one of the fastest known algorithms for calculating pi.
    It converges very rapidly, gaining about 14 digits per iteration.
    
    Args:
        digits (int): Number of decimal digits to calculate (default: 5)
    
    Returns:
        float: Pi calculated to the specified precision
    """
    from decimal import Decimal, getcontext
    
    # Set precision higher than needed to ensure accuracy
    getcontext().prec = digits + 10
    
    C = 426880 * Decimal(10005).sqrt()
    K = Decimal(6)
    M = Decimal(1)
    X = Decimal(1)
    L = Decimal(13591409)
    S = Decimal(13591409)
    
    # Number of iterations needed (each iteration gives ~14 digits)
    iterations = (digits // 14) + 1
    
    for i in range(1, iterations + 1):
        M = M * (K ** 3 - 16 * K) / ((i) ** 3)
        K += 12
        L += 545140134
        X *= -262537412640768000
        S += Decimal(M * L) / X
    
    pi = C / S
    
    # Round to the specified number of digits
    return round(float(pi), digits)


def get_pi_to_5th_digit():
    """
    Calculate pi to the 5th decimal digit.
    
    Returns:
        float: Pi calculated to 5 decimal places (3.14159)
    """
    return calculate_pi(5)


if __name__ == "__main__":
    pi_value = get_pi_to_5th_digit()
    print(f"Pi to the 5th digit: {pi_value}")
    print(f"Formatted: {pi_value:.5f}")