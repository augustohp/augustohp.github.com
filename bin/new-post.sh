#!/usr/bin/env bash

set -e

AWK=$(which awk)
SED=$(which sed)
PROGRAM="$0"
BASEDIR=$(dirname "$0")
POSTS_DIR="$BASEDIR/../_posts"

for program in AWK SED
do
	if [ -z "$${!program@}" ]
	then
		echo "Missing '$program' binary."
		exit 1
	fi
done

displayHelp()
{
	cat <<-EOT
	Usage: $PROGRAM <title>
	EOT
}

today=$(date "+%Y-%m-%d")
title=$@
title_slugfied=$(echo "$title" | $AWK '{print tolower($0)}' | sed 's/ /-/g')
post_file="${POSTS_DIR}/${today}-${title_slugfied}.md"

if [ -z "$title" ]
then
	echo "A title is needed."
	exit 1
fi

touch $post_file
cat <<-EOT > "${post_file}"
	---
	title: $title
	layout: post
	date: $today
	category:
	---

	Something inspiring here.

	<!--
	vim: spell spelllang=pt
	-->
EOT
echo $post_file
