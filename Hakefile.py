#!/usr/bin/env python3

from hake import start, task, default_task, run_tasks

@default_task
def task_default():
  run_tasks('build', 'install')

@task('build')
def task_build():
  print('Build')

@task('install')
def task_install():
  print('Install')

start()