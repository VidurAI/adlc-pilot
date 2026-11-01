# Source this to get the pilot's local toolchain on PATH (dev machine). Nothing here
# is required by the kit. Relocatable: ADLC_ROOT is exported by the Makefile; when
# sourced by hand it falls back to the git top-level of the current directory.
export ADLC_ROOT="${ADLC_ROOT:-$(git rev-parse --show-toplevel 2>/dev/null || pwd)}"
if [ -d /opt/homebrew/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home ]; then
  export JAVA_HOME="/opt/homebrew/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home"
else
  export JAVA_HOME="$(/usr/libexec/java_home -v 21 2>/dev/null)"
fi
export DOTNET_ROOT="$ADLC_ROOT/.toolchain/dotnet"
export PATH="$JAVA_HOME/bin:$DOTNET_ROOT:$PATH"
export DOTNET_CLI_TELEMETRY_OPTOUT=1
export DOTNET_NOLOGO=1
export GRAPHIFY_BACKEND=none
export GRAPHIFY_NO_TIPS=1
