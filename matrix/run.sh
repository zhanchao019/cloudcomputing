hadoop jar /usr/hdp/3.0.1.0-187/hadoop-mapreduce/hadoop-streaming.jar \
-files  /home/team13/matrix_zhanchao/MatMulMapper.py,/home/team13/matrix_zhanchao/MatMulReducer.py \
-mapper MatMulMapper.py \
-reducer MatMulReducer.py  \
-input /user/team13/zhanchao/hadoop/input \
-output /user/team13/zhanchao/hadoop/output
