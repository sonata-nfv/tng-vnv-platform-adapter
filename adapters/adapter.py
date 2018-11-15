#!/usr/bin/python

from flask import Flask, request, jsonify, render_template
import os, sys, logging, uuid


class Adapter:

    def __init__(self, name, host, type):
        self.name = name
        self.host = host
        self.type = type

    def getName(self):
        return self.name
    def setName(self, newName):
        self.name = newName        

    def getHost(self):
        return self.host
    def setHost(self, newHost):
        self.host = newHost

    def getType(self):
        return self.type
    def setType(self, newType):
        self.type = newType        

