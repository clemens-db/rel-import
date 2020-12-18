# Databricks notebook source
# Add the current project directory to the system path.
# We are working on making this just work without having to modify the sys.path
import sys
sys.path.append("/Workspace/Projects/clemens@databricks.com/rel-import")

# COMMAND ----------

# Run code defined in neighboring python files
import hello
print(hello.world())

# COMMAND ----------

# hello is a module imported from /Workspace/Projects/sai.suram@databricks.com/awesome/hello.py
# Lets print and see python confirm that for us 
print(hello)