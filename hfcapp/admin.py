from django.contrib import admin
from .models import Transformationimg
from .models import gellaryimg
from .models import Resultsimg
from .models import Rewardsimg
from .models import Packages
from .models import morePackages
from .models import Orders

# Register your models here.
admin.site.register(Transformationimg)
admin.site.register(gellaryimg)
admin.site.register(Rewardsimg)
admin.site.register(Resultsimg)
admin.site.register(Packages)
admin.site.register(morePackages)
admin.site.register(Orders)

