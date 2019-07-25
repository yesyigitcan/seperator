# -*- coding: utf-8 -*-
"""
Info:
    Linkedin: https://www.linkedin.com/in/yesyigitcan/
"""

import xml.etree.ElementTree as ET

class XML_Query_Helper:
    
    def __init__(self,path):
        if(type(path) != str):
            self.root = ET.ElementTree(path).getroot()
        else:
            self.root = ET.parse(path).getroot()
        
    def columns(self):
        temp = []
        for i in self.root:
            temp.append(i.tag)
        return temp
        
    def XML2List(self,column_name,special_key = "NO_REQUIRED_SPECIAL_KEY",extra_label = [],extra_values = [],target_columns = "NO_REQUIRED_TARGET_COLUMNS",leaf_node = False,leaf_num = 0,special_col = []):
        
        len_label = len(extra_label)
        len_values = len(extra_values)
        if(len_label != len_values):
            print("Extra Label Size Must Be Equal to Extra Values Size. But it is not!")
            return
        
        column = self.root.findall(column_name)
        self.label_set = []
        self.values_set = []
        for i in column: # i 
            for j in i:
                
                if(special_key == "NO_REQUIRED_SPECIAL_KEY"):
                    if(target_columns == "NO_REQUIRED_TARGET_COLUMNS"):
                        
                        if(leaf_node):
                            
                            if(j.text == None):
                                
                                leaf_counter = 1
                                for leaf in j:
                                    
                                    if(leaf_counter > leaf_num and j.tag not in special_col):
                                        break
                                    self.label_set.append(j.tag + "_" + str(leaf_counter))
                                    self.values_set.append(leaf.text)
                                    leaf_counter += 1
                            else:
                                self.label_set.append(j.tag)
                                self.values_set.append(j.text)
                        else:
                            self.label_set.append(j.tag)
                            self.values_set.append(j.text)
                    else:
                        if(leaf_node):
                            if(j.text == None):
                                leaf_counter = 1
                                for leaf in j:
                                    if(leaf_counter > leaf_num):
                                        break
                                    tag_name = leaf.tag + "_" + str(leaf_counter)
                                    if(tag_name in target_columns):
                                        self.label_set.append(tag_name)
                                        self.values_set.append(leaf.text)
                                        leaf_counter += 1
                            else:
                                if(j.tag[:2] in target_columns):
                                    self.label_set.append(j.tag)
                                    self.values_set.append(j.text)
                        else:
                            if(j.tag[:2] in target_columns):
                                self.label_set.append(j.tag)
                                self.values_set.append(j.text)
                        
                elif(j.tag[:2] == special_key):
                    if(target_columns == "NO_REQUIRED_TARGET_COLUMNS"):
                        if(leaf_node):
                            if(j.text == None):
                                leaf_counter = 1
                                for leaf in j:
                                    
                                    if(leaf_counter > leaf_num and j.tag not in special_col):
                                        break
                                    self.label_set.append(j.tag + "_" + str(leaf_counter))
                                    self.values_set.append(leaf.text)
                                    leaf_counter += 1
                            else:
                                self.label_set.append(j.tag)
                                self.values_set.append(j.text)
                        else:
                            self.label_set.append(j.tag)
                            self.values_set.append(j.text)
                    else:
                        if(leaf_node):
                            if(j.text == None):
                                leaf_counter = 1
                                for leaf in j:
                                    if(leaf_counter > leaf_num and j.tag not in special_col):
                                        break
                                    tag_name = j.tag + "_" + str(leaf_counter)
                                    if(tag_name in target_columns):
                                        self.label_set.append(tag_name)
                                        self.values_set.append(leaf.text)
                                        leaf_counter += 1
                            else:
                                if(j.tag in target_columns):
                                    self.label_set.append(j.tag)
                                    self.values_set.append(j.text)
                        else:
                            if(tag_name in target_columns):
                                self.label_set.append(j.tag)
                                self.values_set.append(j.text)
                    
        
        for i in range(len_label):
            self.label_set.append(extra_label[i])
            self.values_set.append(extra_values[i])
        return self.label_set,self.values_set
        
        
    def XML_Query(self,db_id,label,values,target_table):
        list_len = len(label)
        if(list_len < 1):
            print("**Empty List**")
            return
        
        query = "INSERT INTO " + target_table + "\n("
        query += "ID"
        for i in range(0,list_len):
            
            query += "," + str(label[i])
        query += ") \nVALUES \n("
        
        query += str(db_id)
            
        for i in range(0,list_len):
            if(values[i] == "SYSDATE"):
              query += "," + values[i]  
            elif(values[i] == None):
                query += ",NULL"
            else:
                if(type(values[i]) == int):
                    query += "," + str(values[i])
                else:
                    query += ",'" + str(values[i]) + "'"
            
        query += ")\n"
        return query
        
