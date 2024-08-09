#!/bin/bash

# Function to check if a script exists and is executable, then run it in the background
run_script() {
    if [ -x "$1" ]; then
        echo "Running $1..."
        ./$1 &
    else
        echo "Script $1 does not exist or is not executable."
    fi
}

# List of scripts to run
SCRIPTS=("arm_camera_rover.sh" "backup_camera_rover.sh" "infrared_camera_rover.sh" "main_camera_rover.sh")

# Loop through the list and run each script in the background
for SCRIPT in "${SCRIPTS[@]}"; do
    run_script "$SCRIPT"
done

# Wait for all background processes to complete
wait

echo "All scripts have finished executing."
