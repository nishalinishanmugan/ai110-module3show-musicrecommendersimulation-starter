# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

---
Each Song includes features like genre, mood, energy, tempo, valence, danceability, and acousticness. All the features are important. For exmaple, genre tells us about the style and mood tells us about the feeling. And the other features tells us more about specifics about the song like tempo and danceability. The UserProfile should tell you what does our listener prefer. They should includes all the factors that songs.csv mention. However, I think genre and mood should be the most important information. The Recommender should give a score for each song by comparing the songs features to the user's preferences. If the song matches the user's preferences for genre and mood, they should earn extra points. If they are farther away from the user's preferences, they should earn less points. The Recommender should reward points based on similaries to be more inligned with the User's preferences. The Recommender should also sort the songs from highest to lowest scores. The highest score songs should be choosen as recommendations because they match the closest to what the user would like. The flow should be look at the UserProfile preferences, compare the song with it and give a score, sort all the songs by score, and then recommend the top score songs to the User. 


Example of User Profile:
user_profile = {
    "favorite_genre": "lofi",
    "favorite_mood": "chill",
    "target_energy": 0.35,
    "target_tempo_bpm": 75,
    "target_valence": 0.60,
    "target_danceability": 0.55,
    "target_acousticness": 0.80
}

Because there are clear classification for the categories, it should be able to separate intense rock from chill lofi with all the filtering. 

Algorithm Recipe:
2.0 points if the song’s genre matches the user’s favorite genre. 1 points if the song’s mood matches the user’s favorite mood
There should be similar points for numeric features: energy, tempo_bpm, valence, danceability, and acousticness.

The closer the song is to the user’s target, the more points it gets.

Sample Recipe: 
score = 0

if song.genre == user_profile["favorite_genre"]:
    score += 2.0

if song.mood == user_profile["favorite_mood"]:
    score += 1.0

score += (1 - abs(song.energy - user_profile["target_energy"]))* 1.5
score += max(0, 1 - abs(song.tempo_bpm - user_profile["target_tempo_bpm"]) / 100) * 1.0
score += (1 - abs(song.valence - user_profile["target_valence"])) * 1.0
score += (1 - abs(song.danceability - user_profile["target_danceability"])) * 1.0
score += (1 - abs(song.acousticness - user_profile["target_acousticness"])) * 1.0


```markdown
## Mermaid Diagram

```mermaid
flowchart TD
    A[User Profile Preferences] --> B[Load songs from songs.csv]
    B --> C[Loop through each song]
    C --> D[Compare song features to user preferences]
    D --> E[Calculate recommendation score]
    E --> F[Store song and score]
    F --> G[Sort all songs by score]
    G --> H[Return Top K recommendations]

In conclusion, this system uses the user's listening behavior to recommend songs based on the features of each song to the specific user preference profile. Each song includes factors such as genre, mood, energy, tempo, valence, danceability, and acousticness. The recommender should loop through each song in songs.csv and give a score based on how close it matches the user's preferences. The songs with the highest scores will be ranks first and be at the top of the recommendation. 

There are some potential biases. The dataset is small, so there isn't a lot of variety. The system might be bias toware teh user's favorite genre even when other songs have similar moods or factors because it is weighted the most. It could ignore great songs that match the user's mood if it's not in the same genre. 

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```
After Implementing Phase 3: Implementation, these are the current results I receive

![alt text](image.png)

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

