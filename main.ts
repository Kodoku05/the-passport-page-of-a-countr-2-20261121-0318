// The offline artwork is committed so the sandbox needs no graphics packages.
import { mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const source = join(dirname(fileURLToPath(import.meta.url)), 'entry.png');
const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const target = join(outputDir, 'entry.png');

try {
  const artwork = readFileSync(source);
  if (!artwork.subarray(0, 8).equals(Buffer.from([137,80,78,71,13,10,26,10]))) {
    throw new Error('Committed artwork has an invalid PNG signature');
  }
  if (artwork.length > 1_048_576 || artwork.length < 33) {
    throw new Error('Committed artwork has an invalid file size');
  }
  if (artwork.readUInt32BE(16) !== 1024 || artwork.readUInt32BE(20) !== 1024) {
    throw new Error('Committed artwork must be exactly 1024 by 1024');
  }
  mkdirSync(outputDir, { recursive: true });
  writeFileSync(target, artwork);
  const written = readFileSync(target);
  if (!written.equals(artwork)) throw new Error('Output differs from committed artwork');
} catch (error) {
  console.error('Kalverra passport:', error instanceof Error ? error.message : error);
  process.exit(1);
}
