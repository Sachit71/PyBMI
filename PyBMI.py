import sys
import pyautogui
x=pyautogui.prompt("Enter weight in Kg over here.")
y=pyautogui.prompt("Enter height in centimetres over here.")
#beta=pyautogui.prompt("Enter age her:")
x=float(x)
y=float(y)
alpha=y/100
z=pow(alpha,2.0)
a=x/z
z=float(z)
a=float(a)
#pyautogui.alert(a)
if (a<18.5):
    pyautogui.alert("Underweight")
a=float(a)
if 18.5<a<25:
    pyautogui.alert("Normal")
a=float(a)
if a>30:
    pyautogui.alert("Overweight")
a=float(a)
pyautogui.alert(a)
