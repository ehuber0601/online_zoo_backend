# Online Zoo App

## Route Table

| url          | route  | method | action                            |
|--------------|--------|--------|-----------------------------------|
| /animals     | index  | GET    | Page with all the animal exhibits |
| /animals/:id | show   | GET    | Show an exhibit                   |
| /animals     | create | POST   | Create a new exhibit              |
| /animals/:id | edit   | PUT    | Edit an exhibit                   |
| /aniamls/:id | delete | DELETE | Delete an exhibit                 |

## Component Tree
- App
    - Navbar
    - Main (Exhibits)
       

## Pages
- Index (All animals)
- Form
- Exhibit (Show)

## Model
- Animal
    - Name (String)
    - Image/Video URL (String)
    - Scientific Name (String)
    - Class (String)
    - Lifespan (String)
    - Fun Fact (String)

## Challenges

## Technologies Used
- Python
- Masonite
- Postgres
- ReactJS
