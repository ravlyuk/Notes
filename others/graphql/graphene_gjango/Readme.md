# GraphQL requests example


``` javascript
{
  all_snippets {
    id
	first_name
    last_name
    birth_date
    sex
    phone
    email
    city
    post_code	
    profession
    created_at
  }
}
```

``` javascript
mutation update_snippet {
update_snippet(id: 1, title: "Python", body: "Minimalistic programming language."){
    snippet {
        id
        title
        body
    } 
}
}
```