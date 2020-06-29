# PyDar
Python powered wifi radar

## v1. Requirements
Apache `sudo apt-get install apache2`
PHP `sudo apt-get install php` 

## Docker GPIO access
`$ docker run --privileged -d whatever`

## TODO

* v1. Run on LAMP server on bare metal - DONE
* v2. Dockerize the app, change base docker image to `raspbian/stretch` use configs from https://github.com/joaquindlz/rpi-docker-lamp/blob/master/Dockerfile
* v3. Allow distributed containers on different systems to call the necessary functions
