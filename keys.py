"""
Write three functions:
sort1(langauges)
sort2(languages)
sort3(langauges)
Goal: Print exactly the below w/ three functions:
1:
    Arabic
    English
    Koine Greek
    Latin
    Romanian
    C++
    JavaScript
    Python
    R
2:
    R
    C++
    Latin
    Arabic
    Python
    English
    Romanian
    JavaScript
    Koine Greek
3:
    JavaScript
    R
    Latin
    Python
    Romanian
    Koine Greek
    English
    Arabic
    C++
"""
languages = {'JavaScript': 'P',
             'Arabic': 'N',
             'R': 'P',
             'Python': 'P',
             'C++': 'P',
             'Koine Greek': 'N',
             'Latin': 'N',
             'Romanian': 'N',
             'English': 'N'}

def divide_list(dictionary):
    dictionary_two = {}
    dictionary_one = {}
    for key in dictionary:
        if languages[key] == 'P':
            dictionary_two[key] = 'P'
        if languages[key] == 'N':
            dictionary_one[key] = 'N'
    return dictionary_one, dictionary_two

x, y = divide_list(languages)

def printing(dictionary):
    for key in sorted(dictionary.keys()):
        print(key)

printing(x)
priting(y)

def sort1(d):
    lst = sorted(sorted(d), key=d.__getitem__)
    print("1:")
    for x in lst:
        print("\t" + x)

sort1(languages)


def sort2(d):
    lst = sorted(d, key=len)
    print('2:')
    for item in lst:
        print("\t" + item)

sort2(languages)

def sort3(d):
    lst = sorted(sorted(d), key=last_char, reverse=True)
    #sorted(d) only shows the dictionary keys, not the values
    print("3:")
    for item in lst:
        print("\t" + item)

def last_char(d):
    return string[-1].lower()
