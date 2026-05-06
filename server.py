from EmotionDetection.emotion_detection import emotion_detector
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def render_index_page():
    return render_template("index.html")

@app.route("/emotionDetector")
def emo_detector():
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    formatted_response = f"For the given statement, the system response is \
    'anger': {response['anger']}, 'disgust': {response['disgust']}, \
    'fear': {response['fear']}, 'joy': {response['joy']} and \
    'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."

    return formatted_response

if __name__ == "__main__":
    app.run(debug = True)

