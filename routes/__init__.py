from .songs import songs_bp
from .composers import composers_bp
from .countries import countries_bp
from .music_styles import music_styles_bp
from .services import services_bp

# Lista com todos os blueprints
all_blueprints = [
    songs_bp,
    composers_bp,
    countries_bp,
    music_styles_bp,
    services_bp
]
