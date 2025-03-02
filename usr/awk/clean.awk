BEGIN {
    FS = " "
    LFS = "\n"
    nfs = "|"
    current_game = 0
}
/Init/ { current_game++ }
/kill/ {
    sub(/^[ 0-9:]+ Kill: [0-9: ]+/, "", $0)
    sub(/ killed /, nfs, $0)
    sub(/ by /, nfs, $0)
    print $0 nfs current_game
}