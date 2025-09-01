# File name: create_dummy_5apk_csv.py
import pandas as pd
import random
import os

# Make sure datasets folder exists
if not os.path.exists("datasets"):
    os.makedirs("datasets")

# Full 470 feature columns (same as training)
columns = [
    'ACCESS_PERSONAL_INFO___', 'ALTER_PHONE_STATE___', 'ANTI_DEBUG_____', 'CREATE_FOLDER_____', 
    'CREATE_PROCESS`_____', 'CREATE_THREAD_____', 'DEVICE_ACCESS_____', 'EXECUTE_____', 
    'FS_ACCESS____', 'FS_ACCESS()____', 'FS_ACCESS(CREATE)____', 'FS_ACCESS(CREATE__APPEND)__', 
    'FS_ACCESS(CREATE__READ)__', 'FS_ACCESS(CREATE__READ__WRITE)', 'FS_ACCESS(CREATE__WRITE)__', 
    'FS_ACCESS(CREATE__WRITE__APPEND)', 'FS_ACCESS(READ)____', 'FS_ACCESS(READ__WRITE)__', 
    'FS_ACCESS(WRITE)____', 'FS_PIPE_ACCESS___', 'FS_PIPE_ACCESS()___', 'FS_PIPE_ACCESS(READ)___', 
    'FS_PIPE_ACCESS(READ__)_', 'FS_PIPE_ACCESS(READ__WRITE)_', 'FS_PIPE_ACCESS(WRITE)___', 
    'NETWORK_ACCESS____', 'NETWORK_ACCESS()____', 'NETWORK_ACCESS(READ)____', 
    'NETWORK_ACCESS(READ__WRITE)__', 'NETWORK_ACCESS(READ__WRITE__)', 'NETWORK_ACCESS(WRITE)____', 
    'NETWORK_ACCESS(WRITE__)__', 'SMS_SEND____', 'TERMINATE_PROCESS', 'TERMINATE_THREAD',
]

# Fill remaining dummy column names if less than 470
while len(columns) < 470:
    columns.append(f"DUMMY_FEATURE_{len(columns)+1}")

# Create dummy data for 5 APKs
data = []
for _ in range(5):  # 5 APKs
    row = [random.randint(0, 1) for _ in range(470)]
    data.append(row)

# Create DataFrame
df = pd.DataFrame(data, columns=columns)

# Save as CSV
df.to_csv("datasets/new_apks_features.csv", index=False)
print("✅ Dummy 5-APK CSV with 470 features created successfully!")
