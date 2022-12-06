import datetime


class user:
    def __init__(self, name):
        self.name = name
        self.last_logged_in_at = None
        self.is_logged_in = False

    def name(self):
        return self.name

    def name(self, value):
        self.name = value

    def is_logged_in(self):
        return self.is_logged_in

    def last_logged_in_at(self):
        return self.last_logged_in_at

    def log_in(self):
      self.is_logged_in = False
      self.last_logged_in_at = datetime.datetime.now()

    def log_out(self):
        self.is_logged_in = False

    def can_edit(self, comment):
        return comment.author == self

    def can_delete(self, comment):
        return False

    def to_string(self):
        return self.name


class moderator(user):
    def __init__(self, name):
        user.__init__(self, name)

    def can_delete(self, comment):
        return True


class admin(moderator):
    def __init__(self, name):
        moderator.__init__(self, name)

    def can_edit(self, comment):
        return True


class comment:
    def __init__(self, author, message, replied_to=None):
        self.author = author
        self.message = message
        self.replied_to = replied_to
        self.created_at = datetime.datetime.now()

    def author(self):
        return self.author

    def author(self, value):
        self.author = value

    def message(self):
        return self.message

    def message(self, value):
        self.message = value

    def created_at(self):
        return self.created_at

    def replied_to(self):
        return self.replied_to

    def replied_to(self, value):
        self.replied_to = value

    def to_string(self):
        if self.replied_to:
            return self.message + " by " + self.author.name + " \
            (replied to " +  self.replied_to.author.name + ")"
        else:
            self.message + " by " + self.author.name

import unittest

user1 = user('User 1')
mod = moderator('Moderator')

class Test(unittest.TestCase):
  def test_instantiation(self):
    self.assertEqual(user1.name,'User 1', 'User name is set correctly')
    user1.name = 'User 1 Updated'
    self.assertEqual(user1.name,'User 1 Updated', 'User name can be updated')
    self.assertIsInstance(mod, user, 'Moderator is a user')            


'''
  Instructions

   Object Oriented Tests
      For this challenge, you are going to build a mock comments section.

  Design
      We're going to focus on two aspects:

  Users
      Users come in 3 flavors, normal users, moderators, and admins. Normal users can only create new comments, and edit the their own comments. Moderators have the added ability to delete comments (to remove trolls), while admins have the ability to edit or delete any comment.
      Users can log in and out, and we track when they last logged in
  Comments
      Comments are simply a message, a timestamp, and the author.
      Comments can also be a reply, so we'll store what the parent comment was.

  Your Challenge
      This is challenge is not about building a fully functional API, but more about focusing on the design from an object-oriented point-of-view.

  We've provided the basic API (which is incomplete), which we would like you to complete being aware of the following Object-Oriented Programming concepts:

  Encapsulation of Properties
      All classes should have no publicly accessible fields
      You should make sure you at least "hide" the required fields, for example, using _name instead of _name. Alternatively, feel free to use a better solution as extra credit.
      The method-based API is provided. These must be completed as-is.
      Additional methods are allowed, though remember to keep read-only properties read-only.
  Instantiation
      Classes should be instantiated with properties (as provided), to create instances with values already assigned.
  User/Moderator/Admin defaults:
      Should be marked as not logged in
      Should return None for the last logged in at property
  Comment defaults:
      Should set the current timestamp for the created at property upon instantiation
      Replied To is optional, and should be None if not provided.

  Inheritance & Access Control
  Note: for the sake of simplicity, you can simply treat object equality as "equal", though more complete solutions will also pass.

  User
      Users can be logged in and out.
      When logging in, set the last_logged_in_at timestamp. Do not modify this timestamp when logging out
      Users can only edit their own comments
      Users cannot delete any comments
  Moderator is a User
      Moderators can only edit their own comments
      Moderators can delete any comments
  Admin is both a User and a Moderator
      Admins can edit any comments
      Admins can delete any comments
  Composition
      Comments contain a reference to the User who created it (author)
      Comments optionally contain a reference to another comment (replied_to)

  When converting to a string (to_string), the following format is used:
      No replied to:
          message + " by " + author.name
      With replied to:
          message + " by " + author.name + " (replied to " + repliedTo.author.name + ")"
  Beyond these basics, you are free to add to the API, but only these concepts will be scored automatically.

  '''
