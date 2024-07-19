# SQL and NoSQL queries and data modeling

# Import necessary libraries
from pymongo import MongoClient

# MongoDB Connection
client = MongoClient('mongodb://localhost:27017/')
db = client.iot_data
collection = db.readings

# Example MongoDB Query: Find all readings for "Temperature Sensor" above 23
results = collection.find({
    "device_name": "Temperature Sensor",
    "readings.value": {"$gt": 23}
})

print("MongoDB Query Results:")
for result in results:
    print(result)

# NoSQL Data Modeling
# Suppose we use MongoDB for storing IoT device readings. A possible data model could be:
nosql_data_model = {
    "device_id": "device_1",
    "device_name": "Temperature Sensor",
    "location": "Building A",
    "readings": [
        {
            "timestamp": "2023-07-18T12:34:56Z",
            "value": 22.5
        },
        {
            "timestamp": "2023-07-18T12:35:56Z",
            "value": 23.0
        }
    ]
}
print("\nNoSQL Data Model Example:")
print(nosql_data_model)

# Example SQL Queries
sql_queries = """
-- Join Query: Get the latest reading for each device
SELECT d.device_name, r.value, r.timestamp
FROM Devices d
JOIN (
    SELECT device_id, value, timestamp
    FROM Readings
    WHERE (device_id, timestamp) IN (
        SELECT device_id, MAX(timestamp)
        FROM Readings
        GROUP BY device_id
    )
) r ON d.device_id = r.device_id;

-- Aggregation Query: Get the average reading value for each device in the last 24 hours
SELECT d.device_name, AVG(r.value) AS avg_value
FROM Devices d
JOIN Readings r ON d.device_id = r.device_id
WHERE r.timestamp > NOW() - INTERVAL '1 DAY'
GROUP BY d.device_name;

-- Filtering Query: Get all readings above a certain threshold for a specific device
SELECT r.*
FROM Readings r
JOIN Devices d ON r.device_id = d.device_id
WHERE d.device_name = 'Device A' AND r.value > 100;
"""
print("\nSQL Queries Example:")
print(sql_queries)
