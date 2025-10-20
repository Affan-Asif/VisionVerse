#!/usr/bin/env python3
"""
Quick test script to verify the application works locally before deploying.
This script tests the basic functionality without needing a browser.
"""

import requests
import time
import sys

def test_health_check(base_url):
    """Test the health check endpoint"""
    print("Testing health check endpoint...")
    try:
        response = requests.get(f"{base_url}/health", timeout=10)
        if response.status_code == 200:
            print("✓ Health check passed!")
            print(f"  Response: {response.json()}")
            return True
        else:
            print(f"✗ Health check failed with status {response.status_code}")
            return False
    except Exception as e:
        print(f"✗ Health check failed: {e}")
        return False

def test_index_page(base_url):
    """Test the index page loads"""
    print("\nTesting index page...")
    try:
        response = requests.get(base_url, timeout=10)
        if response.status_code == 200:
            print("✓ Index page loaded successfully!")
            return True
        else:
            print(f"✗ Index page failed with status {response.status_code}")
            return False
    except Exception as e:
        print(f"✗ Index page failed: {e}")
        return False

def main():
    base_url = "http://localhost:5000"
    
    print("=" * 50)
    print("YOLOv11 Object Detection - Local Test")
    print("=" * 50)
    print(f"\nTesting server at: {base_url}")
    print("Make sure the server is running with: python app.py")
    print()
    
    # Wait a bit for server to be ready
    print("Waiting for server to be ready...")
    time.sleep(2)
    
    # Run tests
    health_ok = test_health_check(base_url)
    index_ok = test_index_page(base_url)
    
    print("\n" + "=" * 50)
    if health_ok and index_ok:
        print("✓ All tests passed!")
        print("\nYour application is ready for deployment!")
        print("\nNext steps:")
        print("1. Test the web interface at http://localhost:5000")
        print("2. Try the live camera feature (click 'Start Camera')")
        print("3. Test image upload")
        print("4. Deploy to Render!")
        return 0
    else:
        print("✗ Some tests failed!")
        print("\nTroubleshooting:")
        print("1. Make sure the server is running: python app.py")
        print("2. Check if port 5000 is available")
        print("3. Verify all dependencies are installed: pip install -r requirements.txt")
        return 1

if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\nTest interrupted by user")
        sys.exit(1)

