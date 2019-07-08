from django.db import models

class User(models.Model):
    UserID = models.AutoField(primary_key=True)
    Login = models.CharField(max_length=30)
    FullName = models.TextField()
    Password = models.CharField(max_length=30)
    RegistrationDate = models.DateField()
    Address = models.TextField()
    BirthDate = models.DateField(null=True)
    Residence = models.TextField()
    PortfolioID = models.PositiveIntegerField(null=True)

    def __str__(self):
        return str(self.FullName)

class Appointement(models.Model):
    AppointementID = models.AutoField(primary_key=True)
    Title = models.TextField()
    Time = models.DateTimeField()
    Place = models.TextField()
    Comment = models.TextField()
    Status = models.TextField()
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        user = User.objects.all().filter(UserID=self.UserID.UserID).first()
        return str(self.Title) + ', ' + str(user)

class Portfolio(models.Model):
    PortfolioID = models.AutoField(primary_key=True)
    Title = models.TextField(null=True)
    Text = models.TextField(null=True)
    UserID = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

class Goal(models.Model):
    GoalID = models.AutoField(primary_key=True)
    Title = models.TextField()
    Deadline = models.DateField()
    Description = models.TextField()
    Status = models.TextField()
    UserID = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def __str__(self):
        user = User.objects.all().filter(UserID=self.UserID.UserID).first()
        return str(self.Title) + ", " + str(user)

class Help(models.Model):
    HelpID = models.AutoField(primary_key=True)
    Email = models.TextField()
    Question = models.TextField()
    UserID = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Question)

class Faq(models.Model):
    QandAID = models.AutoField(primary_key=True)
    QuestionText = models.TextField()
    AnswerText = models.TextField()

