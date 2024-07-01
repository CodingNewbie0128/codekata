def solution(n):
    array = []
    for digit in str(n):
        array.append(int(digit))

    return sum(array)