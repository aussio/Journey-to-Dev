
def test_luhn_function():
    print('If successful, this will print True, False, False, True')

    print is_luhn_number(49927398716)
    print is_luhn_number(49927398717)
    print is_luhn_number(1234567812345678)
    print is_luhn_number(1234567812345670)


def is_luhn_number(card_number):
    """
    0) The rightmost digit is the check number. Excluding this number, then:
        1) From the (second)rightmost digit, double every-other digit.
             - if the product is greater than 9 (more than one digit), sum those digits.
        2) Take the sum of all digits, including those made in step 1.
    3) if the sum * 9, mod 10, is equal to your check number, then pass.
    """
    card_number_iterable = [int(digit) for digit in str(card_number)]
    check_digit = card_number_iterable[-1]
    odd_digits = card_number_iterable[-2::-2]
    even_digits = card_number_iterable[-3::-2]

    result_sum = sum(even_digits)
    for digit in odd_digits:
        if digit > 4:
            result_sum += (2*digit - 9)
        else:
            result_sum += (2*digit)

    return (result_sum * 9) % 10 == check_digit

if __name__ == '__main__':
    test_luhn_function()
