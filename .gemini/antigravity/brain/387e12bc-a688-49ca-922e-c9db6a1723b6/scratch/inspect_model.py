import joblib
import os

model_path = r'c:\Users\jeebr\Documents\Projects\nlp-newton-fake-news-classification\Model\best_fake_news_model.joblib'
if os.path.exists(model_path):
    model = joblib.load(model_path)
    print(f"Model type: {type(model)}")
    if isinstance(model, dict):
        print("Model is a dictionary. Keys:", model.keys())
    
    if hasattr(model, 'feature_names_in_'):
        print(f"Feature names count: {len(model.feature_names_in_)}")
    
    # Check if it's an XGBoost model
    try:
        import xgboost as xgb
        if isinstance(model, xgb.XGBClassifier):
            print("It is an XGBoost Classifier")
            print(f"Number of features: {model.get_booster().num_features()}")
    except ImportError:
        pass
else:
    print("Model not found")
