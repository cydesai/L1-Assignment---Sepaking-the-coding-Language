#Following Code will check if given text string is Palindrome or not

def is_palindrome(text):
  import re
  Special_char = ",!.?'-"
  if len(text)<=1000:
    text1=re.sub("[,!.?'-]","",text)
    #print(text1)
    text1 = text1.lower()
    text1 = text1.replace(" ","")
    if text1 == text1[::-1]:
      print("YES")
    else:
      print("NO")

text = "Too hot to hoot."
is_palindrome(text)
