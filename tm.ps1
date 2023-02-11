$Duration = 20

$TimeOut=New-TimeSpan -Seconds $Duration
$Sw=[Diagnostics.Stopwatch]::StartNew()
While ($Sw.Elapsed -lt $TimeOut)
{
    Try
    {
     timeout /t 10
     echo done
        
    }
    Catch [system.exception]
    {
        # Writing the exception in the console
        Write-Host $_.Exception
        Exit;
    }
} #EndOf While ($Sw.Elapsed -lt $TimeOut)
