FROM python:3.10
EXPOSE 5000
COPY . /app
WORKDIR /app    
RUN pip install -r requirements.txt
CMD ["flask","run","--host=0.0.0.0"]