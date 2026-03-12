    FROM python:3.12

    RUN pip3 install pyinaturalist redis

    COPY conservation_status.py /code/conservation_status.py

    RUN chmod ugo+x /code/conservation_status.py

    ENV PATH="/code:$PATH"