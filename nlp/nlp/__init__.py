from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_route('home', '/') # to get input from the user
    config.add_route('content', '/content') # to display the output from the model
    config.scan()
    return config.make_wsgi_app()
