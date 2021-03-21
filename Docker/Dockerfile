# Dockerize the app, change base docker image to `raspbian/stretch` use configs from https://github.com/joaquindlz/rpi-docker-lamp/blob/master/
FROM joaquindlz/rpi-docker-lamp:latest
RUN rm -fr /app && git clone https://github.com/edrapac/PyDar.git /app
RUN apt-get update && apt-get -y install python-gpiozero
EXPOSE 80 3306
CMD ["/run.sh"]

