## Dialogflow Gateway
A simple python-based open source implementation of dialogflow-gateway HTTP API for Dialogflow Web UI.

### Requirements
- Python>=3.7
- `pip install -r requirements.txt`
- Setup the credentials in `main.py`

### HTTP Endpoints

- To retrieve agent details: `/get_dialogflow_agent` ([Request-Response Format](https://github.com/mishushakov/dialogflow-gateway-docs#retrieving-agents))
- To get Dialogflow response for a query: `/detect_intent` ([Request-Response Format](https://github.com/mishushakov/dialogflow-gateway-docs#detecting-intents))
