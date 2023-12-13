from flask import Flask, render_template, jsonify, abort, request, Request
from common.auth_checks import is_valid_token, is_administrator, is_moderator, is_planet_owner, is_fleet_owner, is_alliance_owner
from common.enums import Badges
import common.routes.alliance.alliance as alliance_alliance
import common.routes.alliance.create   as alliance_create
import common.routes.alliance.disband  as alliance_disband
import common.routes.alliance.join     as alliance_join
import common.routes.alliance.leave    as alliance_leave
import common.routes.alliance.modify   as alliance_modify
import common.routes.fleet.fleet       as fleet_fleet
import common.routes.fleet.move        as fleet_move
import common.routes.fleet.recall      as fleet_recall
import common.routes.galaxy.galaxy     as galaxy_galaxy
import common.routes.planet.planet     as planet_planet
import common.routes.planet.building   as planet_building
import common.routes.planet.defenses   as planet_defenses
import common.routes.planet.shipyard   as planet_shipyard
import common.routes.planet.spy        as planet_spy
import common.routes.user.activity     as user_activity
import common.routes.user.technology   as user_technology
import common.routes.user.register     as user_register
import common.routes.user.login        as user_login

app = Flask(
    import_name=__name__,
    static_folder="../static",
    template_folder="../templates"
)
def start_app() -> Flask:
    return app

class RequestData():
    def __init__(self, request_data: dict) -> None:
        self.data = request_data
    
    def get_data(self, name: str | list[str]) -> object | list[object] | None:
        if isinstance(name, list):
            list_of_data = []
            for entry in name:
                data = self.get_data(entry)
                list_of_data.append(data)
            return list_of_data
        if name in self.data.keys():
            return self.data[name]
        return None


############
### GAME ###
############
@app.route("/")
def page_index():
    return render_template("index.htm"), 200

@app.route("/planet/overview")
def page_planet_overview():
    return render_template("planet_overview.htm"), 200

@app.route("/planet/buildings")
def page_planet_buildings():
    return render_template("planet_buildings.htm"), 200

@app.route("/planet/defense")
def page_planet_defense():
    return render_template("planet_defense.htm"), 200

@app.route("/planet/shipyard")
def page_planet_shipyard():
    return render_template("planet_shipyard.htm"), 200

@app.route("/planet/fleet")
def page_planet_fleet():
    return render_template("planet_fleet.htm"), 200

@app.route("/technology")
def page_technology():
    return render_template("technology.htm"), 200

@app.route("/galaxy")
def page_galaxy():
    return render_template("galaxy.htm"), 200

@app.route("/alliance")
def page_alliance():
    return render_template("alliance.htm"), 200

@app.route("/chat")
def page_chat():
    return render_template("chat.htm"), 200


###########
### API ###
###########
@app.route("/api/admin", methods=["POST"])
def api_admin():
    data = RequestData(request.get_json())
    auth_token = request.headers.get("Authorization")

    if not (is_valid_token(auth_token))                             : return abort(401)
    if not (is_administrator(auth_token))                           : return abort(403)
    
    return abort(501)

@app.route("/api/alliance", methods=["GET"])
def api_alliance():
    data = RequestData(request.get_json())
    auth_token = request.headers.get("Authorization")
    alliance_id = data.get_data("allianceID")

    if alliance_id is None                                          : return abort(400)

    return alliance_alliance.main()

@app.route("/api/alliance/create", methods=["POST"])
def api_alliance_create():
    data = RequestData(request.get_json())
    auth_token = request.headers.get("Authorization")

    if not (is_valid_token(auth_token))                             : return abort(401)
    
    return alliance_create.main()

@app.route("/api/alliance/modify", methods=["POST"])
def api_alliance_modify():
    data = RequestData(request.get_json())
    auth_token = request.headers.get("Authorization")
    alliance_id = data.get_data("allianceID")

    if alliance_id is None                                          : return abort(400)
    if not (is_valid_token(auth_token))                             : return abort(401)
    if not (is_alliance_owner(auth_token, alliance_id))             : return abort(403)

    return alliance_modify.main()

@app.route("/api/alliance/disband", methods=["DELETE"])
def api_alliance_disband():
    data = RequestData(request.get_json())
    auth_token = request.headers.get("Authorization")
    alliance_id = data.get_data("allianceID")

    if alliance_id is None                                          : return abort(400)
    if not (is_valid_token(auth_token))                             : return abort(401)
    if not (is_alliance_owner(auth_token, alliance_id))             : return abort(403)

    return alliance_disband.main()

@app.route("/api/alliance/join", methods=["POST"])
def api_alliance_join():
    data = RequestData(request.get_json())
    auth_token = request.headers.get("Authorization")
    alliance_id = data.get_data("allianceID")

    if alliance_id is None                                          : return abort(400)
    if not (is_valid_token(auth_token))                             : return abort(401)

    return alliance_join.main()

@app.route("/api/alliance/leave", methods=["POST"])
def api_alliance_leave():
    data = RequestData(request.get_json())
    auth_token = request.headers.get("Authorization")
    alliance_id = data.get_data("allianceID")

    if alliance_id is None                                          : return abort(400)
    if not (is_valid_token(auth_token))                             : return abort(401)

    return alliance_leave.main()

@app.route("/api/coffee", methods=["GET"])
def api_coffee():
    if True                                                         : return abort(418)

@app.route("/api/fleet", methods=["GET"])
def api_fleet():
    data = RequestData(request.get_json())
    auth_token = request.headers.get("Authorization")
    fleet_id = data.get_data("fleetID")

    if fleet_id is None                                             : return abort(400)
    if not (is_valid_token(auth_token))                             : return abort(401)
    if not (is_fleet_owner(auth_token, fleet_id))                   : return abort(403)

    return fleet_fleet.main()

@app.route("/api/fleet/move", methods=["POST"])
def api_fleet_move():
    data = RequestData(request.get_json())
    auth_token = request.headers.get("Authorization")
    fleet_id = data.get_data("fleetID")

    if fleet_id is None                                             : return abort(400)
    if not (is_valid_token(auth_token))                             : return abort(401)
    if not (is_fleet_owner(auth_token, fleet_id))                   : return abort(403)

    return fleet_move.main()

@app.route("/api/fleet/recall", methods=["POST"])
def api_fleet_recall():
    data = RequestData(request.get_json())
    auth_token = request.headers.get("Authorization")
    fleet_id = data.get_data("fleetID")

    if fleet_id is None                                             : return abort(400)
    if not (is_valid_token(auth_token))                             : return abort(401)
    if not (is_fleet_owner(auth_token, fleet_id))                   : return abort(403)

    return fleet_recall.main()

@app.route("/api/galaxy", methods=["GET"])
def api_galaxy():
    auth_token = request.headers.get("Authorization")

    if not (is_valid_token(auth_token))                             : return abort(401)

    return galaxy_galaxy.main()

@app.route("/api/planet", methods=["GET"])
def api_planet():
    auth_token = request.headers.get("Authorization")
    planet_id = request.args.get("planet") if not request.args.get("planet") == 'null' else None

    if planet_id is None                                            : return "Parameter 'planet_id' must not be 'None'.", 400
    if not (is_valid_token(auth_token))                             : return abort(401)
    if not (is_planet_owner(auth_token, planet_id))                 : return abort(403)

    return planet_planet.main(int(planet_id))

@app.route("/api/planet/building", methods=["POST"])
def api_planet_building():
    data = RequestData(request.get_json())
    auth_token = request.headers.get("Authorization")
    planet_id = data.get_data("planetID")
    building_type = data.get_data("building")

    if not (isinstance(planet_id, int))                             : return "Parameter 'planet_id' must be 'int'.", 400
    if not (isinstance(building_type, int))                         : return "Parameter 'building_type' must be 'int'.", 400
    if not (is_valid_token(auth_token))                             : return abort(401)
    if not (is_planet_owner(auth_token, planet_id))                 : return abort(403)

    return planet_building.main(planet_id, building_type)

@app.route("/api/planet/defenses", methods=["POST"])
def api_planet_defenses():
    data = RequestData(request.get_json())
    auth_token = request.headers.get("Authorization")
    planet_id = data.get_data("planetID")
    defense_type = data.get_data("defense")
    defense_amount = data.get_data("amount")

    if not (isinstance(planet_id, int))                             : return "Parameter 'planet_id' must be 'int'.", 400
    if not (isinstance(defense_type, int))                          : return "Parameter 'defense' must be 'int'.", 400
    if not (isinstance(defense_amount, int))                        : return "Parameter 'amount' must be 'int'.", 400
    if not (is_valid_token(auth_token))                             : return abort(401)
    if not (is_planet_owner(auth_token, planet_id))                 : return abort(403)

    return planet_defenses.main(planet_id, defense_type, defense_amount)

@app.route("/api/planet/shipyard", methods=["POST"])
def api_planet_shipyard():
    data = RequestData(request.get_json())
    auth_token = request.headers.get("Authorization")
    planet_id = data.get_data("planetID")
    ship_type = data.get_data("ship")
    ship_amount = data.get_data("amount")

    if not (isinstance(planet_id, int))                             : return "Parameter 'planet_id' must be 'int'.", 400
    if not (isinstance(ship_type, int))                             : return "Parameter 'ship' must be 'int'.", 400
    if not (isinstance(ship_amount, int))                           : return "Parameter 'amount' must be 'int'.", 400
    if not (is_valid_token(auth_token))                             : return abort(401)
    if not (is_planet_owner(auth_token, planet_id))                 : return abort(403)

    return planet_shipyard.main(planet_id, ship_type, ship_amount)

@app.route("/api/planet/spy", methods=["POST"])
def api_planet():
    data = RequestData(request.get_json())
    auth_token = request.headers.get("Authorization")
    planet_id = data.get_data("planetID")

    if planet_id is None                                            : return abort(400)
    if not (is_valid_token(auth_token))                             : return abort(401)
    if not (is_planet_owner(auth_token, planet_id))                 : return abort(403)

    return planet_spy.main()

@app.route("/api/user/technology", methods=["POST"])
def api_user_technology():
    data = RequestData(request.get_json())
    auth_token = request.headers.get("Authorization")
    user_id = data.get_data("userID")

    if user_id is None                                              : return abort(400)
    if not (is_valid_token(auth_token))                             : return abort(401)

    return user_technology.main()

@app.route("/api/user/activity", methods=["POST"])
def api_user_activity():
    data = RequestData(request.get_json())
    auth_token = request.headers.get("Authorization")
    user_id = data.get_data("userID")

    if user_id is None                                              : return abort(400)
    if not (is_valid_token(auth_token))                             : return abort(401)

    return user_activity.main()

@app.route("/api/user/register", methods=["POST"])
def api_user_register():
    data = RequestData(request.get_json())
    username = data.get_data("username")
    password = data.get_data("password")

    if username is None                                             : return abort(400)
    if password is None                                             : return abort(400)

    return user_register.main(username, password)

@app.route("/api/user/login", methods=["POST"])
def api_user_login():
    data = RequestData(request.get_json())
    username = data.get_data("username")
    password = data.get_data("password")

    if username is None                                             : return abort(400)
    if password is None                                             : return abort(400)

    return user_login.main(username, password)


#######################
### ERROR HANDELING ###
#######################
@app.errorhandler(401)
def page_401(error):
    return render_template("error.htm", error_code = 401, error_name="Unauthorized", error_message="We do not have authorization to access this page."), 401

@app.errorhandler(403)
def page_403(error):
    return render_template("error.htm", error_code = 403, error_name="Forbidden", error_message="We do not have the necessary permissions to access this page."), 403

@app.errorhandler(404)
def page_404(error):
    return render_template("error.htm", error_code = 404, error_name="Not Found", error_message="We could not find the requested page."), 404