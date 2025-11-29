from diagrams.onprem.database import MongoDB, PostgreSQL
from diagrams.onprem.network import Nginx
from diagrams.onprem.compute import Server
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.monitoring import Grafana, Prometheus, Datadog
from diagrams.aws.compute import ECS, EKS, Lambda, EC2
from diagrams.aws.storage import S3, Snowball
from diagrams.aws.database import ElastiCache, RDS, DDB 
from diagrams.aws.network import ELB, Route53, VPC, APIGateway
from diagrams.gcp.analytics import BigQuery, Dataflow, PubSub
from diagrams.gcp.compute import AppEngine, Functions
from diagrams.onprem.ci import Jenkins, GitlabCI, GithubActions 
from diagrams.onprem.container import Docker 
from diagrams.onprem.logging import Loki 
from diagrams.onprem.queue import Kafka, RabbitMQ  
from diagrams.onprem.tracing import Jaeger, Tempo
from diagrams.onprem.vcs import Git, Github, Gitlab
from diagrams.aws.general import Marketplace, MobileClient, User, Users, Client
from diagrams.aws.integration import Eventbridge, SNS, SQS , SF
from diagrams.aws.management import Cloudwatch, SSM, ParameterStore
from diagrams.aws.security import Cognito, IAM
from diagrams.generic.compute import Rack
from diagrams.programming.language import Nodejs, Java, Go, Csharp, Kotlin, Python

NODE_TYPES = {
     # Generics
    "User": User,
    "TechUser": Client, 
    "Client": Client,
    "Frontend": User,
    "Web": Server,
    "API": Nginx,
    "Application": Nginx,
    "Marketplace": Marketplace,
    "MobileClient": MobileClient,
    "Rack": Rack,

    # Languages
    "NodeJs": Nodejs,
    "Java": Java,
    "Go": Go,
    "Csharp": Csharp,
    "Kotlin": Kotlin,
    "Python": Python,

    # Custom icons  
    "SwaggerUI": "custom_swagger",

    # Databases
    "MongoDB": MongoDB,
    "Database": MongoDB,
    "PostgreSQL": PostgreSQL,
    "Dynamodb": DDB,
    "RDS": RDS,
    "ElastiCache": ElastiCache,
    "MongoExpress": Server,

    # Cache / Queue
    "Redis": Redis,
    "SQS": SQS,
    "Kafka": Kafka,
    "RabbitMQ": RabbitMQ,

    # AWS General / Compute / Storage
    "ECS": ECS,
    "EKS": EKS,
    "Lambda": Lambda,
    "EC2": EC2,
    "S3": S3,
    "Snowball": Snowball,

    # AWS Network
    "APIGateway": APIGateway,
    "ELB": ELB,
    "Route53": Route53,
    "VPC": VPC,
    "Nginx": Nginx,

    # AWS Integration
    "Eventbridge": Eventbridge,
    "SNS": SNS,
    "SF": SF,                # StepFunctions

    # AWS Security
    "Cognito": Cognito,
    "IAM": IAM,

    # Monitoring
    "Grafana": Grafana,
    "Prometheus": Prometheus,
    "Datadog": Datadog,
    "Loki": Loki,
    "Jaeger": Jaeger,
    "Tempo": Tempo,
    "Cloudwatch": Cloudwatch,

    # CI/CD
    "Jenkins": Jenkins,
    "GitlabCI": GitlabCI,
    "GithubActions": GithubActions,

    # VCS
    "Git": Git,
    "Github": Github,
    "Gitlab": Gitlab,

    # GCP
    "BigQuery": BigQuery,
    "Dataflow": Dataflow,
    "PubSub": PubSub,
    "AppEngine": AppEngine,
    "Functions": Functions,

    # Containers
    "Docker": Docker,

    # Managment
    "SystemsManager": SSM,
    "ParameterStore": ParameterStore,

    # Safe Fallback
    "Default": User
}