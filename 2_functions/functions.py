"""
Python code to demonstrate functions.

"""
# Declare Functions

#  Song title
def title():
    # Song Title
    title = "Sugar"
    return title

# Song artist
def artist():
    # Name of Artist
    artist = "Maroon 5"
    return artist

# Song artist
def releaseYear():
    # Year of release
    releaseYear = 2014
    return releaseYear

def downloadable():
    # Available for digital digital download?
    downloadable = True
    return downloadable

# Call Functions

title = title()
artist = artist()
releaseYear = releaseYear()
downloadable = downloadable()

# Print results
print("Title: " + title)
print("Artist: " + artist)
print("Year of Release", releaseYear)
print("Downloadable", downloadable)
