from flask import Flask, abort
from constants import environment as envConst
from utils import mysqlUtils
from routes import api
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

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
mysql = mysqlUtils.connectDB(app,
                            envConst.ensembldb_host,
                            envConst.ensembldb_port,
                            envConst.ensembldb_user,
                            envConst.ensembldb_password,
                            envConst.ensembldb_db_name)

app.register_blueprint(api.get_blueprint(mysql, cache))

if __name__ == "__main__":
    app.run(debug=True)
