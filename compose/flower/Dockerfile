FROM python:3.10

ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONUNBUFFERED 1

ARG PROJ_DIR=/back_proj

RUN mkdir -p ${PROJ_DIR}
COPY ./musicbackend ${PROJ_DIR}

WORKDIR ${PROJ_DIR}

RUN pip install -r requirements.txt

CMD ["celery", "-A", "musicbackend", "flower"]
