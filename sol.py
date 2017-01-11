def Binary_Search(arr, to_find):
    """
    params: arr (a list ordered from least to greatest)
            to_find (the item to find in arr)
    returns: index (int), x, s.t. arr[x] == to_find
            None(none-type) if for all x, arr[x] != to_find
    """
    def split(arr, to_find, start):
        if len(arr) == 1:
            if arr[0] == to_find:
                return start
            else:
                return None
        else:
            mid = len(arr)//2
	    if arr[mid] > to_find:
                return split(arr[0:mid], to_find, start)
            else:
                return split(arr[mid:], to_find, start+mid)

    return split(arr, to_find, 0)
   
 
def Bisection(func, left_side, right_side, tol=1e-5):
    """
       (For sanity assume that func and func_prime define there own division correctly,
       that is, don't cast anything to a float)
       params: func (a function)
               left_side (a value for the function to take on, it should have opposite sign from `right_side`)
               right_side (a value for the function to take on, it should have opposite sign from `left_side`)
               tol (a value for which the function should return once a value at least that distance from zero is found)
       returns: root (float), x, s.t. abs(func(x))<tol
                None(none-type) if func(left_side), func(right_side) < 0 or func(left_side), func(right_side) > 0
    """
    pass
