import requests
from ripe.atlas.sagan import SslResult

source = "https://atlas.ripe.net/api/v1/measurement-latest/1012449/"
response = requests.get(source).json

for probe_id, result in response.items():
    result = result[0]                 # There's only one result for each probe
    parsed_result = SslResult(result)  # Parsing magic!

    # Each SslResult has n certificates
    for certificate in parsed_result.certificates:
        print(certificate.checksum)  # Print the checksum for this certificate

    # Make use of the handy get_checksum_chain() to render the checksum of each certificate into one string if you want
    print(parsed_result.get_checksum_chain())
