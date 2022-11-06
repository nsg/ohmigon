ARG BUILD_FROM
FROM $BUILD_FROM

# Install packages
RUN apk add python3 py3-pip
RUN pip install pyserial paho-mqtt

ADD run.sh src README.md DOCS.md /
RUN chmod +x /run.sh

CMD [ "/run.sh" ]
