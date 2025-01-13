user_profile = {
    'name': 'Alice Smith',
    'preferences': {
        'language': ['English', 'Japanese'],
        'notifications': True,
    }
}

print(user_profile["preferences"])
print(user_profile["preferences"]["language"])
print(user_profile["preferences"]["language"][0])