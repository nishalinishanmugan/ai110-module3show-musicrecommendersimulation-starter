"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def print_recommendations(profile_name: str, user_prefs: dict, songs: list[dict]) -> None:
    """Print the top recommendations for one user profile."""
    print(f"\n=== {profile_name} ===")
    print(f"User profile: {user_prefs}\n")

    recommendations = recommend_songs(user_prefs, songs, k=5)

    for index, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"{index}. {song['title']} by {song['artist']}")
        print(f"   Genre: {song['genre']} | Mood: {song['mood']} | Energy: {song['energy']}")
        print(f"   Score: {score:.2f}")
        print(f"   Reasons: {explanation}")
        print()


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    profiles = {
        "High-Energy Pop": {
            "genre": "pop",
            "mood": "happy",
            "energy": 0.85,
        },
        "Chill Lofi": {
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.40,
        },
        "Deep Intense Rock": {
            "genre": "rock",
            "mood": "intense",
            "energy": 0.90,
        },
        "Edge Case: High Energy but Relaxed Mood": {
            "genre": "jazz",
            "mood": "relaxed",
            "energy": 0.90,
        },
    }

    for profile_name, user_prefs in profiles.items():
        print_recommendations(profile_name, user_prefs, songs)


if __name__ == "__main__":
    main()
