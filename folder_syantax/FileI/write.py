# write a file called John Doe.txt it should contain data about John Doe

f=open("John Doe.txt", "wt")

string ='''
John Doe is a nice guy. He lives in Nyc and he works with
python
His favorite is apndas
'''

f.write(string)
