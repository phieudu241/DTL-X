import re
import sys

regex = [
	[
		r'(# direct methods\n.method public static )appkiller\(\)V([\s\S]*?.end method)[\w\W]*',
		r'\1constructor <clinit>()V\2',
	],
	[
		r'.*invoke.*pairip.*\)Z.*',
		r'invoke-static {}, Lsec/blackhole/dtlx/Schadenfreude;->neutralize()Z'
	]
]

def replace_content(input_path):
	with open(input_path, 'r', encoding='utf-8') as f:
		content = f.read()

	for pattern, replacement in regex:
		content = re.sub(pattern, replacement, content)

	output_path = input_path + '.output'
	with open(output_path, 'w', encoding='utf-8') as f:
		f.write(content)

	print(f'Output written to: {output_path}')


if __name__ == '__main__':
	print(sys.argv)
	if len(sys.argv) < 2:
		print('Usage: python test.py <input_file>')
		sys.exit(1)
	replace_content(sys.argv[1])

# Example usage:
# python test.py input.smali