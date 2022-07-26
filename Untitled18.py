#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[4]:


def test():
    #empty string
    assert(add("")==0),"empty string doesn't return 0"
    
    #1 number
    assert(add("1")==1),"string \"1\" doesn't return 1"
    assert(add("2")==2),"string \"2\" doesn't return 2"

     #2 number
    assert(add("1,2")==3),"string \"1,2\" doesn't return 3"
    assert(add("2,3")==5),"string \"2,3\" doesn't return 5"
    
     #3 number
    assert(add("1,2,3")==6),"string \"1,2,3\" doesn't return 6"
    assert(add("2,3,6")==11),"string \"2,3,6\" doesn't return 11"

     #1 number
    assert(add("1,2,3,4")==10),"string \"1,2,3,4\" doesn't return 10"
    assert(add("1,4,5,6")==16),"string \"1,4,5,6\" doesn't return 16"
    
     #Handle new lines
    assert(add("1\n2")==3),"string \"1\n2\" doesn't return 3"
    assert(add("3\n4")==7),"string \"3\n4\" doesn't return 7"
    
    assert(add("//;\n1;2")),"string \"//;\n1;2\" doesn't return 3"
   
    
    print('PASSED ALL TESTS')

def add(numbersString):
    if len(numbersString)==0:
        return 0
    elif len(numbersString) == 1:
        return int(numbersString)
    elif numbersString[0] == "-": raise Exception('negatives not allowed ' )
    elif numbersString[0] == "/":
        result = 0
        delim=""
        lines= numbersString.split("\n")
        for char in range(2,len(lines[0])):
            delim=delim+lines[0][char]
        numbers = lines[1].split(delim) 
        return multipleNumbers(numbers)
    

    else:
        result = 0
        delim = ","
        if numbersString[1] !=",":
            delim = "\n"
        numbers = numbersString.split(delim)
        return multipleNumbers(numbers)

    
def multipleNumbers(numbers):
    result=0
    for num in numbers:
        result +=int(num)
    return result


test()


# In[ ]:




