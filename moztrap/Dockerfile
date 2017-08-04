FROM lemonlatte/docker-moztrap

RUN apt-get update \
    apt-get install -y python-dev libmysqlclient-dev \
    pip install mysqlclient

COPY local.py /moztrap/moztrap/settings/local.py
COPY checkdb.py /checkdb.py
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod 755 /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]
