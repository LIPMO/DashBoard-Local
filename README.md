# 🚀 DashBoard-Local  

**DashBoard-Local** est un tableau de bord auto-hébergé qui vous permet de centraliser vos applications locales et liens préférés dans une interface moderne et personnalisable. Inspiré du style iOS dark, il offre une expérience fluide et intuitive.  

## ✨ Fonctionnalités  
- 📌 **Ajout et gestion d’applications** (nom, URL, icône personnalisée).  
- 🎨 **Interface moderne** avec un design inspiré du thème iOS dark.  
- 💾 **Stockage local** des applications dans un fichier JSON.  
- 🌐 **Accès via le réseau local** grâce à un serveur Flask.  
- ⚡ **Transitions fluides** et ergonomie optimisée.  

---

## 📥 Installation  

### 🔹 1. Prérequis  
- **Python 3.x**  
- **Flask** (serveur web)  

### 🔹 2. Cloner le dépôt  
```bash
git clone https://github.com/LIPMO/DashBoard-Local.git
cd DashBoard-Local
```

### 🔹 3. Installer les dépendances  
```bash
pip install flask
```

### 🔹 4. Lancer le serveur  
```bash
python app.py
```
Le tableau de bord sera accessible sur **http://localhost:3000** 🚀  

---

## 🛠️ Configuration  
Les applications sont stockées dans le fichier **data/apps.json**. Vous pouvez les modifier manuellement ou via l’interface.  

---

## 🎨 Personnalisation  
Le design peut être modifié dans les fichiers **HTML, CSS et JavaScript** situés dans le dossier `static/`.  

---

## 📜 Licence  
Ce projet est sous licence **MIT**.  

---

💡 **Idéal pour ceux qui veulent une alternative locale et personnalisable à Heimdall ou Dashy !**