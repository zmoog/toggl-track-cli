import pytest
from click.testing import CliRunner

from toggl_track.cli import cli


env = {
    "TOGGL_API_TOKEN": "1234567890abcdef1234567890abcdef", # fake token for testing
}


@pytest.mark.vcr
@pytest.mark.block_network
def test_list_filter_by_description(save_to_tmp):
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(
            cli,
            ["entries", "--description", "ecs@mappings", "list", "--start-date", "2024-01-26", "--end-date", "2024-01-27"],
            env=env,
        )
        save_to_tmp(result.output, name="test_list_filter_by_description")
        assert result.exit_code == 0
        assert (
            result.output
            == """                                  Time Entries                                  
                                                                                
  At           Description          Start      Stop       Duration   Tags       
 ────────────────────────────────────────────────────────────────────────────── 
  2024-01-26   Migrate to           01:50 PM   02:48 PM   0:58       type:goal  
               ecs@mappings                                                     
               template shipped                                                 
               with Elasticsearch                                               
  2024-01-26   Migrate to           08:44 AM   12:20 PM   3:36       type:goal  
               ecs@mappings                                                     
               template shipped                                                 
               with Elasticsearch                                               
 ────────────────────────────────────────────────────────────────────────────── 
                                               Total      4:34                  
                                                                                

"""
        )
        

@pytest.mark.vcr
@pytest.mark.block_network
def test_list(save_to_tmp):
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(
            cli,
            [
                "entries",
                "list",
                "--start-date", "2024-02-26",
                "--end-date", "2024-02-27"
            ],
            env=env,
        )
        save_to_tmp(result.output, name="test_list")
        assert result.exit_code == 0
        assert (
            result.output
            == """                              Time Entries                               
                                                                         
  At           Description        Start      Stop       Duration   Tags  
 ─────────────────────────────────────────────────────────────────────── 
  2024-02-26   Ristrutturazione   10:03 AM   12:07 PM   2:04             
 ─────────────────────────────────────────────────────────────────────── 
                                             Total      2:04             
                                                                         

"""
        )
        
@pytest.mark.vcr
@pytest.mark.block_network
def test_list_with_a_running_time_entry(save_to_tmp):
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(
            cli,
            [
                "entries",
                "list",
                "--start-date", "2024-02-03",
                "--end-date", "2024-02-05"
            ],
            env=env,
        )
        save_to_tmp(result.output, name="test_list_with_a_running_time_entry")
        assert result.exit_code == 0
        assert (
            result.output
            == """                                  Time Entries                                  
                                                                                
  At           Description      Start      Stop       Duration   Tags           
 ────────────────────────────────────────────────────────────────────────────── 
  2024-02-05   How to           11:00 PM   01:09 AM   2:09       type:support…  
               performance                                                      
               test the                                                         
               aws-s3 input                                                     
               in SQS mode                                                      
  2024-02-04   How to           09:42 PM   10:59 PM   1:17       type:support…  
               performance                                                      
               test the                                                         
               aws-s3 input                                                     
               in SQS mode                                                      
  2024-02-04   How to           05:29 PM   07:35 PM   2:06       type:support…  
               performance                                                      
               test the                                                         
               aws-s3 input                                                     
               in SQS mode                                                      
  2024-02-03   Learn            06:07 PM   07:50 PM   1:43                      
               Concurrent                                                       
               Programming                                                      
               with Go                                                          
 ────────────────────────────────────────────────────────────────────────────── 
                                           Total      7:16                      
                                                                                

"""
        )
        

@pytest.mark.vcr
@pytest.mark.block_network
def test_list_as_ndjson(save_to_tmp):
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(
            cli,
            [
                "--format", "ndjson",
                "entries",
                "--project-id", "178435728",
                "list",
                "--start-date", "2024-01-26",
                "--end-date", "2024-01-27"
            ],
            env=env,
        )
        save_to_tmp(result.output, name="test_list_as_ndjson")
        assert result.exit_code == 0
        assert (
            result.output
            == """{"id": 3297435983, "workspace_id": 1815018, "user_id": 2621333, "project_id": 178435728, "task_id": null, "billable": false, "at": "2024-01-28T08:39:01+00:00", "description": "IHAC using AWS WAF integration and expresses concern about the throughput", "start": "2024-01-26T17:26:31+00:00", "stop": "2024-01-26T18:00:35+00:00", "duration": 2044, "tags": ["type:support/question"]}
{"id": 3297169916, "workspace_id": 1815018, "user_id": 2621333, "project_id": 178435728, "task_id": null, "billable": false, "at": "2024-01-26T16:34:41+00:00", "description": "S3 SQS ingest delay in performance with Elastic Agent #4264", "start": "2024-01-26T14:48:28+00:00", "stop": "2024-01-26T16:34:41+00:00", "duration": 6373, "tags": ["type:support/sdh"]}
{"id": 3297063846, "workspace_id": 1815018, "user_id": 2621333, "project_id": 178435728, "task_id": null, "billable": false, "at": "2024-01-26T14:48:28+00:00", "description": "Migrate to ecs@mappings template shipped with Elasticsearch [step 3]", "start": "2024-01-26T13:50:21+00:00", "stop": "2024-01-26T14:48:28+00:00", "duration": 3487, "tags": ["type:goal"]}
{"id": 3297055770, "workspace_id": 1815018, "user_id": 2621333, "project_id": 178435728, "task_id": null, "billable": false, "at": "2024-01-26T13:50:21+00:00", "description": "sync", "start": "2024-01-26T13:45:19+00:00", "stop": "2024-01-26T13:50:21+00:00", "duration": 302, "tags": ["type:sync"]}
{"id": 3296620722, "workspace_id": 1815018, "user_id": 2621333, "project_id": 178435728, "task_id": null, "billable": false, "at": "2024-01-26T12:20:37+00:00", "description": "Migrate to ecs@mappings template shipped with Elasticsearch [step 3]", "start": "2024-01-26T08:44:02+00:00", "stop": "2024-01-26T12:20:37+00:00", "duration": 12995, "tags": ["type:goal"]}
{"id": 3296545927, "workspace_id": 1815018, "user_id": 2621333, "project_id": 178435728, "task_id": null, "billable": false, "at": "2024-01-26T08:44:02+00:00", "description": "sync", "start": "2024-01-26T07:48:47+00:00", "stop": "2024-01-26T08:44:02+00:00", "duration": 3315, "tags": ["type:sync"]}
"""
        )
        