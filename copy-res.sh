if [ ! $# -eq 1 ]; then
    echo "usage: $0 download-dir"
    exit 1
fi

rm -rf tmp
mkdir tmp
find  $1 -name "*res" -print | xargs -I {} cp -rf {} tmp
