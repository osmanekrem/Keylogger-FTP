# Keyboard Logger with FTP Upload
This is a script to log all keyboard input and upload the log file to an FTP server. The script uses the pynput library to capture keyboard input and ftplib library to upload the log file to an FTP server. 

## Usage
1. Edit the FTP server login credentials in the code (ftp.server.com, username, password).
2. Change the key sequence to the desired trigger to start the keyboard logger.
3. Run the script.
4. Type the trigger sequence on the keyboard to start logging.
5. The log file will be uploaded to the FTP server once the trigger sequence is completed.

## Libraries
- pynput (for capturing keyboard input)
- ftplib (for uploading the log file to FTP server)
- os (for creating a child process to run the keyboard listener in the background)

