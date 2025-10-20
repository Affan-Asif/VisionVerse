#!/usr/bin/env python3
"""
Generate a secure random secret key for Flask application.
Run this script to generate a new SECRET_KEY for production use.
"""

import secrets

def generate_secret_key():
    """Generate a cryptographically secure random secret key."""
    return secrets.token_hex(32)

if __name__ == '__main__':
    print("=" * 60)
    print("Flask SECRET_KEY Generator")
    print("=" * 60)
    print()
    print("Generated SECRET_KEY:")
    print("-" * 60)
    secret_key = generate_secret_key()
    print(secret_key)
    print("-" * 60)
    print()
    print("Copy this key and add it to your Render environment variables:")
    print()
    print("On Render Dashboard:")
    print("1. Go to your service → Environment")
    print("2. Add new environment variable:")
    print("   Key: SECRET_KEY")
    print("   Value: <paste the key above>")
    print("3. Click 'Save Changes'")
    print()
    print("For local development, create a .env file:")
    print(f"SECRET_KEY={secret_key}")
    print()
    print("⚠️  IMPORTANT:")
    print("- Never commit this key to Git!")
    print("- Use different keys for dev and production")
    print("- Keep this key secret!")
    print("=" * 60)

