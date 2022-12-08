from django.core.paginator import Paginator

books = ["A", "B", "C", "D", "E", "F"]

p = Paginator(books, 2)
print(p.count)
print(p.num_pages)
print(p.page_range)

page = p.page(10)
print(type(page))
print(page.object_list)

print(page.has_next())
print(page.has_previous())

print(page.next_page_number())

for o in page:
    print(o)