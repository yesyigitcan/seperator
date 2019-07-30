# seperator
Description: Python script to parse an xml file which retrieved from a DB table and move its values to selected table in a datawarehouse

Class Name: XML_Query_Helper
Functions:
  1) __init__(path): Create an Elemantary Tree Root by any path or xml script directly
  2) columns(): Returns columns of given xml
  3) XML2List(...): Creates two lists (Label Set, Values Set). One stores labels of attributes, other one stores values.
     Parameters:
      1) Column Name: Only selected column of xml is joint into lists.
      2) Special_key: Only ones satisfy special key (first 2 letters) is joint. Default: "NO_REQUIRED_SPECIAL_KEY"
      3) Extra Label: Any extra information can be joint. You need to declare them as lists (Extra Label, Extra Values).
      4) Extra Values
      5) Target_columns: Only ones which exist in target data warehouse table (XML may have more columns than DWH). 
         Default: "NO_REQUIRED_TARGET_COLUMNS"
      6) Leaf_node: If XML has string series, you need to set leaf_node True. Default: False
      7) Leaf_num: How many of these string series will be joint. Default: 0
      8) Special_col: For any column that you do not want it to be depend on leaf_num.
   4) XML_Query(id,...): It basically converts given lists to INSERT SQL command.
     Parameters:
      1) Db_id: Source DB's ID.
      2) Label
      3) Values
      4) Target_table: Target table of DWH.
        
