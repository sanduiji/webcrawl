# webcrawl
test for web crawling

## README for webcrawl_with_format.py
This script crawls main documents from [site](https://www.w3cschool.cn/hadoop)(https://www.w3cschool.cn/hadoop) and store them conbined in one `.md` file. 
To apply this script to other site, a little changes should be made. this description introduces how the script works and instructs how changes should be made.

- access the site like all other method and locate navigation side bar
- fetch all links for parts of the documents and restore the name of their parent document
- add **#** to documents title according to their relations
- use `tag.decode_contents()` to decode html code then save rather than save them directly.
