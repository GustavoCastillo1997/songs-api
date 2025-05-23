from .song_routes import song_bp
from .composer_routes import composer_bp
from .country_routes import country_bp
from .music_style_routes import music_style_bp
from .service_routes import service_bp

# Lista com todos os blueprints
all_blueprints = [
    song_bp,
    composer_bp,
    country_bp,
    music_style_bp,
    service_bp
]
