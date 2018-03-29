
# coding: utf-8

# In[1]:


def cal(mark,*args):
    x1 = 0
    x2 = 0

    for v in args:
        if x1 == 0:
            x1 = v
        else:
            x2 = v

    if(mark == "+"):
        print(x1,"+",x2,"=",(x1+x2))
    elif(mark == "-"):
        print(x1,"-",x2,"=",(x1-x2))
    elif(mark == "*"):
        print(x1,"x",x2,"=",(x1*x2))
    elif(mark == "/"):
        print(x1,"÷",x2,"=",(x1/x2))

