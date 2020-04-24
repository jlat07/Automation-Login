# Automation-Login
![Login GIF](https://media.giphy.com/media/kEhjZr7aMUoVVV3eOt/giphy.gif)  

The goal is to have an Automation Library to help carry out a repetitive task with ease to save time or also be utilized as a fail-safe in the event you forget.

This login script came about while in my coding boot camp during the Covid-19 stay at home era. Even though we were working from home remotely, we still had to sign in to our portal, and click an attendance button daily. Sounds easy enough, but if we can automate the process to avoid forgetting, why not. 

---
**Set environment variables in .env file**  
*URL="link-to-website"*  
*username: "Johnny@email.com"*  
*password: "@pples33d"*  

**The script uses Selenium Webdriver to automate the process:**  
v1 uses the chrome browser, that opens up on the screen and carries out the process.  
v2 uses a headless browser, that carries out the process in the background.  

**Adding terminal functionality**  
Set up a .bash/.zshrc alias to run the script from the terminal easily.  
*alias login_zcw="python <Path-to-Attendance_Script_v2_Headless.py>"*  

**Cron Job**  
As a backup, you can add it to cron jobs that would run on specific dates and times purely as a backup. I set mine up for 7:55 am and 8:55 am, M-F. (Remember computer must be and awake for cron jobs to run)   
*55 7 * * 1-5 login_zcw*  
*55 8 * * 1-5 login_zcw* 
 
 **Future Features**  
*Screenshot feature in the workings, that saves an image once logged in for extra assurance.*