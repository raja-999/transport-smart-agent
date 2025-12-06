# 🚇 Transport Smart Agent

**Intelligent Transport Recommendation System**  
*Chatbot + n8n Automation + FastAPI API + NSGA-II Optimization*

---

## 🎯 Project Goal

This project demonstrates a full **end-to-end intelligent transport recommendation system** that suggests the **optimal transport mode** for a user based on multiple personal and contextual factors.

The system integrates:

- 🌐 **FastAPI** – Backend prediction API  
- 🤖 **NSGA-II** – Multi-objective optimization  
- 🔁 **n8n** – Workflow automation  
- 💬 **Chatbot** – WhatsApp / Telegram interface  
- 🧪 **Synthetic Data** – Privacy-safe student dataset  

**User inputs considered:**  

- Distance to school  
- Age  
- Current transport mode  
- Car / Bike ownership  
- Driving license  
- Comfort preference  
- Cost preference  
- Environmental preference  
- Punctuality preference  

---

## 🔄 How the System Works (Pipeline)

1. **User submits transport data** via a Google Form, web form, or chatbot.  
2. **n8n receives the submission** through a Webhook.  
3. **n8n forwards the data** to the FastAPI `/predict` endpoint.  
4. **FastAPI processes the request** using NSGA-II + ML model.  
5. **The model returns a recommended transport mode.**  
6. **n8n sends the recommendation** to the user via WhatsApp / Telegram / Email.  

This setup mirrors **real-world applications** connecting AI models with user interfaces for smart recommendations.  

---

## 🚀 How to Use the n8n Workflow

1. Log in to [n8n.io](https://n8n.io) (cloud or self-hosted).  
2. Create a new workflow.  
3. Import **`Transport Workflow.json`**.  
4. Copy the generated **Webhook URL**.  
5. Run the workflow.  
6. Submit transport data from your form.  
7. Receive a **personalized recommendation** on WhatsApp / Telegram.  

---

## 👩‍💻 Author & Citation

**Raja Ben Bey**  
Master's in Data Science (Decision Support & Optimization)  

Passionate about **AI, optimization, automation & smart mobility**  

If you use this project, please cite:  
