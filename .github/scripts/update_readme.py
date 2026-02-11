import json
import os
import re
from pathlib import Path

# Read current README
with open('README.md', 'r', encoding='utf-8') as f:
    readme_content = f.read()

# Find all car directories and build complete car list
cars_dir = Path('cars')
car_dirs = [d.name for d in cars_dir.iterdir() if d.is_dir()]

cars_list = []

for car_dir in sorted(car_dirs):
    ui_json_path = cars_dir / car_dir / 'ui' / 'ui_car.json'

    if not ui_json_path.exists():
        print(f"WARNING: No ui_car.json found for {car_dir}, skipping")
        continue

    # Read car metadata
    with open(ui_json_path, 'r', encoding='utf-8') as f:
        car_data = json.load(f)

    car_name = car_data.get('name', car_dir)
    car_year = car_data.get('year', '')
    description = car_data.get('description', '').split('\n\n')[0]  # Get first paragraph

    # Format display name as "Year Name" for GitHub display
    display_name = f"{car_year} {car_name}" if car_year else car_name

    print(f"Found car: {display_name}")
    cars_list.append({
        'name': display_name,
        'description': description,
        'car_dir': car_dir
    })

# Sort cars alphabetically by name (handles year prefix correctly)
cars_list.sort(key=lambda x: x['name'])

# Build new Available Cars section content with links
car_lines = [f"- **[{car['name']}](cars/{car['car_dir']}/CLAUDE.md)** - {car['description']}" for car in cars_list]
new_cars_content = '\n'.join(car_lines)

# Find and replace the Available Cars section
pattern = r'(## 🏎️ Available Cars\n\n)(.*?)(\n## )'

def replace_cars_section(match):
    header = match.group(1)
    current_content = match.group(2).strip()
    next_section = match.group(3)

    # Only update if content actually changed
    if current_content == new_cars_content:
        return match.group(0)  # No change needed

    return f"{header}{new_cars_content}{next_section}"

old_readme = readme_content
readme_content = re.sub(pattern, replace_cars_section, readme_content, flags=re.DOTALL)

# Only write if content changed
if readme_content != old_readme:
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)
    print(f"Updated README with {len(cars_list)} car(s)")
else:
    print("README is already up to date")
