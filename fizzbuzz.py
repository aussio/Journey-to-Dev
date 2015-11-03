
def test_fizz_buzz():
    print('If this test is successful, it will return True all three times.')
    print fizz_buzz(15) == "1\n2\nfizz\n4\nbuzz\nfizz\n7\n8\nfizz\nbuzz\n11\nfizz\n13\n14\nfizzbuzz\n"
    print fizz_buzz(18) == "1\n2\nfizz\n4\nbuzz\nfizz\n7\n8\nfizz\nbuzz\n11\nfizz\n13\n14\nfizzbuzz\n16\n17\nfizz\n"
    print fizz_buzz(21) == "1\n2\nfizz\n4\nbuzz\nfizz\n7\n8\nfizz\nbuzz\n11\nfizz\n13\n14\nfizzbuzz\n16\n17\nfizz\n19\nbuzz\nfizz\n"

"""
This is an example of the quickest solution I could think of.
"""
def fizz_buzz(integer):
    output = ""

    for number in range(integer + 1)[1:]:
        if number % 15 == 0:
            output += 'fizzbuzz\n'
        elif number % 5 == 0:
            output += 'buzz\n'
        elif number % 3 == 0:
            output += 'fizz\n'
        else:
            output += '{}\n'.format(number)

    return output

if __name__ == '__main__':
    test_fizz_buzz()
