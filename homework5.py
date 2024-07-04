immutable_var=5,'food',[7,8],True
print(immutable_var)
immutable_var[2][0]=4
print(immutable_var) #изменить можно только список внутри кортежа, сам же кортеж явлется не изменяемым типом данных
metable_list=[True,'string',23,11]
print(metable_list)
metable_list.extend(['forest',1])
metable_list.remove('string')
print(metable_list)
