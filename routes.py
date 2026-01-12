"""
Flask routes and API endpoints for Wine Quality Detection
Handles HTTP requests and responses
"""

from flask import Flask, request, jsonify
from templates import get_html_template


def setup_routes(app, wine_analyzer):
    """
    Setup all Flask routes for the application
    
    Args:
        app: Flask application instance
        wine_analyzer: WineQualityModel instance
    """
    
    @app.route('/')
    def home():
        """Serve the main web interface"""
        return get_html_template()
    
    @app.route('/api/predict', methods=['POST'])
    def predict_quality():
        """
        Predict wine quality from input features
        
        Expected JSON body:
            {
                "features": {
                    "fixed_acidity": 7.4,
                    "volatile_acidity": 0.3,
                    ...
                }
            }
            
        Returns:
            JSON with prediction results
        """
        try:
            data = request.get_json()
            features = data.get('features', {})
            
            if not features:
                return jsonify({
                    'success': False,
                    'error': 'No features provided'
                }), 400
            
            print("\n📊 Received features:", features)
            
            # Make prediction
            result = wine_analyzer.predict(features)
            print("✅ Prediction result:", result)
            
            if 'error' in result:
                return jsonify({
                    'success': False,
                    'error': result['error']
                }), 500
            
            return jsonify({
                'success': True,
                'result': result
            })
            
        except Exception as e:
            print(f"❌ API Error: {str(e)}")
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500
    
    @app.route('/api/stats')
    def get_stats():
        """
        Get model statistics
        
        Returns:
            JSON with model accuracy
        """
        return jsonify({
            'accuracy': wine_analyzer.get_accuracy()
        })
    
    return app
