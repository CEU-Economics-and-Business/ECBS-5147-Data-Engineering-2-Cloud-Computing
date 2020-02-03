---
layout: default
---
[Home](./README.md) | 
[Internet](./internet.md) | 
[AWS](./aws.md) | 
[Serverless](./serverless.md) | 
[Optional - Big Data History](./big_data_history.md) | 
[Spark Overview](./apachespark.md) | 
[Spark DataFrame API, SQL and Internals](spark-continued.md) |
<!--
[Spark Overview](./spark_overview.md).
[Spark DataFrame & SQL API](./sparkAPI.md).
[Spark Internals](./spark_internals.md).
-->
[Help/Resources](./resources.md).

## Using AWS programatically

## Table of Contents
- [Preamble](#preamble)
    + [Glossary and abbreviations](#glossary-and-abbreviations)
  * [Regions](#regions)
  * [Availability-Zones](#availability-zones)
    + [Availability Zones Video](#availability-zones-video)
  * [Edge Locations](#edge-locations)
- [Part 1. AWS Services Overview](#part-1-aws-services-overview)
- [What Services Will Be Tested On The Exam?](#what-services-will-be-tested-on-the-exam)
- [Part 2](#part-2)
  * [Amazon S3 - Stands for Simple Storage Service](#amazon-s3---stands-for-simple-storage-service)
    + [Video 1 - S3 Basics](#video-1---s3-basics)
    + [Video 2 - S3 Netflix Video](#video-2---s3-netflix-high-level-demo)
  * [Data Consistency for S3](#data-consistency-for-s3)
  * [S3 Guarantees:](#s3-guarantees)
  * [S3 Features Overview:](#s3-features-overview)
  * [S3 Storage Classes](#s3-storage-classes)
  * [S3 Charges for:](#s3-charges-for)
  * [S3 Security and Encryption](#s3-security-and-encryption)
  * [Encryption in Transit is achieved by:](#encryption-in-transit-is-achieved-by)
  * [S3 Version Control - Great back-up tool](#s3-version-control---great-back-up-tool)
  * [Cross-Region Replication](#cross-region-replication)
  * [Transfer Acceleration](#transfer-acceleration)
  * [CloudFront (Global)](#cloudfront-global)
  * [Storage Gateway:](#storage-gateway)
- [Part 3](#part-3)
  * [EC2 - Elastic Cloud Compute](#ec2---elastic-cloud-compute)
    + [How Netflix uses AWS EC2 Video](#how-netflix-uses-aws-ec2-video)
    + [EC2 Basics Video](#ec2-basics-video)
  * [Pricing Options](#pricing-options)
    + [On-Demand](#on-demand)
    + [Reserved](#reserved)
    + [Spot](#spot)
    + [Dedicated Hosts](#dedicated-hosts)
  * [EC2 Instance Types](#ec2-instance-types)
- [Part 4](#part-4)
  * [EBS - Elastic Block Storage](#ebs---elastic-block-storage)
    + [Elastic Block Store (EBS) Video](#elastic-block-store-ebs-video)
  * [EBS Volume Types](#ebs-volume-types)
- [Part 6 - Launching an EC2 Instance](#part-6---launching-an-ec2-instance)
    + [What do I need to perform this tutorial?](#what-do-i-need-to-perform-this-tutorial)
  * [Creating an account](#creating-an-account)
  * [Logging into the AWS console](#logging-into-the-aws-console)
  * [What is a Region?](#what-is-a-region)
  * [How much does it cost to use AWS EC2 resources?](#how-much-does-it-cost-to-use-aws-ec2-resources)
  * [How does billing work?](#how-does-billing-work)
  * [Necessary steps for launching an Instance](#necessary-steps-for-launching-an-instance)
    + [Step 1. Choosing an AMI](#step-1-choosing-an-ami)
    + [Step 2. Choosing an Instance Type](#step-2-choosing-an-instance-type)
    + [Step 3. Configuring Instance Details](#step-3-configuring-instance-details)
    + [Step 4. Adding Storage](#step-4-adding-storage)
    + [Storage volume options](#storage-volume-options)
    + [Step 5. Tagging the Instance](#step-5-tagging-the-instance)
    + [Step 6. Configuring a Security Group:](#step-6-configuring-a-security-group)
    + [Step 7. Reviewing the Instance before Launch](#step-7-reviewing-the-instance-before-launch)
    + [Step 8. Assigning a Key Pair](#step-8-assigning-a-key-pair)
    + [Step 9. Reviewing launch status](#step-9-reviewing-launch-status)
    + [Step 10. Examining a new Instance in the EC2 Console](#step-10-examining-a-new-instance-in-the-ec2-console)
    + [Step 11. Logging into an instance](#step-11-logging-into-an-instance)
    + [Step 12. NGINX](#step-12-install-nginx)
  * [Trouble-shooting and advanced topics](#trouble-shooting-and-advanced-topics)
    + [I cannot log into my EC2 instance, what might have gone wrong?](#i-cannot-log-into-my-ec2-instance-what-might-have-gone-wrong)
  * [How do storage volumes appear within a Linux instance on Amazon EC2?](#how-do-storage-volumes-appear-within-a-linux-instance-on-amazon-ec2)
  * [Taking stock of computing resources within an Ubuntu Linux instance](#taking-stock-of-compute-resources-within-an-ubuntu-linux-instance)
  * [Basic setup and administration of an Ubuntu Linux instance](#basic-setup-and-administration-of-an-ubuntu-linux-instance)
  * [Setting up an Apache web server](#setting-up-an-apache-web-server)
  * [What is the difference between the 'Start', 'Stop', 'Reboot', and 'Terminate' (Instance States)?](#what-is-difference-between-the-start-stop-reboot-and-terminate-instance-states)
  * [Tidying up and shutting down AWS resources](#tidying-up-and-shutting-down-aws-resources)
  * [Further reading (Optional)](#further-reading-optional)
  * [Practice Questions](#practice-questions)
  
* * *

## Part 1. Preamble, Regions, Availability Zones (AZ), Edge Locations

#### Preamble
Cloud computing allows users to quickly access an arbitrary amount of computing resources from a distance without the need to buy or maintain hardware themselves. There are many cloud computing services. This note describes the use of Amazon Web Services ([AWS](http://aws.amazon.com/)) and its resources. However, the fundamental concepts covered here will generally apply to other cloud computing services such as [Google Cloud](https://cloud.google.com/) and [Microsoft Azure](https://azure.microsoft.com/), though with substantial differences in the jargon used by each provider.

#### Glossary and abbreviations
- [AWS](http://aws.amazon.com/) - Amazon Web Services. A collection of cloud computing services provided by Amazon. 
- [EC2](http://aws.amazon.com/ec2/) - Elastic Compute. A particular AWS service that provides 'resizable cloud hosting services'. This service allows you to configure and rent computers to meet you compute needs on an as-needed basis.
- [EBS](http://aws.amazon.com/ebs/) - Elastic Block Storage. A data storage solution offered through the EC2 service. This service allows you to rent disk storage and associate that storage with your compute resources. EBS volumes are generally backed by SSD devices. EBS volumes can only be directly attached to a single EC2 instance at a time.
- [S3](http://aws.amazon.com/s3/) - Simple storage service. A storage service that is cheaper than EBS and allows for storage of larger amounts of data with some drawbacks [compared to EBS TODO](http://www.tomsitpro.com/articles/cost-of-the-cloud-book,2-694-2.html). S3 volumes store data as objects that are accessed by an API or command-line interface or other application designed to work with S3. EBS volumes, on the other hand, can be mounted (directly connected to an EC2 instance) as if they were a local disk drive associated with the Instance.
- [SSD](http://en.wikipedia.org/wiki/Solid-state_drive) - Solid state drive. A particular type of storage hardware that is generally faster and more expensive than traditional hard drives.
- [HDD](http://en.wikipedia.org/wiki/Hard_disk_drive) - Hard disk drive. A particular type of storage hardware that is generally cheaper and larger but slower than SSD. HDD drives are traditional hard drives that access data on a spinning magnetic disk.
- [Ephemeral storage](http://stackoverflow.com/questions/11566223/what-data-is-stored-in-ephemeral-storage-of-amazon-ec2-instance) - Also known as Instance Store storage. Data storage associated with an EC2 instance that is local to the host computer. This storage *does not persist* when the instance is stopped or terminated. In other words, anything you store in this way will be lost if the system is stopped or terminated. Instance store volumes may be backed by SSD or HDD devices.

### Regions

**AWS Region** is a physical, geographical area or location, consisting of 2 or more Availability Zones.

**_Current regions across the world:_**

- US East (N. Virginia) - `us-east-1`
- US East (Ohio) - `us-east-2`
- US West (Northern California) - `us-west-1`
- US West (Oregon) - `us-west-2`
- Canada (Central) - `ca-central-1`
- EU (Frankfurt) - `eu-central-1`
- EU (Ireland) - `eu-west-1`
- EU (London) - `eu-west-2`
- EU (Paris) - `eu-west-3`
- Asia Pacific (Tokyo) - `ap-northeast-1`
- Asia Pacific (Seoul) - `ap-northeast-2`
- Asia Pacific (Osaka-Local) - `ap-northeast-3`
- Asia Pacific (Singapore) - `ap-southeast-1`
- Asia Pacific (Sydney) - `ap-southeast-2`
- Asia Pacific (Mumbai) - `ap-south-1`
- South America (Sao Paulo) - `sa-east-1`

### Availability-Zones

- **AWS Availability Zones** are one or more discrete data centers, each with redundant power, networking and connectivity housed in separate facilities. Deploying your application across multiple Availability Zones is useful for redundancy, low latency and fault tolerance.

**_Regions with multiple Availability Zones:_**

- US East
  - Ohio (3)
  - North Virginia (6)
- US West
  - Oregon (3)
  - Northern California (3)
- Canada
  - Central (3)
- South America
  - Sao Paulo (3)
- Europe
  - Ireland (3)
  - Frankfurt (3)
  - London (3)
  - Paris (3)
- Asia Pacific
  - Singapore (3)
  - Seoul (2)
  - Tokyo (4)
  - Mumbai (2)
  - Sydney (3)
  - Beijing (2)
  - Ningxia (2)
  
#### Availability Zones Video
  
[![AZ](assets/AZ.png)](https://www.youtube.com/watch?v=ET_CSqdGsYg "Availability Zones")

### Edge Locations

- **AWS Edge Locations** are locations [around the world](https://aws.amazon.com/about-aws/whats-new/2019/10/cloudfront-south-america-200-edge-location/) meant for caching content, enhancing the user experience, reducing latency. Edge locations are specifically used by two AWS Services, AWS Cloudfront and AWS CDN. For example, if you use Amazon's services for hosting a website, your website's images can be copied to multiple locations to make sure every request to that image is fulfilled from a server that is geographically close to you. Every Region has its own set Availability Zones and Edge Locations. Edge locations can be located in a country that isn't listed as an availability zone (think about this as an independent data center).

## Part 1. AWS Services Overview

Here is a list of some of the more important AWS services for your reference. We only cover a few of them in the class.

**Compute:**
-    `EC2` - Elastic Compute Cloud
-    `EC2 Container Services` - Containerization Docker 
-    `Elastic Beanstalk` - Plug and Play Web application deployment - for developers
-    `Lambda (serverless)` - Code/Functions uploaded to the cloud to run at different points

**Storage:**
-    `S3` - Simple Storage Service - object-based storage - buckets
-    `EFS` - Elastic File System
-    `Glacier` - Data Archival 
-    `Snowball` - Physically move large amounts of data to aws data center

**Databases:**
-    `RDS` - Relation Database Service - postgres, mysql, oracle
-    `DynamoDB` - Non-Relational DB
-    `Elasticache` - Fully in-memory database
-    `Redshift` - Data Warehousing Business Intelligence, complex queries
    
**Networking and Content Delivery:**
-    `VPC (highlight)` - Amazon virtual private cloud - virtual datacenter - configure avail zones, firewall, network acl etc.
-    `Cloudfront` - AWS content delivery network, store assets specific regions around the world
-    `Route 53` - AWS DNS service - lookup ip to get ipv4 and ipv6 address

**Machine Learning:**
-    `Sage maker` - Managed notebook environment
-    `Comprehend` - Sentiment analysis
-    `Deep lens` - Computer vision on camera, a physical piece of hardware
-    `Lex` - Chatbot engine. This powers Alexa 
-    `Polly` - text to speech, voices sound real
-    `Rekognition` - Image processing
-    `Amazon translate` - Translate to other languages
-    `Amazon transcribe` - Speech recognition

**Analytics:**
-    `Athena` - SQL queries ins S3 buckets, serverless
-    `EMR` - elastic map reduce - processing large amounts of data, chops data up for analysis
-    `Kinesis` - solutions architect highlight, ingesting large amounts data
-    `Kinesis Video streams` - ingesting streams and analyze    
-    `Quicksight` - business intelligence tool
-    `Glue` - ETL tool (extract transform load)

**Security Identity and Compliance:**
-    `IAM` - identity access management

**AR/VR:**
-    `Sumerian` - tools to create an environment, super new

**Application Integration:**
-    `SNS` - Notification services

**Customer Engagement:**
-    `Simple Email Service` - send emails through Amazon's email service

**IOT:**
-    `iOT` - devices sending sensor information
-    `iOT Device Management` - device management
-    `Amazon FreeRTOS` - OS for microcontrollers

* * *

## What Services Are you expected to know?
- `EC2`
- `S3`, `Glacier`, `EBS`
- `Transcribe`
- `Translate`
- `Comprehend`
- `Rekognition`
- `Polly`

* * *

## Part 2

### Amazon S3 - Stands for Simple Storage Service
- S3 provides secure, durable, highly-scalable object storage. 
- Store and retrieve any amount of data from anywhere on the web
- Safe place to store your files
  - Object-based storage up to 5TB (Objects consist of: KEY - name of the object, VALUE - data that is made up of a sequence of bits, VERSION ID - important for versioning, S3 allows you to have multiple versions of your files, METADATA - data about data you are storing, SUBRESOURCES - access control lists torrent)
- Unlimited storage
- **Files are stored in Buckets -> folder in which you store your files.**
- **Buckets must be unique globally.** When you create a bucket it gets a web address. That's why it has to be unique.
- When you upload to S3, you will receive HTTP 200 code if successful

#### Video 1 - S3 Basics
[![S3](assets/S3.png)](https://www.youtube.com/watch?v=f9hXcxHnQuE "S3 Basics")

#### Video 2 - S3 Netflix [High Level] Demo
[![S3Netflix](assets/S3Netflix.png)](https://www.youtube.com/watch?v=06AQA3xXXLA "How Netflix uses AWS")


### Data Consistency for S3
- Read  after Write consistency for PUTS of new objects
  - If you upload a file you are able to read it immediately, you are able to read it straight after writing to it -> you are doing a PUT of that object into S3
- Eventual consistency for overwrite PUTS and DELETES
- If you update that object / delete == eventual consistency
- If you update an existing file/ delete a file and read it immediately you may get the older version or not. Changes to objects can take some time to propagate. 

### S3 Guarantees:
- Built for 99.99% availability for the S3 platform
- Amazon guarantees 99.999999999% durability for S3 information (Tip: 11 9s!)

### S3 Features Overview:
- Tiered Storage Available
- Lifecycle Management 
- Versioning
- Encryption
- Secure your Data using Access Control Lists and Bucket Policy


### S3 Storage Classes

| S3 STANDARD       | S3 - IA         | S3 ONE ZONE - IA |
|:-------------|:------------------|:-------------|
|99.99% availability 99.999999999% durability stored redundantly across multiple devices in multiple facilities and is designed to sustain the loss of 2 facilities concurrently. | Infrequently Accesses: For data that is accessed less frequently but requires rapid access when needed. Lower fee than S3 but you are charged for retrieval fee.| For when you want a lower cost option for infrequently accessed data, but do not require the multiple Availability Zone data resilience. Stored in one Availability Zone.| 


| S3 - INTELLIGENT TIERING  | S3 - GLACIER       | S3 - GLACIER DEEP ARCHIVE |
|:-----------------|:-----------------|:-----------------|
|Designed to optimize costs by automatically moving data to the most cost-effective access tier without performance impact or operational overhead.| Secure, durable, and low-cost storage class for data archiving. You can reliably store any amount of data at costs  that are competitive with or cheaper than on-premise solutions. Retrieval times configurable from minutes to hours | S3's lowest-cost storage class where a retrieval time of 12 hours is acceptable.| 


### S3 Charges for:
- Storage
- Requests
- Storage Management Pricing
- Data Transfer Pricing
- Transfer Acceleration: fast, easy, secure transfer of files over long distances between end-users and an S3 bucket. 
- Cross-Region Replication Pricing: I.e. When you upload an object to `us-east-1` and cross-region replication is turned on, the object will be replicated automatically to your bucket in Sydney. 
- S3 is not suitable to install an operating system / database on, because it is object-based storage.

### S3 Security and Encryption
- By default all newly created buckets are private. 
- You can set up access to your buckets using 
  - 1: bucket policies (bucket level)
  - 2: Access Control Lists (ACL) - individual objects
- S3 buckets: can be configured to create Access Logs, which log all requests made to the S3 bucket. This can be sent to another bucket and even to another bucket in another account.

### Encryption in Transit is achieved by:
- https -> secured
- Always achieved by using RSA
- Encrypt at Rest (source side) is achieved by:
  - AWS Key Management Service, Managed Keys - SSE-KMS
 
### S3 Version Control - Great back-up tool
Using Versioning with S3:
- Stores all versions of an object (including all writes and deletes of an object)
- Once enabled, versioning cannot be disabled, only suspended
- Integrates with Lifecycle Rules
- Lifecycle Management and Glacier integration


## Part 3

### EC2 - Elastic Cloud Compute

AWS EC2 is a web service that provides resizable compute capacity in the cloud. EC2 reduces the time required to obtain and boot new server instances to minutes, allowing you to quickly scale capacity, both up and down, as your computing requirements change.

EC2 has changed the economics of cloud computing by allowing you to pay only for capacity that you actually use. EC2 provides developers with the tools to build failure resistant applications and isolate themselves from common failure scenarios.

#### How Netflix uses AWS EC2 Video
[![EC2Netflix](assets/EC2Netflix.png)](https://www.youtube.com/watch?v=izyqJPl9wW8 "EC2 Netflix Video")

#### EC2 Basics Video
[![EC2](assets/EC2.png)](https://www.youtube.com/watch?v=dO1X7QG_4xw&t=3s "EC2 Basics Video")

### Pricing Options

#### On Demand

- Allows you to pay a fixed rate by the hour (or by the second) with no commitment.

**_Use Cases_**

- Perfect for users that want the low cost and flexibility of EC2 without any of the upfront payment or long term commitment.
- Applications that cannot be interrupted.
- Applications being developed or tested on EC2 for the first time.

#### Reserved Instances (RI)

Provides you with a capacity reservation, and offer a significant discount on the hourly charge for an instance. 1 year or 3 years terms.

**_Use Cases_**

- Applications with steady-state or predictable usage
- Applications that require reserved capacity
- Users can make upfront payments to reduce their total computing costs even further
  - Standard RIs (Up to 75% off on-demand)
  - Convertible RIs (Up to 54% off on-demand) feature the capability to change the attributes of the RI as long as the exchange results in the creation of Reserved Instances of equal or greater value. Ability to go from CPU intensive instance to Memory intensive.
  - Scheduled RIs are available to launch within the time window you reserve. This option allows you to match your capacity reservation to predictable recurring schedule that only requires a fraction of a day, a week, or a month.

#### Spot

Enables you to bid whatever price you want for an instance capacity, providing for even greater savings if your applications have flexible start and end times.

**Use Cases**

- Applications that have flexible start and end times.
- Applications that are only feasible at very low compute prices
- Used for single compute instances to save on costs.

#### Dedicated Hosts

[Physical EC2 server](https://aws.amazon.com/ec2/dedicated-hosts/) dedicated for your use. Physical CPUs, Physical Memory, ..., just like your laptop. Dedicated Hosts can help you reduce costs by allowing you to use your existing server-bound software licenses (I.e. licenses where you pay per CPU). Dedicated Hosts also help you stay compliant to corporate regulations.

**Use Cases**

- Useful for regulatory requirements that may not support multi-tenant virtualization.
- Great for licensing which does not support multi-tenancy or cloud deployments
- Can be purchased On-Demand (hourly).
- Can be purchased as a Reservation for up to 70% off the On-Demand price.

### EC2 Instance Types

*You won't need to know these by heart.*

| Family | Specialty                     | Use Cases                       |
| :------:|:-----------------------------:| :------------------------------:|
| F1     | Field Programmable Gate Array | Genomics research, financial analytics, real-time video processing, big data etc|
| I3      | High Speed Storage            | NoSQL DBs, Datawarehousing |
| G3      | Graphics Intensive            | Video Encoding / 3D Application Streaming|
| H1      | High Disk Throughput          | MapReduce-based workloads, distributed file systems such as HDFS and MapR-FS |
| T2      | Lowest Cost General Purpose   | Web Servers / Small DBs |
| D2      | Dense Storage                 | Fileservers / Data Warehousing / Hadoop |
| R4      | Memory Optimization           | Memory Intensive Apps/DBs |
| M5      | General Purpose               | Application Servers |
| C5      | Compute Optimized             | CPU Intensive Apps / DBs |
| P3      | Graphics / General Purpose GPU | Machine Learning, Bit Coin Mining etc |
| X1      | Memory Optimized               | SAP HANA / Apache Spark |


**How to remember EC2 instance types F.I.G.H.T.D.R.M.C.P.X**
  - **_F_** - FGPA
  - **_I_** - IOPS
  - **_G_** - Graphics
  - **_H_** - High Disk Throughput
  - **_T_** - Cheap General Purpose (think T2 Micro)
  - **_D_** - Density
  - **_R_** - Ram
  - **_M_** - Main choice for general purpose applications
  - **_C_** - Compute
  - **_P_** - Graphics(Pics)
  - **_X_** - Extreme Memory

* * *

## Part 4

### EBS - Elastic Block Storage

Amazon EBS allows you to create storage volumes and attach them Amazon EC2 instances. Once attached, you can create a file system on top of theses volumes, run a database, or use them in any other way you would use a block device. EBS volumes are placed in a specific Availability Zone, where they are automatically replicated to protect you from the failure of a single component.

`_TLDR; A disk in the cloud that you attach to your EC2 instances_`

#### Elastic Block Store (EBS) Video
[![EBS](assets/EBS.png)](https://www.youtube.com/watch?v=S0gzrxsVQHo "Elastic Block Store (EBS)")


### EBS Volume Types

- General Purpose SSD (GP2)
  - General purpose, balances both price and performance.
  - Ratio of 3 IOPS per GB with up to 10,000 IOPS and the ability to burst up to 3000 IOPS for extended periods of time for volumes at 3334 GB and above
- Provisioned IOPS SSD (IO1)
  - Designed for I/O intensive applications such as large relational or NoSQL databases.
  - Use if you need more than 10,000 IOPS
  - Provision up to 20,000 IOPS per volume
  - Super high performance
- Throughput Optimized HDD (ST1)
  - Big Data
  - Data warehouses
  - Log processing
  - Cannot be a boot volume
- Cold HDD (SC1)
  - Lowest cost storage for infrequently accessed workloads
  - File server
  - Cannot be a boot volume
- Magnetic (Standard)
  - Lowest cost per GB of all EBS volume types that is bootable. Magnetic volumes are ideal for workloads where data is accessed infrequently, and applications where the lowest storage cost is important


* * *

## Part 6 - Launching an EC2 Instance

#### What do I need to perform this tutorial?
- A computer with access to the internet, a Web Browser, and a command-line terminal application (e.g. `Terminal` on a Mac, `putty` on Windows, etc.)
- We are going to access the Amazon EC2 console in your web browser and use it to configure and rent a remote computer from Amazon. 
- We are then going to log into that computer from the command line using a terminal application. 
    - The computer you are working on can be almost anything and could be running Windows, Mac OSX, or Linux. 
 - The computer that we configure and rent from Amazon will be a Linux machine (though there are many other possibilities). - - You will use the terminal application on your computer to remotely log in to this computer. 
 - The Amazon AWS computer you rent will be physically located somewhere that is likely far away from you. 
 - Depending on the `Region` you select in Amazon AWS it could be physically located in one of several large compute warehouses in North America, South America, Europe or Asia. **Make sure that you use the Ireland Region in this class.** 

***
**Google Data Center, The Dalles, Oregon ([source](http://en.wikipedia.org/wiki/File:Google_Data_Center,_The_Dalles.jpg)):**
![Image of a data center](Images/AWS/DataCenter.jpg)

- Since we are going to create an Amazon instance that is running a Linux operating system you will need to use your knowledge of working at a Linux command line. For reference, look up your notes from the Different Shapes of Data class. 

### Creating an account
**(You do not need to create an account for this course, but this is how you would do it:)**
- In order to use AWS for the first time, you will need to create an account. 
- In order to create and run instances as described, you will need to associate a credit card with that account for billing purposes. Refer to the sections below on how billing works, how to estimate costs, and how to ensure that you have properly shut down everything that you could be billed for. 
- To log into AWS, go to [aws.amazon.com](http://aws.amazon.com/) and hit the [Sign In to the Console](https://console.aws.amazon.com/console/home) button as shown below. 
- If needed, create an account and activate it by associating a credit card. 

### Logging into the AWS console

**How we are going to do this:**
- Please follow this URL: https://ceu.signin.aws.amazon.com/console . This is the login page of CEU's official AWS account.
- Username: First part of your CEU email address (e.g example@ceu.edu -> `example` == username)
- Password: TBA
- Once you are logged in, select `EC2` from the list of Amazon Web Services. This tutorial is entirely focused on `EC2` (with some mention of `S3`) so the `EC2` console will be the starting point for many of the activities described below.

* * *

**AWS log in:**

![AWS-Login](Images/AWS/console-login.png)

* * *
* * *
**Before launching and using an EC2 instance please make sure to create a Security Group by following the steps described here:**

**STEP 1:** After logging in: Go to `Services` -> `EC2` -> `Security Groups`
![AWS-Security-Group](Images/AWS/security-group-aws.png)

**STEP 2:** Click `Create Security Group`
*Note: When you create an `Inbound rule` and `Outbound rule` is created automatically, so you can leave that empty. Security Groups are stateful. So if you allow HTTP in, it is automatically allowed out as well.*
- Set up an HTTP and an SSH protocol:
![AWS-Security-Group](Images/AWS/sec-rules.png)

After creation, you will see two HTTP rules and two SSH rules;
- `HTTP 0.0.0.0/0`  -> IPv4
- `HTTP ::/0` -> IPv6
- `SSH 0.0.0.0/0` -> IPv4
- `SSH ::/0` -> IPv6

If you make a change to a Security Group - that change takes effect immediately. In this class, you will need to open port 8787 TCP to the world to get SSH access to your instances. 
- You can attach more than one Security Group to an EC2 instance.

Now create your EC2 instance and later attach this Security Group to it by clicking on `Instances` -> `Select your EC2 Instance` -> `Actions` -> `Networking` -> `Change Security Groups` -> Then select this Security Group and assign it to your EC2 instance.

![AWS-Security-Group](Images/AWS/sg-assign-aws.png)


* * *

**List of AWS services (select EC2 for this tutorial):**
![AWS-Services](Images/AWS/AWS-Services.png)
***
**The AWS EC2 dashboard:**
![AWS-EC2-Dashboard](Images/AWS/AWS-EC2-Dashboard.png)
***

### What is a Region?
- As discussed before, an AWS `Region` is a set of compute resources that Amazon maintains (each like the `Data Center` image shown above). 
- Each `Region` corresponds to a physical warehouse of compute hardware (computers, storage, networking, etc.). 
- At the time of writing, there are 8 regions: `(US East (N.Virginia)`, `US West (Oregon)`, `US West (N. California)`, `EU (Ireland)`, `EU (Frankfurt)`, `Asia Pacific (Singapore)`, `Asia Pacific (Tokyo)`, `Asia Pacific (Sydney)`, and `South America (Sao Paulo)`.
- When you are logged into the AWS EC2 console you are always operating in one of these 8 regions. 
- The current region is shown in the upper right corner of the console between the `User` menu and the `Support` menu. 
- It is important to pay attention to what region you are using for several reasons. First, when you launch an EC2 instance, this happens in a specific region. 
  - If you switch regions later, you will not see this instance. 
  - To find info in the console you will have to switch back to the region where that instance was created. 
    - The same reasoning applies to EBS volumes, AMIs, and other resources. 
    - These are tracked within a region. Second, the cost to use many AWS resources varies by region. 
    - Third, since each region is located in a different part of the world, this may influence network performance when you are accessing the instance and especially if you need to transfer large amounts of data in or out. 
    - For example, if you are working in the US and you are going to be uploading RNA-seq data to EC2 instances, it probably does not make sense to create those instances in `Asia Pacific (Sydney)`. 
- Generally, you should choose a region that is close to you or your users. 
  - But the cost is also a consideration. 
  - It is important to be aware of regions when it comes to billing because if you are using resources in multiple regions it is easy to lose track of what you have running and you might wind up paying for something that you forgot to shut down. 
- We will discuss billing and cost in further detail below.

***
**The `Region` menu in the EC2 console:**
![AWS-EC2-Regions](Images/AWS/AWS-EC2-Regions.png)
***

### How much does it cost to use AWS EC2 resources?
- Estimating the cost to use AWS resources can get complicated.  
- For the most part, when you launch an EC2 instance or create an EBS or S3 volume, you are renting and reserving that resource. 
- You will generally be charged for as long as you reserve that resource regardless of how you use it. 
  - For example, if you rent an 8-core machine with 1Tb of the disk, and 64Gb of RAM, once you start that machine you will be charged an hourly rate for as long as it is running. 
    - Even if you do not use it much. 
    - Even if you do not log into it at all! 
    - You have reserved it, it is being run for you, that resource can not be rented to someone else, so you must pay for it. 
- To get a sense of how much particular resource costs, spend some time examining the [AWS EC2 Pricing](https://aws.amazon.com/ec2/pricing/) list. Here is an even better site for checking EC2 prices: https://ec2instances.info/ 
- Remember that `Region` can influence cost, so once you decide on the type of resources you need you should compare the cost of that resource across multiple regions. 
- The pricing list is an extremely long page, broken down into several major categories: 
- `Free Tier` (lightweight resources you can experiment with for free) 
- `On-Demand Instances` (rent by the hour, as we do in this tutorial)
- `Reserved Instances` (get a discount by renting longer term)
- `Reserved Instance Volume Discounts` (get further discounts by being an enterprise-scale user)
- `Spot Instances` (bid for unused Amazon EC2 capacity in an open market)
- `Data transfer` (moving data in and out of EC2)
- `EBS-Optimized Instances` (for high-performance file I/O)
- `Amazon Elastic Block Store` (rent storage volumes separately from Instances)
-  etc.  
- Amazon provides a [Monthly Calculator](http://calculator.s3.amazonaws.com/index.html) to help you predict what your costs might look like.

- In this explanatory section, we are going to use an `On-Demand Instance`. 
    - Let look more closely at that section of the [pricing list](https://ec2instances.info/) by referring to the example screenshot below. 
    - Note that we have selected `US West (Oregon)` for now as an example as our region and we are looking at the `General Purpose` section of the table and assuming that we will launch a `Linux` instance. 
    - These tables enumerate the features of various computer configurations that you can rent by the hour. 
    - Consider a particular instance type in this table, for example, `m3.xlarge`.  
    - For this instance, we are told the number of CPUs that will be available on the machine (4), the amount of memory (15 GiB), the storage that will be pre-configured (2 x 80GB SSD drives), and the cost per hour to rent this machine ($0.140 per Hour).  
    - Note how much jargon is used in these tables.
      - Memory is reported in GiB and storage is reported in GB ([1GiB ≈ 1.074GB](http://en.wikipedia.org/wiki/Gibibyte)). 
      - For the number of CPUs, we are told both the number of vCPUs (virtual CPUs) and ECUs ([Elastic Compute Units](http://aws.amazon.com/ec2/faqs/#What_is_an_EC2_Compute_Unit_and_why_did_you_introduce_it)). 
      - A virtual CPU is a reference to the number of physical CPUs that are available on the machine. 
      - It is referred to as `virtual` because we are actually creating a [virtual machine](http://en.wikipedia.org/wiki/Virtual_machine) when we create an EC2 instance. 
      - This virtualization allows Amazon to create a set of smaller virtual computers of varying specifications from larger physical computers that they maintain. 
      - An ECU is a unit of computing that is meant to allow more accurate comparisons between machines that might have different generations of CPUs, recognizing that not all CPUs are created equally. 
      - The storage descriptions for EC2 instances may use the terms: `EBS only`, `SSD`, and `HDD`.  
- We will discuss EBS (Elastic Block Storage) in more detail below, but briefly, EBS allows us to define one or more storage volumes of almost any size we wish. The hardware details of that storage will be handled for us behind the scenes. 
- EBS volumes exist independently of an EC2 machine and can be moved from one machine to another and the contents can be stored and attached to multiple EC2 instances over time (though only one instance at a time). 
- `SSD` refers to a solid state drive that is associated with the machine. 
- `HDD` refers to a hard disk drive that is associated with the machine. 
- `SSD` drives tend to be higher performance than `HDD` but also more expensive per unit of storage space. 
- When an instance indicates that it has `2 x 40 SSD` this means that it has two solid state drives, and each are 40GB in size.  
- The `SSD` and `HDD` drives associated with each instance and described in the pricing list are considered `ephemeral`. 
- We will discuss this important concept in more detail below.     

***
**An example AWS EC2 price list:**
![AWS-EC2-PriceList](Images/AWS/AWS-EC2-PriceList.png)
***

### How does billing work?

- Generally, you get an accounting of usage and cost on a 30-day cycle. 
- You can get more detailed information on your account by going to the `Billing and Cost Management` section of the `User` menu in the EC2 console
- You can also refer to the [billing section](http://aws.amazon.com/ec2/faqs/#Billing) of the EC2 FAQ page. 

- Briefly, Amazon describes billing as follows:

> You pay only for what you use and there is no minimum fee. Pricing is per instance-hour consumed for each instance type. Partial instance-hours consumed are billed as full hours. There is no Data Transfer charge between two Amazon Web Services within the same region (i.e. between Amazon EC2 US West and another AWS service in the US West). Data transferred between AWS services in different regions will be charged as Internet Data Transfer on both sides of the transfer. Usage for other Amazon Web Services is billed separately from Amazon EC2. Billing commences when Amazon EC2 initiates the boot sequence of an AMI instance. Billing ends when the instance terminates, which could occur through a web services command, by running “shutdown -h”, or through instance failure. Instance-hours are billed for any time your instances are in a “running” state. If you no longer wish to be charged for your instance, you must "stop" or "terminate" the instance to avoid being billed for additional instance-hours. Billing starts when an instance transitions into the running state.

- This sounds simple but it tends to be more complicated than this. 
- EBS usage is billed separately from EC2 resources, even though the two are often intricately linked. 
  - For example, the root volume on a Linux Instance often exists as an EBS volume. 
  - You will be charged for whether the system is running or stopped. 
  - Similarly, if you have an EC2 instance with an extra EBS volume(s) attached to it, you will be charged for this storage even when the EC2 instance is stopped. 
  - When you terminate the instance, associated EBS volumes may or may not be automatically destroyed. 
  - This behavior depends on how you configured the instance. 
    - We will discuss this configuration in further detail below. 
  - Similarly, if you create a `Snapshot` of your instance, this gets saved to EBS storage and you will be charged for these as long as they exist. 
  - When you create an AMI to save the state of your instance for later, this is stored as a `Snapshot`.  
  - The good news is that small EBS volumes are very cheap and by default, the root volume for most instances is small (usually 8GB).

- If you choose an instance type with pre-configured storage or you attach EBS volumes for storage but set them to be deleted upon termination of the instance, and you never create any `Snapshots` or save the instance as an `AMI`, when you terminate that instance, all costs associated with it will be gone. 
- The cost will,therefore, be the hourly rate from the [pricing list](https://ec2instances.info/) multiplied by the number of hours it was running rounded up to the closest whole hour.

- In the `Billing and Cost Management` section of the EC2 console, you can create billing alerts that will warn you of ongoing costs. 
- If you find that you are being charged a monthly fee but you are not intentionally using any resources, you should follow these steps. 
- Log in to the AWS EC2 console. 
  - Now, *for each AWS Region*, determine the following; Are there any?:
    - `Running Instances`? 
    - `Volumes`? `
    - `Elastic IPs`?
    - `Snapshots`?  
    - If any of these values are greater than 0, in *any one or more regions*, you are likely being billed monthly for resources that Amazon is reserving for you until told otherwise. 
    - If you terminate or delete all of these items, your monthly bill should return to $0.

### Necessary steps for launching an Instance
- In the following sections, we are going to launch an example instance, configure it in the AWS EC2 console, discuss some of the important concepts of this configuration and log into the instance once it is running. 
- In each case, screenshots from an example instance will be shown and discussed. 
- To get started, make sure you are logged into AWS and go to the `EC2 dashboard`. 
- To start using EC2 we will launch a virtual server running the latest stable version of the Ubuntu operating system. 
- We will decide on the basic hardware for this server, configure storage that will be available on it, configure its security, and so on. 
- Once it is running we will log in to this server and perform some additional exercises and configuration. 
- To get started press the blue `Launch Instance` button. 
- Remember that you are launching this instance in a particular `Region`. 
- In the following example, we launched an instance in `EU West (Ireland)`. (Pick the closest to your location)

***
**Launching an instance:**
- **Please make sure to select `EU West (Ireland)`.**
![AWS-EC2-LaunchInstance](Images/AWS/az-eu-west.png)
***

### Step 1. Choosing an AMI 
- An [AMI](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) or `Amazon Machine Instance` is a template for launching an instance.  
- The AMI includes a template for a pre-configured root volume that contains an operating system (e.g. Ubuntu Linux, Windows, etc.)
- The AMI also includes basic configuration of storage volumes that will be available within an instance
- The first step to launching an instance is to select an AMI. 
- Refer to the screenshot below. 
- There are four main options when selecting an AMI: 
- `Quick Start`
- `My AMIs`
- `AWS Marketplace`
- `Community AMIs`
- We will select `Amazon Linux 2 AMI (HVM), SSD Volume Type ` AMI as our starting point
- The `Quick Start` AMIs section is a relatively short list of basic systems that have been chosen by Amazon as common starting points
- These have some degree of "official" support and testing on AWS
- The `My AMIs` section contains AMIs that you have created yourself, perhaps using a `Quick Start` or `Community AMI` as a starting point
- For example, you might start with an Ubuntu AMI and install all of the bioinformatics software and other infrastructure you need to run an analysis pipeline
- You could then store this configured machine as an AMI to save your work
- Having an AMI allows you to share a complete system configuration, and to fire up a cluster of identical instances that are ready to go
- The `AWS Marketplace` contains AMIs where a company (often a software company) has configured a machine for certain applications
- You can browse through this section to get an idea of what kinds of applications are available
- Finally, the `Community AMI` section contains thousands of AMIs created by users around the world
- These AMIs are specific to each `Region` so if someone tells you about an AMI they want to share, be sure to search for it in the correct region
- If you create your own AMI and you want to share it with others, you can 'publish' it to the community
- It will still appear in your `My AMIs` section, but it will also then appear and be searchable in the `Community AMI` section.

- For this tutorial we will select the AMI from the `My AMIs` list: 
- The full-length description for this AMI is `Ubuntu - CEU - SSH on 8787`
- We are also told that the `Root device type` is `EBS` and the `Virtualization type` is `HVM`
- We will discuss storage in more detail but this means that the AMI is configured so that the `root volume` of the operating system will be installed on an EBS volume
- In practical terms, this means that information stored on the root volume, including the OS itself, will persist if we stop the instance (i.e. the root volume is *not* ephemeral)
- The term `HVM` refers to a type of virtualization technology that will be used by the instance, the other common type being `PV`.
- A detailed discussion of virtualization technology is outside of the scope of this class but you can learn more details here: [Linux AMI virtualization types](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/virtualization_types.html)
- Once you are ready to proceed, press the blue `Select` button

***
**Step 1. Choose an Amazon Machine Image (AMI):**
![AWS-EC2-ChooseAnAMI](Images/AWS/AMI-aws.png)
***

### Step 2. Choosing an Instance Type
- Once an AMI is selected, the next step is to choose an instance type
- In simple terms, in the previous step, we decided on the operating system we want to run, and now we need to choose the hardware that it will run on
- Refer to the following screenshot for this discussion
  - Note that in this example, we have selected `General purpose` in the drop-down filter
  - Pick `t2.nano` Instance Type
  - Note that the price per hour for each of these options is not listed here
    - To get the price, note the instance type name (e.g. t2.nano`) and refer back to the [EC2 pricing list](https://ec2instances.info/)
- We discussed many of the details described in this table of instance types in the pricing discussion above
- Briefly, we are given a series of options that differ in their number of CPUs, memory, pre-configured storage, network performance, etc.
- To view more or fewer details you can adjust this table using the `Show/Hide Columns option`
- In the example depicted below, we have selected the `t2.nano` option 
- Once you are ready, proceed to the next step by pressing the `Next: Configure Instance Details` button

***
**Step 2. Choose an Instance Type:**
![AWS-EC2-ChooseAnInstanceType](Images/AWS/ec2nano.png)
***

### Step 3. Configuring Instance Details
- Once an instance type is selected the next step is to configure the instance details
- This step in the launch-an-instance procedure introduces many advanced concepts that will be covered only briefly here
- To learn more about each of the options available in this step you can mouse over the `i` symbol beside each
- For the most part, leaving all of these options at their default value will be fine
- Refer to the following screenshot while we discuss a few of these options briefly
- Using the `Number of instances` option you could launch multiple instances of the same AMI with the same hardware configurations at the same time
- However, in our example, only `one` instance will be launched
- You also have the option to attempt to negotiate a cheaper rental by using the [Request Spot Instances](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html) option
- The `Shutdown behavior` option determines what will happen if you shut down the instance from within the AMI (e.g. by issuing a `sudo shutdown` command in Linux)
- To prevent accidental termination of your instance, you may want to set this option to `Stop`
- You can also help prevent accidental termination of your instance by using the `Enable termination protection` option
- These options can also be adjusted later for any instance in the console
- Once you are ready, proceed to the next step by pressing the `Next: Add Storage` button

***
**Step 3. Configure Instance Details:**
![AWS-EC2-ConfigureInstanceDetails](Images/AWS/AWS-EC2-ConfigureInstanceDetails.png)
***

### Step 4. Adding Storage
- The next step is to configure the disk/storage that will be available in the instance
- The starting point of this page depends on what instance type we selected in Step 2
  - Remember that we selected an instance type with an EBS root volume (during AMI selection) 
  - These two volumes are summarized in the `Add Storage` view
  - The first volume is 8 GiB.  This is the root volume where the operating system will exist
  - It is set to be deleted on termination of the instance but we could choose to keep it as well
  
 **Do not do this**, however, you could add more volumes here
- We could add a second/third.. volume to our instance
- Choose `EBS` as the `Type`, set the device to `/dev/sdc`, give it a size of 500 GiB, and set the volume type to `General Purpose (SSD)`
- Now when we log into the instance we will expect to find two/three distinct storage volumes/devises. 

***
**Step 4a. Add Storage:**
![AWS-EC2-AddStorage1](Images/AWS/S3StorageRevised.png)
***

**This is how you would add Additional Storage :**
![AWS-EC2-AddStorage2](Images/AWS/AWS-EC2-AddStorage2.png)
***

### Storage volume options 

#### What is ephemeral or `Instance Store` storage? What is `EBS` storage? Which is the better option for `Root device type`?
- An `EBS` ([elastic block storage](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html)) volume can be linked to single instance
- `EBS` volumes can be set to persist even if the instance is destroyed
- They could therefore later be reassigned to a different instance
- In the context of bioinformatics analysis, you might decide to write your analysis results to an EBS volume
- Once the analysis was complete you could then shut down the instance to save money but keep your results indefinitely on the EBS volume
- The [Instance Store](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html) volumes are considered 'ephemeral' or transient
  - Therefore, you must be careful when storing data to these volumes because if the machine is stopped or terminated, the data will be unrecoverable
- Instance store volumes are created from disks that are physically attached to the host computer while EBS volumes are created from disk arrays in the same `Availability Zone` but are not physically attached to the host computer
- Instead, the host computer accesses EBS volumes over a network
- EBS volumes can be added at will to an existing instance
  - On the other hand, Instance Store volumes can only be added or configured when the instance is created

- The `Root device type` refers to the type of volume used to store the operating system itself
- This is usually a small volume (often 8 GiB) that can be either `EBS` or `Instance Store` type
- This type option can be selected during the choice of AMI or when configuring storage during the setup of the AMI
- Once you launch the AMI though you can not change the `Root device type`
- There are [pros and cons](http://stackoverflow.com/questions/3630506/benefits-of-ebs-vs-instance-store-and-vice-versa) to both `EBS` and `Instance Store` for the root device type
- The `Instance Store` type may have a performance advantage but the `EBS` type is more flexible and safer from the perspective of accidental data loss
- For a beginner just starting to use AWS, we recommend `EBS`
- A bioinformatics analysis instance might use an `EBS` volume for `Root device type`, use an `Instance Store` volume for `/tmp` where all temporary files and staging of data will occur and use an additional `EBS` volume to store the final results
- Notice that this is how we have configured the example instance in this tutorial
- You can examine the types of volumes for an existing Instance in the EC2 dashboard by selecting a running Instance and examining the `Root device type` value
- Once you are ready, proceed to the next step by pressing the `Next: Tag Instance` button

### Step 5. Tagging the Instance
- As you start to have a large number of instances running or saved you may want to start assigning `Tags` to these instances to help track their usage and billing details
- Try creating a `Tag` as a simple key/value pair
- Once you are ready, proceed to the next step by pressing the `Next: Configure Security Group` button

***
**Step 5. Tag Instance:**
![AWS-EC2-TagInstance](Images/AWS/ec2-tags.png)
***

### Step 6. Configuring a Security Group
**(Don't do this here, create a Security Group separately and attach that to this EC2 Instance as explained above.)**
- A `Security Group` controls how services and users can access your instance once it is running
- When you launch a new instance you can choose to configure a new Security Group and use it or select one that you created previously
- You can also select a `default` security group
- The purpose of Security Group settings is to determine what Inbound and Outbound network traffic will be allowed on the instance
- Since Inbound traffic could be coming from anyone (including those with malicious intentions) it is highly recommended that most incoming traffic be blocked and only certain incoming services be allowed on an as-needed basis
- In the example below we created a Security Group called `CEU-Tutorial` that only allows incoming traffic of two types:
  - `SSH` (over port 22) 
  - `HTTP` (over port 80)
- The first rule will allow us to log in to our instance remotely using the SSH protocol
- The second rule will allow us to set up a web server on the instance and access web content remotely using a web browser
- Both of these rules could be made significantly more secure by limiting access to only certain IP addresses
  - For example, if you will access your AWS instances only from your university you could limit access to your universities IP address (or a range of addresses)
- You can reconfigure the `Security Group` settings at any time, but they will not take effect until the instance has been rebooted
- Create two Incoming rules that match those in the screenshot and name your new security group
- Once you are ready, proceed to the next step by pressing the `Review and Launch` button

***
**Step 6. Configure Security Group:**
![AWS-EC2-ConfigureSecurityGroup](Images/AWS/Security-Group-AWS.png)
***

### Step 7. Reviewing the Instance before Launch
- At this stage, you will be presented with a final summary describing the configuration of your instance
- Some warnings may appear
- A conservative security warning is often presented here if you have allowed any broad Incoming access to the instance
- Once you are ready, proceed to the next step by pressing the `Launch` button

***
**Step 7. Review Instance Launch:**
![AWS-EC2-ReviewInstanceLaunch](Images/AWS/Review-AWS.png)
***

### Step 8. Assigning a Key Pair
- You will now be presented with a final, but very important configuration step, assignment of a `Key Pair`
- A Key Pair consists of two keys, a `public key` and a `private key`
- The `public key` will be stored in AWS. The `private key` will be presented to you on the creation and it *must be saved by you* to allow you to log into your instance later
- If this is your first instance you will have to `Create a new key pair`
- In the example below, we have chosen to create a new key pair called `AWS-Tutorial`
- Once the name is chosen, press the `Download Key Pair` button
- You will download a simple text file called `CEU-Tutorial.pem`
- Store this file somewhere on your computer (e.g. your home directory) and remember the location
- The contents of this file will contain an RSA key that should look something like this:

```
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAhEpF18lIUouMH8qia/BSB70vrQVq/mTTkiRbsACB78rzy3XGRMfvwUseIsGY
H6SDOAFrRlmTrAArH5A0t2TZ8PKrq7b9FtEAvMCeE7rWEiqBblAWiER0k1pbnIqyKJJCo1YRSUs0
oNMdvjB4CUylYraSsSNFYJG5gRwcNhBENLDVnDS79geQcPLu/JeEiJ9V+w+CCYAG40f7li/TuULr
rSy6Oq6jgn2Gy7rrHU7XHU5hcEvxuSeoLb8h/bH1N+cN/H7x3ipEjIDdA2ScCkRXum1V6/kTFQFq
vDG0lqoTlmTNKgDGpb+rdzJgOg/3QX4RSrX/c0W6aFkV9Ib/jQxT+wIDAQABAoIBADAvWXc6wpQG
bjiaN0T3mPlmqHnuEkWs9f8yLQ9TcACmvNwr/tbIuISAVu6z8zP7WSxKIAfU0twAh7SMcxclrdh8
m5kFIvRvlkQqKKnpENY3E0PZ+gsSXB/b9qhzQGdUtt8Fl3BJ61Z07016HA7PEyJ8e7v3q+p7ycTE
N2Zd0GocRIX8zxdRo9GS8ouS0QcFgNF8KblzlJ6Vs0gI7o7mIRZIm9vWkuR9Lp9uEPD2flUIvN3z
yRmY/FE/R1yc76Uq+g8eywifRAh+GFyyO8PmFoYRni4Ki6+tEIFaq5JauT0JJF66EZeZP8ZKoWm9
1K30Ucti2D5l8t+CpbBM5JxhmjECgYEAxz1ET42F1sBGYqNn5hmfjrRp+YF3EYz2awRSibOeerpJ
Bh1QZeB7/QD3wcB00XFiMu/3haP9xs4eesjSSug+1F59nyzDplNsybz1sYpUQwP9LjX0loUCIb8r
3O2VdLJ5ZJ9dfNgpStC/wi7kkr8xjK5XiHgP6DLk6+H1Lr2d+kMCgYEAqfpUseZ/sm1vYt80LlWI
r8ozsUmzuISRspGVUppyDD47Iyj/1mkiWnsFDDl07oBcFIUFIEd1rkJNB3gXKSr76kcY0X4lav7a
0dvse2T9PC/pLSFkax9UjVnydCN8ElyNoXI2wT5HuLDjjCmHBD/4E9ZOO201JICSbRxaykl17+kC
gYEAxRiWuxwFiqwq9Okxny856LIRJAIvB+2q17Mu84n8/OvL0YCuSBoKjf6nGcSJy6eevUUmV84i
/sho3o5Lek7F2NCg9RYTdjaRKAEGDNwK/0Cy9UPq8fwiX7/+ZE+jyg3EiQYeNaKhNqHLEQ3SkFkT
a1gMv7QGCG5QiAi/w71QyoECgYARcn+VDyrWXsNLK8wIYYE5QhESRpVrADiQUr84DmBcf1rEniW8
lWgQT4ZSHeexv300If9Hs+4RZ/7OIHaIJEBdaNTUVBV1KRm+5sscU15m+if+GOpc0Id2RuBLKYVH
wTZMdxPFvCXSgF2q+mxAdGx7ZMj88pW83HGrP3jWQLoZWQKBgQCX5jxy3QXlPpwDppqwKKBQ8cGn
YDDQHCeD5LhrVCUqo5DCobswzmGKU/xEqYsqlk/Mz1Zkvg4FbJwJDgQGkSyAu071NLi0O6w27dm+
UHuvF5mCDdAHWirFUBSiebxOpEQnkZ9IPXUUCSC6IQvPFbdGN8G3WjoER6Lw121Q4rJxGA==
-----END RSA PRIVATE KEY-----
```

- If this is not your first instance and you have already created a key pair, and *you still have that key file*, you can choose to use the existing key pair. 

***
**Step 8. Select an existing Key Pair or create a new Key Pair:**
![AWS-EC2-CreateKeyPair](Images/AWS/keypair-aws.png)
***

- To prepare for logging into our instance, let's create a directory on our own `local` computer (i.e. the one you are sitting at) and store the key file there
- Later we will use this file to log onto the AWS instance
- We are using a mac system
- To create a directory and move the key file we downloaded into that directory we can down the following in a Mac Terminal session:

```bash
mkdir ~/CEU-Tutorial
mv ~/Downloads/CEU-Tutorial.pem ~/CEU-Tutorial
cd ~/CEU-Tutorial
chmod 400 CEU-Tutorial.pem 
ls
```

- The `chmod 600 CEU-Tutorial.pem` command changes the permissions of your key file so that only you can read it
- This is an important security setting
- If you attempt to log into your instance using a key file with inappropriate permissions, the login command may fail
- So you should always perform this command on any new key file (or copy of such a file) before attempting to use it to log into an instance

### Step 9. Reviewing launch status
- Once you have launched your instance, you will be presented with yet another review page
- When you are ready, proceed to the next step by hitting the `View Instances` button

***
**Step 9. Review launch status:**
![AWS-EC2-LaunchStatus](Images/AWS/AWS-EC2-LaunchStatus.png)
***

### Step 10. Examining a new Instance in the EC2 Console
- You should now see the EC2 Console view for a new instance
- This view shows a table of all Instances you have created in the current `Region`
- When an instance is terminated it will remain visible in this table for a brief time and then will be automatically removed
- You should see a single entry that when selected looks much like the example below
- After a few minutes, your instance should achieve an `Instance State` of `running`
- Note the incredible wealth of information available both in the table and in the `Description` view below
- Much of the configuration we described above will be summarized here
- To work effectively with your instances you will need to become familiar with certain features of this EC2 console view
- For example, the `Name`, `Instance Type`, `AMI ID`, `Root device type`, `Root device`, and `Block devices` will help to remind you what kind of instance you configured
- In order to remotely log into the instance, the following items in the console will be relevant: `Instance State`, `Key Pair Name`, `Security Groups`, and `Public IP` (or `Public DNS`)
- Try to familiarize yourself with each of these features and how to find them in the console for each instance you have running

- To modify an instance in the EC2 console you can select that instance (or a series instances) using the blue checkboxes at the left
- You can then perform various tasks using the `Actions` menu
- You can also right-click on a single instance to obtain a similar menu
- Before logging into this instance lets take a momemt to examine various important sections of the EC2 console in particular the `EC2 Dashboard`, `Volumes`, `Security Groups`, and `Key Pairs`

***
**Step 10. EXAMPLE! Console view of a new Instance (Please don't replicate this instance here)**
![AWS-EC2-Console](Images/AWS/AWS-EC2-Console.png)
***

#### Check
- The EC2 dashboard should now show a running Instance, Volumes, etc.
- Review new Volumes
- Review new Security Groups
- Review new Key Pairs

* * *

### Step 11. Connecting to your instance using SSH

>So you've started your instance but how do you get to it? If you're not familiar with ssh, it's the command that allows you to log into a computer remotely over the network. In the simplest possible terms, it allows you to use a computer that's not physically right in front of you. 

- We are finally ready to log into our instance
- To do this, open a terminal session on your local computer (e.g. using `Mac Terminal` or `Windows Putty`)
- Change directories to the location where you stored your key file `CEU-Tutorial.pem`
- Now do a `chmod 600 yourpemfilename.pem`, otherwise, you won't be able to SSH due to bad permissions
- Now at the same time, view your instance in the EC2 console
- Make sure that the `Key pair name` for this instance matches the `.pem` key file
- Also, get the `Public IP` value from the console and use it instead of the example one below. Note that you could use the `Public DNS` value instead if you want

- Finally, log in as follows (https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html)
```bash
cd ~/CEU-Tutorial
chmod 400 CEU-Tutorial.pem
ssh -i AmazonKey.pem ec2-user@XXXXX

# Example:
ssh -i /Desktop/nginxtest.pem ec2-user@ec2-3-248-227-104.eu-west-1.compute.amazonaws.com
```

If successful, you will see something like this: 
```bash

       __|  __|_  )
       _|  (     /   Amazon Linux AMI
      ___|\___|___|

https://aws.amazon.com/amazon-linux-ami/...
```

```In this example, we open a terminal command line session on our local computer. We moved to the location of my `.pem` key file. We then made sure the permissions of this file were set correctly using a `chmod` command. You only need to do this step once but there is no harm in doing it again. Then we executed an SSH command to remotely log into our AWS instance using the `Public IP`. Our SSH command included an option to use the `.pem` file to identify us as the owner of the instance. We logged into the instance as a user called `name` as an example now that is a user that we know will be defined by default on all systems.```

**Pitfall:** One thing to watch out for is the following: the ssh address is based on your IP address and if you start and stop your instance the IP can change, changing the address you ssh into along with it (again, the value in the field Public DNS). If you've re-started your instance and are having trouble sshing, check that your address is correct.

### Step 12. Install NGINX
- Now that we are in, let's set up NGINX 
- Run `sudo apt update` to apply all updates to your os.
- To install NGINX run: `sudo apt install nginx`
- Now you will have an html folder so `cd /var/www/html` and list contents: `ls`
- You will see one `.html` file
- Use your preferred text editor e.g Nano, Vim, Emacs and make some changes to the html file (e.g `nano`)
- Now you will see the changes if you visit your website

![NGINX](Images/AWS/nginx.png)

* * *

### What is difference between the 'Start', 'Stop', 'Reboot', and 'Terminate' (Instance States)?
- From the AWS EC2 console, you can change the state of each of your instances
- The `Start` command will boot a system that has been powered down
- The `Stop` command will power down the instance and is similar to performing `sudo shutdown` from within the instance (if you have configured your instance that way during creation)
  - Do not forget that if you stop an instance with ephemeral `Instance Store` volumes, the contents of these volumes will be lost
- The `Reboot` command will simply reboot the machine
  - This is equivalent to using a `sudo reboot` command from within the instance
- The `Terminate` command will destroy the instance and any ephemeral `Instance Store` volumes associated with it
- If the root device is an EBS volume it may or may not be destroyed depending on how you configured the instance during the creation
- If there were additional EBS volumes associated with the instance and you `Terminate` the instance, these may also be destroyed if you selected that option when they were being created
- Before terminating an instance you should think carefully about whether there is data you want to save and if so, how the volumes will behave on termination
- Similarly, if you want to destroy all components of an instance, including all associated volumes, you may need to terminate the instance and then separately destroy certain volumes 

### Tidying up and shutting down AWS resources
- Once you are done with this tutorial you should terminate or delete all resources that were created to ensure you are not charged
- Specifically, you should remove: `Instances`, `Volumes` and `Snapshots`
- You may also decide to remove other entities that were created for demonstration purposes including: `Tags`, `AMIs`, `Security Groups` and `Key Pairs`
- All of this can be done in the AWS EC2 console
- When you are all done, the `EC2 Dashboard` should show `0` for all resource types except `Security Groups` where a single default security configuration will remain

### Further reading (Optional)
- This is a basic introduction to AWS cloud computing that assumes all configuration of the instance will occur within the AWS EC2 console of your web browser and all configuration of the Ubuntu Linux system will occur by the user manually executing commands and perhaps saving the outcome as a custom AMI
- For large scale computing and complex deployments of compute infrastructure on the cloud, these methods will not be sustainable
- Here is a list of more advanced topics for discussion on how to move beyond the console and automate the configuration of your system:
- Use of the [AWS command-line interface (CLI)](http://aws.amazon.com/cli/)
- Use of the [AWS EC2 API](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/Welcome.html)a
- Use of [AWS SDKs](http://aws.amazon.com/tools/#SDKs)
- Use of [S3](http://aws.amazon.com/s3/) and [glacier](http://aws.amazon.com/glacier/)
- Use of [vagrant](https://www.vagrantup.com/) to launch AWS instances
- Use of [puppet](https://puppetlabs.com/puppet/what-is-puppet) to configure Linux systems




* * * 
### Practice Questions

#### What are the advantages of cloud computing?
** Answer
6 advantages: 
- Trade capital expense for variable expense
- Stop guessing about capacity
- Increase speed and agility
- Stop spending money running and maintaining data centers
- Go global in minutes

#### What are the types of cloud computing?

** Answer
- Infrastructure as a Service (IaaS)
- Platform as a Service (PaaS)
- Software as a Service (Software as a Service)

More here: https://aws.amazon.com/types-of-cloud-computing/

#### What is S3 and what does it mean?

** Answer
S3 stands for Simple Storage Service.
S3 is on object storage with a simple web interface to store and 
retrieve any amount of data from anywhere on the web. 

#### What are some usages of S3?

** Answer
You can use Amazon S3: 
- as primary storage for cloud-native applications
- as a bulk repository, or "data lake," for analytics
- as a target for backup and recovery and disaster recovery
- with serverless computing. 

#### What are the features of S3?

** Answer
**9 features:**

- Simple: easy-to-use web-based management console + REST API
- Durable: your data is redundantly stored across multiple facilities and multiple devices in each facility
- Scalable: you can store as much data as you want and access it 
when needed.
- Secure: Amazon S3 supports data transfer over SSL and automatic encryption of your data once it is uploaded. You can also configure bucket policies to manage object permissions and control access to your data using IAM
- Available: designed for up to 99.99% availability of objects over a given year and is backed by the Amazon S3 Service Level Agreement ensuring that you can rely on it when needed. 
- Low cost: Using lifecycle policies, you can set policies to automatically migrate your data to Standard - Infrequent Access and Amazon Glacier as it ages to further reduce costs
- Simple data transfer: Amazon provides multiple options for
cloud data migration and makes it simple and cost-effective for you to move large volumes of data into or out of Amazon S3. You can choose from network-optimized, physical disk-based, or third-party connector methods for import to or export from Amazon S3
- Integrated: Amazon S3 is deeply integrated with other AWS services to make it easier to build solutions that use a range of AWS services
- Easy to manage: Amazon S3 Storage Management features allow you to take a data-driven approach to storage optimization, data security, and management efficiency. These enterprise-class capabilities give you data about your data, so you can manage your storage based on that personalized metadata.


#### What is AWS EC2?

** Answer
EC2 stands for Amazon Elastic Compute Cloud. 
It is a web service that provides secure, resizable =compute capacity= in the cloud. 
It is designed to make web-scale computing easier for developers.

#### What is a region?

** Answer
A Region is a physical location in the world where we have multiple Availability Zones (AZs).


#### What is an Availability Zone?

** Answer
AZs consist of one or more discrete data centers, each with redundant power, networking,and connectivity, housed in separate facilities.

#### What is an Edge Location?

** Answer
Edge Locations are endpoints for AWS which are used for caching content. There are many more Edge Locations than Regions. Currently, there are over 96 EL.* Question :drill:

#### What is the difference between a region, an Availability Zone and an Edge Location?

** Answer
- A region is a physical location in the World which consists of two or more Availability Zones.
- An AZ is one or more discrete data centers, each with redundant power, networking and connectivity, 
housed in separate facilities
- Edge locations are endpoints for AWS which are used for caching content.


#### What is the root account?

** Answer
This is the email address used to sign up in AWS.
Unlimited access to do things in the cloud.


#### Which permissions have new users when created?

** Answer
New users have NO permissions when first created

#### What is the difference between access keys and user/pass?

** Answer
You cannot use the Access Key ID and Secret Key to login in the console. You can use this to access AWS via the APIs and CLI however.

#### Size of the files on S3?

** Answer
From 0 Bytes to 5 TB

#### What is the data consistency model for S3?

** Answer
- Read after Write consistency for PUTS of new Objects
- Eventual Consistency for overwrite PUTS and DELETES (can take some time to propagate)

#### What are the different Tiers/Classes of storage for S3?

** Answer
- S3 standard: 99.99% availability, 99.999999999% durability, stored redundantly across multiple devices in multiple facilities, and is designed to sustain the loss of 2 facilities concurrently. No retrieval fees

- S3 - IA (Infrequently Accessed): For data that is accessed less frequently, but requires rapid access when needed. Lower fee than S3, but you are charged a retrieval fee.

- S3 One Zone - IA: want a lower cost option for infrequently accessed data, but do not require the multiple AZ data resilience.

- Glacier: Very cheap, but used for archival only. Expedited (higher fees less retrieval time -- within minutes),
 Standard (3-5 hours) or Bulk (5-12 hours).


#### S3 Charges?

** Answer
Charged for 
- Storage
- Requests
- Storage Management Pricing (the tags you use on your data, added on the metadata of your files)
- Data Transfer Pricing (when you transfer data from one region to another)
- Transfer Acceleration

#### More questions to review:
 - How do Security Groups and EC2 Instances Relate?
 - When to use Glacier, S3, EBS?
 - You need a computer for 8 hours. You need 16GB of RAM and 2 vCPUs. Which type of an EC2 instance would you choose? What would be the price?  

# Recap video

[Here is a youtube](https://youtu.be/6FfLocjBcNE) video that will help you to complete your homework. It has detailed info about how to SSH into an EC instance both from Windows, Mac and Linux.

* * *

#### Sourcers/Credits:
https://d1.awsstatic.com/whitepapers/architecture/AWS_Well-Architected_Framework.pdf?did=wp_card&trk=wp_card
https://d1.awsstatic.com/whitepapers/aws-overview.pdf?did=wp_card&trk=wp_card
https://d1.awsstatic.com/whitepapers/aws_cloud_adoption_framework.pdf?did=wp_card&trk=wp_card
https://cloudacademy.com/learning-paths/aws-fundamentals-1/
https://acloud.guru/
https://d1.awsstatic.com/whitepapers/aws_pricing_overview.pdf?did=wp_card&trk=wp_card
https://d1.awsstatic.com/whitepapers/AWS_DevOps.pdf?did=wp_card&trk=wp_card
https://d1.awsstatic.com/whitepapers/Security/AWS_Security_Best_Practices.pdf?did=wp_card&trk=wp_card
https://d1.awsstatic.com/whitepapers/AWS%20Storage%20Services%20Whitepaper-v9.pdf?did=wp_card&trk=wp_card
https://aws.amazon.com/getting-started/use-cases/?awsf.getting-started-use-case=use-case%23big-data-analytics&e=gs&p=gsrc_control&sc_ichannel=so&sc_icategory=abtest&sc_iname=awswt-7&sc_iurl=gsrc&sc_iversion=a-use-case-bd-analytics
https://ec2instances.info/
https://medium.com/@ashanpriyadarshana/aws-services-overview-8432cb578227
https://www.businessnewsdaily.com/10772-aws-training-resources.html
https://aws.amazon.com/solutions/case-studies/vodafone/
https://aws.amazon.com/solutions/case-studies/siemens/
https://aws.amazon.com/solutions/case-studies/atlassian/
https://www.smallbusinesscomputing.com/biztools/the-pros-and-cons-of-cloud-computing.html
https://www.lifewire.com/cloud-computing-explained-2373125
https://www.linkedin.com/pulse/11-pros-cons-cloud-computing-everyone-should-know-umesh-singh/
