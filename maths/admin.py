from django.contrib import admin

from .models import MathHighScore, AdvMathScore, SimpleMathScore


admin.site.register(MathHighScore)
admin.site.register(AdvMathScore)
admin.site.register(SimpleMathScore)
