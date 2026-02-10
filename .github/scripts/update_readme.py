import json
import os
import re
from pathlib import Path

# Read current README
with open('README.md', 'r', encoding='utf-8') as f:
    readme_content = f.read()

# Find all car directories
cars_dir = Path('cars')
car_dirs = [d.name for d in cars_dir.iterdir() if d.is_dir()]

# Track if we need to update
cars_to_add = []

for car_dir in sorted(car_dirs):
    ui_json_path = cars_dir / car_dir / 'ui' / 'ui_car.json'

    if not ui_json_path.exists():
        print(f"⚠️  No ui_car.json found for {car_dir}, skipping")
        continue

    # Read car metadata
    with open(ui_json_path, 'r', encoding='utf-8') as f:
        car_data = json.load(f)

    car_name = car_data.get('name', car_dir)
    car_year = car_data.get('year', '')
    description = car_data.get('description', '').split('\n\n')[0]  # Get first paragraph

    # Format display name as "Year Name" for GitHub display
    display_name = f"{car_year} {car_name}" if car_year else car_name

    # Check if car is already in README's Available Cars section
    available_cars_section = readme_content.split('## 🏎️ Available Cars')[1].split('##')[0] if '## 🏎️ Available Cars' in readme_content else ''

    # More robust detection: normalize whitespace and check multiple patterns
    def normalize(text):
        return ' '.join(text.strip().split())

    base_car_name = car_name.replace(' (AT)', '').replace(' (MT)', '').strip()
    normalized_display = normalize(display_name)
    already_exists = False

    for line in available_cars_section.split('\n'):
        if line.strip().startswith('- **'):
            normalized_line = normalize(line)
            # Extract just the car name from line (between ** and **)
            if '**' in normalized_line:
                line_name = normalized_line.split('**')[1] if len(normalized_line.split('**')) > 1 else ''
                # Check for exact match (year + name)
                if normalized_display == normalize(line_name):
                    already_exists = True
                    print(f"✓ Car already in README: {display_name}")
                    break

    if not already_exists:
        print(f"🆕 New car detected: {display_name}")
        cars_to_add.append({
            'name': display_name,
            'description': description
        })

if cars_to_add:
    # Find the "Available Cars" section and update it
    # Look for the pattern between "## 🏎️ Available Cars" and the next "##"
    pattern = r'(## 🏎️ Available Cars\n\n)(.*?)(\n## )'

    def replace_cars_section(match):
        header = match.group(1)
        current_content = match.group(2)
        next_section = match.group(3)

        # Parse existing cars into a dict (keyed by normalized name for deduplication)
        cars_dict = {}
        for line in current_content.strip().split('\n'):
            if line.startswith('- **'):
                # Extract car name from between ** markers
                if '**' in line and ' - ' in line:
                    name_part = line.split('**')[1].strip()
                    desc_part = line.split(' - ', 1)[1].strip() if ' - ' in line else ''
                    # Use year+name as key for deduplication
                    cars_dict[name_part] = {'name': name_part, 'description': desc_part}

        # Add new cars (won't duplicate due to dict keying)
        for car in cars_to_add:
            cars_dict[car['name']] = car

        # Sort cars alphabetically by name (handles year prefix correctly)
        sorted_cars = sorted(cars_dict.values(), key=lambda x: x['name'])

        # Reconstruct section
        car_lines = [f"- **{car['name']}** - {car['description']}" for car in sorted_cars]
        new_content = '\n'.join(car_lines)
        return f"{header}{new_content}{next_section}"

    readme_content = re.sub(pattern, replace_cars_section, readme_content, flags=re.DOTALL)

    # Write updated README
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)

    print(f"✅ Added {len(cars_to_add)} new car(s) to README")
else:
    print("✅ README is up to date")
