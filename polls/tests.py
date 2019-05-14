from django.test import TestCase
from django.utils import timezone

from .models import Question
import datetime
# Create your tests here.


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently()가 pub_date를 가진 질문에 대해 False를 반환함

        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)

        """
        assertIs() 메소드를 사용하여 False가 반환되기를 바랬지만 
        was_published_recently() 가 True를 반환한다
        """
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently ()는 pub_date의 질문에 대해 False를 반환합니다
        1일 이상
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently ()는 pub_date의 질문에 대해 True를 반환합니다.
        마지막날
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)