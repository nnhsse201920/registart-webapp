from app import app, db
from app.models import *

@app.shell_context_processor
def make_shell_context():
    return {'db': db,
            'Organizers': Organizers, 
            'Assignments': Assignments,
            'Students': Students, 
            'Organizations': Organizations,
            'Activity': Activity,
            'Connection' : Connection}