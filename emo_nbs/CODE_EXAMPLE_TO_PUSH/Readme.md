## This folder contains the implementation of our EMO-AI model


### Context model: text -> [V,A]
 
<a target="_blank" id="bt" href = "https://colab.research.google.com/github/Kelvinthedrugger/-AI-/blob/main/emo_nbs/CODE_EXAMPLE_TO_PUSH/EMO_AI_context_model/Gradual_unfreeze_example.ipynb">
<!---the image--->
<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab">
</a>
 
  
   
### VA-Regression model: [V,A] -> [S,V,A,F]

 
 
<a target="_blank" id="bt" href = "https://colab.research.google.com/github/Kelvinthedrugger/-AI-/blob/main/emo_nbs/CODE_EXAMPLE_TO_PUSH/EMO_AI_VA_Regression_model/tf_only_FINISH_UNFREEZE_ALL_SEGTEXT_Gradual_unfreeze_Modularized_RN_THIS_ON_PLURK_NEW_arch_1_works_fix_data.ipynb">
<!---the image--->
<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab">
</a>
 
 
 #### Load pretrained model
 
 One can load our pretrained weight as a reference, just use the following code snippet
 
 ```python
# visit the link and click the mouse by oneself will work, too
!wget -q https://www.dropbox.com/s/xji5ztmtwbac296/9826model-20220910T034210Z-001.zip

# for windows user, you might have to manually unzip the file
!unzip 9826model-20220910T034210Z-001.zip

import tensorflow as tf
model = tf.keras.models.load_model("9826model")
model.evaluate(x_test,y_test)
 ```
  
<b>Output</b>

It may seemed like we're overfitting, but it's not, this is the result indeed

![image](https://user-images.githubusercontent.com/59814445/190057707-6c58e683-70a9-4415-b9b8-cec458575642.png)


