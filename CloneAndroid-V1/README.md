# Clone Android

![alt text](http://52.7.242.59/Felaban/apipruebas/web/users/a.png)

Hello friend, This is an application to clone phones.

## Installation

This version supports python 3.6 onwards

```bash
$ virtualenv -p python3 env
```
Active virtualenviroment

```bash
$ source env/bin/activate
```
Installing requirements

```bash
(env)$ ./install -h   # see options
(env)$ ./install [target]
```

## Usage

```bash
(env)$ python run.py [port default:8000]
```

the access credentials will be displayed in the terminal window.
open your browser

![browser](http://52.7.242.59/Felaban/apipruebas/web/users/ab.png)

![browser](http://52.7.242.59/Felaban/apipruebas/web/users/abc.png)

## Information

Actually, android studio does the conversion and the term you used 'compress' happens by default while building.

The compilation process for Android apps is very different from other Java applications. But it begins in the same way: your Java source code files are compiled into .class files using the javac command:

The .class files contain standard Oracle JVM Java byte-codes. But Android devices dont use this byte-code format. Instead, Android has its own distinct byte-code format called Dalvik. Dalvik byte-codes, like Oracle JVM byte-codes, are machine-code instructions for a theoretical processor.

The compilation process needs to convert the .class files, and any .jar libraries into a single classes.dex file containing Dalvik byte-codes. This is done with the dx command: This is how your classes.dex file is generated.

The classes.dex file and the resources from your application, such as images and layouts, are then compressed into a zip-like file called an Android Package or .apk file. This is done with the Android Asset Packaging Tool or aapt:
Your proguard rules, during the build process, help to

Shrink    – detects and removes unused classes, fields, methods, and attributes.
Optimize  – analyzes and optimizes the bytecode of the methods.
Obfuscate – renames the remaining classes, fields, and methods using short meaningless names.

Hope it helps you to some extent.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
It is free and open source.
