const fs = require('fs')

try {
  for (let file of fs.readdirSync('game/tl/chinese').filter(file => /\.rpy$/.test(file))) {
    let name = file.match(/^(.+)\.rpy$/)[1]
    let content = fs.readFileSync(`game/tl/chinese/${file}`, 'utf-8')
    let result = []
    let map = new Map()
    if (fs.existsSync(`paratranz/${name}.json`)) {
      for (let item of JSON.parse(fs.readFileSync(`paratranz/${name}.json`, 'utf-8').substring(1)))
        map.set(item.key, item)
      for (let match of content.matchAll(/translate chinese (.+_.+):/g))
        result.push(map.get(match[1]))
      fs.writeFileSync(
        `paratranz/${name}.json`,
        JSON.stringify(result, null, 2))
    }
    result = []
    map.clear()
    if (fs.existsSync(`paratranz/${name}_strings.json`)) {
      for (let item of JSON.parse(fs.readFileSync(`paratranz/${name}_strings.json`, 'utf-8').substring(1)))
        map.set(item.key, item)
      for (let match of content.matchAll(/# (.+\.rpym?_L\d+_\d+)/g))
        result.push(map.get(match[1]))
      fs.writeFileSync(
        `paratranz/${name}_strings.json`,
        JSON.stringify(result, null, 2))
    }
    map.clear()
  }
} catch (error) {
  console.error(error)
}