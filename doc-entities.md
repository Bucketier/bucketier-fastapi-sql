## Bucket
A list of rankings, each item can be expanded into anouther list of rankings.
```
bucket_id: string          (uuid)
name: string               "Food from France"
slug: string               "foodfromfrance"
owner_id: string           (uuid)
owner_display_name: string "John"
owner_color: string        'default' or 'red' etc
```

## List
A specific user's rankings (user_id) of a specific sublist (slug) in a bucket (bucket_id).
Note, slug is the list's path from the bucket.
```
bucket_id: string

list_id: string           "bucket_id:slug:user_id"
name: string              "Fish"
slug: string              "foodfromfrance/fish"
user_id: string           (uuid)
user_display_name: string "Dave" Owner of the list.
user_color: string        'default' or 'red' etc
```

## Item
Just a item in a list.
```
bucket_id: string
list_id: string

item_id: string  "list_id:slug"
name: string     "Chicken Ramen"
slug: string     "chickenramen"
score: number    A number out of 10
review: string   The user's review.
```