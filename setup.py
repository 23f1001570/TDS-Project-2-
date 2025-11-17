"""
Setup and Installation Script
"""

import subprocess
import sys
import os
from pathlib import Path

def create_env_file():
    """Create .env file if it doesn't exist"""
    env_path = Path('.env')
    
    if env_path.exists():
        print("✓ .env file already exists")
        return
    
    print("Creating .env file...")
    
    email = input("Enter your student email: ")
    secret = input("Enter your secret key: ")
    api_key = input("Enter your OpenAI API key: ")
    
    env_content = f"""# Environment Configuration
STUDENT_EMAIL={email}
SECRET_KEY={secret}
OPENAI_API_KEY={api_key}
PORT=5000
DEBUG=True
"""
    
    env_path.write_text(env_content)
    print("✓ .env file created")

def install_dependencies():
    """Install Python dependencies"""
    print("\nInstalling dependencies...")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("✓ Dependencies installed successfully")
    except subprocess.CalledProcessError as e:
        print(f"✗ Error installing dependencies: {e}")
        return False
    return True

def create_directories():
    """Create necessary directories"""
    print("\nCreating directories...")
    dirs = ['downloads', 'outputs', 'temp']
    for dir_name in dirs:
        Path(dir_name).mkdir(exist_ok=True)
    print("✓ Directories created")

def main():
    """Main setup function"""
    print("="*50)
    print("LLM Analysis Quiz - Setup")
    print("="*50)
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("✗ Python 3.8 or higher is required")
        sys.exit(1)
    
    print(f"✓ Python {sys.version_info.major}.{sys.version_info.minor}")
    
    # Create .env file
    create_env_file()
    
    # Create directories
    create_directories()
    
    # Install dependencies
    if not install_dependencies():
        print("\n⚠ Some dependencies failed to install")
        print("You may need to install them manually")
    
    print("\n" + "="*50)
    print("Setup completed!")
    print("="*50)
    print("\nNext steps:")
    print("1. Edit .env file with your credentials")
    print("2. Run: python app.py")
    print("3. Test: python test_endpoint.py")
    print("="*50)

if __name__ == '__main__':
    main()
