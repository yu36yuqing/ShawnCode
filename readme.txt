function parse_git_dirty {
  [[ $(git status 2> /dev/null | tail -n1) != "nothing to commit (working directory clean)" ]] && echo "*"
}
function parse_git_branch {
  git branch --no-color 2> /dev/null | sed -e '/^[^*]/d' -e "s/* \(.*\)/[\1$(parse_git_dirty)]/"
}
PROMPT_COMMAND="find_git_branch; $PROMPT_COMMAND"
green=$'\e[1;32m'
magenta=$'\e[1;35m'
normal_colours=$'\e[m'

PS1="\[$green\]\u@\h:\w\[$magenta\]\$(parse_git_branch)\[$green\]\\$\[$normal_colours\]"
