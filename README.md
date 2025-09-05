# Analyse automatique des réponses à des formulaires numériques

🎓 Projet de fin de cycle – Ingénierie Informatique  
👨‍💻 Développeur : Tayo Tate Desmond Corentin  
📌 Objectif : automatiser l’analyse des réponses ouvertes des formulaires pour gagner du temps et extraire des insights pertinents.

---

## 🚀 Fonctionnalités

L’application propose 3 fonctionnalités principales :  

1. **Détection d’objectif du formulaire**  
   - Analyse les questions du formulaire pour déterminer son objectif principal  
   - Catégories : Satisfaction client, Étude de marché, Analyse de performance, Planification d’événement, Autre  

2. **Résumé automatique des réponses ouvertes**  
   - Résume de manière abstractif les réponses collectées  
   - Permet d’identifier rapidement les points clés exprimés par les utilisateurs  

3. **Chatbot intelligent**  
   - Répond aux questions basées uniquement sur les données importées du formulaire  
   - Permet une interaction instantanée avec les réponses collectées  

---

## 🛠️ Technologies utilisées

- **Langages & Frameworks** : Python, Streamlit  
- **Data** : Pandas, JSON  
- **LLM** : Ollama (local), Hugging Face (en ligne)  
- **NLP** : Transformers, NLTK, spaCy (pour prétraitement optionnel)  
- **API & Environnements** : Hugging Face Inference API, Python-dotenv  

---

## 📂 Structure du projet

form-response-analyzer/
│── app.py # Script principal Streamlit
│── requirements.txt # Dépendances Python
│── .env # Variables d'environnement (API keys)
│── README.md # Documentation du projet
│── 📂 src/
│ └── llm_helper.py # Abstraction pour LLM (local ou Hugging Face)
│── 📂 data/ # Exemple de données anonymisées
│ ├── sample_data_chatbot.json
│ ├── sample_data_form_goal.json
│ ├── sample_data_summarization1.json
│ ├── sample_data_summarization2.json
│ └── test_data_for_form_goal.json
│── 📂 notebooks/ # Notebooks pour expérimentations
│ ├── chatbot.ipynb
│ └── form_goal.ipynb


---

## ⚡ Installation

1. **Cloner le dépôt**  
```bash
git clone https://github.com/ton-username/automatic-form-analysis.git
cd automatic-form-analysis


2. **Créer un environnement virtuel (optionnel mais recommandé)**

python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows


3. **Installer les dépendances**

pip install -r requirements.txt


4. **Créer un fichier .env avec vos clés API :**

# Clé Hugging Face Inference API
HF_API_KEY=hf_xxxxxxxxxxxxxxxxxxxxx

5. **🏃‍♂️ Lancer l’application**
streamlit run app.py

* L’interface Streamlit s’ouvrira dans ton navigateur.

* Tu pourras choisir la fonctionnalité depuis la sidebar et uploader tes fichiers CSV/JSON.

📌 Exemple d’utilisation

1. **Détection d’objectif**

* Upload d’un fichier questions.csv ou questions.json

* Clique sur “Analyser l’objectif” → résultat affiché directement

2. **Résumé automatique**

* Upload d’un fichier responses.json contenant les réponses ouvertes

* Clique sur “Générer le résumé” → résumé abstractif des réponses

3. **Chatbot intelligent**

* Upload d’un fichier CSV/JSON avec les données

* Posez vos questions dans le champ texte → le chatbot répond basé uniquement sur vos données

🔗 Liens utiles

* Hugging Face Models – Mistral

* Streamlit Documentation

---

## 📓 Notebooks Colab

Pour mieux comprendre le fonctionnement et le prototypage des fonctionnalités, deux notebooks Colab sont disponibles :  

1. **Chatbot RAG (Retrieval-Augmented Generation)**  
   - Prototype du chatbot intelligent utilisant des données de formulaire  
   - Explore la logique RAG et les interactions avec le modèle  
   - [Ouvrir dans Colab](https://colab.research.google.com/drive/19Gdn3ychZTzWUWjaVR2pHmYwREOjjkmR?usp=sharing)  

2. **Détection d’objectif du formulaire**  
   - Notebook démontrant l’analyse automatique des questions  
   - Permet de tester l’extraction d’objectif avec différents jeux de données  
   - [Ouvrir dans Colab](https://colab.research.google.com/drive/12E6Mj7iUW6MMUluLj9NZX9b8gCGrLHjX?usp=sharing)  


📜 Licence

Ce projet est sous licence MIT.
Libre d’utilisation, modification et distribution.


---