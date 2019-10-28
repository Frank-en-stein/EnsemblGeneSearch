from flask import Flask, abort
from flask_mysqldb import MySQL
from constants import environment as envConst
from utils import mysqlUtils
from routes import api
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
app.config['MYSQL_HOST'] = envConst.ensembldb_host
app.config['MYSQL_PORT'] = envConst.ensembldb_port
app.config['MYSQL_USER'] = envConst.ensembldb_user
app.config['MYSQL_PASSWORD'] = envConst.ensembldb_password
app.config['MYSQL_DB'] = envConst.ensembldb_db_name

### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###

cache = None
mysql = MySQL(app)

app.register_blueprint(api.get_blueprint(mysql, cache))

if __name__ == "__main__":
    app.run(debug=True)
