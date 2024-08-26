export PATH=$HOME/bin:$HOME/dev/scripts:/usr/local/bin:/usr/local/opt:$PATH

# Path to your oh-my-zsh installation.
export ZSH="$HOME/.oh-my-zsh"

# espressif idf and adf frameworks
export ESP_PATH=~/esp
export IDF_PATH=~/esp/esp-idf
export ADF_PATH=~/esp/esp-adf
export DSP_PATH=~/esp/esp-dsp

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
ZSH_THEME="robbyrussell"
#ZSH_THEME="af-magic"

#alias sub='/Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl'

# Set list of themes to pick from when loading at random
# Setting this variable when ZSH_THEME=random will cause zsh to load
# a theme from this variable instead of looking in $ZSH/themes/
# If set to an empty array, this variable will have no effect.
# ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion.
# Case-sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment one of the following lines to change the auto-update behavior
# zstyle ':omz:update' mode disabled  # disable automatic updates
# zstyle ':omz:update' mode auto      # update automatically without asking
# zstyle ':omz:update' mode reminder  # just remind me to update when it's time

# Uncomment the following line to change how often to auto-update (in days).
# zstyle ':omz:update' frequency 13

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS="true"

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# You can also set it to another string to have that shown instead of the default red dots.
# e.g. COMPLETION_WAITING_DOTS="%F{yellow}waiting...%f"
# Caution: this setting can cause issues with multiline prompts in zsh < 5.7.1 (see #5765)
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# You can set one of the optional three formats:
# "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# or set a custom format using the strftime function format specifications,
# see 'man strftime' for details.
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load?
# Standard plugins can be found in $ZSH/plugins/
# Custom plugins may be added to $ZSH_CUSTOM/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(git)

source $ZSH/oh-my-zsh.sh

# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='mvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.


# to produce the highest quality text-to-spech mp3 audio files, use elevenlabs.io 
# https://elevenlabs.io/
# best voice: Paul, Grace. 
# best settings: Default, Elevel Multilingual v1

# this function calls 'ffmpeg' to convert an mp3 audio file to an mp4 video file (suitable for upload to youtube)
# ffmpeg also adds a static image file to the video (Title.jpg)
# usage:    convert_mp3_to_mp4  my-audio       (input: my-audio.mp3 -> output: my-audio.mp4)
convert_mp3_to_mp4() {
    local base_name="$1"
    local input_audio="${base_name}.m4a"
    # local input_audio="${base_name}.mp3"
    local output_video="${base_name}.mp4"
    local image_path="Title.jpg" # Ensure this path is correct
    # local image_path="${Title}.jpg"

    # Diagnostic messages to confirm file names
    echo "Input audio file: $input_audio"
    echo "Output video file: $output_video"

    # Check if the input audio file exists
    if [[ ! -f "$input_audio" ]]; then
        echo "Error: Input audio file does not exist."
        return 1
    fi

    # Run ffmpeg command
    ffmpeg -loop 1 -framerate 1 -i "$image_path" -i "$input_audio" -c:v libx264 -preset ultrafast -tune stillimage -c:a aac -b:a 192k -shortest -movflags +faststart "$output_video"

}

# ================================= aliases ============================
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"

# Aaron Adapy.com

alias adapy='cd ~/dev/esp32_dev/Aaron_Adapy'
alias aaron='cd ~/dev/esp32_dev/Aaron_Adapy'


# gnu radio companion for hackrf development (note: osomocom Source, set GRC Device Arguments to "hackrf")
function grc() {
# source /Users/phil/radioconda/bin/activate  # commented out by conda initialize
    # nohup gnuradio-companion > /dev/null 2>&1 &
    nohup gnuradio-companion > /Users/phil/logs/gnuradio-companion.log 2>&1 &
}

# alias grc='conda activate base && gnuradio-companion'
alias hackrf='grc'
alias sdr='grc'

# cd to directory containing GRC project files
alias gnu='cd ~/dev/Electronics/GNU_Radio_GRC'

# alias gnuradio='nohup gnuradio-companion > /dev/null 2>&1 &'

# open the GPT4 (chatgpt) local app
alias chat='cd ~/dev/scripts && ./chatgpt.sh'
alias gpt='cd ~/dev/scripts && ./chatgpt.sh'

# launches the NanoVNASaver GUI application from the terminal (runs in a python virtual environment)
alias vna='source ~/dev/Electronics/nanovna/bin/activate && NanoVNASaver'
alias nano='source ~/dev/Electronics/nanovna/bin/activate && NanoVNASaver'

# launches the TinySA Ultra spectrum analyzer app from the terminal (runs in a python virtual environment)
alias tiny='source ~/dev/Electronics/tinysa/bin/activate && cd /Users/phil/dev/Electronics/tinysa/QtTinySA && ./QtTinySA.py'
alias tinysa='source ~/dev/Electronics/tinysa/bin/activate && cd /Users/phil/dev/Electronics/tinysa/QtTinySA && ./QtTinySA.py'

alias dbmtowatts='cd ~/dev/scripts && ./dbm_to_watts'
alias wattstodbm='cd ~/dev/scripts && ./watts_to_dbm'
alias freqwave='cd ~/dev/scripts && ./freq_wavelength'
alias ham='cd ~/dev/Electronics/AARL_ham_radio_amateur'

# NSA decompiler tool called Ghidra (able to convert .hex and .asm files to c source files)
alias ghidra='~/dev/Decompler/ghidra_11.1_DEV/ghidrarun'
alias decompile='~/dev/Decompler/ghidra_11.1_DEV/ghidrarun'
alias decompiler='~/dev/Decompler/ghidra_11.1_DEV/ghidrarun'

# list esp-idf releases available on github
alias lsidf='curl "https://api.github.com/repos/espressif/esp-idf/releases" | jq -r ".[].tag_name" | sort'
alias bt='cd ~/dev/esp32_dev/BluetoothDiscovery && idfsh'
alias btsource='cd ~/esp/esp-idf/examples/bluetooth/bluedroid/classic_bt/a2dp_source'
alias btsink='cd ~/esp/esp-idf/examples/bluetooth/bluedroid/classic_bt/a2dp_sink'
alias bthfp='cd ~/esp/esp-idf/examples/bluetooth/bluedroid/classic_bt/hfp_ag'
alias format='clang-format'
alias search='python3 /Users/phil/dev/scripts/search.py'
alias fsearch='python3 /Users/phil/dev/scripts/fsearch.py'
alias prifix='python3 /Users/phil/dev/scripts/esptypefix.py'
alias react='cd ~/dev/react_native'
alias profile='cd ~ && sub .bash_profile'
# this alias lists all the account usernames
alias users='dscl . list /Users | grep -v “^_”'
# list users alias
alias lu='dscl . list /Users | grep -v “^_”'
# alias to get the MAC Address of connected bluetooth devices
alias blue='blueutil --connected'
# alias to get the MAC Address of all previously paired/connected bluetooth devices
alias blueall='blueutil --paired'
alias target_esp32='idf.py set-target esp32'
alias target_esp32s3='idf.py set-target esp32s3'
alias esp='cd $HOME/dev/esp32_dev'
alias idf='cd $HOME/esp/esp-idf'
alias adf='cd $HOME/esp/esp-adf'
alias espressif='cd ~/.espressif'
alias learn='cd ~/dev/ESP32_IDF_Projects/examples'
alias ard='cd $HOME/Documents/Arduino'
alias ardlist='arduino-cli board listall'	#list all the arduino "fully qualified board names" (FQBN)
alias ardupload='arduino-cli upload ~/Documents/Arduino/ESP32_Internet_Radio/ESP32_Internet_Radio.ino -b esp32:esp32:uPesy_wroom -p /dev/tty.usbserial-0001'
alias platform='cd $HOME/Documents/PlatformIO/Projects'
alias idfsh='. ~/esp/esp-idf/export.sh'		#sets up path variable for IDF development (IDF_PATH, IDF build tools, PYTHONPATH)
alias idfcp='idf.py create-project -p . $1'
alias idftarget='idf.py set-target esp32'
alias idfcpfx='idf.py create-project-from-example'
alias idft='idf.py set-target esp32'
alias idfcb='idf.py fullclean build'
alias idfbfm='idf.py fullclean build flash monitor'
alias cb='idf.py fullclean build'
alias fm='idf.py -p /dev/tty.usbserial-0001 flash monitor'
alias m1='idf.py -p /dev/tty.usbserial-0001 monitor'
alias idfb='idf.py build'
alias idff='idf.py -p /dev/tty.usbserial-0001 flash'
alias idffm='idf.py -p /dev/tty.usbserial-0001 flash monitor'
alias f1='idf.py -p /dev/tty.usbserial-0001 flash'
alias m1='idf.py -p /dev/tty.usbserial-0001 monitor'
alias f2='idf.py -p /dev/tty.usbserial-2 flash'
alias m2='idf.py -p /dev/tty.usbserial-2 monitor'
alias s3='idf.py -p /dev/tty.usbmodem14101 -b 115200 set-target esp32s3 flash monitor'
alias idfm='idf.py -p /dev/tty.usbserial-0001 monitor'
alias idfc='idf.py fullclean'
alias idfv='idf.py --version'
alias idfh='idf.py --help'
alias idfhelp='idf.py --help'
alias idfmenu='idf.py menuconfig'
alias idfconfig='idf.py menuconfig'
alias idferase='idf.py -p /dev/cu.usbserial-0001 erase-flash'
alias z='sub ~/.zshrc'
#reset ESP32 to factory defaults
#alias idfreset = 'esptool.py --chip esp32 --port /dev/tty.usbserial-0001 erase_flash'
#alias idfupdate='cd ~/esp && rm -rf esp-idf && git clone --recursive https://github.com/espressif/esp-idf.git'
alias idfupdate='cd ~/esp/esp-idf && git pull && ./install.sh'
alias idftargets='idf.py --list-targets'
alias idfdebug='source ~/esp/esp-idf/export.sh && idf.py build && idf.py openocd gdb monitor'
alias idfdb='source ~/esp/esp-idf/export.sh && idf.py build && idf.py openocd gdb monitor'
#alias idfdebug='source ~/esp/esp-idf/export.sh && idf.py build && idf.py openocd gdbgui monitor' #gdbgui requires python 3.10 or older
alias idfchip='esptool.py --port /dev/tty.usbserial-0001 chip_id'
alias idfid='esptool.py --port /dev/tty.usbserial-0001 flash_id'

alias red='node-red'
alias project='cd ~/dev/esp32_dev/TheIntercom && idfsh'
alias glib_path=/Users/phil/dev/lib_global/c_cpp
alias mqtt='/usr/local/sbin/mosquitto -c /usr/local/etc/mosquitto/mosquitto.conf'
alias broker='/usr/local/sbin/mosquitto -c /usr/local/etc/mosquitto/mosquitto.conf'
# alias lsusb='system_profiler SPUSBDataType'
alias lsusb='ls /dev/tty* | grep usb'
alias lausb='ls -la /dev/{tty,cu}.*'
alias shell='ps -p $$'
alias lsh='cat /etc/shells'
alias chzsh='chsh -s /bin/zsh'
alias chbash='chsh -s /bin/bash'
alias open='open .' # the macos console command to open to the desktop' 
alias wave='play -n synth 3 sine'
alias golist='go list ./...' 
alias gohome='cd ~/dev/go'
alias gosrc='cd ~/dev/go/src'
alias gobin='cd ~/dev/go/bin'
alias golib='cd ~/dev/go/lib'
alias gopkg='cd ~/dev/go/pkg'
alias gomod='cd ~/dev/go/pkg/mod'
alias gosumdb='cd ~/dev/go/pkg/sumdb'
alias goplay='cd ~/dev/go/src/goplay'
alias goclass='cd ~/dev/go/src/udemy/go-course'
alias udemy='cd ~/dev/go/src/udemy/go-course'
alias restartkafka='brew services restart kafka'
alias startkafka='/usr/local/opt/kafka/bin/kafka-server-start /usr/local/etc/kafka/server.properties'
alias startzookeeper='/usr/local/Cellar/kafka/3.0.0/libexec/bin/zookeeper-server-start.sh'
alias uav='cd /Users/phil/dev/uav'
alias memory='cat /proc/meminfo'
alias cpu='grep -c ^processor /proc/cpuinfo'
alias mfg="cat /proc/cpuinfo | grep 'model name' | uniq"
alias elastic='cd ~/dev/elasticsearch-2.4.0/bin && ./elasticsearch'
alias ports='sudo lsof -nP -i | grep LISTEN'
alias sub='/Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl'
alias te='open -a TextEdit '
alias macdown='/Applications/MacDown.app'
alias newec2='ssh -i ~/.ssh/log-pipeline-ecs-server-key-pair.pem ubuntu@35.162.218.33'
alias ec2='ssh -i ~/.ssh/log-pipeline-ecs-server-key-pair.pem ubuntu@ec2-52-42-169-172.us-west-2.compute.amazonaws.com'
alias listeners='sudo lsof -i -P | grep -i "listen"'
alias size='du -sh *'
alias ytdl='youtube-dl -f bestvideo[ext=mp4]+bestaudio[ext=m4a]'
alias videos='cd ~/Videos'
alias setup='cd ~/dev/shell_scripts && ./setup_iterm.sh'
alias scripts='cd ~/dev/scripts'
alias oldvm='cd /Users/phil/dev/virtual_machines/ubuntu1404 && ./up.sh && ./ssh.sh'
alias oldvmdir='cd /Users/phil/dev/virtual_machines/ubuntu1404'
alias dev='cd /Users/phil/dev'
# echo "alias python=/usr/bin/python3" >> ~/.zshrc
#alias python=python3
# alias python='/Users/phil/.espressif/python_env/idf5.1_py3.10_env/bin/python >> ~/.zshrc'
alias python='/usr/local/bin/python3'
alias py='python3'
alias py2='python2'
alias py3='python3'
alias pip='/usr/local/bin/pip3'
alias pip2='/usr/local/bin/pip'
alias pip3='/usr/local/bin/pip3'
PIP_BREAK_SYSTEM_PACKAGES=1
alias pippackages='cd /usr/local/lib/python3.11/site-packages'
alias gs='git status'
alias ga='git add -A'
alias gp='git push'
alias gd='git diff'
alias gl='git log --graph --decorate'
alias awsphil='cd /Users/phil/dev/shell_scripts && ./to_phil_aws.sh && cd ~/.aws'
alias awszip='cd /Users/phil/dev/shell_scripts && ./to_zipline_aws.sh && cd ~/.aws'
alias pg-start='brew services start postgresql@14'
alias pg-stop='brew services stop postgresql@14'
alias pg-restart='brew services restart postgresql@14'
alias pg-status='pg_ctl -D /usr/local/var/postgres status'
# alias connectdb='psql postgres'
alias connectdb='psql adsb'
alias startdb='/usr/local/opt/postgresql/bin/postgres -D /usr/local/var/postgres'
#alias startdb='docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=postgres -d postgres'
#alias stopdb='docker stop postgres && docker rm postgres'
#alias connectdb='docker run -it --rm --link postgres:postgres postgres psql -h postgres -U postgres'
alias startpg='pg_ctl -D /usr/local/var/postgres start'
alias stoppg='pg_ctl -D /usr/local/var/postgres stop'
#alias connectpg='psql -h 127.0.0.1 -p 5432 -U phil'
alias dockerkill='docker rm -f $(docker ps -aq)'
####### FLIGHTAWARE DUMP1090 (note: requires a separate web server for http. SEE 'webserver' alias below.) #######
alias dump='adsb'
alias adsbserver='cd /Users/phil/dev/adsb/flightaware/dump1090/public_html && python3 -m http.server 8080'
alias show='nc localhost 30003'
alias dump2='adsb2'
alias lint='golangci-lint'
alias reload='source ~/.zshrc'
alias f='find . -name'	# search for files by name
alias s='grep -r'		# search for text within files 
alias cd..='cd ..'
alias ..='cd ..'
alias ...='cd ../../../'
alias ....='cd ../../../../'
alias .....='cd ../../../../'
alias .2='cd ../..'
alias .3='cd ../../..'
alias .4='cd ../../../..'
alias .5='cd ../../../../..'
alias l.='ls -ld .* --color=auto' #list hidden files and directories
alias lx="ls -la | egrep '^-' | egrep '^.{3,9}x'" #list executable files
alias ll='ls -lG' # long list 
alias la='ls -laG' # long list all
alias lf="ls -l | egrep '^-'" #list files only
alias ld="ls -l | egrep '^d'" #list directories only
alias lss='ls -laShG' # list all sorted by file size in human readable format
alias lS='ls -laShG' # list all sorted by file size in human readable format
alias c='clear'
alias cls='clear'

alias connectdb='psql adsb'
alias adsb='echo "--flightaware dump1090--" && sleep 2 && cd /Users/phil/dev/adsb/flightaware/dump1090 && ./dump1090
alias adsbraw='cd /Users/phil/dev/adsb/flightaware/dump1090 && ./dump1090 --raw' ##produces hex output
alias dump='adsb'
alias adsbserver='cd /Users/phil/dev/adsb/flightaware/dump1090/public_html && python3 -m http.server 8080'
alias adsb2='echo "--antirez dump1090--" && sleep 2 && cd /Users/phil/dev/adsb/antirez/dump1090 && ./dump1090 --interactive --net
alias dump2='adsb2'
alias adsbrecord='cd /usr/local/bin && ./rtl_sdr -f 1090000000 -s 2000000 -g 50
alias adsbplayback='cd /Users/phil/dev/adsb/antirez/dump1090 && ./dump1090 --interactive --net --loop --ifile

# commands to setup a python virtual environment and install dependencies (isolates python dependencies from other python dependencies)
# python3 -m venv dirname               (this will create the directory and setup the virtual environment)
# source dirname/bin/activate           (this activates the virtual environment)
# python3 -m pip install xyz            (command to install packages, etc)
# deactivate                            (command to deactivate the virtual environment)

# tabtab source for electron-forge package
# uninstall by removing these lines or running `tabtab uninstall electron-forge`
#[[ -f /Users/phil/dev/macgpt/node_modules/tabtab/.completions/electron-forge.zsh ]] && . /Users/phil/dev/macgpt/node_modules/tabtab/.completions/electron-forge.zsh


function stop_conda() {
    conda deactivate
}
function start_conda() {
    conda activate
}

# function start_conda() {
#     # >>> conda initialize >>>
#     # !! Contents within this block are managed by 'conda init' !!
#     __conda_setup="$('/Users/phil/radioconda/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
#     if [ $? -eq 0 ]; then
#         eval "$__conda_setup"
#     else
#         if [ -f "/Users/phil/radioconda/etc/profile.d/conda.sh" ]; then
#             . "/Users/phil/radioconda/etc/profile.d/conda.sh"
#         else
#             export PATH="/Users/phil/radioconda/bin:$PATH"
#         fi
#     fi
#     unset __conda_setup

#     if [ -f "/Users/phil/radioconda/etc/profile.d/mamba.sh" ]; then
#         . "/Users/phil/radioconda/etc/profile.d/mamba.sh"
#     fi
#     # <<< conda initialize <<<
# }


export PATH="$PATH:/Applications/microchip/xc8/v2.46/bin:/Users/phil/.local/bin"

# path to the Ghidra decompiler (NSA) 
export GHIDRA_HOME=" ~/dev/Decompler/ghidra"



