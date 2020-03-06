# texture_classification

#### Author : masato shiota  Mar/06/2020

 - codes
   - コードたち. 基本jupyter lab上で
      - 1D-CNN.py, 1D-CNN_3ch.py : 学習判別
      - preprocessing~ : 次元削減、正規化は
      - plot_result.py :精度とかのグラフ作りは
 - logs
   - 学習ログ.
     - events : keras_callbackの. tensorboardとか
     - cm.csv, cm.png : confusion matrix sklearn参照
     - cr.txt : classification report sklearn参照
     - loss_acc.png
     - trainingtime.txt
 - preprocessed
   - 前処理済みデータとその他
     - graph_plot~ とか。　ほとんどグラフ
     - train_~ 前処理したrawdata
 - rawdata
   - 我妻さんから拝借した9種のテクスチャデータ
