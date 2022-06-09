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
export PATH=~/.local/bin:"$PATH"

alias status='git status & git fetch'
alias commit='git commit -a -m'
alias push='git push'
alias pull='git pull'
alias code='vscodium'
alias qconfig='vim ~/.config/qtile/config.py'
alias rec='cat ~/recordatorios'
alias recu='vim ~/recordatorios'
alias libros='ranger ~/Desktop/Libros'
alias vpnmit='sudo openvpn --config ~/client.ovpn'
alias gpumit='ssh josfemova@gpu.psfc.mit.edu'

alias get_idf='. $HOME/esp/esp-idf/export.sh'

powerline-daemon -q
. /usr/share/powerline/bindings/zsh/powerline.zsh


# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/josfemova/miniconda3/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/josfemova/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/home/josfemova/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/josfemova/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

