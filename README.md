# Dataset Tookit:

## Running the app

We assume that you have `git` and `virtualenv` and `virtualenvwrapper` installed.

    # Clone the code repository 
    git clone https://github.com/vectorspace-ai/data-visualization-toolkit.git

    # Run 'start.sh'
    ./start.sh

    # If the browser does not open, open your browser of choice and go to
    localhost:5000
    
## Updating data directory
You can add custom datasets to the app. All you need to do is place them in the data directory. The app will parse them from there

    # If the local data directory is not already created, create it by
    mkdir data
    mkdir datasets

    # Then extract the datasets inside the datasets folder
    cp "*.csv" data/datasets/.


    
