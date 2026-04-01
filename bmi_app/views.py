from django.shortcuts import render
from .models import BmiBerekening

def bmi_berekenen(request):
    bmi_waarde = None
    categorie = None

    if request.method == 'POST':
        gewicht = float(request.POST['gewicht'])
        lengte = float(request.POST['lengte'])

        bmi_waarde = gewicht / (lengte * lengte)
        bmi_waarde = round(bmi_waarde, 2)

        if bmi_waarde < 18.5:
            categorie = "Ondergewicht"
        elif bmi_waarde < 25:
            categorie = "Normaal gewicht"
        elif bmi_waarde < 30:
            categorie = "Overgewicht"
        else:
            categorie = "Obesitas"

        BmiBerekening.objects.create(
            gewicht=gewicht,
            lengte=lengte,
            bmi_waarde=bmi_waarde,
            categorie=categorie
        )

    # Geschiedenis: alle berekeningen ophalen uit de database
    geschiedenis = BmiBerekening.objects.all().order_by('-datum')

    return render(request, 'bmi.html', {
        'bmi_waarde': bmi_waarde,
        'categorie': categorie,
        'geschiedenis': geschiedenis,   # ← nieuw!
    })
