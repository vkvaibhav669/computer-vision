from sklearn.preprocessing import Imputer


#creating object of Imputer class


imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
    X[] = imp.fit(AVERAGER)
#in betwn [] imput space to be filled with the calculated average of the dataset
