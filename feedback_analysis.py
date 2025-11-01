def positive_feedback_percentage(ratings):
    if not ratings:
        return 0
    
    positive = len([r for r in ratings if r >= 4])
    return round((positive / len(ratings)) * 100, 2)


ratings = [5, 4, 3, 5, 2, 4, 1, 5]
print("Positive Feedback:", str(positive_feedback_percentage(ratings)) + "%")
