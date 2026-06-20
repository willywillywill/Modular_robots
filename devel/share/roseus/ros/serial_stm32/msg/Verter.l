;; Auto-generated. Do not edit!


(when (boundp 'serial_stm32::Verter)
  (if (not (find-package "SERIAL_STM32"))
    (make-package "SERIAL_STM32"))
  (shadow 'Verter (find-package "SERIAL_STM32")))
(unless (find-package "SERIAL_STM32::VERTER")
  (make-package "SERIAL_STM32::VERTER"))

(in-package "ROS")
;;//! \htmlinclude Verter.msg.html


(defclass serial_stm32::Verter
  :super ros::object
  :slots (_x _y ))

(defmethod serial_stm32::Verter
  (:init
   (&key
    ((:x __x) 0)
    ((:y __y) 0)
    )
   (send-super :init)
   (setq _x (round __x))
   (setq _y (round __y))
   self)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:serialization-length
   ()
   (+
    ;; int8 _x
    1
    ;; int8 _y
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int8 _x
       (write-byte _x s)
     ;; int8 _y
       (write-byte _y s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int8 _x
     (setq _x (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _x 127) (setq _x (- _x 256)))
   ;; int8 _y
     (setq _y (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _y 127) (setq _y (- _y 256)))
   ;;
   self)
  )

(setf (get serial_stm32::Verter :md5sum-) "6a20b9d8cfb71fa36c504f7f2d8fb5dc")
(setf (get serial_stm32::Verter :datatype-) "serial_stm32/Verter")
(setf (get serial_stm32::Verter :definition-)
      "int8 x
int8 y
")



(provide :serial_stm32/Verter "6a20b9d8cfb71fa36c504f7f2d8fb5dc")


