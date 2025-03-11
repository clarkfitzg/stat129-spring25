# Goal: Demonstrate xpath from the command line

# First Download a local copy of the page by uncommenting the following
# Not necessary, but makes things more convenient

#wget https://www.irs.gov/charities-non-profits/form-990-series-downloads

#xmllint --html -xpath "//li/a/@href" /stat129/form-990-series-downloads
xmllint --html -xpath "//li/a[contains(@href, '.zip')]/@href" /stat129/form-990-series-downloads |
	sed "s/ href=//" |
	tr --delete '"' > urls.txt
