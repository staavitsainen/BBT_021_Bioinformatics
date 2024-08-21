#!/usr/bin/env python3

import datetime
today_date = datetime.datetime.now()

name = input('What is your name? ')
print('Hello %s! :)' %name)
age = input('How old are you (Please enter a number e.g. 7)? ')
age = int(age)
year_born = today_date.year - age
print('%s, you were born in %s!\nNice to meet you! Bye! :)' %(name, year_born))
