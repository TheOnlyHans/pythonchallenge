import urllib.request
pc = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345')
print(pc.read())
