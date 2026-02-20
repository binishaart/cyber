from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import plotly
import json

app = Flask(__name__)

# Dummy data (replace with real scraping logic if allowed)
def get_threat_data():
    data = {
        "Threat": ["Malware", "Phishing", "Ransomware", "Zero-Day", "Botnet"],
        "Count": [50, 70, 40, 10, 25]
    }
    df = pd.DataFrame(data)
    return df

@app.route("/")
def index():
    df = get_threat_data()
    
    # Create a bar chart
    fig = px.bar(df, x="Threat", y="Count", color="Count", title="Emerging Cyber Threats")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    return render_template("index.html", graphJSON=graphJSON)

if __name__ == "__main__":
    app.run(debug=True)
