from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
PATH = "E:\VS Code\DailyMath\chromedriver.exe"

classes = {     # Dictionary of classes available in Paul's Online Math Notes websites
"Algebra" : 'Alg',
"Calc1" : 'CalcI',
"Calc2" : 'CalcII',
"Calc3" : 'CalcIII',
"Diff Eq" : 'DE',
"All classes" : 'not yet implemented'
}

print("From the following classes: ")
for key, value in classes.items():  # Loop to print out classes in dict
    print(key)
inp = input("Which class do you want to get a problem for? ")

driver = webdriver.Chrome(PATH)
problems_link = "https://tutorial.math.lamar.edu/Problems/" + classes[inp] + '/' + classes[inp] + ".aspx"
driver.get(problems_link)  # Paul's online math notes Problems/user input
#print(driver.title)
#assert "Pauls Online Math Notes" in driver.title    # Here for bug catching reasons. All this does is make sure "Pauls Online Math Notes" is the title of the website. Helps make sure the correct site was loaded properly

#driver.close()
