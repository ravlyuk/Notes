# GraphQL requests example

## Graphene_django
### GET

``` javascript
{
  persons {
    id
    first_name
    last_name
    birth_date
    phone
    email
    city
    post_code	
    profession
    created_at
  }
}
```

### Create
``` javascript
mutation create_person {
  create_person(     
    first_name: "Peter",
    last_name: "Parker",
    birth_date: "2000-07-04",
    phone: "063-83-41-777",
    email: "peterparker@gmail.com",
    city: "New York",
    post_code: 21177,
    profession: "superhero"){
      person {
        id
        first_name
        last_name
        birth_date
        phone
        email
        city
        post_code	
        profession
        created_at
      } 
  }
}
```

### Update
``` javascript
mutation update_person {
  update_person(id: 1,     
    first_name: "Yevhenii",
    last_name: "Ravliuk",
    birth_date: "1993-07-04",
    phone: "063-83-41-729",
    email: "kobtok1@gmail.com",
    city: "Lviv",
    post_code: 21166,
    profession: "programmer"){
      person {
        id
        first_name
        last_name
        birth_date
        phone
        email
        city
        post_code	
        profession
        created_at
      } 
  }
}
```

### Delete
``` javascript
mutation delete_person {
  delete_person(id: 8){
      deleted
  }
}
```


## Graphene_django_CUI

### Create
``` javascript
mutation {
    create_person(input: {first_name: "Elon", last_name: "Musk", birth_date: "1980-07-04", phone: "0749674912", email: "elonmusk@gmail.com", city: "New York", post_code: 95356, profession: "CEO"}){
        person{
        id
        first_name
        last_name
        birth_date
        phone
        email
        city
        post_code	
        profession
        created_at
        }
    }
}
``` 

### Update
``` javascript
mutation update_person {
  update_person(id: 2, input: {
    first_name: "Yevhenii",
    last_name: "Ravliuk",
    birth_date: "1993-07-04",
    phone: "063-83-41-729",
    email: "kobtok1@gmail.com",
    city: "Lviv",
    post_code: 21166,
    profession: "programmer"
    
  }){
      person {
          id
          first_name
          last_name
          birth_date
          phone
          email
          city
          post_code
          profession
      } 
  }
}
```

### Patch
``` javascript
mutation {
    patch_person(id: 2, input: {city: "Kyiv"}){
        person{
            id
            first_name
           	last_name
          	city
        }
    }
}
```

### Delete
``` javascript
mutation {
    delete_person(id: "1"){
        found
        deleted_id
    }
}
```