from ArtistData import artist_data
class TreeNode:
    def __init__(self, genre=None, artist=None, ranking=None, song=None, albums=None):
        self.genre = genre
        self.artist = artist
        self.ranking = ranking
        self.song = song
        self.albums = albums
        self.children = {}
    
    def add_genre_node(self, genre):
        if genre in self.children.keys():
            print(f"The genre '{genre}' is already stored in the tree.")
        else:
            self.children[genre] = TreeNode(genre)
    
    def add_artist_node(self, genre, artist, ranking, song, albums):
        if genre not in self.children.keys():
            self.add_genre_node(genre)
        current_genre = self.children[genre]
        if artist not in current_genre.children.keys():
            current_genre.children[artist] = TreeNode(genre, artist, ranking, song, albums)
        else:
            print(f"The artist '{artist}' is already stored in the tree.")


    def print_children_keys(self):
        for key in self.children.keys():
            print(key)

    def store_data_set(self, data_set):
        for data in data_set:
            self.add_artist_node(data[0], data[1], data[2], data[3], data[4])


music_tree = TreeNode()




music_tree.store_data_set(artist_data)

for artist in music_tree.children["Rap"].children.values():
    print(f"""
--------------------------------------
    Genre: {artist.genre}
    Artist: {artist.artist}
    Billboard Ranking: {artist.ranking}/100
    Top Song: {artist.song}
    # of Albums: {artist.albums}
--------------------------------------
    """)
