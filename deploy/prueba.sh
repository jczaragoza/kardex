#!/bin/bash
DJANGODIRAPP=$(dirname $(cd `dirname $0` && pwd))
DJANGO_SETTINGS_MODULE=config.settings

DJANGODIR=$(dirname $(dirname $(cd `dirname $0` && pwd)))
cd $DJANGODIR
source env/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE

DIA=`date +"%d%m%Y"`

cd $DJANGODIRAPP

exec python3 manage.py dumpdata > /home/antoniog/kardex/app/backup/respaldoapp$DIA.json





