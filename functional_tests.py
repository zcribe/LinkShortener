from selenium import webdriver


# Joe starts hit browser
browser = webdriver.Firefox()

# He needs to dictate the link to a news story over the phone. He googles
# for a link shortener and navigates to the page.
browser.get('http://localhost:8000')

# He notices that the page title and header mention that it is a URL
# shortening service.
assert 'URLShortener' in browser.title

# He sees a form there.

# He is invited to paste in a link and click a button

# He pastes in a link and clicks on a button

# He is redirected to a new page.

# He sees the title of the page

# He notices a generated link

# He copies it and then visits it to check it.

# He is happy with the service provided and closes the browser.
browser.close()