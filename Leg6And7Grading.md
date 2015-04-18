####Leg 6

10/10

The work is there for a good update schema, but you're doing a lot of work
on the client side. Look in to tastypie's "filtering" mechanism. Using that,
you can submit the newest id that you have to the server, and it will only
send you back items with data after that. 

####Leg 7

1/10

The code framework is here, but you allow every user to do every operation
on every post. A similar problem exists for Users, but you don't authorize
anyone for the delete method. You could do this easier by disabling
"DELETE" in the Resource itself, using the allowed methods parameter.

You also don't seem to have any authentication at all.

####Notes
