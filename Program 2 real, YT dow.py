"""
Youtube downloader for CS246
"""
#gets the import from pytube
from pytube import YouTube

again = True #Allows for a reset to happen
while again == True: #while reset is true
     link = input("Enter the link of YouTube video you want to download:  ") #asks for video to download
     yt = YouTube(link)
     #Showing details
     print("Title: ",yt.title) #Showing details
     print("Number of views: ",yt.views)
     print("Length of video: ",yt.length)
     print("Rating of video: ",yt.rating)
     good = input("Do you want to download this video? y/n ")  
     #Checks if you want to download video
     if good == 'y':    
          ys = yt.streams.get_highest_resolution() #Getting the highest resolution possible
          #Starting download
          print("Downloading...")
          ys.download('/Users/speed/Downloads')
          print("Download completed!!")
     while good == ('n'): #allows for you to download another video if you got it incorrect
          link = input("Enter the link of YouTube video you want to download:  ")
          yt = YouTube(link)
          print("Title: ",yt.title)
          print("Number of views: ",yt.views)
          print("Length of video: ",yt.length)
          print("Rating of video: ",yt.rating)
          good = input("Do you want to download this video? y/n ")
          if good == 'y':     #Getting the highest resolution possible
               ys = yt.streams.get_highest_resolution()
               #Starting download
               print("Downloading...")
               ys.download('/Users/speed/Downloads') #places the video in my downloads folder
               print("Download completed!!")
     down = input("Do you want to download another video? y/n ") #checks if you want to download another video
     if down == ('y'):
          again = True
     else:
          again = False
    