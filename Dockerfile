FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt
COPY ./api /code/app
RUN python3 -m nltk.downloader stopwords
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8818"]