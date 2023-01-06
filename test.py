import pandas as pd

data = pd.read_csv("birthdays.csv")

with open("letter_templates/letter_2.txt") as file:
    contents = file.read()
    contents = contents.replace("[NAME]", "KD")
print(contents)