from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class User(models.Model):
    Username = models.CharField(null=False,unique=True,max_length=200, default="##")
    first_name=models.CharField(null=False,max_length=200)
    last_name=models.CharField(null=True,max_length=200)
    
    
    def __str__(self):
        return str(self.first_name)
    

class Hackathon(models.Model):
    
    CHOICES = [
        ('Image', 'Image'),
        ('File', 'File'),
        ('Link', 'Link'),
        
    ]
    title=models.CharField(null=False,max_length=200)
    description=models.TextField(null=True)
    background_image=models.ImageField(
        verbose_name='background image',
        upload_to="background_img/",
        null=True,
        blank=True,
    )
    Hackathon_image = models.ImageField(
        verbose_name='background image',
        upload_to="background_img/",
        null=True,
        blank=True,
    )
    type_os_sub = models.CharField(max_length=10, choices=CHOICES, default="Text")
    start_date=models.DateField()
    end_date=models.DateField()
    reward_price=models.FloatField()

    def __str__(self):
        res=str(self.id)+self.title
        return str(res)
    
class Reistration(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    hackathon_id = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    registration_date = models.DateField(null=True)
    
    def __str__(self):
        
        return str(self.id)
    
class Submission(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    hackathon_id = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    submission_name=models.CharField(null=False,max_length=400)
    summary=models.TextField(null=False,default=" ")
    Submission_image = models.ImageField(
        verbose_name='submission image',
        upload_to="submission/",
        null=True,
        blank=True,
    )
    submission_link=models.CharField( max_length=400,null=True,blank=True)
    
    def clean(self):
        super().clean()
        if self.Submission_image and self.submission_link:
            raise ValidationError(
                'Only one of Submission image or submission link can be provided')
        elif not self.Submission_image and not self.submission_link:
            raise ValidationError(
                'Either Submission image or submission link must be provided')

        # Check the value of type_os_sub in the related Hackathon
        if self.hackathon_id.type_os_sub == 'Image' and not self.Submission_image:
            raise ValidationError(
                'Submission image is required for this hackathon type')
        elif self.hackathon_id.type_os_sub == 'Link' and not self.submission_link:
            raise ValidationError(
                'Submission link is required for this hackathon type')
            
    
    
    def __str__(self):
        return str(self.id)
    
    
    
    
    
