"""
Wine Quality Machine Learning Model
Contains the model class with training, prediction, and persistence capabilities
"""

import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
from config import MODEL_CONFIG, TRAINING_CONFIG, EXPECTED_FEATURES


class WineQualityModel:
    """Machine learning model for wine quality classification"""
    
    def __init__(self):
        """Initialize the model with Random Forest classifier and scaler"""
        self.model = RandomForestClassifier(**MODEL_CONFIG)
        self.scaler = StandardScaler()
        self.feature_names = None
        self.accuracy = 0
    
    def train(self, df):
        """
        Train the wine quality model
        
        Args:
            df: pandas.DataFrame with features and 'quality' column
            
        Returns:
            Model accuracy score
        """
        print("\n" + "="*60)
        print("🧠 TRAINING WINE QUALITY MODEL")
        print("="*60)
        
        # Separate features and target
        X = df.drop('quality', axis=1)
        y = df['quality']
        self.feature_names = X.columns.tolist()
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, 
            test_size=TRAINING_CONFIG['test_size'],
            random_state=TRAINING_CONFIG['random_state'],
            stratify=y
        )
        
        print(f"\n📊 Dataset split:")
        print(f"   Training samples: {len(X_train)}")
        print(f"   Testing samples: {len(X_test)}")
        
        # Scale features
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        # Train model
        print(f"\n🔧 Training Random Forest with {MODEL_CONFIG['n_estimators']} trees...")
        self.model.fit(X_train_scaled, y_train)
        
        # Evaluate
        y_pred = self.model.predict(X_test_scaled)
        self.accuracy = accuracy_score(y_test, y_pred)
        
        print(f"\n✅ Model Accuracy: {self.accuracy * 100:.2f}%")
        print(f"\n📊 Classification Report:")
        print(classification_report(
            y_test, y_pred,
            target_names=['Bad Wine', 'Good Wine']
        ))
        
        return self.accuracy
    
    def predict(self, features_dict):
        """
        Predict wine quality from features
        
        Args:
            features_dict: Dictionary with feature values
            
        Returns:
            Dictionary with prediction results
        """
        try:
            # Create features list in correct order
            features_list = [
                features_dict.get(feat, 0) for feat in EXPECTED_FEATURES
            ]
            
            # Convert to DataFrame
            features_df = pd.DataFrame([features_list], columns=EXPECTED_FEATURES)
            
            # Scale features
            features_scaled = self.scaler.transform(features_df)
            
            # Make prediction
            prediction = self.model.predict(features_scaled)[0]
            probability = self.model.predict_proba(features_scaled)[0]
            
            return {
                'quality': "Good Wine" if prediction == 1 else "Bad Wine",
                'confidence': round(max(probability) * 100, 2),
                'good_probability': round(probability[1] * 100, 2),
                'bad_probability': round(probability[0] * 100, 2),
            }
            
        except Exception as e:
            print(f"❌ Prediction error: {str(e)}")
            return {
                'error': str(e),
                'quality': 'Error',
                'confidence': 0
            }
    
    def save_model(self, filepath):
        """
        Save the trained model to disk
        
        Args:
            filepath: Path where to save the model
        """
        try:
            with open(filepath, 'wb') as f:
                pickle.dump({
                    'model': self.model,
                    'scaler': self.scaler,
                    'feature_names': self.feature_names,
                    'accuracy': self.accuracy
                }, f)
            print(f"\n✅ Model saved to {filepath}")
        except Exception as e:
            print(f"❌ Error saving model: {e}")
    
    def load_model(self, filepath):
        """
        Load a trained model from disk
        
        Args:
            filepath: Path to the saved model file
        """
        try:
            with open(filepath, 'rb') as f:
                data = pickle.load(f)
                self.model = data['model']
                self.scaler = data['scaler']
                self.feature_names = data['feature_names']
                self.accuracy = data.get('accuracy', 0)
            print(f"✅ Model loaded from {filepath}")
        except Exception as e:
            print(f"❌ Error loading model: {e}")
            raise
    
    def get_accuracy(self):
        """
        Get model accuracy as formatted string
        
        Returns:
            Accuracy percentage string
        """
        return f"{self.accuracy * 100:.1f}"
