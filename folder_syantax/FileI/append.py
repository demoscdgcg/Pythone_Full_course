# append an exsiting  a file called John Doe.txt it should contain data about John Doe Home town

f=open("John Doe.txt", "a")

string ='''
John Doe  intially lived in the phonex .
he is a very nice guy
'''

f.write(string)
