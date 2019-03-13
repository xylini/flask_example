from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def page_not_found(error):
    return render_template('404.html'), 404

def create_app(object_name):
    app = Flask(__name__)
    app.config.from_object(object_name)
    app.register_error_handler(404, page_not_found)

    db.init_app(app)
    migrate.init_app(app, db)

    from .auth import create_module as auth_create_module
    from.blog import create_modeule as blog_create_module
    from .main import create_module as main_create_module
    auth_create_module(app)
    blog_create_module(app)
    main_create_module(app)

    # from .blog.controllers import blog_blueprint
    # from .main.controllers import main_blueprint, GenericListView
    # from .blog.models import Post, User, Comment, Tag
    #
    # app.register_blueprint(main_blueprint)
    # app.register_blueprint(blog_blueprint)
    # app.register_error_handler(404, page_not_found)
    #
    # app.add_url_rule(
    #     '/generic_posts', view_func=GenericListView.as_view(
    #         'generic_posts', model=Post)
    # )
    #
    # app.add_url_rule(
    #     '/generic_users', view_func=GenericListView.as_view(
    #         'generic_users', model=User)
    # )
    #
    # app.add_url_rule(
    #     '/generic_comments', view_func=GenericListView.as_view(
    #         'generic_comments', model=Comment)
    # )
    #
    # app.add_url_rule(
    #     '/generic_tags', view_func=GenericListView.as_view(
    #         'generic_tags', model=Tag)
    # )

    return app
