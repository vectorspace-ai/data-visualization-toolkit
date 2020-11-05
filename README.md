# Dataset Tookit:

## About the Toolkit

The Dataset Toolkit(DTK) is meant to visualize datasets provided by VectorSpace AI.
In its current iteration, it has:

    # Graph Network
    # Scatter Plot

## Running the app

We assume that you have `git` and `virtualenv` and `virtualenvwrapper` installed.
It is STRONGLY recommended that you use Python 3

    # Clone the code repository 
    git clone https://github.com/vectorspace-ai/data-visualization-toolkit.git

    # Run 'start.sh'
    ./start.sh

    # If the browser does not open, open your browser of choice and go to
    localhost:5000

## Using the app
Once the browser instance is running, please select the visualization method of choice.
For scatterplot, there are no parameter inputs required by a client.
For Graph Network, the client must specify the following:
    
    # **Rows/Columns:** from which of these vectors the root nodes will be sourced from the dataset.
    # **Root Node:** the base node where the graph network will be generated from. 
    # **Min Relationship Strength:** the minimum threshold for a correlation between two nodes to be included in the graph network calculation. *Default: 0.0001*
    #  **Max Branch Depth:** the maximum depth from the root node will calculate the graph network to. *Default: 3*
    # **Max Branches**: the maximum number of branches per node to be displayed. *Default: 3*
    # **Max Nodes**: the max number of nodes to display in the dataset. *Default: 50*



    
## Updating data directory
You can add custom datasets to the app. All you need to do is place them in the data directory. The app will parse them from there

    # If the local data directory is not already created, create it by
    mkdir data
    mkdir data/datasets

    # Then extract the datasets inside the datasets folder
    cp "*.csv" data/datasets/.


    
