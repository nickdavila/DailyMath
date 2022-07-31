<div id="top"></div>

<div align="center">

[![LinkedIn][linkedin-shield]][linkedin-url]

# DailyMath v0.2
 A program to give me a daily math (Algebra to Differential Equations) problem to solve. 
  


</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About Of The Project</a>
    </li>
    <li><a href="#prerequisites">Prerequisites</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

I've always liked the idea of having a brain 'warm-up' much like stretching before exercise. Usually I play chess or try and find some type of brain teaser, but I recently started to realize that I have been forgetting my basic maths. So I'm creating a web-scraper to go through 'Paul's Online Math Notes' and give a random problem from his website (https://tutorial.math.lamar.edu/). All credits for the math problems go to him!




<p align="right">(<a href="#top">back to top</a>)</p>

## Prerequisites

As of 7/31/2022 (v0.2)

Import the following libraries:

```
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random


# Can use pip install for these
```
If you have any trouble with selenium, you can go to the website: https://selenium-python.readthedocs.io/

### Installation

Before running:

IF YOU ARE USING CHROME you should change the following line of code to wherever your chromedriver.exe file is

PATH = "E:\VS Code\DailyMath\chromedriver.exe"

You really only need to download and run the python file. Depending on your browser you might need a specific driver somewhere too, like for example if you're using chrome (like me) then you'll also need the chromedriver.exe which might be outdated depending on when you're reading this. To download that you can go to https://chromedriver.chromium.org/home.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

I use VS code with the virtual environment (DailyMathVenv) that you can see in the repository. All I do is click the run button in Visual Studio and this is what I see:

From the following classes: 

Algebra

Calc1

Calc2

Calc3

Diff Eq

All classes (ideally, but not yet implemented)

Which class do you want to get a problem for?

From there I just type in one of the class names

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Make more user friendly by checking if mispelled. Should allow for easy retrying to type the name and not have to re-run program
- [x] Right now not really scraping just re-directing to problems for each website, so actually scrape the website
- [ ] Have a way to make more questions more random (worried about repeating questions), or have some sort of question pool and people can opt to choose if they want to see that question again or not
- [ ] Quick way to restart so that if a problem is repeat/too easy, can get a new problem
- [ ] Implement a way for people to get problems from all the classes in a question pool
- [ ] Make this a GUI one day

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

If you have a suggestion that would make this better, please fork the repo and create a pull request or you can also simply email me!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Nick Davila - ndavila@utexas.edu

Project Link: [https://github.com/nickdavila/LAE-ML-Classification](https://github.com/nickdavila/LAE-ML-Classification)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* Thank you to Paul Dawkins of Lamar University (author of Paul's Online Math Notes) for his amazing teaching and math exercises.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License.

[MIT](https://choosealicense.com/licenses/mit/)

<p align="right">(<a href="#top">back to top</a>)</p>

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/nickmdavila/
[product-screenshot]: images/cns_urf_2022_poster-1.jpg
