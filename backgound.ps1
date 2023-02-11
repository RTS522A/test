$elapsedTime = [system.diagnostics.stopwatch]::StartNew()

$job = Start-Job {
  $i = 0
  while ($true) {
    echo DOING JOB $i
    Start-Sleep -s 10
    $i++
    if ($i -ge 3) {break}
	
	
 }
}

while ($true)
{
  # Check for available job output, if any.
  if ($result = $job | Receive-Job ) {
      $duration = $elapsedTime.Elapsed.ToString("hh\:mm\:ss")
      Write-Host $duration : $result
      # .... send email logic here
      # for success result
  }

  if('Completed' -eq $job.JobStateInfo.State) {
      Write-Host $duration : "JOB DONE"
      break
  }

  # if this is running for more than
  # 60 minutes break the loop
  if($elapsedTime.Elapsed.Minutes -ge 1)
  {
      $elapsedTime.Stop()
      $duration = $elapsedTime.Elapsed.ToString("hh\:mm\:ss")
      
      # .... send email logic here
      # for script running longer 
      # than 60 minutes
      
      # Forcefully remove the background job.
      $job | Remove-Job -Force
      Write-Host "break jo": $duration
      break
  }
  Start-Sleep -Milliseconds 500
}
