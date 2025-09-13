# PCA of Premier League Player Statistics

### Line of Work

1. Create 3D-PCA Data from dataset
    - 4 neighborhoods (GK, DR, MF, FW)
    - 11 neighborhoods (11 players on a team)
    - X number of neighborhoods (Football Manager play styles)
2. Save each separate Dataset
3. Use [igraph](https://python.igraph.org/en/stable/tutorial.html) to plot nodes
    - probably wont use edges
    - only for showing player progression
    1. Only show one year
        - explain x, y, z axis meanings
    2. Show all years
    3. Go through sub positions (4 -> 11 -> X)
    4. Show certain players nodes throughout years
        - Big Movements
        - No (litle) movement
        - Popular Players


### Other Tasks

- Could do a 2D PCA but it would probably be similar to 3D
    - Can do just to check or if big difference, talk about
    - 2D analysis + year over year == 3D analysis??
- Mutual Information????
- nationality analysis
- 'how/what position do most french players in PL play most often?'
    - 'Do players from same nation play similarly?'

### Done So Far

- grab data from csvs
- compute PCA function
    - saves to csv 
    - plot pca