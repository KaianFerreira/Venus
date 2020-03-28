FROM python:3.6.10-slim-buster
WORKDIR /app
COPY . /app  
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["main.py"]