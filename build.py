print('Building Site...')
pages = [
    {
        "filename": "content/index.html",
        "output": "docs/index.html",
        "title": "Home Page",
    },
    {
        "filename": "content/blog.html",
        "output": "docs/blog.html",
        "title": "My Blog",
    },
    {
        "filename": "content/projects.html",
        "output": "docs/projects.html",
        "title": "My Projects",
    },
    {
        "filename": "content/contact.html",
        "output": "docs/contact.html",
        "title": "Contact Page",
    },
]

def main():
    # Read in template files
    top = open('./templates/top.html').read()
    bottom = open('./templates/bottom.html').read()

    # Loop through each dictionary in page list to compile html pages
    for page in pages:
        content = open(page['filename']).read()
        doc = top + content + bottom
        open(page['output'], 'w+').write(doc)


    # # Read index file
    # content = open('./content/index.html').read()

    # # Combine files into new file for about page
    # index_html = top_html + content + bottom_html
    # open('./docs/index.html', 'w+').write(index_html)

    # # Combine files into new file for blog page
    # content = open('./content/blog.html').read()
    # blog_html = top_html + content + bottom_html
    # open('./docs/blog.html', 'w+').write(blog_html)

    # # Combine files into new file for projects page
    # content = open('./content/projects.html').read()
    # projects_html = top_html + content + bottom_html
    # open('./docs/projects.html', 'w+').write(projects_html)

    # # Combine files into new file for contact page
    # content = open('./content/contact.html').read()
    # contact_html = top_html + content + bottom_html
    # open('./docs/contact.html', 'w+').write(contact_html)

main()