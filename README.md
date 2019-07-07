# PiLapse
Is an Pi based timelapse camera running endless by python and a webserver serving the last image on port 8080/8000 


## starting websserver, script not working by now, good if it could be done inside python
edit/add  sudo nano /etc/rc.local

cd /home/somedir
python -m SimpleHTTPServer &

## cron load python script at reboot, dont use sudo cron!!!
edit/add crontab -e

@reboot python /home/pi/timelapesSimple.py &

