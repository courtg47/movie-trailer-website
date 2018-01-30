import media
import fresh_tomatoes

""" Below contains all movies that will be displayed on our Movie Trailer
web page with all needed information including title, url to the
movie poster, and a link to the movie trailer.
"""

apollo_13 = media.Movie("Apollo 13",
                        "https://static.rogerebert.com/uploads/movie/"
                        "movie_poster/apollo-13-1995/"
                        "large_iQa98vAzqHaM115SldO9mGQ2Yx.jpg",
                        "https://www.youtube.com/watch?v=nEl0NsYn1fU")

the_right_stuff = media.Movie("The Right Stuff",
                              "https://resizing.flixster.com/"
                              "3hbYejSUmKr1pLw2AAUq41KJbOk=/"
                              "206x305/v1.bTsxMTIwNDc3Mjtq"
                              "OzE3NjM0OzEyMDA7MTIwMDsxNjAw",
                              "https://www.youtube.com/watch?v=d_RvMbcdS1Q")

the_martian = media.Movie("The Martian",
                          "https://images-na.ssl-images-amazon.com/"
                          "images/I/A1dlLt5G-nL._SL1500_.jpg",
                          "https://www.youtube.com/watch?v=ej3ioOneTy8")

gravity = media.Movie("Gravity",
                      "https://upload.wikimedia.org/"
                      "wikipedia/en/f/f6/Gravity_Poster.jpg",
                      "https://www.youtube.com/watch?v=VlhJm_KkKEg")

interstellar = media.Movie("Interstellar",
                           "https://upload.wikimedia.org/"
                           "wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=8EdxTFS3fD0")

star_wars = media.Movie("Star Wars: The Force Awakens",
                        "https://images-na.ssl-images-amazon.com/"
                        "images/I/814X0lSCJQL._SL1412_.jpg",
                        "https://www.youtube.com/watch?v=sGbxmsDFVnE")


movies = [apollo_13, the_right_stuff, the_martian, gravity,
          interstellar, star_wars]

# opens a webbrowser and displays information about the movies above.
fresh_tomatoes.open_movies_page(movies)
