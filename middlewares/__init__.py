from middlewares.error_handler import ErrorHandler

def add_middlewares(app):
    app.add_middleware(ErrorHandler)