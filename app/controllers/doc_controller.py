from flask import render_template, Blueprint


class DocumentationControoler(object):
    
    documentation_controller = Blueprint('documentation_controller', __name__)
    
    @documentation_controller.route('/docs', methods=['GET'])
    def index():
        return render_template('documentation.html')