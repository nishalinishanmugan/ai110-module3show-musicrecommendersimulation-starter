# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---
My model name is VibeRecommenderSimulator. 

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---
This recommender suggests songs based on what kind of music the user likes, such as their favorite genre, mood, and energy level. It assumes the user knows what type of vibe they want or like. This project is for classroom exploration. 

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

The features of each song are genre, mood, energy, tempo_bpm, valence, danceability, and acousticness. The model gives each song a score based on how well it matches the user’s preferences. If the genre or mood matches, the song gets extra points. It also checks how close the song’s energy, tempo_bpm, valence, danceability, and acousticness is to what the user wants. And the song also gets points based on this. Songs with higher scores are recommended first to the user. I determined the points based on all these factors from the starter logic and implemented it using Clause in recommender.py. 

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---
The song.csv dataset contains 20 songs with features such as genre, mood, energy, tempo, valence, danceability, and acousticness. I expanded the dataset to include more genres like metal, reggae, classical, and bossa nova when I added 10 extra songs to the original 10. There are a lot of moods and genres represented like intense, chill, lofi, rock, and so on. The dataset is very small and does not fully represent all types of music or listening preferences.

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---
The system works well when the user has a clear preference, like chill lofi or intense rock. It does a good job matching songs with similar energy and genre. The results felt accurate based on what I was expecting. When I took out mood from the recommender.py, the results were less accurate, which shows that mood matters. 

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

---

The recommender only analyzes a few features like genre, mood, and energy. It could analyze more features like whether or not the user likes a specific artist or tempo. The songs.csv only had 20 songs, so it's a small sample size. There could be unrepresented genres and moods. So users with less common preferences would probably get weaker recommendations. The score can also proritize genre orenergy. For example, Gym Hero can rank high for users that want upbeat pop because it's high energy mood matches even if the mood doesn't fit. The system fices less accurate results to users with more mixed or unusual tastes. It would probably favor users with strong weighted features. 

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

---
I tested the system with differnt profiles like High_Energy, Chill LoFi, Deep Intense Rock, and high energy with relaxed mood for an edge case. I checked whether the recommendations felt right based on the type of music each user would probably want. The results mostly matched what I was expecting.  But some high-energy songs kept appearing even when the mood was not the best match. This showed me that the recommender is bias to energy. I also compared the results before and after removing mood from the scoring, and the recommendations became less accurate, which helped confirm that mood is an important feature. Gym Hero keeps showing up because the system sees that its energy level is close to what the user wants, so it scores well even if its mood is not the best emotional match.

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---
I want to expand the dataset to include more songs, more genres, more artists, more preferences, and so on. I also want to test with more user profiles and a variery of user profiles. I want to find more information on user profiles and different artist, genres, tempos, etc from Spotify. I want to improve the scoring system to balance out features and create better recommendations. Increasing the dataset would improve diversty among the top results as well as handle more complex user tastes, especially if I did research with Spotify or Apple Music.  

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

As I worked on this project, I learned how the recommender uses the songs.csv data to recommend songs to the user based on the user's profile by comparing features and assigning scores. I saw how small changes like removing mood from the recommender can make it less accurate. I was surprised that the system worked relatively okay though. This project changed how I think about real music recommenders. I now understand that they rely heavily on data and weighting, and that bias can easily appear if certain features are overemphasized. Music Recommenders that Apple Music or Spotify must be complex to consider many factors and many genres. Even if a system seems “smart,” human judgment is still important for understanding context, emotion, and nuance that a basic model cannot fully understand. I did need to double check the AI tools as I worked on this project. My biggest learning moment was seeing how the recommendations changes when factors were taken out. I would try to expand the datset if I had more time. 

