import sys, os
from flask import Flask, request, make_response, jsonify
from flask_cors import CORS, cross_origin

import dialogflow
from google.api_core.exceptions import InvalidArgument
from google.protobuf.json_format import MessageToDict

DIALOGFLOW_PROJECT_ID = os.environ['GOOGLE_CLOUD_PROJECT'] # Ensure GCP Project ID is set
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/user/Downloads/service_account_keys.json" #If local machine

DOMAINS_ALLOWED = "*" # You can restrict only for your sites here
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": DOMAINS_ALLOWED}})

@app.route('/')
def index():
    return 'The server is running... Yaayy!!!'

@app.route('/get_dialogflow_agent', methods=['GET'])
def get_dialogflow_account_details():
    client = dialogflow.AgentsClient()
    parent = client.project_path(DIALOGFLOW_PROJECT_ID)
    details = client.get_agent(parent)
    return make_response(jsonify(MessageToDict(details)))

@app.route('/detect_intent', methods=['POST'])
def get_response_for_query():
    input_ = request.get_json(force=True)
    session_id = input_["session"]
    text_data = input_["queryInput"]["text"]["text"]
    language_code = input_["queryInput"]["text"]["languageCode"]

    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(
        DIALOGFLOW_PROJECT_ID, session_id)
    text_input = dialogflow.types.TextInput(
        text=text_data, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    try:
        response = session_client.detect_intent(
            session=session, query_input=query_input)
    except InvalidArgument:
        raise

    return make_response(jsonify(MessageToDict(response)))

if __name__ == '__main__':
    # Run Flask server
    app.run(port=8000, debug=True)
