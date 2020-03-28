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

# apply_template function will read in base template and
# replace content string with code from each html page
def apply_template(content):
    template = open('./templates/base.html').read()
    template = template.replace("{{content}}", content)
    return template


# def build(doc):
#     finished_doc = open(page['output'], 'w+').write(doc)
#     return finished_doc


# main function will run other functions for building template,
# reading files and writing to docs directory
def main():
    for page in pages:
        print('Reading files')
        content = open(page['filename']).read()
        print('Compiling templates')
        doc = apply_template(content) 
        print(doc)
        # build(doc)

main()


# def main():
#     # Read in base template file
#     template = open('./templates/base.html').read()

#     # Loop through each dictionary in page list to compile html pages
#     for page in pages:
#         content = open(page['filename']).read()
#         doc = template.replace("{{content}}", content)
#         open(page['output'], 'w+').write(doc)

# main()
