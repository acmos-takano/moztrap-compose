#!/bin/bash

# Sleep when asked to, to allow the database time to start
# before Moztrap tries to run /checkdb.py below.
: ${MOZ_SLEEP:=0}
sleep $MOZ_SLEEP

# Setup database automatically if needed
if [ -z "$MOZ_SKIP_DB_CHECK" ]; then
  echo "Running database check"
  python /checkdb.py
  DB_CHECK_STATUS=$?

  if [ $DB_CHECK_STATUS -eq 1 ]; then
    echo "Failed to connect to database server or database does not exist."
    exit 1
  elif [ $DB_CHECK_STATUS -eq 2 ]; then
    echo "Configuring initial database"
    cd moztrap
    ./with_venv.sh ./manage.py syncdb --migrate --noinput
    ./with_venv.sh ./manage.py create_default_roles
    ./with_venv.sh ./add_user.py admin admin@localhost.local 000000 --is_admin
  fi
fi

exec "$@"
