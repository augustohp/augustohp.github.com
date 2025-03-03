BEGIN {
    FS = "|"   
}
{
    # Sets a player as a key in the players array
    players[$1] = $1
    players[$2] = $2
}
END {
    # Removes <world> from players
    for (name in players) {
        if (name == "<world>")
            continue
        print name
    }
}