Based on RPI-Info-Screen
========================

See http://www.raspberrypi.org/phpBB3/viewtopic.php?f=41&amp;t=51807

BETA VERSION - EXPECT ERRORS!

Before running:  
1) Remove the plugin folders you don't want to use (I haven't got round to implementing a way of enabling/disabing plugins yet).  
2) Edit default.py - Line 16 sets the screen size (this will be moved into a config file at some point)  
3) Run default.py  
4) Pressing "n" moves between screens, "q" quits (this should be handled by GPIO at a later date)  

Any problems, you can post issues on GitHub and I may take a look!

Config directory can be used on a fresh raspbian to configure a 5$ ili9341 2.2.inch tft
Boot console is visible right after firmware upgrade and reboot
Configured for the following GPIO : reset:25,led:18,dc:24
