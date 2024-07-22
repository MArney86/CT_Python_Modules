def mood_response(mood): #initialize the response function
    moods_responses = {'happy':'Awesome, keep it up!!!',
                       'sad':"I'm sorry you feel sad. Is there anything I can do help you feel better?",
                       'playful':"Let's go out and have some fun!",
                       'aloof':"What's got you feeling so distant?",
                       'uneasy':"What's on your mind?",
                       'calm':"Relaxing vibes are good for the soul.",
                       'thankful':"Giving thanks is a good way to let people know you care what they do.",
                       'cheerful':"Smiles and cheer make everyone want to be your friend",
                       'mischievous':"Just don't cause any mischief that could hurt someone",
                       'serious':"Don't forget to have some fun too. Gotta keep it all in balance.",
                       'eager':"Keep your wits about you, ambition can easily be sidetracked.",
                       'tense':"Don't let things get you all wound up. Take some time to relax",
                       'angry':"Feel the feelings and let them go.",
                       'fearful':"Things may seem scary, but life has a way of balancing out.",
                       'scared':"Fear is just your mind keeping you alert!",
                       'depressed':"This will pass and you will feel better again.",
                       'silly':"What's a good joke you've heard recently?",
                       'lonely':"Don't worry, there's always someone new to meet around the corner.",
                       'antagonistic':"What happened to make you feel this way?"} #a dictionary containing moods as keys and responses for values
    if mood.lower() in moods_responses.keys(): #check that the input mood is in the dictionary's keys
      return moods_responses[mood.lower()] #return the corresponding response for the input mood
    else: #mood is not already in the dictionary's keys
      return "That mood was not in our database." #notify user that that mood is not in our dictionary