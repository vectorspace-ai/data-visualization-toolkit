import hdbscan

"""
Distances used in HDBSCAN clustering to perform the best clusters
"""

distances = {'braycurtis': hdbscan.dist_metrics.BrayCurtisDistance,
             'canberra': hdbscan.dist_metrics.CanberraDistance,
             'chebyshev': hdbscan.dist_metrics.ChebyshevDistance,
             'cityblock': hdbscan.dist_metrics.ManhattanDistance,
             'dice': hdbscan.dist_metrics.DiceDistance,
             'euclidean': hdbscan.dist_metrics.EuclideanDistance,
             'infinity': hdbscan.dist_metrics.ChebyshevDistance,
             'jaccard': hdbscan.dist_metrics.JaccardDistance,
             'kulsinski': hdbscan.dist_metrics.KulsinskiDistance,
             'l1': hdbscan.dist_metrics.ManhattanDistance,
             'l2': hdbscan.dist_metrics.EuclideanDistance,
             'manhattan': hdbscan.dist_metrics.ManhattanDistance,
             'matching': hdbscan.dist_metrics.MatchingDistance,
             'p': hdbscan.dist_metrics.MinkowskiDistance,
             'rogerstanimoto': hdbscan.dist_metrics.RogersTanimotoDistance,
             'russellrao': hdbscan.dist_metrics.RussellRaoDistance,
             'sokalmichener': hdbscan.dist_metrics.SokalMichenerDistance,
             'sokalsneath': hdbscan.dist_metrics.SokalSneathDistance,
             }
