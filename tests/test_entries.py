import click.testing
from click.testing import CliRunner
from toggl_track.cli import cli


def save_result(result: click.testing.Result):
    """Saves the result object to the filesystem for inspection."""
    with open("output.txt", "w") as f:
        f.write(result.output)


def test_entries():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ["entries", "list"])
        save_result(result)
        assert result.exit_code == 0
        assert (
            result.output
            == """                                  Time Entries                                  
                                                                                
  Date         Description       Start      Stop       Duration   Tags          
 ────────────────────────────────────────────────────────────────────────────── 
  2023-01-25   community:        11:04 PM   11:27 PM   0:22:59    type:support  
               https://github…                                                  
                                                                                

"""
        )
        
