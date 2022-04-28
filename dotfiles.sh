#!/bin/bash
ln -sf ~/Dotfiles/.bashrc ~/.bashrc
ln -sf ~/Dotfiles/.xprofile ~/.xprofile

#Inside .config
ln -sf ~/Dotfiles/.config/alacritty ~/.config/alacritty
rm -rf ~/.config/alacritty/alacritty
ln -sf ~/Dotfiles/.config/picom ~/.config/picom
rm -rf ~/.config/picom/picom
ln -sf ~/Dotfiles/.config/qtile ~/.config/qtile
rm -rf ~/.config/qtile/qtile
ln -sf ~/Dotfiles/.config/rofi ~/.config/rofi
rm -rf ~/.config/rofi/rofi
ln -sf ~/Dotfiles/.config/Thunar ~/.config/Thunar
rm -rf ~/.config/Thunar/Thunar
ln -sf ~/Dotfiles/.config/nvim ~/.config/nvim
rm -rf ~/.config/nvim/nvim
