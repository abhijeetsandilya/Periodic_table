import streamlit as st

def classic_grid(df, key_pref="el"):
    periods = range(1,8)
    groups = range(1,19)
    pos = {(int(r['period']), int(r['group'])): int(r['atomic_number']) for _, r in df.dropna(subset=['period','group']).iterrows()}
    picked = None
    for p in periods:
        cols = st.columns(18, gap="small")
        for g, col in zip(groups, cols):
            with col:
                z = pos.get((p,g))
                if not z:
                    st.write("")
                else:
                    el = df[df['atomic_number']==z].iloc[0]
                    if st.button(f"{z}\n{el['symbol']}", key=f"{key_pref}_{z}"):
                        picked = int(z)
    return picked

def compact_grid(df, key_pref="el"):
    cols = st.columns(18, gap="small")
    picked = None
    for idx, row in df.iterrows():
        col_idx = idx % 18
        with cols[col_idx]:
            z = int(row['atomic_number'])
            if st.button(f"{z}\n{row['symbol']}", key=f"{key_pref}_{z}"):
                picked = z
    return picked


