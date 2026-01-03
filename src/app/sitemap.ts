import path from 'path'
import { promises as fs } from 'fs'

export const dynamic = 'force-static'

export default async function sitemap() {
  const baseUrl = 'https://g-ogaki.github.io/competitive-programming-python-library'

  const libraryPath = path.join(process.cwd(), 'library')
  const items = await fs.readdir(libraryPath)

  const documents = items.map((slug) => ({
    url: `${baseUrl}/${slug}`,
    lastModified: new Date(),
    changeFrequency: 'weekly' as const,
    priority: 0.8,
  }))

  return [
    {
      url: baseUrl,
      lastModified: new Date(),
      changeFrequency: 'weekly',
      priority: 1,
    },
    ...documents,
  ]
}
