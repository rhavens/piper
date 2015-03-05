# Optimizations

Used Pagespeed Tools
BENCHMARK: 43/100

<h1> Fixes needed </h1>
<ul>
	<li>Gzip file compression</li>
	<li>Eliminate render blocking JS and CSS</li>
	<li>Minify CSS and HTML </li>
	<li>Browser caching</li>
	<li>Optimize Images</li>
</ul>
	
<h1> Caching </h1>

<p> Redis Server Advantages: </p>

<ul>
<li>Memcached only allows serialized strings (up to 1 MB) as values in a key-value pair</li>
<li>Redis allows key names and values as large as 512 MB</li>
<li>Redis has six data types which allows for far more control over what is cached in the server</li> 
<li>Memcached relies on one algorithm (LRU) for data eviction</li>
<li>Redis gives far more control in how data eviction occurs within the server</li>
<li>Methods include: no-eviction, allkeys-LRU, (similar to the memcached algorithm), volatile-LRU(remove less used keys first but only if they have an expire set), allkeys-random(randomized eviction), volatile-random, volatile-ttl</li>
 
<p>Static Content: We optimize our cache for serving static content by setting the header to allow for a long max-age.</p>

<p>IP Address:  We will also cache our IP address to avoid the difficulty of repeated DNS lookups, which take between 20 - 120 ms. Nothing can load while the DNS is being resolved, so this is a huge benefit to client-side loading speed.</p>

<p>Dynamic Content:  Content that is frequently updated is best left out of the cache as requests constantly need to be made to the servers to ensure the content is up to date.</p> 

<p>HTML5 Application Cache

The HTML5 Application Cache allows for resources to be recycled within the user's own browser, reducing the number of redundant requests sent to the server. This offline cache improves performance and allows for a greater number of users to be serviced simultaneously. This is especially useful for those with subpar internet connections or for users who choose to go offline.</p>

<h1> Minify files </h1>

<p>- Javascript and CSS minification

Javascript and CSS minification reduces the size of the files, limiting the amount of wasted bandwidth. This decreases overall server load and has the added benefit of improving the efficiency of the cache. The smaller the files stored in the cache, the more items it can hold.


- Combining Javascript/CSS files

Reduces the number of seperate HTTP requests sent to the server. Less files need to be accessed and less files need to be transmitted.</p>


<h1> Code execution location </h1>

<p>- Javascript at bottom of pages

Having relevant Javascript code placed at the bottom of pages allows for non-dynamic content to load first. Pure HTML/CSS is lightweight, so it loads quickly and efficiently. JavaScript is loaded synchronously, so while it is being loaded, users see only a blank screen.</p>


<h1> GZIP Compression </h1>

<p>- Compressing HTTP requests/responses

We plan on using Gzip to reduce the size of HTTP requests and responses to even further lower the amount of traffic sent to the server. As with other optimization methods we improve single-user performance which translates into a huge performance boost at a large scale. Gzip is known to reduce file size by 70% in requests and responses.</p>

<h1> Issues </h1>

<p>We have decided to only allow images of the type .jpeg and .png. .gifs are too expensive and taxing for the small benefit they add, and they do not add much value towards our site's public image.

Additionally, our database still runs on SQLite, which is infamous for poor scaling. We intend to move to PostgreSQL, a more efficient and optimized database management system.</p> 
