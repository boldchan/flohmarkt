FROM python:3.10-alpine

WORKDIR /code

COPY . /code/

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

CMD ["uvicorn", "main:app", "--reload", "--port", "5000"]