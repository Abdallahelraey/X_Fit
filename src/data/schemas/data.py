import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

class DataHandler:
    def __init__(self, data_path):
        self.data = self.load_data(data_path)
        self.features, self.labels = self.preprocess_data()

    def load_data(self, data_path):
        # Assume data is in a CSV file, adjust loading logic as needed
        data = pd.read_csv(data_path)
        return data

    def preprocess_data(self):
        # Assume labels are in a column named 'label'
        labels = self.data['label']

        # Assume features are all columns except 'label'
        features = self.data.drop('label', axis=1)

        # Perform preprocessing on features, e.g., scaling
        features = self.scale_features(features)

        # Encode labels
        labels = self.encode_labels(labels)

        return features, labels

    def scale_features(self, features):
        # Standardize features using StandardScaler
        scaler = StandardScaler()
        scaled_features = scaler.fit_transform(features)
        return pd.DataFrame(scaled_features, columns=features.columns)

    def encode_labels(self, labels):
        # Encode categorical labels using LabelEncoder
        label_encoder = LabelEncoder()
        encoded_labels = label_encoder.fit_transform(labels)
        return pd.Series(encoded_labels, name='label')

    def split_data(self, test_size=0.2, random_state=42):
        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(
            self.features, self.labels, test_size=test_size, random_state=random_state
        )
        return X_train, X_test, y_train, y_test

# Example usage:
# Assume you have a CSV file 'workout_data.csv' with features and labels
data_path = 'workout_data.csv'

# Create an instance of DataHandler
data_handler = DataHandler(data_path)

# Get preprocessed features and labels
features, labels = data_handler.features, data_handler.labels

# Split data into training and testing sets
X_train, X_test, y_train, y_test = data_handler.split_data()

# Print shapes of training and testing sets
print(f"Training Features Shape: {X_train.shape}")
print(f"Training Labels Shape: {y_train.shape}")
print(f"Testing Features Shape: {X_test.shape}")
print(f"Testing Labels Shape: {y_test.shape}")
