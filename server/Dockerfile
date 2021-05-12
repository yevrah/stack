FROM python:3.9
WORKDIR /app
COPY requirements.txt ./

RUN pip install meinheld gunicorn -r requirements.txt

COPY gunicorn_conf.py main.py config.py rider.py ./
COPY src ./src

ENV PYTHONPATH=/app
EXPOSE 5000
CMD ["gunicorn", "-k", "egg:meinheld#gunicorn_worker", "-c", "/app/gunicorn_conf.py", "main:app"]
