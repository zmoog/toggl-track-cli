import pytest
from click.testing import CliRunner

from toggl_track.cli import cli


env = {
    "TOGGL_API_TOKEN": "1234567890abcdef1234567890abcdef", # fake token for testing
}


@pytest.mark.vcr
@pytest.mark.block_network
def test_list(save_to_tmp):
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(
            cli,
            ["entries", "list", "--start-date", "2023-01-26", "--end-date", "2023-01-27"],
            env=env,
        )
        save_to_tmp(result.output, name="test_list")
        assert result.exit_code == 0
        assert (
            result.output
            == """                                  Time Entries                                  
                                                                                
  At           Description       Start      Stop       Duration   Tags          
 ────────────────────────────────────────────────────────────────────────────── 
  2023-01-26   Community:        10:25 PM   10:54 PM   0:28       type:support  
               Allow parsing                                                    
               of IPv6                                                          
               addresses in                                                     
               ingest pipeline                                                  
  2023-01-26   Community: Fix    09:45 PM   10:25 PM   0:40       type:support  
               parsing error                                                    
               client port is                                                   
               blank and                                                        
               adjust for                                                       
               timeStamp                                                        
  2023-02-03   Community: Fix    09:45 PM   09:45 PM   0:00       type:support  
               parsing error                                                    
               client port is                                                   
               blank and                                                        
               adjust for                                                       
               timeStamp                                                        
  2023-02-03   Community: Fix    09:45 PM   09:45 PM   0:00       type:support  
               parsing error                                                    
               client port is                                                   
               blank and                                                        
               adjust for                                                       
               timeStamp                                                        
  2023-01-26   Community:        08:39 PM   09:45 PM   1:05       type:support  
               Azure Signin                                                     
               Module                                                           
               authentication…                                                  
               Issue                                                            
  2023-01-26   🍲 Dinner         06:59 PM   08:39 PM   1:39                     
  2023-01-26   Community:        05:13 PM   06:58 PM   1:44       type:support  
               Azure Signin                                                     
               Module                                                           
               authentication…                                                  
               Issue                                                            
  2023-01-26   🚌 Shuttling      04:48 PM   05:13 PM   0:25                     
               kids between                                                     
               home and                                                         
               whatever                                                         
  2023-01-26   Community:        03:55 PM   04:48 PM   0:52       type:support  
               Azure Signin                                                     
               Module                                                           
               authentication…                                                  
               Issue                                                            
  2023-01-26   Drop header log   03:47 PM   03:55 PM   0:08       type:support  
               line in                                                          
               CloudFront                                                       
               events                                                           
  2023-01-26   ElasticOnAzure:   03:03 PM   03:47 PM   0:43       type:support  
               questions from                                                   
               Deniz Coskun                                                     
  2023-01-26   Cloud             01:01 PM   02:30 PM   1:29       type:meeting  
               Monitoring -                                                     
               Weekly                                                           
  2023-01-26   🍜 Lunch          12:35 PM   01:00 PM   0:24                     
  2023-01-26   sync              12:06 PM   12:35 PM   0:28       type:sync     
  2023-01-26   gather town       11:31 AM   12:06 PM   0:35       type:meeting  
  2023-01-26   azure2: follow    10:55 AM   11:31 AM   0:35       type:goal     
               up                                                               
  2023-01-26   sync              08:24 AM   10:55 AM   2:31       type:sync     
  2023-01-26   toggl-track:      07:28 AM   08:08 AM   0:39                     
               list time                                                        
               entries                                                          
  2023-01-26   toggl-track:      06:48 AM   07:17 AM   0:28                     
               list time                                                        
               entries                                                          
  2023-01-26   🥐 Breakfast      06:06 AM   06:48 AM   0:42                     
  2023-01-26   toggl-track:      05:11 AM   06:06 AM   0:54                     
               list time                                                        
               entries                                                          
 ────────────────────────────────────────────────────────────────────────────── 
                                            Total      16:39                    
                                                                                

"""
        )
        
@pytest.mark.vcr
@pytest.mark.block_network
def test_list_with_a_running_time_entry(save_to_tmp):
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(
            cli,
            ["entries", "list", "--start-date", "2023-02-03", "--end-date", "2023-02-05"],
            env=env,
        )
        save_to_tmp(result.output, name="test_list_with_a_running_time_entry")
        assert result.exit_code == 0
        assert (
            result.output
            == """                                  Time Entries                                  
                                                                                
  At           Description       Start      Stop       Duration   Tags          
 ────────────────────────────────────────────────────────────────────────────── 
  2023-02-04   toggl-track:      05:37 AM              -                        
               insights                                                         
  2023-02-03   Community:        08:18 PM   10:09 PM   1:51       type:support  
               Allow parsing                                                    
               of IPv6                                                          
               addresses in                                                     
               ingest pipeline                                                  
  2023-02-03   🍲 Dinner         07:19 PM   08:18 PM   0:58                     
  2023-02-03   sync              06:19 PM   06:55 PM   0:35       type:sync     
  2023-02-03   🚌 Shuttling      04:46 PM   06:19 PM   1:33                     
               kids between                                                     
               home and                                                         
               whatever                                                         
  2023-02-03   App Service       04:40 PM   04:46 PM   0:06       type:goal     
               logs                                                             
               integration:                                                     
               troubleshootign                                                  
               lucianpy issues                                                  
  2023-02-03   Community:        04:21 PM   04:40 PM   0:18       type:support  
               Allow parsing                                                    
               of IPv6                                                          
               addresses in                                                     
               ingest pipeline                                                  
  2023-02-03   Community: Fix    03:15 PM   04:21 PM   1:05       type:support  
               parsing error                                                    
               client port is                                                   
               blank and                                                        
               adjust for                                                       
               timeStamp                                                        
  2023-02-03   Community:        02:37 PM   03:15 PM   0:38       type:support  
               Azure Signin                                                     
               Module                                                           
               authentication…                                                  
               Issue                                                            
  2023-02-03   Rosanna           11:06 AM   02:37 PM   3:31                     
  2023-02-03   Community:        09:25 AM   11:06 AM   1:41       type:support  
               Azure Signin                                                     
               Module                                                           
               authentication…                                                  
               Issue                                                            
  2023-02-03   sync              08:37 AM   09:25 AM   0:48       type:sync     
  2023-02-03   toggl-track:      07:06 AM   08:07 AM   1:01                     
               insights                                                         
  2023-02-03   🥐 Breakfast      06:08 AM   07:06 AM   0:57                     
  2023-02-03   toggl-track:      05:51 AM   06:08 AM   0:16                     
               insights                                                         
 ────────────────────────────────────────────────────────────────────────────── 
                                            Total      15:24                    
                                                                                

"""
        )
        

@pytest.mark.vcr
@pytest.mark.block_network
def test_list_as_ndjson(save_to_tmp):
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(
            cli,
            ["--format", "ndjson", "entries", "--project-id", "178435728", "list", "--start-date", "2023-01-26", "--end-date", "2023-01-27"],
            env=env,
        )
        save_to_tmp(result.output, name="test_list_as_ndjson")
        assert result.exit_code == 0
        assert (
            result.output
            == """{"id": 2819125097, "workspace_id": 1815018, "user_id": 2621333, "project_id": 178435728, "task_id": null, "billable": false, "at": "2023-01-26T22:54:33+00:00", "description": "Community: Allow parsing of IPv6 addresses in ingest pipeline", "start": "2023-01-26T22:25:35+00:00", "stop": "2023-01-26T22:54:33+00:00", "duration": 1738, "tags": ["type:support"]}
{"id": 2819082262, "workspace_id": 1815018, "user_id": 2621333, "project_id": 178435728, "task_id": null, "billable": false, "at": "2023-01-26T22:25:35+00:00", "description": "Community: Fix parsing error client port is blank and adjust for timeStamp", "start": "2023-01-26T21:45:11+00:00", "stop": "2023-01-26T22:25:35+00:00", "duration": 2424, "tags": ["type:support"]}
{"id": 2819082247, "workspace_id": 1815018, "user_id": 2621333, "project_id": 178435728, "task_id": null, "billable": false, "at": "2023-02-03T07:46:39+00:00", "description": "Community: Fix parsing error client port is blank and adjust for timeStamp", "start": "2023-01-26T21:45:10+00:00", "stop": "2023-01-26T21:45:11+00:00", "duration": 1, "tags": ["type:support"]}
{"id": 2819082217, "workspace_id": 1815018, "user_id": 2621333, "project_id": 178435728, "task_id": null, "billable": false, "at": "2023-02-03T07:46:39+00:00", "description": "Community: Fix parsing error client port is blank and adjust for timeStamp", "start": "2023-01-26T21:45:08+00:00", "stop": "2023-01-26T21:45:10+00:00", "duration": 2, "tags": ["type:support"]}
{"id": 2819003151, "workspace_id": 1815018, "user_id": 2621333, "project_id": 178435728, "task_id": null, "billable": false, "at": "2023-01-26T21:45:09+00:00", "description": "Community: Azure Signin Module authentication_processing_details Issue", "start": "2023-01-26T20:39:47+00:00", "stop": "2023-01-26T21:45:09+00:00", "duration": 3922, "tags": ["type:support"]}
{"id": 2818714203, "workspace_id": 1815018, "user_id": 2621333, "project_id": 178435728, "task_id": null, "billable": false, "at": "2023-01-26T18:58:23+00:00", "description": "Community: Azure Signin Module authentication_processing_details Issue", "start": "2023-01-26T17:13:25+00:00", "stop": "2023-01-26T18:58:23+00:00", "duration": 6298, "tags": ["type:support"]}
{"id": 2818566057, "workspace_id": 1815018, "user_id": 2621333, "project_id": 178435728, "task_id": null, "billable": false, "at": "2023-01-26T16:48:22+00:00", "description": "Community: Azure Signin Module authentication_processing_details Issue", "start": "2023-01-26T15:55:39+00:00", "stop": "2023-01-26T16:48:22+00:00", "duration": 3163, "tags": ["type:support"]}
{"id": 2818549545, "workspace_id": 1815018, "user_id": 2621333, "project_id": 178435728, "task_id": null, "billable": false, "at": "2023-01-26T15:55:39+00:00", "description": "Drop header log line in CloudFront events", "start": "2023-01-26T15:47:14+00:00", "stop": "2023-01-26T15:55:39+00:00", "duration": 505, "tags": ["type:support"]}
{"id": 2818461010, "workspace_id": 1815018, "user_id": 2621333, "project_id": 178435728, "task_id": null, "billable": false, "at": "2023-01-26T15:47:14+00:00", "description": "ElasticOnAzure: questions from Deniz Coskun", "start": "2023-01-26T15:03:41+00:00", "stop": "2023-01-26T15:47:14+00:00", "duration": 2613, "tags": ["type:support"]}
{"id": 2818271775, "workspace_id": 1815018, "user_id": 2621333, "project_id": 178435728, "task_id": null, "billable": false, "at": "2023-01-26T14:30:36+00:00", "description": "Cloud Monitoring - Weekly", "start": "2023-01-26T13:01:35+00:00", "stop": "2023-01-26T14:30:36+00:00", "duration": 5341, "tags": ["type:meeting"]}
{"id": 2818128524, "workspace_id": 1815018, "user_id": 2621333, "project_id": 178435728, "task_id": null, "billable": false, "at": "2023-01-26T12:35:31+00:00", "description": "sync", "start": "2023-01-26T12:06:40+00:00", "stop": "2023-01-26T12:35:31+00:00", "duration": 1731, "tags": ["type:sync"]}
{"id": 2818075670, "workspace_id": 1815018, "user_id": 2621333, "project_id": 178435728, "task_id": null, "billable": false, "at": "2023-01-26T12:06:40+00:00", "description": "gather town", "start": "2023-01-26T11:31:30+00:00", "stop": "2023-01-26T12:06:40+00:00", "duration": 2110, "tags": ["type:meeting"]}
{"id": 2818022697, "workspace_id": 1815018, "user_id": 2621333, "project_id": 178435728, "task_id": null, "billable": false, "at": "2023-01-26T11:31:31+00:00", "description": "azure2: follow up", "start": "2023-01-26T10:55:58+00:00", "stop": "2023-01-26T11:31:31+00:00", "duration": 2133, "tags": ["type:goal"]}
{"id": 2817783218, "workspace_id": 1815018, "user_id": 2621333, "project_id": 178435728, "task_id": null, "billable": false, "at": "2023-01-26T10:55:58+00:00", "description": "sync", "start": "2023-01-26T08:24:19+00:00", "stop": "2023-01-26T10:55:58+00:00", "duration": 9099, "tags": ["type:sync"]}
"""
        )
        