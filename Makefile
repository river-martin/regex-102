engines:
	make -C engines/java8-runner
	make -C engines/pcre2-runner
	make -C engines/bru

clean:
	make -C engines/java8-runner clean
	make -C engines/pcre2-runner clean
	make -C engines/bru clean

.PHONY: engines clean