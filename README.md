# Improve Tesseract OCR's

Docker Implementation to train Tesseract v. 4

Tesseract 4.0 comes with an LSTM model that can be retrained to improve OCR Accuracy.

## Before Training

- [Choose a name for your model](https://github.com/tesseract-ocr/tesstrain#choose-model-name)

Choose a name for your model. By convention, Tesseract stack models including language-specific resources use (lowercase) three-letter codes defined in ISO 639 with additional information separated by underscore.

- [Ground Truth Data](https://github.com/tesseract-ocr/tesstrain#provide-ground-truth)

Generate ground truth data with set of line images (.tiff or .png) and original transcriptions in .gt.txt files. his list of files will be split into training and evaluation data, the ratio is defined by the <code>RATIO_TRAIN variable</code>.

## Training

- Start a container using the specifications in the Docker file using docker-compose;  Run 

```shell
docker-compose -f docker.dev.yml up
```
- Execute and Interactive Bash Terminal in the running container using

```shell
docker exec -ti train-ocr bash
```
 - Create a ground truth folder and migrate all the training images and transcriptions into it
 -
 ```shell
mkdir -p /app/src/tesstrain/data/<model_name>-ground-truth
cp -a /app/data/ground-truth/* /app/src/tesstrain/data/<model_name>-ground-truth/.
cd /app/src/tesstrain
```
- Time to Train!!!

```shell
make training MODEL_NAME=<model_name> START_MODEL=eng PSM=7 TESSDATA=/usr/local/share/tessdata 
```

To test model

- Modify the script in `src/test.py`
- Run the script 
