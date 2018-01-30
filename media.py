import webbrowser


class Movie():
    """ This class stores information about each movie, including
    movie title, poster image, and a link to the trailer.
    """

    def __init__(self, movie_title, poster_image, trailer_youtube):
        """ Initializes Movie class with required information,
        including title, poster image url, and trailer url. """
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ This function shows the movie trailer in a web browser. """
        webbrowser.open(self.trailer_youtube_url)
