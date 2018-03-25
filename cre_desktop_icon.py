#!/usr/bin/python3
import os

exe_name = str(input("please input the exe's name : ")).strip()
startup = str(input("please input the start command : ")).strip()
icon_path = str(input("please input the icon's path : ")).strip()

content = """[Desktop Entry]
Type=Application
Exec={eexec}
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name[en_US]={name}
Name={name}
Comment[en_US]=
Comment=
Icon={icon}
""".format(eexec=startup, name=exe_name, icon=icon_path)

filename = exe_name+'.desktop'
with open(filename, 'w') as f:
    f.write(content)
    
os.system('chmod 755 *.desktop && mv *.desktop ~/Desktop')

