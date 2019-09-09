import numpy as np
import matplotlib.pyplot as plt

def display2dImages(imagesSet,tupleImages, figsize=(70,70)):
    '''
        This function is used to plot several images from a array of multiple
        images, geven (tupleImages) the tuple representing (rows,columns)
        and so nrows*ncolumns images.
        Note that this function is simplistic and sensitive to its usecase.
        we will make it more generic later for general use.
    '''
    nbrObs=max(imagesSet.shape) # We suppose that the "imageSet" number of samples is the largest axis
    imSet=np.reshape(imagesSet, (-1,nbrObs))
    imgDim=int(np.sqrt(imSet.shape[0]))
    nrows, ncols=tupleImages
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize, sharex=True, sharey=True)
    for i, ax in enumerate(axes.flatten()):    
        I=np.reshape(imSet[:,i],(imgDim,imgDim))
        ax.imshow(I,cmap='gray')
    fig.tight_layout() 
