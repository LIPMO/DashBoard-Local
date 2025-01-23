from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Données simulées pour les liens
links = [
    {"name": "Google", "url": "https://www.google.com", "icon": "/static/images/default-icon.png"},
    {"name": "YouTube", "url": "https://www.youtube.com", "icon": "/static/images/default-icon.png"},
]

@app.route("/")
def display_links():
    return render_template("display.html", links=links)

@app.route("/edit", methods=["GET", "POST"])
def edit_links():
    if request.method == "POST":
        name = request.form.get("name")
        url = request.form.get("url")
        icon = request.form.get("icon") or "/static/images/default-icon.png"
        links.append({"name": name, "url": url, "icon": icon})
        return redirect(url_for("display_links"))
    return render_template("edit.html", links=links)

@app.route("/delete/<int:link_id>")
def delete_link(link_id):
    if 0 <= link_id < len(links):
        links.pop(link_id)
    return redirect(url_for("display_links"))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
