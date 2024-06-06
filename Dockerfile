FROM python:3.7.2
WORKDIR /app
EXPOSE 5000

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY requirements.txt .
RUN pip install -U pip \
    pip install gunicorn[gevent] \
    pip install -r requirements.txt

# Run the application:
COPY . .
ENTRYPOINT ["/app/docker-entrypoint.sh"]
