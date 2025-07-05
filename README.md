
<h1 align="center"> 🤖AI-CODE-EXPLAINER </h1>



<p align="center">
  A web app built with Streamlit that explains <strong>Python and <strong>JavaScript code snippets in beginner-friendly language using <strong>Gemini (Google's Generative AI).
---
</p>

<p align="center">
  <img src="https://img.shields.io/badge/AI-Powered-blueviolet?style=flat-square&logo=google" />
  <img src="https://img.shields.io/badge/Made%20With-Streamlit-ff4b4b?style=flat-square&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" />
</p>




## 🚀 Features

🧠 Explains Python and JavaScript code for beginners

✨ Clean and responsive UI using Streamlit

🔐 Secure usage of API keys via .env

⚡ Powered by Google's Gemini 1.5 Flash model
---

## 📂 Project Structure


```bash
├── app.py             
├── .env               
├── requirements.txt   
└── README.md 
```         

## 📦 Installation

### 1️⃣Clone the repo

```bash 
git clone https://github.com/vermaaryan11/code-Explainer/new/main?readme=1
cd your-repo-name
```
---

### 2️⃣ Clone the repo
```bash 
python -m venv venv
source venv/bin/activate    
```
---

### 3️⃣ Install dependecies 
```bash
pip install -r requirements.txt
```

---
### 4️⃣ Set your Gemini API key 

Create a .env file in the root directory with:

```bash
GEMINI_API_KEY=your_google_generative_ai_key
```



## 🔑 Gemini API Setup

1. Visit: [Google AI Studio](https://makersuite.google.com/app)  
2. Generate API Key from: [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)  

3. In `main.py`:


```python
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")
```
---## 📦 Tech Stack

| Technology     | Description                        |
|----------------|------------------------------------|
| ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)     | Flask backend server          |
| ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)       | Interactive UI frontend       |
| ![Gemini](https://img.shields.io/badge/Gemini_API-ff6f00?logo=google&logoColor=white) | AI analysis and suggestions   |

---

## 📸 Screenshots

<b>Interface
![Screenshot 2025-07-04 143208](https://github.com/user-attachments/assets/4edaed76-dd9d-480c-88a6-5d587cacb0e4)

<b>Giving Pyhton code as input
![Screenshot 2025-07-04 144053](https://github.com/user-attachments/assets/394ed563-fbcd-4e14-8ec9-4afd96e02a15)
<b>Output
![Screenshot 2025-07-04 144103](https://github.com/user-attachments/assets/ac1efda9-5bdb-41ae-a213-8e8c11f86f45)

![Screenshot 2025-07-04 144108](https://github.com/user-attachments/assets/0c6bef03-8fce-42c2-8e58-f20caa64f41d)

<b>Giving JavaScript code as input
![Screenshot 2025-07-04 144601](https://github.com/user-attachments/assets/d5d70902-7b1c-49d5-89b4-4c0c660696ca)
<b>JS code output
![Screenshot 2025-07-04 144609](https://github.com/user-attachments/assets/14375c8f-a53f-498d-815d-34dca3d0f157)

![Screenshot 2025-07-04 144613](https://github.com/user-attachments/assets/e6b9e6a9-e55b-4eab-9e08-e93d0f758510)


---


##  📄 License 

 This project is licensed under the **MIT License** 
 
   ---
## Made by Aryan Verma
🤝 


