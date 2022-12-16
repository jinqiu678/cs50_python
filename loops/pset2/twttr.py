tweet = input("Input: ")
new_tweet = ""
for i in tweet:
    if i not in ['a', 'e', 'i', 'o', 'u']:
        new_tweet = new_tweet + i

print("Output:", new_tweet)