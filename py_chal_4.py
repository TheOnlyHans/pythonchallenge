import urllib.request
pc = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345')
x = pc.read()[-1:-6:-1]
x = x[::-1]
print(x)