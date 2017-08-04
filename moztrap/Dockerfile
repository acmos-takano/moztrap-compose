FROM lemonlatte/docker-moztrap

COPY local.py /moztrap/moztrap/settings/local.py
COPY docker-entrypoint.sh /docker-entrypoint.sh
COPY checkdb.py /checkdb.py

ENTRYPOINT ["/docker-entrypoint.sh"]
