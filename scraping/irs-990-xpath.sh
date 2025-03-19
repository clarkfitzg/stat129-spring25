# Goal: Demonstrate xpath from the command line

# First Download a local copy of the page by uncommenting the following
# Not necessary, but makes things more convenient

#wget https://www.irs.gov/charities-non-profits/form-990-series-downloads

# Experiments with xpath

#xmllint --html -xpath "//li/a[contains(@href, '.zip')]/@href" /stat129/form-990-series-downloads 2>/dev/null

# Only prints the first one
#xmllint --html -xpath "string(//li/a[contains(@href, '.zip')]/@href)" /stat129/form-990-series-downloads 2>/dev/null

# The text of the node appears to work well enough
xmllint --html -xpath "//li/a[contains(@href, '.zip')]/text()" /stat129/form-990-series-downloads 

# Or hack away to get the *actual* URL
# https://stackoverflow.com/questions/11611385/how-can-i-get-the-value-from-an-attribute-using-xmllint-and-xpath#comment47903351_11684170

xmllint --html -xpath "//li/a[contains(@href, '.zip')]/@href" /stat129/form-990-series-downloads |
	sed "s/ href=//" |
	tr --delete '"' > urls.txt
