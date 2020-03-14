FROM lunacircle4/python:3.8.1

ENV EXPOSE_PORT=8000

WORKDIR /root/web

COPY requirements.txt entrypoint.sh ./

RUN apt update \
    && apt install -y libmariadb-dev wget \         
    && rm -rf /var/lib/apt/lists/* \
    && pip3 --no-cache-dir install -r requirements.txt \
    && rm -rf requirements.txt \
    && chmod +x entrypoint.sh

ENTRYPOINT ["sh", "./entrypoint.sh"]
