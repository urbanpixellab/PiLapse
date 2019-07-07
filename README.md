# PiLapse
# PiLapse

##websserver 
edit/add  sudo nano /etc/rc.local
cd /home/somedir
python -m SimpleHTTPServer &

##cron load python script at reboot, no sudo!!!
edit/add crontab -e
@reboot python /home/pi/timelapesSimple.py &

