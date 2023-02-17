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
            ["entries", "group-by", "--field", "tags", "--start-date", "2023-01-26", "--end-date", "2023-01-27"],
            env=env,
        )
        save_to_tmp(result.output, name="test_group_by_tags")
        assert result.exit_code == 0
        assert (
            result.output
            == """       Time Entries        
                           
  tags           Duration  
 ───────────────────────── 
  type:support   5:44      
                 5:14      
  type:sync      3:00      
  type:meeting   2:04      
  type:goal      0:35      
 ───────────────────────── 
  Total          16:39     
                           

"""
        )
        

@pytest.mark.vcr
@pytest.mark.block_network
def test_group_by_tags_and_filter(save_to_tmp):
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(
            cli,
            ["entries", "--project-id", "178435728", "group-by", "--field", "tags", "--start-date", "2023-01-26", "--end-date", "2023-01-27"],
            env=env,
        )
        save_to_tmp(result.output, name="test_group_by_tags_and_filter")
        assert result.exit_code == 0
        assert (
            result.output
            == """       Time Entries        
                           
  tags           Duration  
 ───────────────────────── 
  type:support   5:44      
  type:sync      3:00      
  type:meeting   2:04      
  type:goal      0:35      
 ───────────────────────── 
  Total          11:24     
                           

"""
        )


@pytest.mark.vcr
@pytest.mark.block_network
def test_group_by_initiative(save_to_tmp):
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(
            cli,
            ["entries", "--project-id", "178435728", "group-by", "--field", "initiative", "--start-date", "2023-01-26", "--end-date", "2023-01-27"],
            env=env,
        )
        save_to_tmp(result.output, name="test_group_by_initiative")
        assert result.exit_code == 0
        assert (
            result.output
            == """                      Time Entries                      
                                                        
  initiative                                  Duration  
 ────────────────────────────────────────────────────── 
  Community                                   4:52      
  sync                                        3:00      
  Cloud Monitoring - Weekly                   1:29      
  ElasticOnAzure                              0:43      
  azure2                                      0:35      
  gather town                                 0:35      
  Drop header log line in CloudFront events   0:08      
 ────────────────────────────────────────────────────── 
  Total                                       11:24     
                                                        

"""
        )


@pytest.mark.vcr
@pytest.mark.block_network
def test_group_by_initiative_as_ndjson(save_to_tmp):
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(
            cli,
            ["--format", "ndjson", "entries", "--project-id", "178435728", "group-by", "--field", "initiative", "--start-date", "2023-01-26", "--end-date", "2023-01-27"],
            env=env,
        )
        save_to_tmp(result.output, name="test_group_by_initiative_as_ndjson")
        assert result.exit_code == 0
        assert (
            result.output
            == """{"field": "initiative", "name": "Community", "duration": 17548}
{"field": "initiative", "name": "sync", "duration": 10830}
{"field": "initiative", "name": "Cloud Monitoring - Weekly", "duration": 5341}
{"field": "initiative", "name": "ElasticOnAzure", "duration": 2613}
{"field": "initiative", "name": "azure2", "duration": 2133}
{"field": "initiative", "name": "gather town", "duration": 2110}
{"field": "initiative", "name": "Drop header log line in CloudFront events", "duration": 505}
"""
        )


@pytest.mark.vcr
@pytest.mark.block_network
def test_group_by_initiative_as_json_with_root_element(save_to_tmp):
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(
            cli,
            ["--format", "json", "--json-root", "entries-by-tags", "entries", "--project-id", "178435728", "group-by", "--field", "tags", "--start-date", "2023-01-26", "--end-date", "2023-01-27"],
            env=env,
        )
        save_to_tmp(result.output, name="test_group_by_initiative_as_json_with_root_element")
        assert result.exit_code == 0
        assert (
            result.output
            == """{"entries-by-tags": [["type:support", 20666], ["type:sync", 10830], ["type:meeting", 7451], ["type:goal", 2133]]}
"""
        )
