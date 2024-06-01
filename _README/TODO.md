```
/         - dashboard (widgets)
/account  - auth page
/project  - project/issue page
```

## The Site Page Template
- [ ] GET
  - [ ] NavBar Links
    - [ ] Index
    - [ ] Project
      - [ ] Subscribed
      - [ ] Created by User
      - [ ] Created by Other Users
    - [ ] Issue
      - [ ] Subscribed
      - [ ] Created by User
      - [ ] Created by Other Users
    - [ ] Account
      - [ ] Register
      - [ ] LogIn
      - [ ] LogOut

## Account Page
- [ ] account
  - [ ] / - Not needed for now
    - [ ] GET
      - [ ] UI
  - [ ] /Register
    - [ ] GET
      - [ ] UI
    - [x] POST
  - [ ] /Login
    - [ ] GET
      - [ ] UI
    - [x] POST
  - [x] /Logout

## Project Page
- [ ] project
  - [ ] /
    - [ ] GET
      - [ ] Created (owned) Project
      - [ ] Subscribed Project
    - [ ] POST
      - [ ] New Issue
      - [ ] Subscribe to the Project

## (Project) Issue Page
- [ ] project
  - [ ] /
    - [ ] GET
      - [ ] Created (owned) Issue
      - [ ] Subscribed Issue
    - [ ] POST
      - [ ] New Issue
      - [ ] Subscribe to an Issue
  - [ ] created/
  - [ ] followed/
