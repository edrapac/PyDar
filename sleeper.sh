# Launch script in background
sudo airodump-ng wlan1mon > log.txt 2>&1
# Get its PID
PID=$!
# Wait for 10 seconds
sleep 2
# Kill it
sudo kill $PID
