# 🧮 Material Python Calculator

An elegant, themeable calculator built with Python and Streamlit.

## ✨ Features

- **Multi-Theme Support**: Switch between Material Light, Dark, and a neon Cyberpunk mode.
- **Calculation History**: Keep track of all your previous operations.
- **Unit Converter**: Convert between Length, Weight, and Temperature units.
- **Pure Python**: No JavaScript required—all logic and UI are handled in Python.

## 🚀 How to Run

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Install Dependencies

Open your terminal (Command Prompt, PowerShell, or Terminal) and navigate to your project directory:

```bash
cd calculator-app
```

Then install the required packages:

```bash
pip install -r requirements.txt
```

This will install **Streamlit**, the Python web framework we use to build the calculator.

### Step 2: Run the App

Run the following command to start the application:

```bash
streamlit run app.py
```

The app will open automatically in your default web browser at `http://localhost:8501`.

### Step 3: Explore Features

- **Calculator**: Use the two input fields to enter two numbers and the operation symbol (+, -, *, /) to calculate the result.
- **Calculation History**: See a list of all recent calculations performed.
- **Unit Converter**: Choose a unit type (Length, Weight, or Temperature), select from and to units, and convert your value instantly.
- **Themes**: Navigate to the sidebar (top left) to switch between Material Light, Material Dark, and Cyberpunk themes.

## 📋 Known Limitations

- The calculator only supports basic arithmetic operations (+, -, *, /).
- Division by zero returns an error message.

## 🛠️ Troubleshooting

- **App won't start?**
  - Ensure you have Python 3.8+ installed.
  - Run `pip install --upgrade streamlit` to update the package.
  
- **Ports blocked?**
  - If port 8501 is blocked, Streamlit will use the next available port. You can change this in `app.py` by editing the `st.page_config` section.

- **Port conflict?**
  - If the port is already in use, delete the process or change the port number in `app.py`.

## 👨‍💻 Contributing

Feel free to submit issues and pull requests!

## 📄 License

This project is open-source and available under the MIT License.

---

*Made with ❤️ using Python and Streamlit.*