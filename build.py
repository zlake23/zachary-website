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

main()