import requests

def fetch_word_details(word, property):
    url = "https://wordsapiv1.p.rapidapi.com/words/{}/{}".format(word, property)

    headers = {
        "X-RapidAPI-Key": "8f75b8ee6bmsh2614f9c7dba0f15p1c3292jsn3b82a459152b",
        "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        word_data = response.json()
        return word_data.get(property, [])
    else:
        print("Failed to fetch {} for the word '{}' from the API.".format(property, word))
        return []

# Example usage:
selected_word = "hatchback"
property_to_fetch = "synonyms"

#word_details = fetch_word_details(selected_word, property_to_fetch)
#if word_details:
#    print("{} of '{}':".format(property_to_fetch.capitalize(), selected_word))
#    print(", ".join(word_details))
#else:
#    print("No {} found for the word '{}'.".format(property_to_fetch, selected_word))