
import pandas as pd
from regex import P
import json



df = pd.DataFrame({"beneficiaries":
    [
        {"db_name": "beneficiary_db", "data_mart_table": "ration_appointments_validation",
            "psql_query": "select * from ration_appointments_validation  as sd   where $incremental_window_condition"
        },
        {"db_name": "beneficiary_db", "data_mart_table": "beneficiary_address",
            "psql_query": "select sd.*,  b.project_id from beneficiary_address sd  JOIN  beneficiaries b on sd.beneficiary_id=b.id and $incremental_window_condition"
        },
        {"db_name": "beneficiary_db", "data_mart_table": "beneficiary_ration_details",
            "psql_query": "select sd.*,  b.project_id from beneficiary_ration_details sd  JOIN  beneficiaries b on sd.beneficiary_id=b.id and $incremental_window_condition"
        },
        {"db_name": "beneficiary_db",
            "data_mart_table": "ration_appointments",
            "psql_query": "select * from ration_appointments as sd where $incremental_window_condition"}
            ]
        })

for column_name, item in df.iteritems():
    
    # print(item[0]['db_name'], item[1]['data_mart_table'], item[2]['psql_query'])

    for i in range(len(item)):
        print(item[0]['db_name'], item[1]['data_mart_table'], item[2]['psql_query'])
        
       
