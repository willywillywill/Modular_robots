
(cl:in-package :asdf)

(defsystem "serial_stm32-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Verter" :depends-on ("_package_Verter"))
    (:file "_package_Verter" :depends-on ("_package"))
  ))