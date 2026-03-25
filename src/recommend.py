def get_recommendations(data):
    recommendations = []

    if data["study_hours"] < 4:
        recommendations.append("Increase study hours")

    if data["attendance"] < 75:
        recommendations.append("Improve attendance")

    if data["internet_usage"] > 5:
        recommendations.append("Reduce internet usage")

    if data["sleep_hours"] < 6:
        recommendations.append("Maintain proper sleep schedule")

    return recommendations