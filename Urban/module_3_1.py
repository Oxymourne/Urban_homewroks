calls = 0


def count_calls():
    global calls
    calls += 1
    return calls


def string_info(string):
    count_calls()
    res = (len(string), string.upper(), string.lower())
    return res


def is_contains(string, list_to_search):
    count_calls()
    for i in range(len(list_to_search)):
        list_to_search[i] = list_to_search[i].lower()
    if string.lower() in list_to_search:
        return True
    else:
        return False


print(string_info('Capybara'))

print(string_info('KeSha'))

print(string_info('Armageddon'))

print(string_info('BuLLet'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN

print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches

print(is_contains('BaLl', ['ReaDy', 'Study', 'BALL']))  # No matches

print(calls)
