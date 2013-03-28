import sys

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("usage trim_hex_files.py <files_to_trim>")

	files = sys.argv[1:]
	for f in files:
		f_old = open(f, 'r')
		hex_lines = f_old.readlines()
		f_old.close()
		new_hex_lines = []
		for i in range(1000):
			hex_line_ind = int(i/1000.0*len(hex_lines))
			print(hex_line_ind)
			new_hex_lines.append(hex_lines[hex_line_ind])
		f_new = open(f, 'w')
		f_new.writelines(new_hex_lines)
		f_new.close()
