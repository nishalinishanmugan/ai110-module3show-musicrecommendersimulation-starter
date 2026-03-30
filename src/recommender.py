from typing import List, Dict, Tuple
from dataclasses import dataclass
import csv


@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def _score_song_for_user(self, user: UserProfile, song: Song) -> Tuple[float, List[str]]:
        """Compute a compatibility score and reasons for a single song against the user's profile."""
        score = 0.0
        reasons = []

        if song.genre.lower() == user.favorite_genre.lower():
            score += 2.0
            reasons.append("genre match (+2.0)")

        if song.mood.lower() == user.favorite_mood.lower():
            score += 1.0
            reasons.append("mood match (+1.0)")

        energy_similarity = max(0.0, 1 - abs(song.energy - user.target_energy))
        energy_points = energy_similarity * 2.0
        score += energy_points
        reasons.append(f"energy similarity (+{energy_points:.2f})")

        if user.likes_acoustic and song.acousticness >= 0.6:
            score += 0.5
            reasons.append("acoustic preference match (+0.5)")
        elif not user.likes_acoustic and song.acousticness < 0.6:
            score += 0.5
            reasons.append("non-acoustic preference match (+0.5)")

        return score, reasons

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the top-k songs ranked by compatibility with the user's profile."""
        scored = []

        for song in self.songs:
            score, _ = self._score_song_for_user(user, song)
            scored.append((song, score))

        ranked = sorted(scored, key=lambda item: item[1], reverse=True)
        return [song for song, _ in ranked[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Return a human-readable explanation of why a song was recommended to the user."""
        _, reasons = self._score_song_for_user(user, song)
        return ", ".join(reasons)


def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    print(f"Loading songs from {csv_path}...")

    songs = []
    with open(csv_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            songs.append({
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            })

    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against a user's preferences.
    Returns a numeric score and a list of reasons.
    """
    score = 0.0
    reasons = []

    # Genre match
    if song["genre"].lower() == user_prefs.get("genre", "").lower():
        score += 2.0
        reasons.append("genre match (+2.0)")

    # Mood match
    if song["mood"].lower() == user_prefs.get("mood", "").lower():
        score += 1.0
        reasons.append("mood match (+1.0)")

    # Energy similarity
    if "energy" in user_prefs:
        energy_similarity = max(0.0, 1 - abs(song["energy"] - user_prefs["energy"]))
        energy_points = energy_similarity * 2.0
        score += energy_points
        reasons.append(f"energy similarity (+{energy_points:.2f})")

    return score, reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py

    Returns:
        List of tuples in the form:
        (song_dict, score, explanation)
    """
    scored_songs = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        scored_songs.append((song, score, explanation))

    ranked_songs = sorted(scored_songs, key=lambda item: item[1], reverse=True)
    return ranked_songs[:k]
