## Taks on Introduction to Django

# Permissions and Groups Setup

# Permissions
The following custom permissions have been defined for the Book model:

'can_view: Allows viewing book details'
'can_create: Allows creating new books'
'can_edit: Allows editing existing books'
'can_delete: Allows deleting books'

# Groups
Three user groups have been set up with the following permissions:

Viewers:

can_view
Editors:

can_view
can_create
can_edit
Admins:

can_view
can_create
can_edit
can_delete