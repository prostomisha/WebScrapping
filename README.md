<h1>Web Crawler</h1>
<h2>Task Description</h2>
Create a web crawler using scraping techniques to extract the first 30 entries from https://news.ycombinator.com/. You'll only care about the number, the title, the points, and the number of comments for each entry.

From there, we want it to be able to perform a couple of filtering operations:

Filter all previous entries with more than five words in the title ordered by the number of comments first.
Filter all previous entries with less than or equal to five words in the title ordered by points.
When counting words, consider only the spaced words and exclude any symbols. For instance, the phrase “This is - a self-explained example” should be counted as having 5 words.

The solution should store usage data, including at least the request timestamp and a field to identify the applied filter. You are free to include any additional fields you deem relevant to track user interaction and crawler behavior. The chosen storage mechanism could be a database, cache, or any other suitable tool.

<h2>Used technologies</h2>

For solving the task I was using the next stack of technologies:

Python language,  

Package Beautifil Soup (for parsing data from the website),

Package Requests (to work with HTTP requests), 

Package datetime (for timestamps), 

Package Pandas (to storage data in data frame format and write it to CSV file)


