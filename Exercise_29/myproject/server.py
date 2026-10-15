from flask import Flask, app, render_template,url_for

# Source - https://stackoverflow.com/a/23327352
# Posted by Martijn Pieters, modified by community. See post 'Timeline' for change history
# Retrieved 2026-10-14, License - CC BY-SA 4.0

app = Flask(__name__, template_folder='template')  # still relative to module



@app.route("/")
def my_site():
    return render_template("./index.html")



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
