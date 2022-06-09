set cc=80
set nocompatible
set shortmess+=I
set number
set relativenumber
set laststatus=2
set hidden
set ignorecase
set smartcase
set incsearch
nmap Q <Nop>
set mouse+=a
set tabstop=4
set shiftwidth=4
set autoindent
set expandtab
"set smartindent 
set clipboard=unnamedplus
set encoding=utf-8
set langmenu=es_ES.UTF-8
syntax on
filetype plugin indent on

set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*

let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0
let g:rustfmt_autosave = 1
