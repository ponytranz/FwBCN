const fs = require('fs')
try {
  let regex = /(# game\/.+\.rpy:\d+)\s+translate chinese (.+):\s+# (.+ )?"(.+)"\s+(.+ )?"(.+)?"/g
  for (let file of fs.readdirSync('tl/chinese').filter(file => /\.rpy$/.test(file))) {
    console.log(`${file}:`)
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
    for (let match of content.matchAll(regex))
      result.push({
        key: match[2],
        original: match[4],
        translation: match[6]
      })
    if (!fs.existsSync('tl/chinese/paratranz'))
      fs.mkdirSync('tl/chinese/paratranz')
    if (result.length)
      fs.writeFileSync(
        `tl/chinese/paratranz/${file.match(/^(.+)\.rpy$/)[1]}.json`,
        JSON.stringify(result, null, 2))
  }
} catch (error) {
  console.error(error)
}