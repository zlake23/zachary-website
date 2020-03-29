print('Building Site...')
pages = [
    {
        "filename": "content/index.html",
        "output": "docs/index.html",
        "title": "Zachary Lake",
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
def apply_template(content, title):
    template = open('./templates/base.html').read()
    template = template.replace("{{content}}", content)
    template = template.replace("{{title}}", title)
    return template

# build function will write the completed webpage 
# to the docs directory
def build(doc, page):
        finished_doc = open(page['output'], 'w+').write(doc)
        return finished_doc

# main function will read in content from pages
# build pages with apply_template and write to docs directory with build
def main():
    for page in pages:
        content = open(page['filename']).read()
        title = page['title']
        print('Reading:', page['filename'])
        
        doc = apply_template(content, title) 
        print('Compiling template:', page['output'])

        finished_webpage = build(doc, page)
    print('Webpage built')
       

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
