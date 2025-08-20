# function that returns the average rating of all reviews of a specific book
def average_rating(rating_list):
    if not rating_list:
        return 0
    
    return round(sum(rating_list) / len(rating_list))