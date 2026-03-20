# Election Ballot System

An election ballot voting system built in Python utilizing socket communication. This project models a centralized election server and multiple polling stations ("Calpis") where voters can securely cast their ballots over a local network.

## Features

* **Client-Server Architecture:** Centralized tallying managed by a main server, with individual voting stations acting as clients communicating via TCP sockets.
* **Vote Validation:** Envelopes are validated to ensure they contain 0 to 4 notes of the exact same party. Votes for unrecognized candidates are automatically flagged.
* **Double Envelopes:** Support for "double envelopes" (an envelope inside an envelope tied to a specific voter), simulating special voting rules or absentee ballots.
* **Live Vote Management:** The server maintains an ongoing count of valid votes and gracefully discards invalid ones.
* **Remote Shutdown:** Administrators can safely conclude the election and terminate the server using a dedicated remote client.

## Installation

1. Clone the repository to your local machine.
2. Ensure you have Python 3.x installed. 

## Project Structure

* **Core Models:**
  * `Voter.py`: Represents a voter with an ID and a name.
  * `Note.py`: Represents a single voting slip for a specific party.
  * `Envelope.py`: Represents a standard voting envelope containing notes and housing validation logic.
  * `DoubleEnvelope.py`: Represents a nested envelope attached to a specific voter.
* **Networking & Logic:**
  * `protocolEnv.py`: Defines the networking protocol, byte-encoding (`pickle`), header generation, and static network variables (IP `127.0.0.1`, Port `80`).
  * `VoteManager.py`: Handles vote tallying and tracking of double envelopes.
* **Executables:**
  * `VoteServer.py`: The central server. Must be running to accept votes.
  * `RegularCalpi.py`: Standard polling station terminal for users to input their ID and cast their votes.
  * `calpi2.py`: Alternative polling station that processes double envelopes.
  * `quiting_client.py`: Sends a quit signal to close the server and fetch final results.

## How to Run

You will need to open multiple terminal windows to simulate the network. 

**1. Start the Server**
Initialize the central tallying server first so clients have a destination to connect to:
```bash
python VoteServer.py
```

**2. Open a Polling Station (Client)**
Open a new terminal window and run a polling station script:
```bash
python RegularCalpi.py
```
Follow the on-screen prompts to enter a voter ID, name, and cast a vote for one of the valid candidates (red, blue, green, yellow).

*(Optional)* Run the alternative polling station in another terminal:
```bash
python calpi2.py
```

**3. Close the Election**
When voting is complete, open a final terminal window to send the shutdown command and display final results on the server:
```bash
python quiting_client.py
```
```
