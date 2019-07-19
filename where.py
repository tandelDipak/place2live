# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_csv("city/output/list_of_countries.csv")

your_country = input("What is your country? ")
your_country = your_country.lower()
your_country = your_country.capitalize()

your_purchasing_power_index = float(
    df[df.country == your_country]["purchasing_power_index"]
)
print(f"In your country purchasing power index is {your_purchasing_power_index}")
your_purchasing_power_index = (
    float(input("What is your desirable purchasing power index (higher is better)? "))
    or your_purchasing_power_index
)

your_safety_index = float(df[df.country == your_country]["safety_index"])
print(f"In your country safety index is {your_safety_index}")
your_safety_index = (
    float(input("What is your desirable safety index (higher is better)? "))
    or your_safety_index
)

your_health_care_index = float(df[df.country == your_country]["health_care_index"])
print(f"In your country health care index is {your_health_care_index}")
your_health_care_index = (
    float(input("What is your desirable health care index (higher is better)? "))
    or your_health_care_index
)

your_climate_index = float(df[df.country == your_country]["climate_index"])
print(f"In your country climate index is {your_climate_index}")
your_climate_index = (
    float(input("What is your desirable climate index (higher is better)? "))
    or your_climate_index
)

your_cost_of_living_index = float(
    df[df.country == your_country]["cost_of_living_index"]
)
print(f"In your country cost of living index is {your_cost_of_living_index}")
your_cost_of_living_index = (
    float(input("What is your desirable cost of living index (lower is better)? "))
    or your_cost_of_living_index
)

your_property_price_to_income_ratio = float(
    df[df.country == your_country]["property_price_to_income_ratio"]
)
print(
    f"In your country house "
    f"price to income ratio index is {your_property_price_to_income_ratio}"
)
your_property_price_to_income_ratio = (
    float(
        input("What is your desirable house price to income ratio (lower is better)? ")
    )
    or your_property_price_to_income_ratio
)

your_traffic_commute_time_index = float(
    df[df.country == your_country]["traffic_commute_time_index"]
)
print(
    f"In your country traffic commute time index is {your_traffic_commute_time_index}"
)
your_traffic_commute_time_index = (
    float(
        input("What is your desirable traffic commute time index (lower is better)? ")
    )
    or your_traffic_commute_time_index
)

your_pollution_index = float(df[df.country == your_country]["pollution_index"])
print(f"In your country pollution index is {your_pollution_index}")
your_pollution_index = (
    float(input("What is your desirable pollution index (lower is better)? "))
    or your_pollution_index
)


values = {
    "purchasing_power_index": 200,
    "safety_index": 200,
    "health_care_index": 200,
    "cost_of_living_index": 0,
    "property_price_to_income_ratio": 0,
    "traffic_commute_time_index": 0,
    "pollution_index": 0,
    "climate_index": 200,
}
df = df.fillna(value=values)

your_purchasing_power_index = float(your_purchasing_power_index)
your_safety_index = float(your_safety_index)
your_health_care_index = float(your_health_care_index)
your_cost_of_living_index = float(your_cost_of_living_index)
your_property_price_to_income_ratio = float(your_property_price_to_income_ratio)
your_traffic_commute_time_index = float(your_traffic_commute_time_index)
your_pollution_index = float(your_pollution_index)
your_climate_index = float(your_climate_index)

out_df = df[df.purchasing_power_index > your_purchasing_power_index][
    df.safety_index > your_safety_index
][df.health_care_index > your_health_care_index][
    df.cost_of_living_index < your_cost_of_living_index
][
    df.property_price_to_income_ratio < your_property_price_to_income_ratio
][
    df.traffic_commute_time_index < your_traffic_commute_time_index
][
    df.pollution_index < your_pollution_index
][
    df.climate_index > your_climate_index
]
print_out_df = out_df[
    ["country", "freedomhouse_score", "quality_of_life_index"]
].dropna().sort_values(by=['freedomhouse_score'], ascending=False)

if print_out_df.empty:
    print(f"There is no country better than {your_country}.")
else:
    with pd.option_context("display.max_rows", None, "display.max_columns", None):
        print(print_out_df)
