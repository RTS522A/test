# Example usage:
#
#   Import-Module .\Split-File.ps1
#
#   Split-File -InputFile "path/to/big-file.zip" -OutputDirectory "path/to/split/output/files" -Verbose
#   Unsplit-File -InputDirectory "path/to/split/output/files" -OutputDirectory "path/to" -OutputFile big-file.zip
 
function Split-File
{
    <#-- Another stackoverflow production
    https://stackoverflow.com/questions/4533570/in-powershell-how-do-i-split-a-large-binary-file
    --#>
 
    [CmdletBinding()]
    Param (
        [Parameter(Mandatory = $true, ValueFromPipeLine = $true, ValueFromPipelineByPropertyName = $true)]
        [String]
        $InputFile,
 
        [Parameter(Mandatory = $true)]
        [String]
        $OutputDirectory,
 
        [Parameter(Mandatory = $false)]
        [String]
        $OutputFilePrefix = "chunk",
 
        [Parameter(Mandatory = $false)]
        [Int32]
        $ChunkSize = 1073741824,
        
        [Parameter(Mandatory = $false)]
        [Int32]
        $ChunkSkip = 0,
        
        [Parameter(Mandatory = $false)]
        [Int32]
        $ChunkTotal = 0
    )
 
    Begin
    {
        Write-Output "Beginning file split..."
    }
 
    Process
    {
        if (-not (Test-Path -Path $OutputDirectory))
        {
            New-Item -ItemType Directory $OutputDirectory | Out-Null
            Write-Verbose "Created OutputDirectory: $OutputDirectory"
        }
 
        $FileStream = [System.IO.File]::OpenRead($InputFile)
        $ByteChunks = New-Object byte[] $ChunkSize
        $ChunkNumber = 1

 
        While ($BytesRead = $FileStream.Read($ByteChunks, 0, $ChunkSize))
        {
          if ($ChunkNumber -gt $ChunkSkip) {
            $OutputFile = Join-Path -Path $OutputDirectory -ChildPath "$OutputFilePrefix$ChunkNumber"
            $OutputStream = [System.IO.File]::OpenWrite($OutputFile)
            $OutputStream.Write($ByteChunks, 0, $BytesRead)
 
            $OutputStream.Close()
 
            Write-Verbose "Wrote File: $OutputFile"
          }   
 
          $ChunkNumber += 1
          if ($ChunkTotal gt 0) {
           if ($ChunkNumber -gt $ChunkSkip+$ChunkTotal) {
            break
           }
          }  
        }
    }
 
    End
    {
        Write-Output "Finished splitting file."
    }
}
 
function Unsplit-File
{
    [CmdletBinding()]
    Param (
        [Parameter(Mandatory = $true)]
        [String]
        $InputDirectory,
 
        [Parameter(Mandatory = $false)]
        [String]
        $InputFilePrefix = "chunk",
 
        [Parameter(Mandatory = $true)]
        [String]
        $OutputDirectory,
 
        [Parameter(Mandatory = $true)]
        [String]
        $OutputFile
    )
 
    Begin
    {
        Write-Output "Beginning file unsplit..."
    }
 
    Process
    {
        if (-not (Test-Path -Path $OutputDirectory))
        {
            New-Item -ItemType Directory $OutputDirectory | Out-Null
            Write-Verbose "Created OutputDirectory: $OutputDirectory"
        }
 
        $OutputPath = Join-Path -Path $OutputDirectory -ChildPath $OutputFile
        $OutputStream = [System.Io.File]::OpenWrite($OutputPath)
 
        $ChunkNumber = 1
        $InputFilename = Join-Path -Path $InputDirectory -ChildPath "$InputFilePrefix$ChunkNumber"
 
        while (Test-Path $InputFilename)
        {
            $FileBytes = [System.IO.File]::ReadAllBytes($InputFilename)
            $OutputStream.Write($FileBytes, 0, $FileBytes.Count)
 
            Write-Verbose "Unsplit File: $InputFilename"
 
            $ChunkNumber += 1
            $InputFilename = Join-Path -Path $InputDirectory -ChildPath "$InputFilePrefix$ChunkNumber"
        }
 
        $OutputStream.close()
    }
 
    End
    {
        Write-Output "Finished unsplitting file."
    }
}
