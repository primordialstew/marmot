def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('foo', '/foo')
    config.add_route('cities', '/cities')
    config.add_route('city', '/cities/{name}')
