"""
Data handling utilities for Wine Quality Detection
Handles dataset loading, creation, and preprocessing
"""

import pandas as pd
import numpy as np
import os
from config import SAMPLE_DATA_RANGES, QUALITY_WEIGHTS, EXPECTED_FEATURES


class DataHandler:
    """Handles data loading and synthetic dataset creation"""
    
    @staticmethod
    def load_dataset(csv_path='winequality.csv'):
        """
        Load wine quality dataset from CSV file
        
        Args:
            csv_path: Path to the CSV file
            
        Returns:
            pandas.DataFrame with wine features and quality labels
        """
        try:
            if os.path.exists(csv_path):
                print(f"\n📊 Loading dataset from {csv_path}...")
                df = pd.read_csv(csv_path)
                
                # Check if quality column exists
                if 'quality' not in df.columns:
                    print("⚠️  Warning: 'quality' column not found. Using sample dataset.")
                    return DataHandler.create_sample_dataset()
                
                # Convert quality to binary (good/bad)
                # Typically quality > 5 is considered good wine
                if df['quality'].max() > 2:  # If quality is on scale (e.g., 3-9)
                    df['quality'] = (df['quality'] > 5).astype(int)
                
                # Keep only expected features if they exist
                available_features = [f for f in EXPECTED_FEATURES if f in df.columns]
                if len(available_features) < len(EXPECTED_FEATURES):
                    print(f"⚠️  Warning: Some features missing. Using sample dataset.")
                    return DataHandler.create_sample_dataset()
                
                df = df[available_features + ['quality']]
                print(f"✅ Loaded {len(df)} wine samples")
                print(f"   Good wines: {(df['quality']==1).sum()}")
                print(f"   Bad wines: {(df['quality']==0).sum()}")
                
                return df
                
            else:
                print(f"⚠️  File '{csv_path}' not found.")
                return DataHandler.create_sample_dataset()
                
        except Exception as e:
            print(f"❌ Error loading dataset: {e}")
            return DataHandler.create_sample_dataset()
    
    @staticmethod
    def create_sample_dataset(n_samples=1000):
        """
        Create a synthetic wine quality dataset
        
        Args:
            n_samples: Number of samples to generate
            
        Returns:
            pandas.DataFrame with synthetic wine data
        """
        print("\n🍷 Creating sample wine dataset...")
        np.random.seed(42)
        
        # Generate random features within realistic ranges
        data = {}
        for feature, (min_val, max_val) in SAMPLE_DATA_RANGES.items():
            data[feature] = np.random.uniform(min_val, max_val, n_samples)
        
        df = pd.DataFrame(data)
        
        # Calculate quality score based on weighted features
        df['quality_score'] = (
            df['alcohol'] * QUALITY_WEIGHTS['alcohol'] +
            (10 - df['volatile_acidity'] * 5) * QUALITY_WEIGHTS['volatile_acidity'] +
            df['citric_acid'] * QUALITY_WEIGHTS['citric_acid'] +
            (1 / df['density']) * QUALITY_WEIGHTS['density'] +
            np.random.uniform(-2, 2, n_samples)  # Add some noise
        )
        
        # Convert to binary classification (good/bad)
        df['quality'] = (df['quality_score'] > df['quality_score'].median()).astype(int)
        df = df.drop('quality_score', axis=1)
        
        print(f"✅ Generated {n_samples} synthetic wine samples")
        print(f"   Good wines: {(df['quality']==1).sum()}")
        print(f"   Bad wines: {(df['quality']==0).sum()}")
        
        return df
    
    @staticmethod
    def validate_features(features_dict):
        """
        Validate that all required features are present
        
        Args:
            features_dict: Dictionary of features
            
        Returns:
            Tuple of (is_valid, missing_features)
        """
        missing = [f for f in EXPECTED_FEATURES if f not in features_dict]
        return len(missing) == 0, missing
