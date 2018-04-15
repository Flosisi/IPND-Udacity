import webbrowser

#Defining what are in the Parent class
class Video ():
    """This class provides a way to store video related information. There are two types of videos in it, which are movie and TV series."""

    def __init__ (self, title, release_year, casts, storyline, poster_image, trailer_youtube):
        """This function is to construct a database for a particular video containing it's own information."""
        self.title = title
        self.year = release_year
        self.casts = casts
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def showtrailer (self):
        """This function is to play a trailer video file of the selected video."""
        webbrowser.open(self.trailer_youtube_url)

#Defining what are in the Child classes
class Movie (Video):
    """This class provides a way to store movie related information. It is a sub-class of class Video."""
    def __init__ (self, title, release_year, casts, storyline, poster_image, trailer_youtube, movie_duration):
        """This function is to construct a database for a particular movie containing it's own information."""
        Video.__init__ (self, title, release_year, casts, storyline, poster_image, trailer_youtube)
        self.duration = movie_duration

class TV_Series (Video):
    """This class provides a way to store TV Series related information. It is a sub-class of class Video."""
    def __init__ (self, title, release_year, casts, storyline, poster_image, trailer_youtube, series_num_seasons, broadcast_status):
        """This function is to construct a database for a particular TV series containing it's own information."""
        Video.__init__ (self, title, release_year, casts, storyline, poster_image, trailer_youtube)
        self.seasons = series_num_seasons
        self.status = broadcast_status
