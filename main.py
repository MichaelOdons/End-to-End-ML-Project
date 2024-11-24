import sys
import os

# Add the 'src' folder to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from src.config.configuration import main