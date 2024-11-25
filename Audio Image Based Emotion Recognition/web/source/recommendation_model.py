import random

def generate_final_result(emotion_data):
    # Extract emotions from the input data
    face_emotion = emotion_data['faceEmotion']
    audio_emotion = emotion_data['audioEmotion']
    text_emotion = emotion_data['textEmotion']

    final_emotions_state = {
        'Positive': 0,
        'Negative': 0
    }

    if face_emotion in ['Happy', 'Surprise', 'Positive', 'Neutral']:
        final_emotions_state['Positive'] += 1
    if audio_emotion in ['Happy', 'Surprise', 'Positive', 'Neutral']:
        final_emotions_state['Positive'] += 1
    if text_emotion in ['Happy', 'Surprise', 'Positive', 'Neutral']:
        final_emotions_state['Positive'] += 1

    if face_emotion in ['Angry', 'Disgusting', 'Fear', 'Negative', 'Sad']:
        final_emotions_state['Negative'] += 1
    if audio_emotion in ['Angry', 'Disgusting', 'Fear', 'Negative', 'Sad']:
        final_emotions_state['Negative'] += 1
    if text_emotion in ['Angry', 'Disgusting', 'Fear', 'Negative', 'Sad']:
        final_emotions_state['Negative'] += 1
        
    emotion_data['finalResult'] = max((k for k, v in final_emotions_state.items() if v != 0), key=lambda k: (final_emotions_state[k], k), default=None)


    # Selecting a random positive or negative song based on the final emotion
    if emotion_data['finalResult'] == 'Positive':
        emotion_data['recommendedSong'] = random.choice([
            "Ude Dil Befikre",       
            "Kar Har Maidaan Fateh",   
            "Happy Budday",            
            "Zindagi Na Milegi Dobara", 
            "Dil Dhadakne Do",         
            "Ainvayi Ainvayi",         
            "Chak De India",           
            "Sooraj Dooba Hai",        
            "Gallan Goodiyaan",        
            "Badri Ki Dulhania",      
            "Dil Chahta Hai",         
            "Zara Sa",                 
            "Ae Watan",                
            "London Thumakda",         
            "Ae Dil Hai Mushkil",     
            "Chak Lein De",            
            "Muskurane Ki Wajah Tum Ho", 
            "Phoolon Ka Taron Ka",    
            "Desi Girl",               
            "Dilli Waali Girlfriend", 
            "Swag Se Swagat",          
            "La La La",               
            "Banno",                   
            "Dil Se Re",              
            "Madhaniya",               
            "Dil Hai Hindustani",     
            "Jeetenge Hum",            
            "Swag Se Swagat",         
            "Mauja Hi Mauja",          
            "Zinda Hoon Mai",          
            "Badtameez Dil",           
            "La La La",                
            "Zindagi Mein Razzak",     
            "Tera Ban Jaunga",         
            "Dhoom Machale",           
            "Chalte Chalte",           
            "Rang De Basanti",         
            "Let's Nacho",             
            "Pehla Nasha",             
            "Dil Dhadakne Do",         
            "Tujh Mein Rab Dikhta Hai" 
        ])

    elif emotion_data['finalResult'] == 'Negative':
        emotion_data['recommendedSong'] = random.choice([
            "Agar Tum Saath Ho",          
            "Channa Mereya",              
            "Tum Hi Ho",                  
            "Tujhe Kitna Chahne Lage",   
            "Kabira",                     
            "Raabta",                     
            "Tum Jo Aaye",                
            "Ae Dil Hai Mushkil",         
            "Tum Se Hi",                 
            "Jeene Laga Hoon",           
            "Sun Saathiya",               
            "Tum Jo Aaye",                
            "Dil Dhadakne Do",           
            "Chupke Chupke",              
            "Mera Mann Kehne Laga",       
            "Mitti Di Khushboo",          
            "Hasi Ban Gaye",              
            "Phir Le Aaya Dil",           
            "Kya Hua Tera Wada",          
            "Tera Ban Jaunga",            
            "Tu Jaane Na",                
            "Tumhe Kitna Chahne Lage",    
            "Khuda Jaane",                
            "Yeh Fitoor Mera",            
            "Zindagi Ke Safar Mein",      
            "Chitthi Toh",                
            "Mausam",                     
            "Agar Tum Saath Ho",          
            "Tere Bina",                  
            "Tere Liye",                  
            "Aashayein",                  
            "Meri Zindagi Mein",          
            "Humari Adhuri Kahani",       
            "Kahin Toh",                  
            "Main Phir Bhi Tumko Chahunga", 
            "Pehli Nazar Mein",           
            "Ek Din Aap",                
            "Agar Tum Saath Ho",         
            "Woh Lamhe Woh Baatein"       
        ])

    return emotion_data