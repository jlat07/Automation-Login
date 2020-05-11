# Automation-Login
![Login GIF](https://media.giphy.com/media/kEhjZr7aMUoVVV3eOt/giphy.gif)  

The goal is to have an Automation Library to help carry out a repetitive task with ease to save time or also be utilized as a fail-safe in the event you forget.

This login script came about while in my coding boot camp during the *Covid-19 stay-at-home pandemic*. Even though we were working from home remotely, we still had to sign in to our portal, and click an attendance button daily. Sounds easy enough, but if we can automate the process to avoid forgetting, why not. 

---
**Requirements:**  
Pip install selenium, and download necessary drivers needed for the browswer of your choice, I used chrome. Depending how you utilize enviroment variables you may or may not need dotenv, your choice.
- selenium (https://pypi.org/project/selenium/)  
-  - Driver: Chrome  
- dotenv (https://pypi.org/project/python-dotenv/)  

**Set environment variables in .env file**  
*URL="link-to-website"*  
*username: "Johnny@email.com"*  
*password: "@pples33d"*  

**The script uses Selenium Webdriver to automate the process:**  
v1 uses the chrome browser, that opens up on the screen and carries out the process.  
v2 uses a headless Chrome browser, that carries out the process in the background.  

**Adding terminal functionality**  
Set up a .bash/.zshrc alias to run the script from the terminal easily.  
*alias login_zcw="python <Path-to-Attendance_Script_v2_Headless.py>"*  

**Cron Job**  
As a backup, you can add it to cron jobs that would run on specific dates and times purely as a backup. I set mine up for 7:55 am and 8:55 am, M-F. (Remember computer must be on and awake for cron jobs to run. Aslo depending on your shell you may not be able to use an alias like the example below. You will need to write out full path to the script.)   
*55 7 * * 1-5 login_zcw*  
*55 8 * * 1-5 login_zcw* 
 
 **Future Features**  
*Screenshot feature in the workings, that takes and saves a screenshot of the browser once attendance is submitted for extra assurance.*