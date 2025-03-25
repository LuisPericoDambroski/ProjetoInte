import os
import sys
import json
import django

# Add project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_root)

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projetoint.settings')
django.setup()

from projetoArton.models import Acessorio  # Replace with your model
json_path = os.path.join(...)  # As above
print(f"JSON path: {json_path}")  # Check this output!

def import_acessorios():
    try:
        # Path to JSON file in json-ameacas-arton
        json_path = os.path.join(
            os.path.dirname(__file__),  # Current script location (projetoArton/)
            '..',  # Go up to projetoint/
            '..',  # Go up to project root (ProjetoInte/projetoint/)
            'json-ameacas-arton',  # Target folder
            'acessorios.json'  # Your JSON file
        )
        
        with open(json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            
        # Insert data here...
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    import_acessorios()