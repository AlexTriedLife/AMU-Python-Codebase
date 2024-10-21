import math


"""
1 mile is equal to 1.6 kilometres.
multiply miles by 1.6 to find kilometres
divide kilometres by 1.6 to find the miles
"""
def miles_to_km(miles):
    return miles * 1.6
def km_to_miles(km):
    if km == 0:
        assert "cannot divide by 0"
        return
    return km / 1.6
if __name__ == '__main__':
    print(km_to_miles(5))
