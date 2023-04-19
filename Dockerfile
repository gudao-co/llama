FROM python:3.9.16

COPY ./requirements.txt ./requirements.txt

COPY ./gen.py ./gen.py

COPY ./main.py ./main.py

RUN pip3 install -r ./requirements.txt

RUN pip3 install llama-index

ENTRYPOINT ["python3","./main.py"]