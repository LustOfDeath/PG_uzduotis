import json
import pandas as pd


def step_two_flight_info(json_data):
    journeys = json_data["body"]["data"]["journeys"]

    flight_data_for_csv = []

    for information in journeys:
        recommendation_id = information['recommendationId']

        price = None
        for recommendation in json_data["body"]["data"]["totalAvailabilities"]:
            if recommendation['recommendationId'] == recommendation_id:
                price = float(recommendation['total'])
                break

        outbound_flight = information['flights'][0]
        taxes = float(information['importTaxAdl'])

        outbound_1_airport_departure = outbound_flight['airportDeparture']['code']
        outbound_1_airport_arrival = outbound_flight['airportArrival']['code']
        outbound_1_time_departure = outbound_flight['dateDeparture']
        outbound_1_time_arrival = outbound_flight['dateArrival']
        outbound_1_flight_number = outbound_flight['number']

        flight_data_for_csv.append({
            "Departure Airport": outbound_1_airport_departure,
            "Departure Time": outbound_1_time_departure,
            "Flight Number": outbound_1_flight_number,
            "Arrival Airport": outbound_1_airport_arrival,
            "Arrival Time": outbound_1_time_arrival,
            "Price": price,
            "Tax": taxes,
        })

    return flight_data_for_csv


def save_flight_info_into_csv(flight_data_for_csv, csv_file):
    data_frame = pd.DataFrame(flight_data_for_csv, columns=[
        "Departure Airport",
        "Departure Time",
        "Flight Number",
        "Arrival Airport",
        "Arrival Time",
        "Price",
        "Tax", ])

    data_frame.to_csv(csv_file, index=False)


with open("flights_information.json") as flight_info_file:
    json_data = json.load(flight_info_file)

json_data = step_two_flight_info(json_data)

save_flight_info_into_csv(json_data, "flight_info_csv.csv")
