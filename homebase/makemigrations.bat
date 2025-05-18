REM create the database migration file (this does not do the actual migration, see migration.bat for that)
python manage.py makemigrations --settings=homebase.settings.dev
REM don't forget to add the new migration file to the repo (right click on the migration file, choose git -> add).