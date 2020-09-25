import math
import datetime
import numpy as np
import pandas as pd
from os.path import join
from scipy.spatial import distance
from enum import Enum


class Distances(Enum):
    PEARSON = "pearson"
    UNCENTERED_PEARSON = "uncentered_pearson"
    EUCLIDEAN = "euclidean"
    COSINE = "cosine"


distances_types = ["pearson", "uncentered_pearson", "euclidean", "cosine"]


class CorrelationMatrix:
    def __init__(self, model, columns, rows, context_control):
        self.model = model  # referring to the model object, provided by Arina
        self.columns = columns.copy()  # list of column labels
        self.rows = rows.copy()  # list of row labels
        self.context_control = context_control.copy()  # list of context filters
        self.matrix = []  # the matrix itself
        self.distance = None  # distance calculation method
        self.context_list_verified = False  # flag set to allow "context_controlled_filtering"
        self.label_processing_done = False  # flag set to allow "initialize_matrix"
        self.threshold = None
        # for testing endpoint
        self.keyvalues = []

    # filters out labels that aren't related to the respective contexts
    # CONVERT TENSOR TO NUMPY ARRAY TO SAVE TIME AND PAIN
    def context_controlled_filtering(self):
        remove_context = []
        for context in self.context_control:
            context_vector = self.model.get_vector(context)
            if self.is_vector_in_model(context_vector):
                remove_context.append(context)

        self.context_control = [context for context in self.context_control if context not in remove_context]

        remove_labels = []
        labels = (self.columns + self.rows)
        for label in labels:
            label_vector = self.model.get_vector(label)
            """if there are contexts specified, this block will execute, and check if the label is in the vocabulary
            or the correlation with the context is within the threshold"""
            # NOTE: pearson correlation is set as the standard
            if len(self.context_control) > 0:
                for context in self.context_control:
                    if self.is_vector_in_model(label_vector):
                        remove_labels.append(label)
                    elif self.pearson_correlation(label_vector, self.model.get_vector(context)) < 0.05:
                        remove_labels.append(label)
                    # print(self.pearson_correlation(label_vector, self.model.get_vector(context)))
            # this is executed if the context list is empty, thus only checking if the label is in the vocabulary
            else:
                self.context_control = ["none"]
                if self.is_vector_in_model(label_vector):
                    remove_labels.append(label)

        self.columns = [column for column in self.columns if column not in remove_labels]
        self.rows = [row for row in self.rows if row not in remove_labels]

        # ready to execute next function
        self.label_processing_done = True

    def generate_matrix(self, distance):
        self.distance = distance
        if self.label_processing_done == True:
            if self.distance == Distances.PEARSON.value or self.distance == Distances.UNCENTERED_PEARSON.value:
                self.threshold = 0.05
            elif self.distance == Distances.EUCLIDEAN.value:
                self.threshold = 60
            elif self.distance == Distances.COSINE.value:
                self.threshold = 0.95
            self.matrix = [[0 for x in range(len(self.rows))] for y in range(len(self.columns))]

            for j, row_word in enumerate(self.rows):
                for i, column_word in enumerate(self.columns):
                    score = self.distance_calculation(self.model.get_vector(row_word),
                                                      self.model.get_vector(column_word))
                    """for distnace calculation methods where the smaller values are closer related, 
                    those falling outside the threshold are set to "infinity"(inf) for easier interpretation of the dataset"""
                    if self.distance == Distances.PEARSON.value or self.distance == Distances.UNCENTERED_PEARSON.value:
                        if score > self.threshold:
                            self.matrix[i][j] = score
                        else:
                            self.matrix[i][j] = 0
                    elif self.distance == Distances.EUCLIDEAN.value or self.distance == Distances.COSINE.value:
                        if score < self.threshold:
                            self.matrix[i][j] = score
                        else:
                            self.matrix[i][j] = "inf"

            self.matrix = np.transpose(self.matrix)
        else:
            print('Illegal operation, call "context_controlled_filtering()" first.')
        return self.matrix

    def get_dataset(self):
        # __________________________________CHECK HERE___________________________#
        # here I want so that when this functon is calld, the browser will download the Pandas dataframe
        # don't know if you need to call df.to_csv() too
        return pd.DataFrame(self.matrix, index=self.rows, columns=self.columns)


    def save_dataset(self, path_to_dataset, dataset_filename):
        df = self.get_dataset()
        filename_creted_name = self.distance + "_" + self.model.model_type[0] + "_" \
                               + dataset_filename + "_context_" + "_".join(self.context_control) \
                               + "_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".csv"
        self.path_to_dataset = join(path_to_dataset, filename_creted_name)
        df.to_csv(self.path_to_dataset)
        #
        #
        # This is how I think it would be nice to name the file with distance caluclation method, name of datas source, the contexts specified and time + .csv at the end of course

    def get_keyvalues(self):
        self.keyvalues[:] = []
        self.keyvalues.append({
            "rows": self.rows,
            "columns": self.columns,
            "threshold": self.threshold,
        })
        return self.keyvalues

    def is_vector_in_model(self, vector):
        if self.model.model_type[0] == "bert":
            return np.all(vector.numpy() == 0)
        else:
            return not any(vector)

    def get_vector(self, word):
        return self.model.get_vector(word)

    # pearson correlation
    def pearson_correlation(self, x, y):
        return np.corrcoef(x, y)[1, 0]

    # euclidean distance
    def euclidean_distance(self, x, y):
        return np.linalg.norm(x - y)

    # cosine similarity
    def cosine_similarity(self, x, y):

        return distance.cosine(x, y)

    # uncentered pearson
    def uncentered_pearson(self, x, y):
        sd_x = self.standard_deviation(x)
        sd_y = self.standard_deviation(y)
        sum = 0
        for i in range(len(x)):
            sum += (x[i] / sd_x) * (y[i] / sd_y)
        return (1 / len(x)) * sum

    # standard deviaton for uncentered pearson
    def standard_deviation(self, a):
        sd = 0
        for i in range(len(a)):
            sd += (a[i]) ** 2
        return math.sqrt((1 / len(a)) * sd)

    # sets the selected distance calculation method
    def distance_calculation(self, x, y):
        """if self.model.model_type=="bert":
            x=x.detach()
            y=y.detach()"""
        if self.distance == Distances.PEARSON.value:
            return self.pearson_correlation(x, y)
        elif self.distance == Distances.EUCLIDEAN.value:
            return self.euclidean_distance(x, y)
        elif self.distance == Distances.COSINE.value:
            return self.cosine_similarity(x, y)
        elif self.distance == Distances.UNCENTERED_PEARSON.value:
            return self.uncentered_pearson(x, y)
