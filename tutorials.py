#intialize list
favorite_movies =[]

#add movies to list
print('enter your favorite 5 movies:')
for i in range(5):
    movie = input()
    favorite_movies.append(movie)

#show list
print('your favorite movies are:')
for movie in favorite_movies:
    print(movie)

#remove movie
del_movie = input('which movie do you want to remove?')
favorite_movies.remove(del_movie)
if del_movie in favorite_movies:
     print(f"{del_movie} has been removed from your list")
else:
    print(f"{del_movie} is not in your list")