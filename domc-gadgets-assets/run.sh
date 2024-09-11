#!/bin/bash

# Start the fake attacker-controlled server
echo "[+] Starting the fake attacker-controlled server at http://localhost:9999 ..."
node attacker.com/server.js &
ATTACKER_PID=$!  # Store the PID of the attacker server

# Run http-server in the gadgets directory
echo "[+] Starting the dom-clobbering gadgets poc webpage at http://localhost:8080 ..."
cd gadgets || { echo "Failed to change directory to gadgets"; exit 1; }
http-server . &
GADGETS_PID=$!  # Store the PID of the http-server

# Define a function to handle cleanup on Ctrl+C (SIGINT)
cleanup() {
  echo "[!] Caught SIGINT. Stopping both servers..."
  kill $ATTACKER_PID
  kill $GADGETS_PID
  exit 0
}

# Trap SIGINT and call the cleanup function
trap cleanup SIGINT

# Keep the script running to maintain both servers
wait
