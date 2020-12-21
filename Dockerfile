FROM python:3.9-slim

RUN apt -f install
RUN apt-get update && apt-get install -y curl && apt-get install -y wget && apt-get install bzip2 -y \
&& apt-get install unzip -y

COPY app/ /app

EXPOSE 5000

WORKDIR /app
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]


