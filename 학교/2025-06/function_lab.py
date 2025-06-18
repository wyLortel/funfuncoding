# Lab 1
def print_hello():
    print("Hello, World")


# Lab 2 - 1
def sum_numbers(a, b):
    return a + b


# Lab 2 - 2
sum_numbers_v2 = lambda a, b: a + b


# Lab 3
def greet_user(name):
    print("Hello, " + name)


# Lab 4
def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


# Lab 5
def is_even(arg_num):
    return arg_num % 2 == 0


# Lab 6
def wrap_in_tag(arg_tag, arg_content):
    return f"<{arg_tag}>{arg_content}</{arg_tag}>"


# Lab 7
def contains(arg_list, arg_target):
    for val in arg_list:
        if val == arg_target:
            return True

    return False


# Lab 8
def calculate_average(*args):
    num_item = len(args)

    if num_item == 0:
        return 0, 0, 0

    sum = 0
    for val in args:
        sum += val

    avg = sum / num_item

    return num_item, sum, avg


# Lab 9
def student_score(name, **scores):
    print(f"{name}의 성적:")
    sum = 0
    for sub, score in scores.items():
        print(f"-{sub}:\t{score}점")
        sum += score
    print(f"총점:\t{sum}점")


# Lab 10
def calc_price(product, price, tax=0.1):
    print(f"{product}의 최종 가격은 {(price + price * tax):.0f}원 입니다")


# Lab 11
def add_numbers(*args, **kwargs):

    options = ["abs", "only_even", "unique"]

    if len(kwargs) > len(options):
        return None

    for key in kwargs:
        if key not in options:
            return None

    values = list(args)

    if "abs" in kwargs and kwargs["abs"] == True:
        for idx, val in enumerate(values):
            if val < 0:
                values[idx] = -val

    if "only_even" in kwargs and kwargs["only_even"] == True:
        values = [v for v in values if v % 2 == 0]

    if "unique" in kwargs and kwargs["unique"] == True:
        temp = []
        for val in values:
            if val not in temp:
                temp.append(val)
        values = temp

    total = 0
    for val in values:
        total += val

    print(f"합계는 {total}입니다")


# Lab 12
def generate_profile(name, age, gender="미정", *interests, **metadata):
    print(f"[고객 프로필]")
    print(f"이름: {name}")
    print(f"나이: {age}")
    print(f"성별: {gender}")

    if len(interests) > 0:
        print(f"관심사: ", end="")
        last_idx = len(interests) - 1
        for idx, val in enumerate(interests):
            print(f"{val}{(", " if idx != last_idx else "\n")}", end="")

    if len(metadata) > 0:
        print(f"추가정보: ", end="")
        last_idx = len(metadata) - 1
        for idx, (key, val) in enumerate(metadata.items()):
            print(f"{val}{(", " if idx != last_idx else "\n")}", end="")
