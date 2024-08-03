# import urllib.request as u


# website_name = input("Enter your website name:")

# source_code = u.urlopen(website_name)

# source_read = source_code.read()
# print(source_read)


import urllib.request as u
import urllib.error

website_name = input("Enter your website name: ").strip()

# Add http:// if the user didn't provide it
if not website_name.startswith("http://") and not website_name.startswith("https://"):
    website_name = "http://" + website_name

try:
    source_code = u.urlopen(website_name)
    source_read = source_code.read()
    print(source_read)
except urllib.error.URLError as e:
    print(f"Failed to retrieve {website_name}: {e.reason}")
except Exception as e:
    print(f"An error occurred: {e}")


