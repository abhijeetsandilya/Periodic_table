import streamlit as st
import pandas as pd
from data_loader import load_elements, get_by_z
from ui_helpers import classic_grid, compact_grid
from plots import bohr_figure, subshell_bar
from electron import config, config_text

st.set_page_config(layout="wide", page_title="Periodic Table — Clean")

df = load_elements("elements_118.csv")

st.title("Periodic Table")
st.write("Click an element.Sidebar has view options.")

classic = ('group' in df.columns and 'period' in df.columns and df['group'].notna().any() and df['period'].notna().any())

st.subheader("Table")
picked = classic and classic_grid(df) or compact_grid(df)

if 'Z' not in st.session_state:
    st.session_state['Z'] = 1
if picked:
    st.session_state['Z'] = picked

Z = int(st.session_state['Z'])
el = get_by_z(df, Z)

st.sidebar.header(f"{el['name']} ({el['symbol']}) — Z={Z}")
view = st.sidebar.radio("View", ["Basic", "Bohr", "Subshells", "Download CSV"])

if view == "Basic":
    st.sidebar.write(f"Name: {el['name']}")
    st.sidebar.write(f"Symbol: {el['symbol']}")
    st.sidebar.write(f"Atomic number: {Z}")
    if 'group' in df.columns and not pd.isna(el.get('group')):
        st.sidebar.write(f"Group: {el.get('group')}, Period: {el.get('period')}")
    st.sidebar.write("---")
    # show rest of CSV fields
    for c in df.columns:
        if c in ('atomic_number','symbol','name','group','period'):
            continue
        v = el.get(c, "")
        if pd.isna(v):
            v = ""
        st.sidebar.write(f"{c}: {v}")

elif view == "Bohr":
    st.header(f"Bohr (illustrative) — {el['name']}")
    fig = bohr_figure(Z)
    st.pyplot(fig)

elif view == "Subshells":
    st.header(f"Subshells — {el['name']}")
    fig = subshell_bar(Z)
    st.pyplot(fig)
    cfg = config(Z)
    st.write("Approx config:")
    st.code(config_text(cfg))

else:
    st.sidebar.download_button("Download CSV", data=open("elements_118.csv","rb"), file_name="elements_118.csv", mime="text/csv")

col1, col2 = st.columns([1,2])
with col1:
    st.markdown(f"### {el['name']} ({el['symbol']}) — Z={Z}")
    st.write(pd.DataFrame([el.drop(labels=['atomic_number']).to_dict()]))

with col2:
    fig1 = bohr_figure(Z)
    st.pyplot(fig1)


