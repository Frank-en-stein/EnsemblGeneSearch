FROM python:3-alpine

RUN python -m pip install --upgrade pip

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000
CMD [ "python", "app.py" ]