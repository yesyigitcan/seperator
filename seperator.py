# -*- coding: utf-8 -*-
"""
Info:
    Linkedin: https://www.linkedin.com/in/yesyigitcan/
"""

import xml.etree.ElementTree as ET

class XML_Query_Helper:
    
    def __init__(self,path,depth_key = 0,key_word = "NO_REQUIRED_KEY_WORD"):
        if(type(path) != str):
            self.root = ET.ElementTree(path).getroot()
        else:
            self.root = ET.parse(path).getroot()
            
        if depth_key != 0:
            if key_word == "NO_REQUIRED_KEY_WORD":
                pass
            else:
                for i in self.root:
                    #body
                    if(key_word in i.tag):
                        for j in i:
                            if(depth_key == 3):
                                for k in j:
                                    for l in k:
                                        self.root = l
                                        return
                            if(depth_key == 2):
                                for k in j:
                                    self.root = k
                                    return
                            else:
                                self.root = j
                                return
                            
     
            
    def columns(self):
        temp = []
        for i in self.root:
            temp.append(i.tag)
        return temp
        
    def XML2List(self,column_name,special_key = "NO_REQUIRED_SPECIAL_KEY",extra_label = [],extra_values = [],target_columns = "NO_REQUIRED_TARGET_COLUMNS",leaf_node = False,leaf_num = 0,special_col = [],all_upper = False):
        
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
                if(all_upper):
                    j.tag = j.tag.upper()
                if(special_key == "NO_REQUIRED_SPECIAL_KEY"):
                    if(target_columns == "NO_REQUIRED_TARGET_COLUMNS"):
                        
                        if(leaf_node):
                            
                            if(j.text == None):
                                
                                leaf_counter = 1
                                for leaf in j:
                                    
                                    if(leaf_counter > leaf_num and j.tag not in special_col):
                                        break
                                    self.label_set.append(j.tag + "_" + str(leaf_counter))
                                    if(j.text != None):
                                        self.values_set.append(leaf.text.replace("'",""))
                                    else:
                                        self.values_set.append(leaf.text)
                                    leaf_counter += 1
                            else:
                                self.label_set.append(j.tag)
                                if(j.text != None):
                                    self.values_set.append(j.text.replace("'",""))
                                else:
                                    self.values_set.append(j.text)
                        else:
                            self.label_set.append(j.tag)
                            if(j.text != None):
                                self.values_set.append(j.text.replace("'",""))
                            else:
                                self.values_set.append(j.text)
                    else:
                        
                        if(leaf_node):
                            if(j.text == None):
                                leaf_counter = 1
                                for leaf in j:
                                    if(leaf_counter > leaf_num and j.tag not in special_col):
                                        break
                                    tag_name = leaf.tag + "_" + str(leaf_counter)
                                    if(tag_name in target_columns):
                                        self.label_set.append(tag_name)
                                        self.values_set.append(leaf.text)
                                        leaf_counter += 1
                            else:
                                if(j.tag in target_columns):
                                    self.label_set.append(j.tag)
                                    if(j.text != None):
                                        self.values_set.append(j.text.replace("'",""))
                                    else:
                                        self.values_set.append(j.text)
                        else:
                           
                            if(j.tag in target_columns):
                                
                                self.label_set.append(j.tag)
                                if(j.text != None):
                                    self.values_set.append(j.text.replace("'",""))
                                else:
                                    self.values_set.append(j.text)
                        
                elif(j.tag[:2] in special_key or j.tag[:1].upper() in special_key or j.tag[:1] in special_key):
                    
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
                                if(j.text != None):
                                    self.values_set.append(j.text.replace("'",""))
                                else:
                                    self.values_set.append(j.text)
                        else:
                            self.label_set.append(j.tag)
                            if(j.text != None):
                                self.values_set.append(j.text.replace("'",""))
                            else:
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
                                        if(j.text != None):
                                            self.values_set.append(leaf.text.replace("'",""))
                                        else:
                                            self.values_set.append(leaf.text)
                                        leaf_counter += 1
                                        
                                    elif(tag_name.upper() in target_columns):
                                        
                                        tag_name = tag_name.upper()
                                        self.label_set.append(tag_name)
                                        if(j.text != None):
                                            self.values_set.append(leaf.text.replace("'",""))
                                        else:
                                            self.values_set.append(leaf.text)
                                        leaf_counter += 1
                                        
                            else:
                                
                                if(j.tag in target_columns):
                                    self.label_set.append(j.tag)
                                    if(j.text != None):
                                        self.values_set.append(j.text.replace("'",""))
                                    else:
                                        self.values_set.append(j.text)
                        else:
                            
                            if(j.tag in target_columns or str(j.tag).upper() in target_columns):
                                
                                self.label_set.append(j.tag)
                                if(j.text != None):
                                    self.values_set.append(j.text.replace("'",""))
                                else:
                                    self.values_set.append(j.text)
                                
                    
        
        for i in range(len_label):
            if(extra_label[i] in target_columns):
                self.label_set.append(extra_label[i])
                self.values_set.append(extra_values[i])
        return self.label_set,self.values_set
        
        
    def XML_Query(self,db_id,label,values,target_table,db_id_name = "ID",is_there_id = 1):
        list_len = len(label)
        if(list_len < 1):
            print("**Empty List**")
            return
        
        query = "INSERT INTO " + target_table + "\n("
        
        if(is_there_id):
            query += db_id_name + ","
            
        for i in range(0,list_len):
            query += str(label[i]) + ","
        query = query[:-1]
        query += ") \nVALUES \n("
        
        if(is_there_id):
            query += str(db_id) + ","
            
        for i in range(0,list_len):
            if(values[i] == "SYSDATE"):
              query += values[i] + ","  
            elif(values[i] == None):
                query += "NULL,"
            elif(type(values[i]) == str and values[i][:7] == "TO_DATE"):
                query += values[i] + ","  
            else:
                if(type(values[i]) != str):
                    query += str(values[i]) + ","
                else:
                    query += "'" + str(values[i]) + "',"
        query = query[:-1]
        query += ")\n"
        return query
        
