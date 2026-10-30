# Source this to get the pilot's local toolchain on PATH (dev machine only; the
# devcontainer is the distributable). Nothing here is required by the kit.
export JAVA_HOME="/opt/homebrew/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home"
export DOTNET_ROOT="/Users/hpatil/ADLC/.toolchain/dotnet"
export PATH="/opt/homebrew/opt/openjdk@21/bin:$DOTNET_ROOT:$PATH"
export DOTNET_CLI_TELEMETRY_OPTOUT=1
export DOTNET_NOLOGO=1
export GRAPHIFY_BACKEND=none
export GRAPHIFY_NO_TIPS=1
