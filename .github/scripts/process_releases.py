import json
import sys
import os
from datetime import datetime
from collections import defaultdict

# Get repository name from environment
repo_name = os.environ.get('GITHUB_REPOSITORY', 'unknown/unknown')

# Read releases
with open('releases.json', 'r') as f:
    releases = json.load(f)

# Group releases by car (tag prefix before the version)
car_releases = defaultdict(list)

for release in releases:
    tag = release['tagName']
    # Extract car name from tag (format: car_name/vYYYY.MM.DD-HHMM)
    if '/' in tag:
        car_name = tag.split('/')[0]
        car_releases[car_name].append(release)

# Sort each car's releases by date (newest first)
for car in car_releases:
    car_releases[car].sort(key=lambda x: x['publishedAt'], reverse=True)

# Generate markdown
print("# 🏎️ Latest Releases\n")
print("Download the latest version of each car mod below. All releases are compatible with Assetto Corsa with Content Manager.\n")
print("| Car | Latest Version | Release Date | Download |")
print("|-----|----------------|--------------|----------|")

# Sort cars alphabetically
for car_name in sorted(car_releases.keys()):
    latest = car_releases[car_name][0]

    # Read ui_car.json to get proper display name with year
    ui_json_path = f'cars/{car_name}/ui/ui_car.json'
    display_name = car_name.replace('_', ' ').title()  # fallback
    try:
        with open(ui_json_path, 'r', encoding='utf-8') as f:
            ui_data = json.load(f)
            car_title = ui_data.get('name', display_name)
            car_year = ui_data.get('year', '')
            # Format as "Year Name" for display
            display_name = f"{car_year} {car_title}" if car_year else car_title
    except:
        pass  # Use fallback if ui_car.json doesn't exist

    # Parse version from tag
    version = latest['tagName'].split('/')[-1] if '/' in latest['tagName'] else latest['tagName']

    # Format date
    pub_date = datetime.fromisoformat(latest['publishedAt'].replace('Z', '+00:00'))
    date_str = pub_date.strftime('%Y-%m-%d')

    # Construct URLs from repo name and tag
    tag_name = latest['tagName']
    download_url = f"https://github.com/{repo_name}/releases/download/{tag_name}/{car_name}_{version}.zip"
    all_releases_url = f"https://github.com/{repo_name}/releases?q={car_name}"

    print(f"| **{display_name}** | `{version}` | {date_str} | [⬇️ Download]({download_url}) · [All Versions]({all_releases_url}) |")

print("\n---")
print("\n### Installation\n")
print("**Recommended Method:** Drag and drop the downloaded zip file onto Content Manager window.\n")
print("**Manual Method:** Extract to `assettocorsa/content/cars/` — the car will appear in your car list.\n")
print("\n---")
print(f"\n*Last updated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')} • [View All Releases](https://github.com/{repo_name}/releases)*")
