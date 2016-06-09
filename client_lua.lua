--
-- Created by IntelliJ IDEA.
-- User: pc30003
-- Date: 6/9/16
-- Time: 12:43 PM
-- To change this template use File | Settings | File Templates.
--

zmq = require 'lzmq'
context = zmq:context()

socket = context:socket(zmq.SUB)
-- Define subscription and messages with prefix to accept.
socket:set_subscribe("")
socket:connect('tcp://127.0.0.1:5000')

while true do
    local incoming_msg = socket:recv()
    print(incoming_msg)
end