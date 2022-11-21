from django.db import models


class Data(models.Model):
    start_point = models.PositiveIntegerField(verbose_name="Start Point",default=0)
    end_point = models.PositiveIntegerField(verbose_name="End Point",default=0)
    string = models.CharField(max_length=100,verbose_name="String")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Createed Date Time")
    
    def __str__(self) -> str:
        return self.pk
    class Meta:
        ordering = ["-created_at"]
        

    