const fs = require('fs')

try {
  for (let file of fs.readdirSync('game/tl/chinese').filter(file => /\.rpy$/.test(file))) {
    let name = file.match(/^(.+)\.rpy$/)[1]
    let result = `# Translation updated at ${new Date()}\n`
    if (fs.existsSync(`paratranz/${name}.json`)) {
      let dialogs = JSON.parse(fs.readFileSync(`paratranz/${name}.json`, 'utf-8'))
      for (let item of dialogs) {
        item.origin = item.context.match(/game\/.+$/)
        item.speaker = item.context.match(/说话人: (\S+)/)[1] + ' '
        if (item.speaker === '无 ')
          item.speaker = null
        result += `# ${item.origin}\ntranslate chinese ${item.key}:\n\n    # ${item.speaker ?? ''}"${item.original}"\n    ${item.speaker ?? ''}"${item.translation !== '' ? item.translation : item.original}"\n\n`
      }
      fs.writeFileSync(`game/tl/chinese/${file}`, result)
    }
    if (fs.existsSync(`paratranz/${name}_strings.json`)) {
      let strings = JSON.parse(fs.readFileSync(`paratranz/${name}_strings.json`, 'utf-8'))
      result += 'translate chinese strings:\n\n'
      for (let item of strings)
        result += `    # ${item.key}\n    old "${item.original}"\n    new "${item.translation !== '' ? item.translation : item.original}"\n\n`
      fs.writeFileSync(`game/tl/chinese/${file}`, result)
    }
  }
} catch (error) {
  console.error(error)
}
