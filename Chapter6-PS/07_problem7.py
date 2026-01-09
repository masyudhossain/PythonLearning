#Write a program to find out whether a given post is talking about “Masyud” or not.
post = input("Enter the post: ")

if("Masyud".lower() in post.lower()):
    print("This post is talking about Masyud")

else:
    print("This post is not talking about Masyud")