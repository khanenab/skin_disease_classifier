Racial bias is a key concern regarding the development, validation, and implementation of machine learning (ML) models in clinical settings.
There are number of ways defined by which we can mitigate the bias, the approach that we have used is:

    1. In the pre-processing, we can re-sample the existing data and incorporate new data that contains examples of all the skin tones and not only just one.


The obstacle that we had to do the above task is the unavailability of the dataset containing darker skin-tones. We had the images of the skin-disease that contain only the fair skin-toned images and those dataset was also very limited. In order to generate more dataset with darker skin tones and more in number, I have done another project in which I am using the computer vision techniques to change the skin tone of the images while keeping the texture of the images intact, which was important for our task because we only want the skin tone of the images to change while the diseases should remain the same. The script __init__ provided in the other project is used to change the colour of the skin tone. By giving the input images and the RGB value of the darker skin tone that we want in the results, we get the desired skin tone in the output images while keeping the disease area as the same. Following is the example of some of the input images and their output with darker skin tone.

<img src="example_images/example1.png" width="300" alt = "alt text">
<img src="example_images/example1-1.png" width="300" alt = "alt text">

<img src="example_images/example83.png" width="300" alt = "alt text">
<img src="example_images/example95.png" width="300" alt = "alt text">

<img src="example_images/example142_1-1.png" width="300" alt = "alt text">
<img src="example_images/example142_1.png" width="300" alt = "alt text">



Once, I generated all the darker skin tone images from the original data, I used the code provided by the other student and used his technique of sliding window to generate more data from both fair and darker skin tone images. The code of the other student can be found here. https://github.com/aequitas-aod/synthesizer_image/blob/main/generate_images.ipynb

Once I had the desired dataset available for both fair and dark skin tone images, I did the multi-class classification project defined in detail below.

This project is about the multi-class classification of skin-disease dataset. The dataset has 9 diseases/classes that we have to predict. The aim of this project is to detect the bias in the machine learning models. Because our dataset contains only fair skin images. I have taken around 1000 images of each class thus having a total data of about 10k images of our dataset. The RESNET model is trained and is used to test the images to detect the type of skin-disease. The test data has a total accuracy of 91.03 % for fair skin images while as for the dark-skin,the test accuracy is 22.72 % for the same skin diseases. Thus making it clear that our model is biased to darker skin-tones.

In order to remove this bias, I have taken the images of the darker skin tone(generated from the other project) and incorporated then in my dataset. I have added the darker images in each disease data. About 1000 fair skin and 1000 dark-skin images of each skin disease class was taken thus, the total input data is approx 18k. The same RESNET model is trained  for 50 epochs and the test accuracy of both the fair and dark skin tone images was calculated. The fair skin images had the total test accuracy of 90.29% for the fair skin tone images and 84.22% for the dark skin images. Hence, for the machine learning model to be un-biased, we need to train the model with all sort of data so that it can learn the task efficiently and effectively.

| Model Trained on data | Test Accuracy on fair data | Test Accuracy on dark data |
|----------|----------|----------|
| Only fair skin images (approx 10k) |91.03%| 22.72% |
| Both fair and dark skin images (approx 18k | 90.29% | 84.22% |

The results, training graphs, and confusion matrix concerning all the datasets chosen can be found in the results folder of this project.
