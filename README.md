# exam-checker
Checks whether you can sign up for the Operating Systems exam.


## How to run

### Docker (recommended)

Build and run:
```
docker build -t exam-checker .
docker run -it -e KUSS_SESSION=_shibsession_TODO -e KUSS_CREDENTIALS=TODO exam-checker
```

### Locally

Copy and set the environment variables:
```
cp example.env .env
```

Install dependencies and run it:
```
pip3 install -r requirements.txt
python3 main.py
```

## Configuration

- **KUSS Session**: Can be extracted with any browser. 
- **Discord Webhook:** Sends notifications using the webhook.
