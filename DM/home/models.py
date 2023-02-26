from django.db import models

# Create your models here.


class mentor(models.Model):
    mentor_name=models.CharField(max_length=20,primary_key=True,unique=True)
    mentor_email=models.CharField(max_length=40)
    mentor_password=models.CharField(max_length=20)

    def __str__(self):
        return self.mentor_name
    
    

class mentee(models.Model):
    mentee_name=models.CharField(max_length=100)
    mentor_name=models.ForeignKey(mentor,on_delete=models.CASCADE)
   #mentor_id=models.ForeignKey(mentor,on_delete=models.CASCADE)

    def __str__(self):
        return self.mentee_name

   



class UserType(models.Model):
    user=models.CharField(max_length=100)
    type=models.CharField(max_length=100)


class menteelist(models.Model):
    mentee_name=models.CharField(max_length=100)
    mentee_email=models.CharField(max_length=100)
    mentee_password=models.CharField(max_length=100)
    mentee_dob=models.CharField(max_length=15,default="dd/mm/yyyy")
    mentee_age=models.IntegerField(default=0)
    mentee_bg=models.CharField(max_length=5,default="0")
    mentee_relegion=models.CharField(max_length=10,default="0")
    mentee_caste=models.CharField(max_length=10,default="0")
    mentee_parish=models.CharField(max_length=20,default="Nil")
    mentee_paddress=models.CharField(max_length=200,default="0")
    mentee_caddress=models.CharField(max_length=200,default="0")
    mentee_mob=models.IntegerField(default=0)
    mentee_tel=models.IntegerField(default=0)
    father_name=models.CharField(max_length=20,default="0")
    father_profession=models.CharField(max_length=20,default="0")
    father_age=models.IntegerField(default=0)
    father_placeofwork=models.CharField(max_length=10,default="0")
    father_mob=models.IntegerField(default=0)
    mother_name=models.CharField(max_length=20,default="0")
    mother_profession=models.CharField(max_length=20,default='0')
    mother_age=models.IntegerField(default=0)
    mother_placeofwork=models.CharField(max_length=10,default='0')
    mother_mob=models.IntegerField(default=0)
    brother_or_sister_std=models.CharField(max_length=20,default="Nil")
    position_in_family=models.CharField(max_length=10,default='0')
    local_guardian_name=models.CharField(max_length=20,default='0')
    local_guardian_profession=models.CharField(max_length=20,default='0')
    local_guardian_age=models.IntegerField(default=0)
    local_guardian_mob=models.IntegerField(default=0)
    local_guardian_address=models.CharField(max_length=100,default='0')
    hostelornot=models.CharField(max_length=5,default='0')
    if_hostel_freqencyvisithome=models.CharField(max_length=15,default='0')
    mode_of_convayence=models.CharField(max_length=20,default='0')
    entrance_rank=models.IntegerField(default=0)
    work_experience=models.CharField(max_length=50,default='0')
    extra_curricular=models.CharField(max_length=50,default='0')
    language_proficiency=models.CharField(max_length=50,default='0')
    other_acheivements=models.CharField(max_length=50,default='0')
    personal_goal=models.CharField(max_length=20,default='0')
    professional_goal=models.CharField(max_length=20,default='0')
    social_goal=models.CharField(max_length=10,default='0')
    strength=models.CharField(max_length=30,default='0')
    weakness=models.CharField(max_length=30,default='0')
    oppertunity=models.CharField(max_length=50,default='0')
    threats=models.CharField(max_length=25,default='0')
    hobbies=models.CharField(max_length=25,default='0')
    rolemodel=models.CharField(max_length=100,default='0')
    first_impression=models.CharField(max_length=20,default='0')
    source_of_income=models.CharField(max_length=20,default='0')
    Economic_background=models.CharField(max_length=20,default="Fine")
    perental_harmony=models.CharField(max_length=50,default='0')
    relationship_with_family=models.CharField(max_length=25,default='0')
    atmosphere_at_home_for_study=models.CharField(max_length=25,default="good")
    relegious_life=models.CharField(max_length=20,default='0')
    social_outlook=models.CharField(max_length=20,default='0')
    read_habit=models.CharField(max_length=20,default='0')
    behaviour=models.CharField(max_length=20,default="good")
    potential=models.CharField(max_length=20,default='0')
    weakness_of_mentee=models.CharField(max_length=25,default='0')
    adjustment_to_college=models.CharField(max_length=25,default="good")
    addiction=models.CharField(max_length=25,default="Nil")
    improvement_area=models.CharField(max_length=20,default='0')
    specific_concern=models.CharField(max_length=20,default='0')
    referal_to_language_lab=models.CharField(max_length=10,default='0')
    fitness_for_MCA=models.CharField(max_length=20,default='0')
    life_goals=models.CharField(max_length=20,default='0')
    core_competency=models.CharField(max_length=20,default="Nil")
    intercollege_representation=models.CharField(max_length=200,default='0')


class assignment(models.Model):
    Book_name=models.CharField(max_length=100)
    mentee_name=models.ForeignKey(mentee,on_delete=models.CASCADE)
    mentor_name=models.ForeignKey(mentor,on_delete=models.CASCADE)
    feedback=models.CharField(max_length=250)

class accommodation(models.Model):
    mentee_name=models.ForeignKey(mentee,on_delete=models.CASCADE)
    hostel_duration=models.DurationField()
    Reason_for_stay=models.CharField(max_length=250)
    stay_by_sjcet_or_not=models.CharField(max_length=10)
    Details=models.CharField(max_length=250)

class academicqualification(models.Model):
    mentee_name=models.ForeignKey(mentee,on_delete=models.CASCADE)
    qualification=models.CharField(max_length=50)
    college_name=models.CharField(max_length=200)
    university_name=models.CharField(max_length=50)
    mark=models.IntegerField()
    medium_of_instruction=models.CharField(max_length=50)

class counselling(models.Model):
    mentee_name=models.ForeignKey(mentee,on_delete=models.CASCADE)
    mentor_name=models.ForeignKey(mentor,on_delete=models.CASCADE)
    time=models.TimeField()
    suggestion=models.CharField(max_length=250)
    technical_assessment=models.CharField(max_length=200)
    interpersonal_assessment=models.CharField(max_length=200)
    communication_assessment=models.CharField(max_length=200)
    leadership_assessment=models.CharField(max_length=200)
    improvement_suggestion=models.CharField(max_length=200)
  

