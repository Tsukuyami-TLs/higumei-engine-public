cd game
assets=$(grep "'\(audio\|images\)[^']\+'" -ro scripts --include='*.rpy' | cut -d':' -f2 | sed "s/'//g" | sort | uniq)
git add -f $assets

