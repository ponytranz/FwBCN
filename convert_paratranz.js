const fs = require('fs')

try {
  if (!fs.existsSync('game/tl/chinese/paratranz'))
    fs.mkdirSync('game/tl/chinese/paratranz')
  for (let file of fs.readdirSync('game/tl/chinese').filter(file => /\.rpy$/.test(file))) {
    let name = file.match(/^(.+)\.rpy$/)[1]
    let content = fs.readFileSync(`game/tl/chinese/${file}`, 'utf-8')
    let result = []
    /*
    match[1] : file
    match[2] : line number
    match[3] : text key
    match[4] : speaker original
    match[5] : text original
    match[6] : speaker translated
    match[7] : text translated
    */
    for (let match of content.matchAll(
      /# (game\/.+\.rpy):(\d+)\s+translate chinese (.+):\s+# (.+ )?"(.+)"\s+(.+ )?"(.+)?"/g
    )) result.push({
      key: match[3],
      original: match[5],
      translation: match[7],
      context: `https://github.com/ponytranz/FwBCN/blob/main/${match[1]}#L${match[2]}`
    })
    if (result.length)
      fs.writeFileSync(
        `game/tl/chinese/paratranz/${name}.json`,
        JSON.stringify(result, null, 2))
    result = []
    /*
    match[1] : file and line number
    match[2] : file
    match[3] : line number
    match[4] : text original
    match[5] : text translated
    */
    let last = '', cnt
    for (let match of content.matchAll(
      /# ((.+):(\d+))\s+old "(.+)"\s+new "(.+)?"/g
    )) {
      if (match[1] !== last) {
        last = match[1]
        cnt = 0
      }
      result.push({
        key: `${match[2]}_L${match[3]}_${cnt++}`,
        original: match[4],
        translation: match[5],
        context: `https://github.com/ponytranz/FwBCN/blob/main/${match[2]}#L${match[3]}`
      })
    }
    if (result.length)
      fs.writeFileSync(
        `game/tl/chinese/paratranz/${name}_strings.json`,
        JSON.stringify(result, null, 2))
  }
} catch (error) {
  console.error(error)
}