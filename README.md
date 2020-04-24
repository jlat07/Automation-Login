# Automation-Login
The goal is to have an Automation Library to help carryout repetitive task with ease to save time or also be utilized as a fail safe in the event you forget to do it.

This login script came about while in my coding boot camp during the Covid-19 stay at home era. Even though we were working from home remotely, we still had to sign into our portal, and click an attendance button daily. Sounds easy enough, but if we can automate the process to avoid forgetting, why not.

v1 uses the chrome browser, that opens up on screen and carries out the process.
v2 uses a headless browser, that carries out the process in the background.

Set up a .bash/.zshrc alias to run the script from the terminal easily.  
*alias login_zcw='python <Path-to-Attendance_Script_v2_Headless.py>'*

Then added a cron job, as a back up that would run the scrip on specific dates and times as backup.  
*55 7 * * 1-5 login_zcw*


