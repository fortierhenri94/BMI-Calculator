#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#BMI = (weight in pounds x 703) / (height in inches x height in inches)


# In[26]:


name = input("Enter your name: ")

weight = int(input("Enter your weight in pounds: "))

height = int(input("Enter your height in inches: "))

BMI = (weight * 703) / (height * height)

print(BMI)

if BMI > 0:
    if(BMI < 18.5):
        print(name + " is underweight")
    elif(BMI < 25):
        print(name + " is normal weight")
    elif(BMI < 30):
        print(name + " is overweight")
    elif(BMI < 35):
        print(name + " is obese")
    elif(BMI < 40):
        print(name + " is severely Obese")
    elif(BMI >= 40):
        print(name + " is morbidly Obese")
    else:
        print(name + "Please enter valid inputs")


# In[24]:


print(weight)


# In[18]:


type(weight)


# In[7]:





# In[ ]:





# In[ ]:




