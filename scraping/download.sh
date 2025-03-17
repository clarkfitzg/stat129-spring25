# wget programmatically downloads files from the internet for us,
#       without a web browser.
#
#   --input-file are all the URL's of what we want to download
#   --user-agent identifies who is making the request. 
#       By passing this string we're pretending to be a Firefox web browser,
#       because many web servers block automated downloads.

wget --input-file=cpi-urls.txt --user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0"
