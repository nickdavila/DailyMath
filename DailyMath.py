from distutils.spawn import find_executable
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random

PATH = "E:\VS Code\DailyMath\chromedriver.exe"  # You should change this line to wherever your chromedriver.exe file is
#Random side note, the program versions (as in like v0.1 or v0.2.1 etc) I'm using I got from: https://stackoverflow.com/questions/396429/how-do-you-know-what-version-number-to-use

classes = {     # Dictionary of classes available in Paul's Online Math Notes websites
"Algebra" : 'Alg',
"Calc1" : 'CalcI',
"Calc2" : 'CalcII',
"Calc3" : 'CalcIII',
"Diff Eq" : 'DE',
"All classes" : 'not yet implemented'
}

print("From the following classes: ")
print("")     # space for neatness
for key, value in classes.items():  # Loop to print out classes in dict
    print(key)

print("")     # space for neatness
inp = input("Which class do you want to get an exercise for? Please type the name exactly how it appears in the list above with no spaces then hit enter. ")

# Loop to catch if input was typed incorrectly
while True:     

    if inp in classes:
        problems_link = "https://tutorial.math.lamar.edu/Problems/" + classes[inp] + '/' + classes[inp] + ".aspx"
        break
    else:
        print("Please retry.")
        inp = input("Which class do you want to get an exercise for? ")

driver = webdriver.Chrome(PATH)
driver.get(problems_link)  # Paul's online math notes Problems/user input
all_links = driver.find_elements(By.CLASS_NAME, 'introlink')

exercise_topic = random.choice(all_links)
print(exercise_topic.get_attribute('href'))
driver.get(exercise_topic.get_attribute('href'))


#driver.close()
