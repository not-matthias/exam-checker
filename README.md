# exam-checker
Checks whether you can sign up for the Operating Systems exam.


## How to run

Copy and set the environment variables:
```
cp example.env .env
```

With Python:
```
pip3 install -r requirements.txt
python3 main.py
```

With Docker:
```
docker build -t exam-checker .
docker run -it exam-checker
```

## Configuration

- **KUSS Session**: Can be extracted with any browser. 
- **Discord Webhook:** Sends notifications using the webhook.
