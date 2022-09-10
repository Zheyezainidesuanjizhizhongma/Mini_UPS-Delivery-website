import ups_amazon_pb2
import world_ups_pb2
import time
import threading
import psycopg2
import socket
import sys
from concurrent.futures import ThreadPoolExecutor
from google.protobuf.internal.decoder import _DecodeVarint32
from google.protobuf.internal.encoder import _EncodeVarint
sys.path.append("..")

conn = 0
u_seqnum = 1
worldSocket = 2
amazonSocket = 3
truck_id = -1
msgDict = dict()
sim_speed = 1000
lock = threading.Lock()
uid = -1


def sendEncodedMessage(mySocket, msg):
    ENCODED_MESSAGE = msg.SerializeToString()
    _EncodeVarint(mySocket.send, len(ENCODED_MESSAGE), None)
    mySocket.send(ENCODED_MESSAGE)


def recvDecodedMessage(mySocket):
    var_int_buff = []
    while True:
        buf = mySocket.recv(1)
        var_int_buff += buf
        msg_len, new_pos = _DecodeVarint32(var_int_buff, 0)
        if new_pos != 0:
            break
    whole_message = mySocket.recv(msg_len)
    return whole_message


def connectToWorld():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1', 12345))
    except socket.error as error_msg:
        print(error_msg)
        sys.exit(1)
    print("success: connect to world")
    # print(s.recv(1024))
    # s.close()
    return s


def connectToAmazon():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # s.connect(('127.0.0.1', 16789))
        s.connect(('vcm-24288.vm.duke.edu', 55555))
        # s.connect(('vcm-26537.vm.duke.edu', 55555))
    except socket.error as error_msg:
        print(error_msg)
        sys.exit(1)
    print("success: connect to Amazon")
    return s


def createNewWorld(mySocket, truck_num):
    myConnect = world_ups_pb2.UConnect()
    myConnect.isAmazon = False
    myConnect.trucks.extend(initializeTrucks(truck_num))
    sendEncodedMessage(mySocket, myConnect)
    connect_msg = recvDecodedMessage(mySocket)
    myConnected = world_ups_pb2.UConnected()
    myConnected.ParseFromString(connect_msg)
    connect_result = myConnected.result
    connect_world_id = myConnected.worldid

    print(connect_result)
    if connect_result == 'connected!':
        return connect_world_id
    else:  # error message
        print(connect_result)
        return None


def initializeTrucks(num):
    truck_list = []
    for i in range(0, num):
        myTruck = world_ups_pb2.UInitTruck()
        myTruck.id = i
        myTruck.x = 0  # initialize every truck's position
        myTruck.y = 0
        truck_list.append(myTruck)
    return truck_list


def connectToDatabase():
    global conn

    conn = psycopg2.connect(database="jlrjytnd", user="jlrjytnd",
                            password="uhhK1B4Bd7nFLNNRsK_Ml7mYfgMZLsy5", host="isilo.db.elephantsql.com", port="5432")
    conn.set_isolation_level(3)  # 3: serializable
    print('connect to database successfully')
    # cur = conn.cursor()
    # cur.execute('''DROP TABLE IF EXISTS ups_front_product_info''')
    # cur.execute('''DROP TABLE IF EXISTS ups_front_package_info''')
    # cur.execute('''DROP TABLE IF EXISTS ups_front_truck_info''')
    # cur.execute('''DROP TABLE IF EXISTS auth_user''')
    # cur.execute('''CREATE TABLE TRUCK_INFO
    #             (TRUCK_ID INT PRIMARY KEY   NOT NULL,
    #             TRUCK_STATUS CHAR(50)     NOT NULL);''')
    #             # USER_ID       INT REFERENCES  USER(USERNAME) ON DELETE SET NULL ON UPDATE CASCADE,
    # cur.execute('''CREATE TABLE PACKAGE_INFO
    #             (PACKAGE_ID   INT PRIMARY KEY NOT NULL,
    #             USER_ID       INT             NOT NULL,
    #             STATUS        CHAR(50)        NOT NULL,
    #             DESTINATION_X INT             NOT NULL,
    #             DESTINATION_Y INT             NOT NULL,
    #             TRUCK_ID      INT REFERENCES  TRUCK_INFO(TRUCK_ID) ON DELETE SET NULL ON UPDATE CASCADE);''')
    # cur.execute('''CREATE TABLE PRODUCT_INFO
    #             (PRODUCT_ID   INT PRIMARY KEY NOT NULL,
    #             DESCRIPTION   CHAR(100)       NOT NULL,
    #             COUNT         INT             NOT NULL,
    #             PACKAGE_ID    INT REFERENCES  PACKAGE_INFO(PACKAGE_ID) ON DELETE SET NULL ON UPDATE CASCADE);''')
    # conn.commit()


# If UPS has not received ack in 5 seconds, it will send again the message
def handleMsgSent(mySocket, seqnum):
    print('handling message sent...')
    print('msgDict: ', msgDict)
    while True:
        time.sleep(5)
        print('rrrrrrrrrrrrr')
        if seqnum in msgDict.keys():
            sendEncodedMessage(mySocket, msgDict[seqnum])
        else:
            break
    print('receive ack successfully: ', seqnum)


def sendErrorMsg(mySocket, originSeqnum, error_msg):
    global u_seqnum

    u_msg = ups_amazon_pb2.UMsgs()
    u_error = u_msg.error.add()
    u_error.err = error_msg
    u_error.originseqnum = originSeqnum
    lock.acquire()
    u_seqnum =u_seqnum + 1
    u_error.seqnum = u_seqnum
    lock.release()
    sendEncodedMessage(mySocket, u_msg)


def handleAReqTruck(tr):
    # 可以看出，全局变量的值改变，必须要有global关键字。不然就被当成了局部变量
    global u_seqnum, truck_id, uid

    # get AReqTruck details
    wh = tr.warehouse
    wh_id = wh.id
    prd = tr.product
    pck_id = tr.packageid
    dest_x = tr.buyer_x
    dest_y = tr.buyer_y
    old_seq_num = tr.sequenceNum
    uname = tr.ups_name  # a system default is used: the empty string for strings

    try:
        if uname:
            # inquire about the existence of the username
            try:
                cur = conn.cursor()
                cur.execute("SELECT ID FROM AUTH_USER WHERE USERNAME='"+uname+"';")
                conn.commit()
            except:
                conn.rollback()

            user_info = cur.fetchone()
            if user_info:
                uid = user_info[0]

        # insert package info
        truck_id = truck_id + 1
        print('truck_id: ', truck_id)

        try:
            cur = conn.cursor()
            cur.execute("INSERT INTO UPS_FRONT_TRUCK_INFO VALUES(" +
                        str(truck_id)+","+"'idle'"+");")
            if uid!=-1:
                cur.execute("INSERT INTO UPS_FRONT_PACKAGE_INFO (package_id, user_id, status, destination_x, destination_y, truck_id) VALUES("+str(pck_id)+"," +
                        str(uid)+", 'packed' ,"+str(dest_x)+","+str(dest_y)+","+str(truck_id)+");")
            else:
                cur.execute("INSERT INTO UPS_FRONT_PACKAGE_INFO (package_id, status, destination_x, destination_y, truck_id) VALUES("+str(pck_id)+"," +
                        "'packed' ,"+str(dest_x)+","+str(dest_y)+","+str(truck_id)+");")
            # insert product info
            for p in prd:
                cur.execute("INSERT INTO UPS_FRONT_PRODUCT_INFO (product_id, description, count, package_id) VALUES("+str(p.id) +
                            ",'"+str(p.description)+"',"+str(p.count)+","+str(pck_id)+");")
            conn.commit()
        except:
            conn.rollback()

        cur.close()

        sendPickup(truck_id, wh_id)
    except:
        sendErrorMsg(amazonSocket, old_seq_num, '[UPS Error]: error in handling AReqTruck')


# UPS sends GoPickUp to World
def sendPickup(truck_id, wh_id):
    global u_seqnum, msgDict

    u_command = world_ups_pb2.UCommands()
    # UPS sends GoPickUp to World
    myGoPickup = u_command.pickups.add()
    myGoPickup.truckid = truck_id
    myGoPickup.whid = wh_id
    lock.acquire()
    u_seqnum = u_seqnum + 1
    myGoPickup.seqnum = u_seqnum  # global variable
    lock.release()
    print('myGoPickup:', myGoPickup)

    u_command.simspeed = sim_speed

    try:
        cur = conn.cursor()
        cur.execute(
            "UPDATE UPS_FRONT_TRUCK_INFO SET TRUCK_STATUS='traveling' WHERE TRUCK_ID="+str(truck_id)+";")
        cur.execute(
            "UPDATE UPS_FRONT_PACKAGE_INFO SET STATUS='loading' WHERE TRUCK_ID="+str(truck_id)+";")
        conn.commit()
    except:
        conn.rollback()
    cur.close()

    # msgDict[u_seqnum] = u_command.SerializeToString()
    msgDict[u_seqnum] = u_command
    sendEncodedMessage(worldSocket, u_command)
    handleMsgSent(worldSocket, u_seqnum)


def sendTruckArrived(truck_id):
    global u_seqnum, msgDict

    u_message = ups_amazon_pb2.UMsgs()
    myTruckArrived = u_message.trucks.add()
    myTruckArrived.truckid = truck_id
    
    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT PACKAGE_ID FROM UPS_FRONT_PACKAGE_INFO WHERE TRUCK_ID="+str(truck_id)+";")
        conn.commit()
    except:
        conn.rollback()
    
    pck_info = cur.fetchone()
    pck_id = pck_info[0]
    myTruckArrived.packageid = pck_id
    lock.acquire()
    u_seqnum = u_seqnum + 1
    myTruckArrived.seqnum = u_seqnum
    lock.release()
    print('myTruckArrived: ', myTruckArrived)

    # msgDict[u_seqnum] =  u_message.SerializeToString()
    msgDict[u_seqnum] = u_message
    sendEncodedMessage(amazonSocket, u_message)
    handleMsgSent(amazonSocket, u_seqnum)
    cur.close()


def handleCompletions(c):
    print('handling completions...')
    # set the truck status to ARRIVE WAREHOUSE
    truck_id = c.truckid

    try:
        cur = conn.cursor()
        cur.execute(
            "UPDATE UPS_FRONT_TRUCK_INFO SET TRUCK_STATUS='arrive warehouse' WHERE TRUCK_ID="+str(truck_id)+";")
        conn.commit()
    except:
        conn.rollback()
    cur.close()
    print('update truck status successfully')

    # UPS sends back to Amazon that the truck has already arrived
    sendTruckArrived(truck_id)


# =========================================================================================
# UPS sends GoDeliver to World
def sendDeliver(truck_id, pck_id):
    global u_seqnum, msgDict

    u_command = world_ups_pb2.UCommands()
    # UPS sends GoDeliver to World
    myGoDeliver = u_command.deliveries.add()
    myGoDeliver.truckid = truck_id
    
    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT DESTINATION_X, DESTINATION_Y FROM UPS_FRONT_PACKAGE_INFO WHERE PACKAGE_ID=" + str(pck_id) + ";")
        conn.commit()
    except:
        conn.rollback()
    
    dest_info = cur.fetchone()
    dest_x = dest_info[0]
    dest_y = dest_info[1]
    pck = myGoDeliver.packages.add()
    pck.packageid = pck_id
    pck.x = dest_x
    pck.y = dest_y
    lock.acquire()
    u_seqnum = u_seqnum + 1
    myGoDeliver.seqnum = u_seqnum  # global variable
    lock.release()
    cur.close()

    print('myGoDeliver:', myGoDeliver)

    #u_command.simspeed = sim_speed

    # update the status of truck and package
    try:
        cur = conn.cursor()
        cur.execute(
            "UPDATE UPS_FRONT_TRUCK_INFO SET TRUCK_STATUS='delivering' WHERE TRUCK_ID="+str(truck_id)+";")
        cur.execute(
            "UPDATE UPS_FRONT_PACKAGE_INFO SET STATUS='delivering' WHERE TRUCK_ID="+str(truck_id)+";")
        conn.commit()
    except:
        conn.rollback()
    cur.close()

    # msgDict[u_seqnum] = u_command.SerializeToString()
    msgDict[u_seqnum] = u_command
    sendEncodedMessage(worldSocket, u_command)
    handleMsgSent(worldSocket, u_seqnum)


def handleACompleteLoading(cl):
    global truck_id

    # get ACompleteLoading details
    truck_id = cl.truckid
    pck_id = cl.packageid
    old_seq_num = cl.sequenceNum

    try:
        print('truck_id: ', truck_id)

        # update the status of package and truck
        try:
            cur = conn.cursor()
            cur.execute(
                "UPDATE UPS_FRONT_TRUCK_INFO SET TRUCK_STATUS='loading' WHERE TRUCK_ID="+str(truck_id)+";")
            cur.execute(
                "UPDATE UPS_FRONT_PACKAGE_INFO SET STATUS='loaded' WHERE PACKAGE_ID="+str(pck_id)+";")
            conn.commit()
        except:
            conn.rollback()
        cur.close()
        print('aaaaaaaaaaaaaaa')
        sendDeliver(truck_id, pck_id)
        print('bbbbbbbbbbbbbbbb')
    except:
        sendErrorMsg(amazonSocket, old_seq_num, '[UPS Error]: error in handling ACompleteLoading')


def sendFinishDelivery(pck_id):
    global u_seqnum, msgDict

    u_message = ups_amazon_pb2.UMsgs()
    myFinishDelivery = u_message.finish.add()
    myFinishDelivery.packageid = pck_id
    lock.acquire()
    u_seqnum = u_seqnum + 1
    myFinishDelivery.seqnum = u_seqnum
    lock.release()
    print('myFinishDelivery: ', myFinishDelivery)

    # msgDict[u_seqnum] =  u_message.SerializeToString()
    msgDict[u_seqnum] = u_message
    sendEncodedMessage(amazonSocket, u_message)
    handleMsgSent(amazonSocket, u_seqnum)


def handleDelivered(d):
    print('handling delivered...')

    truck_id = d.truckid
    pck_id = d.packageid

    try:
        cur = conn.cursor()
        cur.execute(
            "UPDATE UPS_FRONT_TRUCK_INFO SET TRUCK_STATUS='idle' WHERE TRUCK_ID="+str(truck_id)+";")
        cur.execute(
            "UPDATE UPS_FRONT_PACKAGE_INFO SET STATUS = 'delivered' WHERE PACKAGE_ID=" + str(pck_id) + ";")
        conn.commit()
    except:
        conn.rollback()
    cur.close()
    print('update truck status successfully')
    print('update package status successfully')

    # UPS sends back to Amazon that the truck has already delivered package
    sendFinishDelivery(pck_id)


# UPS sends query to World about truck status
def sendQuery(truck_id):
    global u_seqnum

    u_command = world_ups_pb2.UCommands()
    myQuery = u_command.queries.add()
    myQuery.truckid = truck_id
    lock.acquire()
    u_seqnum = u_seqnum + 1
    myQuery.seqnum = u_seqnum
    lock.release()
    print('myQuery: ', myQuery)

    # msgDict[u_seqnum] =  u_command.SerializeToString()
    msgDict[u_seqnum] = u_command
    sendEncodedMessage(worldSocket, u_command)
    handleMsgSent(worldSocket, u_seqnum)


def handleTruckStatus(ts):
    print('handling truck status...')

    truck_id = ts.truckid
    truck_status = ts.status
    truck_x = ts.x
    truck_y = ts.y

    print('truck id: ', truck_id)
    print('truck status: ', truck_status)
    print('truck x: ', truck_x)
    print('truck y: ', truck_y)


# =========================================================================================


# UPS sends back to Amazon acks
def sendRecvAmazonAcks(ua_response):
    print('sending back Amazon acks...')
    # send back to Amazon acks that
    ack_list = []

    # lock.acquire()
    if ua_response.reqtruck:
        for tr in ua_response.reqtruck:
            ack_list.append(tr.sequenceNum)
    if ua_response.completeloading:
        for cl in ua_response.completeloading:
            ack_list.append(cl.sequenceNum)
    if ua_response.err:
        for e in ua_response.err:
            ack_list.append(e.seqnum)
    if ua_response.acks:
        for a in ua_response.acks:
            print('qqqqqqqqqqqqq ack: ', a)
            if a in msgDict.keys():
                print('eeeeeeeeeeeeeee ack: ', a)
                msgDict.pop(a)
    # lock.release()

    if ack_list:
        print('ack_list: ', ack_list)
        u_msg = ups_amazon_pb2.UMsgs()
        u_msg.acks.extend(ack_list)
        print('sendAmazonAcks: ', u_msg)
        sendEncodedMessage(amazonSocket, u_msg)


# UPS sends back to World acks and receive acks from World
def sendRecvWorldAcks(world_response):
    global msgDict

    print('sending back World acks...')
    # send back to World acks that
    ack_list = []

    if world_response.completions:
        for cp in world_response.completions:
            ack_list.append(cp.seqnum)
    if world_response.delivered:
        for d in world_response.delivered:
            ack_list.append(d.seqnum)
    if world_response.truckstatus:
        for ts in world_response.truckstatus:
            ack_list.append(ts.seqnum)
    if world_response.error:
        for e in world_response.error:
            ack_list.append(e.seqnum)
    if world_response.acks:  # receive acks from World
        print('vvvvvvvvvvvvvvvv')
        for a in world_response.acks:
            if a in msgDict.keys():
                msgDict.pop(a)

    print('ack_list: ', ack_list)
    if ack_list:
        u_commands = world_ups_pb2.UCommands()
        u_commands.acks.extend(ack_list)
        print('sendWorldAcks: ', u_commands)
        sendEncodedMessage(worldSocket, u_commands)


def handleAmazon():
    print("handling Amazon...")
    pool = ThreadPoolExecutor(max_workers=30)

    while True:
        try:
            # test if ups can receive msg from amazon
            ua_response = ups_amazon_pb2.AMsgs()
            ua_response.ParseFromString(recvDecodedMessage(amazonSocket))
            print('====================')
            print('ua_response: ', ua_response)
            sendRecvAmazonAcks(ua_response)

            if ua_response.reqtruck:
                # UPS send GoPickUp to World
                print('reqtruck: ', ua_response.reqtruck)
                for tr in ua_response.reqtruck:
                    #handleAReqTruck(tr)
                    pool.submit(handleAReqTruck, tr)
            elif ua_response.completeloading:
                print('completeloading: ', ua_response.completeloading)
                for cl in ua_response.completeloading:
                    # handleACompleteLoading(tr)
                    pool.submit(handleACompleteLoading, cl)
            elif ua_response.err:
                print('err: ', ua_response.err)
                for e in ua_response.err:
                    print('error:', e.err, ' originseqnum:', e.originseqnum)
        except:
            print('error')
            continue


def handleWorld():
    print("handling World...")
    pool = ThreadPoolExecutor(max_workers=30)

    while True:
        try:
            world_response = world_ups_pb2.UResponses()
            world_response.ParseFromString(recvDecodedMessage(worldSocket))
            print('world_response: ', world_response)
            print('zzzzzzzzzzzzzzzz')
            # send back acks to World
            sendRecvWorldAcks(world_response)

            if world_response.completions:
                print('completions: ', world_response.completions)
                for c in world_response.completions:
                    # handleCompletions(c)
                    pool.submit(handleCompletions, c)
            if world_response.delivered:
                print('delivered: ', world_response.delivered)
                for d in world_response.delivered:
                    # handleDelivered(d)
                    pool.submit(handleDelivered, d)
            if world_response.truckstatus:
                print('truckstatus: ', world_response.truckstatus)
                for ts in world_response.truckstatus:
                    # handleTruckStatus(ts)
                    pool.submit(handleTruckStatus, ts)
            if world_response.error:
                print('error: ', world_response.error)
                for e in world_response.err:
                    print('error:', e.err, ' originseqnum:', e.originseqnum)
            if world_response.finished:
                print('UPS finish the service..')
                break
        except:
            print('error~~~')
            continue


def handleFunc(truck_num):
    global amazonSocket
    global worldSocket

    # connect to Amazon
    amazonSocket = connectToAmazon()

    # connect to World
    worldSocket = connectToWorld()
    world_id = createNewWorld(worldSocket, truck_num)

    if(world_id == None):
        return "error"
    else:
        print('world id:', world_id)
        world_id = str(world_id)
        amazonSocket.send(world_id.encode('utf-8'))

        # wait for Amazon to connect to World
        time.sleep(1)
            
        t1 = threading.Thread(target=handleAmazon)
        t2 = threading.Thread(target=handleWorld)
        t1.start()
        t2.start()
        t1.join()
        t2.join()


if __name__ == '__main__':
    truck_number = 100
    connectToDatabase()  # main函数中不需要使用gloabl来声明
    cur = conn.cursor()
    cur.execute("DELETE FROM UPS_FRONT_FEEDBACK_INFO;")
    cur.execute("DELETE FROM UPS_FRONT_PRODUCT_INFO;")
    cur.execute("DELETE FROM UPS_FRONT_PACKAGE_INFO;")
    cur.execute("DELETE FROM UPS_FRONT_TRUCK_INFO;")
    conn.commit()
    handleFunc(truck_number)
    conn.close()
