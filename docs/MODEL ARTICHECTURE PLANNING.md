MODEL ARTICHECTURE PLANNING


Memembership
   -slug
   -type(free,pro,enterprise)
   -price
   -stripe plan id

UserMembership
    -user              (foregin key to default user) 
    -stripe customer id
    -memebership type (foregin key)
    -membership type (foreign key to membership)

Subscription
   -user membership
   -stripe subscription id (foriegnkey to UserMembership )

Course
 -slug
 -title
 -description(ForiegnKey to Membership)
 -allowed memberships

Lesson
    -slug
    -title
    -course(foreignKey to Course)
    -position
    -thumbnail


