from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/competitors')
def get_competitors():
    data = [
        {
            "competitor": "Accenture",
            "collaboration": "Worked with Liberty Global (Virgin Media’s parent company) on automation and video transformation.",
            "source": "https://newsroom.accenture.com/news/2024/virgin-media-o2-partners-with-accenture-to-enhance-private-5g-solutions-for-uk-businesses-tapping-into-estimated-half-a-billion-pound-uk-market"
        },
        {
            "competitor": "TCS",
            "collaboration": "Digital transformation partner for Liberty Global (Virgin Media’s parent).",
            "source": "https://www.tcs.com/what-we-do/industries/communications-media-information-services/case-study/vodafone-hungary-fixed-telco-services"
        },
        {
            "competitor": "Cognizant",
            "collaboration": "Provided consulting and modernization services to Virgin Media Ireland.",
            "source": "https://www.cognizant.com/us/en/newsroom/press-releases/virgin-media-ireland-partners-with-cognizant-to-modernize-operations"
        },
        {
            "competitor": "Capgemini",
            "collaboration": "Handled cloud infrastructure for Liberty Global.",
            "source": "https://www.capgemini.com/ca-en/industries/telecommunications/digital-transformation/"
        }
    ]
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
