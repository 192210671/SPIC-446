!pip install faker

import pandas as pd
from faker import Faker
import random

# Initialize Faker for generating synthetic data
fake = Faker()

# Define the number of records in the dataset
num_records = 1000

# Generate synthetic data with PII
data = {
    'DeviceID': [fake.uuid4() for _ in range(num_records)],
    'SensorData': [fake.random_number(2) for _ in range(num_records)],
    'Location': [fake.city() for _ in range(num_records)],
    # Add more relevant fields as needed
}

# Create a Pandas DataFrame
df = pd.DataFrame(data)

# Cloud Communication and Computation
df['CloudCommunicationCost'] = [random.uniform(1, 10) for _ in range(num_records)]
df['CloudComputationCost'] = [random.uniform(5, 20) for _ in range(num_records)]

# Fog Communication and Computation
df['FogCommunicationCost'] = [random.uniform(0.5, 5) for _ in range(num_records)]
df['FogComputationCost'] = [random.uniform(1, 10) for _ in range(num_records)]

# Data Blinding
df['BlindedSensorData'] = df['SensorData'] + random.uniform(-1, 1)

# Proxy Provable Data Processing Scheme
df['ProxyProcessingTime'] = [random.uniform(0.1, 2) for _ in range(num_records)]
df['ProxyProcessingEfficiency'] = [random.uniform(0.7, 1.0) for _ in range(num_records)]
df['ProxyProcessingAccuracy'] = [random.uniform(0.8, 1.0) for _ in range(num_records)]

# Remote Data Possession Checking
df['PossessionCheckTime'] = [random.uniform(0.2, 3) for _ in range(num_records)]
df['PossessionCheckResult'] = [random.choice([True, False]) for _ in range(num_records)]

# Model Efficiency and Accuracy
df['ModelEfficiency'] = [random.uniform(0.7, 1.0) for _ in range(num_records)]
df['ModelAccuracy'] = [random.uniform(0.8, 1.0) for _ in range(num_records)]

# Save the dataset to a CSV file
df.to_csv('data_integrity_audit_cloud_fog_dataset.csv', index=False)
