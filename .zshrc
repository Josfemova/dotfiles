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

export RUST_COMPILER_RT_ROOT=$RUST_XTENSA/src/llvm-project/compiler-rt




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


#useful scripts
alias yt='~/UsefulScripts/yt'
alias suwupawmansuw='sudo pacman -Syu'
alias solve='~/REPOSITORIOS/solve/target/release/solve -i'
alias espelf="esptool.py elf2image"
alias flashesp="esptool.py write_flash"
alias espread="python ~/UsefulScripts/ttyUSB0Read.py"
alias gdb-arm="arm-none-eabi-gdb"

powerline-daemon -q
. /usr/share/powerline/bindings/zsh/powerline.zsh



