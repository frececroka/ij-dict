# Infinite Jest - Annotations

This is a rudimentary dictionary meant to be used while reading Infinite Jest on a Kindle. It incorporates the page-by-page annotations from the [Infinite Jest wiki](http://infinitejest.wallacewiki.com/) and a few character descriptions.

You can find the latest build from the CI server [here](https://s3.amazonaws.com/ij-dict/ij-dict.mobi).

Open issues:

+ There are -- of course -- keywords that cannot be defined unambigously. This includes "Kent", which could refer to "Kent Blott" or "U.S.S. Millicent Kent". The New Oxford American Dictionary shows multiple pages in these cases, one possible meaning per page. (Compare the behaviour for "we're". You get three pages with "we're", "be" and "were".) It is unclear how such behaviour can be achieved.
+ The coverage of characters in this dictionary is lacking.
+ Many of the page-by-page annotations are not suitable for the dictionary format. This includes annotations for a longer group of words, for instance quotes.
+ The `ij-scraper-py` pulls the page-by-page annotations from the IJ wiki. It fails to parse some of these annotations. The two prevailing markups are `<p><b>Keyword</b> <br/> Description</p>` and `<p><b>Keyword</b></p><p>Description</p>`. The scraper can handle the former but not the latter.
