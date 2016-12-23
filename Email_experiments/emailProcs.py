###########################################################################
#   Python 3 Functions for processing IMAP email
#   by Jon Nuljon
#   December, 2016
###########################################################################
import os
import imaplib
import email

# we need an instance of IMAP4_SSL subclass
# this represents a secure IMAP4 connection to the mail server
def connection(mailServer, user, password):
    connectedServer = imaplib.IMAP4_SSL(mailServer) # establishes secure connection
    connectedServer.login(user, password)
    # lets make sure we are AUTHenticated
    connectedServer.select('INBOX')         # selects the mailbox folder we want
    return connectedServer                  # give the caller a connected server

# for closing connections
def close_connection(connectedServer):
    connectedServer.close()                 # this only works if state is select

# we need to collect assets received via MIME email transport
def getEmailMessages(connectedServer):
    # lets initialize a list to hold our email messages
    emailMessages = []
    # we search for new message IDs by flag 'UnSeen' for unread messages or 'ALL' for everything
    # should receive a tuple containing a response [OK | NOT OK]
    # followed by string of bytes that are messageIDs each separated by a space
    response, messageIDs = connectedServer.search(None,'ALL')
    # check response was OK and  messages not empty -- b'' means no bytes were returned
    if ((response == 'OK') and (messageIDs != [b''])):
        # iterate through the messageIDs bytes 
        # by splitting it into a list of bytes (words) each of which is an ID
        for ID in messageIDs[0].split():
            # lets try
            try:
                # fetch the RFC822 MIME message parts matched to ID (FLAG may be set to 'Seen')
                response, data = connectedServer.fetch(ID,'(RFC822)')
                # or to fetch the message covertly (so FLAG remains UnSeen) do this
                # response, data = connectedServer.fetch(ID, '(BODY.PEEK[])')
            except:
                # on exception we will close the connection
                connectedServer.close()
                # and return something like ('ID NOT OK')
                return emailMessages.append(str(ID) + ' ' + response)
            # lets extract the payload, i.e. the message parts, from data return
            # looks something like [(RFC822,'message parts'] index as data[0][1]
            # and use email module to cast the payload into a Message instance
            message = email.message_from_bytes(data[0][1])
            # append the message object to our asset list
            emailMessages.append(message)
            # lets try
            try:
                # to have the server retain the message in 'Seen' folder while testing/debugging
                response, data = connectedServer.store(ID, '+FLAGS', '\\Seen')
                # later we will no longer retain messages on  server by saving to "Deleted' folder
                # response, data = connectedServer.store(ID, '+FLAGS', '\\Deleted')
            except:
                # on exception we will close the connection
                close_connection(connectedServer)
                # and cast the ID as a string so we can return it with response ('ID NOT OK')
                return emailMessages.append(str(ID) + ' ' + response)
        #done iterating so close the connection and go home with our messages
        close_connection(connectedServer)
        return emailMessages
    # if search returned an empty byte there was no email to retrieve
    elif MessageIDs == [b'']:
        # close the connection
        close_connection(connectedServer)
        # and tell the caller
        return emailMessages.append(str(ID) + ' no messages to retrieve')
    # otherwise search response was not OK
    else:
        # close the connection
        close_connection(connectedServer)
        # and tell the caller
        return emailMessages.append('search response ' + response)
    # we should not be here any more, but if we are somehow, close and report back
    close_connection(connectedServer)
    return emailMessages.append('heads up! we are somehow out of bounds')

# given a message object, this function will find attached file assets and put them
# in a special place or dump them to the default location
def saveFileAssets(aMessage, fileDump='.\\fileDump'):
     # we will return the URL if we find any attached file asset(s)
     # initially our signal to the caller is 'None found'
    URLs = ['None found']
    # use the email module's walk method to iterate through the message's MIME parts
    for parts in aMessage.walk():
        # if the part is 'multi-part', continue to next iteration
        if parts.get_content_maintype() == 'multipart':
            continue
        # if part  has content-disposition of 'None', continue to next iteration
        if parts.get_content_disposition() == 'None':
            continue
        # lets get a filename
        filename = parts.get_filename()
        # if we don't have a filename as either a byte or string, just continue to the next iteration
        if not isinstance(filename, (bytes,str)):
            continue
        # since we did have a byte or string, assemble the URL- join method conserves memory
        URL= os.path.join(fileDump, filename)
        # if this is the first URL (we have not overwritten default yet)
        if URLs[0] == "None found":
            # overwrite the default item
            URLs[0] = URL
        else:
            # other wise add the URL to the end of the list of URLs
            URLs.append(URL)
        # if we are sure file does not already exist in the fileDump
        if not os.path.isfile(URL):
            # open a new dumpFile for writing binary mode
            dumpFile = open(URL, 'wb')
            # write the message part payload
            dumpFile.write(parts.get_payload(decode = True))
            # close the dumpFIle
            dumpFile.close()
        # from here we will should continue to iterate automatically but lets be clear
        continue
    # done iterating so lets return the URLs to caller
    return URLs


if __name__ == '__main__':
    # set the host server
    mailServer = 'bootstrap.nuljon.com'
    # set the username
    user = "publish@bootstrap.nuljon.com"
    # set the password
    password = ''
    # call the connection function passing host and credentials and assign the connected server
    myServer = connection(mailServer, user, password)
    # output connected server to console for debugging
    print(myServer)
    # pass our connected server to function for retrieving messages and assign them
    myMessages = getEmailMessages(myServer)
    # output the messages to console for debugging
    print(myMessages)
    # iterate through the messages
    for myMessage in myMessages:
        # pass each message to the function for saving attachments and assign URLs
        URLs=saveFileAssets(myMessage)
        # output the URLs to console for debugging
        print(URLs)
    # we are done for now
    exit()
