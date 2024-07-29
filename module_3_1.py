calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    r = len(string)
    d = string.lower()
    s = string.upper()
    gg = (r, s, d)
    return gg
def is_contains(string, list_to_search):
    count_calls()
    new_list_to_search = [i.casefold() for i in list_to_search]
    string = string.casefold()
    if string in new_list_to_search:
        return True
    else:
        return False
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
