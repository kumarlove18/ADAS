# Advance-Driver-Assistance-System
ADAS is an innovative system designed to enhance driver safety and improve vehicle operation by providing real-time assistance in identifying potential hazards on the road. Leveraging state-of-the-art technologies such as PyTorch, Data Collection, OpenCV, YOLOv7, Jetson Nano, and HPC, our system offers a comprehensive set of features to assist drivers in making informed decisions while driving.

### Key Features

- **Speed Breaker Detection:** Utilizing computer vision techniques, our system detects unmarked speed breakers on the road, alerting the driver in advance to take appropriate action.

- **Traffic Light Detection:** With advanced image processing algorithms, ADAS identifies traffic lights and provides timely alerts to the driver, ensuring adherence to traffic regulations.

- **Overspeed Warning:** ADAS monitors the vehicle's speed and warns the driver if they exceed the speed limit, promoting safer driving habits and reducing the risk of accidents.

### How It Works

1. **Data Collection:** We collected and annotated a large dataset comprising over 50,000 images of speed breakers and 10,000 images of traffic lights, including a diverse range of scenarios and lighting conditions.

2. **Model Training:** Leveraging the powerful capabilities of YOLOv7, we trained a pre-existing model on our annotated dataset, enabling accurate detection of speed breakers and traffic lights in real-time.

3. **Implementation:** Our system is deployed on Jetson Nano, a high-performance embedded computing platform, ensuring efficient execution of computer vision algorithms in real-time.

### Future Improvements

- **Enhanced Model Accuracy:** Continuously refining and fine-tuning our detection model to improve accuracy and robustness in detecting speed breakers and traffic lights under various environmental conditions.

- **Extended Feature Set:** Exploring additional features such as lane departure warning, pedestrian detection, and collision avoidance to further enhance driver safety and vehicle operation.

- **Integration with Cloud Services:** Implementing cloud-based services for data storage, analysis, and remote monitoring, enabling seamless integration with smart city infrastructure and fleet management systems.
