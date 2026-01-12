"""
Model Management Utilities
Handles model loading, validation, and retraining logic
"""

import os
from model import WineQualityModel
from data_handler import DataHandler
from config import MODEL_FILE, EXPECTED_FEATURES


class ModelManager:
    """Manages model lifecycle: loading, validation, and initialization"""
    
    @staticmethod
    def initialize_model(data_path='winequality.csv'):
        """
        Initialize or load the wine quality model
        
        Args:
            data_path: Path to the wine quality dataset
            
        Returns:
            Initialized WineQualityModel instance
        """
        wine_analyzer = WineQualityModel()
        
        # Check if saved model exists and is valid
        if os.path.exists(MODEL_FILE):
            try:
                print("\n📦 Checking existing model...")
                wine_analyzer.load_model(MODEL_FILE)
                
                # Validate features match
                if wine_analyzer.feature_names == EXPECTED_FEATURES:
                    print("✅ Model loaded successfully with correct features!")
                    print(f"   Model accuracy: {wine_analyzer.get_accuracy()}%")
                    return wine_analyzer
                else:
                    print("⚠️  Old model detected with different features.")
                    print("   Retraining with updated features...")
                    os.remove(MODEL_FILE)
                    
            except Exception as e:
                print(f"⚠️  Error loading model: {e}")
                print("   Training new model...")
                if os.path.exists(MODEL_FILE):
                    os.remove(MODEL_FILE)
        
        # Train new model
        print("\n🔧 Training new model...")
        wine_analyzer = ModelManager._train_new_model(wine_analyzer, data_path)
        
        return wine_analyzer
    
    @staticmethod
    def _train_new_model(wine_analyzer, data_path):
        """
        Train a new model from scratch
        
        Args:
            wine_analyzer: WineQualityModel instance
            data_path: Path to dataset
            
        Returns:
            Trained WineQualityModel instance
        """
        # Load dataset
        df = DataHandler.load_dataset(data_path)
        
        # Train model
        wine_analyzer.train(df)
        
        # Save model
        wine_analyzer.save_model(MODEL_FILE)
        
        return wine_analyzer
    
    @staticmethod
    def validate_model_features(wine_analyzer):
        """
        Validate that model has correct features
        
        Args:
            wine_analyzer: WineQualityModel instance
            
        Returns:
            Boolean indicating if features are valid
        """
        if wine_analyzer.feature_names is None:
            return False
        return wine_analyzer.feature_names == EXPECTED_FEATURES
