import logging
from os import environ, listdir, path, remove

from boto3 import client
from botocore.exceptions import ClientError


def upload_model():
    try:
        AWS_SECRET_ACCESS_KEY = environ["AWS_SECRET_ACCESS_KEY"]
        AWS_ACCESS_KEY_ID = environ["AWS_ACCESS_KEY_ID"]
        AWS_DEFAULT_REGION = environ["AWS_DEFAULT_REGION"]
        BUCKET_NAME = environ["BUCKET_NAME"]

        s3_client = client(
            "s3",
            region_name=AWS_DEFAULT_REGION,
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        )

        absolute_path = path.dirname(__file__)
        relative_path = "models"
        full_path = path.join(absolute_path, "../../", relative_path)

        for model in listdir(full_path):
            model_path = path.join(full_path, model)

            s3_client.upload_file(model_path, BUCKET_NAME, model)

            remove(model_path)

    except KeyError as error:
        logging.error(error)
        print(error)
        exit(1)

    except ClientError as error:
        logging.error(error)
        print(error)
        exit(1)

    except Exception as error:
        print(error)
        exit(1)


if __name__ == "__main__":
    upload_model()
