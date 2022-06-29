# Best image for builds with numpy
FROM python:3.9.13-slim-buster
# Copy the script directory
COPY /data/etl/ /
# Avoid ssl issues 
RUN pip install ndg-httpsclient
RUN pip install pyopenssl
RUN pip install pyasn1

RUN  pip install --no-cache-dir --upgrade -r /requirements.txt
CMD ["python", "etl.py"]
EXPOSE 80
