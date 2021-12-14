FROM python:3.8.12-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["pred.py", "predict-model.bin", "dv.bin", "./"]

EXPOSE 9698

ENTRYPOINT ["gunicorn", "pred:app"]