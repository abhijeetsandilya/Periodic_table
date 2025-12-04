import pandas as pd

def load_elements(path="elements_118.csv"):
    df = pd.read_csv(path)
    df.columns = [c.strip() for c in df.columns]
    if 'atomic_number' not in df.columns:
        raise ValueError("CSV needs an 'atomic_number' column.")
    df['atomic_number'] = df['atomic_number'].astype(int)
    df = df.sort_values('atomic_number').reset_index(drop=True)

    # optional tidy-ups
    if 'group' in df.columns:
        df['group'] = pd.to_numeric(df['group'], errors='coerce').astype('Int64')
    if 'period' in df.columns:
        df['period'] = pd.to_numeric(df['period'], errors='coerce').astype('Int64')
    return df

def get_by_z(df, z):
    row = df[df['atomic_number'] == int(z)]
    return row.iloc[0] if not row.empty else None

def find_by_symbol(df, s):
    return df[df['symbol'].str.lower() == s.lower()]

def search_name(df, name):
    return df[df['name'].str.lower().str.contains(name.lower())]