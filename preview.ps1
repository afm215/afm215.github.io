param(
    [int]$Port = 4000,
    [switch]$LiveReload
)

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

# Ensure UTF-8 encoding for Ruby on Windows paths with accented characters (e.g. "thèse")
chcp 65001 | Out-Null
$env:RUBYOPT = "-EUTF-8:UTF-8"

# Keep all Bundler and Jekyll caches strictly inside the local folder
$env:BUNDLE_APP_CONFIG = ".bundle"
$env:BUNDLE_PATH = "vendor/bundle"
$env:BUNDLE_USER_HOME = ".bundle_cache"

if (-not (Test-Path "vendor/bundle")) {
    Write-Host "Installing Ruby gems locally into ./vendor/bundle ..." -ForegroundColor Cyan
    bundle install
}

$serveArgs = @(
    "exec", "jekyll", "serve",
    "--host", "127.0.0.1",
    "--port", "$Port",
    "--force_polling"
)

if ($LiveReload) {
    $serveArgs += "--livereload"
}

Write-Host "Starting local Jekyll preview server at http://127.0.0.1:$Port/ ..." -ForegroundColor Green
bundle @serveArgs
