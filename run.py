from app.infrastructure.flask_setup import create_app
from app import db
from flak_migrate import Migrate

app = create_app()

migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)