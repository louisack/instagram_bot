## select first tem on list##
import csv


with open("temp.csv", encoding= "utf8") as f:
    content = csv.reader(f)
    dict = {}
    for row in content:
        # row is a list of strings
        # use string.join to put them together
        dict[row[0]] =row[-3]
    del dict["Title"]
    print(dict)

captions = list(dict.keys())
urls = list(dict.values())
print_url=str(urls[0])
print(print_url)
print(captions[0])
x = captions[0]
print(x)
y = x.split(" ")
y.append(".jpg")
z = "-".join(y)

print(z)




try:
    from urllib.request import urlretrieve
except ImportError:
    from urllib import urlretrieve

urlretrieve(print_url, z)




