from flask import  *
import json
app = Flask(__name__)

def calculate_hospital_score(hospital, disease):
    if disease in hospital["diseases"]:
        cost = hospital["diseases"][disease]["cost"]
        capability = hospital["diseases"][disease]["rating"]
        # You can define your own scoring system here.
        # For example, a simple score can be cost divided by capability.
        score = cost // capability
        return score
    return None
def load_hospital_data():
    with open('hospital.json', 'r') as file:
        return json.load(file)

hospital_data = load_hospital_data()
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/text", methods=["GET", "POST"])
def text():
    if request.method == "POST":
        disease = request.form["disease"]
        hospitals = []
        for hospital in hospital_data:
            score = calculate_hospital_score(hospital, disease)
            if score is not None:
                hospitals.append((hospital, score))

        # Sort hospitals by score in ascending order
        hospitals.sort(key=lambda x: x[1])

        return render_template("diseases.html", hospitals=hospitals, disease=disease)

    return render_template("diseases.html", hospitals=[], disease="")
@app.route('/voice')
def voice():
    return render_template('amaan.html', audio_text=None)

@app.route('/convert', methods=['POST'])
def convert():
    audio_text = ""
    if request.method == 'POST':
        with microphone as source:
            try:
                recognizer.adjust_for_ambient_noise(source)
                audio_data = recognizer.listen(source, timeout=0.0005)
                audio_text = recognizer.recognize_google(audio_data)
            except sr.UnknownValueError:
                audio_text = "Could not understand the audio"
            except sr.RequestError as e:
                audio_text = "Error occurred during audio recognition; {0}".format(e)
    return render_template('amaan.html', audio_text=audio_text)
@app.route("/medp")
def medp():
    return render_template('medicine_price.html')
if __name__ == "__main__":
    app.run(debug=True)
