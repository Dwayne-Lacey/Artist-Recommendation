class TreeNode:
    def __init__(self, genre=None, artist=None, ranking=None, albums=None):
        self.genre = genre
        self.artist = artist
        self.ranking = ranking
        self.albums = albums
        self.children = {}
    
    def add_genre_node(self, genre):
        if genre in self.children.keys():
            print(f"The genre '{genre}' is already stored in the tree.")
        else:
            self.children[genre] = TreeNode(genre)
    
    def add_artist_node(self, genre, artist, ranking, albums):
        if genre not in self.children.keys():
            self.add_genre_node(genre)
        current_genre = self.children[genre]
        if artist not in current_genre.children.keys():
            current_genre.children[artist] = TreeNode(genre, artist, ranking, albums)
        else:
            print(f"The artist '{artist}' is already stored in the tree.")


    def print_children_keys(self):
        for key in self.children.keys():
            print(key)




music_tree = TreeNode()
music_tree.add_genre_node("Rock")
music_tree.add_genre_node("Rock")
music_tree.add_genre_node("Rap")
music_tree.add_genre_node("Metal")
music_tree.add_genre_node("Country")
music_tree.add_genre_node("Rap")
print("\n")

music_tree.add_artist_node("Rock", "Linkin Park", "35/100", "4")
music_tree.add_artist_node("Rock", "Five Finger Death Punch", "20/100", "6")
music_tree.add_artist_node("Rock", "Bring Me The Horizon", "1/100", "8")

for artist in music_tree.children["Rock"].children.values():
    print(f"""
--------------------------------------
    Genre: {artist.genre}
    Artist: {artist.artist}
    Billboard Ranking: {artist.ranking}
    # of Albums: {artist.albums}
--------------------------------------
    """)
