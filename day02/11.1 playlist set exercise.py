your_playlist = {
    "All I Want for Christmas is You",
    "Silent Night, Holy Night",
    "Star ng Pasko",
    "Pasko na Sinta Ko",
}

friend_playlist = {
    "Baby, It's Cold Outside",
    "All I Want for Christmas is You",
    "Kampana ng Simbahan",
    "Christmas Bonus",
}

#to combine sets
print(your_playlist.union(friend_playlist))
print(your_playlist | friend_playlist)

#to extract the same values from the sets
print(your_playlist.intersection(friend_playlist))
print(your_playlist & friend_playlist)

#gets all values that are unique in the set defined (order of set matters)
print(your_playlist.difference(friend_playlist))

#all unique values that do not have a duplicate
print(your_playlist.symmetric_difference(friend_playlist))