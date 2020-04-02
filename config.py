import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'gsolvit'

    @staticmethod
    def init_app(app):
        pass

config = {
    'default': Config,
    'USER': 'reader',
    'PASSWORD': 'reader',
    'DATABASE_NAME': 'studentTrainPlan'
}
