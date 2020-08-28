FROM tiangolo/uwsgi-nginx-flask:python3.7
WORKDIR /flaskblog
COPY . .
RUN pip install -U pip
RUN pip install -r requirements.txt
ENTRYPOINT ["bash", "-c", "flask run --host '0.0.0.0' --port=5001"]
