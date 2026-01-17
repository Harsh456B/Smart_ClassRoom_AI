from collections import Counter
import os
from datetime import datetime

def analyze_emotions(emotion_log):
    """
    Phase 3: Emotion & Engagement Analytics
    Returns analytics for Phase 4 alerts
    """

    if not emotion_log:
        print("\nNo emotions detected")
        return None

    counts = Counter(emotion_log)
    total = sum(counts.values())

    print("\nEmotion Summary:")
    for emo, cnt in counts.items():
        print(f"{emo} : {cnt}")

    dominant_emotion = counts.most_common(1)[0][0]
    print("Dominant Emotion:", dominant_emotion)

    # Engagement logic
    happy = counts.get("Happy", 0)
    neutral = counts.get("Neutral", 0)

    weighted_score = (happy * 1.0) + (neutral * 0.5)
    engagement_score = int((weighted_score / total) * 100)

    if engagement_score >= 70:
        engagement_level = "High Engagement"
    elif engagement_score >= 40:
        engagement_level = "Moderate Engagement"
    else:
        engagement_level = "Low Engagement"

    print("Engagement Score:", engagement_score, "%")
    print("Engagement Level:", engagement_level)

    # Save report
    os.makedirs("reports", exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("reports/session_summary.txt", "w") as f:
        f.write("SMART CLASSROOM AI – SESSION REPORT\n")
        f.write(f"Session Time: {timestamp}\n\n")

        f.write("Emotion Summary\n")
        for emo, cnt in counts.items():
            percent = int((cnt / total) * 100)
            f.write(f"{emo}: {cnt} ({percent}%)\n")

        f.write(f"\nDominant Emotion: {dominant_emotion}\n")
        f.write(f"Engagement Score: {engagement_score}%\n")
        f.write(f"Engagement Level: {engagement_level}\n")

    # 🔹 RETURN for Phase 4
    return {
        "engagement_score": engagement_score,
        "engagement_level": engagement_level,
        "dominant_emotion": dominant_emotion
    }
