This is a sample system used to generate CDL files that can be processed by ASP. This repo contains a system definition file which is used by adli_system to inject logs and system level metadata in the programs.

Support for repo based system level log injection is being added currently.

### Dependencies:

The start and stop system python scripts rely on PM2 to mange the processes. So this adds a dependency on node and npm. Once that is installed, install PM2 using:

```shell
npm i pm2
```

To install the python dependencies (websockets), run:
```shell
pip install -r requirements.txt
```

### Starting the system

  ```shell
  python utils/start_system.py
  ```

### Stopping the system

  ```shell
  python utils/stop_system.py
  ```

### Checking PM2

  ```shell
  pm2 ps
  ```


## Overview:

![Simplified System Diagram](docs/systemDiagram.png)

The system consists of 5 programs:

- Job Handler 
- Merge Sort Worker
- Radix Sort Worker
- Bubble Sort Worker
- Simulated Client

The job handler starts a websocket server which accepts incoming connections from the client and each of the workers. When the workers connect to the job handler, they are registered and the type of they job they process is indexed. 

When the client connects to the job handler, it first registers the client connection. Any subsequent messages contain a request with a job type and this passed onto the relevant workers. The workers process the job and return a result which is passed back to the client. 

The simulateClient.py program connects to the job handler and periodically sends jobs to the job handler from different users and accepts the results.

To run the system, start the program in the following order:
- Job Handler
- Start Workers
- Start Simulated Client

I will automate this process soon, I am just manually running the programs to generate logs that I can use to extract system level traces.


