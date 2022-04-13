class StringUtility:

  def __init__(self,string):
    self.st = string
    
  '''
  Sets up the string that is used in other methods.
  Args:
    self[str]: inputted str
  Return: None
  '''
  
  def __str__(self):
   return self.st

  '''
  Returns the string that was set up in the init function.
  Args:
    self[str]: inputted str
  Return: 
  [str]: Returns the string that is used in other methods.
  '''
  
  def vowels(self):
    count = 0
    for c in str(self.st):
      if c in "aeiouAEIOU":
        count += 1
    if count < 5:
      return str(count)
    else:
      return "many"

  
  '''
  Counts the vowels in a given string
    self[str]: inputted str
  Return: 
  [str]: Returns the count if there are less than 5 vowels in a given string. 
  [str]: Returns the string 'many' if there are more than 5 vowels in a given string.
  '''
  

  def bothEnds(self):
    return (self.st[0] + self.st[1]+ self.st[-2]+ self.st[-1]) if len(self.st) > 2 else ""
  
  '''
 Takes the first and last two letters of a given string and combines them to form a new string.
  Args:
    self[str]: inputted str
  Return: 
  [str]: Returns the new string that was created if the string has more than 2 characters.
  [str]: Returns an empty string if the given string has less than two characters.
  '''    

  def fixStart(self):
    return (self.st[0]+self.st[1:].replace(self.st[0],'*')) if self.st.count(self.st[:0]) > 1 else self.st
    
    
  '''
  Takes the first character in a string and makes repeating characters into '*' while leaving the first character unchanged.
  Args:
    self[str]: inputted str
  Return: 
  [str]: Returns the new string that was created if the first character in the string repeats more than once.
  [str]: Returns the given string if the first character does not repeat in a string.
  '''    
    
     

  def asciiSum(self):
    return sum(ord(i) for i in self.st)

  '''
  Adds all the ascii values in a string.
  Args:
    self[str]: inputted str
  Return: 
  [int]: Returns the sum which is the total ascii value for the string.
  '''
  
  def cipher(self):
    lower = ("abcdefghijklmnopqrstuvwxyz")
    upper = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    my_string = self.st
    size = len(my_string)
    empty_string = " "
    new_string = ""
    for c in my_string:
      if c in lower:
        my_string = chr(((ord(c) + size - 97) % 26)+ 97) 
        new_string += my_string
      if c in upper:
        my_string = chr(((ord(c)+ size - 65) % 26)+ 65)
        new_string += my_string
      if c in empty_string:
        new_string = new_string + c
    return new_string     

  '''
  increments all letters in a given string by the length of the given string.
  Args:
    self[str]: inputted str
  Return: 
  [str]: The new string that was created after all the characters were shifted by the appropriate values.
  '''