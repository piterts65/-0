calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()
def is_contains(string,list_to_search):
    count_calls()
    string = string.lower()
    for i in list_to_search:
        if i.lower() == string:
           return True
    return False
        
print(string_info('CopyBARA'))
print(string_info('armfgeDon'))
print(string_info('TicHer'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))# Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))# No matches
print(is_contains('Glass',['Klass','шанс','glasS','pass']))# Glass ~ glasS
print(calls)





















