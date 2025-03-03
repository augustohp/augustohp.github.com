#!/usr/bin/env bash
# vim: noet ts=4 sw=4 ft=sh:

set -e

PROGRAM="$0"
BASEDIR=$(dirname "$0")
POSTS_DIR="$BASEDIR/../_posts"

if [ -n "$DEBUG" ]
then 
	set -x
fi


displayHelp()
{
	cat <<-EOT
	Usage: $PROGRAM <title>
	EOT
}

assert_environment()
{
	 for program in awk
	 do
		  if [ -z "$(command -v $program)" ]
		  then
			   echo "Error: Missing '$program'!"
			   exit 1
		  fi
	  done
  }

# Usage: echo "this is a title" | slugify
slugify()
{
	awk '{
		gsub(/[^a-zA-Z0-9\-\s]/, "-")
		$0 = tolower($0)
		print
	}'
}

# Usage: create_post_file "This is a great post title"
create_post_file()
{
	post_title="$1"

	title_slugfied="$(echo "${post_title}" | slugify)"
	today="$(date '+%Y-%m-%d')"
	post_file="${POSTS_DIR}/${today}-${title_slugfied}.md"
	touch $post_file

	cat <<-EOT > "${post_file}"
	---
	title: $post_title
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
 }

 main()
 {
	 post_title="$@"

	 assert_environment
	 if [ -z "$post_title" ]
	 then
		 read -p "Title of the post: " post_title
	 fi
	 if [ -z "$post_title" ]
	 then
		 echo "Error: A title is needed!"
		 exit 1
	 fi

	 create_post_file "${post_title}"
 }

 main "$@"
