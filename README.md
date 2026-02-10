# 🏠 House Price Prediction Web App

A simple and interactive **machine learning web application** that predicts house prices in Bangalore based on user inputs like area, BHK, bathrooms, balconies, and location.

The project combines **Machine Learning + Flask** to deliver real-time predictions through a clean web interface.

---

## ✨ Features

- Predict house prices in **₹ Lakhs**
- User-friendly web interface
- Location dropdown for easy selection
- Trained on real Bangalore housing data
- Clean dark-themed UI

---

## 🛠 Tech Stack

- **Python**
- **Pandas, NumPy**
- **Scikit-learn**
- **Flask**
- **HTML & CSS**
- **Git & GitHub**

---
## 🤖 Machine Learning Details

### 🔄 Steps Involved

- Data cleaning and preprocessing  
- Feature engineering  
- Train–test split  
- Model training and evaluation  

### 🧪 Training Environment

- Model training and experimentation were performed in **Google Colab**

### 📦 Model File

- The trained model file (`.pkl`) is **excluded from the repository** due to GitHub file size limitations


---

## 📊 Dataset

- Bangalore House Prices dataset  
- ~13,000 cleaned records  
- **Target:** House Price (₹ Lakhs)

### 🔢 Input Features

- Total Square Feet  
- BHK  
- Bathrooms  
- Balconies  
- Location  

---

## 🚀 How the App Works

1. User enters property details  
2. Data is sent to the Flask backend  
3. Machine learning model predicts the price  
4. Predicted price is displayed on the screen  

---

## 📂 Project Structure

```text
HOUSEPRICE/
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── app.py
├── bengaluru_house_prices.csv
├── House_Price_Prediction.ipynb
└── README.md
