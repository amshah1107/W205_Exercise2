echo "Creating the tcount database"
python create_database.py
cd extweetwordcount
sparse run &
sleep 5m
