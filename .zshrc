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
#export RUSTC=$RUST_XTENSA/build/x86_64-unknown-linux-gnu/stage2/bin/rustc
#export RUSTDOC=$RUST_XTENSA/build/x86_64-unknown-linux-gnu/stage2/bin/rustdoc
#export XARGO_RUST_SRC=$RUST_XTENSA/library

#export RUST_COMPILER_RT_ROOT=$RUST_XTENSA/src/llvm-project/compiler-rt
export PATH=~/.local/bin:"$PATH"

export PATH=/opt/android-sdk:"$PATH"
export ANDROID_SDK_ROOT=/opt/android-sdk

export ZEPHYR_TOOLCHAIN_VARIANT="espressif"
export ESPRESSIF_TOOLCHAIN_PATH="${HOME}/.espressif/tools/zephyr"
export PATH=/home/josfemova/.espressif/tools/xtensa-esp32-elf/esp-2021r2-8.4.0/xtensa-esp32-elf/bin:"$PATH"
export PATH=/home/josfemova/.espressif/tools/xtensa-lx106-elf/bin:"$PATH$"
export PICO_SDK_PATH=/usr/share/pico-sdk

alias status='git status & git fetch'
alias commit='git commit -a -m'
alias push='git push'
alias pull='git pull'
alias code='vscodium'
alias qconfig='vim ~/.config/qtile/config.py'
alias solvedir='cd ~/Desktop/Electro/activos/octave'
alias rec='cat ~/recordatorios'
alias recu='vim ~/recordatorios'
alias libros='ranger ~/Desktop/Libros'
alias vpnmit='sudo openvpn --config ~/client.ovpn'
alias gpumit='ssh josfemova@gpu.psfc.mit.edu'

#useful scripts
alias yt='~/UsefulScripts/yt'
alias xtensatime='source ~/UsefulScripts/xtensatime.sh'
alias suwupawmansuw='sudo pacman -Syu'
alias solve='~/REPOSITORIOS/solve/target/release/solve -i'
alias gdb-arm="arm-none-eabi-gdb"

export ESP_IDF=/opt/esp-idf
export ESPIDF=/opt/esp-idf

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

