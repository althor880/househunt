# house
Python module to search Redfin and combine with results from the Zillow API

# Pre-Requisites

There must be a file named 'ZWSID' in the working directory, which contains on the first line your Zillow API ID

# house.House class

Class that describes a house and its physical details:

## Properties:

- street_address
- city
- state
- zip_code
- beds
- baths
- sq_ft
- parking
- parking_type
- lot_size
- home_type

## Methods
- detailed():
  - Returns a formatted string containing more details than the basic string representation
- from_dict(dictionary):
  - Takes a dictionary as an argument and builds a House object using the key/values. The dictionary must contain a value for each of the classes properties (e.x. dictionary['street_address'] = "42 Wallaby Way")
- to_dict():
  - returns a dictionary containing all the properties of the house object. Formatted so as to be useable with the .from_dict(dictionary) method. (useful for serializing the object in a .json file)

## Example Usage

###

```
>>> from house import House
>>> h = House()
>>> print h
None None, None None
>>> h.street_address = "42 Wallaby Way"
>>> h.city = "Sydney"
>>> h.state = "Australia"
>>> h.zip_code = "12345"
>>> h.beds = 3
>>> h.baths = 1.5
>>> print h
42 Wallaby Way Sydney, Australia 12345
>>> print h.detailed
Address: 42 Wallaby Way Sydney, Australia 12345
Home Type: None
Beds: 3
Baths: 1.5
SqFt: None
Lot Size: None
Parking Spaces: None
Parking Type: None

```
