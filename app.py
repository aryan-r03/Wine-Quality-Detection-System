"""
Wine Quality Detection - Main Application
Entry point for the Flask web application
"""

from flask import Flask
from model_manager import ModelManager
from routes import setup_routes
from config import SERVER_CONFIG


def create_app(data_path='winequality.csv'):
    """
    Create and configure the Flask application
    
    Args:
        data_path: Path to wine quality dataset
        
    Returns:
        Configured Flask app instance
    """
    app = Flask(__name__)
    
    # Initialize or load the model
    print("\n" + "="*60)
    print("🍷 WINE QUALITY DETECTION - INITIALIZATION")
    print("="*60)
    
    wine_analyzer = ModelManager.initialize_model(data_path)
    
    # Setup routes
    setup_routes(app, wine_analyzer)
    
    return app


if __name__ == '__main__':
    print("\n" + "="*60)
    print("🍷 WINE QUALITY DETECTION - MACHINE LEARNING PROJECT")
    print("="*60)
    print("\n📊 Starting Flask server...")
    print(f"🌐 Open your browser: http://127.0.0.1:{SERVER_CONFIG['port']}")
    print("="*60 + "\n")
    
    app = create_app()
    app.run(
        debug=SERVER_CONFIG['debug'],
        host=SERVER_CONFIG['host'],
        port=SERVER_CONFIG['port']
    )
