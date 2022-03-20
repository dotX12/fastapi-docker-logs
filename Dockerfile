FROM python:3.10-slim

COPY requirements.txt requirements.txt

RUN pip3 install -U pip wheel
RUN pip3 install -r requirements.txt

COPY . .


CMD ["uvicorn", "main:app", "--port", "4243", "--reload"]
