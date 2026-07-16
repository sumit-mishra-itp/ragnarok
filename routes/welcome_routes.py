from flask import Blueprint, jsonify

welcome_bp = Blueprint('welcome', __name__)

@welcome_bp.route('/', methods=['GET'])
def welcome():
    """Return welcome message.
    
    Returns:
        str: Welcome message 'Hello Neurostack User'
        HTTP Status: 200 OK
    """
    return 'Hello Neurostack User', 200

@welcome_bp.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint for monitoring.
    
    Returns:
        JSON: Status object
        HTTP Status: 200 OK
    """
    return jsonify({'status': 'healthy', 'service': 'ragnarok'}), 200