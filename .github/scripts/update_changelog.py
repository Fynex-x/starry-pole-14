import yaml
import datetime
import os
import sys
import subprocess

changelog_dir = 'Resources/Changelog/'
os.makedirs(changelog_dir, exist_ok=True)

now = datetime.datetime.now()
timestamp = now.strftime('%Y%m%d_%H%M%S')
file_name = f"auto_{timestamp}.yml"
file_path = os.path.join(changelog_dir, file_name)

commit_author = os.getenv('GITHUB_ACTOR', 'Unknown')
try:
    msg = subprocess.check_output(['git', 'log', '-1', '--pretty=%B']).decode('utf-8').strip()
    if not msg or "Auto-update" in msg:
        sys.exit(0)
    commit_message = msg
except:
    commit_message = "Автоматическое изменение"

entry_data = {
    'author': commit_author,
    'changes': [
        {
            'message': commit_message,
            'type': 'Tweak'
        }
    ]
}

with open(file_path, 'w', encoding='utf-8') as f:
    yaml.dump(entry_data, f, allow_unicode=True, sort_keys=False, default_flow_style=None, indent=2)

print(f"Created: {file_name}")
