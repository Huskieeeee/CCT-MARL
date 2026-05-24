from pathlib import Path
import pandas as pd

root = Path(__file__).resolve().parents[1]
for csv_path in sorted((root / 'docs' / 'results').glob('*.csv')):
    print('\n==', csv_path.name)
    try:
        df = pd.read_csv(csv_path)
        print(df.head().to_string(index=False))
    except Exception as e:
        print('Could not read:', e)
