FROM python:3.6

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt


ENTRYPOINT ["python", "src/fermodel_example.py"]