# househunt

Python module to search Redfin and combine with results from the Zillow API

## Setup

There must be a file named 'ZWSID' in the working directory, which contains on the first line your Zillow API ID

## Classes in house.py

### House

Class that describes a house and its physical details.

#### Properties:

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

#### Methods

- hsh:
  - Returns a md5 hash of the house's address, city, state, and zip - used to uniquely identify house for cacheing purposes
- detailed:
  - Returns a formatted string containing more details than the basic string representation
- to_dict():
  - returns a dictionary containing all the properties of the house object. Formatted so as to be useable with the .from_dict(dictionary) method. (useful for serializing the object in a .json file)
- from_dict(dictionary):
  - Takes a dictionary as an argument and builds a House object using the key/values. The dictionary must contain a value for each of the classes properties (e.x. dictionary['street_address'] = "42 Wallaby Way") (useful for loading house objects from a .json file)

#### Example Usage

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
>>> h2 = House(street_address="1600 Pennsylvania Ave.", city="Washington D.C.", state="Washington D.C.", zip_code="20006")
>>> print h2
1600 Pennsylvania Ave. Washington D.C., Washington D.C. 20006
```

### Listing

Class that describes a real estate listing and its details.

#### Properties

- house
  - Contains a House object (see House class for details)
- list_price
- zestimate
- days_on_market
- original_list_price
- status
- mls_id
- open_house_date
- open_house_start_time
- open_house_end_time
 
#### Methods

- hsh:
  - returns the hsh value of the Listing's House object (used for uniquely identifying a listing for cacheing)
- detailed:
  - Returns a formatted string containing more details than the basic string representation
- to_dict():
  - returns a dictionary containing all the properties of the listing object. Formatted so as to be useable with the .from_dict(dictionary) method. (useful for serializing the object in a .json file)
- from_dict(dictionary):
  - Takes a dictionary as an argument and builds a Listing object using the key/values. The dictionary must contain a value for each of the classes properties (e.x. dictionary['list_price'] = 1000000) (useful for loading listing objects from a .json file)
- get_zestimate():
  - sets the objects zestimate property first checking for a cached value (in order to not exceed the Zillow API restriction on number of requests in 24 hours) and secondly querying the Zillow API. See ListCache class for details on cacheing, ans ZillAPI class for details on querying Zillow.

#### Example Usage

```
>>> from house import House, Listing
>>> h = House(street_address="42 Wallaby Way", city="Sydney", state="Australia", zip="12345")
>>> l = Listing(house=h, list_price=123456, days_on_market=5)
>>> print l.detailed
House Details:
Address: 42 Wallaby Way Sydney, Australia 12345
Home Type: None
Beds: 3
Baths: 1.5
SqFt: None
Lot Size: None
Parking Spaces: None
Parking Type: None

Status: None
List Price: 123455
Zestimate: None
MLS ID: None
Days on Market: 5
Original Price: None
>>> l.get_zestimate()
>>> print l.detailed
House Details:
Address: 42 Wallaby Way Sydney, Australia 12345
Home Type: None
Beds: 3
Baths: 1.5
SqFt: None
Lot Size: None
Parking Spaces: None
Parking Type: None

Status: None
List Price: 123455
Zestimate: 554321
MLS ID: None
Days on Market: 5
Original Price: None
```
