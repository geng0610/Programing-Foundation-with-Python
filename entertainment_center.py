import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", 
	"A story of a boy and his toys that come to life", 
	"http://www.impawards.com/1995/posters/toy_story_ver1.jpg",
	"https://youtu.be/KYz2wyBy3kc")

avatar = media.Movie("Avatar",
	"a marine on an alien planet",
	"http://www.impawards.com/2009/posters/avatar_ver5_xlg.jpg",
	"https://www.youtube.com/watch?v=cRdxXPV9GNQ")

avengers = media.Movie("Avengers",
	"super heroes fighting force of evil",
	"http://thecarnivoreproject.typepad.com/.a/6a00d8345295c269e201a3fcf6d061970b-800wi",
	"https://www.youtube.com/watch?v=MZoO8QVMxkk")

#print (avengers.storyline)
#avengers.show_trailer()

ratatouille = media.Movie("Ratatouille",
	"a mouse becomes a chef",
	"http://www.pixartalk.com/wp-content/uploads/2009/06/ratus1.jpg",
	"https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
	"romatic chick flick in paris",
	"http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
	"https://www.youtube.com/watch?v=BYRWfS2s2v4")

hunger_games = media.Movie("Hunger Games",
	"poor people fighting each other",
	"http://www.usmagazine.com/uploads/assets/articles/48687-see-the-brand-new-hunger-games-movie-poster/1327101273_hunger-games-poster_1.jpg",
	"https://www.youtube.com/watch?v=4S9a5V9ODuY")

movies = [toy_story, avatar, avengers, ratatouille, midnight_in_paris, hunger_games]

fresh_tomatoes.open_movies_page(movies)
#print (media.Movie.VALID_RATINGS)

#print (media.Movie.__name__)
#print (media.Movie.__module__)