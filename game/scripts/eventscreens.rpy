#routes x

screen choosechar:
    hbox:
        xalign 0.5
        yalign 0.1
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "Choose your character."

# screen choosereward:
#     hbox:
#         xalign 0.5
#         yalign 0.01
#         frame:
#             background "#706969"
#             xalign 0.5
#             yalign 0.5
#             padding (50,50)
#             margin (0,0,10,0)
#             text "Exchange Reward.\nYou can exchange your book page here for a permanent additional heart that will help you in your jouney "

screen choose_route: 
    hbox: 
        xalign 0.5 
        yalign 0.5 
        yoffset 30 
        spacing 20 
        imagebutton: 
            idle "boychar2" 
            hover "boychar" 
            action Jump("variable1") 
        imagebutton: 
            idle "girlchar" 
            hover "girlchar2" 
            action Jump("variable2") 

screen arrows():
    hbox:
        xalign 0.09
        yalign 0.10
        add "arrow"

screen hearts():
    hbox:
        xalign 0.01
        yalign 0.02
        
        for i in range(max_lives):
            fixed xysize(50, 50): 
                add "background"
                add "border"
                if i < lives:
                    add "heart"
                    
screen books():
    hbox:
        xalign 0.0
        yalign 0.08
        for i in range(pages):
            fixed xysize(55, 55): 
                add "book"

screen fullbooks():
    hbox:
        xalign 0.01
        yalign 0.01
        add "fullbook"

screen addpages():
    hbox:
        xalign 0.5
        yalign 0.5
        add "addpage"



screen gameUI():
    imagebutton:
        xalign 0.88
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "sts"
        hover "sts1"
        action ShowMenu("StatsUI")

screen StatsUI():
    hbox:
        xalign 0.5
        yalign 0.5
        frame:
            add "#4b3b3b"
            xalign 0.5
            yalign 0.5
            padding (750,370)
            margin (0,0,0,0)
            vbox:
                xalign 0.25
                yalign 0.3
                spacing 10
                text "PLAYER STATS" size 40
                text "Name:" size 40
                text "Score:" size 40
                text "Lives:" size 40
                text "Pages:" size 40
            
            vbox:
                
                xalign 0.85
                yalign 0.3
                spacing 10
                text '       ' size 40
                text '[player_name]' size 40
                text '[player_score]' size 40
                text '[lives]' size 40
                text '[pages]' size 40

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()
    
screen rewardbutton():
    imagebutton:
        xalign 0.82
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "sps"
        hover "sps1"
        action ShowMenu("rewardshop")

screen rewardshop(): 
    vbox:
        xalign 0.5
        yalign 0.05
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "                   EXCHANGE REWARD.\n\nYou can exchange your book page here for a \n additional heart that will help you\nin your jouney.\n1 page = 1 heart "
    vbox:
        xalign 0.5
        yalign 0.5
        yoffset 30 
        spacing 20 

        imagebutton: 
            idle "exchange2" 
            hover "exchange" 
            if pages >= 1:
                action [SetVariable("pages", pages - 1), SetVariable("max_lives", max_lives + 1), SetVariable("lives", lives + 1), ToggleScreen("adisplay"), ToggleScreen("rewardshop"), ]
                
        # imagebutton: 
        #     idle "exchange2" 
        #     hover "exchange" 
        #     if lives >= 1 and player_score >= 1:
        #         action [SetVariable("player_score", player_score + 1), SetVariable("lives", lives - 1)]
                  
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "close"
        action Return()

screen adisplay():
    vbox:
        add "addh"
        xalign 0.5
        yalign 0.7

    imagebutton:
        xalign 0.5
        yalign 0.01
        xoffset -30
        yoffset 30
        idle "close"
        action [ToggleScreen("adisplay"), ToggleScreen("rewardshop")]


#puzzles
screen question1():
    hbox:
        xalign 0.5
        yalign 0.4
        frame:
            background "#4b3b3b"
            xalign 0.5
            yalign 0.5
            padding (50,100)
            margin (0,0,10,0)
            text "Which word belongs in the blank space?.\nYou left _____ phone at home.\n\na. your\nb. you're\nc. youre\nd. you'll"

screen question2(): 
    hbox:
        xalign 0.5
        yalign 0.4
        frame:
            background "#4b3b3b"
            xalign 0.5
            yalign 0.5
            padding (50,100)
            margin (0,0,10,0)
            text "Which word belongs in the blank space?.\n_____ dinner last night, I watched a movie with my family.\n\na. After\nb. when\nc. our\nd. On"

screen question3():
    hbox:
        xalign 0.5
        yalign 0.4
        frame:
            background "#4b3b3b"
            xalign 0.5
            yalign 0.5
            padding (50,100)
            margin (0,0,10,0)
            text "Which word belongs in the blank space?.\nThe teacher ____________ the students for not studying for the test.\n\na. Praisess\nb. Scolded\nc. Encourager\nd. Congratulated"

screen question4():
    hbox:
        xalign 0.5
        yalign 0.4
        frame:
            background "#4b3b3b"
            xalign 0.5
            yalign 0.5
            padding (50,100)
            margin (0,0,10,0)
            text "Which word belongs in the blank space?.\nShe was ____________ when she heard the news.\n\na. Happiness\nb. Sad\nc. Worry\nd. Laugh"

screen question5():
    hbox:
        xalign 0.5
        yalign 0.4
        frame:
            background "#4b3b3b"
            xalign 0.5
            yalign 0.5
            padding (50,100)
            margin (0,0,10,0)
            text "Which word belongs in the blank space?.\nThe team lost and their performance was ____________ in the championship game.\n\na. Incredibles\nb. Disappointing\nc.Insanely \nd. Outstanding"

screen question6():
    hbox:
        xalign 0.5
        yalign 0.4
        frame:
            background "#4b3b3b"
            xalign 0.5
            yalign 0.5
            padding (50,100)
            margin (0,0,10,0)
            text "Which word belongs in the blank space?.\nHe __________ like ice cream.\n\na. want\nb. doesn't\nc. isn't\nd. not"

screen question7():
    hbox:
        xalign 0.5
        yalign 0.4
        frame:
            background "#4b3b3b"
            xalign 0.5
            yalign 0.5
            padding (50,100)
            margin (0,0,10,0)
            text "Which word belongs in the blank space?.\nShe _______ a cat.\n\na. haves \nb. has \nc. is have\nd. not have"

screen question8():
    hbox:
        xalign 0.5
        yalign 0.4
        frame:
            background "#4b3b3b"
            xalign 0.5
            yalign 0.5
            padding (50,100)
            margin (0,0,10,0)
            text "Which word belongs in the blank space?.\nI _________ to the park yesterday.\n\na. goed \nb. went \nc. go \nd. was"

screen question9():
    hbox:
        xalign 0.5
        yalign 0.4
        frame:
            background "#4b3b3b"
            xalign 0.5
            yalign 0.5
            padding (50,100)
            margin (0,0,10,0)
            text "Which word belongs in the blank space?.\nThey _________ happy.\n\na. am \nb. is \nc. are \nd. be "

screen question10():
    hbox:
        xalign 0.5
        yalign 0.4
        frame:
            background "#4b3b3b"
            xalign 0.5
            yalign 0.5
            padding (50,100)
            margin (0,0,10,0)
            text "Which word belongs in the blank space?.\nWe _________ to the party.\n\na. didn't went \nb. didn't go \nc. don't go\nd. wasn't go"


screen question11():
    hbox:
        xalign 0.5
        yalign 0.4
        frame:
            background "#4b3b3b"
            xalign 0.5
            yalign 0.5
            padding (50,100)
            margin (0,0,10,0)
            text "What is the definition of \'apprehensive'?.\n\na. feeling nervous or worried\nb. having a lot of knowledge or experience\nc. behaving in a showy way to impress others\nd. causing disgust or horror"

screen question12():
    hbox:
        xalign 0.5
        yalign 0.4
        frame:
            background "#4b3b3b"
            xalign 0.5
            yalign 0.5
            padding (50,100)
            margin (0,0,10,0)
            text "What is the definition of 'conjecture'?.\n\na. a fact or piece of information that is known\nb. a conclusion based on incomplete evidence\nc. the feeling of being grateful for something\nd. a state of confusion or uncertainty"

screen question13():
    hbox:
        xalign 0.5
        yalign 0.4
        frame:
            background "#4b3b3b"
            xalign 0.5
            yalign 0.5
            padding (50,100)
            margin (0,0,10,0)
            text "What is the definition of 'diligent'?.\n\na. showing great attention to detail or effort\nb. unwilling to give up or compromise\nc. characterized by a lack of order or planning\nd. having a tendency to change one's mind frequently"

screen question14():
    hbox:
        xalign 0.5
        yalign 0.4
        frame:
            background "#4b3b3b"
            xalign 0.5
            yalign 0.5
            padding (50,100)
            margin (0,0,10,0)
            text "What is the definition of 'indignant'?.\n\na. feeling angry or annoyed about something unfair\nb. lacking energy or enthusiasm\nc. showing a lack of interest or concern\nd. having a tendency to avoid social situations"

screen question15():
    hbox:
        xalign 0.5
        yalign 0.4
        frame:
            background "#4b3b3b"
            xalign 0.5
            yalign 0.5
            padding (50,100)
            margin (0,0,10,0)
            text "What is the definition of 'resilient'?.\n\na. having a tendency to take risks or be impulsive\nb. characterized by a lack of attention or focus\nc. showing a lack of emotion or enthusiasm\nd. able to recover quickly from difficulties or setbacks"

screen question16():
    hbox:
        xalign 0.5
        yalign 0.4
        frame:
            background "#4b3b3b"
            xalign 0.5
            yalign 0.5
            padding (50,100)
            margin (0,0,10,0)
            text "Which word means 'extremely angry'?\n\na. Content \nb. Furious\nc. Pensive\nd. Elated"

screen question17():
    hbox:
        xalign 0.5
        yalign 0.4
        frame:
            background "#4b3b3b"
            xalign 0.5
            yalign 0.5
            padding (50,100)
            margin (0,0,10,0)
            text "Which word means 'to feel or express deep sorrow or regret'?\n\na. Commend\nb. Condemn\nc. Approve\nd. Praise"

screen question18():
    hbox:
        xalign 0.5
        yalign 0.4
        frame:
            background "#4b3b3b"
            xalign 0.5
            yalign 0.5
            padding (50,100)
            margin (0,0,10,0)
            text "Which word means 'to feel or express deep sorrow or regret'?\n\na. Celebrate\nb. Mourn\nc. Rejoice\nd. Delight"

screen question19():
    hbox:
        xalign 0.5
        yalign 0.4
        frame:
            background "#4b3b3b"
            xalign 0.5
            yalign 0.5
            padding (50,100)
            margin (0,0,10,0)
            text "Which word means 'to make a formal request for something'?\n\na. Inquire\nb. Demand\nc. Command\nd. Request"

screen question20():
    hbox:
        xalign 0.5
        yalign 0.4
        frame:
            background "#4b3b3b"
            xalign 0.5
            yalign 0.5
            padding (50,100)
            margin (0,0,10,0)
            text "Which word means 'to cause great fear or distress'?\n\na. Terrify\nb. Calm\nc. Soothe\nd. Comfort"

