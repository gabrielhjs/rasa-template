FROM rasa/rasa:3.6.6

COPY config.yml config.yml
COPY credentials.yml credentials.yml
COPY domain.yml domain.yml
COPY endpoints.yml endpoints.yml
COPY requirements/rasa.txt requirements.txt
COPY models models

USER root

RUN pip install --require-hashes -r requirements.txt
RUN python -m spacy download pt_core_news_md

USER 1001

CMD [ "run", "-vv"]