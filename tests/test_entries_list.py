import click.testing
import pytest
from click.testing import CliRunner

from toggl_track.cli import cli


env = {
    "TOGGL_API_TOKEN": "1234567890abcdef1234567890abcdef", # fake token for testing
}


@pytest.mark.vcr
@pytest.mark.block_network
def test_list():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(
            cli,
            ["entries", "list", "--start-date", "2023-01-26", "--end-date", "2023-01-27"],
            env=env,
        )
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
  2023-01-26   Community: Fix    09:45 PM   09:45 PM   0:00                     
               parsing error                                                    
               client port is                                                   
               blank and                                                        
               adjust for                                                       
               timeStamp                                                        
  2023-01-26   Community: Fix    09:45 PM   09:45 PM   0:00                     
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
                                                                                

"""
        )
        
