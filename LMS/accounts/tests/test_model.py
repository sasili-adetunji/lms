from .base import AuthBaseTest


class UserProfileTest(AuthBaseTest):
    """
    Test User Profile model
    """

    def test_user_profile(self):
        # test if the profile created in the setup exists
        self.assertEqual(self.user.username, 'test_user')
