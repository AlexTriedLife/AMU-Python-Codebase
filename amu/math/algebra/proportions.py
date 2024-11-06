"""
proportion:  n1 / d1 = n2 / d2 
n1 and n2 are the numerators of term 1 and term 2
d1 and d2 are the denominators of term 1 and term 2
0 or None means unknown
"""
def cross_multiply_proportion(n1, d1, n2, d2):
    # unknown
    answer = 0
    # Check which parameter is undefined
    if n1 == 0 or n1 is None:
        answer = d1 * n2 / d2
        print(f"n1 = {answer}")
    if n2 == 0 or n2 is None:
        answer = d2 * n1 / d1
        print(f"n2 = {answer}")

    return answer

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
    cross_multiply_proportion(2,4,0,2)
