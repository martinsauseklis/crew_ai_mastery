"""
Quick setup script for AI Mastery Platform.

This script helps you get started quickly by:
1. Checking Python version
2. Creating virtual environment (optional)
3. Installing dependencies
4. Setting up .env file
"""

import sys
import subprocess
import os
from pathlib import Path


def check_python_version():
    """Check if Python version is 3.10 or higher."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 10):
        print(f"❌ Python 3.10+ required. You have Python {version.major}.{version.minor}")
        sys.exit(1)
    print(f"✓ Python {version.major}.{version.minor} detected")


def install_dependencies():
    """Install required Python packages."""
    print("\n📦 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ Dependencies installed successfully")
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        sys.exit(1)


def setup_env_file():
    """Create .env file from template."""
    env_file = Path(".env")
    env_example = Path(".env.example")

    if env_file.exists():
        print("\n✓ .env file already exists")
        return

    if env_example.exists():
        print("\n📝 Creating .env file...")
        env_example.read_text()
        with open(env_file, 'w') as f:
            f.write(env_example.read_text())
        print("✓ .env file created")
        print("\n⚠️  IMPORTANT: Edit .env and add your API key(s)")
        print("   - OPENAI_API_KEY or ANTHROPIC_API_KEY")
    else:
        print("\n⚠️  .env.example not found")


def main():
    """Run the setup process."""
    print("🚀 AI Mastery Platform - Setup\n")

    check_python_version()
    install_dependencies()
    setup_env_file()

    print("\n" + "="*60)
    print("✅ Setup complete!")
    print("="*60)
    print("\nNext steps:")
    print("1. Edit .env and add your API key(s)")
    print("2. Run: python main.py run")
    print("\nFor help: python main.py --help")
    print("="*60)


if __name__ == "__main__":
    main()
