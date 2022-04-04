1. "cd detector/YOLOv3/weight/" Download Yolov3.weights from https://pjreddie.com/media/files/yolov3.weights
2. You can use the other YOLOv3 detector to train for your own use and put your own weights file under .\detector\YOLOv3_pytorch\logs
3. Create a virtual environment
4. "pip install -r requirements.txt", pytorch should be installed seperately from https://pytorch.org/ depending on CPU/GPU
   * some packages should be installed manually *
5. Change the "project_root" to your own root string in the /deepsort/.env file
6. Install redis and execute "redis-server.exe redis.windows.conf" to launch the Redis Server
7. "python manage.py runserver" to launch the Django Server

http://127.0.0.1:8000/deepsort/run/1/: starts the tracking thread
http://127.0.0.1:8000/deepsort/stream/: shows the video



Illustration of codes:
1. Detector folder: the detector part contains different detection models. Here exists two YOLOv3 models where one is based on darknet framework that can use pretrained weights (on COCO) on web, while another is implemented by Pytorch that can either use pretrained weights or be trained by yourself. To detect trolly, we are now using the second one, (i.e. YOLOv3_pytorch). Any other state-of-art detection model can be put in this folder, making the interface that get the image/frame as input and send the bounding boxes, confidence and labels as output to the deepsort part.
2. Deep_sort folder: the deep folder contains a CNN model using pretrained weights to extract features for objects. Here it is not useful because all trollys look the same. the sort folder contains main algorithm of tracking, both Kalman filter and Hungarian algorithm. The deep_sort.py file uses mentioned two parts to allocate different IDs to objects.
3. Deepsort folder: this folder contains model part, view part and url configuration for the django server. Tracking thread will open a an additional thread to send the video frame to the model, store the output frame to a thread queue (this can also be implement by Redis or another cache server). Then the gen and live function in the view part can get a frame from the queue each time, encode the image, and return to the server. There is also a function called process_manager which can set environment variables to begin the tracking thread or terminate it by sending url parameters to it. Model part is remained to be developed if there is any data (e.g. coordinates and ids of trollys) collected by tracking algorithm requiring to be stored in the database.
4. Trolly_tracking folder: this folder contains some setting of the "trolly_tracking" app.
5. deepsort.py is a testing demo of tracking algorithm that can test the model locally.
6. manage.py is the entrance of the django server.
7. Details of Utils folder
8. Details of modelweights
