FROM python:3.10

ENV ARTIFACT_PATH=home/app/models/logreg.pkl
ENV FLASK_APP=home/app/src/delay_api.py

RUN mkdir -p /home/app
RUN mkdir -p /home/app/src
RUN mkdir -p /home/app/models

COPY /src /home/app/src
COPY /models /home/app/models

COPY requirements.txt /home/app/
RUN pip3 install -r /home/app/requirements.txt

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
