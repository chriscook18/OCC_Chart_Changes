*** OVERVIEW ***
For any chart on the Official Charts Company website (www.officialcharts.com) this will grab the Top 10, new entries 
and re-entries and format them into a format compatiable for BB forum posts.

*** USE ***
This is Python-based. You need to be able to run Python and have the libraries lxml and requests installed.

This currently supports 3 different pages to be scrapped. Naturally adding a new site is as simple as either a) adding a new entry to the webLink dictionary or changing an existing one. 

After scrapping it will then output the code that can be pasted into the forum.

*** OUTPUT FORMAT ***
An example of the output is http://forums.stevehoffman.tv/threads/uk-albums-chart-analysis-thread.614213/page-12#post-19978889
This currently outputs in the following format:
Top 10 items:
(#) Artist - [i]Album[/i] (Last week's position)

New/rentries:
Artist - [i]Album[/i] (Position it has entered at)

*** NOTES WITH OCC DATA ***
Sometimes the OCC data is slightly wrong - artist names may be truncated or lacking "The" preface (e.g. Beatles instead of The Bealtes)
Occasionally they count an album that has already charted in the past as a new entry instead of a re-entry.

*** ISSUES/FEATURE IDEAS ***
* It seems that apostrophes are triggering the capitalisation - e.g. "I'LL" is becoming "I'Ll" instead of "I'll"
* It can't tell whether to tweak the titles to say "Other re-entries" depending on whether or not there are re-entries in the Top 10
* Could consider adding support for common artist name issues, e.g. "Beatles" -> "The Beatles", but I'm not sure how sensible that is.

