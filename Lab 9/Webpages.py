import urllib.request
pagefile = urllib.request.urlopen("http://www.cs.otago.ac.nz")
page = pagefile.read()
print(page)