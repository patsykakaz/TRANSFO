#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from base64 import b64encode
from hashlib import sha1
# 
from pysimplesoap.client import SoapClient, SimpleXMLElement
from pysimplesoap.helpers import *

def authenticateByEmail(username,password):
    # wsdl = "http://dev.aboweb.com/aboweb/ClientService?wsdl"
    client = SoapClient(location = "http://aboweb.com/aboweb/ClientService",trace=False)
    client['wsse:Security'] = {
           'wsse:UsernameToken': {
                'wsse:Username': 'admin.webservices@mbc.com',
                # 'wsse:Password': 'tRPTUOP+QQYzVcxYZeQXsiTJ+dw=',
                'wsse:Password': 'pYsIJKF18hj0SvS3TwrQV3hWzD4=',
                }
            }
    params = SimpleXMLElement('<?xml version="1.0" encoding="UTF-8"?><ges:authenticateByEmail xmlns:ges="http://www.gesmag.com/"><email>'+username+'</email><encryptedPassword>'+ b64encode(sha1(password).digest()) +'</encryptedPassword></ges:authenticateByEmail>')
    response = client.call("authenticateByEmail",params)
    xml = SimpleXMLElement(client.xml_response)
    return str(xml('result'))

def ABM_ACCES_CLIENT(username,password):
    clientABM = SoapClient(wsdl="http://aboweb.com/aboweb/abmWeb?wsdl", ns="web", trace=False)
    clientABM['AuthHeaderElement'] = {'login': 'admin.webservices@mbc.com', 'password': 'MBC1475'}
    resultABM = clientABM.ABM_ACCES_CLIENT('207',username,password)
    xml = SimpleXMLElement(clientABM.xml_response)
    return xml('codeClient')

def ABM_TEST_MAIL(mail):
    # webservice to check for mail occurence in aboweb DB
    # Status should be 00 (found) or 01 (not found)
    clientABM = SoapClient(wsdl="http://aboweb.com/aboweb/abmWeb?wsdl", ns="web", trace=False)
    clientABM['AuthHeaderElement'] = {'login': 'admin.webservices@mbc.com', 'password': 'MBC1475'}
    resultABM = clientABM.ABM_TEST_MAIL(refEditeur='207',refSociete='1',email=mail)
    xml = SimpleXMLElement(clientABM.xml_response)
    return xml('status')

def ABM_MOT_PASSE_OUBLIE(mail):
    clientABM = SoapClient(wsdl="http://aboweb.com/aboweb/abmWeb?wsdl", ns="web", trace=False)
    clientABM['AuthHeaderElement'] = {'login': 'admin.webservices@mbc.com', 'password': 'MBC1475'}
    resultABM = clientABM.ABM_MOT_PASSE_OUBLIE(refEditeur='207',email=mail)
    xml = SimpleXMLElement(clientABM.xml_response)
    return xml('return')

def getClient(codeClient):
    client = SoapClient(location="http://aboweb.com/aboweb/ClientService?wsdl",trace=False)
    client['wsse:Security'] = {
           'wsse:UsernameToken': {
                'wsse:Username': 'admin.webservices@mbc.com',
                'wsse:Password': 'pYsIJKF18hj0SvS3TwrQV3hWzD4=',
                # 'wsse:Password': 'tRPTUOP+QQYzVcxYZeQXsiTJ+dw=',
                }
            }
    params = SimpleXMLElement('<?xml version="1.0" encoding="UTF-8"?><ges:getClient xmlns:ges="http://www.gesmag.com/"><codeClient>'+codeClient+'</codeClient></ges:getClient>');
    result = client.call("getClient",params)
    xml = SimpleXMLElement(client.xml_response)
    return xml.children().children().children()

def createOrUpdateClientEx(target):
    client = SoapClient(location="http://aboweb.com/aboweb/ClientService?wsdl",trace=False)
    client['wsse:Security'] = {
           'wsse:UsernameToken': {
                'wsse:Username': 'admin.webservices@mbc.com',
                'wsse:Password': 'pYsIJKF18hj0SvS3TwrQV3hWzD4=',
                }
            }
    target = SimpleXMLElement('<?xml version="1.0" encoding="UTF-8"?><ges:createOrUpdateClientEx xmlns:ges="http://www.gesmag.com/">'+ repr(target) +'</ges:createOrUpdateClientEx>')
    client.call('createOrUpdateClientEx',target)
    xml = SimpleXMLElement(client.xml_response)
    return xml


def getAbonnements(codeClient):
    # return xml containing a list of user abonnements 
    clientAbonnement = SoapClient(location ="http://aboweb.com/aboweb/AbonnementService",trace=False)
    clientAbonnement['wsse:Security'] = {
                    'wsse:UsernameToken': {
                        'wsse:Username': 'admin.webservices@mbc.com',
                        # 'wsse:Password': 'tRPTUOP+QQYzVcxYZeQXsiTJ+dw=',
                        'wsse:Password': 'pYsIJKF18hj0SvS3TwrQV3hWzD4=',
                    }
                }

    params = SimpleXMLElement('<?xml version="1.0" encoding="UTF-8"?><ges:getAbonnements xmlns:ges="http://www.gesmag.com/"><codeClient>%s</codeClient><offset>0</offset></ges:getAbonnements>' % codeClient)
    result = clientAbonnement.call("getAbonnements",params)
    xml = SimpleXMLElement(clientAbonnement.xml_response)
    return xml

