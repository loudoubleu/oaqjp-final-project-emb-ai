''' Executing this function initiates the application of emotion
    detection/analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''

    return render_template("index.html")

@app.route("/emotionDetector")
def emo_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detection()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''

    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        formatted_response = "Invalid text! Please try again!"
    else:
        formatted_response = f"For the given statement, the system response is \
        'anger': {response['anger']}, 'disgust': {response['disgust']}, \
        'fear': {response['fear']}, 'joy': {response['joy']} and \
        'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."

    return formatted_response

if __name__ == "__main__":
    app.run(debug = True)
    