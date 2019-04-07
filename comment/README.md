# CMD

```bash
sudo apt-get update
sudo apt-get -y install apache2 libapache2-mod-wsgi-py3 python3-pip python3-django
sudo  apt-get install mysql-server mysql-client libmysqlclient-dev python3-dev
sudo apt-get install git-core
sudo nano .bashrc

######## ADDED BY FAISAL ######
export LC_CTYPE=en_US.UTF-8
export LC_ALL=en_US.UTF-8
############################

source .bashrc
sudo a2enmod wsgi
sudo service apache2 restart
sudo a2dissite 000-default
sudo pip3 install virtualenv


######### EDIT #######
Allowed host
####################

./manage.py makemigrations	
./manage.py migrate
./manage.py createsuperuser

./manage.py collectstatic
deactivate

sudo nano /etc/apache2/sites-available/000-default.conf
 
```

```
<VirtualHost *:80>
	DocumentRoot /home/ubuntu/sites/aria16/
	ServerName aria16.in
    ServerAlias aria16.in *.aria16.in
	ServerAdmin faisal_manzer@yahoo.in
	WSGIDaemonProcess aria16.in python-home=/home/ubuntu/sites/aria16/venv python-path=/home/ubuntu/sites/aria16
	WSGIProcessGroup aria16.in

	WSGIScriptAlias / /home/ubuntu/sites/aria16/__aria16__/wsgi.py process-group=aria16.in

	<Directory /home/ubuntu/sites/aria16/__aria16__>
		<Files wsgi.py>
			Require all granted
		</Files>
	</Directory>

	Alias /static /home/ubuntu/sites/aria16/static
	<Directory /home/ubuntu/sites/aria16/static>
		Require all granted
	</Directory>

    Alias /media /home/ubuntu/sites/aria16/media
	<Directory /home/ubuntu/sites/aria16/media>
		Require all granted
	</Directory>
</VirtualHost>
```