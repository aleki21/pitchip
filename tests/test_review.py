
import unittest
from app.models import Comment, User
from app import db

class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.user_James = User(username = 'Tester',password = 'password', email = 'tester@gmail.com')
        self.new_comment = Comment(pitch_id=12345,pitch_title='Comment test',comment='This is a test comment',user = self.user_Tester)


    def tearDown(self):
            Comment.query.delete()
            User.query.delete()

    def test_check_instance_variables(self):
            self.assertEquals(self.new_comment.pitch_id,11111)
            self.assertEquals(self.new_comment.pitch_title,'Comment test')
            self.assertEquals(self.new_comment.movie_comment,'This is a test comment')
            self.assertEquals(self.new_comment.user,self.user_Tester)

    def test_save_comment(self):
            self.new_comment.save_comment()
            self.assertTrue(len(Comment.query.all())>0)

    def test_get_comment_by_id(self):

            self.new_comment.save_comment()
            got_comments = Comment.get_comments(11111)
            self.assertTrue(len(got_comments) == 1)