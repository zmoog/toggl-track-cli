import pytest
from click.testing import CliRunner

from toggl_track.cli import cli


env = {
    "TOGGL_API_TOKEN": "1234567890abcdef1234567890abcdef", # fake token for testing
}


@pytest.mark.vcr
@pytest.mark.block_network
def test_group_by_tags(save_to_tmp):
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(
            cli,
            ["entries", "group-by", "--field", "tags", "--start-date", "2024-01-26", "--end-date", "2024-01-27"],
            env=env,
        )
        save_to_tmp(result.output, name="test_group_by_tags")
        assert result.exit_code == 0
        assert (
            result.output
            == """            Time Entries            
                                    
  tags                    Duration  
 ────────────────────────────────── 
  type:goal               4:34      
                          2:16      
  type:support/sdh        1:46      
  type:sync               1:00      
  type:support/question   0:34      
 ────────────────────────────────── 
  Total                   10:11     
                                    

"""
        )
        

@pytest.mark.vcr
@pytest.mark.block_network
def test_group_by_tags_and_filter(save_to_tmp):
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(
            cli,
            [
                "entries",
                "--project-id", "178435728",
                "group-by",
                "--field", "tags",
                "--start-date", "2024-01-26",
                "--end-date", "2024-01-27"
             ],
            env=env,
        )
        save_to_tmp(result.output, name="test_group_by_tags_and_filter")
        assert result.exit_code == 0
        assert (
            result.output
            == """            Time Entries            
                                    
  tags                    Duration  
 ────────────────────────────────── 
  type:goal               4:34      
  type:support/sdh        1:46      
  type:sync               1:00      
  type:support/question   0:34      
 ────────────────────────────────── 
  Total                   7:55      
                                    

"""
        )


@pytest.mark.vcr
@pytest.mark.block_network
def test_group_by_initiative(save_to_tmp):
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(
            cli,
            ["entries",
             "--project-id", "178435728",
             "group-by",
             "--field", "initiative",
             "--start-date", "2024-01-26",
             "--end-date", "2024-01-27"
             ],
            env=env,
        )
        save_to_tmp(result.output, name="test_group_by_initiative")
        assert result.exit_code == 0
        assert (
            result.output
            == """                                  Time Entries                                  
                                                                                
  initiative                                                          Duration  
 ────────────────────────────────────────────────────────────────────────────── 
  Migrate to ecs@mappings template shipped with Elasticsearch         4:34      
  S3 SQS ingest delay in performance with Elastic Agent #4264         1:46      
  sync                                                                1:00      
  IHAC using AWS WAF integration and expresses concern about the      0:34      
  throughput                                                                    
 ────────────────────────────────────────────────────────────────────────────── 
  Total                                                               7:55      
                                                                                

"""
        )


@pytest.mark.vcr
@pytest.mark.block_network
def test_group_by_initiative_as_ndjson(save_to_tmp):
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(
            cli,
            [
                "--format", "ndjson",
                "entries",
                "--project-id", "178435728",
                "group-by",
                "--field", "initiative",
                "--start-date", "2024-01-27",
                "--end-date", "2024-01-29"
            ],
            env=env,
        )
        save_to_tmp(result.output, name="test_group_by_initiative_as_ndjson")
        assert result.exit_code == 0
        assert (
            result.output
            == """{"field": "initiative", "name": "synthetics kt session #2", "duration": 17928}
"""
        )


@pytest.mark.vcr
@pytest.mark.block_network
def test_group_by_initiative_as_json_with_root_element(save_to_tmp):
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(
            cli,
            [
                "--format", "json",
                "--json-root", "entries-by-tags",
                "entries",
                "--project-id", "178435728",
                "group-by",
                "--field", "tags",
                "--start-date", "2024-01-26",
                "--end-date", "2024-01-27",
            ],
            env=env,
        )
        save_to_tmp(result.output, name="test_group_by_initiative_as_json_with_root_element")
        assert result.exit_code == 0
        assert (
            result.output
            == """{"entries-by-tags": [["type:goal", 16482], ["type:support/sdh", 6373], ["type:sync", 3617], ["type:support/question", 2044]]}
"""
        )
