# 최대값 구하기
def get_max_num(number_list):
    number = number_list[0] # index 참조
    for current_number in number_list:
        if current_number > number:
            number = current_number
    return number

# 최대값의 인덱스 찾기
def get_max_index(number_list):
    number = number_list[0] # index 참조
    max_index = 0
    for index, current_number in enumerate(number_list):
        if current_number > number:
            number = current_number
            max_index = index
    return max_index

numbers = [17, 92, 18, 33, 58, 7, 33, 42]

print(get_max_num(numbers))  # 92
print(get_max_index(numbers))  # 1
