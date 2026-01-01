# Dzud and Drought, Assessing Climate Risk from Extreme Rainfall and Drought using Satellite Data

## Project Overview

This project investigates how extreme weather, specifically drought, dzud and extreme rainfall, creates climate risk in semi‑arid and arid regions. Using satellite derived precipitation data, reanalysis data and geospatial analysis in Python, the project applies percentile based and persistence based frameworks to evaluate climate extremes relative to local climatology.

The completed part of the analysis focuses on Chad during 2011, a year embedded within a multi year regional drought that led to severe food insecurity across the Sahel. Although national annual rainfall appeared near normal, this project demonstrates that seasonal timing, spatial heterogeneity, and persistence of dry conditions explain the severity of impacts. The continuation of the analysis will involve the analysis of Mongolia during 2009-2010, a 10 month time frame in which serious drought and low rainfall in the summer of 2009 set up for poor conditions going into the winter dzud that lasted well into 2010, resulting in serious food insecurity and mass migration to the urban centres by the rural subsistence farmers of Mongolia.

This repository is intended as a portfolio‑quality demonstration of applied climate data science and geospatial analysis.

**Note**:
Visual themes for all visualisations and figures was selected off of a single accent colour. This colour was chosen for personal consistency and as a reminder to of explaining concepts out loud to someone who may not have knowledge in the area.

## 2011 Chad
The climatological analysis of Chad in 2011 has been completed as of 29/12/2025

### Methods
This project combines temporal, seasonal, and spatial analyses:

**Historical Baseline**
- 29 year climatology (1981–2009) to represent pre drought conditions and provide context to the 2011 drought
- Annual and wet season rainfall distributions
- Anomalies, standardized z scores, and percentile thresholds

**Event Detection**
- Drought (local scale):
    7 day rolling mean
    10th percentile thresholds of rainfall in N'Djamena
- Drought (country scale):
    ≥7 consecutive days with rainfall < 1 mm per grid cell
    Persistence based definition suitable for semi arid climates
- Extreme rainfall:
    Daily precipitation above the 90th percentile per grid cell

**Spatial Analysis**
- Grid cell specific thresholds to account for strong climatic gradients
- Percentile normalization to enable comparison across desert, Sahelian, and tropical zones
- Representative drought and extreme rainfall days mapped across Chad

### Key Findings

**Annual Rainfall Is Misleading**  
National annual rainfall in 2011 was near the historical mean. This masks severe climate stress experienced on the ground.

**Wet‑Season Failure Explains the Crisis**  
June–September rainfall in the Sahel fell below the 10th percentile. 2011 ranks among the driest wet seasons in the historical  record.

**Drought and Flood Risk Co‑exist**  
Large portions of Chad experienced persistent drought. Localized regions simultaneously experienced extreme rainfall events.Highlights compound climate risk in semi arid regions.

**Spatial Perspective Is Essential**  
National averages hide regional extremes. Percentile spatial mapping reveals coherent drought patterns and localized rainfall extremes.

### Tools
Python, xarray, Pandas & GeoPandas, rioxarray, NumPy, Matplotlib, Seaborn

## 2009-2010 Mongolia
This notebook is still being worked upon.

## Mongolia Chad cross climate comparison and analysis
This notebook is still being worked upon.

## Planned Extensions
- Comparative case study in Mongolia and the Dzud of 2009-2010
- Cross regional comparison of drought and extreme rainfall patterns
- Summary statistics comparing climate risk profiles across regions


