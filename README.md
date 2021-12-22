# Websocket testing Stream
It's simple implementation of webcam streaming in browser using websocket.

# How to use
* run `FLASK_APP=wsdemo.py flask run --host 0.0.0.0`
* run `python3 ws-server.py`
* first open `http://localhost:5000`
* second open `http://localhost:5000/send` and allow webcam stream

have fun

# TODO
* need fix recover of streaming
* need fix new connection receiv stream
