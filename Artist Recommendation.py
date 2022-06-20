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
    
    # Creates TreeNode for each unique genre within tree
    def add_genre_node(self, genre):
        if genre.lower() in self.children.keys():
            print(f"The genre '{genre}' is already stored in the tree.")
        else:
            self.children[genre.lower()] = TreeNode(genre)
    
    # Adds TreeNode for each artist, call to genre node function if genre doesn't already exist in tree
    def add_artist_node(self, genre, artist, ranking, song, albums):
        if genre.lower() not in self.children.keys():
            self.add_genre_node(genre)
        current_genre = self.children[genre.lower()]
        if artist not in current_genre.children.keys():
            current_genre.children[artist] = TreeNode(genre, artist, ranking, song, albums)
        else:
            print(f"The artist '{artist}' is already stored in the tree.")

    # Used to build each TreeNode for genres and artists
    def store_data_set(self, data_set):
        for data in data_set:
            self.add_artist_node(data[0], data[1], data[2], data[3], data[4])
    
    # Standard quicksort function to sort the list of keys for the children of each TreeNode
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
    
    # Modified instance of a binary search used to identify all matches for however many letters are passed to function by removing each match from the search list
    def modified_binary_search(self, search, data_list):
        keys_to_search = data_list.copy()
        target = search.lower()
        self.quicksort(keys_to_search, 0, len(keys_to_search) - 1)
        left_pointer = 0
        right_pointer = len(keys_to_search)
        results = []
        while right_pointer - left_pointer > 1:
            mid_idx = (left_pointer + right_pointer) // 2            
            current_value = keys_to_search[mid_idx]
            if current_value[0:len(search)] == target:
                results.append(keys_to_search.pop(mid_idx))
                right_pointer = len(keys_to_search)
            elif current_value[0:len(search)] > target:
                right_pointer = mid_idx
            elif current_value[0:len(search)] < target:
                left_pointer = mid_idx
        
        if len(results) == 0:
            return None
        else:
            return results
    
    # Handles the logic used to gather target of search and perform all searches needed to navigate down to the potential genre to search
    def search_loop(self, list):
        print("What genre of music would you like to listen to?")
        search_value = input("Type the beginning of that genre and press enter to see if it's there.\n")
        search_results = self.modified_binary_search(search_value, list)
        if search_results == None:
            print(f"There were no genres found for {search_value}.")
            return None
        elif len(search_results) > 1:
            print(f"With those beginning letters, your choices are {search_results}.")
            self.search_loop(search_results)
        else:
            user_response = ""
            while user_response != "y" and user_response != "n":
                user_response = input(f"The only option with those beginning letters is {search_results[0]}. Do you want to look at {search_results[0]} artists? Enter 'y' for yes 'n' for no. \n").lower()
            if user_response == "y":
                for artist in self.children[search_results[0]].children.values():
                    print(f"""
                --------------------------------------
                    Genre: {artist.genre}
                    Artist: {artist.artist}
                    Billboard Ranking: {artist.ranking}/100
                    Top Song: {artist.song}
                    # of Albums: {artist.albums}
                    """)
                    
# Function to execute program
def recommend_artists():
    music_tree = TreeNode()    
    music_tree.store_data_set(artist_data)
    sort_list = list(music_tree.children.keys())    

    print("""
                         :+""  ~<<::""+:
                +Xi<<<<!<  `<<!?!<<<HMti%L
            :?HMMMM:<<<!<~ <<<!X<<<!MM88MMh?x
          !HMRMMRMMM:<<<!< <<<!!<<<MR88MRMMRMH?.
        ?NMMMMMMMMMMM<<<?<  <<!!<<XM88RMMMMMMMMM?
      !88888MMMMMMRMMk<<!!  <<H!<<M88MRMMRMMMRMMRM!
     <M8888888MMMMMMMM:<<!  <<H<<488RMMMMMMMMMMMMMM>:
   xHMRMMR888888RMMMMMM<<!< <!!<<988RMMMRMMRMMMMM?!<<%
  :XMMMMMMMM88888MMMMMMH<<~ ~~~<X8RMMMMMMMMMMM!!<~    k
  <<<!MMRMMRMMR8888MMP.n~       #R.#MMRMMRM?<~~   .nMMh.
 !MMH:<<<!*MMMMMMM8Pu! n"       "+ "h!MM!!~   :@MMMMMMM/
.HMRMMRMMMH:<<"*RM M @             * "   .nMMMMMMMRMMRMMk
MMMMMMMMMMMMMMMMx < "      .u.        4'MMMMMMMMMMMMMMMM9
!RMMRMMMRMMRMMMMMX M     @P   #8     4 MMRMMMRMMRMMMMMMR<
!MMMMMMMMMMMMMMMMM !    '8     8!    ' MtMMMMMMMMMMMMMMM!
kMMRMMRMMRMMMRMMR4 H     #8.  @8     H MMMMRMMMMMMRMMRMM!
MMMMMMMMMMMMMMMMM>M         "`      .~i <!?MMMMMMMMMMMMM9
'9MMRMMMRMMRMMP!   : %             H @ 8NRMHx<<<!!MMMMMR!
 >MMMMMMMMM"   <<HMk!i *u       .* x*xR88888MMMMHi<<<<~<
  !RMM#~   :<:MMRMMMMH.*n:      :*.HRMMMRM8888888MRMMM!
  !     <<:tMMMMMMMMMM8RM<::: :<<XMMMMMMMMMR88888888MM!
   ~ <<<XHMRMMMMMMRMM8RM<<<<< `!<<MRMMRMMRMMMRR888888#
     :HMMMMMMMMMMMM988MM<<X!<~'~<<<MMMMMMMMMMMMMR88#!
      ~MMRMMMRMMRMM88MM<<<?<<  <<<<!RMMMRMMRMMMMMM!
        xMMMMMMMM988MM%<<<?<<: <!<<<?MMMMMMMMMMMX
          !?MMMM@88MMR<<<<!<<<  <:<<<MRMMRMMMP!
            "X*988RMM!<<<?!<<~  <!<<<<MMMMM?"
                !X*MM<<<<H!<<`  <?<<<<<)!
                     "+:uX!<<< .::+""


               Welcome to the Artist Finder! 


    """)
    program_loop = True
    while program_loop == True:
        music_tree.search_loop(sort_list)
        user_response = ""
        while user_response != "y" and user_response != "n":
                user_response = input(f"Would you like to to search another genre? Enter 'y' for yes 'n' for no. \n").lower()
        if user_response == "n":
            program_loop = False
    
    print("Thank you for using the Artist Finder!")


recommend_artists()


