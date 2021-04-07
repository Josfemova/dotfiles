# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
bindkey -v
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/home/jose/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall
export EDITOR=vim
export PAGER=less
export RANGER_LOAD_DEFAULT_RC=FALSE
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

alias status='git fetch & git status'
alias commit='git commit -m'
alias push='git push'
alias pull='git pull'
alias code='vscodium'
alias qconfig='vim ~/.config/qtile/config.py'

