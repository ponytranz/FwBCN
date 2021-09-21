const fs = require('fs')

try {
  // convert
  if (!fs.existsSync('paratranz'))
    fs.mkdirSync('paratranz')
  if (!fs.existsSync('generated'))
    fs.mkdirSync('generated')
  let result
  for (let file of fs.readdirSync('game/tl/chinese').filter(file => /\.rpy$/.test(file))) {
    let filename = file.match(/^(.+)\.rpy$/)[1]
    let content = fs.readFileSync(`game/tl/chinese/${file}`, 'utf-8')
    // game/tl/chinese/ 作为 main 分支的基底，以及 sort.js 的排序依据
    // generated/ 用来避免每次都要用 RenPy 重新生成翻译基底
    if (/# TODO: Translation updated at/.test(content))
      fs.renameSync(`game/tl/chinese/${file}`, `generated/${file}`)
    else
      content = fs.readFileSync(`generated/${file}`, 'utf-8')
    /*
    match[1] : file
    match[2] : line number
    match[3] : text key
    match[4] : speaker original
    match[5] : text original
    match[6] : speaker translated
    match[7] : text translated
    */
    result = []
    for (let match of content.matchAll(
      /# (game\/.+\.rpym?):(\d+)\s+translate chinese (.+):\s+# (.+ )?"(.+)"\s+(.+ )?"(.+)?"/g
    )) result.push({
      key: match[3],
      original: match[5],
      context: `说话人: ${match[4] ?? '无 '}\n代码: ${/^renpy\/common/.test(match[1])
        ? `https://github.com/renpy/renpy/blob/master/${match[1].replace(/ /g, '%20')}`
        : `https://github.com/ponytranz/FwBCN/blob/empty/${match[1].replace(/ /g, '%20')}`
        }#L${match[2]}`
    })
    if (result.length)
      fs.writeFileSync(
        `paratranz/${filename}.json`,
        JSON.stringify(result, null, 2))
    /*
    match[1] : file and line number
    match[2] : file
    match[3] : line number
    match[4] : text original
    match[5] : text translated
    */
    let last = '', cnt
    result = []
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
        context: `代码: ${/^renpy\/common/.test(match[2])
          ? `https://github.com/renpy/renpy/blob/master/${match[2].replace(/ /g, '%20')}`
          : `https://github.com/ponytranz/FwBCN/blob/empty/${match[2].replace(/ /g, '%20')}`
          }#L${match[3]}`
      })
    }
    if (result.length)
      fs.writeFileSync(
        `paratranz/${filename}_strings.json`,
        JSON.stringify(result, null, 2))
  }
  // reconvert
  for (let file of fs.readdirSync('generated').filter(file => /\.rpy$/.test(file))) {
    let filename = file.match(/^(.+)\.rpy$/)[1]
    result = ''
    if (fs.existsSync(`paratranz/${filename}.json`)) {
      let dialogs = JSON.parse(fs.readFileSync(`paratranz/${filename}.json`, 'utf-8'))
      for (let item of dialogs) {
        item.origin = item.context.match(/game\/.+$/)
        item.speaker = item.context.match(/说话人: (\S+)/)[1] + ' '
        if (item.speaker === '无 ')
          item.speaker = null
        result += `# ${item.origin}\ntranslate chinese ${item.key}:\n\n    # ${item.speaker ?? ''}"${item.original}"\n    ${item.speaker ?? ''}"${item.translation ?? ''}"\n\n`
      }
    }
    if (fs.existsSync(`paratranz/${filename}_strings.json`)) {
      let strings = JSON.parse(fs.readFileSync(`paratranz/${filename}_strings.json`, 'utf-8'))
      result += 'translate chinese strings:\n\n'
      for (let item of strings)
        result += `    # ${item.key}\n    old "${item.original}"\n    new "${item.translation ?? ''}"\n\n`
    }
    fs.writeFileSync(`game/tl/chinese/${file}`, result)
  }
} catch (error) {
  console.error(error)
}