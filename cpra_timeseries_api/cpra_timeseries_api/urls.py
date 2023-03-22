"""cpra_timeseries_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cpra_timeseries_api_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ecoregion/annual/land_area/', views.EcoregionAnnualLandAreaTimeSeriesView.as_view(), name="ecoregion_annual_land_area"),
    path('ecoregion/annual/vegetation_coverage_area/', views.EcoregionAnnualVegetationCoverageAreaTimeSeriesView.as_view(), name="ecoregion_annual_vegetation_coverage_area"),
    path('ecoregion/annual/habitat_suitability_unit/', views.EcoregionAnnualHabitatSuitabilityUnitTimeSeriesView.as_view(), name="ecoregion_annual_habitat_suitability_unti"),
    path('clara/decadal/eadd/', views.ClaraDecadalEADDTimeSeriesView.as_view(), name="clara_decadal_eadd"),
    path('clara/decadal/easd/', views.ClaraDecadalEASDTimeSeriesView.as_view(), name="clara_decadal_easd")
]
