from django.db import models
import json

class User(models.Model):
    UserID = models.AutoField(primary_key=True)
    Login = models.CharField(max_length=30)
    FullName = models.TextField()
    Password = models.CharField(max_length=30)
    RegistrationDate = models.DateField()
    Address = models.TextField()
    BirthDate = models.DateField(null=True)
    Residence = models.TextField()
    CVID = models.PositiveIntegerField(null=True)
    PortfolioID = models.PositiveIntegerField(null=True)
    IsAdmin = models.BooleanField(default=False)

class CVID(models.Model):
    CVID = models.AutoField(primary_key=True)
    ## Other
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)

class Appointement(models.Model):
    AppointementID = models.AutoField(primary_key=True)
    Time = models.DateTimeField()
    Place = models.TextField()
    Comment = models.TextField()
    Status = models.TextField() ## Gonna be something else I suppose
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)

class Portfolio(models.Model):
    PortfolioID = models.AutoField(primary_key=True)
    Data = models.TextField()
    UserID = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

class Goal(models.Model):
    GoalID = models.AutoField(primary_key=True)
    Deadline = models.DateField()
    Description = models.TextField()
    Status = models.TextField()
    UserID = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

class QuestionTip(models.Model):
    QuestionID = models.AutoField(primary_key=True)
    Text = models.TextField()
    IsAnonymous = models.BinaryField()
    Status = models.TextField()
    Time = models.DateTimeField()
    UserID = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

class Answer(models.Model):
    AnswerID = models.AutoField(primary_key=True)
    Text = models.TextField()
    Status = models.TextField()
    Time = models.DateTimeField()
    QuestionID = models.ForeignKey(QuestionTip, default=1, on_delete=models.CASCADE)
    UserID = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

class Faq(models.Model):
    QandAID = models.AutoField(primary_key=True)
    QuestionText = models.TextField()
    AnswerText = models.TextField()

