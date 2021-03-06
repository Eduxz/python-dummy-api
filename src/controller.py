from flask import Flask,request,jsonify
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/v1/api', methods=['POST'])
def postSomeThing():
    content = request.json
    name = content['name']
    logger.info('name: %s',name)
    return "Hello %s" %name

@app.route("/")
def hello():
    return "Hello Banana!"

if __name__ == '__main__':
  app.run(port=int(os.getenv('PORT', 5000)),use_reloader=False)
    
