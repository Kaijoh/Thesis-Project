screen bmapbutton():
    imagebutton:
        xalign 0.94
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "mi"
        hover "mii"
        action ShowMenu("bmapscreen")

screen bmapscreen():
    add "map"
    vbox:
        xalign 0.08
        yalign 0.1
        yoffset 30 
        spacing 20 
        text "Ruins (Hard)\n 2 pages needed to unlock."

        imagebutton: 
            idle "rn" 
            hover "rn1"
            if pages >= 2:
                action Jump("bthirdvillain") 
    vbox:
        xalign 0.5
        yalign 0.8
        yoffset 30 
        spacing 20 
        text "Cave (Medium)\n 1 page needed to unlock."

        imagebutton: 
            idle "cv" 
            hover "cv1"
            if pages >= 1:
                action Jump("bsecondvillain") 
    vbox:
        xalign 0.94
        yalign 0.3
        yoffset 30 
        spacing 20 
        text "Forest (Easy)"

        imagebutton: 
            idle "mt" 
            hover "mt1"
            if pages >= 0:
                action Jump("bfirstvillain") 
            
                
                  
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()

screen gmapbutton():
    imagebutton:
        xalign 0.94
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "mi"
        hover "mii"
        action ShowMenu("gmapscreen")

screen gmapscreen():
    add "map"
    vbox:
        xalign 0.08
        yalign 0.1
        yoffset 30 
        spacing 20 
        text "Ruins (Hard)\n 2 pages needed to unlock."

        imagebutton: 
            idle "rn" 
            hover "rn1"
            if pages >= 2:
                action Jump("gthirdvillain") 
    vbox:
        xalign 0.5
        yalign 0.8
        yoffset 30 
        spacing 20 
        text "Cave (Medium)\n 1 page needed to unlock."

        imagebutton: 
            idle "cv" 
            hover "cv1"
            if pages >= 1:
                action Jump("gsecondvillain") 
    vbox:
        xalign 0.94
        yalign 0.3
        yoffset 30 
        spacing 20 
        text "Forest (Easy)"

        imagebutton: 
            idle "mt" 
            hover "mt1"
            if pages >= 0:
                action Jump("gfirstvillain") 
            
                
                  
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()


screen soundson():
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "spon"
        hover "spon1"
        action [ Preference("all mute", "toggle"), ToggleScreen("soundsoff"), ToggleScreen("soundson"), ]

screen soundsoff():
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "spoff"
        hover "spoff1"
        action [  Preference("all mute", "toggle"), ToggleScreen("soundson"), ToggleScreen("soundsoff"), ]