def bit_plus_plus(total,operations):
    result = 0
    for i in operations:
        if i == 'X++' or i == '++X':
            result = result + 1
        else:
            result = result - 1
    return result

if __name__ == "__main__":
    total = int(input())
    operations = []
    for _ in range(0,total):
        operations.append(input())
    print(bit_plus_plus(total,operations))
        