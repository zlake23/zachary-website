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

def apply_template(content):
    template = open('./templates/base.html').read()
    template.replace("{{content}}", content)
    return template

def main(doc):
    for page in pages:
        content = open(page['filename']).read()
        doc = apply_template(content)
    return doc

def build():
    for page in pages:
        open(page['output'], 'w+').write(main(doc))
# def main():
#     # Read in base template file
#     template = open('./templates/base.html').read()

#     # Loop through each dictionary in page list to compile html pages
#     for page in pages:
#         content = open(page['filename']).read()
#         doc = template.replace("{{content}}", content)
#         open(page['output'], 'w+').write(doc)

# main()