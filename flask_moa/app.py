from flask import Flask
from flask_restful import Api
from views import JobCreateViews, JobRUDViews, JobTaskViews



def __set_app():
    app = Flask(__name__)
    api = Api(app)

    return app, api


def __set_uris(api):
    api.add_resource(JobRUDViews, '/api/jobs/<int:job_id>')
    api.add_resource(JobCreateViews, '/api/jobs')
    api.add_resource(JobTaskViews, '/api/jobs/<int:job_id>/run')


def get_app():
    # Set app
    app, api = __set_app()
    __set_uris(api)

    return app, api


def main():
    app, api = get_app()
    app.run(debug=True)


if __name__ == '__main__':
    main()