__author__ = 'Gadfly4ever'

import webbrowser

# The class to store movie data


class Movie():

    def __init__(self, title, description, director, release, poster_image_url, trailer_youtube_url):
        """
        The constructor for the class Movie()
        """
        self.title = title
        self.description = description
        self.director = director
        self.release_year = release
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """
        shows the movie trailer of which the link is passed to it
        """
        webbrowser.open(self.trailer_link)

