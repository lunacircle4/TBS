# development
FROM lunacircle4/python:3.8.1 as dev
WORKDIR /root/api
EXPOSE 8000
COPY requirements.txt entrypoint.sh init.sh ./
RUN apt update \
    && apt install -y libmariadb-dev \         
    && rm -rf /var/lib/apt/lists/* \
    && pip3 --no-cache-dir install -r requirements.txt \
    && rm -rf requirements.txt \
    && chmod +x entrypoint.sh
ENTRYPOINT ["sh", "./entrypoint.sh"]
