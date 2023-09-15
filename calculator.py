#!/usr/bin/env python
# coding: utf-8

# In[1]:


import ipywidgets as widgets
from IPython.display import display
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b == 0:
        raise valueError("Cannot divide by 0")
        return a/b
    
#create input widgets
num1 = widgets.FloatText(description = "Enter Number 1:")
num2 = widgets.FloatText(description = "Enter Number 2:")

#Create buttons for operations
add_button = widgets.Button(description="Add")
subtract_button = widgets.Button(description="Subtract")
multiply_button = widgets.Button(description="Multiply")
divide_button = widgets.Button(description="Divide")

#Create a label for the result
result_label = widgets.Label()

def on_add_button_click(b):
    try:
        result = (num1.value+num2.value)
        result_label.value="Result:" + str(result)
    except Exception as e:
             result_label.value="Error:" + str(e)
    
def on_subtract_button_click(b):
    try:
        result = (num1.value-num2.value)
        result_label.value="Result:" + str(result)
    except Exception as e:
             result_label.value="Error:" + str(e)
def on_multiply_button_click(b):
    try:
        result = (num1.value*num2.value)
        result_label.value="Result:" + str(result)
    except Exception as e:
             result_label.value="Error:" + str(e)               
def on_divide_button_click(b):
    try:
        result = (num1.value/num2.value)
        result_label.value="Result:" + str(result)
    except Exception as e:
             result_label.value="Error:" + str(e)  
                
add_button.on_click(on_add_button_click)
subtract_button.on_click(on_subtract_button_click)
multiply_button.on_click(on_multiply_button_click)
divide_button.on_click(on_divide_button_click)

#Display the widgets
display(num1, num2, add_button, subtract_button, multiply_button, divide_button, result_label)


# In[ ]:




