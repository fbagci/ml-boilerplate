echo "Run tests"
python -m unittest discover -s ./src/tests/ --console=plain &> test_error.log
sleep 30
! grep -iE -B 4 -A 10 --color "(^FAIL:|^ERROR:)" test_error.log