from cgi import test
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random

# Function that goes through all the links in a specific div (indented group in page)
# Outder div is /html/body/div[2]/div[9]/div[outer_div]/a[1]
# We dont change a[1] here because we do that outside of the function
# Returns a list of the elements found in that div
# Could've done this in a double for loop, but I wanted to get some functions to help with visibility

def get_problems(outer_div, links_ls):
    try:
        for i in range(1, 20):
            x_path_iterator = "/html/body/div[2]/div[9]/div[" + str(outer_div) + "]/a[" + str(i) + ']'
            return_value = driver.find_element(By.XPATH, x_path_iterator)
            links_ls.append(return_value)

    except:
        return return_value

PATH = "E:\VS Code\DailyMath\chromedriver.exe"  # You should change this line to wherever your chromedriver.exe file is
#Random side note, the program versions (as in like v0.1 or v0.2.1 etc) I'm using I got from: https://stackoverflow.com/questions/396429/how-do-you-know-what-version-number-to-use

classes = {     # Dictionary of classes available in Paul's Online Math Notes websites
"Algebra" : 'Alg',
"Calc1" : 'CalcI',
"Calc2" : 'CalcII',
"Calc3" : 'CalcIII',
"All classes" : 'not yet implemented'
}

print("From the following classes: ")
print("")     # space for neatness
for key, value in classes.items():  # Loop to print out classes in dict
    print(key)

print("")     # space for neatness
inp = input("Which class do you want to get an exercise for? Please type the name exactly how it appears in the list above with no spaces then hit enter: ")

# Loop to catch if input was typed incorrectly
while True:     

    if inp in classes and inp != "All classes":
        problems_link = "https://tutorial.math.lamar.edu/Problems/" + classes[inp] + '/' + classes[inp] + ".aspx"
        break
    elif inp == "All classes":
        print("Sorry, not implemented yet. Still working on it! :)")
        # I believe there's a way to go straight to the else, but I can't remember how
        print("Please retry.")
        inp = input("Which class do you want to get an exercise for? ")
    else:
        print("Please retry.")
        inp = input("Which class do you want to get an exercise for? ")

driver = webdriver.Chrome(PATH)
driver.get(problems_link)  # Goes to Paul's online math notes Problems/user input page

# Example: /html/body/div[2]/div[9]/div[2]/a[1]
# /html/body/div[2]/div[9]/div[outer div]/a[inner div]
# I'm sure there's better named for those but that's how they made sense in my head
# Here only outer div matters because I took care of inner div in get_problems definition 
# Got the numbers by manually looking at the website's code and seeing the highest and lowest number for the outer div's
# Subtract 1 from the right number to get the real number, just have to add one for the range() function to fully reach, could've added 1 to i but it's the same thing

outer_div_ranges = {
    "Algebra" : [2, 9],
    "Calc1" : [2, 8],
    "Calc2" : [2, 8],
    "Calc3" : [2, 8]
}

links_with_problems = []
for i in range(outer_div_ranges[inp][0], outer_div_ranges[inp][1]):
    return_value = get_problems(i, links_with_problems)

for link in links_with_problems:
    print('link', link.get_attribute('href'))

exercise_topic = random.choice(links_with_problems)
print(exercise_topic)
driver.get(exercise_topic.get_attribute('href'))    # Go to the page that was randomly picked

# Right now, code just goes to a page with multiple problems. Which can be okay.
# If I want to make it where it goes to a specific problem there's a hurdle I need to get over.
# It's pretty much the same problem I had with the 'inner div' where I didn't know how many links there were in a page/section.
# I won't manually go look because that's a lot of work. 
# What I could do is write a try and except block and whenever I get an error I can record the number before the one that gave me the error and I'll know that's how many problems there are.
# The reason I need to know how many problems a page has is because the links to them are like this  .../Prob1.aspx .../Prob2.aspx .../Prob3.aspx and so on.
# So I need to know how far I need to go in order to pick a problem that's actually in the page

#driver.close()
