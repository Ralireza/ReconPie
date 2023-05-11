# Domain to IP Mapping
The tool should be able to map all subdomains to their corresponding IP addresses. This feature will help in identifying the hosting provider of the target website and any other websites hosted on the same server.
1. OSI model network
2. socket in pyhton
3. subdomains to ip

# Open Systems Interconnection (OSI) model
is a conceptual framework that describes the functions of a networking or telecommunication system. It divides communication into seven layers, each of which interacts with adjacent layers to perform a specific set of functions.

Here's a brief overview of the seven layers in the OSI model:

1. Physical layer: This layer deals with the physical transmission of data over a communication channel. It defines the electrical, mechanical, and timing specifications for the physical medium (such as copper wires, fiber-optic cables, or wireless channels) used for communication.

2. Data link layer: This layer organizes data bits into frames, adds error detection and correction codes, and manages access to the physical medium. It ensures that data is transmitted reliably between two directly connected nodes, such as two computers or a computer and a switch.

3. Network layer: This layer provides logical addressing and routing services to enable data to be transmitted across multiple network segments. It determines the best path for data to travel, based on the destination address and network conditions.

4. Transport layer: This layer provides end-to-end reliability and error recovery mechanisms to ensure that data is delivered successfully between applications running on different hosts. It is responsible for dividing data from upper layers into smaller segments, reassembling them at the receiving end, and ensuring that they arrive in the correct order.

5. Session layer: This layer establishes, maintains, and terminates connections between applications running on different hosts. It also provides synchronization and recovery services in case of errors or interruptions.

6. Presentation layer: This layer translates, encrypts, or compresses data to ensure that it can be understood by the receiving application. It deals with issues of data representation, such as character encoding, compression, and encryption.

7. Application layer: This layer provides services to user applications, such as email, web browsing, file transfer, and remote login. It interacts directly with the application software and implements application-level protocols, such as HTTP, SMTP, or FTP.

Each layer in the OSI model performs a specific set of functions, and its protocols interact with adjacent layers to provide end-to-end communication between applications running on different hosts. The OSI model is not a standard, but a conceptual framework that helps network designers and implementers understand how networking systems operate and communicate.