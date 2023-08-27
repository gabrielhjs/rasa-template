FROM rasa/rasa-sdk:3.6.2

COPY requirements/sdk.txt requirements.txt

USER root

RUN pip install --require-hashes -r requirements.txt

COPY src/actions actions

USER 1001