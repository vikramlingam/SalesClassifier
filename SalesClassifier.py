import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QPushButton, QVBoxLayout, QWidget
import joblib
from sklearn.ensemble import RandomForestClassifier

class SalesClassifierApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sales Transaction Classifier")
        self.setGeometry(100, 100, 1200, 800)
        
        # Initialize model
        try:
            self.model = joblib.load('sales_classifier_model.joblib')
        except:
            self.model = self.train_default_model()
            
        self.setup_ui()
    
    def setup_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout()
        
        # Add buttons
        self.upload_btn = QPushButton("Upload Sales Data")
        self.classify_btn = QPushButton("Classify Transactions")
        self.export_btn = QPushButton("Export Results")
        
        # Add table
        self.table = QTableWidget()
        
        # Add to layout
        layout.addWidget(self.upload_btn)
        layout.addWidget(self.classify_btn)
        layout.addWidget(self.export_btn)
        layout.addWidget(self.table)
        
        self.central_widget.setLayout(layout)
        
        # Connect signals
        self.upload_btn.clicked.connect(self.upload_file)
        self.classify_btn.clicked.connect(self.classify_data)
        self.export_btn.clicked.connect(self.export_results)

    def train_default_model(self):
        # Create a simple model for demonstration
        X = [[100, 1], [200, 2], [300, 3], [1000, 1], [2000, 2], [3000, 3]]
        y = ['Retail', 'Retail', 'Retail', 'Wholesale', 'Wholesale', 'Wholesale']
        
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X, y)
        return model