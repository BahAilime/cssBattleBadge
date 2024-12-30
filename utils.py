def fetch_user_data(user_id):
    """
    Fetches the user data for the given user_id from the CSSBattle.dev API.

    Args:
        user_id (str): The user id to fetch the data for.

    Returns:
        dict: A dictionary containing the user's data.
    """
    url = f"https://us-central1-cssbattleapp.cloudfunctions.net/getRank?userId={user_id}"
    response = requests.get(url)
    return response.json()

def process_data(data, username):
    """
    Processes the given data by rounding the score to 2 decimal places and
    creating the name and meanScore fields.

    Args:
        data (dict): The user's data fetched from the CSSBattle.dev API.
        username (str): The username of the user.

    Returns:
        dict: The processed data with the name, score and meanScore fields set.
    """
    data["score"] = round(data["score"], 2)
    data["name"] = f"{username.capitalize()}'s CSSBattle.dev Stats" if username else "CSSBattle.dev Stats"
    data["meanScore"] = f"{round(float(data['score']) / (float(data['playedCount']) if data['playedCount'] != 0 else 1), 2)} / 600"
    return data
