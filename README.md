# PyDar
Python powered wifi radar!

## What is this?
PyDar is a Command and Control web server and script suite for interacting with Wifi interfaces; using a mixture of Scapy and Aircrack-ng on the back end, PyDar can be used for things like sniffng and deauthing. Additionally, PyDar is meant to provide the means to control servo motors either through a RaspberryPi's GPIO pins or via an Arduino. The idea behind that (see diagram below) is that PyDar will be used to control a Wifi Antenna (or Cantenna) mounted on a servo, and based on wifi strength measurements, can be used to best position the antenna where the strength of the desired wifi signal is the strongest, much like swiveling a radar dish to get the best broadcast strength (hence PyDar).

Pydar is still very much in it's infancy. Infact, it still has a lot of features and tasks to build out, the full Project board can be found [here](https://github.com/edrapac/PyDar/projects/1)

### v1. Software Requirements
Right now PyDar only has Linux support, and has been specifically confirmed to work on Ubuntu, Debian, and Raspbian. Below are the software configs for getting it working. Omit the Web Server configs if you are only interested in running the CLI tools

<b>Web Server Configs</b>
Apache `sudo apt-get install apache2`
PHP `sudo apt-get install php` 

Visudo entry 
```
www-data ALL=(ALL) NOPASSWD:/usr/bin/pinout
www-data ALL=(ALL) NOPASSWD:/home/pi/PyDar/move_left.py
www-data ALL=(ALL) NOPASSWD:/home/pi/PyDar/move_right.py
www-data ALL=(ALL) NOPASSWD:/usr/bin/python3
```

Ownership issues

`chown www-data:www-data /PyDar`

`chown www-data:www-data /var/www/html`

Remember to copy index.php to /var/www/html
### Docker GPIO access
`$ docker run --privileged -d whatever`

### TODO

* v1. Run on LAMP server on bare metal - DONE
* v2. Dockerize the app, change base docker image to `raspbian/stretch` use configs from https://github.com/joaquindlz/rpi-docker-lamp/blob/master/Dockerfile
* v3. Allow distributed containers on different systems to call the necessary functions


### Troubleshooting

Sometimes numpy will give you an error that it can't be imported even though you have already installed it through pip. If that happens try running `sudo apt-get install libatlas-base-dev`

### Useful information used in Development
* The [iwconfig](https://sandilands.info/sgordon/capturing-wifi-in-monitor-mode-with-iw) dos
	1. These provide a very detailed look into how monitor mode and the 2.4 GHz wifi bands work
