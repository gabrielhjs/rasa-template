FROM rasa/rasa:3.6.6

COPY config.yml config.yml
COPY credentials.yml credentials.yml
COPY domain.yml domain.yml
COPY endpoints.yml endpoints.yml

RUN pip install boto3

CMD [ "run", "--model", "model.tar.gz", "--remote-storage", "aws"]