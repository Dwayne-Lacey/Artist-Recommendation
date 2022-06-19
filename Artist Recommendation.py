import random
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
    
    def quicksort(self, data_list, start, end):
        if start >= end:
            return
        #select random element to be pivot
        pivot_idx = random.randrange(start, end + 1)
        pivot_element = data_list[pivot_idx]
        # swap random element with last element in sub-lists
        data_list[end], data_list[pivot_idx] = data_list[pivot_idx], data_list[end]
        
        # tracks all elements which should be to left (lesser than) pivot
        less_than_pointer = start

        for i in range(start, end):
            # we found an element out of place
            if data_list[i] < pivot_element:
                # swap element to the right-most portion of lesser elements
                data_list[i], data_list[less_than_pointer] = data_list[less_than_pointer], data_list[i]
                # tally that we have one more lesser element
                less_than_pointer += 1
        # move pivot element to the right-most portion of lesser elements        
        data_list[end], data_list[less_than_pointer] = data_list[less_than_pointer], data_list[end]
        # recursively sort left and right sub-lists
        self.quicksort(data_list, start, less_than_pointer - 1)
        self.quicksort(data_list, less_than_pointer + 1, end)



        


music_tree = TreeNode()




music_tree.store_data_set(artist_data)
sort_list = list(music_tree.children.keys())
print(sort_list)
music_tree.quicksort(sort_list, 0, len(sort_list) - 1)
print(sort_list)


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

