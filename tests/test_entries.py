import click.testing
import pytest
from click.testing import CliRunner

from toggl_track.cli import cli


def save_result(result: click.testing.Result):
    """Saves the result object to the filesystem for inspection."""
    with open("/tmp/output.txt", "w") as f:
        f.write(result.output)


@pytest.mark.vcr
@pytest.mark.block_network
def test_entries():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ["entries", "list", "--start-date", "2023-01-26", "--end-date", "2023-01-27"])
        assert result.exit_code == 0
        assert (
            result.output
            == """                                  Time Entries                                  
                                                                                
  At           Description     Start      Stop       Duration     Tags          
 ────────────────────────────────────────────────────────────────────────────── 
  2023-01-26   Community:      10:25 PM   10:54 PM   28 minutes   type:support  
               Allow parsing                                                    
               of IPv6                                                          
               addresses in                                                     
               ingest                                                           
               pipeline                                                         
  2023-01-26   Community:      09:45 PM   10:25 PM   40 minutes   type:support  
               Fix parsing                                                      
               error client                                                     
               port is blank                                                    
               and adjust                                                       
               for timeStamp                                                    
  2023-01-26   Community:      09:45 PM   09:45 PM   a second                   
               Fix parsing                                                      
               error client                                                     
               port is blank                                                    
               and adjust                                                       
               for timeStamp                                                    
  2023-01-26   Community:      09:45 PM   09:45 PM   2 seconds                  
               Fix parsing                                                      
               error client                                                     
               port is blank                                                    
               and adjust                                                       
               for timeStamp                                                    
  2023-01-26   Community:      08:39 PM   09:45 PM   an hour      type:support  
               Azure Signin                                                     
               Module                                                           
               authenticati…                                                    
               Issue                                                            
  2023-01-26   🍲 Dinner       06:59 PM   08:39 PM   an hour                    
  2023-01-26   Community:      05:13 PM   06:58 PM   an hour      type:support  
               Azure Signin                                                     
               Module                                                           
               authenticati…                                                    
               Issue                                                            
  2023-01-26   🚌 Shuttling    04:48 PM   05:13 PM   25 minutes                 
               kids between                                                     
               home and                                                         
               whatever                                                         
  2023-01-26   Community:      03:55 PM   04:48 PM   52 minutes   type:support  
               Azure Signin                                                     
               Module                                                           
               authenticati…                                                    
               Issue                                                            
  2023-01-26   Drop header     03:47 PM   03:55 PM   8 minutes    type:support  
               log line in                                                      
               CloudFront                                                       
               events                                                           
  2023-01-26   ElasticOnAzu…   03:03 PM   03:47 PM   43 minutes   type:support  
               questions                                                        
               from Deniz                                                       
               Coskun                                                           
  2023-01-26   Cloud           01:01 PM   02:30 PM   an hour      type:meeting  
               Monitoring -                                                     
               Weekly                                                           
  2023-01-26   🍜 Lunch        12:35 PM   01:00 PM   24 minutes                 
  2023-01-26   sync            12:06 PM   12:35 PM   28 minutes   type:sync     
  2023-01-26   gather town     11:31 AM   12:06 PM   35 minutes   type:meeting  
  2023-01-26   azure2:         10:55 AM   11:31 AM   35 minutes   type:goal     
               follow up                                                        
  2023-01-26   sync            08:24 AM   10:55 AM   2 hours      type:sync     
  2023-01-26   toggl-track:    07:28 AM   08:08 AM   39 minutes                 
               list time                                                        
               entries                                                          
  2023-01-26   toggl-track:    06:48 AM   07:17 AM   28 minutes                 
               list time                                                        
               entries                                                          
  2023-01-26   🥐 Breakfast    06:06 AM   06:48 AM   42 minutes                 
  2023-01-26   toggl-track:    05:11 AM   06:06 AM   54 minutes                 
               list time                                                        
               entries                                                          
                                                                                

"""
        )
        
