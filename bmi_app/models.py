from django.db import models

# Dit is onze tabel in de SQLite database
class BmiBerekening(models.Model):
    gewicht = models.FloatField()                    # Input 1
    lengte = models.FloatField()                     # Input 2
    bmi_waarde = models.FloatField()                 # Output 1
    categorie = models.CharField(max_length=50)      # Output 2
    datum = models.DateTimeField(auto_now_add=True)  # Automatisch datum

    def __str__(self):
        return f"BMI {self.bmi_waarde} - {self.categorie}"