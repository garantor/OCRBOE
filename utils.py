import re
from datetime import datetime

def parse_date(date_str):
    """Parses '5 APRIL 2027' to datetime object."""
    try:
        return datetime.strptime(date_str.strip(), "%d %B %Y")
    except ValueError:
        return None

def extract_eta_dates(text):
    """
    Extracts start and/or end date from ETA approval text.
    Returns exact date strings and their datetime objects.
    """
    # Match both formats
    match_range = re.search(r"valid from\s+(\d{1,2}\s+\w+\s+\d{4})\s+to\s+(\d{1,2}\s+\w+\s+\d{4})", 
                            text, re.IGNORECASE)
    match_until = re.search(r"valid until[:\-]?\s*(\d{1,2}\s+\w+\s+\d{4})", 
                            text, re.IGNORECASE)

    if match_range:
        start_str = match_range.group(1)
        end_str = match_range.group(2)
        start_date = parse_date(start_str)
        end_date = parse_date(end_str)
        return {
            "start_date_str": start_str,
            "end_date_str": end_str,
            "start_date": start_date,
            "end_date": end_date
        }
    elif match_until:
        end_str = match_until.group(1)
        end_date = parse_date(end_str)
        return {
            "start_date_str": None,
            "end_date_str": end_str,
            "start_date": None,
            "end_date": end_date
        }
    else:
        return None

def datetime_to_millis(dt):
    """Converts a datetime object to milliseconds since epoch."""
    if dt:
        return int(dt.timestamp() * 1000)
    return None
