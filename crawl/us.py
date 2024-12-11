import pandas as pd
from dotenv import load_dotenv
import os
from census import Census

# Load environment variables from .env file
load_dotenv()

# Access the API key
API_KEY = os.getenv("CENSUS_API_KEY")

# Years for decennial census
years = [2000, 2010, 2020, 2021]

# Store results
data = []

print(API_KEY)

dsource = "pep"
dname = "population"

state = "39"  # Ohio
county = "*"

c = Census(API_KEY)

for year in years:
    base_url = f"https://api.census.gov/data/{year}/{dsource}/{dname}"
    # cols = [i + "_" + str(year) for i in ["DENSITY", "POP"]]
    # params = {
    #     "get": ",".join(cols),
    #     "for": f"county:{county}" f"&in=state:{state}",
    #     "key": API_KEY,
    # }
    # print(base_url)
    # response = requests.get(base_url, params=params)
    # va_census = c.acs5.state_county_tract(
    #     fields=["NAME", "B01001_001E", "B01001_002E", "B01001_026E"],
    #     state_fips=state,
    #     county_fips="*",
    #     tract="*",
    #     year=year,
    # )
    pop_census = c.sf1.state_county_tract(
        fields=["NAME", "P001001", "P003002", "P003003"],
        state_fips=state,
        county_fips="*",
        tract="*",
        year=year,
    )
    print(pop_census)
    # print(va_census)
# Create a DataFrame
print(data)
# df = pd.DataFrame(data, columns=["Population", "State", "Year"])
# df["Year"] = years
# print(df)
