# а) Функция filter_numbers
def filter_numbers(numbers, condition=None):
    if condition is None:
        return numbers
    result = []
    for x in numbers:
        if condition(x):
            result.append(x)
    return result

# б) Функция transform_numbers
def transform_numbers(numbers, transform_function=None):
    if transform_function is None:
        return numbers
    result = []
    for x in numbers:
        result.append(transform_function(x))
    return result

# в) Функция cube_numbers
def cube_numbers(*lists):
    result = []
    for lst in lists:
        for x in lst:
            result.append(x ** 3)
    return result

# г) Функция product_non_zero
def product_non_zero(*args):
    product = 1
    found_non_zero = False
    for x in args:
        if x != 0:
            product *= x
            found_non_zero = True
    return product
