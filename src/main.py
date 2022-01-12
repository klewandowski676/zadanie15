def filter_countries(orginal_countries, country_filter):
    filtered_countries = []
    
    for country in orginal_countries:
        if country.startswith(country_filter):
            filtered_countries.append(country)

    return filtered_countries
