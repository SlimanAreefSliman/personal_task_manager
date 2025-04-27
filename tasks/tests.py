from django.test import TestCase
from django.contrib.auth.models import User
from .models import Category, Task, Subtask

class TaskModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.category = Category.objects.create(name='Work', owner=self.user)

    def test_category_creation(self):
        category = Category.objects.get(name='Work')
        self.assertEqual(category.owner, self.user)
        self.assertEqual(str(category), 'Work')

    def test_task_creation(self):
        task = Task.objects.create(
            title='Test Task',
            description='Test Description',
            status='TODO',
            priority='MEDIUM',
            owner=self.user,
            category=self.category
        )
        self.assertEqual(task.title, 'Test Task')
        self.assertEqual(task.owner, self.user)
        self.assertEqual(task.category, self.category)
        self.assertEqual(str(task), 'Test Task')

    def test_subtask_creation(self):
        task = Task.objects.create(
            title='Parent Task',
            owner=self.user,
            category=self.category
        )
        subtask = Subtask.objects.create(
            title='Test Subtask',
            status='TODO',
            parent_task=task,
            owner=self.user
        )
        self.assertEqual(subtask.title, 'Test Subtask')
        self.assertEqual(subtask.parent_task, task)
        self.assertEqual(subtask.owner, self.user)
        self.assertEqual(str(subtask), 'Test Subtask')
