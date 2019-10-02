from locust import TaskSet, task, HttpLocust


class PostsTasks(TaskSet):

    def on_start(self):
        print("login example")

    def on_stop(self):
        print("logout example")

    @task
    def get_posts(self):
        self.client.get("/posts/")

    @task
    def get_posts_id(self):
        self.client.get("/posts/1")

    @task
    def post_posts(self):
        self.client.post(
            "/posts/", {"title": "API Testing", "body": "Example testing API with Locust"})


class ApiUser(HttpLocust):
    host = "https://jsonplaceholder.typicode.com"
    min_wait = 1000
    max_wait = 3000
    task_set = PostsTasks
