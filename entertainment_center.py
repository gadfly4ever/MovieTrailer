__author__ = 'Gadfly4ever'

import media
import fresh_tomatoes

# The movie data bank

memento = media.Movie("Memento", "After his wife is killed, he loses his short term memory ...", "Christopher Nolan",
                      "2000", "http://www.impawards.com/2001/posters/memento.jpg", "https://youtu.be/UFuFFdK7i44")

inception = media.Movie("Inception", "It all starts with a dream ... or a reality?! ...", "Christopher Nolan", "2010",
                        "http://www.impawards.com/2010/posters/inception_ver3_xlg.jpg", "https://youtu.be/8hP9D6kZseM")

in_the_mood_for_love = media.Movie("In the Mood for Love", "Partners of two neighbors cheat on them, together.",
                                   "Kar-Wai Wong", "2000",
                                   "http://andantemoderato.com/wp-content/uploads/2014/12/In-The-Mood-For-Love-poster."
                                   "jpg", "https://youtu.be/BnFjSHQFVkA")

happy_together = media.Movie("Happy Together", "A gay couple break up and get together repeatedly.", "Kar-Wai Wong",
                             "1997",
                             "http://images.moviepostershop.com/happy-together-movie-poster-1996-1020200742.jpg",
                             "https://youtu.be/cMx0UgohOfE")

_2046 = media.Movie("2046", "A writer goes to a hotel and works on his latest work: Planet 2046.", "Kar-Wai Wong",
                    "2004", "http://movieposters.2038.net/p/2046.jpg", "https://youtu.be/vfNe3zFT9rk")

shawshank_redemption = media.Movie("Shawshank Redemption", "An innocent prisoner tries to get free.", "Frank Darabont",
                                   "1994",
                                   "http://cdn.gowatchit.com/posters/original/TheShawshankRedemption-PosterArt.jpg",
                                   "https://youtu.be/NmzuHjWmXOc")

mommy = media.Movie("Mommy", "A problematic adolescent and his mom. What happens next?", "Xavier Dolan", "2014",
                    "http://4.bp.blogspot.com/-F7q7mRm6f2U/U8gDSBqB0MI/AAAAAAAALgk/ksr9EyJgxZM/s1600/MOMMY_Poster_27x39"
                    "_ANG_LR.jpg", "https://youtu.be/Q9LVLCYvqSI")

boyhood = media.Movie("Boyhood", "A 6 year old becomes 18 years old in a 12 year movie time span.", "Richard Linklater",
                      "2014", "http://a5.mzstatic.com/us/r30/Music4/v4/93/bb/48/93bb480e-2bcf-3ef1-23fe-957576bd5840/"
                      "cover326x326.jpeg", "https://youtu.be/Ys-mbHXyWX4")

gloomy_sunday = media.Movie("Gloomy Sunday", "3 Men in love with one woman. The woman only in love with two of them.",
                            "Rolf Schuebel", "1999",
                            "http://images.moviepostershop.com/gloomy-sunday-movie-poster-1999-1020474405.jpg",
                            "https://youtu.be/x6ZRALrrI3s")

godfather = media.Movie("The Godfather", "Italian Mafia and the mysteries of it.", "Francis Ford Coppola", "1972",
                        "http://fontmeme.com/images/The-Godfather-Poster.jpg", "https://youtu.be/YBrs0wvkPls")


fight_club = media.Movie("Fight Club", "Two people start a fight club. Are they really two?", "David Fincher", "1999",
                         "http://www.powerfmsa.com.au/images/fight-club-movie-poster-1020270798.jpg",
                         "https://youtu.be/D3Yw9Yc1YmY")

seven = media.Movie("SE7EN", "The seven capital vices, a detective and his assistant ...", "David Fincher", "1995",
                    "http://www.impawards.com/1995/posters/seven_ver1.jpg", "https://youtu.be/J4YV2_TcCoE")

matrix = media.Movie("Matrix", "Unfortunately nobody can be told what the matrix is.", "The Wachowski Brothers", "1999",
                     "https://www.movieposter.com/posters/archive/main/9/A70-4902", "https://youtu.be/vKQi3bBA1y8")


# List of movies
movies = [memento, inception, in_the_mood_for_love, happy_together, _2046, shawshank_redemption, mommy, boyhood,
          gloomy_sunday, godfather, fight_club, seven, matrix]

# Calling the web page showing the movie posters/trailers
fresh_tomatoes.open_movies_page(movies)