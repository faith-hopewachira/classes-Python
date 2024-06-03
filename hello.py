def hello(name):
    print(f"Hello my name is {name}")



def school(name, school_name):
    print(f"Hello {name}, you study at {school_name}")


def country(name, age , country):
    print(f"Hello my name is {name} and i am {age} years old. I come from {country}")


# def anagram(s1,s2):
#     if(Counter(s1)==Counter(s2)):
#         print("Anagrams")
#     else:
#         print("Not anagrams")


def anotherAnagram(s1,s2):
    if sorted(s1.lower()) == sorted(s2.lower()):
        print("anagram")
    else:
        print("not anagram")



def reverse(str):
    print(str[::-1])


def my_vowels(name, vowels):

    count = sum(name.count(vowel)for vowel in vowels)
    print(count)


def year_of_birth(name = "faith", age= 21):
    print(f"Hello {name} you were born in {2024 - age}")

def year_of_birth1(name,age):
    print(f"Hello {name} I am {age}")

def my_country(country = "Uganda"):
    print(f"Hello AkiraChix from {country}")



# n = 10
# d= dict()
# for x in range(1, n+1):
#     d[x] = x * x
# print(d)

# x = [1,2,3,4,5]
# y = [6,7,8,9,10]
# z = x + y
# print(z)

# name = "faith"
# a = name[::-1]
# print(a)



# def my_home(home_country = "Kenya"):


def greet(name):
    print(f"Hello{name}")




