# PyDar
Python powered wifi radar

## What is this?
PyDar is a tool for the Raspberry Pi (but works on any form of Linux!) and provides the means to scan surrounding wifi networks (by means of scapy) and send the results to a web server. The web server in turn will render the results of the scan to the HTML, providing near-realtime updates of wifi scans that can be accessed through the web portal. Additionally the web server has the functionality to access the GPIO pins on the Pi, which enables users of the application to issue GPIO commands. While the most basic hardware requirements of PyDar is simply a Raspberry Pi, the idea behind the GPIO functionality is that a user could connect an additional wireless interface, such as a [Cantenna](https://jacobsalmela.com/2013/09/07/wi-fi-cantenna-2-4ghz-how-to-make-a-long-range-wi-fi-antenna/) and attach this interface to a servo. One could then issue commands to the servo using the GPIO pins on the Pi, allowing the interface to swivel, like a radar :)

## Usage
Currently, the web server and scripts must be ran on the host that is capturing the wireless packets. There is plans in the future to move the server and helper scripts to a Docker image to cut down on the host requirements.

### v1. Requirements - tested and working on Raspbian as well as Ubuntu 20.04
Apache `sudo apt-get install apache2`
PHP `sudo apt-get install php` 

Visudo entry - since some of the commands issued by the web server interact with wireless interfaces, sudo is required for the following paths
<b>Please Note:</b> This assumes you have cloned this repo to your home directory. Modify the Visudo entries as needed if you have cloned this repo to a different place.
```
www-data ALL=(ALL) NOPASSWD:/usr/bin/pinout
www-data ALL=(ALL) NOPASSWD:/home/pi/PyDar/move_left.py
www-data ALL=(ALL) NOPASSWD:/home/pi/PyDar/move_right.py
www-data ALL=(ALL) NOPASSWD:/usr/bin/python3
```

Ownership issues - These ensure that the service account can access the relevant scripts

`chown www-data:www-data /PyDar`

`chown www-data:www-data /var/www/html`


### Running the tool
The tool can currently be ran in one of two ways, either using the apache web server, or creating an ad-hoc server with php itself. Both examples will be shown below.

<b>Using Apache:</b>

Copy all of the scripts in this top level directory to /var/www/html

Browse to http://localhost:80/ and begin interacting with the server.

<b>Using ad-hoc</b>

This is the quickest method to get the server up and running, once you have fulfilled all the above requirements, cd into this directory and from here run `php -S localhost:9000` 

Browse to http://localhost:9000 and begin interacting with the server.


## Troubleshooting

Sometimes numpy will give you an error that it can't be imported even though you have already installed it through pip. If that happens try running `sudo apt-get install libatlas-base-dev`

