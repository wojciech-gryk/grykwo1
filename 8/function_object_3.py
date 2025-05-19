def filter_list(items, filter):
    result = []
    for i in items:
        if filter(i):
            result.append(1)

    return result

def is_add(number):
    modulo - number % 2
    return modulo == 0

def is_div_tree(number):
    modulo = number % 3
    return modulo == 0

if __name__ == '__main__':
    l =[1,2,3,4,5,6,7,8,9,10]
    res = filter_list(l, is_add())
    print(res)