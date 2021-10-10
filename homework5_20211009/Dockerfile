FROM agrigorev/zoomcamp-model:3.8.12-slim


RUN pip --no-cache-dir install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]
RUN pipenv install --deploy --system && \
    rm -rf /root/.cache

COPY ["score.py", "./"]

EXPOSE 9698

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:9698", "score:app"] 

