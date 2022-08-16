
# For the project frontend app

### use flask since it's the easiest

    we still need html for the pages, i feel tired
    what i need is just to 
        1. show login info & login: done
        2. show search chatroom: done
        2.5: jump to chatroom:done
        3. show the conversation:done
        4. fix multiple people connection problem: shxt
    
    note:
        user (sort of) controls which webpage to visit
        start from scratch:
            make sure 'hello' page works
            make sure 'redirect to login page' works
            make sure 'redirect after press login button' works
            make sure 'search chatroom in html' works
            make sure 'kickstart chatroom' works

            lastly, make sure '>1 user online' works


### server: just run 'python -m http.server'

### fix multiple session problem

#### just use dict() to solve it ?!
when user A login -> ret["userA"] = driver_a

when user B login -> .. # the same

when user A logout-> delete "userA" from ret

acc_driver = {} # {"username": driver_of_the_user}

if the driver of the user is not removed, the login session won't be closed

#### cons
the UI is pretty ugly, requires the username (user account) for every action...

try to came up with a better way to handle the backend

refresh problem (not that urgent but necessary)

Language (on FB) problem is just really annoying 
 (affects xpath and so on)


### embed javascript in html if you're smart enough (?
