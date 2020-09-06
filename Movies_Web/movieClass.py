import webbrowser
class Movie:
    '''Provides storage for Movie ralated items'''
    def __init__(self,movie_name,movie_plot,movie_poster,movie_trailer_url):
        self.movie_name = movie_name
        self.movie_plot = movie_plot
        self.movie_poster = movie_poster
        self.movie_trailer_url = movie_trailer_url