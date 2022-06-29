# Main code of the project

from requests import get
from bs4 import BeautifulSoup
from csv import reader, writer

print("These are the websites I am going to check:")
with open("sites.csv") as file:
    data = reader(file)
    for row in data:
        print(row)
if input("Would you like to add more? (y/n) ") == "y":
    with open("sites.csv", "a+") as file:
        write = writer(file)
        while input("Continue? (y/n) ") == "y":
            name = input("Enter site name: ")
            url = input("Enter site url: ")
            write.writerow([name, url])