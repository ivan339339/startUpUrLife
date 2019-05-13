from django.db import models

class User(models.Model):
    UserID = models.AutoField(primary_key=True)
    Login = models.CharField(max_length=30)
    Password = models.CharField(max_length=30)
    RegistrationDate = models.DateField()

class Admin(models.Model):
    AdminID = models.ForeignKey(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=30)
    Role = models.CharField(max_length=30) ## As long as we dont have roles

class Customer(models.Model):
    CustomerID = models.ForeignKey(User, on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    Adress = models.TextField()
    Residence = models.TextField()
    CVID = models.PositiveIntegerField()
    PortfolioID = models.PositiveIntegerField()

class CVID(models.Model):
   CVID = models.AutoField(primary_key=True)
   ## Other
   CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Appointement(models.Model):
    AppointementID = models.AutoField(primary_key=True)
    TimeOfAppointement = models.DateTimeField()
    PlaceOfAppointement = models.TextField()
    Comment = models.TextField()
    Status = models.TextField() ## Gonna be something else I suppose
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Portfolio(models.Model):
    PortfolioID = models.AutoField(primary_key=True)
    ## Othert
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Goal(models.Model):
    GoalID = models.AutoField(primary_key=True)
    Deadline = models.DateField()
    Text = models.TextField()
    Status = models.TextField()
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)

class QuestionTip(models.Model):
    QuestionID = models.AutoField(primary_key=True)
    Text = models.TextField()
    IsAnonymous = models.BinaryField()
    Status = models.TextField()
    Time = models.DateTimeField()
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Answer(models.Model):
    AnswerID = models.AutoField(primary_key=True)
    Text = models.TextField()
    Status = models.TextField()
    Time = models.DateTimeField()
    QuestionID = models.ForeignKey(QuestionTip, on_delete=models.CASCADE)
    AdminID = models.ForeignKey(Admin, on_delete=models.CASCADE)

class Faq(models.Model):
    QandAID = models.AutoField(primary_key=True)
    QuestionText = models.TextField()
    AnswerText = models.TextField()

