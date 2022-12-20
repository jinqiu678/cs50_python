def main():
    tweet = input("Input: ")
    shorten(tweet)

    
def shorten(tweet):
    new_tweet = ""
    for i in tweet:
        if i not in ['a', 'e', 'i', 
        'o', 'u', 'A', 'E',
        'I', 'O', 'U']:
            new_tweet = new_tweet + i
    return new_tweet

if __name__ == "__main__":
    main()