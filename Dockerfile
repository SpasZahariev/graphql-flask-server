FROM python:3

# WORKDIR /src

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "./start.sh"]
# CMD [ "python", "main.py" ]
# CMD [ "gunicorn", "app:app"]