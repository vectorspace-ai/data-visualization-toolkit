Dataset Tookit Informal Functional Requirements:
(experimental pipeline)

1. Select a data source
    a)select an ontology

2. Create stopwords list for the curren knowledge domain and corpus
    a) This can be done by collecting basic statistics on the corpus
    b) Stopwords would include any terms that have a frequency count <= 2 across the corpus or vector space

3. Pretrain a model with Miriam Websters 60k word dictionary. 

4. Create a correlation matrix dataset from this model

5. Observe relevance in correlations, optimize if necessary 

6. Preprocess for unique identifiers e.g. stock symbols, gene symbols, drug compound names or additional feature attributes that would be used when extracting relationships           

7. Add primary data source to model

8. Add additional data sources to model e.g. molecular biology encyclopedias, papers etc.

9. Generate final correlation matrix dataset

Data interpretation and visualization:
1. Take a vector and extract unique identifiers e.g. stock symbols
2. For each stock symbol, extract its vector and extract the unique identifiers within this vector
3. Create a graph using Highcharts or another cool visualization
4. Implement chartfleau for the coolest visualization: https://www.chartfleau.com/tutorials/d3swarm/

Advanced option/customizations: 

1. Near real-time or support for dynamic updating

2. Using unique identifiers map, apply context-contrlled summarization and link to original papers/documents where summarization is highlighted  
    a) Enable one-click resummarization and display

3. Vector branching for maximum relevancy
### To Run

```
    virtualenv venv
    source/bin/activate venv
    pip install requirements.txt
    go to main directory
    export FLASK_APP=app/application.py
    export PYTHONPATH=$PYTHONPATH:$PWD
    flask run
```

