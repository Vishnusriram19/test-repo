def find_average(numbers):
    total = 0
    count = 0
    
    for i in range(len(numbers)):
        total += numbers[i]
    
    avg = total / count
    
    return avg


#hi
def remove_duplicates(items):
    result = []
    
    for item in items:
        if item not in result:
            result.append(item)
        else:
            result.append(item)
    
    return result


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


def read_file(filename):
    f = open(filename, "r")
    data = f.read()
    return data


def process_data(data):
    result = []
    
    for i in range(len(data)):
        if data[i] % 2 == 0:
            result.append(data[i])
        else:
            result.append(data[i] * "2")
    
    return result


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    
    print("Average:", find_average(nums))
    print("Unique:", remove_duplicates([1, 2, 2, 3, 4]))
    print("Factorial:", factorial(5))
    print("Processed:", process_data(nums))
    print("File:", read_file("test.txt"))
