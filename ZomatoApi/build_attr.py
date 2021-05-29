import json


def header_cookies(response_dict):
    cookies = f'fre={response_dict["fre"]}; rd={response_dict["rd"]}; zl={response_dict["zl"]}; fbtrack={response_dict["fbtrack"]}; PHPSESSID={response_dict["PHPSESSID"]}; fbcity={response_dict["fbcity"]}; ltv={response_dict["ltv"]}; lty={response_dict["lty"]}; locus={response_dict["locus"]}; csrf={response_dict["csrf"]};AWSALBTG={response_dict["AWSALBTG"]}; AWSALBTGCORS={response_dict["AWSALBTGCORS"]};'

    #cookies = f'fre={response.cookies["fre"]}; rd={response.cookies["rd"]}; zl={response.cookies["zl"]}; fbtrack={response.cookies["fbtrack"]}; _ga=GA1.2.844008201.1614798189; _gcl_au=1.1.106489336.1614798189; _fbp=fb.1.1614798192963.1985538829; dpr=2; _gid=GA1.2.994941466.1615563966; expab=3; PHPSESSID={response.cookies["PHPSESSID"]}; fbcity={response.cookies["fbcity"]}; ltv={response.cookies["ltv"]}; lty={response.cookies["lty"]}; locus={response.cookies["locus"]}; csrf={response.cookies["csrf"]}; _gat_global=1; _gat_city=1; _gat_country=1; AWSALBTG={response.cookies["AWSALBTG"]}; AWSALBTGCORS={response.cookies["AWSALBTGCORS"]};'

    return cookies


def req_headers(cookies, csrf):
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-IN,en;q=0.9,hi-IN;q=0.8,hi;q=0.7,en-GB;q=0.6,en-US;q=0.5",
        "content-type": "application/json",
        "cookie": cookies,
        "origin": "https://www.zomato.com",
        "referer": "https://www.zomato.com/bangalore/indiranagar-restaurants",
        "sec-ch-ua": '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
        "x-zomato-csrft": csrf,
    }

    return headers


def req_payload(searchMetaData,currentLocation):
    

    PreviousSearchId = json.loads(searchMetaData["previousSearchParams"]
    )["PreviousSearchId"]
    postbackParams = json.loads(searchMetaData["postbackParams"]
    )
    processed_chain_ids = postbackParams["processed_chain_ids"]
    shown_res_count = postbackParams["shown_res_count"]
    search_id = postbackParams["search_id"]
    totalResults = searchMetaData["totalResults"]
    hasMore = searchMetaData["hasMore"]
    getInactive =searchMetaData["getInactive"]

    payload = (
        '{"context":"delivery","filters":"{\\"searchMetadata\\":{\\"previousSearchParams\\":\\"{\\\\\\"PreviousSearchId\\\\\\":\\\\\\"'
        + PreviousSearchId
        + '\\\\\\",\\\\\\"PreviousSearchFilter\\\\\\":[\\\\\\"{\\\\\\\\\\\\\\"category_context\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"delivery_home\\\\\\\\\\\\\\"}\\\\\\"]}\\",\\"postbackParams\\":\\"{\\\\\\"processed_chain_ids\\\\\\":'
        + str(processed_chain_ids)
        + ',\\\\\\"shown_res_count\\\\\\":'
        + str(shown_res_count)
        + ',\\\\\\"search_id\\\\\\":\\\\\\"'
        + str(search_id)
        + '\\\\\\"}\\",\\"totalResults\\":'
        + str(totalResults)
        + ',\\"hasMore\\":'
        + str(hasMore).lower()
        + ',\\"getInactive\\":'
        + str(getInactive).lower()
        + '},\\"dineoutAdsMetaData\\":{},\\"appliedFilter\\":[{\\"filterType\\":\\"category_sheet\\",\\"filterValue\\":\\"delivery_home\\",\\"isHidden\\":true,\\"isApplied\\":true,\\"postKey\\":\\"{\\\\\\"category_context\\\\\\":\\\\\\"delivery_home\\\\\\"}\\"}],\\"urlParamsForAds\\":{}}","addressId":'
        + str(currentLocation["addressId"])
        + ',"entityId":'
        + str(currentLocation["entityId"])
        + ',"entityType":"'
        + str(currentLocation["entityType"])
        + '","locationType":"'
        + str(currentLocation["locationType"])
        + '","isOrderLocation":'
        + str(currentLocation["isOrderLocation"])
        + ',"cityId":'
        + str(currentLocation["cityId"])
        + ',"latitude":"'
        + str(currentLocation["latitude"])
        + '","longitude":"'
        + str(currentLocation["longitude"])
        + '","userDefinedLatitude":'
        + str(currentLocation["userDefinedLatitude"])
        + ',"userDefinedLongitude":'
        + str(currentLocation["userDefinedLongitude"])
        + ',"entityName":"'
        + str(currentLocation["entityName"])
        + '","orderLocationName":"'
        + str(currentLocation["orderLocationName"])
        + '","cityName":"'
        + str(currentLocation["cityName"])
        + '","countryId":'
        + str(currentLocation["countryId"])
        + ',"countryName":"'
        + str(currentLocation["countryName"])
        + '","displayTitle":"'
        + str(currentLocation["displayTitle"])
        + '","o2Serviceable":'
        + str(currentLocation["o2Serviceable"]).lower()
        + ',"placeId":"'
        + str(currentLocation["placeId"])
        + '","cellId":"'
        + str(currentLocation["cellId"])
        + '","deliverySubzoneId":'
        + str(currentLocation["deliverySubzoneId"])
        + ',"placeType":"'
        + str(currentLocation["placeType"])
        + '","placeName":"'
        + str(currentLocation["placeName"])
        + '","isO2City":'
        + str(currentLocation["isO2City"]).lower()
        + ',"fetchFromGoogle":'
        + str(currentLocation["fetchFromGoogle"]).lower()
        + ',"fetchedFromCookie":'
        + str(currentLocation["fetchedFromCookie"]).lower()
        + ',"isO2OnlyCity":'
        + str(currentLocation["isO2OnlyCity"]).lower()
        + ',"address_template":'
        + str(currentLocation["address_template"])
        + ',"otherRestaurantsUrl":"'
        + str(currentLocation["otherRestaurantsUrl"])
        + '"}'
    )

    return payload

def req_payload_dine(searchMetaData,currentLocation):
    

    PreviousSearchId = json.loads(searchMetaData["previousSearchParams"]
    )["PreviousSearchId"]
    postbackParams = json.loads(searchMetaData["postbackParams"]
    )
    TotalRestaurantsShown = postbackParams["TotalRestaurantsShown"]
    TotalResultsShown = postbackParams["TotalResultsShown"]
    TotalRailsShown = postbackParams["TotalRailsShown"]
    ProcessedRails = postbackParams["ProcessedRails"]
    ShownRails = postbackParams["ShownRails"]
    Page = postbackParams["Page"]
    AdsPostBackParams = postbackParams["AdsPostBackParams"]
    HasMoreAds = postbackParams["HasMoreAds"]
    SolrOffset = postbackParams["SolrOffset"]
    CurrentVg = postbackParams["CurrentVg"]
    VgSet = postbackParams["VgSet"]
    search_id = postbackParams["search_id"]

    totalResults = searchMetaData["totalResults"]
    hasMore = searchMetaData["hasMore"]
    getInactive =searchMetaData["getInactive"]

    payload = (
        '{"context":"dineout","filters":"{\"searchMetadata\":{\"previousSearchParams\":\"{\\\"PreviousSearchId\\\":\\\"'
        + PreviousSearchId
        + '\\\",\\\"PreviousSearchFilter\\\":[\\\"{\\\\\\\"category_context\\\\\\\":\\\\\\\"go_out_home\\\\\\\"}\\\",\\\"{\\\\\\\"context\\\\\\\":\\\\\\\"dineout_home\\\\\\\"}\\\"]}\",\"postbackParams\":\"{\\\"TotalRestaurantsShown\\\":'
        + str(TotalRestaurantsShown)
        + ',\\\"TotalResultsShown\\\":'
        + str(TotalResultsShown)
        + ',\\\"TotalRailsShown\\\":'
        + str(TotalRailsShown)
        + ',\\\"ProcessedRails\\\":\\\"'
        + ProcessedRails
        + '\\\",\\\"ShownRails\\\":\\\"'
        + ShownRails
        + '\\\",\\\"Page\\\":'
        + str(Page)
        + ',\\\"AdsPostBackParams\\\":\\\"'
        + AdsPostBackParams
        + '\\\",\\\"HasMoreAds\\\":'
        + str(HasMoreAds).lower()
        + ',\\\"SolrOffset\\\":'
        + str(SolrOffset)
        + ',\\\"CurrentVg\\\":'
        + str(CurrentVg)
        + ',\\\"VgSet\\\":'
        + str(VgSet).lower()
        + ',\\\"search_id\\\":\\\"'
        + search_id
        + '\\\"}\",\"totalResults\":'
        + str(totalResults)
        + ',\"hasMore\":'
        + str(hasMore).lower()
        + ',\"getInactive\":'
        + str(getInactive).lower()
        + '},\"dineoutAdsMetaData\":{},\"appliedFilter\":[{\"filterType\":\"category_sheet\",\"filterValue\":\"go_out_home\",\"isHidden\":,\"isApplied\":true,\"postKey\":\"{\\\"category_context\\\":\\\"go_out_home\\\"}\"},{\"filterType\":\"context\",\"filterValue\":\"dineout_home\",\"isHidden\":true,\"isApplied\":true,\"postKey\":\"{\\\"context\\\":\\\"dineout_home\\\"}\"}],\"urlParamsForAds\":{}}","addressId":'
        + str(currentLocation["addressId"])
        + ',"entityId":'
        + str(currentLocation["entityId"])
        + ',"entityType":"'
        + str(currentLocation["entityType"])
        + '","locationType":"'
        + str(currentLocation["locationType"])
        + '","isOrderLocation":'
        + str(currentLocation["isOrderLocation"])
        + ',"cityId":'
        + str(currentLocation["cityId"])
        + ',"latitude":"'
        + str(currentLocation["latitude"])
        + '","longitude":"'
        + str(currentLocation["longitude"])
        + '","userDefinedLatitude":'
        + str(currentLocation["userDefinedLatitude"])
        + ',"userDefinedLongitude":'
        + str(currentLocation["userDefinedLongitude"])
        + ',"entityName":"'
        + str(currentLocation["entityName"])
        + '","orderLocationName":"'
        + str(currentLocation["orderLocationName"])
        + '","cityName":"'
        + str(currentLocation["cityName"])
        + '","countryId":'
        + str(currentLocation["countryId"])
        + ',"countryName":"'
        + str(currentLocation["countryName"])
        + '","displayTitle":"'
        + str(currentLocation["displayTitle"])
        + '","o2Serviceable":'
        + str(currentLocation["o2Serviceable"]).lower()
        + ',"placeId":"'
        + str(currentLocation["placeId"])
        + '","cellId":"'
        + str(currentLocation["cellId"])
        + '","deliverySubzoneId":'
        + str(currentLocation["deliverySubzoneId"])
        + ',"placeType":"'
        + str(currentLocation["placeType"])
        + '","placeName":"'
        + str(currentLocation["placeName"])
        + '","isO2City":'
        + str(currentLocation["isO2City"]).lower()
        + ',"fetchFromGoogle":'
        + str(currentLocation["fetchFromGoogle"]).lower()
        + ',"fetchedFromCookie":'
        + str(currentLocation["fetchedFromCookie"]).lower()
        + ',"isO2OnlyCity":'
        + str(currentLocation["isO2OnlyCity"]).lower()
        + ',"address_template":'
        + str(currentLocation["address_template"])
        + ',"otherRestaurantsUrl":"'
        + str(currentLocation["otherRestaurantsUrl"])
        + '"}'
    )

    return payload


