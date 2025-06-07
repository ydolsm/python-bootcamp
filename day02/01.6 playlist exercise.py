def add(song, playlist):
	"""Add song to playlist"""
	playlist.append(song)
	print(playlist)

def remove(song, playlist):
	"""Remove song from playlist"""
	playlist.remove(song)
	print(playlist)

def play(playlist):
	"""Print the first song in the playlist (if any) and remove"""
	print(playlist[0])
	song_played = playlist.pop(0)
	#print(song_played)

def show_all(playlist):
	"""Print all contents in the playlist"""
	print(playlist)


def playlist_app():
	playlist = []
	finish = False
	valid_action = ["add","remove","play","show all","exit",]

	while not finish:
			user_choice = input("Input action: ")
			if user_choice not in valid_action:
				print("Enter a valid action: add, remove, play, show all, exit")
			elif user_choice == "add":
				song = input("Input song name to add: ")
				add(song, playlist)

			elif user_choice == "remove":
				song = input("Input song name to remove: ")
				if song not in playlist:
					print("Song not found!")
				else:
					remove(song, playlist)
			elif user_choice == "play":
				play(playlist)
			elif user_choice == "show all":
				show_all(playlist)
			elif user_choice == "exit":
				finish = True

playlist_app()