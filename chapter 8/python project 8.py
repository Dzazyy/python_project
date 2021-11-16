my_list = [{'name':'Homer', 'age':39}, {'name':'Bart', 'age':10}]

my_list.sort(lambda x,y : cmp(x['name'], y['name']))
print(my_list)