# coding=utf-8
import yaml

config = yaml.load(file("dsql-config.yml"))
print config["DSQL"]["Hadoop"]["Client"][2]

