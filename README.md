California 14ers Data Analysis

A data science project analyzing California's 15 highest peaks over 14,000 feet. Built with Python to explore elevation patterns, climbing difficulty, and route characteristics.

About the Dataset

This project examines California's "14ers", peaks exceeding 14,000 feet elevation. The dataset includes 15 peaks with 11 attributes each, sourced from Peakbagger/SummitPost/MountainProject

Data Fields:
- Peak name, elevation, and mountain range
- Climbing difficulty (YDS Class 1-5) 
- Route distance and elevation gain
- Geographic coordinates
- Best climbing months
- Topographic prominence


Breaking this into multiple development stages:

Stage 1: Data Setup (Complete)
- Raw data collection and DataFrame creation
- Data validation and type conversion

Stage 2: Statistical Analysis (Next)
- Basic statistics and breakdowns by range/difficulty
- Prominence and route analysis  

Stage 3: Advanced Analytics (Planned)
- Correlation studies and climbing recommendations

Stage 4: Visualizations (Planned) 
- Charts, maps, and dashboard creation

Stage 5: Final Insights (Planned)
- Seasonal analysis and route optimization

Current Progress

Stage 1 is complete with a working pandas DataFrame containing all 15 peaks. Basic validation shows:

- Elevation range: 14,003 to 14,499 feet
- 13 peaks in Sierra Nevada, 2 in other ranges  
- Difficulty spread from Class 1 (hiking) to Class 5 (technical climbing) (Yosemite Decimal System)
- Route distances for all peaks

Tech Stack

- Python with pandas for data handling
- matplotlib and seaborn for visualization
- Standard data science workflow

Usage

bash
pip install pandas matplotlib seaborn
python stage1_data_setup.py

Next Steps

Working on statistical breakdowns and starting visualization development. Will add interactive elements and geographic mapping in later stages.
