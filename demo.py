from us_visa.pipline.training_pipeline import TrainPipeline
from us_visa.constants import DATABASE_NAME

#print(DATABASE_NAME)
pipline  = TrainPipeline()
pipline.run_pipeline()