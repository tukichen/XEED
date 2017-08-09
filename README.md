# Machine Learning to Fighting Against Parkinson

Code and documentation for construction machine learning models to monitor Parkinson's symptoms. 

**Author**:
* [Qiaolin Chen](http://www.linkedin.com/in/qiaolin-chen/)

**Contents** :

- [Background and Data](#background-and-data)
- [Feature Generation and Exploratory Analysis](#EDA)
- [Models](#models)
- [Final Model and Visualization](#final-model)

![alt tag](https://github.com/tukichen/XEED/blob/master/Wearable_device.png)

## Background and Data
### Study Design
Parkinson's disease is an degenerative movement disorder affecting 7-9 millions patients. There is no cure. Physical therapy can help but is evaluation is subjective and limited to short periods of clinic visits. [XEED](https://www.xeedlimits.com) is a company which produces wearable devices to capture motion of patients limbs. These motion data can then be synchronized to smartphones, so that Physical therapists can monitor patients’ movement and symptoms and evaluate the severity of the disease, provide personalized recommendations between therapy sessions to delay disease progression.

In this study, patients and healthy controls subject will come into wear XEED divices on 4 limbs and be monitored for the subsequent 8-9 hours in an clinic for activities and symptoms. Patients will take Parkinson's medications twice during the study period, once at begining of the study and again 4 hours later.  

![alt tag](https://github.com/tukichen/XEED/blob/master/Study_design.png)

### Data Collected
Movement data from the device 
* timestamp
* orientation and acceleration information
There will be an XEED device on each wrist and each ankle that will collect unix time accurate to the second with real world time, acceleration in the X,Y, and Z directions with +/- 1 mg resolution, and orientation with accuracy of +/- 3 degrees in Roll and Pitch, and +/- 5 degrees in Yaw. The orientation is self correcting and referenced to the earth’s magnetic field and gravity. The data were collected at intervals of 32 samples/second. 

For some parts of the study period, the following data are also collected: 
* patient activities walk, resting  
* “ON”, “OFF”, and dyskinetic (DYS) states of patients: occurrence of symptoms like tremors and jerky movements, “dance-like” movements.


### Study Goal
The resting study consists of two phases: (1) resting recognition phase and (2) state determination phase. 

* Phase 1 is to take streams of data from the XEED devices and create a method to reliably identify the times during which resting occurred in PD subjects and healthy controls. 
Resting, defined as near zero acceleration, is a key activity in determining patient states because it is an easily identifiable activity that is performed multiple times throughout the day subconsciously. Resting tremors is a key symptom used in evaluating the severity of the disease. 

* Phase 2 will require differentiating resting features between healthy subjects and PD subjects if any. 
These features should be instrumental in determining the patient’s ON, OFF, or DYS state. A wide range of PD resting data and control resting data will be provided to account for variability across people, gender, body sizes, and time of day. Medication data and United Parkinson’s Disease Rating Scale (UPDRS) data will be provided when available for intra-person comparisons and to avoid false positives. If an accurate state determination can be reached within the scope of the project, the next step will be identifying the UPDRS score that corresponds to the resting pattern. 

## Feature Generation and Exploratory Analysis
Data from the XEED devices stored as binary files were processed and converted to python Pandas dataframes. 
The orientation information encoded as quaternions with an offset (q0, q1, q2, q3) were normalized. 
The acceleration dimensions (ax, ay, az) were also normalized and used to compute magnitude of accelerations.


## Models

### Logistic Regression
### Bayesian Logistic Regression
### XGBoost

## Cross Validation


## Final Model


