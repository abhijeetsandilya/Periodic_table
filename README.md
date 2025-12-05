# Periodic_table
A simple, interactive Periodic Table explorer built with Python and Streamlit. You can click any element to view its basic details, see a Bohr-style shell diagram, and check its electron configuration.

This is a small interactive periodic table built with Python and Streamlit.
You can click any element to see its details, look at a simple Bohr-style shell diagram, and view its electron configuration. The goal of the project was mainly to learn Streamlit, organize code into modules, and make something visual and fun.
The code is split into a few short modules (data_loader.py, electron.py, plots.py, and ui_helpers.py)

## Features

Clickable periodic table

Sidebar with element info

Bohr-style electron shell visualization

Electron configuration (Aufbau-style)

Modular, beginner-friendly code

Works completely locally — no APIs needed

## Project Structure
periodic_table/
│
├── app.py               # Main Streamlit app
├── data_loader.py       # Reads and cleans element CSV
├── electron.py          # Electron config + Bohr shell logic
├── plots.py             # Matplotlib visualizations
├── ui_helpers.py        # Periodic table grid layout
├── elements_118.csv     # Element data
└── requirements.txt

## Requirements
Streamlit

pandas

matplotlib

## How to Run

Make sure you have Python 3.9+ installed.

### 1. Install the libraries manually

Run these commands in your terminal:

pip install streamlit

pip install pandas

pip install matplotlib

### 2. Go to the project folder

In your terminal, navigate to the directory containing app.py:

cd path/to/your/project

### 3. Start the app

Run Streamlit:

streamlit run app.py

### 4. Open in browser

Streamlit will open automatically, or you can visit:

http://localhost:8501

## Data
The project uses a simple CSV file (elements_118.csv) containing the atomic number, symbol, and name of all 118 elements. If you want a full dataset (mass, radius, electronegativity, etc.), you can expand the CSV and the app will display the extra fields automatically.
Improve electron configuration accuracy for more exceptions
