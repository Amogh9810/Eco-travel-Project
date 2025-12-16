# 🌍 Eco-Friendly Travel Planner

<p align="center">
  <img src="https://sb.ecobnb.net/app/uploads/sites/3/2023/07/eco-friendly-transportation-choices-1170x490.jpg" alt="Eco-Friendly Travel Planner Screenshot" width="600"/>
</p>

**Eco-Friendly Travel Planner** is a full-stack web application designed to help users make more sustainable travel decisions by comparing different travel options based on their estimated carbon emissions and overall eco-friendliness.

## ✨ Features

* **🌱 Compare Travel Modes:** Offers comparisons between various travel modes, such as **Train**, **Bus**, and **Car**.
* **📊 Carbon Emission Estimation:** Provides estimated **CO₂ emissions** for each travel option.
* **⭐ Eco-Score Ranking:** Implements an **Eco-score ranking** system to visually highlight and encourage greener choices.
* **🔗 RESTful API Communication:** Establishes seamless **Frontend–backend communication** using a robust REST API.
* **🧩 Modular Structure:** Built with a **modular and scalable project structure** for easy maintenance and future expansion.

---

## 🛠️ Tech Stack

### Frontend
* **React** (Vite for fast development)
* **TypeScript**
* **HTML & CSS**
* **Fetch API** (for backend communication)

### Backend
* **Python**
* **Flask** (micro-framework for the API)
* **Flask-CORS** (to handle cross-origin requests)
* **RESTful API** design

---

## 🔄 How It Works

1.  The user enters their **source** and **destination** into the intuitive frontend interface.
2.  The frontend initiates a `POST` request to the backend API.
3.  The backend processes the route request and returns a set of available travel options.
4.  Each returned option includes:
    * **Distance**
    * **Estimated CO₂ emissions**
    * **Eco-score**
5.  The frontend dynamically renders and displays the comparison results to the user.

> **⚠️ Note on Data:** This project currently utilizes **mock route data** to demonstrate the full-stack architecture, data flow, and sustainability logic. It is a showcase of full-stack development skills and system design concepts.

---


## 🌱 Why This Project?

Transportation is a significant global contributor to carbon emissions. This project directly addresses this challenge by demonstrating how software systems can effectively **incorporate sustainability metrics** into everyday decision-making tools, like travel planners, empowering users to choose lower-impact options.

## 🧠 Key Learnings

* **Full-Stack Development:** Building a cohesive full-stack application using modern frameworks (React/Vite/TypeScript and Flask/Python).
* **API Design:** Designing and implementing robust REST APIs and effectively handling **CORS** issues.
* **Integration:** Mastering frontend–backend integration, data serialization, and debugging.
* **Sustainability in Software:** Applying real-world sustainability concepts and metrics within a software project.
* **System Design:** Structuring a modular, scalable, and maintainable application.

## 🔮 Future Improvements

* Integration with **OpenStreetMap** or similar services for real-time route calculation.
* Implementing **dynamic distance-based emission computation** for greater accuracy.
* Adding an **interactive map visualization** of routes.
* Developing **user accounts and travel history** functionality.
* Incorporating **AI-based eco-route recommendations**.

---
