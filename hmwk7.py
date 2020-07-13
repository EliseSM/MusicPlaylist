## ------------------------------------------------------
##        Name: Elise Schatzki-McClain
##    Filename: hmwk7.py
##     Section: L02
##        Date: 3/21/19
##  References: 
## ------------------------------------------------------

#import statements
import webbrowser

#This defines the inital playlist
playlist = []

#This function asks the user what action they want to do, and then performs the action
def action():
    print("============================")
    print("Welcome to the MUSIC LIBRARY")
    print("============================")
    print("")
    #This is a welcome message
    answer = input("Select option: ADD, REMOVE, PRINT, PLAY, QUIT ")
    #This is asking for the user's action 
    while answer != "QUIT" and answer != "quit":
        
        if answer in ["add", "ADD"]:
            addSong()
        if answer in ["remove", "REMOVE"]:
            removeSong()
        if answer in ["print", "PRINT"]:
            printSong()
        if answer in ["play", "PLAY"]:
            playSong()

        answer = input("Select option: ADD, REMOVE, PRINT, PLAY, QUIT ")
    #This loopsends the action to other functions to perform the action
    #If the action is quit, it sends the action back to main and the program ends
    return()
             

#This function creates a dictionary of a new song and adds it to the playlist list
def addSong():
    #This defines a new dictionary called song
    song = {}
    #This asks the user attributes of the song
    title = input("Song title: ")
    artist = input("Artist: ")
    album =  input("Album title: ")
    url = input("Spotify URL: ")
    
    #This takes those attributes and adds them to the dictionary 
    song["title"] = title
    song["album"] = album
    song["url"] = url
    song["artist"] = artist              
    

    #This then takes the new song dictionary created and adds it to the playlist
    playlist.append(song)
    


#This function removes the a specifc song dictionary from the playlist
def removeSong():
    #This asks the user which song they want to remove
    num = int(input("Which # song do you want to remove?"))
    n = num - 1
    #This then removes the song from the list of songs in playlist
    del playlist[n]
    print("Song #", num, "removed.")


#This function prints the full songs and their attributes in a list             
def printSong():
    
    count = 0
    #This loops through each song in the playlist and prints each of its attributes in a specifc format
    for song in playlist:
                   
        #This is a counter so that each song can be numbered in the list
        count = count + 1
        print(count , ". " ,
              "{0}".format(song['title']) , " by " ,
              "{0}".format(song['artist']) , " (" ,
              "{0}".format(song['album']), ")")

                   
        

#This function plays the song requested by the user                  
def playSong():

    #This asks the user which song wants to be played
    song_num = int(input("Which # song would you like to play? ")) - 1
    thissong = playlist[song_num]
    #This takes the attributes from the correct song in the list
    songtitle = thissong['title']
    songurl = thissong['url']

    print("Now playing", songtitle)
    
    #This is plays the song requested
    webbrowser.open(songurl)
    
    



#This function initally calls for the actions to start in the action(), then ends the program
def main():
    action()
    print("Sorry to see you go!")


main()
