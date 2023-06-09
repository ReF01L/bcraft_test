FROM python:3.10

WORKDIR /opt/project/

RUN pip install --upgrade pip

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY ./ ./

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
