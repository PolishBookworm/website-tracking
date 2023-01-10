# Main code of the project

from requests import get
from bs4 import BeautifulSoup
from csv import reader, writer

# Printing and updating list of checked websites
print("These are the websites I am going to check:")
with open("sites.csv") as file:
    data = reader(file)
    for row in data:
        print(f"{row[0]} ({row[1]})")
while input("Would you like to add more? (y/n) ") == "y":
    with open("sites.csv", "a+") as file:
        write = writer(file)
        name = input("Enter site name: ")
        url = input("Enter site url: ")
        tag = input("What tags would you like to check? ")
        list_of_content = BeautifulSoup(
            get(url).content, "html.parser").select(tag)
        content = []
        for element in list_of_content:
            content.append(element.text)
        write.writerow([name, url, tag, content])


# TODO
# * Finish, of course
# * Denest
