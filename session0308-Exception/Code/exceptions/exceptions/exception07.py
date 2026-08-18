from abc import ABC, abstractmethod

from datetime import datetime

# -------------------------------
# User-Defined Exceptions
# -------------------------------
class PostNotFoundError(Exception):
    def __init__(self, post_id):
        self.post_id = post_id

    def __str__(self):
        return f"Post with ID {self.post_id} not found."


class InvalidContentError(Exception):
    def __str__(self):
        return "Title and content must not be empty."


# -------------------------------
# Abstract Base Class
# -------------------------------
class BlogEntity(ABC):
    @abstractmethod
    def display(self):
        pass


# -------------------------------
# Post Class (Inheritance)
# -------------------------------
class Post(BlogEntity):
    _id_counter = 1  # class variable

    def __init__(self, title: str, content: str, author: str, tags: set):
        if not title.strip() or not content.strip():
            raise InvalidContentError()
        self.id = Post._id_counter
        Post._id_counter += 1
        self.title = title
        self.content = content
        self.author = author
        self.created_at = datetime.now()
        self.tags = tags  # set
        self.comments = []  # list of tuples (username, comment)

    def add_comment(self, user: str, comment: str):
        self.comments.append((user, comment))

    def display(self):
        print(f"\n--- Post ID: {self.id} ---")
        print(f"Title   : {self.title}")
        print(f"Author  : {self.author}")
        print(f"Tags    : {', '.join(self.tags)}")
        print(f"Posted  : {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Content : {self.content}")
        if self.comments:
            print("\nComments:")
            for user, comment in self.comments:
                print(f"- {user}: {comment}")


# -------------------------------
# Blog Manager
# -------------------------------
class BlogApp:
    def __init__(self):
        self.posts = []  # list of Post objects
        self.users = set()
        self.post_lookup = {}  # dictionary: id -> Post

    def create_post(self, title, content, author, tags):
        tags_set = set(tag.strip() for tag in tags.split(",") if tag)
        post = Post(title, content, author, tags_set)
        self.posts.append(post)
        self.post_lookup[post.id] = post
        self.users.add(author)
        print(f"\nPost '{title}' created with ID {post.id}")

    def list_posts(self):
        if not self.posts:
            print("\nNo posts available.")
            return
        for post in self.posts:
            post.display()

    def find_post(self, post_id: int) -> Post:
        if post_id in self.post_lookup:
            return self.post_lookup[post_id]
        raise PostNotFoundError(post_id)

    def comment_on_post(self, post_id: int, username: str, comment: str):
        post = self.find_post(post_id)
        post.add_comment(username, comment)
        print(f"\nComment added by {username} on post ID {post_id}")
        self.users.add(username)

    def delete_post(self, post_id: int):
        post = self.find_post(post_id)
        self.posts.remove(post)
        del self.post_lookup[post_id]
        print(f"\nPost ID {post_id} deleted.")

    def display_stats(self):
        print("\nBlog Stats:")
        print(f"Total Posts  : {len(self.posts)}")
        print(f"Total Users  : {len(self.users)}")
        print(f"All Users    : {', '.join(sorted(self.users))}")


# -------------------------------
# Main Application
# -------------------------------
def main():
    app = BlogApp()

    while True:
        print("\n Blog Application Menu:")
        print("1. Create Post")
        print("2. View All Posts")
        print("3. Add Comment to Post")
        print("4. Delete Post")
        print("5. Blog Stats")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                title = input("Enter post title: ")
                content = input("Enter post content: ")
                author = input("Enter your name: ")
                tags = input("Enter tags (comma separated): ")
                app.create_post(title, content, author, tags)
            elif choice == 2:
                app.list_posts()
            elif choice == 3:
                post_id = int(input("Enter post ID to comment on: "))
                user = input("Your name: ")
                comment = input("Your comment: ")
                app.comment_on_post(post_id, user, comment)
            elif choice == 4:
                post_id = int(input("Enter post ID to delete: "))
                app.delete_post(post_id)
            elif choice == 5:
                app.display_stats()
            elif choice == 6:
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except (PostNotFoundError, InvalidContentError) as e:
            print("Exception:", e)


# -------------------------------
# Run the Application
# -------------------------------
if __name__ == "__main__":
    main()

