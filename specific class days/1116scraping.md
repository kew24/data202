Scraping Examples
================
Kaitlyn Westra
11/16/2020

Solar Flares
============

``` r
if (!file.exists('flare.data2')) {
  #download.file("https://archive.ics.uci.")
  #get file from UCI ML archive
}
```

    ## NULL

``` r
#way more stuff here
```

Wunderground
============

``` r
library(rvest)
```

    ## Loading required package: xml2

    ## 
    ## Attaching package: 'rvest'

    ## The following object is masked from 'package:purrr':
    ## 
    ##     pluck

    ## The following object is masked from 'package:readr':
    ## 
    ##     guess_encoding

``` r
html <- read_html('https://www.wunderground.com/history/monthly/KGRR/date/2020-11')
html %>%
  html_nodes("lib-city-history-observation table")
```

    ## {xml_nodeset (0)}

Look at inspect = = &gt; inspector and = = &gt; network. Get the json object. Copy --&gt; copy response. Make new text file & paste that!

I obviously did something wrong, as my .json isn't telling me all the information I want. I think I copied the wrong .json file, but I don't know where the right one is. But... this is what it would look like if I had used the right file.

``` r
library(jsonlite)
```

    ## 
    ## Attaching package: 'jsonlite'

    ## The following object is masked from 'package:purrr':
    ## 
    ##     flatten

``` r
weather_hist <- jsonlite::read_json("./data/wunderground-hist.json", simplifyVector = TRUE)
observations <- weather_hist$observations
glimpse(observations)
```

    ##  NULL

``` r
weather_hist$status %>% glimpse()
```

    ##  chr "ok"

when you're typing, look at the grey thing for a function to see which package you're using it from
turns anything ambiguous into an error

BigQuery: Google Cloud Platform (CalvinDSDev)
Free to access from Google.
