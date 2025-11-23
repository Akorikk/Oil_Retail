# Oil_Retail

setup.py ==> I have use -e . in the end of requirements.txt to setup my local package you can see oil_retail is my local package because inside oil_retail we are having so many components now lets say i want to import something from oil_retail so we import like this from oil_retail.configuration import data_ingestion we can only import if it is set as a local package -e . it will look particular file called setup.py inside setup.py we have to give little details it is important to do if you wanna imort anything from oil_retail we can check using pip list if oil_retail is insatll as a local package or not 

Logging ==> Logging helps your project record what is happening while the code runs.It tells you the steps, warnings, and errors so you can debug easily.It creates a history of events (in a log file) so your ML pipeline becomes reliable and production-ready.

Utils ==> if you usinf the same function again and agian in your implementation lets say you want yo read yaml file so i need to read this yaml file in each and and every component like data ingetsion data validation model trainer etc so every time you need to write the same function again and again for reading this file insted of doing this we can create a one fucntion for yaml file and  we can keep inside the utils and whenever we need it we import it from utils iw will helps you to implement the project without repeting that function if you notice i have used ConfigBox and ensure_annotation in each and every function in utils what is the use of this ConfigBox lets you access dictionary keys like attributes, making your config files easier and cleaner to use. for example this is the code we have written from box import ConfigBox

config = ConfigBox({
    "project_name": "my_app",
    "version": 1.0
})

print(config.project_name)   # instead of config["project_name"]
print(config.version)  now we want to see version we write like this config["version"] so instead of writing this we can write like this config.version
if we are using configbox and next is ensure_annotations => It enforces that function arguments and return values follow Python type annotations at runtime. It checks if the types you annotated are actually correct when the function runs. Python does not check types for example def add(a: int, b: int) -> int:
    return a + b

add("10", 20) we can see that 10 is in string form 
it will give you unexpected result with no error Even though a should be an int, Python allows "10". With ensure_annotations Catches bugs early Stops wrong data types entering your functions and its will throw error the correxct way its makes large projects safer & more stable that why i have use ensure_annotations on top of all function written in utiles.common.py

## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in oil_retail config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py

