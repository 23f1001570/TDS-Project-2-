import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_endpoint():
    """Test the quiz endpoint with demo URL"""
    
    # Configuration
    email = os.getenv('STUDENT_EMAIL')
    secret = os.getenv('SECRET_KEY')
    endpoint_url = "http://localhost:5000/quiz"
    demo_url = "https://tds-llm-analysis.s-anand.net/demo"
    
    # Test payload
    payload = {
        "email": email,
        "secret": secret,
        "url": demo_url
    }
    
    print("Testing Quiz Endpoint")
    print("=" * 50)
    print(f"Endpoint: {endpoint_url}")
    print(f"Demo URL: {demo_url}")
    print(f"Payload: {json.dumps(payload, indent=2)}")
    print("=" * 50)
    
    try:
        # Test 1: Valid request
        print("\nTest 1: Valid request")
        response = requests.post(
            endpoint_url,
            json=payload,
            headers={'Content-Type': 'application/json'}
        )
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        
        # Test 2: Invalid JSON
        print("\nTest 2: Invalid JSON")
        response = requests.post(
            endpoint_url,
            data="invalid json",
            headers={'Content-Type': 'application/json'}
        )
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        
        # Test 3: Invalid secret
        print("\nTest 3: Invalid secret")
        invalid_payload = payload.copy()
        invalid_payload['secret'] = 'wrong-secret'
        response = requests.post(
            endpoint_url,
            json=invalid_payload,
            headers={'Content-Type': 'application/json'}
        )
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        
        # Test 4: Missing fields
        print("\nTest 4: Missing fields")
        incomplete_payload = {"email": email}
        response = requests.post(
            endpoint_url,
            json=incomplete_payload,
            headers={'Content-Type': 'application/json'}
        )
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        
        print("\n" + "=" * 50)
        print("Testing completed!")
        print("Check the server logs for quiz solving progress.")
        
    except requests.exceptions.ConnectionError:
        print("\n❌ Error: Could not connect to endpoint.")
        print("Make sure the Flask server is running: python app.py")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")

if __name__ == '__main__':
    test_endpoint()
