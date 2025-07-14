def to_base(n, base):
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if n == 0:
        return '0'
    result = ''
    while n > 0:
        n, r = divmod(n, base)
        result = digits[r] + result
    return result


num, base = map(int, input().split())

print(to_base(num, base))
