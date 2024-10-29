# Week 3 - Serverless

## Introduction
Data on the web is growing exponentially, with platforms like Google serving as the first source for knowledge. Despite the vast availability of data, much of it is unstructured (in HTML format) and not readily downloadable. This requires expertise to access and utilize effectively for building useful models.

## Web Scraping
**Web scraping** is a technique for converting unstructured data on the web into a structured format that is easier to access and use. 

### How to Scrape?
There are several popular methods for scraping data from the web:

1. **Human Copy-Paste**: Manually copying data is slow and inefficient but can be useful for small tasks.
  
2. **Text Pattern Matching**: Using regular expressions to extract information programmatically.
  
3. **API Interface**: Many websites (e.g., Facebook, Twitter, LinkedIn) offer public/private APIs to retrieve data in a structured format.
  
4. **DOM Parsing**: Programs can retrieve dynamic content generated by client-side scripts and parse web pages into a DOM tree for data extraction.

## Web Scraping Demo
![Web Scraping Demo](https://github.com/tidyverse/rvest/tree/master/demo)

### Example: Scraping IMDb Data
Using the **`rvest`** package in R, we can scrape data from IMDb for the 100 most popular feature films released in 1994.

```r
library(rvest)

# Load the webpage
the_shawshank_redemption <- read_html("https://www.imdb.com/title/tt0111161/")
cast <- the_shawshank_redemption %>%
  html_nodes("#titleCast .primary_photo img") %>%
  html_attr("alt")
cast
```
Output:
``` csharp
[1] "Tim Robbins" "Morgan Freeman" "Bob Gunton" "William Sadler" "Clancy Brown" "Gil Bellows" "Mark Rolston" "James Whitmore" "Jeffrey DeMunn" "Larry Brandenburg" "Neil Giuntoli" "Brian Libby" "David Proval" "Joseph Ragno" "Jude Ciccolella"
```
**Package Installation**
Make sure to install the necessary packages:
```r
install.packages("rvest")
install.packages("httr")
```
**Selector Gadget**
Use Selector Gadget, an open-source tool, to easily select elements on a webpage. This tool helps in identifying the correct HTML tags for scraping.

![Using the selector gadget](https://ceu-cloud-class.github.io/static/0bee7fdb1b13849bd24ae0f360206166/2bf90/selector1.png)

**Scraping Steps**
Check Robots.txt: Always check the robots.txt file of a website to comply with their crawling rules. 
[IMDB Robots.txt] (https://www.imdb.com/robots.txt)
Scrape Various Fields:
Rank:
```r
rank_data_html <- html_nodes(webpage,'.text-primary')
rank_data <- as.numeric(html_text(rank_data_html))
head(rank_data)
# Output: 1, 2, 3, 4, 5, 6
```
Title:
```r
title_data_html <- html_nodes(webpage,'.lister-item-header a')
title_data <- html_text(title_data_html)
head(title_data)
# Output: "The Shawshank Redemption" "Pulp Fiction" ...
```

![Scraping IMDB](https://ceu-cloud-class.github.io/static/75035c46e005bd942247b027b852b62a/42267/selector2.png)
Description:
```r
description_data_html <- html_nodes(webpage,'.ratings-bar+ .text-muted')
description_data <- gsub("\n","", html_text(description_data_html))
head(description_data)
```
Runtime:
```r
runtime_data_html <- html_nodes(webpage,'.text-muted .runtime')
runtime_data <- as.numeric(gsub(" min","", html_text(runtime_data_html)))
head(runtime_data)
```
Genre:
```r
genre_data_html <- html_nodes(webpage,'.genre')
genre_data <- as.factor(gsub(",.*","", gsub("\n","", html_text(genre_data_html))))
head(genre_data)
```
Rating:
```r
rating_data_html <- html_nodes(webpage,'.ratings-imdb-rating strong')
rating_data <- as.numeric(html_text(rating_data_html))
head(rating_data)
```
Director:
```r
directors_data_html <- html_nodes(webpage,'.text-muted+ p a:nth-child(1)')
directors_data <- as.factor(html_text(directors_data_html))
head(directors_data)
```
Actor:
```r
actors_data_html <- html_nodes(webpage,'.lister-item-content .ghost+ a')
actors_data <- as.factor(html_text(actors_data_html))
head(actors_data)
```
Creating a DataFrame: Combine all scraped data into a single DataFrame:
```r
movies_df <- data.frame(Rank = rank_data, Title = title_data,
                         Description = description_data, Runtime = runtime_data,
                         Genre = genre_data, Rating = rating_data,
                         Director = directors_data, 
                         Actor = actors_data)

view(movies_df)
```
Simple Plot: Visualize the data using ggplot2:
```r
library('ggplot2')
ggplot(movies_df, aes(x=Runtime, y=Rank)) +
  geom_point(aes(size=Rating, col=Genre))
```

# Week 3 - AWS Overview

## Amazon Polly
![Amazon Polly](https://ceu-cloud-class.github.io/static/6a88c765c243cb7bb35b975127f01921/eea4a/polly.jpg)

Amazon Polly is a cloud service that transforms text into lifelike speech, enhancing engagement and accessibility in applications. It supports multiple languages and offers a variety of realistic voices, allowing for the development of speech-enabled applications in various regions. Key features include:

- **Pay-per-use Model:** Only pay for synthesized text, with no extra costs for caching and replaying generated speech.
- **High-Quality Speech:** Utilizes neural text-to-speech (TTS) technology for natural-sounding speech with high pronunciation accuracy.
- **Low Latency:** Provides fast responses, suitable for low-latency applications like dialog systems.
- **Extensive Language and Voice Support:** Offers numerous voices in various languages, including options for US and British English.
- **Cost-effective and Cloud-Based:** Reduces local resource requirements, enabling broader language and voice support without significant device resource consumption.

### Use Cases
- Newsreaders
- Games
- eLearning platforms
- Accessibility applications for visually impaired users
- Internet of Things (IoT) applications

### Installation
To install the Amazon Polly package in R:
```r
install.packages("aws.polly", repos = c(getOption("repos"), "http://cloudyr.github.io/drat"))
```

###Setting Up Credentials
You can set AWS credentials directly in R:
```r
Sys.setenv("AWS_ACCESS_KEY_ID" = "mykey",
           "AWS_SECRET_ACCESS_KEY" = "mysecretkey",
           "AWS_DEFAULT_REGION" = "us-east-1",
           "AWS_SESSION_TOKEN" = "mytoken")
```

### Using Polly
To synthesize speech using Polly:
```r
library("aws.polly")
library("tuneR")

vec <- synthesize("Forget that! There are places in this world that aren't made out of stone...", voice = "Joey")
play(vec)  # Play the synthesized speech
```
##Amazon Comprehend

Amazon Comprehend is a natural language processing (NLP) service that analyzes documents to extract insights without needing to provide training data. It can handle text files in UTF-8 format and provides the following capabilities:

-Entity Recognition: Identifies entities such as people and locations in documents.
-Key Phrase Extraction: Extracts important phrases from the text.
-Language Detection: Identifies the primary language in a document (supports 100 languages).
-Sentiment Analysis: Determines the emotional tone of a document (positive, negative, neutral, or mixed).
-Syntax Analysis: Parses each word and identifies its part of speech.

Amazon Comprehend can examine and analyze documents in these languages: English, Spanish, French, German, Italian, Portuguese.

A detailed description of how credentials can be specified is provided at: https://github.com/cloudyr/aws.signature/. The easiest way is to simply set environment variables on the command line prior to starting R or via an Renviron.site or .Renviron file, which are used to set environment variables in R during startup (see ? Startup). They can be also set within R:

```r
Sys.setenv("AWS_ACCESS_KEY_ID" = "mykey",
           "AWS_SECRET_ACCESS_KEY" = "mysecretkey",
           "AWS_DEFAULT_REGION" = "us-east-1",
           "AWS_SESSION_TOKEN" = "mytoken")
```
To install and use Comprehend w/ R:
```r
install.packages("aws.comprehend", repos = c(cloudyr = "http://cloudyr.github.io/drat", getOption("repos")))

library("aws.comprehend")

# simple language detection
detect_language("I have to remind myself that some birds aren’t meant to be caged.")
```
![](https://ceu-cloud-class.github.io/static/deabf62155514fe5589720fe7b20da68/cbe7f/language.png)
```r
detect_sentiment("The world went and got itself in a big damn hurry.")
```
![](https://ceu-cloud-class.github.io/static/061069839a2a97ad02fae24e2a3d369f/c50e3/sentiment.png)

```r
# named entity recognition
txt <- c("The convicts in Shawshank have become so used to the idea of being in prison, that they can't really remember life outside of it.", "Ellis Boyd Redding makes a reference to the fact that prison life is all about routine.")
detect_entities(txt)
```
![](https://ceu-cloud-class.github.io/static/efe53aaa605dfe9f945f5951c3342343/97a96/entities.png)

```r
detect_phrases(txt)
```
![](https://ceu-cloud-class.github.io/static/c3cb5f2b9c547838a07c5dd3bbebb6f6/80521/phrases.png)

## Amazon S3
![](https://ceu-cloud-class.github.io/static/1560da3e4ff1f266ffd99ff434366e3d/5a190/s3.png)

![Documentation](https://cran.r-project.org/web/packages/aws.s3/aws.s3.pdf)
To install the latest development version you can install from the cloudyr drat repository:
```r
# latest stable version
install.packages("aws.s3", repos = c("cloudyr" = "http://cloudyr.github.io/drat"))

# on windows you may need:
install.packages("aws.s3", repos = c("cloudyr" = "http://cloudyr.github.io/drat"), INSTALL_opts = "--no-multiarch")
```
Set credentials:

```r
keyTable <- read.csv("credentials.csv", header = T)
AWS_ACCESS_KEY_ID <- as.character(keyTable$Access.key.ID)
AWS_SECRET_ACCESS_KEY <- as.character(keyTable$Secret.access.key)

#activate
Sys.setenv("AWS_ACCESS_KEY_ID" = AWS_ACCESS_KEY_ID,
           "AWS_SECRET_ACCESS_KEY" = AWS_SECRET_ACCESS_KEY,
           "AWS_DEFAULT_REGION" = "eu-west-1") 
```
The package can be used to examine publicly accessible S3 buckets and publicly accessible S3 objects without registering an AWS account. If credentials have been generated in the AWS console and made available in R, you can find your available buckets using:

```r
library("aws.s3")
bucketlist()
```
If your credentials are incorrect, this function will return an error. Otherwise, it will return a list of information about the buckets you have access to.

### Working with AWS S3 Objects

This package contains many functions useful for working with objects in S3:

- **`bucketlist()`**: Provides the data frames of buckets to which the user has access.
- **`get_bucket()`** and **`get_bucket_df()`**: Provide a list and data frame, respectively, of objects in a given bucket.
- **`object_exists()`**: Returns a logical value indicating whether an object exists. **`bucket_exists()`** provides the same functionality for buckets.
- **`s3read_using()`**: Provides a generic interface for reading from S3 objects using a user-defined function. **`s3write_using()`** offers a generic interface for writing to S3 objects using a user-defined function.
- **`get_object()`**: Returns a raw vector representation of an S3 object. This can be parsed in various ways, such as using `rawToChar()`, `xml2::read_xml()`, `jsonlite::fromJSON()`, and others depending on the file format.
- **`save_object()`**: Saves an S3 object to a specified local file without reading it into memory.
- **`s3connection()`**: Provides a binary-readable connection to stream an S3 object into R, which is useful for reading very large files. **`get_object()`** also allows reading of byte ranges (see the documentation for examples).
- **`put_object()`**: Stores a local file into an S3 bucket. The `multipart = TRUE` argument can be used to upload large files in pieces.
- **`s3save()`**: Saves one or more in-memory R objects to an `.Rdata` file in S3 (analogous to `save()`). **`s3saveRDS()`** is an analogue for `saveRDS()`. **`s3load()`** loads one or more objects into memory from an `.Rdata` file stored in S3 (analogous to `load()`). **`s3readRDS()`** is an analogue for `readRDS()`.
- **`s3source()`**: Sources an R script directly from S3.

## Example Session
```R
library(aws.s3)

# List bucket(s) on S3
bucketlist()

# Make a unique S3 bucket name
my_name <- "ceu-class-"  # Type in your name here
bucket_name <- paste(c(my_name, sample(c(0:3, letters), size = 3, replace = TRUE)), collapse = "")
print(bucket_name)

# Now we can create the bucket on S3
put_bucket(bucket_name)

# Bucket location
get_location(bucket_name)

# Create a text file using the website content:
write("This is a simple text file", "my_content.txt")

# Send the text file to AWS S3 bucket
put_object("my_content.txt", bucket = bucket_name)

# We have data on The Cloud! Check on your browser. Now let's get it back on our computer:
save_object("my_content.txt", bucket = bucket_name, file = "my_content_s3.txt")

list.files()

# Let's delete this object
delete_object("my_content.txt", bucket = bucket_name)

# We're finished with this bucket, so let's delete it.
delete_bucket(bucket_name)
```
### Amazon Translate

![](https://ceu-cloud-class.github.io/static/06bc3f0e8d76e43076f204df8da331e3/081d5/translate.png)
Amazon Translate is a neural machine translation service that delivers fast, high-quality, and affordable language translation. It uses deep learning models for more accurate and natural-sounding translations compared to traditional statistical and rule-based algorithms. Amazon Translate allows you to localize content, such as websites and applications, for international users and to efficiently translate large volumes of text.

**Install**

```r
install.packages("aws.translate", repos = c(getOption("repos"), "http://cloudyr.github.io/drat"))
```
**Example**


```r
library("aws.translate")

# Translate some text from English
translate("Hello World!", from = "en", to = "it")
# Output: [1] "Ciao Mondo!" 
# attr(,"SourceLanguageCode") [1] "en" 
# attr(,"TargetLanguageCode") [1] "it"

# Translate some text to English
translate("Hola mundo!", from = "auto", to = "en")
# Output: [1] "Hello world!" 
# attr(,"SourceLanguageCode") [1] "es" 
# attr(,"TargetLanguageCode") [1] "en"

```

# Amazon Rekognition

Amazon Rekognition makes it easy to add image and video analysis to your applications. You just provide an image or video to the Rekognition API, and the service can identify the objects, people, text, scenes, and activities, as well as detect any inappropriate content. Amazon Rekognition also provides highly accurate facial analysis and facial recognition on images and videos that you provide. You can detect, analyze, and compare faces for a wide variety of user verification, people counting, and public safety use cases.

Amazon Rekognition is based on the same proven, highly scalable deep learning technology developed by Amazon’s computer vision scientists to analyze billions of images and videos daily and requires no machine learning expertise to use. Amazon Rekognition is a simple and easy-to-use API that can quickly analyze any image or video file stored in Amazon S3. Amazon Rekognition is always learning from new data, and we are continually adding new labels and facial recognition features to the service.

## Example (Python Code - Optional)

```python
import boto3

BUCKET = "amazon-rekognition"
KEY = "test.jpg"

def detect_labels(bucket, key, max_labels=10, min_confidence=90, region="eu-west-1"):
    rekognition = boto3.client("rekognition", region)
    response = rekognition.detect_labels(
        Image={
            "S3Object": {
                "Bucket": bucket,
                "Name": key,
            }
        },
        MaxLabels=max_labels,
        MinConfidence=min_confidence,
    )
    return response['Labels']


for label in detect_labels(BUCKET, KEY):
    print("{Name} - {Confidence}%".format(**label))
```

Output
```python
People - 99.2436447144%
Person - 99.2436447144%
Human - 99.2351226807%
Clothing - 96.7797698975%
Suit - 96.7797698975%
```

## Example 2: Face Detection (Optional)

```python
import boto3

BUCKET = "amazon-rekognition"
KEY = "test.jpg"
FEATURES_BLACKLIST = ("Landmarks", "Emotions", "Pose", "Quality", "BoundingBox", "Confidence")

def detect_faces(bucket, key, attributes=['ALL'], region="eu-west-1"):
    rekognition = boto3.client("rekognition", region)
    response = rekognition.detect_faces(
        Image={
            "S3Object": {
                "Bucket": bucket,
                "Name": key,
            }
        },
        Attributes=attributes,
    )
    return response['FaceDetails']

for face in detect_faces(BUCKET, KEY):
    print("Face ({Confidence}%)".format(**face))
    # emotions
    for emotion in face['Emotions']:
        print("  {Type} : {Confidence}%".format(**emotion))
    # quality
    for quality, value in face['Quality'].items():
        print("  {quality} : {value}".format(quality=quality, value=value))
    # facial features
    for feature, data in face.items():
        if feature not in FEATURES_BLACKLIST:
            print("  {feature}({data[Value]}) : {data[Confidence]}%".format(feature=feature, data=data))
```

Output
```python
Face (99.945602417%)
SAD : 14.6038293839%
HAPPY : 12.3668470383%
DISGUSTED : 3.81404161453%
Sharpness : 10.0
Brightness : 31.4071826935
Eyeglasses(False) : 99.990234375%
Sunglasses(False) : 99.9500656128%
Gender(Male) : 99.9291687012%
EyesOpen(True) : 99.9609146118%
Smile(False) : 99.8329467773%
MouthOpen(False) : 98.3746566772%
Mustache(False) : 98.7549591064%
Beard(False) : 92.758682251%

```

##Amazon Transcribe
[demo](https://www.youtube.com/watch?v=09UXBHrAX2A)