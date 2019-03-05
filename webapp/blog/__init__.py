def create_modeule(app, **kwargs):
    from .controllers import blog_blueprint
    app.register_blueprint(blog_blueprint)