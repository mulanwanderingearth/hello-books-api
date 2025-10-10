from app import create_app
import os

app = create_app()

if __name__ == '__main__':
    # Use debug=True for development; in production use a proper WSGI server
    host = os.environ.get('HOST', '127.0.0.1')
    port = int(os.environ.get('PORT', '5000'))
    debug = os.environ.get('FLASK_DEBUG', '1') in ('1', 'true', 'True')
    app.run(host=host, port=port, debug=debug)
