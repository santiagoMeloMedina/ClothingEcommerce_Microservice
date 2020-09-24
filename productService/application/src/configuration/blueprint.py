
from configuration.handler import app
import controller.product as PC
import controller.category as CC
import controller.characteristic as CCH

app.register_blueprint(PC.controller)
app.register_blueprint(CC.controller)
app.register_blueprint(CCH.controller)