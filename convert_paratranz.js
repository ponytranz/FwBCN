const fs = require('fs')

try {
  if (!fs.existsSync('tl/chinese/paratranz'))
    fs.mkdirSync('tl/chinese/paratranz')
  for (let file of fs.readdirSync('tl/chinese').filter(file => /\.rpy$/.test(file))) {
    let name = file.match(/^(.+)\.rpy$/)[1]
    let content = fs.readFileSync(`tl/chinese/${file}`, 'utf-8')
    let result = []
    /*
    match[1] : file and line number
    match[2] : text key
    match[3] : speaker original
    match[4] : text original
    match[5] : speaker translated
    match[6] : text translated
    */
    for (let match of content.matchAll(
      /(# game\/.+\.rpy:\d+)\s+translate chinese (.+):\s+# (.+ )?"(.+)"\s+(.+ )?"(.+)?"/g
    )) result.push({
      key: match[2],
      original: match[4],
      translation: match[6]
    })
    if (result.length)
      fs.writeFileSync(
        `tl/chinese/paratranz/${name}.json`,
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
        translation: match[5]
      })
    }
    if (result.length)
      fs.writeFileSync(
        `tl/chinese/paratranz/${name}_strings.json`,
        JSON.stringify(result, null, 2))
  }
} catch (error) {
  console.error(error)
}