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

Here's a list of other important training parameters that you can explore:

```
Variables

    MODEL_NAME         Name of the model to be built. Default: foo
    START_MODEL        Name of the model to continue from. Default: ''
    PROTO_MODEL        Name of the proto model. Default: OUTPUT_DIR/MODEL_NAME.traineddata
    WORDLIST_FILE      Optional file for dictionary DAWG. Default: OUTPUT_DIR/MODEL_NAME.wordlist
    NUMBERS_FILE       Optional file for number patterns DAWG. Default: OUTPUT_DIR/MODEL_NAME.numbers
    PUNC_FILE          Optional file for punctuation DAWG. Default: OUTPUT_DIR/MODEL_NAME.punc
    DATA_DIR           Data directory for output files, proto model, start model, etc. Default: data
    OUTPUT_DIR         Output directory for generated files. Default: DATA_DIR/MODEL_NAME
    GROUND_TRUTH_DIR   Ground truth directory. Default: OUTPUT_DIR-ground-truth
    CORES              No of cores to use for compiling leptonica/tesseract. Default: 4
    LEPTONICA_VERSION  Leptonica version. Default: 1.78.0
    TESSERACT_VERSION  Tesseract commit. Default: 4.1.1
    TESSDATA_REPO      Tesseract model repo to use (_fast or _best). Default: _best
    TESSDATA           Path to the .traineddata directory to start finetuning from. Default: ./usr/share/tessdata
    MAX_ITERATIONS     Max iterations. Default: 10000
    EPOCHS             Set max iterations based on the number of lines for training. Default: none
    DEBUG_INTERVAL     Debug Interval. Default:  0
    LEARNING_RATE      Learning rate. Default: 0.0001 with START_MODEL, otherwise 0.002
    NET_SPEC           Network specification. Default: [1,36,0,1 Ct3,3,16 Mp3,3 Lfys48 Lfx96 Lrx96 Lfx256 O1c\#\#\#]
    FINETUNE_TYPE      Finetune Training Type - Impact, Plus, Layer or blank. Default: ''
    LANG_TYPE          Language Type - Indic, RTL or blank. Default: ''
    PSM                Page segmentation mode. Default: 13
    RANDOM_SEED        Random seed for shuffling of the training data. Default: 0
    RATIO_TRAIN        Ratio of train / eval training data. Default: 0.90
    TARGET_ERROR_RATE  Stop training if the character error rate (CER in percent) gets below this value. Default: 0.01
```

To test model

- Modify the script in `src/test.py`
- Run the script 
