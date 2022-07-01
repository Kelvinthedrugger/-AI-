# backend APIs
# connect to ai model, return output to frontend (unity, mobile, etc)
# connect to database, and so on


"""
Description:
when user push the analyze botton, we will kick off a command/script to call this
python script. And pass the selected dialogue to this script

Advanced stuff:
    when we select texts in a mobile app (e.g., Line), a set of button will appear
    , can we add a button to kickstart our app ?

    dynamically track selected user's dialogue (and analyze it)


script:
    get the dialogue -> call the ai model -> get the output[1]
    -> plot (a part of ?) dataset distribution and the user input


model:
    load the pre-trained weight -> inference the user's diaglogue -> return output


[1] output: most likely a data point: on the x-y emotion coordinate thing

"""

def main():
    pass


if __name__ =="__main__":
    main()

