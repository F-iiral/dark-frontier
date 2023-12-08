from flask import Flask, render_template, jsonify, abort, request
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

############
### GAME ###
############
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
    data = request.get_json()
    auth_token = request.headers.get("Authorization")

    if not (is_valid_token(auth_token))                             : return abort(401)
    if not (is_administrator(auth_token))                           : return abort(403)
    
    return abort(501)

@app.route("/api/alliance", methods=["GET"])
def api_alliance():
    data = request.get_json()
    alliance_id = data["allianceID"]

    return alliance_alliance.main()

@app.route("/api/alliance/create", methods=["POST"])
def api_alliance_create():
    data = request.get_json()
    alliance_id = data["allianceID"]

    if not (is_valid_token(request.headers.get("Authorization")))   : return abort(401)
    if not (is_alliance_owner(alliance_id))                         : return abort(403)
    
    return alliance_create.main()

@app.route("/api/alliance/modify", methods=["POST"])
def api_alliance_modify():
    data = request.get_json()
    alliance_id = data["allianceID"]

    if not (is_valid_token(request.headers.get("Authorization")))   : return abort(401)
    if not (is_alliance_owner(alliance_id))                         : return abort(403)

    return alliance_modify.main()

@app.route("/api/alliance/disband", methods=["DELETE"])
def api_alliance_disband():
    data = request.get_json()
    alliance_id = data["allianceID"]

    if not (is_valid_token(request.headers.get("Authorization")))   : return abort(401)
    if not (is_alliance_owner(alliance_id))                         : return abort(403)
    
    return alliance_disband.main()

@app.route("/api/alliance/join", methods=["POST"])
def api_alliance_join():
    data = request.get_json()
    alliance_id = data["allianceID"]

    if not (is_valid_token(request.headers.get("Authorization")))   : return abort(401)
    
    return alliance_join.main()

@app.route("/api/alliance/leave", methods=["POST"])
def api_alliance_leave():
    data = request.get_json()
    alliance_id = data["allianceID"]

    if not (is_valid_token(request.headers.get("Authorization")))   : return abort(401)
    
    return alliance_leave.main()

@app.route("/api/coffee", methods=["GET"])
def api_coffee():
    return abort(418)

@app.route("/api/fleet", methods=["GET"])
def api_fleet():
    data = request.get_json()
    fleet_id = data["fleetID"]

    if not (is_valid_token(request.headers.get("Authorization")))   : return abort(401)
    if not (is_fleet_owner(fleet_id))                               : return abort(403)
    
    return fleet_fleet.main()

@app.route("/api/fleet/move", methods=["POST"])
def api_fleet_move():
    data = request.get_json()
    fleet_id = data["fleetID"]

    if not (is_valid_token(request.headers.get("Authorization")))   : return abort(401)
    if not (is_fleet_owner(fleet_id))                               : return abort(403)
    
    return fleet_move.main()

@app.route("/api/fleet/recall", methods=["POST"])
def api_fleet_recall():
    data = request.get_json()
    fleet_id = data["fleetID"]

    if not (is_valid_token(request.headers.get("Authorization")))   : return abort(401)
    if not (is_fleet_owner(fleet_id))                               : return abort(403)
    
    return fleet_recall.main()

@app.route("/api/galaxy", methods=["GET"])
def api_galaxy():
    if not (is_valid_token(request.headers.get("Authorization")))   : return abort(401)
    
    return galaxy_galaxy.main()

@app.route("/api/planet", methods=["GET"])
def api_planet():
    data = request.get_json()
    planet_id = data["planetID"]

    if not (is_valid_token(request.headers.get("Authorization")))   : return abort(401)
    if not (is_planet_owner(planet_id))                             : return abort(403)

    return planet_planet.main()

@app.route("/api/planet/building", methods=["POST"])
def api_planet_building():
    data = request.get_json()
    planet_id = data["planetID"]

    if not (is_valid_token(request.headers.get("Authorization")))   : return abort(401)
    if not (is_planet_owner(planet_id))                             : return abort(403)
    
    return planet_building.main()

@app.route("/api/planet/defenses", methods=["POST"])
def api_planet_defenses():
    data = request.get_json()
    planet_id = data["planetID"]

    if not (is_valid_token(request.headers.get("Authorization")))   : return abort(401)
    if not (is_planet_owner(planet_id))                             : return abort(403)
    
    return planet_defenses.main()

@app.route("/api/planet/shipyard", methods=["POST"])
def api_planet_shipyard():
    data = request.get_json()
    planet_id = data["planetID"]

    if not (is_valid_token(request.headers.get("Authorization")))   : return abort(401)
    if not (is_planet_owner(planet_id))                             : return abort(403)
    
    return planet_shipyard.main()

@app.route("/api/user/technology", methods=["POST"])
def api_user_technology():
    data = request.get_json()
    user_id = data["userID"]

    if not (is_valid_token(request.headers.get("Authorization")))   : return abort(401)
    
    return user_technology.main()

@app.route("/api/user/activity", methods=["POST"])
def api_user_activity():
    data = request.get_json()
    user_id = data["userID"]

    if not (is_valid_token(request.headers.get("Authorization")))   : return abort(401)
    
    return user_activity.main()

@app.route("/api/user/register", methods=["POST"])
def api_user_register():
    data = request.get_json()
    username = data["username"]
    password = data["password"]

    return user_register.main(username, password)

@app.route("/api/user/login", methods=["POST"])
def api_user_login():
    data = request.get_json()
    username = data["username"]
    password = data["password"]

    return user_login.main(username, password)


#####################
### FUNCTIONALITY ###
#####################
@app.route("/")
def page_index():
    return render_template("index.htm"), 200

@app.errorhandler(401)
def page_401(error):
    return render_template("401.htm"), 401

@app.errorhandler(403)
def page_403(error):
    return render_template("403.htm"), 403

@app.errorhandler(404)
def page_404(error):
    return render_template("404.htm"), 404