url = "https://maps.googleapis.com/maps/api/geocode/json?components=postal_code:"
pincode = raw_input("> ")
country = raw_input("> ")
url = url + pincode + "|country:" + country
print url
