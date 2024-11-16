# SalesClassifier

A Python GUI application that automatically classifies sales transactions using machine learning.

## Overview
This application demonstrates how to:
```
• Build a PyQt5 GUI application for data processing
• Incorporate a machine learning model for classification
• Handle large data files
• Export results to Excel
• Package everything into a standalone executable
```

## Features
```
✨ Drag-and-drop interface for CSV/Excel files
🔄 Automatic classification of sales transactions
⏱️ Real-time processing with progress feedback
📊 Export results to Excel
👥 No Python knowledge required for end users
```

## Installation
```
1. Download the latest release
2. Extract to your preferred location
3. Run SalesClassifier.exe
```

## For Developers
If you want to modify the source code:

### Clone the repository
```bash
git clone https://github.com/yourusername/sales-classifier.git
```

### Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run the application
```bash
python main.py
```

## Creating Executable

### Install auto-py-to-exe
```bash
pip install auto-py-to-exe
```

### Convert to executable
```bash
python -m auto-py-to-exe
```

### In auto-py-to-exe:
```
1. Select main.py as Script Location
2. Choose "One Directory"
3. Add sales_classifier_model.joblib as Additional Files
4. Convert!
```

## Sample Data Structure
The application expects CSV/Excel files with the following columns:
```
transaction_date | amount | items | customer_type | region
2024-01-01      | 1000   | 5     | New          | North
2024-01-02      | 500    | 2     | Existing     | South
```

## Model Details
The ML model classifies transactions into categories:
```
• Retail
• Wholesale
• Online
• B2B
• Special Orders
```

Based on features like:
```
• Transaction amount
• Number of items
• Customer type
• Regional patterns
```

## Contributing
Feel free to submit issues and pull requests.

## Acknowledgments
```
• PyQt5 for the GUI framework
• scikit-learn for ML capabilities
• auto-py-to-exe for making distribution possible
```
