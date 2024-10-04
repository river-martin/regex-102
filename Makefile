engines:
	make -C engines/java8-runner
	make -C engines/pcre2-runner
	make -C engines/bru
	cmake engines/re2-runner
	cmake --build engines/re2-runner

clean:
	make -C engines/java8-runner clean
	make -C engines/pcre2-runner clean
	make -C engines/bru clean
	make -C engines/re2-runner clean

.PHONY: engines clean