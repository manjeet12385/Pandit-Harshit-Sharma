import { resolve } from 'path'
import { defineConfig } from 'vite'
import fs from 'fs'

const getInputs = () => {
  const inputs = {}
  
  // All root HTML files
  const rootFiles = fs.readdirSync(__dirname)
  for (const f of rootFiles) {
    if (f.endsWith('.html')) {
      const key = f.replace('.html', '').replace(/[^a-zA-Z0-9_]/g, '_')
      inputs[key] = resolve(__dirname, f)
    }
  }

  // All puja-in city HTML files
  const pujaDir = resolve(__dirname, 'puja-in')
  if (fs.existsSync(pujaDir)) {
    const files = fs.readdirSync(pujaDir)
    for (const f of files) {
      if (f.endsWith('.html')) {
        const key = 'puja_' + f.replace('.html', '').replace(/[^a-zA-Z0-9_]/g, '_')
        inputs[key] = resolve(pujaDir, f)
      }
    }
  }
  return inputs
}

export default defineConfig({
  build: {
    rollupOptions: {
      input: getInputs()
    }
  }
})
