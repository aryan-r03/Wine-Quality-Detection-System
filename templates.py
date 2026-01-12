"""
HTML Template for Wine Quality Detection Web Interface
Contains the complete frontend HTML/CSS/JavaScript
"""

def get_html_template():
    """Return the main HTML template as a string"""
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wine Quality Detection - AI Analysis</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Courier New', monospace;
            background: linear-gradient(135deg, #0a0a0a 0%, #4a0000 50%, #0a0a0a 100%);
            min-height: 100vh;
            color: #fff;
            overflow-x: hidden;
            position: relative;
        }
        
        /* Circuit Board Background */
        .circuit-bg {
            position: fixed;
            inset: 0;
            opacity: 0.08;
            pointer-events: none;
            background-image: 
                linear-gradient(90deg, #ff0000 1px, transparent 1px),
                linear-gradient(0deg, #ff0000 1px, transparent 1px);
            background-size: 50px 50px;
        }
        
        .circuit-dots {
            position: fixed;
            inset: 0;
            opacity: 0.1;
            pointer-events: none;
        }
        
        .circuit-dot {
            position: absolute;
            width: 3px;
            height: 3px;
            background: #00ffff;
            border-radius: 50%;
            box-shadow: 0 0 5px #00ffff;
        }
        
        /* Wine Bottles - Top Left */
        .wine-bottles {
            position: absolute;
            top: 30px;
            left: 30px;
            display: flex;
            gap: 15px;
            z-index: 100;
        }
        
        .bottle-icon {
            width: 50px;
            height: 50px;
            background: rgba(139, 0, 0, 0.3);
            border: 1px solid rgba(220, 20, 60, 0.5);
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            cursor: pointer;
            transition: all 0.3s;
            backdrop-filter: blur(10px);
        }
        
        .bottle-icon:hover {
            background: rgba(139, 0, 0, 0.6);
            transform: scale(1.1);
        }
        
        /* Top Info Panel */
        .info-panel {
            position: absolute;
            top: 30px;
            left: 25%;
            z-index: 100;
            font-size: 11px;
            color: rgba(220, 20, 60, 0.6);
            line-height: 1.6;
        }
        
        .info-title {
            font-size: 12px;
            letter-spacing: 1px;
            margin-bottom: 8px;
        }
        
        /* Scanning Frame - Top Right - REMOVED */
        
        .corner {
            position: absolute;
            width: 15px;
            height: 15px;
        }
        
        .corner.tl {
            top: -2px;
            left: -2px;
            border-top: 2px solid #00ffff;
            border-left: 2px solid #00ffff;
        }
        
        .corner.tr {
            top: -2px;
            right: -2px;
            border-top: 2px solid #00ffff;
            border-right: 2px solid #00ffff;
        }
        
        .corner.bl {
            bottom: -2px;
            left: -2px;
            border-bottom: 2px solid #00ffff;
            border-left: 2px solid #00ffff;
        }
        
        .corner.br {
            bottom: -2px;
            right: -2px;
            border-bottom: 2px solid #00ffff;
            border-right: 2px solid #00ffff;
        }
        
        /* Main Container */
        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 100px 40px 40px;
            position: relative;
            z-index: 10;
        }
        
        .main-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 60px;
            align-items: start;
        }
        
        /* Left Side - Inputs */
        .input-section {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }
        
        .preset-buttons {
            display: flex;
            gap: 12px;
            margin-bottom: 20px;
        }
        
        .preset-btn {
            padding: 10px 20px;
            background: rgba(0, 100, 0, 0.2);
            border: 1px solid rgba(34, 139, 34, 0.5);
            border-radius: 20px;
            color: #4ade80;
            font-size: 12px;
            cursor: pointer;
            transition: all 0.3s;
            font-family: 'Courier New', monospace;
        }
        
        .preset-btn:hover {
            background: rgba(0, 100, 0, 0.4);
        }
        
        .preset-btn.bad {
            background: rgba(139, 0, 0, 0.2);
            border-color: rgba(220, 20, 60, 0.5);
            color: #ef4444;
        }
        
        .preset-btn.bad:hover {
            background: rgba(139, 0, 0, 0.4);
        }
        
        .input-field {
            position: relative;
        }
        
        input[type="number"] {
            width: 100%;
            padding: 14px 20px;
            background: rgba(139, 0, 0, 0.2);
            border: 1px solid rgba(220, 20, 60, 0.4);
            border-radius: 25px;
            color: #FFD700;
            font-size: 13px;
            font-family: 'Courier New', monospace;
            transition: all 0.3s;
            backdrop-filter: blur(5px);
        }
        
        input[type="number"]:focus {
            outline: none;
            border-color: rgba(220, 20, 60, 0.8);
            background: rgba(139, 0, 0, 0.3);
            box-shadow: 0 0 15px rgba(255, 215, 0, 0.3);
        }
        
        input[type="number"]::placeholder {
            color: rgba(255, 215, 0, 0.4);
        }
        
        .input-label {
            position: absolute;
            right: 20px;
            top: 50%;
            transform: translateY(-50%);
            font-size: 10px;
            color: rgba(255, 215, 0, 0.3);
        }
        
        /* Sparkle Effect */
        .sparkle {
            position: absolute;
            width: 4px;
            height: 4px;
            background: #FFD700;
            border-radius: 50%;
            pointer-events: none;
            animation: sparkleAnim 2s ease-in-out infinite;
            box-shadow: 0 0 10px #FFD700;
        }
        
        @keyframes sparkleAnim {
            0%, 100% {
                opacity: 0;
                transform: scale(0);
            }
            50% {
                opacity: 1;
                transform: scale(1);
            }
        }
        
        /* Right Side - Analysis */
        .analysis-section {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 30px;
        }
        
        .scan-frame-large {
            position: relative;
            width: 400px;
            height: 400px;
            border: 2px solid rgba(220, 20, 60, 0.3);
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .scan-content {
            text-align: center;
        }
        
        .wine-icon {
            font-size: 80px;
            margin-bottom: 20px;
        }
        
        .status-text {
            font-size: 12px;
            color: rgba(220, 20, 60, 0.6);
            letter-spacing: 2px;
        }
        
        .spinner {
            width: 60px;
            height: 60px;
            border: 4px solid rgba(220, 20, 60, 0.2);
            border-top-color: #00ffff;
            border-radius: 50%;
            animation: spin 1s linear infinite;
            margin: 0 auto 20px;
        }
        
        @keyframes spin {
            to { transform: rotate(360deg); }
        }
        
        .result-icon {
            font-size: 100px;
            margin-bottom: 20px;
            animation: drunkSway 2s ease-in-out infinite;
        }
        
        .result-icon.good {
            color: #4ade80;
        }
        
        .result-icon.bad {
            color: #ef4444;
        }
        
        /* Gentleman Drunk Animation - Gentle sway */
        @keyframes gentlemanDrunk {
            0%, 100% {
                transform: rotate(-3deg) translateX(-5px);
            }
            50% {
                transform: rotate(3deg) translateX(5px);
            }
        }
        
        .gentleman-drunk {
            animation: gentlemanDrunk 3s ease-in-out infinite;
        }
        
        /* Homeless Drunk Animation - Wild wobble */
        @keyframes homelessDrunk {
            0% {
                transform: rotate(-15deg) translateX(-10px) translateY(0);
            }
            25% {
                transform: rotate(10deg) translateX(8px) translateY(-5px);
            }
            50% {
                transform: rotate(-12deg) translateX(-8px) translateY(3px);
            }
            75% {
                transform: rotate(15deg) translateX(10px) translateY(-3px);
            }
            100% {
                transform: rotate(-15deg) translateX(-10px) translateY(0);
            }
        }
        
        .homeless-drunk {
            animation: homelessDrunk 1.5s ease-in-out infinite;
        }
        
        /* Hiccup effect */
        @keyframes hiccup {
            0%, 90%, 100% {
                transform: scale(1);
            }
            95% {
                transform: scale(1.1);
            }
        }
        
        .hiccup {
            animation: hiccup 3s ease-in-out infinite;
        }
        
        /* Stumble effect */
        @keyframes stumble {
            0%, 100% {
                transform: translateY(0) rotate(0deg);
            }
            10% {
                transform: translateY(-10px) rotate(-5deg);
            }
            20% {
                transform: translateY(5px) rotate(3deg);
            }
            30% {
                transform: translateY(-5px) rotate(-2deg);
            }
            40% {
                transform: translateY(0) rotate(0deg);
            }
        }
        
        .stumble {
            animation: stumble 2s ease-in-out infinite;
        }
        
        .result-title {
            font-size: 28px;
            font-weight: bold;
            margin-bottom: 20px;
        }
        
        .result-title.good {
            color: #4ade80;
        }
        
        .result-title.bad {
            color: #ef4444;
        }
        
        .result-stats {
            font-size: 13px;
            line-height: 2;
        }
        
        .stat-line {
            color: #ff9999;
        }
        
        .stat-good {
            color: #4ade80;
        }
        
        .stat-bad {
            color: #ef4444;
        }
        
        .analyze-btn {
            position: relative;
            padding: 16px 50px;
            background: rgba(139, 0, 0, 0.3);
            border: 1px solid rgba(220, 20, 60, 0.5);
            border-radius: 30px;
            color: #ff9999;
            font-size: 13px;
            font-family: 'Courier New', monospace;
            cursor: pointer;
            transition: all 0.3s;
            backdrop-filter: blur(10px);
            display: flex;
            align-items: center;
            gap: 12px;
        }
        
        .analyze-btn:hover {
            background: rgba(139, 0, 0, 0.5);
            border-color: rgba(220, 20, 60, 0.8);
        }
        
        .analyze-btn:disabled {
            opacity: 0.5;
            cursor: not-allowed;
        }
        
        .btn-icon {
            width: 20px;
            height: 20px;
            border: 2px solid currentColor;
            border-radius: 50%;
            position: relative;
        }
        
        .btn-icon::after {
            content: '';
            position: absolute;
            width: 6px;
            height: 6px;
            background: currentColor;
            border-radius: 50%;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
        }
        
        /* Bottom Decorative */
        .bottom-frame {
            position: fixed;
            bottom: 30px;
            left: 30px;
            width: 180px;
            height: 120px;
            border: 1px solid rgba(220, 20, 60, 0.2);
        }
        
        .system-status {
            position: fixed;
            bottom: 30px;
            right: 30px;
            text-align: right;
            font-size: 10px;
            color: rgba(220, 20, 60, 0.4);
            line-height: 1.8;
        }
        
        @media (max-width: 1024px) {
            .main-grid {
                grid-template-columns: 1fr;
            }
            
            .info-panel {
                position: relative;
                left: 0;
                margin-bottom: 20px;
            }
        }
    </style>
</head>
<body>
    <!-- Circuit Board Background -->
    <div class="circuit-bg"></div>
    <div class="circuit-dots" id="circuitDots"></div>
    
    <!-- Wine Bottles - Top Left -->
    <div class="wine-bottles">
        <div class="bottle-icon">🍷</div>
        <div class="bottle-icon">🍷</div>
    </div>
    
    <!-- Info Panel - Top -->
    <div class="info-panel">
        <div class="info-title">AI WINE DETECTION PROJECT - ANALYSIS IN PROGRESS</div>
        <div>BOTTLE 1: CHARDONNAY</div>
        <div>BOTTLE 2: SAUVIGNON BLANC</div>
        <div>ALC. VOL: 13.5%</div>
        <div>ORIGIN: FRANCE</div>
        <div>QUALITY SCORE: 92</div>
    </div>
    
    <!-- Scanning Frame - Top Right - REMOVED -->
    
    <!-- Main Container -->
    <div class="container">
        <div class="main-grid">
            <!-- Left Side - Input Fields -->
            <div class="input-section">
                <div class="preset-buttons">
                    <button class="preset-btn" onclick="loadGoodWine()">⬤ GOOD SAMPLE</button>
                    <button class="preset-btn bad" onclick="loadBadWine()">⬤ BAD SAMPLE</button>
                </div>
                
                <div class="input-field">
                    <input type="number" id="fixed_acidity" placeholder="Fixed Acidity (4-16 g/L)" step="0.1">
                </div>
                
                <div class="input-field">
                    <input type="number" id="volatile_acidity" placeholder="Volatile Acidity (0-2 g/L)" step="0.01">
                </div>
                
                <div class="input-field">
                    <input type="number" id="citric_acid" placeholder="Citric Acid (0-1 g/L)" step="0.01">
                </div>
                
                <div class="input-field">
                    <input type="number" id="residual_sugar" placeholder="Residual Sugar (0-20 g/L)" step="0.1">
                </div>
                
                <div class="input-field">
                    <input type="number" id="chlorides" placeholder="Chlorides (0-1 g/L)" step="0.001">
                </div>
                
                <div class="input-field">
                    <input type="number" id="free_sulfur_dioxide" placeholder="Free SO2 (0-100 mg/L)" step="1">
                </div>
                
                <div class="input-field">
                    <input type="number" id="total_sulfur_dioxide" placeholder="Total SO2 (0-300 mg/L)" step="1">
                </div>
                
                <div class="input-field">
                    <input type="number" id="density" placeholder="Density (0.99-1.01 g/cm³)" step="0.0001">
                </div>
                
                <div class="input-field">
                    <input type="number" id="pH" placeholder="pH (2.5-4.5)" step="0.01">
                </div>
                
                <div class="input-field">
                    <input type="number" id="sulphates" placeholder="Sulphates (0-2 g/L)" step="0.01">
                </div>
                
                <div class="input-field">
                    <input type="number" id="alcohol" placeholder="Alcohol (8-15 %)" step="0.1">
                </div>
            </div>
            
            <!-- Right Side - Analysis Area -->
            <div class="analysis-section">
                <div class="scan-frame-large">
                    <div class="corner tl"></div>
                    <div class="corner tr"></div>
                    <div class="corner bl"></div>
                    <div class="corner br"></div>
                    
                    <div class="scan-content" id="scanContent">
                        <div class="wine-icon">🍷</div>
                        <div class="status-text">AWAITING ANALYSIS</div>
                    </div>
                </div>
                
                <button class="analyze-btn" id="analyzeBtn" onclick="analyzeWine()">
                    <div class="btn-icon"></div>
                    Analyze Wine Quality
                </button>
            </div>
        </div>
    </div>
    
    <!-- Bottom Decorative Frame -->
    <div class="bottom-frame"></div>
    
    <!-- System Status -->
    <div class="system-status">
        <div>SYSTEM STATUS: ACTIVE</div>
        <div>ML MODEL: LOADED</div>
        <div>ACCURACY: 92.4%</div>
    </div>
    
    <script>
        // Generate circuit dots
        const circuitDots = document.getElementById('circuitDots');
        for (let i = 0; i < 30; i++) {
            const dot = document.createElement('div');
            dot.className = 'circuit-dot';
            dot.style.left = Math.random() * 100 + '%';
            dot.style.top = Math.random() * 100 + '%';
            circuitDots.appendChild(dot);
        }
        
        // Generate sparkles on input fields
        function createSparkles() {
            const inputFields = document.querySelectorAll('.input-field');
            inputFields.forEach(field => {
                if (Math.random() > 0.7) { // 30% chance per field
                    const sparkle = document.createElement('div');
                    sparkle.className = 'sparkle';
                    sparkle.style.left = Math.random() * 90 + 5 + '%';
                    sparkle.style.top = Math.random() * 60 + 20 + '%';
                    sparkle.style.animationDelay = Math.random() * 2 + 's';
                    field.appendChild(sparkle);
                    
                    setTimeout(() => sparkle.remove(), 2000);
                }
            });
        }
        
        // Create sparkles periodically
        setInterval(createSparkles, 1000);
        
        function loadGoodWine() {
            document.getElementById('fixed_acidity').value = 7.4;
            document.getElementById('volatile_acidity').value = 0.3;
            document.getElementById('citric_acid').value = 0.5;
            document.getElementById('residual_sugar').value = 1.9;
            document.getElementById('chlorides').value = 0.076;
            document.getElementById('free_sulfur_dioxide').value = 11;
            document.getElementById('total_sulfur_dioxide').value = 34;
            document.getElementById('density').value = 0.9978;
            document.getElementById('pH').value = 3.51;
            document.getElementById('sulphates').value = 0.56;
            document.getElementById('alcohol').value = 12.5;
        }
        
        function loadBadWine() {
            document.getElementById('fixed_acidity').value = 8.5;
            document.getElementById('volatile_acidity').value = 0.8;
            document.getElementById('citric_acid').value = 0.1;
            document.getElementById('residual_sugar').value = 2.1;
            document.getElementById('chlorides').value = 0.15;
            document.getElementById('free_sulfur_dioxide').value = 5;
            document.getElementById('total_sulfur_dioxide').value = 15;
            document.getElementById('density').value = 1.001;
            document.getElementById('pH').value = 3.8;
            document.getElementById('sulphates').value = 0.4;
            document.getElementById('alcohol').value = 9.2;
        }
        
        async function analyzeWine() {
            const features = {
                fixed_acidity: parseFloat(document.getElementById('fixed_acidity').value),
                volatile_acidity: parseFloat(document.getElementById('volatile_acidity').value),
                citric_acid: parseFloat(document.getElementById('citric_acid').value),
                residual_sugar: parseFloat(document.getElementById('residual_sugar').value),
                chlorides: parseFloat(document.getElementById('chlorides').value),
                free_sulfur_dioxide: parseFloat(document.getElementById('free_sulfur_dioxide').value),
                total_sulfur_dioxide: parseFloat(document.getElementById('total_sulfur_dioxide').value),
                density: parseFloat(document.getElementById('density').value),
                pH: parseFloat(document.getElementById('pH').value),
                sulphates: parseFloat(document.getElementById('sulphates').value),
                alcohol: parseFloat(document.getElementById('alcohol').value)
            };
            
            // Validate inputs
            if (Object.values(features).some(v => isNaN(v))) {
                alert('Please fill all fields with valid numbers');
                return;
            }
            
            const analyzeBtn = document.getElementById('analyzeBtn');
            const scanContent = document.getElementById('scanContent');
            
            // Show loading
            analyzeBtn.disabled = true;
            scanContent.innerHTML = `
                <div class="spinner"></div>
                <div class="status-text">ANALYZING...</div>
            `;
            
            try {
                const response = await fetch('/api/predict', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ features: features })
                });
                
                const data = await response.json();
                
                if (data.success) {
                    displayResult(data.result);
                } else {
                    alert('Error: ' + (data.error || 'Unknown error'));
                    resetScanContent();
                }
            } catch (error) {
                alert('Error analyzing wine: ' + error.message);
                resetScanContent();
            } finally {
                analyzeBtn.disabled = false;
            }
        }
        
        function displayResult(result) {
            const isGood = result.quality === 'Good Wine';
            const scanContent = document.getElementById('scanContent');
            
            // Choose drunk person emoji and animation
            const personEmoji = isGood ? '🤵' : '🧟'; // Gentleman vs Zombie/Homeless
            const drunkClass = isGood ? 'gentleman-drunk' : 'homeless-drunk';
            const extraClass = isGood ? 'hiccup' : 'stumble';
            
            scanContent.innerHTML = `
                <div class="result-icon ${isGood ? 'good' : 'bad'} ${drunkClass}">
                    ${isGood ? '✓' : '✕'}
                </div>
                <div class="result-title ${isGood ? 'good' : 'bad'}">
                    ${result.quality.toUpperCase()}
                </div>
                <div class="${extraClass}" style="font-size: 80px; margin: 20px 0;">
                    ${personEmoji}
                </div>
                <div class="result-stats">
                    <div class="stat-line">CONFIDENCE: ${result.confidence}%</div>
                    <div class="stat-good">GOOD: ${result.good_probability}%</div>
                    <div class="stat-bad">BAD: ${result.bad_probability}%</div>
                </div>
            `;
        }
        
        function resetScanContent() {
            document.getElementById('scanContent').innerHTML = `
                <div class="wine-icon">🍷</div>
                <div class="status-text">AWAITING ANALYSIS</div>
            `;
        }
    </script>
</body>
</html>
"""
