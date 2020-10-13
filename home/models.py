from django.db import models

# AGES = (
#     0, "Select",
#     1, "Below 18",
#     2, "Above 18 and below 30",
#     3, "Above 30 and Below 50",
#     4, "Above 50"
# )

GENDER = (
    (0, "Select"),
    (1, "Male"),
    (2, "Female"),
    (3, "Rather")
)


class Questionnaire(models.Model):
    name = models.CharField(max_length=200)
    gender = models.IntegerField(choices=GENDER, default=0)
    age = models.IntegerField()
    location = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
