# Usage:
# First create tempcount.txt containing the results of uniq -c for all the temperature observations.
# Then run the following:
# 
# $ Rscript uniq_to_hist.R tempcount.txt
#
# This will produce a file temp_histogram.pdf

hist_from_count = function(countfile, upper = 140, lower = -60, varname = "temperature (degrees F)", ...)
{
    # Plot a histogram of the temperature for our weather data.

    d = read.table(countfile, row.names = NULL)
    colnames(d) = c("count", "value")
    d[["count"]] = as.numeric(d[["count"]])

    # Convert from tenths of degree celsius to Fahrenheit
    d[["value"]] = (d[["value"]]/10 * (9/5)) + 32

    # Drop outliers
    d = d[lower < d[["value"]] & d[["value"]] < upper, ]

    # general logic for creating a histogram from output of bash table:
    #        sort | uniq --count > counts.txt
    result = hist(d[["value"]], plot = FALSE, ...)
    d[["bin"]] = cut(d[["value"]], breaks = result[["breaks"]])
    counts = tapply(d[["count"]], d[["bin"]], sum)
    counts[is.na(counts)] = 0

    result[["counts"]] = counts
    result[["density"]] = counts / sum(counts)
    result[["xname"]] = varname
    result
}


# Example usage, assuming you've saved resulting table as temp_counts.txt
args = commandArgs(TRUE)
h = hist_from_count(args[1])
pdf("temp_histogram.pdf")
plot(h)
dev.off()
