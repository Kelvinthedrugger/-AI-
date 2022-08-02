# fetch content from plurk website using their public APIs


"""
#useful APIs

/APP/FriendsFans/getxxxByOffset: If only you have friends/fans/following

/APP/Profile/getPublicProfile
    require: user_id; use "search" to get this

/APP/Timeline/getPlurks

/APP/Responses/get: fetch responses, so, be active on social apps!
    require: plurk_id; needs to hack-around it, play around and try xpath again ...

/APP/PlurkSearch/search: search plurks (not sure what "plurk" means, ~20)
    require: query after users

/APP/UserSearch/search: search users (~10)
    require: query after users


/APP/Emoticons/get: get emoji's

"""

# Check visit limit!
#   Search: emojis
#   fetch top 20 posts (since it's a tryout, see how to set fetch limit as well
#   save it, in case the visit limit reaches, change to save once every 500 posts


def main():
    # loop thru emojis ## 6 categories
    #   search the emoji
    #   fetch xxx (500) posts, some constrain like "visit 20 posts tops at a time"?
    #   save them

    pass


if __name__ =="__main__":
    main()

