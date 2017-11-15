import urllib.request
'''
y= 12345
new = ''
pc = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+str(y))
x = pc.readline()
y = str(x)
print(y[1:5])


x = x[::-1]
for char in x:
    if str(char).isdigit():
        new += str(x)
x = new
print(x[1])
'''



count = 1
nothing = 12345

while count < 401:
    pc = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+str(nothing))
    x = str(pc.read())
    nothing = ''
    for num in x:
        if num.isdigit():
            nothing += str(num)
    print(nothing)
    count +=1
    
