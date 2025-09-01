import re
import tldextract
import pandas as pd

def extract_features(url):
    features = {}
    
    # Length of URL
    features['url_length'] = len(url)
    
    # Number of dots
    features['num_dots'] = url.count('.')
    
    # Number of slashes
    features['num_slash'] = url.count('/')
    
    # Check if IP address is used
    ip_pattern = r'(\d{1,3}\.){3}\d{1,3}'
    features['has_ip'] = 1 if re.search(ip_pattern, url) else 0
    
    # HTTPS present or not
    features['https'] = 1 if url.startswith("https") else 0
    
    # Extract domain parts
    ext = tldextract.extract(url)
    features['domain_length'] = len(ext.domain)
    
    # Suspicious words
    suspicious_words = ['login', 'verify', 'bank', 'update', 'free']
    features['has_suspicious_word'] = 1 if any(word in url.lower() for word in suspicious_words) else 0
    
    return features

# Helper: Convert full dataset (CSV) into features DataFrame
def extract_features_from_dataset(csv_file):
    data = pd.read_csv(csv_file)
    feature_list = []
    
    for url in data['url']:
        feats = extract_features(url)
        feature_list.append(feats)
    
    features_df = pd.DataFrame(feature_list)
    features_df['label'] = data['label']
    return features_df

# Direct test run
if __name__ == "__main__":
    test_url = "http://fakebank-login.com/verify"
    print("Test Features:", extract_features(test_url))
