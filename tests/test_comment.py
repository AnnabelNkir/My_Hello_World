import unittest
from app.models import Post, User, Comment

class TestPost(unittest.TestCase):
    
    def setUp(self):
        self.user_Collins = User(first_name = "Annabel",
                                last_name = "Micheni",
                                username = "AnnabelNkir",
                                password = "easy",
                                email = "pitchybellah@mail.com")
        self.new_post = Post(post_title = "Sample Title",
                            post_content = "Hey you!",
                            user_id = self.user_Annabel.id)
        self.new_comment = Comment(comment = "Nice job",
                                    post_id = self.new_post.id,
                                    user_id = self.user_Collins.id)

    def test_instance(self):
        self.assertTrue(isinstance(self.user_Annabel, User))
        self.assertTrue(isinstance(self.new_post, Post))
        self.assertTrue(isinstance(self.new_comment, Comment))