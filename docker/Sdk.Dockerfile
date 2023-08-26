FROM rasa/rasa-sdk:3.6.2

COPY src/actions actions

COPY requirements/sdk.txt requirements.txt

USER root

RUN pip install --require-hashes -r requirements.txt

USER 1001