import os
from webapp import create_app


# @app.before_request
# def before_request():
#     session['page_loads'] = session.get('page_loads', 0) + 1
#     g.random_key = random.randrange(1, 10)
#     # print(session['page_loads'])
#     # print(g.random_key)
#
#
#
#
#


env = os.environ.get('WEBAPP_ENV', 'dev')
app = create_app('config.%sConfig' % env.capitalize())


if __name__ == '__main__':
    app.run()
