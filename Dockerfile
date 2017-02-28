FROM alpine:latest
RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    rm -r /root/.cache
COPY ./app/web_app/requirements.txt /tmp/requirements.txt
RUN pip3 install -qr /tmp/requirements.txt
RUN mkdir -p /opt/webapp
COPY ./app/web_app /opt/webapp/
WORKDIR /opt/webapp
EXPOSE 5001
CMD ["python3", "app.py"]
