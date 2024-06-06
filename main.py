questionNum = input('Input the question number that you want to run the code for: ')

try:
  __import__('question'+questionNum)
  
except ModuleNotFoundError:
  print('I did not write code for that question')