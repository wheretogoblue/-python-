bookclub= ('John', 'Peter', 'Curry', 'Mike', 'Kevin')
print("原先的讀書會成員")
for member in bookclub:
    print(member)
    
bookclub_list= list(bookclub)
bookclub_list.extend(['Mary','Tom','Carlo'])
bookclub= tuple(bookclub_list)

print("新的讀書會成員")
for member in bookclub:
    print(member)
