from pathlib import Path
import re, sys
root=Path(__file__).resolve().parents[1]
errors=[]
for p in sorted((root/'skills').glob('*/SKILL.md')):
    text=p.read_text()
    if 'display_name: "[CS STANDARD]' not in text: errors.append(f"{p}: missing display prefix")
    for bad in [r'https?://', r'@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', r'\b(?:fil|w|con|vlt)_[A-Za-z0-9]+\b']:
        if re.search(bad,text): errors.append(f"{p}: possible public identifier matches {bad}")
    ph=set(re.findall(r'\[[A-Z][A-Z0-9_]+\]', text))
    if '[TO_CONFIRM]' not in ph: errors.append(f"{p}: missing TO_CONFIRM behavior")
print('\n'.join(errors) if errors else 'Validation passed')
sys.exit(bool(errors))
