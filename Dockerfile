FROM python:3.6.5
WORKDIR /home/tumn/app
EXPOSE 8000

COPY . /home/tumn/app

RUN pip3 install pipenv
RUN pipenv install
RUN chmod a+x /home/dimigoin/app/docker-entrypoint.sh

ENTRYPOINT ["/home/tumn/app/docker-entrypoint.sh"]
CMD ["pipenv", "run", "gunicorn", "tumn:app", "-w", "4", "-b", "0.0.0.0:8000"]