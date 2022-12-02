# DDoS Simulator
This project simulates a DDoS on a mock server using Docker, Django, PostgreSQL, Redis, and Nginx.

## Setup
The project uses the following:
- Python
- Django
- PostgreSQL 
- Redis 
- Nginx 
- 
## Building

To build, run ```docker-compose build```

## Running
To run the web API, run ```docker-compose up -d```, then go to 
http://localhost/api/core/data using your web browser. You should 
see a list of data. Initially, it will be empty.

## Simulating a DDoS Attack

Then, in your virtual environment, run ```pip install -r requirements.txt```
to install the depedencies needed for the DDoS script. After that, you can
run a DDoS attack using ```python ddos_attack.py```.
