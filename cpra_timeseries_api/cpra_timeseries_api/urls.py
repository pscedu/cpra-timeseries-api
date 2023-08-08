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
from cpra_timeseries_api_app.views import block_group, clara, ecoregion, extraction_point, hydro_compartment, parish

block_group_urls = [
    # TODO: Communicate with Eric/Heather about the entries here.
    # path('block_group/decadal/population_change/',
    #      block_group.BlockGroupDecadalPopulationChangeTimeSeriesView.as_view(),
    #      name="block_group_decadal_population_change"),
]

clara_urls = [
    path('clara/decadal/eadd/', clara.ClaraDecadalEADDTimeSeriesView.as_view(), name="clara_decadal_eadd"),
    path('clara/decadal/nseadd/', clara.ClaraDecadalNSEADDTimeSeriesView.as_view(), name="clara_decadal_nseadd"),
    path('clara/decadal/easd/', clara.ClaraDecadalEASDTimeSeriesView.as_view(), name="clara_decadal_easd"),
    path('clara/decadal/nseasd/', clara.ClaraDecadalNSEASDTimeSeriesView.as_view(), name="clara_decadal_nseasd"),
    path('clara/decadal/damage/', clara.ClaraDecadalDamageTimeSeriesView.as_view(), name="clara_decadal_damage"),
    path('clara/decadal/exposure_asset_count/',
         clara.ClaraDecadalExposureAssetCountTimeSeriesView.as_view(),
         name="clara_decadal_exposure_asset_count"),
    path('clara/decadal/exposure_critical_infrastructure_count/',
         clara.ClaraDecadalExposureCriticalInfrastructureCountTimeSeriesView.as_view(),
         name="clara_decadal_exposure_critical_infrastructure_count"),
    path('clara/decadal/exposure_historical_properties_count/',
         clara.ClaraDecadalExposureHistoricPropertiesCountTimeSeriesView.as_view(),
         name="clara_decadal_exposure_historical_properties_count"),
]

ecoregion_urls = [
    path('ecoregion/annual/land_area/', ecoregion.EcoregionAnnualLandAreaTimeSeriesView.as_view(),
         name="ecoregion_annual_land_area"),
    path('ecoregion/annual/vegetation_coverage_area/',
         ecoregion.EcoregionAnnualVegetationCoverageAreaTimeSeriesView.as_view(),
         name="ecoregion_annual_vegetation_coverage_area"),
    path('ecoregion/annual/habitat_suitability_unit/',
         ecoregion.EcoregionAnnualHabitatSuitabilityUnitTimeSeriesView.as_view(),
         name="ecoregion_annual_habitat_suitability_unit"),
]

hydro_compartment_urls = [
    path('hydro_compartment/decadal/elevation_exceedance/',
         hydro_compartment.HydroCompartmentDecadalElevationExceedance.as_view(),
         name="hydro_compartment_decadal_elevation_exceedance"),
    path('hydro_compartment/decadal/elevation_storm/',
         hydro_compartment.HydroCompartmentDecadalElevationStorm.as_view(),
         name="hydro_compartment_decadal_elevation_storm"),
    path('hydro_compartment/decadal/wave_height_exceedance/',
         hydro_compartment.HydroCompartmentDecadalWaveHeightExceedance.as_view(),
         name="hydro_compartment_decadal_wave_height_exceedance"),
    path('hydro_compartment/decadal/wave_height_storm/',
         hydro_compartment.HydroCompartmentDecadalWaveHeightStorm.as_view(),
         name="hydro_compartment_decadal_wave_height_storm"),
    path('hydro_compartment/annual/salinity_mean/',
         hydro_compartment.HydroCompartmentAnnualSalinityMeanTimeSeriesView.as_view(),
         name="hydro_compartment_annual_salinity_mean"),
    path('hydro_compartment/annual/salinity_two_week_max/',
         hydro_compartment.HydroCompartmentAnnualSalinityTwoWeekMaxTimeSeriesView.as_view(),
         name="hydro_compartment_annual_salinity_two_week_max"),
    path('hydro_compartment/annual/water_level_mean/',
         hydro_compartment.HydroCompartmentAnnualWaterLevelMeanTimeSeriesView.as_view(),
         name="hydro_compartment_annual_water_level_mean"),
    path('hydro_compartment/annual/tss_mean/',
         hydro_compartment.HydroCompartmentAnnualTSSMeanTimeSeriesView.as_view(),
         name="hydro_compartment_annual_tss_mean"),
    path('hydro_compartment/annual/land_area/',
         hydro_compartment.HydroCompartmentAnnualLandAreaTimeSeriesView.as_view(),
         name="hydro_compartment_annual_land_area"),
    path('hydro_compartment/annual/tidal_range/',
         hydro_compartment.HydroCompartmentAnnualTidalRangeTimeSeriesView.as_view(),
         name="hydro_compartment_annual_tidal_range"),
    path('hydro_compartment/daily/salinity_mean/',
         hydro_compartment.HydroCompartmentDailySalinityMeanTimeSeriesView.as_view(),
         name="hydro_compartment_daily_salinity_mean"),
    path('hydro_compartment/daily/water_level_mean/',
         hydro_compartment.HydroCompartmentDailyWaterLevelMeanTimeSeriesView.as_view(),
         name="hydro_compartment_daily_water_level_mean"),
    path('hydro_compartment/daily/tss_mean/',
         hydro_compartment.HydroCompartmentDailyTSSMeanTimeSeriesView.as_view(),
         name="hydro_compartment_daily_tss_mean"),
    path('hydro_compartment/daily/temperature/',
         hydro_compartment.HydroCompartmentDailyTemperatureTimeSeriesView.as_view(),
         name="hydro_compartment_daily_temperature"),
    path('hydro_compartment/daily/tidal_range/',
         hydro_compartment.HydroCompartmentDailyTidalRangeTimeSeriesView.as_view(),
         name="hydro_compartment_daily_tidal_range"),
]

parish_urls = [
    path('parish/decadal/population/', parish.ParishDecadalPopulationTimeSeriesView.as_view(),
         name="parish_decadal_population"),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    *block_group_urls,
    *clara_urls,
    *ecoregion_urls,
    *hydro_compartment_urls,
    *parish_urls,
]
