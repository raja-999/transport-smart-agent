🚇 Transport Smart Agent
Intelligent Transport Recommendation System
Chatbot + n8n Automation + FastAPI API + NSGA-II Optimization
🎯 Project Goal

This project demonstrates how to build an end-to-end intelligent transport recommendation system using:

🌐 FastAPI (backend prediction API)

🤖 NSGA-II (multi-objective optimization)

🔁 n8n (workflow automation)

💬 Chatbot (WhatsApp/Telegram interface)

🧪 Synthetic Data (privacy-safe student dataset)

The system suggests the optimal transport mode for a user based on:

Distance to school

Age

Current mode

Car / Bike ownership

Driving license

Comfort preference

Cost preference

Environmental preference

Punctuality preference

🔄 How the System Works (Pipeline)

User fills a transport form (Google Form / Web form / Chatbot)

n8n receives the submission using a Webhook

n8n sends the data to the FastAPI endpoint /predict

FastAPI runs the NSGA-II + ML model

The model returns a recommended transport mode

n8n forwards the result to WhatsApp / Telegram / Email

The user receives a personalized transport recommendation

This pipeline replicates how real companies connect AI models to chatbots.
