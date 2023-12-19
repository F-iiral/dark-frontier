# Dark Frontier

## Overview
Python- (backend) and TypeScript- (frontend) -based online browser game.

## To-Do
### Frontend
- [x] Add missing assets to every page.
- [ ] Add functionality to the `/planet/overview` page.
- [x] Add functionality to the `/planet/buildings` page.
- [x] Add functionality to the `/planet/defenses` page.
- [ ] Add functionality to the `/planet/shipyard` page.
- [ ] Add functionality to the `/planet/fleet` page.
- [ ] Add functionality to the `/planet/technology` page.
- [ ] Add functionality to the `/galaxy` page.
- [ ] Add functionality to the `/alliance` page.
- [ ] Add functionality to the `/chat` page.
- [ ] Add a way to view other user's profiles.

### Backend
- [x] Add functionality to the `/planet` API.
- [ ] Add functionality to the `/fleet` API.
- [ ] Add functionality to the `/user` API.
- [ ] Add functionality to the `/galaxy` API.
- [ ] Add functionality to the `/alliance` API.
- [ ] Add functionality to the `/admin` API.
- [ ] Add a mail system between players.
- [ ] Add an alliance system.
- [ ] Add support for multiple galaxies (subdomains + multiple DBs).

## Requirements
- Python 3.11.4+
- TypeScript 5.3.2+

## Setup
1. Clone the repository to your machine.
2. Install all requirements and dependencies.
3. Create a `.env` file with the following template:
```
DEV_MODE = True
SPIRAL_CIRCLE = True
SPIRAL_COUNT = 3
STAR_CIRCLE = False
STAR_COUNT = 500
RESOURCE_SPEED = 1.0
FLEET_SPEED = 1.0
`````
4. Run the `_setup.py` file to create the database.
5. Run the `_app.py` file in dev mode to compile TypeScript into JavaScript.
