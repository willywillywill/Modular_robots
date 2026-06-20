; Auto-generated. Do not edit!


(cl:in-package serial_stm32-msg)


;//! \htmlinclude verter.msg.html

(cl:defclass <verter> (roslisp-msg-protocol:ros-message)
  ((x
    :reader x
    :initarg :x
    :type cl:fixnum
    :initform 0)
   (y
    :reader y
    :initarg :y
    :type cl:fixnum
    :initform 0))
)

(cl:defclass verter (<verter>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <verter>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'verter)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name serial_stm32-msg:<verter> is deprecated: use serial_stm32-msg:verter instead.")))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <verter>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader serial_stm32-msg:x-val is deprecated.  Use serial_stm32-msg:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <verter>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader serial_stm32-msg:y-val is deprecated.  Use serial_stm32-msg:y instead.")
  (y m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <verter>) ostream)
  "Serializes a message object of type '<verter>"
  (cl:let* ((signed (cl:slot-value msg 'x)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'y)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <verter>) istream)
  "Deserializes a message object of type '<verter>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'x) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'y) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<verter>)))
  "Returns string type for a message object of type '<verter>"
  "serial_stm32/verter")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'verter)))
  "Returns string type for a message object of type 'verter"
  "serial_stm32/verter")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<verter>)))
  "Returns md5sum for a message object of type '<verter>"
  "6a20b9d8cfb71fa36c504f7f2d8fb5dc")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'verter)))
  "Returns md5sum for a message object of type 'verter"
  "6a20b9d8cfb71fa36c504f7f2d8fb5dc")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<verter>)))
  "Returns full string definition for message of type '<verter>"
  (cl:format cl:nil "int8 x~%int8 y~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'verter)))
  "Returns full string definition for message of type 'verter"
  (cl:format cl:nil "int8 x~%int8 y~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <verter>))
  (cl:+ 0
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <verter>))
  "Converts a ROS message object to a list"
  (cl:list 'verter
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
))
