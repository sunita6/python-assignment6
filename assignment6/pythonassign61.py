print("convert to a dictionary in one line code using list comprehension(without using zip method)")
list1=[1,2,3,4,5,6,7,8]
list2=["a","b","c","d","e"]
mydict={list1[i]:list2[i] for i in range(len(list2))}
print(mydict)

#output

#convert to a dictionary in one line code using list comprehension(without using zip method)
#{1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

