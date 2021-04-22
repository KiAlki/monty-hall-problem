from flask import Flask, request

from app.game import run_multiple_rounds, SWITCH_OPTION_KEEP, SWITCH_OPTION_CHANGE

ERROR_MESSAGE = "Request body must contains choose_option and attempts. " \
                "choose_option should be equal keep or change"


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev",
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    @app.route('/play', methods=['POST'])
    def play_game():
        json_data = request.get_json()
        if not validate_json(json_data):
            return {"error": ERROR_MESSAGE}, 400
        return run_multiple_rounds(**json_data)

    def validate_json(json) -> bool:
        if "choose_option" not in json.keys() or "attempts" not in json.keys():
            return False
        if json["choose_option"] not in [SWITCH_OPTION_KEEP, SWITCH_OPTION_CHANGE]:
            return False
        return True

    return app
