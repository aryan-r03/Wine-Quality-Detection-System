"""
Configuration file for Wine Quality Detection system
Contains all constants and model parameters
"""

# Model Parameters
MODEL_CONFIG = {
    'n_estimators': 100,
    'random_state': 42
}

# Training Configuration
TRAINING_CONFIG = {
    'test_size': 0.2,
    'random_state': 42
}

# Model File Path
MODEL_FILE = 'wine_model.pkl'

# Expected Features (in order)
EXPECTED_FEATURES = [
    'fixed_acidity',
    'volatile_acidity', 
    'citric_acid',
    'residual_sugar',
    'chlorides',
    'free_sulfur_dioxide',
    'total_sulfur_dioxide',
    'density',
    'pH',
    'sulphates',
    'alcohol'
]

# Sample Data Ranges (for generating synthetic dataset)
SAMPLE_DATA_RANGES = {
    'fixed_acidity': (4.6, 15.9),
    'volatile_acidity': (0.12, 1.58),
    'citric_acid': (0.0, 1.0),
    'residual_sugar': (0.9, 15.5),
    'chlorides': (0.012, 0.611),
    'free_sulfur_dioxide': (1, 72),
    'total_sulfur_dioxide': (6, 289),
    'density': (0.99007, 1.00369),
    'pH': (2.74, 4.01),
    'sulphates': (0.33, 2.0),
    'alcohol': (8.4, 14.9)
}

# Quality Score Weights (for synthetic dataset)
QUALITY_WEIGHTS = {
    'alcohol': 0.3,
    'volatile_acidity': 0.2,
    'citric_acid': 2,
    'density': 3
}

# Server Configuration
SERVER_CONFIG = {
    'host': '0.0.0.0',
    'port': 5000,
    'debug': True
}

# Sample Wine Data (Good Wine)
GOOD_WINE_SAMPLE = {
    'fixed_acidity': 7.4,
    'volatile_acidity': 0.3,
    'citric_acid': 0.5,
    'residual_sugar': 1.9,
    'chlorides': 0.076,
    'free_sulfur_dioxide': 11,
    'total_sulfur_dioxide': 34,
    'density': 0.9978,
    'pH': 3.51,
    'sulphates': 0.56,
    'alcohol': 12.5
}

# Sample Wine Data (Bad Wine)
BAD_WINE_SAMPLE = {
    'fixed_acidity': 8.5,
    'volatile_acidity': 0.8,
    'citric_acid': 0.1,
    'residual_sugar': 2.1,
    'chlorides': 0.15,
    'free_sulfur_dioxide': 5,
    'total_sulfur_dioxide': 15,
    'density': 1.001,
    'pH': 3.8,
    'sulphates': 0.4,
    'alcohol': 9.2
}
