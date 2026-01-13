from sklearn.ensemble import IsolationForest
from sklearn.feature_extraction.text import TfidfVectorizer

# ML algo Processor/ logic
class LogAnomalyDetector:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.model = IsolationForest(
            contamination=0.1, # assume 10% logs are abnormal
            random_state=42
        )
        self.is_trained = False

    def train(self, log_messages):
        """
        Train model on log messages
        """
        X = self.vectorizer.fit_transform(log_messages)
        self.model.fit(X)
        self.is_trained = True
    
    def detect(self, log_messages):
        """
        Detect anomalies in logs
        """
        if not self.is_trained:
            raise Exception("Model not trained")

        X = self.vectorizer.transform(log_messages)
        predictions = self.model.predict(X)

        # -1 = anomaly, 1 = normal
        return predictions
