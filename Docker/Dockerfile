FROM joaquindlz/rpi-docker-lamp:latest
RUN rm -fr /app && git clone https://github.com/edrapac/PyDar.git /app
EXPOSE 80 3306
CMD ["/run.sh"]

