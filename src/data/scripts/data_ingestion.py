

import os
from datetime import datetime
from pymongo import MongoClient
import pandas as pd

# MongoDB connection details
MONGO_URI = "mongodb+srv://<username>:<password>@<cluster>.mongodb.net/<database>?retryWrites=true&w=majority"
DATABASE_NAME = "your_database_name"
COLLECTION_NAME = "your_collection_name"

# Local directory for saving data
DATA_DIR = "data/raw"

def ingest_data():
    """
    Ingests data from an Atlas MongoDB database and saves it to a local directory.
    """
    # Create the data directory if it doesn't exist
    os.makedirs(DATA_DIR, exist_ok=True)

    # Connect to the MongoDB database
    client = MongoClient(MONGO_URI)
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]

    # Fetch data from the MongoDB collection
    data = list(collection.find())

    # Convert the data to a Pandas DataFrame
    df = pd.DataFrame(data)

    # Save the data to a local CSV file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(DATA_DIR, f"data_{timestamp}.csv")
    df.to_csv(file_path, index=False)

    print(f"Data ingested and saved to {file_path}")

if __name__ == "__main__":
    ingest_data()
    
    
    

# OR we can use the following code based on the database_utils file that we made


import os
from datetime import datetime
import pandas as pd
from utils.database_utils import connect_to_database

# MongoDB connection details
MONGO_URI = "mongodb+srv://<username>:<password>@<cluster>.mongodb.net/<database>?retryWrites=true&w=majority"
DATABASE_NAME = "your_database_name"
COLLECTION_NAME = "your_collection_name"

# Local directory for saving data
DATA_DIR = "data/raw"

def ingest_data():
    """
    Ingests data from an Atlas MongoDB database and saves it to a local directory.
    """
    # Create the data directory if it doesn't exist
    os.makedirs(DATA_DIR, exist_ok=True)

    # Connect to the MongoDB database
    client = connect_to_database(MONGO_URI)
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]

    # Fetch data from the MongoDB collection
    data = list(collection.find())

    # Convert the data to a Pandas DataFrame
    df = pd.DataFrame(data)

    # Save the data to a local CSV file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(DATA_DIR, f"data_{timestamp}.csv")
    df.to_csv(file_path, index=False)

    print(f"Data ingested and saved to {file_path}")

if __name__ == "__main__":
    ingest_data()