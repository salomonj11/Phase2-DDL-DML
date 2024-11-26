# TRY THIS QUERY
query5 = {
    "number_of_reviews": {"$lt": 500},
    "review_scores.review_scores_communication": {"$gte": 9}
}

# Update Your Projections
projection = {
    "_id": 1,
    "name": 1,
    "number_of_reviews": 1,
    "review_scores_communication": "$review_scores.review_scores_communication",
    "review_scores_checkin": "$review_scores.review_scores_checkin"
}

# Execute The Query
results = collection.find(query5, projection).sort("review_scores.review_scores_checkin", -1).sort("number_of_reviews", -1).limit(5)

# Print
print("Corrected Query 5 results:")
for document in results:
    print(document)





-------------------------- IF YOU WANNA KEEP YOUR OLD ONE TRY THIS --------------------------------------

# Access my database and collection
db = client['sample_airbnb']
collection = db['listingsAndReviews']

# Define my query 🧐
query5 = {
    "number_of_reviews": {"$lt": 500},
    "review_scores.review_scores_communication": {"$gte": 9}
}

# Define my projection 📖
projection = {
    "_id": 1,
    "name": 1,
    "number_of_reviews": 1,
    "review_scores_communication": "$review_scores.review_scores_communication",
    "review_scores_checkin": "$review_scores.review_scores_checkin" 
}

# Execute the query with sorting and limiting 🤔
results = collection.find(query5, projection).sort("review_scores.review_scores_checkin", -1).sort("number_of_reviews", -1).limit(5)

# Print the results aka we done! 🥳
print("Query 5 results:")
for document in results:
    print(document)
