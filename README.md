Note: This is a MSR study as part of the MSR course 2022 at UniKo, CS department, SoftLang Team

**Team name**: ALPHA

**Student names**:
- Abdelrahman ALHayek
- AmeerAli Khan 

Underlying paper: https://dblp.org/rec/conf/msr/DabicAB21

### Repository Instructions
0. `model-type` have two choice `[random_forest,svc]` and `combine-labels` also have two choices `[True,False]`. Use `combine-label` if you want to combine label 1-2 as Noice and 3-4 as Expert. Use `synthetic_method` to choose the oversampling technique.

1. Upgrade pip and install the required package: 


    `$pip install --upgrade pip `


    `$pip install -r requirement.txt`
2. Grid search the parameters: 


    `$cd msr_alpha_assignmnet3_2022/process`


    `$python -m hyper_paramter_tuning --model_type <model-type> --combine_labels <combine-labels> --synthetic_method <synthetic_method>`

3. Train the model and generate classification report.


    `$cd msr_alpha_assignmnet3_2022/process`


    `$python -m main --model_type <model-type> --combine_labels <combine-labels> --synthetic_method <synthetic_method>`

4. default values :
    - model_type : **random_forest**
    - combine_labels : **true**
    - synthetic_method: **prowsyn**

Note: In assignment 2 we made a mistake and did comparision without SMOTE (use_smote=False in our code). Below section **'Output delta'** we are mentioning the corrected version.

### Objective of reproduction with subsections as follows:
Description-This paper extends the expertise identification approaches, to the context of third-party software components (external libraries), using a supervised learning. We reproduce the code and compare the over sampling techniques such as PROWSYN with SMOTE 
- **Input data**- The paper focus on three popular libraries: FACEBOOK/REACT (for building enriched Web interfaces), MONGODB/NODE-MONGODB (for accessing MongoDB databases), and SOCKETIO/SOCKET.IO (for realtime communication), to identify experts in these libraries.The selected features (per Github user) like number of commits, number of client projects a candidate expert has contributed to.
- **Output data**- The paper collects the data from mentioned libraries, and train classifiers like RandomForest and SVM to find the experts in these papers, the classifiers are evaluated by precision, recall, F-score.

### Findings of reproduction with subsections as follows:
- **Our Process is slightly different than paper**:,
1. Since Test dataset size is not clear we assume `20%` data for testing (before SMOTE)
2. It not clear if the model is train on all the datasource (react, mongodb, socketio) or trained on each datasource seperately. We trained our model on all the datasource (combination of REACT, SOCKETIO, MONGODB)
3. Author also uses grid search for hyper-parameter tuning but they have not published the choosen value. Hence we did our own hyper-parameter tuning. 
4. Author didnt publish which library they used for SMOTE processing, we used `smote_variants` API for SMOTE.
5. Paper only talks about few feature for filling N/A data and all other feature we have filled N/A with value `-99999`.
6. We are not sure if reported F-measure is macro or weighted average. Hence consired it to be weighted average.

### Please find the comparing of the metrics below for each Models and combine-labels Type
**Output delta** Comparision of paper SMOTE and reproduce  SMOTE: 
1. Author reported maximum `F-measure of 0,56 (MONGODB)` for 3 class classifier. --> We reported `F-measure of 0.43 (MONGODB)`. `Delta of -0.13`
2. For 5 class classification, author only report score for `React` data because other dataset don't have sufficient data. `Precision ranges from 0.0 (Novice 2, SVM)` to `0.50 (Expert 4, Random Forest)`. `F-measure is 0.24 (Random Forest) and 0.15 (SVM)`. --> We report `precision 0.04 (Novice 2, SVM) to 0.49 (Expert 4, RF)`. `F-measure of 0.33 (RF) and 0.28 (SVM)`. Over all there is `precision is almost same with F-measure delta 0.09-0.13`
3. For 3 class classification, author report `precision` results are greater for experts than for novice, both for `REACT (0.65 vs 0.14)` and `MONGODB (0.61 vs 0.60)`, while socketio has the highest precision for `novices (0.52)`. --> We also report higher precision for expert than novice `(1.0 vs 0.33, MONGODB)`. For React precision of expert is higher than `Novice (0.61 vs 0.33)` for socketio expert have highest `precision (1.00)`. `Delta of  (-0.04 vs 0.19) for react. For MONGODB -0.39 and for socketio 0.48`
4. For 3 class classification, author report `recall`, range from `0.09 (REACT, novices)` to `0.83(REACT, experts)`. --> We report recall of `0.10 (REACT, Novice)` and `0.89 (SocketIo, novice)`. `Delta of -0.01 to 0.04`
5. For 3 class classification, author report `F-measure` is `0.36 (REACT)`, `0.56 (MONGODB)` and `0.42 (SOCKETIO)`. --> We report F-measure of `0.5 (REACT)`, `0.43 (MONGODB)`, `0.62 (SOCKETIO)`. `Delta of 0.14, -0.13, 0.2 respectively.` 
6. To see the metrics from each mode type and oversampling technique please check the `notebook/output_analyze_msr.ipynb`. 

### MSR study enhancement 
* **Threat** 
— Internal threat, which is the use of SMOTE of oversampling may not the best technique to fix the class imbalance.
* **Traces** 
— "Furthermore, to tackle the imbalanced behavior of our ground truth, we used a technique called SMOTE, commonly used on several software engineering problems [29]–[32]. But we acknowledge that there are other techniques ," THREATS TO VALIDITY page 285
* **Theory** 
— SMOTE depends on using KNN to find the similar samples and create new samples accordingly, thus SMOTE would create samples that may not exist in reality, that would impact the performance Metrics like Precision, recall , F1 score , so we hypothesize that ProWsyn has a better impact on the classification performance.
* **Methodology** 
— The use of simple ProWsyn -Proximity Weighted Synthetic Oversampling Technique-, to oversample both the labels and train data, which could enhance the performance Metrics like Precision, recall , F1 score .
* **Feasibility** 
— This an evaluation threat, at which we aim to reach a better generalization and better F1 score , thus there is no obvious concessions that would have to be made for this study which is already an MSR study
* **Process** 
— We have changed the oversampling algorithm and kept the same steps as done in assignmnet 2 and the paper
* **Data** 
— We used the same Data set for the three libraries.
* **Results** 
— Classification performance with ProWsyn is almost as good as smote, For the react Library ProWsyn has F1 score `51%` with combined labels for both classifiers which is slighlty better than SMOTE, with regard to MongoDb and SocketIo , ProWsyn has not shown significant imporovment over SMOTE, in addition to having relatively small amount of Data, we can not confirm or deny our hypothesis. we are attaching a screenshot of the comparison below to support our conculsion , from all detailed obervation please go through the `notebook/output_analyze_msr.ipynb`


`Analysis with combine labels (3 Classes)`
![analysis_combinelabels](https://user-images.githubusercontent.com/13449847/189760480-c3f5f257-5fdc-4a60-ac56-909b12c439ac.png)

`Analysis without combine labels (5 Classes)`
![analysis_nocombinelabels](https://user-images.githubusercontent.com/13449847/189760724-a5fd61dd-65ff-4462-99f8-ba6e28ca20b9.png)


### Implementation of reproduction with subsections as follows:
- **Hardware requirements** : Google colab 
- **Software requirements** :sklearn - smote_varients - pandas - numpy and for further information check requirments.txt
- **Validation**: Above screenShot compare the metrics from PROWSYN (Current), SMOTE (Baseline) and Paper (Original). This comparision is done in similar way as done in paper. 
- **Data**: Original training data size is 460 and after apply smote the training size increased to 930 and 726 for 5 classes and 3 classes respectively, while the testing size 115 rows for all libraries 
