# Smart-Facial-Recognition-Doorlock-

This is the Readme file of ECE 5466 Team 5 final project

To use the raspberry pi, you should first download the system - Raspbian, and install it. Here is the link of the install guild:
https://www.youtube.com/watch?v=ntaXWS8Lk34

Hardware part
We need Raspberry pi, LED, Button, photoregister, servo motor. These things can buy through amazon or in local place like micro-center.
You need to follow the picture in the final report to connect the circuit to the raspberry pi.

Software part
You need to follow the guideline in report or other online resources to correctly install OpenCV package(For both PC and Raspberry Pi)
https://www.geeksforgeeks.org/how-to-install-opencv-for-python-in-windows/
You will need Python and Visual Studio to programming and training existing module
https://visualstudio.microsoft.com/
For the specific code please refer to attached FRcode.py file, it covers all codes including facial recognition, tolerance change and image transmission.

Reminder
You need to download an app called IFTTT on your phone.
Here is the website of IFTTT:https://ifttt.com/explore
And go to ITFFF web page to create an event. And change the code in the facial recognition part as your trigger code. Here is the guild:
https://www.labno3.com/2021/08/09/using-ifttt-with-the-raspberry-pi/

Remote control
Then you need to use your raspberry pi to build a web server. Install apache2, php5, Wiring pi and other packages. Here are the guilds:
Wiring pi:http://wiringpi.com/download-and-install/
Apache2 and php5:https://www.raspberrypi.com/documentation/computers/remote-access.html
Then install the android app to your phone. Remember to change the IP address of the web server into the one you created.


Detailed steps
Setup all the things above, then put light.py, lock1.py, index.php, test.py in raspberry pi. Put execute.py and PythonApplication3.py in your computer. Run test.py in your raspberry pi. Also run execute.py and PythonApplication3.py if you want to start your work in your computer.
