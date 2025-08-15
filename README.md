# First steps

I recently got hold of a Tuya-alike smart camera — one of those cheap IP cams running on Anyka silicon. I tried [guino's LSCOutdoor1080P project](https://github.com/guino/LSCOutdoor1080P), but it didn't behave properly (camera version was too new). Telnet access works fine though, so I started digging.
## Poking at the interface

- Firstly, I have tried running `nc localhost 8012`, but the camera just rebooted.
- Later, I have sent hex codes like 0x`00 00 00 00`, which yielded a response.
- After running [a script](snippets/scan.py), only the first 16 codes did something, so the version provided only queries them.
- Each and every one of the 16 codes seem to have a header attached, which contains:
	1. The 4-byte opcode given
	2. Some sort of 4-byte response opcode (eg. for 0x0A, it is 0x`2C 01 00 00`)
	3. 4-byte response length
	- Then, the actual payload is provided
# Things to note:
1. Opcode 0x0A returned:
{header} libplat_ai \[version\] libplat_ao \[version\] libmpi_aenc \[version\] libmpi_adec \[version\] AudioFilter Version \[version\] AudioCodec Version \[version\]
2. Opcode 0x05 returned:
{header} audio tool heartbeat!
3. Codes like `DA 00 00 00 01 00 00 00` return the same things as `01 00 00 00`. The `DA` here doesn't seem to be anything noteworthy - just an arbitrary number. Codes `10 - FF` seem to serve the same function.

## Why is this so short?
Well, I haven't done so much about this. To be honest, I was also talking with Copilot about it, which has helped a lot. This repo is just a scratchpad for now — expect messy notes, half-working scripts, and weird behavior.

### Am I at MIT?
Nope. The MIT license is just permissive. If you’re reading this and wondering — people outside MIT use it too. Wild, I know.
