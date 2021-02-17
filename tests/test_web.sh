./run_server.sh &
sleep 1
export PYTHONPATH=$(pwd)
python3 tests/test_web.py
pkill -f flask