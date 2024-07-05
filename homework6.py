my_dict={'osina':22,'el':40,'bereza':79}
print('Dict: ',my_dict)
print(my_dict.get('el'))
print(my_dict.get('ysen'))
my_dict.update({'dyb':22,'olha':81})
print('Deleted value: ',my_dict.pop('osina'))
print('Modified dictonary:',my_dict)
my_set={0,True,2,True,'Red',2,11,8}
print('Set: ',my_set)
my_set.update({3,'Len'})
my_set.remove(11)
print('Modified set: ',my_set)