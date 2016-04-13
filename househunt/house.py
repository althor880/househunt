# house.py

import os
import hashlib
import urllib
import urllib2
import StringIO
import csv
import requests
import xmltodict
import searchresults

from tinydb import TinyDB, Query

from datetime import datetime, timedelta

class House(object):
    """
    House class
    """
    def __init__(
        self,
        street_address=None,
        city=None,
        state=None,
        zip_code=None,
        beds=None,
        baths=None,
        sq_ft=None,
        parking=None,
        parking_type=None,
        lot_size=None,
        home_type=None
    ):
        self.street_address=street_address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.beds = beds
        self.baths = baths
        self.sq_ft = sq_ft
        self.parking = parking
        self.parking_type = parking_type
        self.lot_size = lot_size
        self.home_type = home_type

    def __repr__(self):
        return "%s %s, %s %s" % (self.street_address, self.city, self.state, self.zip_code)

    @property
    def detailed(self):
        detail_string = "Address: %s\nHome Type: %s\nBeds: %s\nBaths: %s\nSqFt: %s\nLot Size: %s\nParking Spaces: %s\nParking Type: %s\n"
        return detail_string % (
            str(self),
            self.home_type,
            self.beds,
            self.baths,
            self.sq_ft,
            self.lot_size,
            self.parking,
            self.parking_type
        )

    @property
    def street_address(self):
        return self._street_address

    @street_address.setter
    def street_address(self, street_address):
        self._street_address = street_address

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        self._city = city

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state

    @property
    def zip_code(self):
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        self._zip_code = zip_code

    @property
    def beds(self):
        return self._beds

    @beds.setter
    def beds(self, beds):
        self._beds = beds

    @property
    def baths(self):
        return self._baths

    @baths.setter
    def baths(self, baths):
        self._baths = baths

    @property
    def sq_ft(self):
        return self._sq_ft

    @sq_ft.setter
    def sq_ft(self, sq_ft):
        self._sq_ft = sq_ft

    @property
    def parking(self):
        return self._parking

    @parking.setter
    def parking(self, parking):
        self._parking = parking

    @property
    def parking_type(self):
        return self._parking_type

    @parking_type.setter
    def parking_type(self, parking_type):
        self._parking_type = parking_type

    @property
    def lot_size(self):
        return self._lot_size

    @lot_size.setter
    def lot_size(self, lot_size):
        self._lot_size = lot_size

    @property
    def home_type(self):
        return self._home_type

    @home_type.setter
    def home_type(self, home_type):
        self._home_type = home_type

    @property
    def hsh(self):
        m = hashlib.md5()
        m.update(str(self))
        return m.hexdigest()

    @classmethod
    def from_dict(cls, dictionary):
        try:
            return cls(
                street_address=dictionary['street_address'],
                city=dictionary['city'],
                state=dictionary['state'],
                zip_code=dictionary['zip_code'],
                beds=dictionary['beds'],
                baths=dictionary['baths'],
                parking=dictionary['parking'],
                parking_type=dictionary['parking_type'],
                sq_ft=dictionary['sq_ft'],
                lot_size=dictionary['lot_size'],
                home_type=dictionary['home_type']
            )
        except:
            return cls()

    def as_dict(self):
        d = {
            'street_address': self.street_address,
            'city': self.city,
            'state': self.state,
            'zip_code': self.zip_code,
            'beds': self.beds,
            'baths': self.baths,
            'parking': self.parking,
            'parking_type': self.parking_type,
            'sq_ft': self.sq_ft,
            'lot_size': self.lot_size,
            'home_type': self.home_type
        }
        return d

class Listing(object):
    """
    Listing class
    """
    def __init__(
        self,
        house=None,
        list_price=None,
        zestimate=None,
        days_on_market=None,
        original_list_price=None,
        status=None,
        mls_id=None,
        open_house_date=None,
        open_house_start_time=None,
        open_house_end_time=None
    ):
        self.house = house
        self.list_price = list_price
        self.zestimate = zestimate
        self.days_on_market = days_on_market
        self.original_list_price = original_list_price
        self.status = status
        self.mls_id = mls_id
        self.open_house_date = open_house_date
        self.open_house_start_time = open_house_start_time
        self.open_house_end_time = open_house_end_time

    def __repr__(self):
        return "Address: %s - List Price: %s - Zestimate: %s" % (str(self.house), str(self.list_price), str(self.zestimate))

    @property
    def detailed(self):
        detail_string = "House Details:\n%s\nStatus: %s\nList Price: %s\nZestimate: %s\nMLS ID: %s\nDays on Market: %s\nOriginal Price: %s\n"
        return detail_string % (
            self.house.detailed,
            self.status,
            self.list_price,
            self.zestimate,
            self.mls_id,
            self.days_on_market,
            self.original_list_price
        )

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        self._house = house

    @property
    def list_price(self):
        return self._list_price

    @list_price.setter
    def list_price(self, list_price):
        self._list_price = list_price

    @property
    def zestimate(self):
        return self._zestimate

    @zestimate.setter
    def zestimate(self, zestimate):
        self._zestimate = zestimate

    @property
    def days_on_market(self):
        return self._days_on_market

    @days_on_market.setter
    def days_on_market(self, days_on_market):
        self._days_on_market = days_on_market

    @property
    def original_list_price(self):
        return self._original_list_price

    @original_list_price.setter
    def original_list_price(self, original_list_price):
        self._original_list_price = original_list_price

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def mls_id(self):
        return self._mls_id

    @mls_id.setter
    def mls_id(self, mls_id):
        self._mls_id = mls_id

    @property
    def open_house_date(self):
        return self._open_house_date

    @open_house_date.setter
    def open_house_date(self, open_house_date):
        self._open_house_date = open_house_date

    @property
    def open_house_start_time(self):
        return self._open_house_start_time

    @open_house_start_time.setter
    def open_house_start_time(self, open_house_start_time):
        self._open_house_start_time = open_house_start_time

    @property
    def open_house_end_time(self):
        return self._open_house_end_time

    @open_house_end_time.setter
    def open_house_end_time(self, open_house_end_time):
        self._open_house_end_time = open_house_end_time

    @property
    def hsh(self):
        return self.house.hsh

    @classmethod
    def from_dict(cls, dictionary):
        try:
            h = House.from_dict(dictionary['house'])
            return cls(
                house=h,
                list_price=dictionary['list_price'],
                zestimate=dictionary['zestimate'],
                days_on_market=dictionary['days_on_market'],
                original_list_price=dictionary['original_list_price'],
                status=dictionary['status'],
                mls_id=dictionary['mls_id'],
                open_house_date=dictionary['open_house_date'],
                open_house_start_time=dictionary['open_house_start_time'],
                open_house_end_time=dictionary['open_house_end_time']
            )
        except:
            return cls()

    def as_dict(self):
        d = {
            'house': self.house.as_dict(),
            'list_price': self.list_price,
            'zestimate': self.zestimate,
            'days_on_market': self.days_on_market,
            'original_list_price': self.original_list_price,
            'status': self.status,
            'mls_id': self.mls_id,
            'open_house_date': self.open_house_date,
            'open_house_start_time': self.open_house_start_time,
            'open_house_end_time': self.open_house_end_time
        }
        return d

    def get_zestimate(self):
        lc = ListCache()
        lc.remove_old_listings()
        if lc.listing_in_cache(self):
            c_list = lc.retrieve_listing(self)
            self.zestimate = c_list.zestimate
        else:
            z_api = ZillAPI()
            z_list = z_api.get_from_zillow(self.house)
            self.zestimate = z_api.get_zestimate(z_list)
            lc.insert_listing(self)


class ListCache(object):

    DB_FILE = 'listing_db.json'
    DB_TTL = timedelta(hours=12)

    def __init__(self):
        self.db = TinyDB(os.path.join(os.path.join(os.getcwd(), os.path.dirname(__file__)), ListCache.DB_FILE))

    @property
    def db(self):
        return self._db

    @db.setter
    def db(self, db):
        self._db = db

    def listing_in_cache(self, listing):
        lquery = Query()
        return self.db.contains(lquery.hsh == listing.hsh)

    def retrieve_listing(self, listing):
        lquery = Query()
        list_dict = self.db.get(lquery.hsh == listing.hsh)
        return Listing.from_dict(list_dict)

    def insert_listing(self, listing):
        if self.listing_in_cache(listing):
            self.update_listing(listing)
        else:
            list_dict = listing.as_dict()
            list_dict['last_updated'] = datetime.now().isoformat()
            list_dict['hsh'] = listing.hsh
            self.db.insert(list_dict)

    def remove_listing(self, listing):
        lquery = Query()
        self.db.remove(lquery.hsh == listing.hsh)

    def update_listing(self, listing):
        lquery = Query()
        if self.listing_in_cache(listing):
            self.remove_listing(listing)
        self.insert_listing(listing)

    def remove_old_listings(self):
        list_ar = self.db.all()
        for listing in list_ar:
            if datetime.strptime(listing['last_updated'], '%Y-%m-%dT%H:%M:%S.%f') < datetime.now() - ListCache.DB_TTL:
                self.remove_listing(Listing.from_dict(listing))

class ZillAPI(object):

    ZIL_URL = 'http://www.zillow.com/webservice/GetSearchResults.htm'
    ZIL_XSD = 'http://www.zillow.com/static/xsd/SearchResults.xsd'
    # Moved ZWSID to an external file to avoid committing to source control. Should be placed in file named 'ZWSID' with the value on the first line
    ZWSID = ''

    def __init__(self):
        ZillAPI.load_zwsid()

    @classmethod
    def load_zwsid(cls, zwsid_filename='ZWSID'):
        with open(os.path.join(os.path.join(os.getcwd(), os.path.dirname(__file__)), zwsid_filename), 'r') as f:
            cls.ZWSID = f.readline().rstrip()


    def get_from_zillow(self, h):
        params = (('zws-id', ZillAPI.ZWSID), ('address', h.street_address), ('citystatezip', h.zip_code))
        urlparams = urllib.urlencode(params)
        zurl = "%s?%s" % (ZillAPI.ZIL_URL, urlparams)
        req = requests.get(zurl)
        req_content = req.content
        req_content_str = StringIO.StringIO(req_content)
        sr = searchresults.parse(req_content_str, silence=True)
        return sr

    def get_zestimate(self, sr):
        zestimates = []
        if sr.response:
            for prop in sr.response.results.result:
                value = prop.zestimate.amount.valueOf_
                if value not in zestimates:
                    zestimates.append(value)
        if len(zestimates) == 1:
            return zestimates[0]
        elif len(zestimates) == 0:
            return None
        else:
            return max(zestimates)

class RFAPI(object):

    DL_URL = 'https://www.redfin.com/stingray/do/gis-search'

    DL_PARAMS = {
        'al': 3,
        'isSearchFormParamsDefault': 'false',
        'lpp': 50,
        'market': 'boston',
        'mpt': 99,
        'no_outline': 'false',
        'num_homes': 500,
        'page_number': 1,
        'region_id': 0,
        'region_type': 6,
        'sf': [1,2,3,5,6],
        'sp': 'true',
        'status': 1,
        'uipt': [1,2,3],
        'v': 8,
        'render': 'csv'
    }

    def __init__(
        self,
        region_ids=[],
        load_listings=False,
        get_zestimates=False
    ):
        self.region_ids = region_ids
        self.result_sets = []
        self.listings = []
        self.dl_urls = []
        if region_ids:
            self.build_dl_urls()
        if load_listings:
            self.load_listings()
        if get_zestimates:
            self.get_zestimates()

    @property
    def region_ids(self):
        return self._region_ids

    @region_ids.setter
    def region_ids(self, region_ids):
        self._region_ids = region_ids

    @property
    def dl_urls(self):
        return self._dl_urls

    @dl_urls.setter
    def dl_urls(self, dl_urls):
        self._dl_urls = dl_urls

    @property
    def result_sets(self):
        return self._result_sets

    @result_sets.setter
    def result_sets(self, result_sets):
        self._result_sets = result_sets

    def build_dl_urls(self):
        self.dl_urls = []
        for region_id in self.region_ids:
            params = RFAPI.DL_PARAMS
            params['region_id'] = region_id
            url_params = urllib.urlencode(params, doseq=True)
            dl_url = "%s?%s" % (RFAPI.DL_URL, url_params)
            self.dl_urls.append(dl_url)

    def add_region_id(self, region_id):
        if region_id not in self.region_ids:
            self.region_ids.append(region_id)
            self.build_dl_urls()

    def retrieve_dls(self):
        for dl_url in self.dl_urls:
            browse = urllib2.urlopen(dl_url)
            csv_str = browse.read()
            csv_f = StringIO.StringIO(csv_str)
            reader = csv.reader(csv_f, delimiter=',')
            headers = reader.next()
            for row in reader:
                ds = zip(headers, row)
                self.result_sets.append(dict(ds))

    def dataset_to_listings(self):
        for rs in self.result_sets:
            try:
                h = House(
                    street_address=rs['ADDRESS'],
                    city=rs['CITY'],
                    state=rs['STATE'],
                    zip_code=rs['ZIP'],
                    beds=rs['BEDS'],
                    baths=rs['BATHS'],
                    parking=rs['PARKING SPOTS'],
                    parking_type=rs['PARKING TYPE'],
                    sq_ft=rs['SQFT'],
                    lot_size=rs['LOT SIZE'],
                    home_type=rs['HOME TYPE']
                )
                l = Listing(
                    house=h,
                    list_price=rs['LIST PRICE'],
                    days_on_market=rs['DAYS ON MARKET'],
                    original_list_price=rs['ORIGINAL LIST PRICE'],
                    status=rs['STATUS'],
                    mls_id=rs['LISTING ID'],
                    open_house_date=rs['NEXT OPEN HOUSE DATE'],
                    open_house_start_time=rs['NEXT OPEN HOUSE START TIME'],
                    open_house_end_time=rs['NEXT OPEN HOUSE END TIME']
                )
                self.listings.append(l)
            except KeyError:
                pass

    def load_listings(self):
        self.retrieve_dls()
        self.dataset_to_listings()

    def get_zestimates(self):
        for listing in self.listings:
            listing.get_zestimate()


if __name__ == '__main__':
    rf_api = RFAPI(region_ids=[9614], load_listings=True, get_zestimates=True)
    # rf_api = RFAPI([9614,20294,10229], load_listings=True)
    for listing in rf_api.listings:
        print listing.detailed


