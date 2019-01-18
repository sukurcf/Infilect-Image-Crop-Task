You can use the `CropAnImageDirectlyNoAPI.py` to crop the image directly without needeing a REST API.

# Infilect-Image-Crop-Task

Django REST API for cropping image
#### Input:
  - An Image file that needs to be cropped
  - Coordinates - in the form of **[{'x':value,'y':value}, {'x':value,'y':value}, {'x':value,'y':value}, ...]**

#### Output:
  - A base64 encoded string of the cropped PNG file

#### Steps:
    1. Clone the repo into your local `git clone https://github.com/sukurcf/Infilect-Image-Crop-Task.git`.
    2. Install the requirements using `pip install -r requirements.txt`.
    3. Run the server using `python manage.py runserver`.
    4. Use a REST client - preferably Postman client and send POST request to `http://127.0.0.1:8000/file/upload/` with the following parameters in body:
        * file : type - file (select file to be uploaded).
        * coordinates : type - string (a string in the form of input mentioned in Input section) above.
    5. The original and cropped images will be saved on the /media/ folder on server and base64 encoded string of the cropped image will be sent as response.
    6. Copy the response and run the `DecodeAPIresponseToPNGimage.py` and provide appropriate inputs to save the encoded string as image in your local.
    7. If you need to crop the image directly without an API, you can try `CropAnImageDirectlyNoAPI.py`.
