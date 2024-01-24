#!/bin/bash

export FECHA=`date +%d_%m_%Y_%H_%M_%S`
export NAME=app_backup_${FECHA}.dump
export DIR=/home/antoniog/backup/
USER_DB=antonio
NAME_DB=kardex
cd $DIR
> ${NAME}
export PGPASSWORD=Ssuac2021$
chmod 777 ${NAME}
echo "procesando la copia de la base de datos"
pg_dump -U $USER_DB -h localhost --port 5432 -f ${NAME} $NAME_DB
echo "backup terminado"




# #!/bin/bash

# export FECHA=`date +%d_%m_%Y_%H_%M_%S`
# export NAME=app_${FECHA}.dump
# export DIR=/home/antoniog/backup/
# USER_DB=antonio
# NAME_DB=kardex
# cd $DIR
# > ${NAME}
# export PGPASSWORD=Ssuac2021$
# chmod 777 ${NAME}
# echo "procesando la copia de la base de datos"
# pg_dump -U $USER_DB -h localhost --port 5432 -f ${NAME} $NAME_DB
# echo "backup terminado"
