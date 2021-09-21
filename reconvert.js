const fs = require('fs')

try {
  // Paratranz 词条顺序只和创建时间相关，和上传文件里的顺序无关，也和字典序无关
  // 因此先排序再还原回 rpy
  let map = new Map()
  for (let file of fs.readdirSync('game/tl/chinese').filter(file => /\.rpy$/.test(file))) {
    let result = '', filename = file.match(/^(.+)\.rpy$/)[1]
    let content = fs.readFileSync(`game/tl/chinese/${file}`, 'utf-8')
    if (fs.existsSync(`paratranz/${filename}.json`)) {
      let speaker, sorted = []
      for (let item of JSON.parse(fs.readFileSync(`paratranz/${filename}.json`, 'utf-8').replace('\uFEFF', ''))) {
        speaker = item.context.match(/说话人: (\S+)/)[1] + ' '
        if (speaker === '无 ')
          speaker = ''
        item.str = `# ${item.context.match(/game\/.+$/)[0]}\ntranslate chinese ${item.key}:\n\n    # ${speaker}"${item.original}"\n    ${speaker}"${item.translation !== '' ? item.translation : item.original}"\n\n`
        map.set(item.key, item)
      }
      for (let match of content.matchAll(/translate chinese (.+_.+):/g)) {
        let dialog = map.get(match[1])
        result += dialog.str
        delete dialog.str
        sorted.push(dialog)
      }
      fs.writeFileSync(
        `paratranz/${filename}.json`,
        JSON.stringify(sorted, null, 2))
      if (!fs.existsSync(`paratranz/${filename}_strings.json`))
        fs.writeFileSync(`game/tl/chinese/${file}`, result)
      map.clear()
    }
    if (fs.existsSync(`paratranz/${filename}_strings.json`)) {
      result += 'translate chinese strings:\n\n'
      let sorted = []
      for (let item of JSON.parse(fs.readFileSync(`paratranz/${filename}_strings.json`, 'utf-8').replace('\uFEFF', ''))) {
        item.str = `    # ${item.key}\n    old "${item.original}"\n    new "${item.translation !== '' ? item.translation : item.original}"\n\n`
        map.set(item.key, item)
      }
      for (let match of content.matchAll(/# (.+\.rpym?_L\d+_\d+)/g)) {
        let dialog = map.get(match[1])
        result += dialog.str
        delete dialog.str
        sorted.push(map.get(match[1]))
      }
      fs.writeFileSync(
        `paratranz/${filename}_strings.json`,
        JSON.stringify(sorted, null, 2))
      fs.writeFileSync(`game/tl/chinese/${file}`, result)
      map.clear()
    }
  }
} catch (error) {
  console.error(error)
}
