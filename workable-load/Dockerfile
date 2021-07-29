FROM python:3.7.3-slim

COPY . /opt/app
WORKDIR /opt/app

RUN buildDeps="build-essential" \
	&& apt-get update \
    && apt-get install -y --no-install-recommends $buildDeps \
    && apt-get install libgomp1 \
    && rm -rf /var/lib/apt/lists/* \
    && pip install -r requirements.txt \
    && apt-get purge -y --auto-remove $buildDeps

CMD python run.py
