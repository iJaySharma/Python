def sort(collection, predicate=None):
    dataset = list(collection)
    m = len(dataset) - 2
    if predicate == None:
        while m >= 0:
            e = 0
            f = 1
            while e <= m:
                if dataset[e] > dataset[f]:
                    dataset[e], dataset[f] = dataset[f], dataset[e]
                e += 1
                f += 1
            m -= 1 
        return dataset
    else:
        while m >= 0:
            e = 0
            f = 1
            while e <= m:
                if predicate(dataset[e]) > predicate(dataset[f]):
                    dataset[e], dataset[f] = dataset[f], dataset[e]
                e += 1
                f += 1
            m -= 1
        return dataset

def sum_of_digits(num): # it might be just sum_of_digits(num): return sum(list(map(int,str(num))))  
    dc = 0
    while num > 0:
        dc += (num % 10)
        num //= 10
    return dc

x = [10, 2, 304, 43, 4050, 432, 543, 33343, 3203000, 3000]
y = sort(x)
print(y)
print("*" * 20)
y = sort(x, sum_of_digits)
print(y)
