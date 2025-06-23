sent_msg="Hi there ! This is a secret message."
unsent_msg="This message is unsending...."
try:
    def msgsent(sent_msg,unsent_msg,file):
        with open(file,'w') as f:
            f.write(sent_msg)
           
        with open(file,'r+') as f:
            f.seek(0)
            og_txt=f.read()
            print("Original MSG = ",og_txt)
            f.truncate(len(unsent_msg))
            f.write(unsent_msg)
            print("Unsent MSG = ",unsent_msg)

finally:
    print('Final block')



msgsent(sent_msg,unsent_msg,'test.txt')

