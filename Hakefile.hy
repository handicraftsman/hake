#!/usr/bin/env hy

(import [hake [start def-task def-default-task run-tasks]])

(def-default-task (fn []
  (run-tasks "build" "install")))

(def-task "build" (fn []
  (print "Build")))

(def-task "install" (fn []
  (print "Install")))

(start)