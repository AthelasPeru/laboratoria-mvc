import os
from app import create_app

if __name__ == '__main__':
	app = create_app()
	# codepicnic enviroment
	if os.environ.get("BASKET_APP_PORT", False):
		app.run(debug=True, port=8080, host="0.0.0.0")
	# localhost
	app.run(debug=True, port=5000)
