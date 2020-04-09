## Dialogflow Gateway HTTP API
A simple python-based open source implementation of dialogflow-gateway HTTP API for Dialogflow.  
Originally developed to work with [Dialogflow Web UI](https://github.com/narVidhai/Dialogflow-Web-Chatbot-UI).

### Requirements
- Python>=3.7
- `pip install -r requirements.txt`
- Setup the credentials in `main.py`

### Deployment

#### Serving locally
1. Run the server: `python main.py`
2. Expose it to Internet. (Example: `ngrok http 8000`)

#### Hosting on GCP App Engine
0. Optional: `gcloud app create` (Only do this unless there's no default service)
1. `gcloud app deploy app.yaml` (Set the `service` paramter in `app.yaml` to deploy in addition to the default service)

You can now use the deployed server as the `API_URL` for the [Web UI](https://github.com/narVidhai/Dialogflow-Web-Chatbot-UI).

### HTTP Endpoints

- To retrieve agent details: `/get_dialogflow_agent` ([Request-Response Format](https://github.com/mishushakov/dialogflow-gateway-docs#retrieving-agents))
- To get Dialogflow response for a query: `/detect_intent` ([Request-Response Format](https://github.com/mishushakov/dialogflow-gateway-docs#detecting-intents))
