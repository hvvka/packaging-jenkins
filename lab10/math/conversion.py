def decimal_to_binary(number):
    """
        Calculates the decimal of the given binary number
        :param number: decimal number in string or integer format
        :return integer of the equivalent decimal number
    """
    decimal = []
    number = list(str(number)[::-1])
    for i in range(len(number)):
        decimal.append(int(number[i]) * (2 ** i))

    return sum(decimal)


def binary_to_decimal(number):
    """
        Calculates the binary of the given decimal number
        :param number: decimal number in string or integer format
        :return : string of the equivalent binary number
    """
    if isinstance(number, str):
        number = int(number)
    binary = []
    while number >= 1:
        remainder = number % 2
        binary.append(remainder)
        number = number // 2

    return ''.join(map(str, binary[::-1]))


def decimal_to_hex(number):
    """
        Calculates the decimal of the given hex number
        :param number: hex number in string or integer format
        :return integer of the equivalent decimal number
    """
    decimal = []
    decimal_equivalents = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    number = list(str(number)[::-1])
    for i in range(len(number)):
        try:
            if int(number[i]) < 10:
                decimal.append(int(number[i]) * (16 ** i))
        except ValueError:
            decimal.append(decimal_equivalents[number[i]] * (16 ** i))

    return sum(decimal)


def hex_to_decimal(number):
    """
        Calculates the hex of the given decimal number
        :param number: decimal number in string or integer format
        :return string of the equivalent hex number
    """
    if isinstance(number, str):
        number = int(number)
    hexadec = []
    hex_equivalents = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    while number >= 1:
        remainder = number % 16
        if remainder < 10:
            hexadec.append(remainder)
        elif remainder >= 10:
            hexadec.append(hex_equivalents[remainder])

        number = number // 16

    return ''.join(map(str, hexadec[::-1]))

