echo "Creating the tcount database"
python create_database.py
cd extweetwordcount
sparse run > sparseoutput.txt&
sparse_pid=$!
date +"%T"
sleep 5m
date +"%T"
kill -9 $sparse_pid
cd ..
rm -rf output
mkdir output
python final_results.py this > output/final_results.txt	
python final_results.py > output/final_results_all.txt
python histogram.py 10 300 > output/histogram.txt
python top_20.py > output/top_20.txt
